------------------------------------------------------------------------------------------------------
-- Soft-Decision Viterbi Decoder for K=7 Convolutional Code
------------------------------------------------------------------------------------------------------
-- Rate 1/2, constraint length K=7, 64 states
-- Generator polynomials: G1 = 171 octal, G2 = 133 octal (NASA Voyager code)
--
-- Supports both hard-decision (1-bit) and soft-decision (3-4 bit) inputs
-- Uses register-exchange for survivor path management (simpler than traceback memory)
--
-- Performance: 
--   Hard decisions: ~5 dB coding gain at BER=10^-5
--   3-bit soft:     ~7 dB coding gain (2 dB improvement over hard)
--   4-bit soft:     ~7.3 dB coding gain (marginal improvement over 3-bit)
--
-- Think of this like a maze solver that tracks 64 parallel adventurer parties,
-- keeping only the most efficient path to each destination
------------------------------------------------------------------------------------------------------

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.numeric_std.ALL;

ENTITY viterbi_decoder_k7 IS
    GENERIC (
        PAYLOAD_BYTES    : NATURAL := 134;   -- Output size in bytes
        ENCODED_BYTES    : NATURAL := 268;   -- Input size in bytes
        SOFT_DECISION_WIDTH : NATURAL := 3;  -- Bits per soft input (1=hard, 3-4=soft)
        TRACEBACK_DEPTH  : NATURAL := 35;    -- Path memory depth (5*K is typical)
        METRIC_WIDTH     : NATURAL := 12     -- Path metric width (avoid overflow)
    );
    PORT (
        clk              : IN  std_logic;
        aresetn          : IN  std_logic;
        
        -- Control
        start            : IN  std_logic;
        busy             : OUT std_logic;
        done             : OUT std_logic;
        
        -- Input buffer (soft decisions, MSB first)
        -- For hard decisions: use only MSB of each symbol
        -- For soft decisions: full SOFT_DECISION_WIDTH bits represent confidence
        --   Most positive value = strong '1', most negative = strong '0'
        input_buffer_g1  : IN  std_logic_vector(ENCODED_BYTES*4-1 DOWNTO 0);
        input_buffer_g2  : IN  std_logic_vector(ENCODED_BYTES*4-1 DOWNTO 0);
        
        -- Output buffer (decoded bits, MSB first)
        output_buffer    : OUT std_logic_vector(PAYLOAD_BYTES*8-1 DOWNTO 0);
        
        -- Debug/monitoring
        path_metric_min  : OUT std_logic_vector(METRIC_WIDTH-1 DOWNTO 0);
        path_metric_max  : OUT std_logic_vector(METRIC_WIDTH-1 DOWNTO 0)
    );
END ENTITY viterbi_decoder_k7;

ARCHITECTURE rtl OF viterbi_decoder_k7 IS

    CONSTANT NUM_STATES : NATURAL := 64;  -- 2^(K-1) states
    CONSTANT TRACEBACK_LENGTH : NATURAL := TRACEBACK_DEPTH;
    
    -- State machine
    TYPE state_t IS (IDLE, INIT_METRICS, DECODE_BITS, TRACEBACK, COMPLETE);
    SIGNAL state : state_t := IDLE;
    
    -- Path metrics: one metric per state (track cumulative "cost" to reach each state)
    TYPE metric_array_t IS ARRAY(0 TO NUM_STATES-1) OF signed(METRIC_WIDTH-1 DOWNTO 0);
    SIGNAL path_metrics_curr : metric_array_t := (OTHERS => (OTHERS => '0'));
    SIGNAL path_metrics_next : metric_array_t := (OTHERS => (OTHERS => '0'));
    
    -- Survivor path memory: register-exchange method
    -- Each state stores its best path history
    TYPE path_history_t IS ARRAY(0 TO TRACEBACK_LENGTH-1) OF std_logic;
    TYPE survivor_memory_t IS ARRAY(0 TO NUM_STATES-1) OF path_history_t;
    SIGNAL survivor_paths_curr : survivor_memory_t;
    SIGNAL survivor_paths_next : survivor_memory_t;
    
    -- Branch metrics: cost to take each transition
    SIGNAL branch_metric_00 : signed(METRIC_WIDTH-1 DOWNTO 0);  -- Output = 00
    SIGNAL branch_metric_01 : signed(METRIC_WIDTH-1 DOWNTO 0);  -- Output = 01
    SIGNAL branch_metric_10 : signed(METRIC_WIDTH-1 DOWNTO 0);  -- Output = 10
    SIGNAL branch_metric_11 : signed(METRIC_WIDTH-1 DOWNTO 0);  -- Output = 11
    
    -- Bit processing
    SIGNAL bit_index : NATURAL RANGE 0 TO ENCODED_BYTES*4;
    SIGNAL output_bit_index : NATURAL RANGE 0 TO PAYLOAD_BYTES*8;
    
    -- Current received symbols (soft decisions)
    SIGNAL rx_g1 : signed(SOFT_DECISION_WIDTH-1 DOWNTO 0);
    SIGNAL rx_g2 : signed(SOFT_DECISION_WIDTH-1 DOWNTO 0);
    
    -- Trellis butterfly outputs (expected G1, G2 for each input bit)
    TYPE output_lut_t IS ARRAY(0 TO NUM_STATES-1, 0 TO 1) OF std_logic_vector(1 DOWNTO 0);
    SIGNAL expected_outputs : output_lut_t;
    
    -- Output buffer working copy
    SIGNAL out_buf : std_logic_vector(PAYLOAD_BYTES*8-1 DOWNTO 0);
    
    -- Best path tracking for traceback
    SIGNAL best_state : NATURAL RANGE 0 TO NUM_STATES-1;
    SIGNAL traceback_bit : NATURAL RANGE 0 TO TRACEBACK_LENGTH-1;
    
    --------------------------------------------------------------------------------------------
    -- Precompute expected outputs for each state transition
    -- This is the trellis structure for K=7, rate 1/2 code
    --------------------------------------------------------------------------------------------
    FUNCTION compute_expected_output(
        current_state : NATURAL;
        input_bit     : std_logic
    ) RETURN std_logic_vector IS
        VARIABLE full_state : std_logic_vector(6 DOWNTO 0);
        VARIABLE g1, g2 : std_logic;
        CONSTANT G1_POLY : std_logic_vector(6 DOWNTO 0) := "1111001";
        CONSTANT G2_POLY : std_logic_vector(6 DOWNTO 0) := "1011011";
    BEGIN
        -- Construct full state (input bit + 6 state bits)
        full_state := input_bit & std_logic_vector(to_unsigned(current_state, 6));
        
        -- Compute G1 output
        g1 := '0';
        FOR i IN 0 TO 6 LOOP
            IF G1_POLY(i) = '1' THEN
                g1 := g1 XOR full_state(6-i);
            END IF;
        END LOOP;
        
        -- Compute G2 output
        g2 := '0';
        FOR i IN 0 TO 6 LOOP
            IF G2_POLY(i) = '1' THEN
                g2 := g2 XOR full_state(6-i);
            END IF;
        END LOOP;
        
        RETURN g1 & g2;
    END FUNCTION;

BEGIN

    --------------------------------------------------------------------------------------------
    -- Initialize expected output LUT (done once at elaboration time)
    --------------------------------------------------------------------------------------------
    gen_lut: PROCESS
    BEGIN
        FOR s IN 0 TO NUM_STATES-1 LOOP
            expected_outputs(s, 0) <= compute_expected_output(s, '0');
            expected_outputs(s, 1) <= compute_expected_output(s, '1');
        END LOOP;
        WAIT;  -- Static initialization
    END PROCESS;

    --------------------------------------------------------------------------------------------
    -- Branch Metric Computation
    -- For soft decisions: Euclidean distance between received and expected
    -- For hard decisions: Hamming distance
    --------------------------------------------------------------------------------------------
    PROCESS(rx_g1, rx_g2)
        VARIABLE diff_g1, diff_g2 : signed(SOFT_DECISION_WIDTH DOWNTO 0);
        VARIABLE metric : signed(METRIC_WIDTH-1 DOWNTO 0);
    BEGIN
        -- Expected output 00 (both symbols are '0' = most negative value)
        diff_g1 := resize(rx_g1, SOFT_DECISION_WIDTH+1) + 
                   to_signed(2**(SOFT_DECISION_WIDTH-1), SOFT_DECISION_WIDTH+1);
        diff_g2 := resize(rx_g2, SOFT_DECISION_WIDTH+1) + 
                   to_signed(2**(SOFT_DECISION_WIDTH-1), SOFT_DECISION_WIDTH+1);
        branch_metric_00 <= resize(diff_g1*diff_g1 + diff_g2*diff_g2, METRIC_WIDTH);
        
        -- Expected output 01 (g1='0', g2='1')
        diff_g1 := resize(rx_g1, SOFT_DECISION_WIDTH+1) + 
                   to_signed(2**(SOFT_DECISION_WIDTH-1), SOFT_DECISION_WIDTH+1);
        diff_g2 := resize(rx_g2, SOFT_DECISION_WIDTH+1) - 
                   to_signed(2**(SOFT_DECISION_WIDTH-1)-1, SOFT_DECISION_WIDTH+1);
        branch_metric_01 <= resize(diff_g1*diff_g1 + diff_g2*diff_g2, METRIC_WIDTH);
        
        -- Expected output 10
        diff_g1 := resize(rx_g1, SOFT_DECISION_WIDTH+1) - 
                   to_signed(2**(SOFT_DECISION_WIDTH-1)-1, SOFT_DECISION_WIDTH+1);
        diff_g2 := resize(rx_g2, SOFT_DECISION_WIDTH+1) + 
                   to_signed(2**(SOFT_DECISION_WIDTH-1), SOFT_DECISION_WIDTH+1);
        branch_metric_10 <= resize(diff_g1*diff_g1 + diff_g2*diff_g2, METRIC_WIDTH);
        
        -- Expected output 11
        diff_g1 := resize(rx_g1, SOFT_DECISION_WIDTH+1) - 
                   to_signed(2**(SOFT_DECISION_WIDTH-1)-1, SOFT_DECISION_WIDTH+1);
        diff_g2 := resize(rx_g2, SOFT_DECISION_WIDTH+1) - 
                   to_signed(2**(SOFT_DECISION_WIDTH-1)-1, SOFT_DECISION_WIDTH+1);
        branch_metric_11 <= resize(diff_g1*diff_g1 + diff_g2*diff_g2, METRIC_WIDTH);
    END PROCESS;

    --------------------------------------------------------------------------------------------
    -- Main Viterbi Decoder State Machine
    --------------------------------------------------------------------------------------------
    PROCESS(clk, aresetn)
        VARIABLE prev_state_0, prev_state_1 : NATURAL RANGE 0 TO NUM_STATES-1;
        VARIABLE metric_0, metric_1 : signed(METRIC_WIDTH-1 DOWNTO 0);
        VARIABLE input_bit_0, input_bit_1 : std_logic;
        VARIABLE expected_out_0, expected_out_1 : std_logic_vector(1 DOWNTO 0);
        VARIABLE branch_met_0, branch_met_1 : signed(METRIC_WIDTH-1 DOWNTO 0);
        VARIABLE min_metric, max_metric : signed(METRIC_WIDTH-1 DOWNTO 0);
    BEGIN
        IF aresetn = '0' THEN
            state <= IDLE;
            busy <= '0';
            done <= '0';
            bit_index <= 0;
            output_bit_index <= 0;
            path_metrics_curr <= (OTHERS => (OTHERS => '0'));
            
        ELSIF rising_edge(clk) THEN
            done <= '0';  -- Pulse signal
            
            CASE state IS
            
                WHEN IDLE =>
                    busy <= '0';
                    IF start = '1' THEN
                        state <= INIT_METRICS;
                        busy <= '1';
                        bit_index <= 0;
                        output_bit_index <= 0;
                    END IF;
                
                WHEN INIT_METRICS =>
                    -- Initialize: state 0 has metric 0, all others have large metric
                    FOR i IN 0 TO NUM_STATES-1 LOOP
                        IF i = 0 THEN
                            path_metrics_curr(i) <= (OTHERS => '0');
                        ELSE
                            path_metrics_curr(i) <= to_signed(2**(METRIC_WIDTH-2), METRIC_WIDTH);
                        END IF;
                        -- Clear survivor paths
                        FOR j IN 0 TO TRACEBACK_LENGTH-1 LOOP
                            survivor_paths_curr(i)(j) <= '0';
                        END LOOP;
                    END LOOP;
                    state <= DECODE_BITS;
                
                WHEN DECODE_BITS =>
                    IF bit_index < (PAYLOAD_BYTES*8 + 6)*2 THEN  -- Include 6 flush bits
                        -- Get received soft symbols
                        rx_g1 <= signed(input_buffer_g1(
                            ENCODED_BYTES*4-1 - bit_index*SOFT_DECISION_WIDTH DOWNTO 
                            ENCODED_BYTES*4 - (bit_index+1)*SOFT_DECISION_WIDTH));
                        rx_g2 <= signed(input_buffer_g2(
                            ENCODED_BYTES*4-1 - bit_index*SOFT_DECISION_WIDTH DOWNTO 
                            ENCODED_BYTES*4 - (bit_index+1)*SOFT_DECISION_WIDTH));
                        
                        -- ACS (Add-Compare-Select) for all states
                        FOR s IN 0 TO NUM_STATES-1 LOOP
                            -- Each state can be reached from two previous states
                            -- Previous state that led here with input bit = 0
                            prev_state_0 := (s * 2) MOD NUM_STATES;
                            -- Previous state that led here with input bit = 1
                            prev_state_1 := ((s * 2) + 1) MOD NUM_STATES;
                            
                            -- Get expected outputs for these transitions
                            expected_out_0 := expected_outputs(prev_state_0, 0);
                            expected_out_1 := expected_outputs(prev_state_1, 1);
                            
                            -- Branch metrics
                            CASE expected_out_0 IS
                                WHEN "00" => branch_met_0 := branch_metric_00;
                                WHEN "01" => branch_met_0 := branch_metric_01;
                                WHEN "10" => branch_met_0 := branch_metric_10;
                                WHEN "11" => branch_met_0 := branch_metric_11;
                                WHEN OTHERS => branch_met_0 := (OTHERS => '0');
                            END CASE;
                            
                            CASE expected_out_1 IS
                                WHEN "00" => branch_met_1 := branch_metric_00;
                                WHEN "01" => branch_met_1 := branch_metric_01;
                                WHEN "10" => branch_met_1 := branch_metric_10;
                                WHEN "11" => branch_met_1 := branch_metric_11;
                                WHEN OTHERS => branch_met_1 := (OTHERS => '0');
                            END CASE;
                            
                            -- Add-Compare-Select
                            metric_0 := path_metrics_curr(prev_state_0) + branch_met_0;
                            metric_1 := path_metrics_curr(prev_state_1) + branch_met_1;
                            
                            IF metric_0 < metric_1 THEN
                                path_metrics_next(s) <= metric_0;
                                input_bit_0 := '0';
                                -- Shift survivor path and prepend decision
                                FOR j IN TRACEBACK_LENGTH-1 DOWNTO 1 LOOP
                                    survivor_paths_next(s)(j) <= survivor_paths_curr(prev_state_0)(j-1);
                                END LOOP;
                                survivor_paths_next(s)(0) <= input_bit_0;
                            ELSE
                                path_metrics_next(s) <= metric_1;
                                input_bit_1 := '1';
                                FOR j IN TRACEBACK_LENGTH-1 DOWNTO 1 LOOP
                                    survivor_paths_next(s)(j) <= survivor_paths_curr(prev_state_1)(j-1);
                                END LOOP;
                                survivor_paths_next(s)(0) <= input_bit_1;
                            END IF;
                        END LOOP;
                        
                        -- Update current metrics
                        path_metrics_curr <= path_metrics_next;
                        survivor_paths_curr <= survivor_paths_next;
                        
                        bit_index <= bit_index + 2;  -- Processed 2 symbols
                    ELSE
                        state <= TRACEBACK;
                        traceback_bit <= 0;
                        
                        -- Find best ending state (should be state 0 due to flush bits)
                        min_metric := path_metrics_curr(0);
                        best_state <= 0;
                        FOR i IN 1 TO NUM_STATES-1 LOOP
                            IF path_metrics_curr(i) < min_metric THEN
                                min_metric := path_metrics_curr(i);
                                best_state <= i;
                            END IF;
                        END LOOP;
                    END IF;
                
                WHEN TRACEBACK =>
                    -- Extract decoded bits from survivor path of best state
                    IF traceback_bit < PAYLOAD_BYTES*8 THEN
                        out_buf(PAYLOAD_BYTES*8 - 1 - traceback_bit) <= 
                            survivor_paths_curr(best_state)(TRACEBACK_LENGTH - 1 - traceback_bit);
                        traceback_bit <= traceback_bit + 1;
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
    
    -- Output assignment
    output_buffer <= out_buf;
    
    -- Debug outputs
    PROCESS(path_metrics_curr)
        VARIABLE min_val, max_val : signed(METRIC_WIDTH-1 DOWNTO 0);
    BEGIN
        min_val := path_metrics_curr(0);
        max_val := path_metrics_curr(0);
        FOR i IN 1 TO NUM_STATES-1 LOOP
            IF path_metrics_curr(i) < min_val THEN
                min_val := path_metrics_curr(i);
            END IF;
            IF path_metrics_curr(i) > max_val THEN
                max_val := path_metrics_curr(i);
            END IF;
        END LOOP;
        path_metric_min <= std_logic_vector(min_val);
        path_metric_max <= std_logic_vector(max_val);
    END PROCESS;

END ARCHITECTURE rtl;
