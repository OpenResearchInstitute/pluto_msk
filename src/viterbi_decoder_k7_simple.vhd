------------------------------------------------------------------------------------------------------
-- FIXED Viterbi Decoder for K=7 Code (NASA Voyager)
------------------------------------------------------------------------------------------------------
-- Corrected Issues:
-- 1. MSB-first bit indexing to match encoder output format
-- 2. Traceback now correctly outputs input bits (LSB of state) not decision bits
------------------------------------------------------------------------------------------------------

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.numeric_std.ALL;

ENTITY viterbi_decoder_k7_simple IS
    GENERIC (
        PAYLOAD_BITS     : NATURAL := 134*8;  -- 1072 bits
        ENCODED_BITS     : NATURAL := 268*8;  -- 2144 bits  
        TRACEBACK_DEPTH  : NATURAL := 35      -- 5*K recommended
    );
    PORT (
        clk              : IN  std_logic;
        aresetn          : IN  std_logic;
        
        start            : IN  std_logic;
        busy             : OUT std_logic;
        done             : OUT std_logic;
        
        -- Hard decision inputs (g1 and g2 bits)
        input_bits_g1    : IN  std_logic_vector(ENCODED_BITS-1 DOWNTO 0);
        input_bits_g2    : IN  std_logic_vector(ENCODED_BITS-1 DOWNTO 0);
        
        output_bits      : OUT std_logic_vector(PAYLOAD_BITS-1 DOWNTO 0)
    );
END ENTITY viterbi_decoder_k7_simple;

ARCHITECTURE rtl OF viterbi_decoder_k7_simple IS

    CONSTANT NUM_STATES : INTEGER := 64;
    CONSTANT METRIC_WIDTH : INTEGER := 12;
    CONSTANT INF_METRIC : INTEGER := 4095;
    
    TYPE state_t IS (IDLE, INITIALIZE, ACS_COMPUTE, TRACEBACK, COMPLETE);
    SIGNAL state : state_t := IDLE;
    
    -- Path metrics arrays are now VARIABLES in the process
    TYPE metric_array_t IS ARRAY(0 TO NUM_STATES-1) OF INTEGER RANGE 0 TO INF_METRIC;
    
    -- Decision memory: stores which previous state was selected (MSB bit)
    TYPE decision_array_t IS ARRAY(0 TO ENCODED_BITS/2) OF std_logic_vector(NUM_STATES-1 DOWNTO 0);
    SIGNAL decisions : decision_array_t;

    -- Force synthesis to use BRAM
    ATTRIBUTE ram_style : STRING;
    ATTRIBUTE ram_style OF decisions : SIGNAL IS "block";
    
    -- Counters
    SIGNAL time_step : INTEGER RANGE 0 TO ENCODED_BITS/2 + 1;
    SIGNAL tb_step : INTEGER RANGE -1 TO ENCODED_BITS/2;
    SIGNAL output_idx : INTEGER RANGE 0 TO PAYLOAD_BITS;
    
    -- Current state during traceback
    SIGNAL tb_state : INTEGER RANGE 0 TO NUM_STATES-1;
    
    -- Output buffer
    SIGNAL out_buf : std_logic_vector(PAYLOAD_BITS-1 DOWNTO 0);
    
    --------------------------------------------------------------------------------------------
    -- Trellis functions
    --------------------------------------------------------------------------------------------
    FUNCTION next_state(curr_state : INTEGER; input_bit : std_logic) RETURN INTEGER IS
        VARIABLE shift_reg : std_logic_vector(5 DOWNTO 0);
    BEGIN
        shift_reg := std_logic_vector(to_unsigned(curr_state, 6));
        RETURN to_integer(unsigned(input_bit & shift_reg(5 DOWNTO 1)));
    END FUNCTION;
    
    FUNCTION compute_output(curr_state : INTEGER; input_bit : std_logic) RETURN std_logic_vector IS
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
    
    FUNCTION hamming_distance(a : std_logic_vector; b : std_logic_vector) RETURN INTEGER IS
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

    PROCESS(clk, aresetn)
        VARIABLE received_symbol : std_logic_vector(1 DOWNTO 0);
        VARIABLE expected_symbol : std_logic_vector(1 DOWNTO 0);
        VARIABLE branch_metric : INTEGER;
        VARIABLE new_metric : INTEGER;
        VARIABLE prev_state_for_0 : INTEGER;
        VARIABLE prev_state_for_1 : INTEGER;
        VARIABLE metric_via_0 : INTEGER;
        VARIABLE metric_via_1 : INTEGER;
        VARIABLE min_metric : INTEGER;
        VARIABLE best_state : INTEGER;
        VARIABLE input_bit_used : INTEGER;
        
        -- **FIX: Use VARIABLES for metrics, not SIGNALS!**
        VARIABLE metrics_old : metric_array_t;
        VARIABLE metrics_new : metric_array_t;
    BEGIN
        IF aresetn = '0' THEN
            state <= IDLE;
            busy <= '0';
            done <= '0';
            time_step <= 0;
            
        ELSIF rising_edge(clk) THEN
            done <= '0';
            
            CASE state IS
            
                WHEN IDLE =>
                    busy <= '0';
                    IF start = '1' THEN
                        state <= INITIALIZE;
                        busy <= '1';
                        time_step <= 0;
                    END IF;
                
                WHEN INITIALIZE =>
                    -- Start with state 0 having metric 0, all others infinity
                    FOR i IN 0 TO NUM_STATES-1 LOOP
                        IF i = 0 THEN
                            metrics_old(i) := 0;
                        ELSE
                            metrics_old(i) := INF_METRIC;
                        END IF;
                    END LOOP;
                    state <= ACS_COMPUTE;
                

WHEN ACS_COMPUTE =>
    IF time_step < ENCODED_BITS/2 THEN
        -- **FIX #1: Read bits in order starting from index 0**
        -- Frame decoder packs: input_bits_g1(0)=first_g1, input_bits_g2(0)=first_g2
        -- So we read sequentially from index 0 up
        received_symbol := input_bits_g1(time_step) & input_bits_g2(time_step);
        
        -- For each current state, find best path from two possible previous states
        FOR curr_st IN 0 TO NUM_STATES-1 LOOP
            -- Two prev states can lead here
            prev_state_for_0 := curr_st / 2;              -- Previous state with MSB=0
            prev_state_for_1 := (curr_st / 2) + 32;       -- Previous state with MSB=1
            
            -- The input bit that created curr_st is its LSB
            input_bit_used := curr_st MOD 2;
            
            -- Metric via path with previous MSB=0
            expected_symbol := compute_output(prev_state_for_0, std_logic(to_unsigned(input_bit_used, 1)(0)));
            branch_metric := hamming_distance(received_symbol, expected_symbol);
            metric_via_0 := metrics_old(prev_state_for_0) + branch_metric;
            
            -- Metric via path with previous MSB=1
            expected_symbol := compute_output(prev_state_for_1, std_logic(to_unsigned(input_bit_used, 1)(0)));
            branch_metric := hamming_distance(received_symbol, expected_symbol);
            metric_via_1 := metrics_old(prev_state_for_1) + branch_metric;
            
            -- Select better path and store decision
            IF metric_via_0 <= metric_via_1 THEN
                metrics_new(curr_st) := metric_via_0;  -- Changed to :=
                decisions(time_step)(curr_st) <= '0';  -- Came from prev_state_for_0
            ELSE
                metrics_new(curr_st) := metric_via_1;  -- Changed to :=
                decisions(time_step)(curr_st) <= '1';  -- Came from prev_state_for_1
            END IF;
        END LOOP;
        
        -- Swap buffers (now happens immediately with variables!)
        metrics_old := metrics_new;
        time_step <= time_step + 1;
        
    ELSE
        -- ACS complete, prepare for traceback
        -- Find best final state (should be state 0 after tail bits)
        min_metric := metrics_old(0);
        best_state := 0;
        FOR i IN 1 TO NUM_STATES-1 LOOP
            IF metrics_old(i) < min_metric THEN
                min_metric := metrics_old(i);
                best_state := i;
            END IF;
        END LOOP;
        
        tb_state <= best_state;
        tb_step <= time_step - 1;
        output_idx <= 0;
        state <= TRACEBACK;
    END IF;


WHEN TRACEBACK =>
    IF tb_step >= 0 THEN
        -- Output the decoded input bit (LSB of current state)
        -- tb_step counts DOWN from last to first, giving us the natural index
        out_buf(tb_step) <= std_logic(to_unsigned(tb_state MOD 2, 1)(0));
        
        -- Move to previous state based on decision
        IF decisions(tb_step)(tb_state) = '0' THEN
            tb_state <= tb_state / 2;              -- Previous state had MSB=0
        ELSE
            tb_state <= (tb_state / 2) + 32;       -- Previous state had MSB=1
        END IF;
        
        tb_step <= tb_step - 1;
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
