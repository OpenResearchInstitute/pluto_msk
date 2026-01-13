------------------------------------------------------------------------------------------------------
-- conv_encoder_k7.vhd
-- K=7 Rate-1/2 Convolutional Encoder (NASA/CCSDS Standard)
------------------------------------------------------------------------------------------------------
-- POSITION IN TRANSMIT CHAIN:
--
--   [ov_frame_encoder]
--        |
--        v
--   +-----------+     +-------------+     +-------------+
--   | PREP_FEC  | --> | THIS MODULE | --> | INTERLEAVE  |
--   | (pack     |     | 1072 bits   |     | (67×32 bit  |
--   |  bytes)   |     | → 2144 bits |     |  shuffle)   |
--   +-----------+     +-------------+     +-------------+
--
--   Instantiated within ov_frame_encoder as U_ENCODER.
--   Receives packed bit buffer, outputs FEC-encoded bits.
--
------------------------------------------------------------------------------------------------------
-- CONVOLUTIONAL CODE PARAMETERS
------------------------------------------------------------------------------------------------------
--   Constraint length: K = 7 (6 memory elements, 64-state trellis)
--   Code rate: 1/2 (each input bit produces 2 output bits)
--   
--   Generator polynomials (NASA/CCSDS standard, also used in 802.11):
--     G1 = 171 octal = 0x79 = 1111001 binary = x^6 + x^5 + x^4 + x^3 + 1
--     G2 = 133 octal = 0x5B = 1011011 binary = x^6 + x^4 + x^3 + x + 1
--
--   In terms of shift register taps (enc_sr[5:0], newest bit at [0]):
--     G1 = input XOR sr[3] XOR sr[2] XOR sr[1] XOR sr[0]
--     G2 = input XOR sr[5] XOR sr[3] XOR sr[2] XOR sr[0]
--
--   Output order: G1 first (MSB), then G2 (LSB) for each input bit
--
------------------------------------------------------------------------------------------------------
-- TIMING AND INTERFACE
------------------------------------------------------------------------------------------------------
--   Operation:
--     1. Assert 'start' for one clock with input_buffer valid
--     2. 'busy' goes HIGH, encoding begins
--     3. One input bit processed per clock (1072 clocks for full frame)
--     4. 'done' pulses HIGH for one clock when complete
--     5. 'output_buffer' holds result (stable until next encoding!)
--
--   Latency: 1074 clocks (1 to load, 1072 to encode, 1 to complete)
--   Throughput: One frame per 1074 clocks
--
--   At 61.44 MHz (PlutoSDR and LibreSDR): ~17.5 µs per frame
--   Frame period at 40 ms: Encoder is idle 99.96% of the time
--
------------------------------------------------------------------------------------------------------
-- IMPLEMENTATION: SHIFT REGISTER ARCHITECTURE
------------------------------------------------------------------------------------------------------
--   This implementation uses shift registers instead of indexed array access:
--
--   ORIGINAL APPROACH (resource-heavy):
--     for i in 0 to INPUT_BITS-1 loop
--       out_buf(i*2) := ...; out_buf(i*2+1) := ...;  -- Variable indexing!
--     end loop;
--   Result: ~3000 LUTs (synthesis creates massive mux/demux trees)
--
--   THIS APPROACH (resource-efficient):
--     in_sr  <= in_sr(N-2 downto 0) & '0';           -- Fixed shift
--     out_sr <= out_sr(M-3 downto 0) & g1 & g2;      -- Fixed shift
--   Result: ~200-400 LUTs (shift registers map to SRLs or BRAM)
--
--   The key insight: variable bit indexing in VHDL synthesizes to huge
--   multiplexers. Shift registers with fixed-position access are free.
--
------------------------------------------------------------------------------------------------------
-- TRELLIS TERMINATION NOTE
------------------------------------------------------------------------------------------------------
--   This encoder does NOT add explicit tail bits (6 zeros to flush the
--   encoder to the all-zeros state). The trellis is left unterminated.
--
--   For Opulent Voice, this is acceptable because:
--     1. Soft Viterbi decoder handles unterminated trellis gracefully
--     2. High SNR expected in typical amateur radio conditions
--     3. Last ~6 bits have slightly reduced protection, not guaranteed errors
--     4. Interleaver spreads any edge errors across the frame
--     5. Avoids 6-bit overhead per frame (0.5% efficiency gain)
--
--   If strict CCSDS compliance is needed, tail bits could be added by
--   padding the input buffer with 6 zeros and adjusting frame sizes,
--   but this is tricky. Adding 6 tail bits would improve FER by ~40% at
--   marginal SNR (reduces frame errors from ~1.7% to ~1.1% at BER=10^-5).
--   Requires interleaver resize (67×32 → 68×32) and frame size changes, blech.
--
------------------------------------------------------------------------------------------------------
-- RESOURCE USAGE
------------------------------------------------------------------------------------------------------
--   Shift registers: in_sr (1072 bits), out_sr (2144 bits), enc_sr (6 bits)
--   BRAM: in_sr and out_latched forced to block RAM via ram_style
--   Logic: ~200-400 LUTs for control and XOR trees (double check this)
--   
--   dont_touch attributes preserve signals for ILA debugging.
--
------------------------------------------------------------------------------------------------------
-- DEBUGGING BYPASS
------------------------------------------------------------------------------------------------------
--   For testing without FEC, uncomment lines 151-152:
--     g1 := curr_bit;
--     g2 := curr_bit;
--   This duplicates bits instead of encoding (maintains frame structure).
--   Prefer using BYPASS_FEC generic in ov_frame_encoder instead.
--
------------------------------------------------------------------------------------------------------
-- ACTIVE ACTIVE ACTIVE ACTIVE ACTIVE ACTIVE ACTIVE ACTIVE ACTIVE ACTIVE ACTIVE
-- Actively developed and tested. Part of the Opulent Voice FPGA reference design.
-- Author: Abraxas3d
-- License: CERN-OHL-S v2
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
