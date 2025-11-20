------------------------------------------------------------------------------------------------------
-- K=7 Convolutional Encoder (FIXED - No Signal Timing Bugs)
------------------------------------------------------------------------------------------------------
-- Rate 1/2, constraint length K=7
-- Generator polynomials: G1 = 171 octal = 1111001 binary
--                        G2 = 133 octal = 1011011 binary
------------------------------------------------------------------------------------------------------

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.numeric_std.ALL;

ENTITY conv_encoder_k7 IS
    GENERIC (
        PAYLOAD_BYTES  : NATURAL := 134;   -- Input size in bytes
        ENCODED_BYTES  : NATURAL := 268    -- Output size in bytes (2x for rate 1/2)
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

    TYPE state_t IS (IDLE, ENCODE_DATA, FLUSH_TRELLIS, COMPLETE);
    SIGNAL state : state_t := IDLE;
    
    SIGNAL input_bit_count  : NATURAL RANGE 0 TO PAYLOAD_BYTES*8;
    SIGNAL output_bit_count : NATURAL RANGE 0 TO ENCODED_BYTES*8;
    
    CONSTANT G1_POLY : std_logic_vector(6 DOWNTO 0) := "1111001";
    CONSTANT G2_POLY : std_logic_vector(6 DOWNTO 0) := "1011011";
    
    SIGNAL out_buf : std_logic_vector(ENCODED_BYTES*8-1 DOWNTO 0);

    ATTRIBUTE ram_style : STRING;
    ATTRIBUTE ram_style OF out_buf : SIGNAL IS "block";
    
    -- Function to compute encoder outputs
    FUNCTION compute_outputs(
        current_bit : std_logic;
        shift_reg : std_logic_vector(5 DOWNTO 0)
    ) RETURN std_logic_vector IS
        VARIABLE full_state : std_logic_vector(6 DOWNTO 0);
        VARIABLE g1, g2 : std_logic;
    BEGIN
        full_state := current_bit & shift_reg;
        
        -- G1 output
        g1 := '0';
        FOR i IN 0 TO 6 LOOP
            IF G1_POLY(i) = '1' THEN
                g1 := g1 XOR full_state(6-i);
            END IF;
        END LOOP;
        
        -- G2 output
        g2 := '0';
        FOR i IN 0 TO 6 LOOP
            IF G2_POLY(i) = '1' THEN
                g2 := g2 XOR full_state(6-i);
            END IF;
        END LOOP;
        
        RETURN g1 & g2;  -- Return as 2-bit vector
    END FUNCTION;

BEGIN

    PROCESS(clk, aresetn)
        VARIABLE shift_reg : std_logic_vector(5 DOWNTO 0);
        VARIABLE current_bit : std_logic;
        VARIABLE outputs : std_logic_vector(1 DOWNTO 0);
    BEGIN
        IF aresetn = '0' THEN
            state <= IDLE;
            shift_reg := (OTHERS => '0');
            input_bit_count <= 0;
            output_bit_count <= 0;
            busy <= '0';
            done <= '0';
            out_buf <= (OTHERS => '0');
            
        ELSIF rising_edge(clk) THEN
            done <= '0';
            
            CASE state IS
            
                WHEN IDLE =>
                    busy <= '0';
                    IF start = '1' THEN
                        state <= ENCODE_DATA;
                        busy <= '1';
                        shift_reg := (OTHERS => '0');
                        input_bit_count <= 0;
                        output_bit_count <= 0;
                    END IF;
                
                WHEN ENCODE_DATA =>
                    -- Process 1,070 bits (stop 2 bits early for tail)
                    IF input_bit_count < PAYLOAD_BYTES*8 - 2 THEN
                        -- Read input bit (MSB first)
                        current_bit := input_buffer(PAYLOAD_BYTES*8 - 1 - input_bit_count);
                        
                        -- Compute outputs using current state
                        outputs := compute_outputs(current_bit, shift_reg);
                        
                        -- Store outputs (g1 first, then g2)
                        out_buf(ENCODED_BYTES*8 - 1 - output_bit_count) <= outputs(1);  -- g1
                        out_buf(ENCODED_BYTES*8 - 2 - output_bit_count) <= outputs(0);  -- g2
                        
                        -- Update shift register
                        shift_reg := shift_reg(4 DOWNTO 0) & current_bit;
                        
                        input_bit_count <= input_bit_count + 1;
                        output_bit_count <= output_bit_count + 2;
                    ELSE
                        state <= FLUSH_TRELLIS;
                        input_bit_count <= 0;
                    END IF;

                WHEN FLUSH_TRELLIS =>
                    -- Add 2 tail bits (produces 4 encoded bits)
                    IF input_bit_count < 2 THEN
                        current_bit := '0';
                        
                        -- Compute outputs
                        outputs := compute_outputs(current_bit, shift_reg);
                        
                        -- Store outputs
                        out_buf(ENCODED_BYTES*8 - 1 - output_bit_count) <= outputs(1);
                        out_buf(ENCODED_BYTES*8 - 2 - output_bit_count) <= outputs(0);
                        
                        -- Update shift register
                        shift_reg := shift_reg(4 DOWNTO 0) & '0';
                        
                        input_bit_count <= input_bit_count + 1;
                        output_bit_count <= output_bit_count + 2;
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
    
    output_buffer <= out_buf;

END ARCHITECTURE rtl;
