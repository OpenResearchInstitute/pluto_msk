------------------------------------------------------------------------------------------------------
-- BRAM-Optimized Viterbi Decoder - SHIFT REGISTER INPUTS
------------------------------------------------------------------------------------------------------
-- This version uses shift registers for the input data to avoid massive muxes.
-- Instead of input_bits_g1(time_step) creating a 1072:1 mux, we:
--   1. Load the parallel input into a shift register
--   2. Shift out one bit per time step
--
-- This saves ~2000 LUTs (2 x 1072:1 mux elimination)
--
-- Interface is IDENTICAL to original - parallel load happens internally.
------------------------------------------------------------------------------------------------------

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.numeric_std.ALL;

ENTITY viterbi_decoder_k7_simple IS
    GENERIC (
        PAYLOAD_BITS     : NATURAL := 134*8;
        ENCODED_BITS     : NATURAL := 268*8;  
        TRACEBACK_DEPTH  : NATURAL := 35
    );
    PORT (
        clk              : IN  std_logic;
        aresetn          : IN  std_logic;
        start            : IN  std_logic;
        busy             : OUT std_logic;
        done             : OUT std_logic;
        input_bits_g1    : IN  std_logic_vector(ENCODED_BITS-1 DOWNTO 0);
        input_bits_g2    : IN  std_logic_vector(ENCODED_BITS-1 DOWNTO 0);
        output_bits      : OUT std_logic_vector(PAYLOAD_BITS-1 DOWNTO 0)
    );
END ENTITY viterbi_decoder_k7_simple;

ARCHITECTURE rtl OF viterbi_decoder_k7_simple IS

    ATTRIBUTE KEEP_HIERARCHY : STRING;
    ATTRIBUTE KEEP_HIERARCHY OF rtl : ARCHITECTURE IS "yes";

    CONSTANT NUM_STATES : INTEGER := 64;
    CONSTANT METRIC_WIDTH : INTEGER := 12;
    CONSTANT INF_METRIC : INTEGER := 4095;
    CONSTANT NUM_SYMBOLS : INTEGER := ENCODED_BITS/2;  -- 1072

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
    
    SIGNAL out_buf : std_logic_vector(PAYLOAD_BITS-1 DOWNTO 0);
    SIGNAL rx_symbol : std_logic_vector(1 DOWNTO 0);

    -- SHIFT REGISTERS for input data (replaces massive mux)
    -- These shift left, MSB contains current symbol
    SIGNAL g1_sr : std_logic_vector(NUM_SYMBOLS-1 DOWNTO 0);
    SIGNAL g2_sr : std_logic_vector(NUM_SYMBOLS-1 DOWNTO 0);

    ATTRIBUTE ram_style : STRING;
    ATTRIBUTE ram_style OF decision_mem : SIGNAL IS "block";

    ATTRIBUTE dont_touch : STRING;
    ATTRIBUTE dont_touch OF state : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF metrics_current : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF metrics_next : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF decision_mem : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF g1_sr : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF g2_sr : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF out_buf : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF time_step : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF tb_time : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF tb_state : SIGNAL IS "true";

    ATTRIBUTE ram_style OF g1_sr : SIGNAL IS "block";
    ATTRIBUTE ram_style OF g2_sr : SIGNAL IS "block";
    ATTRIBUTE ram_style OF out_buf : SIGNAL IS "block";


    
    FUNCTION compute_output(curr_state : INTEGER; input_bit : std_logic) 
        RETURN std_logic_vector IS
        CONSTANT G1_POLY : std_logic_vector(6 DOWNTO 0) := "1111001";
        CONSTANT G2_POLY : std_logic_vector(6 DOWNTO 0) := "1011011";
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
    
    FUNCTION hamming_distance(a, b : std_logic_vector) RETURN INTEGER IS
        VARIABLE dist : INTEGER := 0;
    BEGIN
        FOR i IN a'RANGE LOOP
            IF a(i) /= b(i) THEN
                dist := dist + 1;
            END IF;
        END LOOP;
        RETURN dist;
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

    -- Main FSM
    PROCESS(clk, aresetn)
        VARIABLE prev_state_0, prev_state_1 : INTEGER RANGE 0 TO NUM_STATES-1;
        VARIABLE input_bit : std_logic;
        VARIABLE expected_0, expected_1 : std_logic_vector(1 DOWNTO 0);
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
            g1_sr <= (OTHERS => '0');
            g2_sr <= (OTHERS => '0');
            
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
                        -- PARALLEL LOAD shift registers from input vectors
                        -- Load bits 0..1071 directly - simple slice, no mux needed
                        -- We'll read from bit 0 and shift right each time step
                        g1_sr <= input_bits_g1(NUM_SYMBOLS-1 DOWNTO 0);
                        g2_sr <= input_bits_g2(NUM_SYMBOLS-1 DOWNTO 0);
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
                        IF state_idx = 0 THEN
                            -- Get current symbol from LSB of shift registers
                            rx_symbol <= g1_sr(0) & g2_sr(0);
                        END IF;
                        
                        IF state_idx < NUM_STATES THEN
                            prev_state_0 := state_idx / 2;
                            prev_state_1 := (state_idx / 2) + 32;
                            input_bit := std_logic(to_unsigned(state_idx MOD 2, 1)(0));
                            
                            expected_0 := compute_output(prev_state_0, input_bit);
                            metric_0 := metrics_current(prev_state_0) + 
                                       to_unsigned(hamming_distance(rx_symbol, expected_0), METRIC_WIDTH);
                            
                            expected_1 := compute_output(prev_state_1, input_bit);
                            metric_1 := metrics_current(prev_state_1) + 
                                       to_unsigned(hamming_distance(rx_symbol, expected_1), METRIC_WIDTH);
                            
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
                            -- SHIFT RIGHT: next symbol moves to bit 0
                            g1_sr <= '0' & g1_sr(NUM_SYMBOLS-1 DOWNTO 1);
                            g2_sr <= '0' & g2_sr(NUM_SYMBOLS-1 DOWNTO 1);
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
                        dec_rd_addr <= (NUM_SYMBOLS-1) * NUM_STATES + best_state_var;
                        state <= TB_FETCH;
                    END IF;
                
                -- SIMPLIFIED 2-CYCLE TRACEBACK
                WHEN TB_FETCH =>
                    -- Cycle 1: Issue BRAM read for current (tb_time, tb_state)
                    state <= TB_USE;
                
                WHEN TB_USE =>
                    -- Cycle 2: Use the decision that was fetched
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

END ARCHITECTURE rtl;
