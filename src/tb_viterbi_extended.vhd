------------------------------------------------------------------------------------------------------
-- Testbench: Soft vs Hard Viterbi Decoder - Extended BER Testing
------------------------------------------------------------------------------------------------------
-- Tests both decoders across a range of BER levels to find breaking points.
-- Tests one full OV frame (134 bytes payload, 268 bytes encoded).
------------------------------------------------------------------------------------------------------

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.numeric_std.ALL;
USE ieee.math_real.ALL;

ENTITY tb_viterbi_extended IS
END ENTITY tb_viterbi_extended;

ARCHITECTURE sim OF tb_viterbi_extended IS

    CONSTANT PAYLOAD_BITS : NATURAL := 134 * 8;  -- 1072 bits = 1 OV frame
    CONSTANT ENCODED_BITS : NATURAL := 268 * 8;  -- 2144 bits
    CONSTANT NUM_SYMBOLS : NATURAL := ENCODED_BITS / 2;  -- 1072
    CONSTANT SOFT_WIDTH : NATURAL := 3;
    CONSTANT SOFT_MAX : NATURAL := 2**SOFT_WIDTH - 1;
    
    CONSTANT CLK_PERIOD : time := 10 ns;
    
    SIGNAL clk : std_logic := '0';
    SIGNAL aresetn : std_logic := '0';
    
    -- Hard decoder signals
    SIGNAL hard_start : std_logic := '0';
    SIGNAL hard_busy : std_logic;
    SIGNAL hard_done : std_logic;
    SIGNAL hard_input_g1 : std_logic_vector(ENCODED_BITS-1 DOWNTO 0);
    SIGNAL hard_input_g2 : std_logic_vector(ENCODED_BITS-1 DOWNTO 0);
    SIGNAL hard_output : std_logic_vector(PAYLOAD_BITS-1 DOWNTO 0);
    
    -- Soft decoder signals
    SIGNAL soft_start : std_logic := '0';
    SIGNAL soft_busy : std_logic;
    SIGNAL soft_done : std_logic;
    SIGNAL soft_input_g1 : std_logic_vector(NUM_SYMBOLS * SOFT_WIDTH - 1 DOWNTO 0);
    SIGNAL soft_input_g2 : std_logic_vector(NUM_SYMBOLS * SOFT_WIDTH - 1 DOWNTO 0);
    SIGNAL soft_output : std_logic_vector(PAYLOAD_BITS-1 DOWNTO 0);
    SIGNAL soft_path_metric : std_logic_vector(15 DOWNTO 0);
    
    -- Test data
    SIGNAL original_data : std_logic_vector(PAYLOAD_BITS-1 DOWNTO 0);
    SIGNAL encoded_g1 : std_logic_vector(NUM_SYMBOLS-1 DOWNTO 0);
    SIGNAL encoded_g2 : std_logic_vector(NUM_SYMBOLS-1 DOWNTO 0);
    
    ----------------------------------------------------------------------------
    -- Convolutional encoder
    ----------------------------------------------------------------------------
    PROCEDURE conv_encode(
        data_in : IN std_logic_vector(PAYLOAD_BITS-1 DOWNTO 0);
        SIGNAL g1_out : OUT std_logic_vector(NUM_SYMBOLS-1 DOWNTO 0);
        SIGNAL g2_out : OUT std_logic_vector(NUM_SYMBOLS-1 DOWNTO 0)
    ) IS
        VARIABLE sr : std_logic_vector(5 DOWNTO 0) := (OTHERS => '0');
        VARIABLE curr_bit : std_logic;
        VARIABLE g1, g2 : std_logic;
        VARIABLE out_idx : INTEGER;
    BEGIN
        sr := (OTHERS => '0');
        out_idx := 0;
        
        FOR i IN PAYLOAD_BITS-1 DOWNTO 0 LOOP
            curr_bit := data_in(i);
            g1 := curr_bit XOR sr(3) XOR sr(2) XOR sr(1) XOR sr(0);
            g2 := curr_bit XOR sr(5) XOR sr(3) XOR sr(2) XOR sr(0);
            g1_out(out_idx) <= g1;
            g2_out(out_idx) <= g2;
            out_idx := out_idx + 1;
            sr := sr(4 DOWNTO 0) & curr_bit;
        END LOOP;
    END PROCEDURE;
    
    FUNCTION hard_to_soft(bit : std_logic; confidence : INTEGER) 
        RETURN std_logic_vector IS
        VARIABLE soft_val : INTEGER;
    BEGIN
        IF bit = '0' THEN
            soft_val := (SOFT_MAX - confidence) / 2;
        ELSE
            soft_val := SOFT_MAX - (SOFT_MAX - confidence) / 2;
        END IF;
        RETURN std_logic_vector(to_unsigned(soft_val, SOFT_WIDTH));
    END FUNCTION;

BEGIN

    clk <= NOT clk AFTER CLK_PERIOD / 2;
    
    U_HARD : ENTITY work.viterbi_decoder_k7_simple
        GENERIC MAP (
            PAYLOAD_BITS => PAYLOAD_BITS,
            ENCODED_BITS => ENCODED_BITS,
            TRACEBACK_DEPTH => 35
        )
        PORT MAP (
            clk => clk,
            aresetn => aresetn,
            start => hard_start,
            busy => hard_busy,
            done => hard_done,
            input_bits_g1 => hard_input_g1,
            input_bits_g2 => hard_input_g2,
            output_bits => hard_output
        );
    
    U_SOFT : ENTITY work.viterbi_decoder_k7_soft
        GENERIC MAP (
            PAYLOAD_BITS => PAYLOAD_BITS,
            ENCODED_BITS => ENCODED_BITS,
            TRACEBACK_DEPTH => 35,
            SOFT_WIDTH => SOFT_WIDTH
        )
        PORT MAP (
            clk => clk,
            aresetn => aresetn,
            start => soft_start,
            busy => soft_busy,
            done => soft_done,
            input_soft_g1 => soft_input_g1,
            input_soft_g2 => soft_input_g2,
            output_bits => soft_output,
            debug_path_metric => soft_path_metric
        );
    
    stim_proc: PROCESS
        VARIABLE seed1, seed2 : INTEGER := 42;
        VARIABLE rand : REAL;
        VARIABLE hard_errors, soft_errors : INTEGER;
        VARIABLE num_injected_errors : INTEGER;
        
        -- BER levels to test (in percent * 100, so 500 = 5.00%)
        TYPE ber_array_t IS ARRAY(0 TO 11) OF INTEGER;
        CONSTANT BER_LEVELS : ber_array_t := (
            0,      -- 0% (clean)
            500,    -- 5%
            1000,   -- 10%
            1500,   -- 15%
            2000,   -- 20%
            2500,   -- 25%
            3000,   -- 30%
            3500,   -- 35%
            4000,   -- 40%
            4500,   -- 45%
            5000,   -- 50% (random)
            0       -- unused
        );
        VARIABLE ber_pct : REAL;
        VARIABLE test_num : INTEGER;
        
    BEGIN
        aresetn <= '0';
        WAIT FOR CLK_PERIOD * 10;
        aresetn <= '1';
        WAIT FOR CLK_PERIOD * 5;
        
        REPORT "================================================================" SEVERITY NOTE;
        REPORT "  Soft vs Hard Viterbi Decoder - BER Sweep Test" SEVERITY NOTE;
        REPORT "  Payload: " & INTEGER'IMAGE(PAYLOAD_BITS) & " bits (1 OV frame)" SEVERITY NOTE;
        REPORT "  Encoded: " & INTEGER'IMAGE(ENCODED_BITS) & " bits" SEVERITY NOTE;
        REPORT "  Soft width: " & INTEGER'IMAGE(SOFT_WIDTH) & " bits" SEVERITY NOTE;
        REPORT "================================================================" SEVERITY NOTE;
        
        -- Test each BER level
        FOR test_idx IN 0 TO 10 LOOP
            test_num := test_idx + 1;
            ber_pct := REAL(BER_LEVELS(test_idx)) / 10000.0;
            
            REPORT "" SEVERITY NOTE;
            REPORT "--- Test " & INTEGER'IMAGE(test_num) & ": BER = " & 
                   INTEGER'IMAGE(BER_LEVELS(test_idx)/100) & "." &
                   INTEGER'IMAGE(BER_LEVELS(test_idx) MOD 100) & "% ---" SEVERITY NOTE;
            
            -- Initialize
            hard_input_g1 <= (OTHERS => '0');
            hard_input_g2 <= (OTHERS => '0');
            
            -- Generate random payload
            FOR i IN 0 TO PAYLOAD_BITS-1 LOOP
                uniform(seed1, seed2, rand);
                IF rand > 0.5 THEN
                    original_data(i) <= '1';
                ELSE
                    original_data(i) <= '0';
                END IF;
            END LOOP;
            WAIT FOR CLK_PERIOD;
            
            -- Encode
            conv_encode(original_data, encoded_g1, encoded_g2);
            WAIT FOR CLK_PERIOD;
            
            -- Inject errors based on BER
            num_injected_errors := 0;
            FOR i IN 0 TO NUM_SYMBOLS-1 LOOP
                -- G1
                uniform(seed1, seed2, rand);
                IF rand < ber_pct THEN
                    hard_input_g1(i) <= NOT encoded_g1(i);
                    IF encoded_g1(i) = '0' THEN
                        soft_input_g1((i+1)*SOFT_WIDTH-1 DOWNTO i*SOFT_WIDTH) <= 
                            std_logic_vector(to_unsigned(SOFT_MAX/2 + 1, SOFT_WIDTH));
                    ELSE
                        soft_input_g1((i+1)*SOFT_WIDTH-1 DOWNTO i*SOFT_WIDTH) <= 
                            std_logic_vector(to_unsigned(SOFT_MAX/2 - 1, SOFT_WIDTH));
                    END IF;
                    num_injected_errors := num_injected_errors + 1;
                ELSE
                    hard_input_g1(i) <= encoded_g1(i);
                    soft_input_g1((i+1)*SOFT_WIDTH-1 DOWNTO i*SOFT_WIDTH) <= 
                        hard_to_soft(encoded_g1(i), SOFT_MAX);
                END IF;
                
                -- G2
                uniform(seed1, seed2, rand);
                IF rand < ber_pct THEN
                    hard_input_g2(i) <= NOT encoded_g2(i);
                    IF encoded_g2(i) = '0' THEN
                        soft_input_g2((i+1)*SOFT_WIDTH-1 DOWNTO i*SOFT_WIDTH) <= 
                            std_logic_vector(to_unsigned(SOFT_MAX/2 + 1, SOFT_WIDTH));
                    ELSE
                        soft_input_g2((i+1)*SOFT_WIDTH-1 DOWNTO i*SOFT_WIDTH) <= 
                            std_logic_vector(to_unsigned(SOFT_MAX/2 - 1, SOFT_WIDTH));
                    END IF;
                    num_injected_errors := num_injected_errors + 1;
                ELSE
                    hard_input_g2(i) <= encoded_g2(i);
                    soft_input_g2((i+1)*SOFT_WIDTH-1 DOWNTO i*SOFT_WIDTH) <= 
                        hard_to_soft(encoded_g2(i), SOFT_MAX);
                END IF;
            END LOOP;
            WAIT FOR CLK_PERIOD;
            
            REPORT "  Channel errors injected: " & INTEGER'IMAGE(num_injected_errors) & 
                   " / " & INTEGER'IMAGE(NUM_SYMBOLS*2) & " bits" SEVERITY NOTE;
            
            -- Run decoders
            hard_start <= '1';
            soft_start <= '1';
            WAIT FOR CLK_PERIOD;
            hard_start <= '0';
            soft_start <= '0';
            
            WAIT UNTIL hard_done = '1' AND soft_done = '1';
            WAIT FOR CLK_PERIOD * 2;
            
            -- Count errors
            hard_errors := 0;
            soft_errors := 0;
            FOR i IN 0 TO PAYLOAD_BITS-1 LOOP
                IF hard_output(i) /= original_data(PAYLOAD_BITS-1-i) THEN
                    hard_errors := hard_errors + 1;
                END IF;
                IF soft_output(i) /= original_data(PAYLOAD_BITS-1-i) THEN
                    soft_errors := soft_errors + 1;
                END IF;
            END LOOP;
            
            REPORT "  Hard decoder output errors: " & INTEGER'IMAGE(hard_errors) & 
                   " / " & INTEGER'IMAGE(PAYLOAD_BITS) SEVERITY NOTE;
            REPORT "  Soft decoder output errors: " & INTEGER'IMAGE(soft_errors) & 
                   " / " & INTEGER'IMAGE(PAYLOAD_BITS) SEVERITY NOTE;
            REPORT "  Soft path metric: " & INTEGER'IMAGE(to_integer(unsigned(soft_path_metric))) SEVERITY NOTE;
            
            IF soft_errors = 0 AND hard_errors = 0 THEN
                REPORT "  Result: BOTH PERFECT" SEVERITY NOTE;
            ELSIF soft_errors < hard_errors THEN
                REPORT "  Result: SOFT WINS by " & INTEGER'IMAGE(hard_errors - soft_errors) & " bits" SEVERITY NOTE;
            ELSIF soft_errors = hard_errors THEN
                REPORT "  Result: TIE (both have " & INTEGER'IMAGE(soft_errors) & " errors)" SEVERITY NOTE;
            ELSE
                REPORT "  Result: HARD WINS (unexpected)" SEVERITY WARNING;
            END IF;
            
            WAIT FOR CLK_PERIOD * 10;
            
        END LOOP;
        
        REPORT "" SEVERITY NOTE;
        REPORT "================================================================" SEVERITY NOTE;
        REPORT "  All BER tests complete!" SEVERITY NOTE;
        REPORT "================================================================" SEVERITY NOTE;
        
        std.env.stop;
        
    END PROCESS;

END ARCHITECTURE sim;
