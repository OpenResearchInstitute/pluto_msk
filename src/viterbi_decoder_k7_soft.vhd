------------------------------------------------------------------------------------------------------
-- Soft Decision Viterbi Decoder - K=7, Rate 1/2
------------------------------------------------------------------------------------------------------
-- Accepts quantized soft decisions instead of hard bits for ~2 dB coding gain.
--
-- SOFT_WIDTH generic controls quantization:
--   3-bit: 8 levels, ~1.5-2 dB gain, minimal resources
--   4-bit: 16 levels, ~2 dB gain
--   8-bit: 256 levels, ~2.5 dB gain (full soft)
--
-- Soft value convention (signed, two's complement interpretation):
--   Most negative = highest confidence '0'
--   Most positive = highest confidence '1'
--   Zero = erasure/no information
--
-- For 3-bit unsigned (current default):
--   0 = strong '0', 7 = strong '1', 3-4 = uncertain
------------------------------------------------------------------------------------------------------

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.numeric_std.ALL;

ENTITY viterbi_decoder_k7_soft IS
    GENERIC (
        PAYLOAD_BITS     : NATURAL := 134*8;   -- 1072 decoded bits
        ENCODED_BITS     : NATURAL := 268*8;   -- 2144 encoded bits
        TRACEBACK_DEPTH  : NATURAL := 35;
        SOFT_WIDTH       : NATURAL := 3        -- Bits per soft symbol (3, 4, or 8)
    );
    PORT (
        clk              : IN  std_logic;
        aresetn          : IN  std_logic;
        start            : IN  std_logic;
        busy             : OUT std_logic;
        done             : OUT std_logic;
        
        -- Soft decision inputs (SOFT_WIDTH bits per encoded bit)
        -- G1 and G2 streams, each NUM_SYMBOLS deep
        input_soft_g1    : IN  std_logic_vector(ENCODED_BITS/2 * SOFT_WIDTH - 1 DOWNTO 0);
        input_soft_g2    : IN  std_logic_vector(ENCODED_BITS/2 * SOFT_WIDTH - 1 DOWNTO 0);
        
        -- Decoded output
        output_bits      : OUT std_logic_vector(PAYLOAD_BITS-1 DOWNTO 0);
        
        -- Debug: final path metric (lower = more confident decode)
        debug_path_metric : OUT std_logic_vector(15 DOWNTO 0)
    );
END ENTITY viterbi_decoder_k7_soft;

ARCHITECTURE rtl OF viterbi_decoder_k7_soft IS

    CONSTANT NUM_STATES : INTEGER := 64;  -- 2^(K-1) for K=7
    CONSTANT NUM_SYMBOLS : INTEGER := ENCODED_BITS/2;  -- 1072 symbol pairs
    
    -- Metric width needs to accommodate accumulated soft metrics
    -- Worst case per symbol: 2 * (2^SOFT_WIDTH - 1) = max branch metric
    -- Over 1072 symbols, need enough bits to not overflow
    -- For SOFT_WIDTH=3: max branch = 14, total max = 14*1072 = 15008, needs 14 bits
    -- For SOFT_WIDTH=8: max branch = 510, total max = 546720, needs 20 bits
    CONSTANT METRIC_WIDTH : INTEGER := SOFT_WIDTH + 12;  -- Scales with soft width
    CONSTANT INF_METRIC : INTEGER := 2**(METRIC_WIDTH-1) - 1;
    
    -- Max soft value for this width
    CONSTANT SOFT_MAX : INTEGER := 2**SOFT_WIDTH - 1;
    
    TYPE state_t IS (IDLE, INITIALIZE, ACS_COMPUTE, FIND_BEST, 
                     TB_FETCH, TB_USE, COMPLETE);
    SIGNAL state : state_t := IDLE;
    
    TYPE metric_array_t IS ARRAY(0 TO NUM_STATES-1) OF unsigned(METRIC_WIDTH-1 DOWNTO 0);
    SIGNAL metrics_current : metric_array_t := (OTHERS => (OTHERS => '0'));
    SIGNAL metrics_next : metric_array_t := (OTHERS => (OTHERS => '0'));

    -- Decision memory in BRAM
    CONSTANT DECISION_DEPTH : INTEGER := NUM_SYMBOLS * NUM_STATES;
    TYPE decision_mem_t IS ARRAY(0 TO DECISION_DEPTH-1) OF std_logic;
    SIGNAL decision_mem : decision_mem_t;
   
    SIGNAL dec_wr_en : std_logic;
    SIGNAL dec_wr_addr : INTEGER RANGE 0 TO DECISION_DEPTH-1;
    SIGNAL dec_wr_data : std_logic;
    SIGNAL dec_rd_addr : INTEGER RANGE 0 TO DECISION_DEPTH-1;
    SIGNAL dec_rd_data : std_logic;
    
    SIGNAL time_step : INTEGER RANGE 0 TO NUM_SYMBOLS;
    SIGNAL state_idx : INTEGER RANGE 0 TO NUM_STATES-1;
    SIGNAL tb_time : INTEGER RANGE -1 TO NUM_SYMBOLS;
    SIGNAL tb_state : INTEGER RANGE 0 TO NUM_STATES-1;
    SIGNAL best_metric : unsigned(METRIC_WIDTH-1 DOWNTO 0);
    
    SIGNAL out_buf : std_logic_vector(PAYLOAD_BITS-1 DOWNTO 0);
    
    -- Current soft symbol pair
    SIGNAL soft_g1_current : unsigned(SOFT_WIDTH-1 DOWNTO 0);
    SIGNAL soft_g2_current : unsigned(SOFT_WIDTH-1 DOWNTO 0);

    -- Shift registers for soft input data
    SIGNAL g1_soft_sr : std_logic_vector(NUM_SYMBOLS * SOFT_WIDTH - 1 DOWNTO 0);
    SIGNAL g2_soft_sr : std_logic_vector(NUM_SYMBOLS * SOFT_WIDTH - 1 DOWNTO 0);

    ATTRIBUTE ram_style : STRING;
    ATTRIBUTE ram_style OF decision_mem : SIGNAL IS "block";
    ATTRIBUTE ram_style OF g1_soft_sr : SIGNAL IS "block";
    ATTRIBUTE ram_style OF g2_soft_sr : SIGNAL IS "block";
    ATTRIBUTE ram_style OF out_buf : SIGNAL IS "block";

    ATTRIBUTE dont_touch : STRING;
    ATTRIBUTE dont_touch OF state : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF metrics_current : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF metrics_next : SIGNAL IS "true";
    
    ----------------------------------------------------------------------------
    -- Compute expected encoder output for given state and input bit
    -- Returns (g1, g2) as 2-bit vector
    ----------------------------------------------------------------------------
    FUNCTION compute_output(curr_state : INTEGER; input_bit : std_logic) 
        RETURN std_logic_vector IS
        CONSTANT G1_POLY : std_logic_vector(6 DOWNTO 0) := "1111001";  -- 171 octal
        CONSTANT G2_POLY : std_logic_vector(6 DOWNTO 0) := "1011011";  -- 133 octal
        VARIABLE full_state : std_logic_vector(6 DOWNTO 0);
        VARIABLE g1, g2 : std_logic;
    BEGIN
        full_state := input_bit & std_logic_vector(to_unsigned(curr_state, 6));
        
        g1 := '0';
        FOR i IN 0 TO 6 LOOP
            IF G1_POLY(i) = '1' THEN
                g1 := g1 XOR full_state(6-i);
            END IF;
        END LOOP;
        
        g2 := '0';
        FOR i IN 0 TO 6 LOOP
            IF G2_POLY(i) = '1' THEN
                g2 := g2 XOR full_state(6-i);
            END IF;
        END LOOP;
        
        RETURN g1 & g2;
    END FUNCTION;
    
    ----------------------------------------------------------------------------
    -- Soft Branch Metric Calculation
    ----------------------------------------------------------------------------
    -- Computes distance between received soft values and expected bits
    --
    -- Convention: 
    --   soft = 0 means strong '0'
    --   soft = SOFT_MAX means strong '1'
    --
    -- If expected = '0': metric = soft_value (low soft = good match)
    -- If expected = '1': metric = SOFT_MAX - soft_value (high soft = good match)
    --
    -- Total branch metric = metric_g1 + metric_g2
    ----------------------------------------------------------------------------
    FUNCTION soft_branch_metric(
        soft_g1 : unsigned;
        soft_g2 : unsigned;
        expected : std_logic_vector(1 DOWNTO 0)  -- g1 & g2
    ) RETURN unsigned IS
        VARIABLE metric_g1 : unsigned(SOFT_WIDTH DOWNTO 0);
        VARIABLE metric_g2 : unsigned(SOFT_WIDTH DOWNTO 0);
        VARIABLE total : unsigned(SOFT_WIDTH+1 DOWNTO 0);
    BEGIN
        -- G1 metric
        IF expected(1) = '0' THEN
            -- Expected '0': low soft value is good
            metric_g1 := resize(soft_g1, SOFT_WIDTH+1);
        ELSE
            -- Expected '1': high soft value is good, so metric = MAX - soft
            metric_g1 := to_unsigned(SOFT_MAX, SOFT_WIDTH+1) - resize(soft_g1, SOFT_WIDTH+1);
        END IF;
        
        -- G2 metric
        IF expected(0) = '0' THEN
            metric_g2 := resize(soft_g2, SOFT_WIDTH+1);
        ELSE
            metric_g2 := to_unsigned(SOFT_MAX, SOFT_WIDTH+1) - resize(soft_g2, SOFT_WIDTH+1);
        END IF;
        
        -- Total branch metric
        total := resize(metric_g1, SOFT_WIDTH+2) + resize(metric_g2, SOFT_WIDTH+2);
        
        RETURN total;
    END FUNCTION;

BEGIN

    -- BRAM write process
    PROCESS(clk)
    BEGIN
        IF rising_edge(clk) THEN
            IF dec_wr_en = '1' THEN
                decision_mem(dec_wr_addr) <= dec_wr_data;
            END IF;
        END IF;
    END PROCESS;
    
    -- BRAM read process
    PROCESS(clk)
    BEGIN
        IF rising_edge(clk) THEN
            dec_rd_data <= decision_mem(dec_rd_addr);
        END IF;
    END PROCESS;
    
    -- Extract current soft symbols from shift register LSBs
    soft_g1_current <= unsigned(g1_soft_sr(SOFT_WIDTH-1 DOWNTO 0));
    soft_g2_current <= unsigned(g2_soft_sr(SOFT_WIDTH-1 DOWNTO 0));

    -- Main FSM
    PROCESS(clk, aresetn)
        VARIABLE prev_state_0, prev_state_1 : INTEGER RANGE 0 TO NUM_STATES-1;
        VARIABLE input_bit : std_logic;
        VARIABLE expected_0, expected_1 : std_logic_vector(1 DOWNTO 0);
        VARIABLE branch_0, branch_1 : unsigned(SOFT_WIDTH+1 DOWNTO 0);
        VARIABLE metric_0, metric_1 : unsigned(METRIC_WIDTH-1 DOWNTO 0);
        VARIABLE min_metric : unsigned(METRIC_WIDTH-1 DOWNTO 0);
        VARIABLE best_state_var : INTEGER RANGE 0 TO NUM_STATES-1;
    BEGIN
        IF aresetn = '0' THEN
            state <= IDLE;
            busy <= '0';
            done <= '0';
            dec_wr_en <= '0';
            time_step <= 0;                              
            state_idx <= 0;                                
            metrics_next <= (OTHERS => (OTHERS => '0'));
            g1_soft_sr <= (OTHERS => '0');
            g2_soft_sr <= (OTHERS => '0');
            best_metric <= (OTHERS => '1');
            
        ELSIF rising_edge(clk) THEN
            done <= '0';
            dec_wr_en <= '0';
            
            CASE state IS

                WHEN IDLE =>
                    busy <= '0';
                    IF start = '1' THEN
                        state <= INITIALIZE;
                        busy <= '1';
                        state_idx <= 0;
                        -- Parallel load shift registers from input vectors
                        g1_soft_sr <= input_soft_g1;
                        g2_soft_sr <= input_soft_g2;
                    END IF;
                
                WHEN INITIALIZE =>
                    IF state_idx < NUM_STATES THEN
                        IF state_idx = 0 THEN
                            metrics_current(state_idx) <= (OTHERS => '0');
                        ELSE
                            metrics_current(state_idx) <= to_unsigned(INF_METRIC, METRIC_WIDTH);
                        END IF;
                        state_idx <= state_idx + 1;
                    ELSE
                        state <= ACS_COMPUTE;
                        state_idx <= 0;
                        time_step <= 0;
                    END IF;
                
                WHEN ACS_COMPUTE =>
                    IF time_step < NUM_SYMBOLS THEN
                        IF state_idx < NUM_STATES THEN
                            -- Butterfly computation
                            prev_state_0 := state_idx / 2;
                            prev_state_1 := (state_idx / 2) + 32;
                            input_bit := std_logic(to_unsigned(state_idx MOD 2, 1)(0));
                            
                            -- Path from prev_state_0
                            expected_0 := compute_output(prev_state_0, input_bit);
                            branch_0 := soft_branch_metric(soft_g1_current, soft_g2_current, expected_0);
                            metric_0 := metrics_current(prev_state_0) + 
                                       resize(branch_0, METRIC_WIDTH);
                            
                            -- Path from prev_state_1
                            expected_1 := compute_output(prev_state_1, input_bit);
                            branch_1 := soft_branch_metric(soft_g1_current, soft_g2_current, expected_1);
                            metric_1 := metrics_current(prev_state_1) + 
                                       resize(branch_1, METRIC_WIDTH);
                            
                            -- Select survivor
                            IF metric_0 <= metric_1 THEN
                                metrics_next(state_idx) <= metric_0;
                                dec_wr_data <= '0';
                            ELSE
                                metrics_next(state_idx) <= metric_1;
                                dec_wr_data <= '1';
                            END IF;
                            
                            dec_wr_addr <= time_step * NUM_STATES + state_idx;
                            dec_wr_en <= '1';
                            state_idx <= state_idx + 1;
                        ELSE
                            -- Done with all states for this time step
                            metrics_current <= metrics_next;
                            state_idx <= 0;
                            time_step <= time_step + 1;
                            -- Shift right: move to next symbol pair
                            g1_soft_sr <= (SOFT_WIDTH-1 DOWNTO 0 => '0') & 
                                         g1_soft_sr(NUM_SYMBOLS*SOFT_WIDTH-1 DOWNTO SOFT_WIDTH);
                            g2_soft_sr <= (SOFT_WIDTH-1 DOWNTO 0 => '0') & 
                                         g2_soft_sr(NUM_SYMBOLS*SOFT_WIDTH-1 DOWNTO SOFT_WIDTH);
                        END IF;
                    ELSE
                        state <= FIND_BEST;
                        state_idx <= 0;
                    END IF;
                
                WHEN FIND_BEST =>
                    IF state_idx = 0 THEN
                        min_metric := metrics_current(0);
                        best_state_var := 0;
                        state_idx <= 1;
                    ELSIF state_idx < NUM_STATES THEN
                        IF metrics_current(state_idx) < min_metric THEN
                            min_metric := metrics_current(state_idx);
                            best_state_var := state_idx;
                        END IF;
                        state_idx <= state_idx + 1;
                    ELSE
                        tb_state <= best_state_var;
                        tb_time <= NUM_SYMBOLS - 1;
                        best_metric <= min_metric;
                        dec_rd_addr <= (NUM_SYMBOLS-1) * NUM_STATES + best_state_var;
                        state <= TB_FETCH;
                    END IF;
                
                WHEN TB_FETCH =>
                    -- Cycle 1: Issue BRAM read
                    state <= TB_USE;
                
                WHEN TB_USE =>
                    -- Cycle 2: Use the fetched decision
                    IF tb_time >= 0 THEN
                        -- Output decoded bit
                        out_buf(tb_time) <= std_logic(to_unsigned(tb_state MOD 2, 1)(0));
                        
                        -- Move to previous state based on decision
                        IF dec_rd_data = '0' THEN
                            tb_state <= tb_state / 2;
                        ELSE
                            tb_state <= (tb_state / 2) + 32;
                        END IF;
                        
                        tb_time <= tb_time - 1;
                        
                        -- Fetch next decision (if not done)
                        IF tb_time > 0 THEN
                            IF dec_rd_data = '0' THEN
                                dec_rd_addr <= (tb_time-1) * NUM_STATES + (tb_state / 2);
                            ELSE
                                dec_rd_addr <= (tb_time-1) * NUM_STATES + ((tb_state / 2) + 32);
                            END IF;
                            state <= TB_FETCH;
                        ELSE
                            state <= COMPLETE;
                        END IF;
                    ELSE
                        state <= COMPLETE;
                    END IF;
                
                WHEN COMPLETE =>
                    done <= '1';
                    busy <= '0';
                    state <= IDLE;
                    
            END CASE;
        END IF;
    END PROCESS;
    
    output_bits <= out_buf;
    debug_path_metric <= std_logic_vector(resize(best_metric, 16));

END ARCHITECTURE rtl;
