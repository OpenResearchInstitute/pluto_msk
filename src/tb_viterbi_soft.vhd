------------------------------------------------------------------------------------------------------
-- Testbench: Soft vs Hard Viterbi Decoder Comparison
------------------------------------------------------------------------------------------------------
-- Tests both decoders with the same input and verifies soft decoder handles
-- noisy/uncertain bits better than hard decoder.
------------------------------------------------------------------------------------------------------

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.numeric_std.ALL;
USE ieee.math_real.ALL;

ENTITY tb_viterbi_soft IS
END ENTITY tb_viterbi_soft;

ARCHITECTURE sim OF tb_viterbi_soft IS

    CONSTANT PAYLOAD_BITS : NATURAL := 134 * 8;  -- 1072
    CONSTANT ENCODED_BITS : NATURAL := 268 * 8;  -- 2144
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
    SIGNAL hard_input_g1 : std_logic_vector(ENCODED_BITS-1 DOWNTO 0);  -- 2144 bits
    SIGNAL hard_input_g2 : std_logic_vector(ENCODED_BITS-1 DOWNTO 0);  -- 2144 bits
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
    SIGNAL encoded_g1 : std_logic_vector(NUM_SYMBOLS-1 DOWNTO 0);  -- 1072 symbols
    SIGNAL encoded_g2 : std_logic_vector(NUM_SYMBOLS-1 DOWNTO 0);  -- 1072 symbols
    
    -- Error injection
    SIGNAL error_mask_g1 : std_logic_vector(NUM_SYMBOLS-1 DOWNTO 0);
    SIGNAL error_mask_g2 : std_logic_vector(NUM_SYMBOLS-1 DOWNTO 0);
    
    ----------------------------------------------------------------------------
    -- Convolutional encoder (same as TX)
    -- Outputs SEPARATE G1 and G2 streams (not interleaved)
    -- g1_out(i) and g2_out(i) are the outputs for input bit i
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
        
        -- Process MSB first (same as actual encoder)
        FOR i IN PAYLOAD_BITS-1 DOWNTO 0 LOOP
            curr_bit := data_in(i);
            
            -- G1 = 171 octal: curr_bit XOR sr(3) XOR sr(2) XOR sr(1) XOR sr(0)
            g1 := curr_bit XOR sr(3) XOR sr(2) XOR sr(1) XOR sr(0);
            
            -- G2 = 133 octal: curr_bit XOR sr(5) XOR sr(3) XOR sr(2) XOR sr(0)
            g2 := curr_bit XOR sr(5) XOR sr(3) XOR sr(2) XOR sr(0);
            
            -- Output: g1_out and g2_out are parallel streams
            -- Index 0 = first output symbol, index NUM_SYMBOLS-1 = last
            g1_out(out_idx) <= g1;
            g2_out(out_idx) <= g2;
            out_idx := out_idx + 1;
            
            -- Shift register update
            sr := sr(4 DOWNTO 0) & curr_bit;
        END LOOP;
    END PROCEDURE;
    
    ----------------------------------------------------------------------------
    -- Convert hard bit to soft value
    -- bit='0' -> soft=0 (strong zero)
    -- bit='1' -> soft=SOFT_MAX (strong one)
    ----------------------------------------------------------------------------
    FUNCTION hard_to_soft(bit : std_logic; confidence : INTEGER) 
        RETURN std_logic_vector IS
        VARIABLE soft_val : INTEGER;
    BEGIN
        IF bit = '0' THEN
            soft_val := (SOFT_MAX - confidence) / 2;  -- Low value for '0'
        ELSE
            soft_val := SOFT_MAX - (SOFT_MAX - confidence) / 2;  -- High value for '1'
        END IF;
        RETURN std_logic_vector(to_unsigned(soft_val, SOFT_WIDTH));
    END FUNCTION;
    
BEGIN

    -- Clock generation
    clk <= NOT clk AFTER CLK_PERIOD / 2;
    
    -- Hard decoder (existing)
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
    
    -- Soft decoder (new)
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
    
    -- Main test process
    stim_proc: PROCESS
        VARIABLE seed1, seed2 : INTEGER := 42;
        VARIABLE rand : REAL;
        VARIABLE hard_errors, soft_errors : INTEGER;
        VARIABLE num_injected_errors : INTEGER;
        VARIABLE error_pos : INTEGER;
        VARIABLE confidence : INTEGER;
        VARIABLE dbg_i : INTEGER;
    BEGIN
        -- Reset
        aresetn <= '0';
        WAIT FOR CLK_PERIOD * 10;
        aresetn <= '1';
        WAIT FOR CLK_PERIOD * 5;
        
        --------------------------------------------------------------------
        -- Test 1: Clean channel (no errors)
        --------------------------------------------------------------------
        REPORT "=== Test 1: Clean channel ===" SEVERITY NOTE;
        
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
        
        -- Prepare hard decoder input (no errors)
        -- Pad upper bits with zeros since hard decoder only uses lower NUM_SYMBOLS bits
        hard_input_g1 <= (ENCODED_BITS-1 DOWNTO NUM_SYMBOLS => '0') & encoded_g1;
        hard_input_g2 <= (ENCODED_BITS-1 DOWNTO NUM_SYMBOLS => '0') & encoded_g2;
        
        -- Prepare soft decoder input (high confidence, no errors)
        FOR i IN 0 TO NUM_SYMBOLS-1 LOOP
            soft_input_g1((i+1)*SOFT_WIDTH-1 DOWNTO i*SOFT_WIDTH) <= 
                hard_to_soft(encoded_g1(i), SOFT_MAX);
            soft_input_g2((i+1)*SOFT_WIDTH-1 DOWNTO i*SOFT_WIDTH) <= 
                hard_to_soft(encoded_g2(i), SOFT_MAX);
        END LOOP;
        WAIT FOR CLK_PERIOD;
        
        -- Run both decoders
        hard_start <= '1';
        soft_start <= '1';
        WAIT FOR CLK_PERIOD;
        hard_start <= '0';
        soft_start <= '0';
        
        -- Wait for completion
        WAIT UNTIL hard_done = '1' AND soft_done = '1';
        WAIT FOR CLK_PERIOD * 2;
        
        -- Check results
        hard_errors := 0;
        soft_errors := 0;
        -- Debug: show first 10 bits
        REPORT "  First 10 original bits:" SEVERITY NOTE;
        FOR dbg_i IN 0 TO 9 LOOP
            REPORT "    Bit " & INTEGER'IMAGE(dbg_i) & ": " & std_logic'image(original_data(dbg_i)) SEVERITY NOTE;
        END LOOP;
        REPORT "  First 10 hard output bits:" SEVERITY NOTE;
        FOR dbg_i IN 0 TO 9 LOOP
            REPORT "    Bit " & INTEGER'IMAGE(dbg_i) & ": " & std_logic'image(hard_output(dbg_i)) SEVERITY NOTE;
        END LOOP;
        REPORT "  First 5 encoded G1/G2:" SEVERITY NOTE;
        FOR dbg_i IN 0 TO 4 LOOP
            REPORT "    Sym " & INTEGER'IMAGE(dbg_i) & ": G1=" & std_logic'image(encoded_g1(dbg_i)) & " G2=" & std_logic'image(encoded_g2(dbg_i)) SEVERITY NOTE;
        END LOOP;
        FOR i IN 0 TO PAYLOAD_BITS-1 LOOP
            -- Decoder output(i) corresponds to original_data(PAYLOAD_BITS-1-i)
            -- because encoder processes MSB first
            IF hard_output(i) /= original_data(PAYLOAD_BITS-1-i) THEN
                hard_errors := hard_errors + 1;
            END IF;
            IF soft_output(i) /= original_data(PAYLOAD_BITS-1-i) THEN
                soft_errors := soft_errors + 1;
            END IF;
        END LOOP;
        
        REPORT "  Hard decoder errors: " & INTEGER'IMAGE(hard_errors) SEVERITY NOTE;
        REPORT "  Soft decoder errors: " & INTEGER'IMAGE(soft_errors) SEVERITY NOTE;
        REPORT "  Soft path metric: " & INTEGER'IMAGE(to_integer(unsigned(soft_path_metric))) SEVERITY NOTE;
        
        ASSERT hard_errors = 0 REPORT "Hard decoder failed clean test!" SEVERITY ERROR;
        ASSERT soft_errors = 0 REPORT "Soft decoder failed clean test!" SEVERITY ERROR;
        
        WAIT FOR CLK_PERIOD * 10;
        
        --------------------------------------------------------------------
        -- Test 2: Channel with errors (hard bits flipped)
        -- Soft decoder should outperform by using confidence info
        --------------------------------------------------------------------
        REPORT "=== Test 2: Noisy channel (5% BER) ===" SEVERITY NOTE;
        
        -- Initialize upper bits of hard decoder inputs
        hard_input_g1 <= (OTHERS => '0');
        hard_input_g2 <= (OTHERS => '0');
        
        -- Generate new random payload
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
        
        -- Inject errors and create soft values
        num_injected_errors := 0;
        FOR i IN 0 TO NUM_SYMBOLS-1 LOOP
            -- G1
            uniform(seed1, seed2, rand);
            IF rand < 0.05 THEN  -- 5% error rate
                -- Error: flip hard bit, use LOW confidence soft value
                hard_input_g1(i) <= NOT encoded_g1(i);
                -- Soft value near middle (uncertain)
                IF encoded_g1(i) = '0' THEN
                    soft_input_g1((i+1)*SOFT_WIDTH-1 DOWNTO i*SOFT_WIDTH) <= 
                        std_logic_vector(to_unsigned(SOFT_MAX/2 + 1, SOFT_WIDTH));  -- Wrong side but low confidence
                ELSE
                    soft_input_g1((i+1)*SOFT_WIDTH-1 DOWNTO i*SOFT_WIDTH) <= 
                        std_logic_vector(to_unsigned(SOFT_MAX/2 - 1, SOFT_WIDTH));  -- Wrong side but low confidence
                END IF;
                num_injected_errors := num_injected_errors + 1;
            ELSE
                -- No error: use HIGH confidence
                hard_input_g1(i) <= encoded_g1(i);
                soft_input_g1((i+1)*SOFT_WIDTH-1 DOWNTO i*SOFT_WIDTH) <= 
                    hard_to_soft(encoded_g1(i), SOFT_MAX);
            END IF;
            
            -- G2
            uniform(seed1, seed2, rand);
            IF rand < 0.05 THEN
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
        
        REPORT "  Injected " & INTEGER'IMAGE(num_injected_errors) & " channel errors" SEVERITY NOTE;
        
        -- Run both decoders
        hard_start <= '1';
        soft_start <= '1';
        WAIT FOR CLK_PERIOD;
        hard_start <= '0';
        soft_start <= '0';
        
        -- Wait for completion
        WAIT UNTIL hard_done = '1' AND soft_done = '1';
        WAIT FOR CLK_PERIOD * 2;
        
        -- Check results
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
        
        REPORT "  Hard decoder errors: " & INTEGER'IMAGE(hard_errors) SEVERITY NOTE;
        REPORT "  Soft decoder errors: " & INTEGER'IMAGE(soft_errors) SEVERITY NOTE;
        REPORT "  Soft path metric: " & INTEGER'IMAGE(to_integer(unsigned(soft_path_metric))) SEVERITY NOTE;
        
        IF soft_errors < hard_errors THEN
            REPORT "  SOFT DECODER WINS! (" & INTEGER'IMAGE(hard_errors - soft_errors) & " fewer errors)" SEVERITY NOTE;
        ELSIF soft_errors = hard_errors THEN
            REPORT "  TIE" SEVERITY NOTE;
        ELSE
            REPORT "  Hard decoder wins (unexpected)" SEVERITY WARNING;
        END IF;
        
        WAIT FOR CLK_PERIOD * 10;
        
        --------------------------------------------------------------------
        -- Test 3: High noise (10% BER)
        --------------------------------------------------------------------
        REPORT "=== Test 3: High noise (10% BER) ===" SEVERITY NOTE;
        
        -- Initialize upper bits of hard decoder inputs
        hard_input_g1 <= (OTHERS => '0');
        hard_input_g2 <= (OTHERS => '0');
        
        -- Generate new random payload
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
        
        -- Inject errors at 10% rate
        num_injected_errors := 0;
        FOR i IN 0 TO NUM_SYMBOLS-1 LOOP
            uniform(seed1, seed2, rand);
            IF rand < 0.10 THEN
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
            
            uniform(seed1, seed2, rand);
            IF rand < 0.10 THEN
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
        
        REPORT "  Injected " & INTEGER'IMAGE(num_injected_errors) & " channel errors" SEVERITY NOTE;
        
        -- Run both decoders
        hard_start <= '1';
        soft_start <= '1';
        WAIT FOR CLK_PERIOD;
        hard_start <= '0';
        soft_start <= '0';
        
        WAIT UNTIL hard_done = '1' AND soft_done = '1';
        WAIT FOR CLK_PERIOD * 2;
        
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
        
        REPORT "  Hard decoder errors: " & INTEGER'IMAGE(hard_errors) SEVERITY NOTE;
        REPORT "  Soft decoder errors: " & INTEGER'IMAGE(soft_errors) SEVERITY NOTE;
        REPORT "  Soft path metric: " & INTEGER'IMAGE(to_integer(unsigned(soft_path_metric))) SEVERITY NOTE;
        
        IF soft_errors < hard_errors THEN
            REPORT "  SOFT DECODER WINS! (" & INTEGER'IMAGE(hard_errors - soft_errors) & " fewer errors)" SEVERITY NOTE;
        ELSIF soft_errors = hard_errors THEN
            REPORT "  TIE" SEVERITY NOTE;
        ELSE
            REPORT "  Hard decoder wins (unexpected)" SEVERITY WARNING;
        END IF;
        
        WAIT FOR CLK_PERIOD * 10;
        
        REPORT "=== All tests complete ===" SEVERITY NOTE;
        std.env.stop;
        
    END PROCESS;

END ARCHITECTURE sim;
