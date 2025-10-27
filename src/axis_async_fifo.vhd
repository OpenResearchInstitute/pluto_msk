------------------------------------------------------------------------------------------------------
-- AXIS-Compliant Asynchronous FIFO - SYNC LAG FIX
------------------------------------------------------------------------------------------------------
-- FIX: Added safety margin to empty detection to account for 2-cycle synchronization lag
-- This prevents reading past actual data and hitting stale tlast markers
------------------------------------------------------------------------------------------------------

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.numeric_std.ALL;

ENTITY axis_async_fifo IS
    GENERIC (
        DATA_WIDTH  : NATURAL := 8;
        ADDR_WIDTH  : NATURAL := 11  -- 2^11 = 2048 bytes
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
        
        -- Control signals
        --prog_packet_size: IN  std_logic_vector...

        -- Status signals
        prog_full       : OUT std_logic;
        prog_empty      : OUT std_logic;
        status_aclk     : IN  std_logic;
        status_aresetn  : IN  std_logic;
        status_req      : IN  std_logic;
        status_ack      : OUT std_logic;
        fifo_overflow   : OUT std_logic;
        fifo_underflow  : OUT std_logic;
        fifo_wr_ptr     : OUT std_logic_vector(ADDR_WIDTH DOWNTO 0);
        fifo_rd_ptr     : OUT std_logic_vector(ADDR_WIDTH DOWNTO 0)
    );
END ENTITY axis_async_fifo;

ARCHITECTURE rtl OF axis_async_fifo IS

    CONSTANT DEPTH : NATURAL := 2**ADDR_WIDTH;
    
    -- Separate arrays for Block RAM inference
    TYPE ram_data_type IS ARRAY (0 TO DEPTH-1) OF std_logic_vector(DATA_WIDTH-1 DOWNTO 0);
    TYPE ram_last_type IS ARRAY (0 TO DEPTH-1) OF std_logic;
    
    SIGNAL ram_data : ram_data_type;
    SIGNAL ram_last : ram_last_type;
    
    ATTRIBUTE ram_style : STRING;
    ATTRIBUTE ram_style OF ram_data : SIGNAL IS "block";
    ATTRIBUTE ram_style OF ram_last : SIGNAL IS "block";
    
    -- Gray code pointers
    SIGNAL wr_ptr_gray      : std_logic_vector(ADDR_WIDTH DOWNTO 0) := (OTHERS => '0');
    SIGNAL wr_ptr_bin       : std_logic_vector(ADDR_WIDTH DOWNTO 0) := (OTHERS => '0');
    SIGNAL rd_ptr_gray      : std_logic_vector(ADDR_WIDTH DOWNTO 0) := (OTHERS => '0');
    SIGNAL rd_ptr_bin       : std_logic_vector(ADDR_WIDTH DOWNTO 0) := (OTHERS => '0');
    
    -- Synchronized pointers
    SIGNAL wr_ptr_gray_sync1 : std_logic_vector(ADDR_WIDTH DOWNTO 0) := (OTHERS => '0');
    SIGNAL wr_ptr_gray_sync2 : std_logic_vector(ADDR_WIDTH DOWNTO 0) := (OTHERS => '0');
    SIGNAL rd_ptr_gray_sync1 : std_logic_vector(ADDR_WIDTH DOWNTO 0) := (OTHERS => '0');
    SIGNAL rd_ptr_gray_sync2 : std_logic_vector(ADDR_WIDTH DOWNTO 0) := (OTHERS => '0');
    
    -- Status flags
    SIGNAL full_int         : std_logic := '0';
    SIGNAL empty_int        : std_logic := '1';
    SIGNAL tready_int       : std_logic := '0';
    SIGNAL tvalid_int       : std_logic := '0';
    SIGNAL prog_full_int    : std_logic := '0';
    SIGNAL prog_empty_int   : std_logic := '0';
    
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
        VARIABLE rd_ptr_bin_sync : std_logic_vector(ADDR_WIDTH DOWNTO 0);
    BEGIN
        IF rising_edge(wr_aclk) THEN
            IF wr_aresetn = '0' THEN
                wr_ptr_bin <= (OTHERS => '0');
                wr_ptr_gray <= (OTHERS => '0');
                full_int <= '0';
                tready_int <= '0';
                prog_full_int <= '0';
                
            ELSE
                -- Synchronize read pointer
                rd_ptr_gray_sync1 <= rd_ptr_gray;
                rd_ptr_gray_sync2 <= rd_ptr_gray_sync1;
                rd_ptr_bin_sync := gray_to_bin(rd_ptr_gray_sync2);
                
                -- AXIS write handshake
                IF s_axis_tvalid = '1' AND tready_int = '1' THEN
                    ram_data(to_integer(unsigned(wr_ptr_bin(ADDR_WIDTH-1 DOWNTO 0)))) <= s_axis_tdata;
                    ram_last(to_integer(unsigned(wr_ptr_bin(ADDR_WIDTH-1 DOWNTO 0)))) <= s_axis_tlast;
                    
                    wr_ptr_bin_next := std_logic_vector(unsigned(wr_ptr_bin) + 1);
                    wr_ptr_bin <= wr_ptr_bin_next;
                    wr_ptr_gray <= bin_to_gray(wr_ptr_bin_next);
                END IF;
                
                -- Full detection
                IF wr_ptr_bin(ADDR_WIDTH) /= rd_ptr_bin_sync(ADDR_WIDTH) AND
                   wr_ptr_bin(ADDR_WIDTH-1 DOWNTO 0) = rd_ptr_bin_sync(ADDR_WIDTH-1 DOWNTO 0) THEN
                    full_int <= '1';
                ELSE
                    full_int <= '0';
                END IF;
                
                -- Programmable full
                IF DEPTH - (unsigned(wr_ptr_bin) - unsigned(rd_ptr_bin_sync)) <= 512 THEN
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
    -- Read Clock Domain - WITH SYNC LAG FIX
    ------------------------------------------------------------------------------
    read_proc: PROCESS(rd_aclk)
        VARIABLE rd_ptr_bin_next : std_logic_vector(ADDR_WIDTH DOWNTO 0);
        VARIABLE wr_ptr_bin_sync : std_logic_vector(ADDR_WIDTH DOWNTO 0);
    BEGIN
        IF rising_edge(rd_aclk) THEN
            IF rd_aresetn = '0' THEN
                rd_ptr_bin <= (OTHERS => '0');
                rd_ptr_gray <= (OTHERS => '0');
                empty_int <= '1';
                tvalid_int <= '0';
                prog_empty_int <= '1';
                m_axis_tdata <= (OTHERS => '0');
                m_axis_tlast <= '0';
                
            ELSE
                -- Synchronize write pointer
                wr_ptr_gray_sync1 <= wr_ptr_gray;
                wr_ptr_gray_sync2 <= wr_ptr_gray_sync1;
                wr_ptr_bin_sync := gray_to_bin(wr_ptr_gray_sync2);
                
                -- AXIS read handshake
                IF tvalid_int = '1' AND m_axis_tready = '1' THEN
                    rd_ptr_bin_next := std_logic_vector(unsigned(rd_ptr_bin) + 1);
                    rd_ptr_bin <= rd_ptr_bin_next;
                    rd_ptr_gray <= bin_to_gray(rd_ptr_bin_next);
                END IF;
                
                -- Present data when not empty
                IF empty_int = '0' THEN
                    m_axis_tdata <= ram_data(to_integer(unsigned(rd_ptr_bin(ADDR_WIDTH-1 DOWNTO 0))));
                    m_axis_tlast <= ram_last(to_integer(unsigned(rd_ptr_bin(ADDR_WIDTH-1 DOWNTO 0))));
                    tvalid_int <= '1';
                ELSE
                    tvalid_int <= '0';
                END IF;
                
                -- FIX: Empty detection with safety margin for sync lag
                -- Stop reading when within 3 bytes of synchronized write pointer
                -- This accounts for the 2-cycle synchronization delay
                IF unsigned(wr_ptr_bin_sync) <= unsigned(rd_ptr_bin) + 3 THEN
                    empty_int <= '1';
                ELSE
                    empty_int <= '0';
                END IF;
                
                -- Programmable empty
                IF unsigned(wr_ptr_bin_sync) <= unsigned(rd_ptr_bin) + 271 THEN
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
                --prog_empty      <= '0';
                --prog_full       <= '0';
                fifo_overflow   <= '0';
                fifo_underflow  <= '0';
                status_ack      <= '0';
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

                IF wr_status_req_sync2 THEN
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

                IF rd_status_req_sync2 THEN
                    fifo_rd_ptr     <= rd_ptr_bin;
                END IF;
            END IF;
        END IF;
    END PROCESS status_rdclk;

END ARCHITECTURE rtl;
