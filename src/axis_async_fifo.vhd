------------------------------------------------------------------------------------------------------
-- AXIS-Compliant Asynchronous FIFO
------------------------------------------------------------------------------------------------------
-- Role in the Data Path:
--   Clock domain crossing buffer between the PS/DMA clock domain and the symbol
--   clock domain. Absorbs timing differences and provides elasticity between
--   bursty DMA transfers and steady symbol-rate consumption by the modulator (TX)
--   or bursty decoder output and steady DMA consumption (RX).
--
--   Think of it as a dimensional portal between two parts of the D&D dungeon that
--   run on different initiative counts. Data goes in on one clock, comes out on
--   another, and the FIFO keeps everyone synchronized.
--
-- Clock Domains:
--   wr_aclk     - Write side (e.g., PS AXI clock at 245 MHz for TX path)
--   rd_aclk     - Read side (e.g., symbol clock derived from sample rate)
--   status_aclk - Status capture domain for debug/monitoring (typically AXI clock)
--
-- CDC Strategy:
--   Gray-coded pointers with 2-stage synchronizers provide metastability protection
--   when passing pointer values between clock domains. Gray code ensures only one
--   bit changes per increment, so a metastable sample can only be off by one.
--
--   FIX v4 adds a registered stage AFTER Gray-to-binary conversion to break
--   critical timing paths at high frequencies. This adds one cycle of latency
--   to empty/full detection, which is safe given FIFO depth and inherent CDC
--   latency (pointers are already 2+ cycles stale from synchronizers).
--
-- Memory Structure:
--   Dual-port Block RAM inferred from separate arrays:
--     ram_data[DEPTH] - Payload bytes (DATA_WIDTH bits each)
--     ram_last[DEPTH] - TLAST flags (1 bit each, stored alongside data)
--
--   TLAST is stored per-entry to preserve frame boundaries through the FIFO.
--   When a byte with TLAST='1' is written, that flag travels with it and
--   emerges on m_axis_tlast when that byte is read.
--
-- Write Side Behavior:
--   Accepts data via AXI-Stream slave interface (s_axis_*).
--   Backpressure via s_axis_tready:
--     - tready='1': FIFO can accept data
--     - tready='0': FIFO is full or nearly full (prog_full asserted)
--
--   If upstream respects tready, overflow cannot occur. The design relies on
--   AXI-Stream flow control rather than overflow detection flags.
--
-- Read Side Behavior (AXI-Stream Compliant Three-State Logic):
--   The read side implements proper AXI-Stream handshaking with three states:
--
--   State A - Becoming Valid:
--     Condition: tvalid_int='0' AND FIFO not empty
--     Action: Present first byte on m_axis_tdata, assert m_axis_tvalid
--     Key: Do NOT advance read pointer—data not yet consumed
--
--   State B - Handshake Complete:
--     Condition: m_axis_tvalid='1' AND m_axis_tready='1'
--     Action: Advance read pointer, present next byte (or deassert tvalid if empty)
--     Key: This is the only state where the pointer advances
--
--   State C - Stalled:
--     Condition: m_axis_tvalid='1' AND m_axis_tready='0'
--     Action: HOLD EVERYTHING STABLE (tdata, tlast, tvalid, pointer)
--     Key: Critical for AXI-Stream compliance—data must not change while valid
--
--   State D - Invalid:
--     Condition: tvalid_int='0' AND FIFO empty
--     Action: Wait for data to arrive, output held at zero
--
-- Frame-Aware Programmable Thresholds:
--   FRAME_SIZE generic allows threshold tuning for different protocols.
--
--   prog_full:  Asserted when remaining space < PROG_FULL_THRESHOLD (one frame)
--               Gives upstream early warning to stop sending before hard full.
--
--   prog_empty: Asserted when fill level < PROG_EMPTY_THRESHOLD (two frames)
--               Gives downstream warning that starvation is approaching.
--               Two frames provides margin for DMA latency to refill.
--
-- Status Capture Interface:
--   A third clock domain (status_aclk) can request synchronized snapshots of
--   wr_ptr and rd_ptr via a request/acknowledge handshake:
--     1. Assert status_req
--     2. State machine synchronizes request to both write and read domains
--     3. Each domain captures its pointer and acknowledges
--     4. When both acknowledge, status_ack pulses and pointers are valid
--
--   This provides a consistent view for debug registers without corrupting
--   the pointers with CDC artifacts.
--
-- Overflow/Underflow Philosophy:
--   This FIFO does NOT implement overflow/underflow detection flags.
--   The design relies entirely on AXI-Stream backpressure:
--     - Overflow prevented by: upstream respecting s_axis_tready
--     - Underflow prevented by: only asserting m_axis_tvalid when data exists
--   If the system is well-behaved (honors flow control), these conditions
--   cannot occur. This is a deliberate design choice, not an omission.
--
-- Generics:
--   DATA_WIDTH - Width of data bus (default 8 for byte-oriented)
--   ADDR_WIDTH - Pointer width; FIFO depth is 2^ADDR_WIDTH (default 11 = 2048)
--   FRAME_SIZE - Frame size in bytes for threshold calculation (default 134 for OV)
--
-- Version History:
--   v4: Pipelined Gray-to-binary conversion for 245 MHz timing closure
--   v3: Three-state read logic for AXI-Stream compliance
--   v2: Added TLAST storage for frame boundary preservation
--   v1: Basic async FIFO with Gray-coded pointers
--
------------------------------------------------------------------------------------------------------


LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.numeric_std.ALL;

ENTITY axis_async_fifo IS
    GENERIC (
        DATA_WIDTH  : NATURAL := 8;
        ADDR_WIDTH  : NATURAL := 11;  -- 2^11 = 2048 bytes default
        FRAME_SIZE  : NATURAL := 134  -- Frame size for threshold calculation (bytes)
    );
    PORT (
        -- Write clock domain (DMA side)
        wr_aclk         : IN  std_logic;
        wr_aresetn      : IN  std_logic;
        
        -- AXIS Slave Interface
        s_axis_tdata    : IN  std_logic_vector(DATA_WIDTH-1 DOWNTO 0);
        s_axis_tvalid   : IN  std_logic;
        s_axis_tready   : OUT std_logic;
        s_axis_tlast    : IN  std_logic;
        
        -- Read clock domain (Symbol clock side)
        rd_aclk         : IN  std_logic;
        rd_aresetn      : IN  std_logic;
        
        -- AXIS Master Interface
        m_axis_tdata    : OUT std_logic_vector(DATA_WIDTH-1 DOWNTO 0);
        m_axis_tvalid   : OUT std_logic;
        m_axis_tready   : IN  std_logic;
        m_axis_tlast    : OUT std_logic;
        
        -- Status signals
        prog_full       : OUT std_logic;
        prog_empty      : OUT std_logic;
        status_aclk     : IN  std_logic;
        status_aresetn  : IN  std_logic;
        status_req      : IN  std_logic;
        status_ack      : OUT std_logic;
        fifo_wr_ptr     : OUT std_logic_vector(ADDR_WIDTH DOWNTO 0);
        fifo_rd_ptr     : OUT std_logic_vector(ADDR_WIDTH DOWNTO 0)
    );
END ENTITY axis_async_fifo;

ARCHITECTURE rtl OF axis_async_fifo IS

    CONSTANT DEPTH : NATURAL := 2**ADDR_WIDTH;

    ---------------------------------------------------------------------------
    -- Frame-Aware Threshold Configuration
    ---------------------------------------------------------------------------
    -- Thresholds provide early warning before the FIFO starves or overflows,
    -- giving upstream/downstream time to react.
    --
    -- FRAME_SIZE is set via generic to support different protocols:
    --   - Opulent Voice 16 kbps OPUS: 134 bytes
    --   - Custom protocols: set at instantiation
    --
    -- If FRAME_SIZE is left at default or set to 0, thresholds will be
    -- conservative (one byte of margin for full, two bytes for empty).
    ---------------------------------------------------------------------------

    -- Resolve frame size: use 1 if FRAME_SIZE is 0 to avoid zero thresholds
    CONSTANT FRAME_SIZE_RESOLVED : NATURAL := maximum(FRAME_SIZE, 1);

    -- Programmable Full Threshold
    -- Asserts prog_full when remaining space drops below one frame.
    -- Clamped to DEPTH for edge case where DEPTH < FRAME_SIZE.
    CONSTANT PROG_FULL_THRESHOLD : NATURAL := minimum(FRAME_SIZE_RESOLVED, DEPTH);
    
    -- Programmable Empty Threshold  
    -- Asserts prog_empty when fill level drops below two frames.
    -- Provides margin for upstream latency to refill before starvation.
    CONSTANT FRAMES_UNTIL_EMPTY_ALERT : NATURAL := 2;
    CONSTANT PROG_EMPTY_THRESHOLD : NATURAL := minimum(
        FRAMES_UNTIL_EMPTY_ALERT * FRAME_SIZE_RESOLVED,
        DEPTH  -- Can't alert for more than the FIFO holds
    );

    -- Separate arrays for Block RAM inference
    TYPE ram_data_type IS ARRAY (0 TO DEPTH-1) OF std_logic_vector(DATA_WIDTH-1 DOWNTO 0);
    TYPE ram_last_type IS ARRAY (0 TO DEPTH-1) OF std_logic;
    
    SIGNAL ram_data : ram_data_type;
    SIGNAL ram_last : ram_last_type;
    
    -- Gray code pointers (reset-initialized in respective clock domains)
    SIGNAL wr_ptr_gray      : std_logic_vector(ADDR_WIDTH DOWNTO 0);
    SIGNAL wr_ptr_bin       : std_logic_vector(ADDR_WIDTH DOWNTO 0);
    SIGNAL rd_ptr_gray      : std_logic_vector(ADDR_WIDTH DOWNTO 0);
    SIGNAL rd_ptr_bin       : std_logic_vector(ADDR_WIDTH DOWNTO 0);
    
    -- CDC Synchronizers (intentionally not reset - avoids cross-domain reset timing issues)
    SIGNAL wr_ptr_gray_sync1 : std_logic_vector(ADDR_WIDTH DOWNTO 0);
    SIGNAL wr_ptr_gray_sync2 : std_logic_vector(ADDR_WIDTH DOWNTO 0);
    SIGNAL rd_ptr_gray_sync1 : std_logic_vector(ADDR_WIDTH DOWNTO 0);
    SIGNAL rd_ptr_gray_sync2 : std_logic_vector(ADDR_WIDTH DOWNTO 0);
    
    -- FIX v4: Registered binary pointers after Gray-to-binary conversion
    -- This breaks the critical path: sync2 -> gray_to_bin -> comparison -> output
    -- Into: sync2 -> gray_to_bin -> REG -> comparison -> output
    SIGNAL wr_ptr_bin_sync  : std_logic_vector(ADDR_WIDTH DOWNTO 0);  -- Now a signal, not variable
    SIGNAL rd_ptr_bin_sync  : std_logic_vector(ADDR_WIDTH DOWNTO 0);  -- For symmetry in write domain
    
    -- Status flags (reset-initialized in respective clock domains)
    SIGNAL full_int         : std_logic;
    SIGNAL tready_int       : std_logic;
    SIGNAL tvalid_int       : std_logic;
    SIGNAL prog_full_int    : std_logic;
    SIGNAL prog_empty_int   : std_logic;
    
    -- Status resync to AXI
    SIGNAL wr_status_ack        : std_logic;
    SIGNAL wr_status_ack_sync1  : std_logic;
    SIGNAL wr_status_ack_sync2  : std_logic;
    SIGNAL wr_status_req_sync1  : std_logic;
    SIGNAL wr_status_req_sync2  : std_logic;
    SIGNAL rd_status_ack        : std_logic;
    SIGNAL rd_status_ack_sync1  : std_logic;
    SIGNAL rd_status_ack_sync2  : std_logic;
    SIGNAL rd_status_req_sync1  : std_logic;
    SIGNAL rd_status_req_sync2  : std_logic;

    SIGNAL srequest             : std_logic;

    TYPE state_type IS (IDLE, WAIT_FOR_WR_ACK, WAIT_FOR_RD_ACK);
    SIGNAL status_state : state_type;

    -- Binary to Gray conversion
    FUNCTION bin_to_gray(bin : std_logic_vector) RETURN std_logic_vector IS
        VARIABLE gray : std_logic_vector(bin'RANGE);
    BEGIN
        gray := bin XOR ('0' & bin(bin'LEFT DOWNTO 1));
        RETURN gray;
    END FUNCTION;
    
    -- Gray to Binary conversion
    FUNCTION gray_to_bin(gray : std_logic_vector) RETURN std_logic_vector IS
        VARIABLE bin : std_logic_vector(gray'RANGE);
    BEGIN
        bin(bin'LEFT) := gray(gray'LEFT);
        FOR i IN bin'LEFT-1 DOWNTO 0 LOOP
            bin(i) := bin(i+1) XOR gray(i);
        END LOOP;
        RETURN bin;
    END FUNCTION;

BEGIN

    s_axis_tready <= tready_int;
    m_axis_tvalid <= tvalid_int;
    prog_full <= prog_full_int;
    prog_empty <= prog_empty_int;

    ------------------------------------------------------------------------------
    -- Write Clock Domain
    ------------------------------------------------------------------------------
    write_proc: PROCESS(wr_aclk)
        VARIABLE wr_ptr_bin_next : std_logic_vector(ADDR_WIDTH DOWNTO 0);
    BEGIN
        IF rising_edge(wr_aclk) THEN
            IF wr_aresetn = '0' THEN
                wr_ptr_bin <= (OTHERS => '0');
                wr_ptr_gray <= (OTHERS => '0');
                full_int <= '0';
                tready_int <= '0';
                prog_full_int <= '0';
                rd_ptr_gray_sync1 <= (OTHERS => '0');
                rd_ptr_gray_sync2 <= (OTHERS => '0');
                rd_ptr_bin_sync <= (OTHERS => '0');  -- FIX v4: Initialize registered signal
                
            ELSE
                -- Synchronize read pointer (2-stage synchronizer)
                rd_ptr_gray_sync1 <= rd_ptr_gray;
                rd_ptr_gray_sync2 <= rd_ptr_gray_sync1;
                
                -- FIX v4: Register the Gray-to-binary conversion output
                -- This is the key timing fix - breaks the combinational path
                rd_ptr_bin_sync <= gray_to_bin(rd_ptr_gray_sync2);
                
                -- AXIS write handshake
                IF s_axis_tvalid = '1' AND tready_int = '1' THEN
                    ram_data(to_integer(unsigned(wr_ptr_bin(ADDR_WIDTH-1 DOWNTO 0)))) <= s_axis_tdata;
                    ram_last(to_integer(unsigned(wr_ptr_bin(ADDR_WIDTH-1 DOWNTO 0)))) <= s_axis_tlast;
                    
                    wr_ptr_bin_next := std_logic_vector(unsigned(wr_ptr_bin) + 1);
                    wr_ptr_bin <= wr_ptr_bin_next;
                    wr_ptr_gray <= bin_to_gray(wr_ptr_bin_next);
                END IF;
                
                -- Full detection (now uses registered rd_ptr_bin_sync)
                IF wr_ptr_bin(ADDR_WIDTH) /= rd_ptr_bin_sync(ADDR_WIDTH) AND
                   wr_ptr_bin(ADDR_WIDTH-1 DOWNTO 0) = rd_ptr_bin_sync(ADDR_WIDTH-1 DOWNTO 0) THEN
                    full_int <= '1';
                ELSE
                    full_int <= '0';
                END IF;
                
                -- Programmable full - frame-aware threshold (now uses registered rd_ptr_bin_sync)
                IF DEPTH - (unsigned(wr_ptr_bin) - unsigned(rd_ptr_bin_sync)) <= PROG_FULL_THRESHOLD THEN
                    prog_full_int <= '1';
                ELSE
                    prog_full_int <= '0';
                END IF;
                
                -- Control tready
                IF prog_full_int = '1' OR full_int = '1' THEN
                    tready_int <= '0';
                ELSE
                    tready_int <= '1';
                END IF;
            END IF;
        END IF;
    END PROCESS write_proc;

    ------------------------------------------------------------------------------
    -- Read Clock Domain - CORRECTED THREE-STATE LOGIC
    ------------------------------------------------------------------------------
    -- State A: Becoming valid (tvalid_int='0' → '1'): Present first byte
    -- State B: Handshake completes (tvalid='1', tready='1'): Advance, present next
    -- State C: Valid but stalled (tvalid='1', tready='0'): HOLD STABLE
    ------------------------------------------------------------------------------
    read_proc: PROCESS(rd_aclk)
        VARIABLE rd_ptr_bin_next : std_logic_vector(ADDR_WIDTH DOWNTO 0);
        VARIABLE empty_current : std_logic;
    BEGIN
        IF rising_edge(rd_aclk) THEN
            IF rd_aresetn = '0' THEN
                rd_ptr_bin <= (OTHERS => '0');
                rd_ptr_gray <= (OTHERS => '0');
                tvalid_int <= '0';
                prog_empty_int <= '1';
                m_axis_tdata <= (OTHERS => '0');
                m_axis_tlast <= '0';
                wr_ptr_gray_sync1 <= (OTHERS => '0');
                wr_ptr_gray_sync2 <= (OTHERS => '0');
                wr_ptr_bin_sync <= (OTHERS => '0');  -- FIX v4: Initialize registered signal
                
            ELSE
                -- Synchronize write pointer (2-stage synchronizer)
                wr_ptr_gray_sync1 <= wr_ptr_gray;
                wr_ptr_gray_sync2 <= wr_ptr_gray_sync1;
                
                -- FIX v4: Register the Gray-to-binary conversion output
                -- This breaks the critical path that was failing timing:
                --   wr_ptr_gray_sync2 -> gray_to_bin -> comparison -> m_axis_tdata
                -- Now becomes:
                --   wr_ptr_gray_sync2 -> gray_to_bin -> wr_ptr_bin_sync (REG)
                --   wr_ptr_bin_sync -> comparison -> m_axis_tdata
                wr_ptr_bin_sync <= gray_to_bin(wr_ptr_gray_sync2);
                
                -- Check if FIFO is currently empty (now uses registered wr_ptr_bin_sync)
                IF wr_ptr_bin_sync = rd_ptr_bin THEN
                    empty_current := '1';
                ELSE
                    empty_current := '0';
                END IF;
                
                ----------------------------------------------------------------------
                -- THREE STATE LOGIC
                ----------------------------------------------------------------------
                
                -- STATE A: Becoming valid (was invalid, now have data)
                -- Action: Present first byte, assert tvalid, DO NOT advance pointer
                IF tvalid_int = '0' AND empty_current = '0' THEN
                    m_axis_tdata <= ram_data(to_integer(unsigned(rd_ptr_bin(ADDR_WIDTH-1 DOWNTO 0))));
                    m_axis_tlast <= ram_last(to_integer(unsigned(rd_ptr_bin(ADDR_WIDTH-1 DOWNTO 0))));
                    tvalid_int <= '1';
                    -- rd_ptr_bin stays same! This is the first presentation
                
                -- STATE B: Handshake completes (valid and ready)
                -- Action: Advance pointer, present next byte OR deassert tvalid
                ELSIF tvalid_int = '1' AND m_axis_tready = '1' THEN
                    rd_ptr_bin_next := std_logic_vector(unsigned(rd_ptr_bin) + 1);
                    rd_ptr_bin <= rd_ptr_bin_next;
                    rd_ptr_gray <= bin_to_gray(rd_ptr_bin_next);
                    
                    -- Check if we'll be empty after this read (uses registered wr_ptr_bin_sync)
                    IF wr_ptr_bin_sync = rd_ptr_bin_next THEN
                        -- Going empty
                        tvalid_int <= '0';
                        m_axis_tlast <= '0';
                        m_axis_tdata <= (OTHERS => '0');
                    ELSE
                        -- More data available - present next byte
                        tvalid_int <= '1';
                        m_axis_tdata <= ram_data(to_integer(unsigned(rd_ptr_bin_next(ADDR_WIDTH-1 DOWNTO 0))));
                        m_axis_tlast <= ram_last(to_integer(unsigned(rd_ptr_bin_next(ADDR_WIDTH-1 DOWNTO 0))));
                    END IF;
                
                -- STATE C: Valid but NOT ready (tvalid='1', tready='0')
                -- Action: HOLD EVERYTHING STABLE - no changes to tdata, tlast, tvalid, rd_ptr
                ELSIF tvalid_int = '1' AND m_axis_tready = '0' THEN
                    -- Explicitly do nothing - all signals hold their values
                    -- This is the critical fix: maintain protocol compliance
                    
                -- All other cases: remain invalid
                ELSE
                    tvalid_int <= '0';
                    m_axis_tlast <= '0';
                    m_axis_tdata <= (OTHERS => '0');
                END IF;
                
                -- Programmable empty (uses registered wr_ptr_bin_sync)
                IF unsigned(wr_ptr_bin_sync) <= unsigned(rd_ptr_bin) + PROG_EMPTY_THRESHOLD THEN
                    prog_empty_int <= '1';
                ELSE
                    prog_empty_int <= '0';
                END IF;
            END IF;
        END IF;
    END PROCESS read_proc;

    ------------------------------------------------------------------------------
    -- Status Clock Domain
    ------------------------------------------------------------------------------

    status_proc : PROCESS (status_aclk)
    BEGIN
        IF rising_edge(status_aclk) THEN
            IF status_aresetn = '0' THEN
                status_ack      <= '0';
                status_state    <= IDLE;
            ELSE

                CASE status_state IS
                    WHEN IDLE =>
                        srequest    <= '0';
                        status_ack  <= '0';
                        IF status_req = '1' THEN
                            srequest     <= '1';
                            status_state <= WAIT_FOR_WR_ACK;
                        END IF;

                    WHEN WAIT_FOR_WR_ACK =>
                        IF wr_status_ack_sync2 = '1' THEN
                            status_state <= WAIT_FOR_RD_ACK;
                        END IF;

                    WHEN WAIT_FOR_RD_ACK =>
                        IF rd_status_ack_sync2 = '1' THEN
                            status_ack   <= '1';
                            srequest     <= '0';
                            status_state <= IDLE;
                        END IF;

                    WHEN OTHERS =>
                        status_state <= IDLE;

                END CASE;

                wr_status_ack_sync1 <= wr_status_ack;
                wr_status_ack_sync2 <= wr_status_ack_sync1;

                rd_status_ack_sync1 <= rd_status_ack;
                rd_status_ack_sync2 <= rd_status_ack_sync1;

            END IF;
        END IF;
    END PROCESS status_proc;

    status_wrclk : PROCESS (wr_aclk)
    BEGIN
        IF rising_edge(wr_aclk) THEN
            IF wr_aresetn = '0' THEN
                wr_status_req_sync1 <= '0';
                wr_status_req_sync2 <= '0';
                wr_status_ack       <= '0';
                fifo_wr_ptr         <= (OTHERS => '0');
            ELSE 
                wr_status_req_sync1 <= srequest;
                wr_status_req_sync2 <= wr_status_req_sync1;
                wr_status_ack       <= wr_status_req_sync2;

                IF wr_status_req_sync2 = '1' THEN
                    fifo_wr_ptr     <= wr_ptr_bin;
                END IF;
            END IF;
        END IF;
    END PROCESS status_wrclk;

    status_rdclk : PROCESS (rd_aclk)
    BEGIN
        IF rising_edge(rd_aclk) THEN
            IF rd_aresetn = '0' THEN
                rd_status_req_sync1 <= '0';
                rd_status_req_sync2 <= '0';
                rd_status_ack       <= '0';
                fifo_rd_ptr         <= (OTHERS => '0');
            ELSE 
                rd_status_req_sync1 <= srequest;
                rd_status_req_sync2 <= rd_status_req_sync1;
                rd_status_ack       <= rd_status_req_sync2;

                IF rd_status_req_sync2 = '1' THEN
                    fifo_rd_ptr     <= rd_ptr_bin;
                END IF;
            END IF;
        END IF;
    END PROCESS status_rdclk;

END ARCHITECTURE rtl;
