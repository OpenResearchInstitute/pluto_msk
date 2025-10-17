------------------------------------------------------------------------------------------------------
-- Byte to Bit De-serializer with Sync Word Insertion
------------------------------------------------------------------------------------------------------
-- Reads 8-bit bytes from FIFO and outputs one bit per symbol clock to MSK modulator
-- Automatically prepends 3-byte sync word (0xE25F35) at start of each frame
------------------------------------------------------------------------------------------------------

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.numeric_std.ALL;

ENTITY byte_to_bit_deserializer IS
    GENERIC (
        BYTE_WIDTH : NATURAL := 8;
        SYNC_WORD  : std_logic_vector(23 DOWNTO 0) := X"E25F35"  -- Barker code sync
    );
    PORT (
        -- Clock and Reset
        clk             : IN  std_logic;
        init            : IN  std_logic;
        
        -- AXIS Slave Interface (from FIFO)
        s_axis_tdata    : IN  std_logic_vector(BYTE_WIDTH-1 DOWNTO 0);
        s_axis_tvalid   : IN  std_logic;
        s_axis_tready   : OUT std_logic;
        s_axis_tlast    : IN  std_logic;
        
        -- Bit Output Interface (to MSK Modulator)
        tx_data         : OUT std_logic;
        tx_req          : IN  std_logic;
        
        -- Frame Boundary Signal
        frame_complete  : OUT std_logic   -- Pulses when frame ends (after 271 bytes total)
    );
END ENTITY byte_to_bit_deserializer;

ARCHITECTURE rtl OF byte_to_bit_deserializer IS

    -- Shift register to hold current byte
    SIGNAL shift_reg        : std_logic_vector(BYTE_WIDTH-1 DOWNTO 0);
    
    -- Bit counter (0 to 7)
    SIGNAL bit_counter      : unsigned(2 DOWNTO 0);
    
    -- Byte counter for sync word (0 to 2)
    SIGNAL sync_byte_count  : unsigned(1 DOWNTO 0);
    
    -- State machine
    TYPE state_t IS (IDLE, SENDING_SYNC, SHIFTING_DATA);
    SIGNAL state            : state_t;
    
    -- Frame boundary flag
    SIGNAL last_byte        : std_logic;
    SIGNAL ready_int        : std_logic;
    
    -- Extract sync word bytes
    CONSTANT SYNC_BYTE_0    : std_logic_vector(7 DOWNTO 0) := SYNC_WORD(23 DOWNTO 16); -- 0xE2
    CONSTANT SYNC_BYTE_1    : std_logic_vector(7 DOWNTO 0) := SYNC_WORD(15 DOWNTO 8);  -- 0x5F
    CONSTANT SYNC_BYTE_2    : std_logic_vector(7 DOWNTO 0) := SYNC_WORD(7 DOWNTO 0);   -- 0x35

BEGIN

    s_axis_tready <= ready_int;

    deserializer_proc: PROCESS(clk)
    BEGIN
        IF rising_edge(clk) THEN
            IF init = '1' THEN
                shift_reg <= (OTHERS => '0');
                bit_counter <= (OTHERS => '0');
                sync_byte_count <= (OTHERS => '0');
                state <= IDLE;
                tx_data <= '0';
                frame_complete <= '0';
                last_byte <= '0';
                ready_int <= '0';
                
            ELSE
                -- Default outputs
                frame_complete <= '0';
                
                CASE state IS
                    
                    WHEN IDLE =>
                        -- Wait for start of new frame
                        ready_int <= '1';
                        bit_counter <= (OTHERS => '0');
                        sync_byte_count <= (OTHERS => '0');
                        
                        IF s_axis_tvalid = '1' THEN
                            -- New frame starting - insert sync word first
                            shift_reg <= SYNC_BYTE_0;  -- Load first sync byte (0xE2)
                            state <= SENDING_SYNC;
                            ready_int <= '0';  -- Don't accept data yet
                        END IF;
                    
                    WHEN SENDING_SYNC =>
                        -- Shift out sync word bytes (3 bytes = 24 bits)
                        IF tx_req = '1' THEN
                            -- Output MSB first
                            tx_data <= shift_reg(BYTE_WIDTH-1);
                            shift_reg <= shift_reg(BYTE_WIDTH-2 DOWNTO 0) & '0';
                            
                            IF bit_counter = BYTE_WIDTH-1 THEN
                                -- Finished shifting current sync byte
                                bit_counter <= (OTHERS => '0');
                                
                                IF sync_byte_count = 2 THEN
                                    -- All 3 sync bytes sent, now accept data from FIFO
                                    sync_byte_count <= (OTHERS => '0');
                                    ready_int <= '1';
                                    state <= SHIFTING_DATA;
                                ELSE
                                    -- Load next sync byte
                                    sync_byte_count <= sync_byte_count + 1;
                                    
                                    CASE sync_byte_count IS
                                        WHEN "00" => shift_reg <= SYNC_BYTE_1;  -- 0x5F
                                        WHEN "01" => shift_reg <= SYNC_BYTE_2;  -- 0x35
                                        WHEN OTHERS => shift_reg <= (OTHERS => '0');
                                    END CASE;
                                END IF;
                            ELSE
                                bit_counter <= bit_counter + 1;
                            END IF;
                        END IF;
                    
                    WHEN SHIFTING_DATA =>
                        -- Accept and shift out data bytes from FIFO
                        -- Ready signal stays high until we have a byte to shift
                        IF s_axis_tvalid = '1' AND ready_int = '1' THEN
                            -- Load new byte from FIFO
                            shift_reg <= s_axis_tdata;
                            last_byte <= s_axis_tlast;
                            ready_int <= '0';  -- De-assert ready while shifting
                        END IF;
                        
                        IF tx_req = '1' AND ready_int = '0' THEN
                            -- Output MSB first
                            tx_data <= shift_reg(BYTE_WIDTH-1);
                            shift_reg <= shift_reg(BYTE_WIDTH-2 DOWNTO 0) & '0';
                            
                            IF bit_counter = BYTE_WIDTH-1 THEN
                                -- Finished shifting all 8 bits
                                bit_counter <= (OTHERS => '0');
                                
                                -- Check if this was the last byte of the frame
                                IF last_byte = '1' THEN
                                    frame_complete <= '1';
                                    last_byte <= '0';
                                    state <= IDLE;
                                ELSE
                                    -- Ready for next byte
                                    ready_int <= '1';
                                END IF;
                            ELSE
                                bit_counter <= bit_counter + 1;
                            END IF;
                        END IF;
                    
                    WHEN OTHERS =>
                        state <= IDLE;
                        
                END CASE;
            END IF;
        END IF;
    END PROCESS deserializer_proc;

END ARCHITECTURE rtl;
