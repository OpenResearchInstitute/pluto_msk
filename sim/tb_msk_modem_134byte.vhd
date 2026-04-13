--------------------------------------------------------------------------------
-- tb_msk_modem_134byte.vhd
-- Phase 2 Full MSK Modem Testbench with 134-byte OV Frames
-- Complete with modem initialization sequence
--
-- Tests complete modem with CORRECT frame sizes:
--   TX: 134 bytes -> Encoder -> 268 bytes -> Deserializer -> Modulator
--   RX: Demodulator -> Frame Sync -> 268 bytes -> Decoder -> 134 bytes
--
-- INTERLEAVER MODE: BIT-LEVEL (67x32)
--   This testbench is configured to test the bit-level interleaver which
--   provides protocol-compliant operation. The 67x32 matrix spreads bits
--   across the frame to maximize burst error correction capability.
--
--   Encoder processing time for interleave: ~2144 clocks (1 bit/clock)
--   Decoder processing time for deinterleave: ~2144 clocks (1 bit/clock)
--
-- RANDOMIZATION: CCSDS LFSR (x^8+x^7+x^5+x^3+1)
--   Pre-FEC randomization ensures bit transitions for clock recovery.
--   This is a standard technique from CCSDS (Consultative Committee for
--   Space Data Systems).
--
-- TX DATA PATTERN:
--   byte_val = (frame_idx * 128 + byte_idx) MOD 256
--   Frame 0: 0x00 -> 0x85  (even frames all the same)
--   Frame 1: 0x80 -> 0x05  (odd frames all the same, wraps)
--   Alternates every frame. 10 frames total = 5 of each type.
--
-- Frame Timing:
--   - 10 frames total
--   - 5ms gap between frames (intentional backpressure test)
--   - Each frame takes ~40ms to transmit serially
--   - Total test time: ~500ms
--
-- Expected Behavior:
--   - Input frames arrive in 50ms (10 x 5ms)
--   - TX FIFO absorbs the burst
--   - Encoder processes quickly, outputs to deserializer
--   - Deserializer creates backpressure (tready LOW)
--   - Frames transmit serially over ~400ms (10 x 40ms)
--   - RX path receives all frames
--   - ALL 10 frames should match input data
--
-- This is CORRECT behavior - system handling backpressure properly!
--------------------------------------------------------------------------------

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.numeric_std.ALL;
USE ieee.std_logic_textio.ALL;
USE std.textio.ALL;

ENTITY tb_msk_modem_134byte IS
END ENTITY tb_msk_modem_134byte;

ARCHITECTURE behavior OF tb_msk_modem_134byte IS

    -- Component declaration (matches actual msk_top)
    COMPONENT msk_top IS
        GENERIC (
            S_AXIS_DATA_W : NATURAL := 32
        );
        PORT (
            -- Single clock (61.44 MHz)
            clk               : IN  std_logic;
            
            -- AXI-Lite (NOW PROPERLY CONNECTED!)
            s_axi_aclk        : IN  std_logic;
            s_axi_aresetn     : IN  std_logic;
            s_axi_awaddr      : IN  std_logic_vector(31 DOWNTO 0);
            s_axi_awvalid     : IN  std_logic;
            s_axi_wdata       : IN  std_logic_vector(31 DOWNTO 0);
            s_axi_wstrb       : IN  std_logic_vector(3 DOWNTO 0);
            s_axi_wvalid      : IN  std_logic;
            s_axi_bready      : IN  std_logic;
            s_axi_araddr      : IN  std_logic_vector(31 DOWNTO 0);
            s_axi_arvalid     : IN  std_logic;
            s_axi_rready      : IN  std_logic;
            s_axi_arready     : OUT std_logic;
            s_axi_rdata       : OUT std_logic_vector(31 DOWNTO 0);
            s_axi_rresp       : OUT std_logic_vector(1 DOWNTO 0);
            s_axi_rvalid      : OUT std_logic;
            s_axi_wready      : OUT std_logic;
            s_axi_bresp       : OUT std_logic_vector(1 DOWNTO 0);
            s_axi_bvalid      : OUT std_logic;
            s_axi_awready     : OUT std_logic;
            s_axi_awprot      : IN  std_logic_vector(2 DOWNTO 0);
            s_axi_arprot      : IN  std_logic_vector(2 DOWNTO 0);
            
            -- TX AXI-Stream (from PS) - 32-bit wide!
            s_axis_aresetn    : IN  std_logic;
            s_axis_aclk       : IN  std_logic;
            m_axis_aclk       : IN  std_logic;  -- RX output clock (sys_cpu_clk)
            s_axis_tvalid     : IN  std_logic;
            s_axis_tready     : OUT std_logic;
            s_axis_tdata      : IN  std_logic_vector(31 DOWNTO 0);
            s_axis_tlast      : IN  std_logic;
            s_axis_tkeep      : IN  std_logic_vector(3 DOWNTO 0);
            
            -- TX control
            tx_enable         : IN  std_logic;
            tx_valid          : IN  std_logic;
            tx_samples_I      : OUT std_logic_vector(15 DOWNTO 0);
            tx_samples_Q      : OUT std_logic_vector(15 DOWNTO 0);
            
            -- RX control
            rx_enable         : IN  std_logic;
            rx_svalid         : IN  std_logic;
            rx_samples_I      : IN  std_logic_vector(15 DOWNTO 0);
            rx_samples_Q      : IN  std_logic_vector(15 DOWNTO 0);
            
            -- RX AXI-Stream (to PS) - 32-bit wide!
            m_axis_tdata      : OUT std_logic_vector(31 DOWNTO 0);
            m_axis_tvalid     : OUT std_logic;
            m_axis_tready     : IN  std_logic;
            m_axis_tlast      : OUT std_logic;
            
            -- Status outputs
            frame_sync_locked     : OUT std_logic;
            frames_received       : OUT std_logic_vector(31 DOWNTO 0);
            frame_sync_errors     : OUT std_logic_vector(31 DOWNTO 0);
            frame_buffer_overflow : OUT std_logic
        );
    END COMPONENT msk_top;

    -- Constants
    CONSTANT CLK_PERIOD     : TIME := 16.276 ns;   -- 61.44 MHz (single clock)
    
    CONSTANT FRAME_BYTES    : NATURAL := 134;     -- OV payload size
    CONSTANT NUM_FRAMES     : NATURAL := 10;      -- Test 10 frames (5 even + 5 odd pattern)
    CONSTANT FRAME_GAP      : TIME := 5 ms;       -- Intentional backpressure test
    
    -- MSK Register Addresses (from working testbench!)
    CONSTANT MSK_INIT_ADDR          : std_logic_vector(31 DOWNTO 0) := X"43C00008";
    CONSTANT MSK_CONTROL_ADDR       : std_logic_vector(31 DOWNTO 0) := X"43C0000C";
    CONSTANT FB_FREQWORD_ADDR       : std_logic_vector(31 DOWNTO 0) := X"43C0001C";
    CONSTANT TX_F1_FREQWORD_ADDR    : std_logic_vector(31 DOWNTO 0) := X"43C00020";
    CONSTANT TX_F2_FREQWORD_ADDR    : std_logic_vector(31 DOWNTO 0) := X"43C00024";
    CONSTANT RX_F1_FREQWORD_ADDR    : std_logic_vector(31 DOWNTO 0) := X"43C00028";
    CONSTANT RX_F2_FREQWORD_ADDR    : std_logic_vector(31 DOWNTO 0) := X"43C0002C";
    CONSTANT LPF_CONFIG_0_ADDR      : std_logic_vector(31 DOWNTO 0) := X"43C00030";
    CONSTANT LPF_CONFIG_1_ADDR      : std_logic_vector(31 DOWNTO 0) := X"43C00034";
    CONSTANT LPF_CONFIG_2_ADDR      : std_logic_vector(31 DOWNTO 0) := X"43C00068";
    CONSTANT RX_SAMPLE_DISCARD_ADDR : std_logic_vector(31 DOWNTO 0) := X"43C00064";
    CONSTANT TX_DATA_WIDTH_ADDR     : std_logic_vector(31 DOWNTO 0) := X"43C00038";
    CONSTANT RX_DATA_WIDTH_ADDR     : std_logic_vector(31 DOWNTO 0) := X"43C0003C";
    CONSTANT SYMBOL_LOCK_CTRL_ADDR  : std_logic_vector(31 DOWNTO 0) := X"43C000A0";
    
    -- Clock and reset
    SIGNAL clk        : std_logic := '0';
    SIGNAL sim_done   : std_logic := '0';
    
    -- AXI-Lite signals
    SIGNAL s_axi_aclk     : std_logic;
    SIGNAL s_axi_aresetn  : std_logic := '0';
    SIGNAL s_axi_awaddr   : std_logic_vector(31 DOWNTO 0) := (OTHERS => '0');
    SIGNAL s_axi_awvalid  : std_logic := '0';
    SIGNAL s_axi_wdata    : std_logic_vector(31 DOWNTO 0) := (OTHERS => '0');
    SIGNAL s_axi_wstrb    : std_logic_vector(3 DOWNTO 0) := (OTHERS => '1');
    SIGNAL s_axi_wvalid   : std_logic := '0';
    SIGNAL s_axi_bready   : std_logic := '1';
    SIGNAL s_axi_araddr   : std_logic_vector(31 DOWNTO 0) := (OTHERS => '0');
    SIGNAL s_axi_arvalid  : std_logic := '0';
    SIGNAL s_axi_rready   : std_logic := '1';
    SIGNAL s_axi_arready  : std_logic;
    SIGNAL s_axi_rdata    : std_logic_vector(31 DOWNTO 0);
    SIGNAL s_axi_rresp    : std_logic_vector(1 DOWNTO 0);
    SIGNAL s_axi_rvalid   : std_logic;
    SIGNAL s_axi_wready   : std_logic;
    SIGNAL s_axi_bresp    : std_logic_vector(1 DOWNTO 0);
    SIGNAL s_axi_bvalid   : std_logic;
    SIGNAL s_axi_awready  : std_logic;
    SIGNAL s_axi_awprot   : std_logic_vector(2 DOWNTO 0) := (OTHERS => '0');
    SIGNAL s_axi_arprot   : std_logic_vector(2 DOWNTO 0) := (OTHERS => '0');
    
    -- TX AXI-Stream (testbench -> DUT) - 32-bit interface!
    SIGNAL s_axis_aresetn : std_logic := '0';
    SIGNAL s_axis_aclk    : std_logic;
    SIGNAL m_axis_aclk    : std_logic;  -- RX output clock
    SIGNAL s_axis_tvalid  : std_logic := '0';
    SIGNAL s_axis_tready  : std_logic;
    SIGNAL s_axis_tdata   : std_logic_vector(31 DOWNTO 0) := (OTHERS => '0');
    SIGNAL s_axis_tlast   : std_logic := '0';
    SIGNAL s_axis_tkeep   : std_logic_vector(3 DOWNTO 0) := "1111";
    
    -- RX AXI-Stream (DUT -> testbench) - 32-bit interface!
    SIGNAL m_axis_tvalid : std_logic;
    SIGNAL m_axis_tready : std_logic := '1';  -- Always ready
    SIGNAL m_axis_tdata  : std_logic_vector(31 DOWNTO 0);
    SIGNAL m_axis_tlast  : std_logic;
    
    -- IQ samples (loopback)
    SIGNAL tx_samples_I : std_logic_vector(15 DOWNTO 0);
    SIGNAL tx_samples_Q : std_logic_vector(15 DOWNTO 0);
    SIGNAL rx_samples_I : std_logic_vector(15 DOWNTO 0);
    SIGNAL rx_samples_Q : std_logic_vector(15 DOWNTO 0);
    
    -- Control signals
    SIGNAL tx_enable : std_logic := '1';
    SIGNAL tx_valid  : std_logic := '1';
    SIGNAL rx_enable : std_logic := '1';
    SIGNAL rx_svalid : std_logic := '1';
    
    -- Status signals
    SIGNAL frame_sync_locked     : std_logic;
    SIGNAL frames_received       : std_logic_vector(31 DOWNTO 0);
    SIGNAL frame_sync_errors     : std_logic_vector(31 DOWNTO 0);
    SIGNAL frame_buffer_overflow : std_logic;
    
    -- Test data storage
    TYPE frame_data_t IS ARRAY(0 TO FRAME_BYTES-1) OF std_logic_vector(7 DOWNTO 0);
    TYPE all_frames_t IS ARRAY(0 TO NUM_FRAMES-1) OF frame_data_t;
    
    SIGNAL tx_frames : all_frames_t;  -- What we sent
    SIGNAL rx_frames : all_frames_t;  -- What we received
    
    -- Test control
    SIGNAL tx_frame_count : NATURAL := 0;
    SIGNAL rx_frame_count : NATURAL := 0;
    SIGNAL test_complete  : BOOLEAN := FALSE;
    SIGNAL start_sending  : std_logic := '0';  -- Gate for TX stimulus
    
    -- Test phase tracking
    SIGNAL test_phase : STRING(1 TO 30) := "INITIALIZATION                ";

    ---------------------------------------------------------------------------
    -- AXI-Lite Write Procedure
    ---------------------------------------------------------------------------
    PROCEDURE axi_write(
        SIGNAL awaddr   : OUT std_logic_vector(31 DOWNTO 0);
        SIGNAL awvalid  : OUT std_logic;
        SIGNAL wdata    : OUT std_logic_vector(31 DOWNTO 0);
        SIGNAL wvalid   : OUT std_logic;
        SIGNAL aclk     : IN  std_logic;
        SIGNAL awready  : IN  std_logic;
        SIGNAL wready   : IN  std_logic;
        SIGNAL bvalid   : IN  std_logic;
        addr : std_logic_vector(31 DOWNTO 0);
        data : std_logic_vector(31 DOWNTO 0)
    ) IS
    BEGIN
        awaddr <= addr;
        awvalid <= '1';
        wdata <= data;
        wvalid <= '1';
        WAIT UNTIL rising_edge(aclk) AND (awready = '1' OR wready = '1');
        WAIT UNTIL rising_edge(aclk) AND awready = '1' AND wready = '1';
        awvalid <= '0';
        wvalid <= '0';
        WAIT UNTIL rising_edge(aclk) AND bvalid = '1';
        WAIT FOR 1 ns;
    END PROCEDURE;

BEGIN

    -- Clock generation (all buses use same clock for loopback test)
    clk <= NOT clk AFTER CLK_PERIOD / 2 WHEN sim_done = '0' ELSE '0';
    s_axi_aclk <= clk;
    s_axis_aclk <= clk;
    m_axis_aclk <= clk;  -- RX output uses same clock in loopback

    -- RF loopback (TX -> RX, perfect channel)
    -- DAC sees [15:4], ADC outputs 12-bit right-justified
    rx_svalid    <= tx_enable AND tx_valid;
    rx_samples_I <= std_logic_vector(resize(signed(tx_samples_I(15 DOWNTO 4)), 16));
    rx_samples_Q <= std_logic_vector(resize(signed(tx_samples_Q(15 DOWNTO 4)), 16));

    -- Instantiate DUT
    DUT: msk_top
        GENERIC MAP (
            S_AXIS_DATA_W => 32
        )
        PORT MAP (
            clk                   => clk,
            s_axi_aclk            => s_axi_aclk,
            s_axi_aresetn         => s_axi_aresetn,
            s_axi_awaddr          => s_axi_awaddr,
            s_axi_awvalid         => s_axi_awvalid,
            s_axi_wdata           => s_axi_wdata,
            s_axi_wstrb           => s_axi_wstrb,
            s_axi_wvalid          => s_axi_wvalid,
            s_axi_bready          => s_axi_bready,
            s_axi_araddr          => s_axi_araddr,
            s_axi_arvalid         => s_axi_arvalid,
            s_axi_rready          => s_axi_rready,
            s_axi_arready         => s_axi_arready,
            s_axi_rdata           => s_axi_rdata,
            s_axi_rresp           => s_axi_rresp,
            s_axi_rvalid          => s_axi_rvalid,
            s_axi_wready          => s_axi_wready,
            s_axi_bresp           => s_axi_bresp,
            s_axi_bvalid          => s_axi_bvalid,
            s_axi_awready         => s_axi_awready,
            s_axi_awprot          => s_axi_awprot,
            s_axi_arprot          => s_axi_arprot,
            s_axis_aresetn        => s_axis_aresetn,
            s_axis_aclk           => s_axis_aclk,
            m_axis_aclk           => m_axis_aclk,
            s_axis_tvalid         => s_axis_tvalid,
            s_axis_tready         => s_axis_tready,
            s_axis_tdata          => s_axis_tdata,
            s_axis_tlast          => s_axis_tlast,
            s_axis_tkeep          => s_axis_tkeep,
            tx_enable             => tx_enable,
            tx_valid              => tx_valid,
            tx_samples_I          => tx_samples_I,
            tx_samples_Q          => tx_samples_Q,
            rx_enable             => rx_enable,
            rx_svalid             => rx_svalid,
            rx_samples_I          => rx_samples_I,
            rx_samples_Q          => rx_samples_Q,
            m_axis_tdata          => m_axis_tdata,
            m_axis_tvalid         => m_axis_tvalid,
            m_axis_tready         => m_axis_tready,
            m_axis_tlast          => m_axis_tlast,
            frame_sync_locked     => frame_sync_locked,
            frames_received       => frames_received,
            frame_sync_errors     => frame_sync_errors,
            frame_buffer_overflow => frame_buffer_overflow
        );

    ---------------------------------------------------------------------------
    -- RESET GENERATION
    ---------------------------------------------------------------------------
    reset_gen: PROCESS
    BEGIN
        s_axi_aresetn <= '0';
        s_axis_aresetn <= '0';
        WAIT FOR 200 ns;
        s_axi_aresetn <= '1';
        s_axis_aresetn <= '1';
        WAIT;
    END PROCESS;

    ---------------------------------------------------------------------------
    -- TEST CONTROLLER
    ---------------------------------------------------------------------------
    test_controller: PROCESS
        VARIABLE errors : NATURAL := 0;
        VARIABLE byte_match : BOOLEAN;
    BEGIN
        WAIT UNTIL s_axi_aresetn = '1';
        WAIT FOR 500 ns;
        
        REPORT "========================================";
        REPORT "MSK MODEM INITIALIZATION";
        REPORT "INTERLEAVER MODE: BIT-LEVEL (67x32)";
        REPORT "DECORRELATION: CCSDS LFSR (spur fix)";
        REPORT "FRAMES: " & INTEGER'IMAGE(NUM_FRAMES) & " (alternating 0x00->0x85 / 0x80->0x05)";
        REPORT "========================================";
        
        test_phase <= "MSK_INITIALIZATION            ";
        
        REPORT "Step 1: Asserting MSK reset...";
        axi_write(s_axi_awaddr, s_axi_awvalid, s_axi_wdata, s_axi_wvalid,
                  s_axi_aclk, s_axi_awready, s_axi_wready, s_axi_bvalid,
                  MSK_INIT_ADDR, X"00000001");
        WAIT FOR 500 ns;
        
        REPORT "Step 2: Configuring NCO frequencies...";
        axi_write(s_axi_awaddr, s_axi_awvalid, s_axi_wdata, s_axi_wvalid,
                  s_axi_aclk, s_axi_awready, s_axi_wready, s_axi_bvalid,
                  FB_FREQWORD_ADDR, X"0039D037");
        axi_write(s_axi_awaddr, s_axi_awvalid, s_axi_wdata, s_axi_wvalid,
                  s_axi_aclk, s_axi_awready, s_axi_wready, s_axi_bvalid,
                  TX_F1_FREQWORD_ADDR, X"01C00DA7");
        axi_write(s_axi_awaddr, s_axi_awvalid, s_axi_wdata, s_axi_wvalid,
                  s_axi_aclk, s_axi_awready, s_axi_wready, s_axi_bvalid,
                  TX_F2_FREQWORD_ADDR, X"01DCF5C3");
        axi_write(s_axi_awaddr, s_axi_awvalid, s_axi_wdata, s_axi_wvalid,
                  s_axi_aclk, s_axi_awready, s_axi_wready, s_axi_bvalid,
                  RX_F1_FREQWORD_ADDR, X"01C00DA7");
        axi_write(s_axi_awaddr, s_axi_awvalid, s_axi_wdata, s_axi_wvalid,
                  s_axi_aclk, s_axi_awready, s_axi_wready, s_axi_bvalid,
                  RX_F2_FREQWORD_ADDR, X"01DCF5C3");
        
        REPORT "Step 3: Configuring PI loop filters...";
        axi_write(s_axi_awaddr, s_axi_awvalid, s_axi_wdata, s_axi_wvalid,
                  s_axi_aclk, s_axi_awready, s_axi_wready, s_axi_bvalid,
                  LPF_CONFIG_0_ADDR, X"00000000");
        axi_write(s_axi_awaddr, s_axi_awvalid, s_axi_wdata, s_axi_wvalid,
                  s_axi_aclk, s_axi_awready, s_axi_wready, s_axi_bvalid,
                  LPF_CONFIG_1_ADDR, X"1D7FFFFF");  -- i_shift 27 to 29 or 4x
                  --LPF_CONFIG_1_ADDR, X"1E7FFFFF");  -- i_shift 27 to 30 or 8x converged at 25
                  --LPF_CONFIG_1_ADDR, X"1F7FFFFF"); -- 16x to match tx power correction converged at 35
        axi_write(s_axi_awaddr, s_axi_awvalid, s_axi_wdata, s_axi_wvalid,
                  s_axi_aclk, s_axi_awready, s_axi_wready, s_axi_bvalid,
                  LPF_CONFIG_2_ADDR, X"147FFFFF");  -- p_shift 18 to 20 or 4x 
                  --LPF_CONFIG_2_ADDR, X"157FFFFF");  -- p_shift 18 to 21 or 8x converged at 25
                  --LPF_CONFIG_2_ADDR, X"167FFFFF"); -- 16x to match tx power correction converged at 35

        axi_write(s_axi_awaddr, s_axi_awvalid, s_axi_wdata, s_axi_wvalid,
                  s_axi_aclk, s_axi_awready, s_axi_wready, s_axi_bvalid,
                  SYMBOL_LOCK_CTRL_ADDR, X"002EE010"); -- threshold 3000 count 16 
        
        REPORT "Step 4: Configuring RX sample decimation...";
        axi_write(s_axi_awaddr, s_axi_awvalid, s_axi_wdata, s_axi_wvalid,
                  s_axi_aclk, s_axi_awready, s_axi_wready, s_axi_bvalid,
                  RX_SAMPLE_DISCARD_ADDR, X"00001818");
        
        REPORT "Step 5: Configuring data widths...";
        axi_write(s_axi_awaddr, s_axi_awvalid, s_axi_wdata, s_axi_wvalid,
                  s_axi_aclk, s_axi_awready, s_axi_wready, s_axi_bvalid,
                  TX_DATA_WIDTH_ADDR, X"00000008");
        axi_write(s_axi_awaddr, s_axi_awvalid, s_axi_wdata, s_axi_wvalid,
                  s_axi_aclk, s_axi_awready, s_axi_wready, s_axi_bvalid,
                  RX_DATA_WIDTH_ADDR, X"00000008");
        
        REPORT "Step 6: Enabling PTT...";
        axi_write(s_axi_awaddr, s_axi_awvalid, s_axi_wdata, s_axi_wvalid,
                  s_axi_aclk, s_axi_awready, s_axi_wready, s_axi_bvalid,
                  MSK_CONTROL_ADDR, X"00000401");
        
        REPORT "Step 7: Releasing MSK reset...";
        axi_write(s_axi_awaddr, s_axi_awvalid, s_axi_wdata, s_axi_wvalid,
                  s_axi_aclk, s_axi_awready, s_axi_wready, s_axi_bvalid,
                  MSK_INIT_ADDR, X"00000000");
        
        WAIT FOR 2 us;
        
        REPORT "========================================";
        REPORT "MSK MODEM INITIALIZATION COMPLETE!";
        REPORT "Using BIT-LEVEL interleaver (67x32)";
        REPORT "Using CCSDS LFSR decorrelation";
        REPORT "========================================";
        REPORT "";
        
        test_phase <= "READY_FOR_TX                  ";
        start_sending <= '1';
        
        WAIT UNTIL tx_frame_count = NUM_FRAMES;
        WAIT FOR 1 us;
        
        test_phase <= "TX_COMPLETE_WAITING_RX        ";
        
        FOR i IN 0 TO 6000 LOOP  -- 600ms timeout (10 frames x ~40ms + margin)
            WAIT FOR 100 us;
            IF rx_frame_count >= NUM_FRAMES THEN
                EXIT;
            END IF;
        END LOOP;
        
        WAIT FOR 1 ms;
        
        test_phase <= "TEST_COMPLETE                 ";
        
        REPORT "========================================";
        REPORT "TEST COMPLETE - VERIFICATION";
        REPORT "========================================";
        REPORT "TX Frames Sent:     " & INTEGER'IMAGE(tx_frame_count);
        REPORT "RX Frames Received: " & INTEGER'IMAGE(rx_frame_count);
        REPORT "Frame Sync Locked:  " & std_logic'IMAGE(frame_sync_locked);
        REPORT "";
        
        errors := 0;
        FOR frame_idx IN 0 TO NUM_FRAMES-1 LOOP
            REPORT "Verifying Frame " & INTEGER'IMAGE(frame_idx) & "...";
            
            FOR byte_idx IN 0 TO FRAME_BYTES-1 LOOP
                byte_match := (tx_frames(frame_idx)(byte_idx) = rx_frames(frame_idx)(byte_idx));
                
                IF NOT byte_match THEN
                    REPORT "  ERROR at byte " & INTEGER'IMAGE(byte_idx) & 
                           ": Expected 0x" & to_hstring(tx_frames(frame_idx)(byte_idx)) &
                           ", Got 0x" & to_hstring(rx_frames(frame_idx)(byte_idx))
                           SEVERITY error;
                    errors := errors + 1;
                    IF errors MOD 10 = 0 THEN
                        REPORT "  (Suppressing further errors...)" SEVERITY note;
                        EXIT;
                    END IF;
                END IF;
            END LOOP;
        END LOOP;
        
        REPORT "";
        REPORT "========================================";
        REPORT "FINAL RESULTS";
        REPORT "========================================";
        REPORT "Frames Sent:     " & INTEGER'IMAGE(tx_frame_count);
        REPORT "Frames Received: " & INTEGER'IMAGE(rx_frame_count);
        REPORT "Total Errors:    " & INTEGER'IMAGE(errors);
        
        IF errors = 0 AND rx_frame_count = NUM_FRAMES THEN
            REPORT "*** SUCCESS! All " & INTEGER'IMAGE(NUM_FRAMES) &
                   " frames transmitted and verified! ***";
        ELSIF rx_frame_count < NUM_FRAMES THEN
            REPORT "*** INCOMPLETE! Only " & INTEGER'IMAGE(rx_frame_count) & 
                   " of " & INTEGER'IMAGE(NUM_FRAMES) & " frames received ***";
        ELSE
            REPORT "*** FAILURE! " & INTEGER'IMAGE(errors) & " byte mismatches detected ***";
        END IF;
        
        test_complete <= TRUE;
        sim_done <= '1';
        WAIT;
    END PROCESS;

    ---------------------------------------------------------------------------
    -- TX STIMULUS (32-bit AXI-Stream, ONE BYTE per transfer)
    ---------------------------------------------------------------------------
    tx_stimulus: PROCESS
        VARIABLE byte_val : NATURAL;
    BEGIN
        WAIT UNTIL start_sending = '1';
        WAIT FOR 100 ns;
        
        REPORT "========================================";
        REPORT "MSK MODEM TEST: 134-byte OV Frames";
        REPORT "Sending " & INTEGER'IMAGE(NUM_FRAMES) & " frames";
        REPORT "Frame size: " & INTEGER'IMAGE(FRAME_BYTES) & " bytes";
        REPORT "Pattern: (frame*128 + byte) mod 256";
        REPORT "  Even frames: 0x00 -> 0x85";
        REPORT "  Odd  frames: 0x80 -> 0x05 (wraps)";
        REPORT "Frame gap: 5ms (backpressure test)";
        REPORT "========================================";
        
        FOR frame_idx IN 0 TO NUM_FRAMES-1 LOOP
            REPORT "Sending Frame " & INTEGER'IMAGE(frame_idx) &
                   " (starts at 0x" &
                   to_hstring(std_logic_vector(to_unsigned((frame_idx*128) MOD 256, 8))) & ")";
            
            FOR byte_idx IN 0 TO FRAME_BYTES-1 LOOP
                byte_val := (frame_idx * 128 + byte_idx) MOD 256;
                tx_frames(frame_idx)(byte_idx) <= std_logic_vector(to_unsigned(byte_val, 8));
                
                s_axis_tdata(7 DOWNTO 0)  <= std_logic_vector(to_unsigned(byte_val, 8));
                s_axis_tdata(31 DOWNTO 8) <= (OTHERS => '0');
                s_axis_tvalid <= '1';
                s_axis_tkeep  <= "1111";
                
                IF byte_idx = FRAME_BYTES - 1 THEN
                    s_axis_tlast <= '1';
                ELSE
                    s_axis_tlast <= '0';
                END IF;
                
                WAIT UNTIL rising_edge(clk) AND s_axis_tready = '1';
            END LOOP;
            
            s_axis_tvalid <= '0';
            s_axis_tlast  <= '0';
            tx_frame_count <= tx_frame_count + 1;
            
            REPORT "Frame " & INTEGER'IMAGE(frame_idx) & " sent";
            
            IF frame_idx < NUM_FRAMES - 1 THEN
                WAIT FOR FRAME_GAP;
            END IF;
        END LOOP;
        
        REPORT "All " & INTEGER'IMAGE(NUM_FRAMES) & " frames transmitted. Waiting for RX...";
        WAIT;
    END PROCESS tx_stimulus;

    ---------------------------------------------------------------------------
    -- RX RECEIVER (32-bit AXI-Stream, lowest 8 bits per transfer)
    ---------------------------------------------------------------------------
    rx_receiver: PROCESS(clk)
        VARIABLE byte_idx  : NATURAL := 0;
        VARIABLE frame_idx : NATURAL := 0;
    BEGIN
        IF rising_edge(clk) THEN
            IF s_axis_aresetn = '0' THEN
                byte_idx  := 0;
                frame_idx := 0;
                rx_frame_count <= 0;
                
            ELSIF m_axis_tvalid = '1' AND m_axis_tready = '1' THEN
                IF frame_idx < NUM_FRAMES AND byte_idx < FRAME_BYTES THEN
                    rx_frames(frame_idx)(byte_idx) <= m_axis_tdata(7 DOWNTO 0);
                    
                    -- Report first 4 bytes of each frame for quick sanity check
                    IF byte_idx < 4 THEN
                        REPORT "RX Frame " & INTEGER'IMAGE(frame_idx) &
                               " Byte[" & INTEGER'IMAGE(byte_idx) & "]" &
                               " = 0x" & to_hstring(m_axis_tdata(7 DOWNTO 0));
                    END IF;
                    
                    byte_idx := byte_idx + 1;
                END IF;
                
                IF m_axis_tlast = '1' THEN
                    REPORT "RX Frame " & INTEGER'IMAGE(frame_idx) &
                           " complete (" & INTEGER'IMAGE(byte_idx) & " bytes)";
                    frame_idx      := frame_idx + 1;
                    rx_frame_count <= frame_idx;
                    byte_idx       := 0;
                END IF;
            END IF;
        END IF;
    END PROCESS rx_receiver;

END ARCHITECTURE behavior;
