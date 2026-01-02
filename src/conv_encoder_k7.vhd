------------------------------------------------------------------------------------------------------
-- K=7 Convolutional Encoder - Shift Register Version (Corrected Polynomials)
------------------------------------------------------------------------------------------------------
-- Rate 1/2, constraint length K=7
-- Generator polynomials: G1 = 171 octal, G2 = 133 octal
--
-- CRITICAL: The polynomial tap interpretation must match the original!
--   G1_POLY = "1111001" with loop using full_state(6-i) means:
--     G1 = curr_bit XOR sr(3) XOR sr(2) XOR sr(1) XOR sr(0)
--   G2_POLY = "1011011" means:
--     G2 = curr_bit XOR sr(5) XOR sr(3) XOR sr(2) XOR sr(0)
--
-- RESOURCE OPTIMIZATION:
--   Original version: ~3000 LUTs (variable bit indexing creates massive mux/demux)
--   This version: ~200-400 LUTs (shift registers, fixed-position access only)
------------------------------------------------------------------------------------------------------

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.numeric_std.ALL;

ENTITY conv_encoder_k7 IS
    GENERIC (
        PAYLOAD_BYTES  : NATURAL := 134;
        ENCODED_BYTES  : NATURAL := 268
    );
    PORT (
        clk            : IN  std_logic;
        aresetn        : IN  std_logic;
        
        start          : IN  std_logic;
        busy           : OUT std_logic;
        done           : OUT std_logic;
        
        input_buffer   : IN  std_logic_vector(PAYLOAD_BYTES*8-1 DOWNTO 0);
        output_buffer  : OUT std_logic_vector(ENCODED_BYTES*8-1 DOWNTO 0)
    );
END ENTITY conv_encoder_k7;

ARCHITECTURE rtl OF conv_encoder_k7 IS

    CONSTANT INPUT_BITS  : NATURAL := PAYLOAD_BYTES * 8;  -- 1072
    CONSTANT OUTPUT_BITS : NATURAL := ENCODED_BYTES * 8;  -- 2144

    TYPE state_t IS (IDLE, ENCODE, COMPLETE);
    SIGNAL state : state_t := IDLE;
    
    -- Input shift register - shifts MSB out first
    SIGNAL in_sr : std_logic_vector(INPUT_BITS-1 DOWNTO 0);
    
    -- Output shift register - accumulates encoded bits
    SIGNAL out_sr : std_logic_vector(OUTPUT_BITS-1 DOWNTO 0);
    
    -- Encoder shift register (6 bits of history for K=7)
    -- sr(0) = most recent previous bit, sr(5) = oldest
    SIGNAL enc_sr : std_logic_vector(5 DOWNTO 0);
    
    -- Bit counter
    SIGNAL bit_count : unsigned(10 DOWNTO 0);  -- counts 0 to 1071
    
    -- Latched output (stable while not encoding)
    SIGNAL out_latched : std_logic_vector(OUTPUT_BITS-1 DOWNTO 0);

    ATTRIBUTE dont_touch : STRING;
    ATTRIBUTE dont_touch OF in_sr : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF out_sr : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF enc_sr : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF out_latched : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF state : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF bit_count : SIGNAL IS "true";
    
    ATTRIBUTE ram_style : STRING;
    ATTRIBUTE ram_style OF in_sr : SIGNAL IS "block";
    ATTRIBUTE ram_style OF out_sr : SIGNAL IS "true";
    ATTRIBUTE ram_style OF out_latched : SIGNAL IS "block";



BEGIN

    PROCESS(clk, aresetn)
        VARIABLE curr_bit : std_logic;
        VARIABLE g1, g2   : std_logic;
    BEGIN
        IF aresetn = '0' THEN
            state <= IDLE;
            busy <= '0';
            done <= '0';
            in_sr <= (OTHERS => '0');
            out_sr <= (OTHERS => '0');
            enc_sr <= (OTHERS => '0');
            bit_count <= (OTHERS => '0');
            out_latched <= (OTHERS => '0');
            
        ELSIF rising_edge(clk) THEN
            -- Default: done is single-cycle pulse
            done <= '0';
            
            CASE state IS
            
                WHEN IDLE =>
                    busy <= '0';
                    IF start = '1' THEN
                        -- Parallel load input shift register
                        in_sr <= input_buffer;
                        out_sr <= (OTHERS => '0');
                        enc_sr <= (OTHERS => '0');
                        bit_count <= (OTHERS => '0');
                        busy <= '1';
                        state <= ENCODE;
                    END IF;
                
                WHEN ENCODE =>
                    -- Get current input bit from MSB of shift register
                    curr_bit := in_sr(INPUT_BITS - 1);
                    
                    ----------------------------------------------------------------
                    -- POLYNOMIAL COMPUTATION - Must match original exactly!
                    ----------------------------------------------------------------
                    -- Original uses: full_state = curr_bit & enc_sr
                    -- With loop: g1 XOR= full_state(6-i) when G1_POLY(i)='1'
                    --
                    -- G1_POLY = "1111001" (bits 6,5,4,3,0 are '1')
                    --   i=0: full_state(6) = curr_bit
                    --   i=3: full_state(3) = enc_sr(3)
                    --   i=4: full_state(2) = enc_sr(2)
                    --   i=5: full_state(1) = enc_sr(1)
                    --   i=6: full_state(0) = enc_sr(0)
                    -- G1 = curr_bit XOR enc_sr(3) XOR enc_sr(2) XOR enc_sr(1) XOR enc_sr(0)
                    --
                    -- G2_POLY = "1011011" (bits 6,4,3,1,0 are '1')
                    --   i=0: full_state(6) = curr_bit
                    --   i=1: full_state(5) = enc_sr(5)
                    --   i=3: full_state(3) = enc_sr(3)
                    --   i=4: full_state(2) = enc_sr(2)
                    --   i=6: full_state(0) = enc_sr(0)
                    -- G2 = curr_bit XOR enc_sr(5) XOR enc_sr(3) XOR enc_sr(2) XOR enc_sr(0)
                    ----------------------------------------------------------------
                    
                    ---------------------------------------
                    -- So You Say You Want A Duplication --
                    -- Bypass? Set g1 and g2 to curr_bit --
                    -- here. Uncomment this and comment  --
                    -- out the full g1 and g2 equation   --
                    -- to drop FEC out of the design.    --
                    -- The interleaver etc. will then    --
                    -- have the right number of bits,    --
                    -- but we won't have any FEC.        --
                    ---------------------------------------

                    --g1 := curr_bit; -- for "fake" FEC
                    --g2 := curr_bit; -- for "fake" FEC, or NOT curr_bit

                    g1 := curr_bit XOR enc_sr(3) XOR enc_sr(2) XOR enc_sr(1) XOR enc_sr(0);
                    g2 := curr_bit XOR enc_sr(5) XOR enc_sr(3) XOR enc_sr(2) XOR enc_sr(0);
                    
                    -- Update encoder shift register (shift in current bit at LSB)
                    enc_sr <= enc_sr(4 DOWNTO 0) & curr_bit;
                    
                    -- Shift input register left (next bit moves to MSB position)
                    in_sr <= in_sr(INPUT_BITS-2 DOWNTO 0) & '0';
                    
                    -- Shift output register left by 2, insert g1 and g2 at LSB
                    -- g1 goes to higher bit position (matches original out_buf indexing)
                    out_sr <= out_sr(OUTPUT_BITS-3 DOWNTO 0) & g1 & g2;
                    
                    -- Count bits processed
                    IF bit_count = INPUT_BITS - 1 THEN
                        -- All bits encoded, latch output
                        out_latched <= out_sr(OUTPUT_BITS-3 DOWNTO 0) & g1 & g2;
                        state <= COMPLETE;
                    ELSE
                        bit_count <= bit_count + 1;
                    END IF;
                
                WHEN COMPLETE =>
                    done <= '1';
                    busy <= '0';
                    state <= IDLE;
                    
            END CASE;
        END IF;
    END PROCESS;
    
    -- Output is latched value (stable during next encoding)
    output_buffer <= out_latched;

END ARCHITECTURE rtl;
