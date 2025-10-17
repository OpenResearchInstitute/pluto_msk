------------------------------------------------------------------------------------------------------
-- AXIS-Compliant Asynchronous FIFO
------------------------------------------------------------------------------------------------------
-- Dual-clock FIFO with AXIS handshaking and TLAST support
-- Implements gray code pointers for safe clock domain crossing
------------------------------------------------------------------------------------------------------

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.numeric_std.ALL;

ENTITY axis_async_fifo IS
    GENERIC (
        DATA_WIDTH  : NATURAL := 8;
        ADDR_WIDTH  : NATURAL := 11  -- 2^11 = 2048 bytes (enough for ~7 frames)
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
        prog_full       : OUT std_logic;  -- Programmable full threshold
        prog_empty      : OUT std_logic   -- Programmable empty threshold
    );
END ENTITY axis_async_fifo;

ARCHITECTURE rtl OF axis_async_fifo IS

    CONSTANT DEPTH : NATURAL := 2**ADDR_WIDTH;
    
    -- Dual-port RAM with TLAST bit
    TYPE ram_entry_t IS RECORD
        data : std_logic_vector(DATA_WIDTH-1 DOWNTO 0);
        last : std_logic;
    END RECORD;
    TYPE ram_type IS ARRAY (0 TO DEPTH-1) OF ram_entry_t;
    SIGNAL ram : ram_type;
    
    -- Gray code pointers (one bit wider to detect full/empty)
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

    -- AXIS interface assignments
    s_axis_tready <= tready_int;
    m_axis_tvalid <= tvalid_int;
    
    ------------------------------------------------------------------------------
    -- Write Clock Domain (DMA side)
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
                prog_full <= '0';
                
            ELSE
                -- Synchronize read pointer into write domain (2-stage)
                rd_ptr_gray_sync1 <= rd_ptr_gray;
                rd_ptr_gray_sync2 <= rd_ptr_gray_sync1;
                
                -- Convert synchronized gray to binary
                rd_ptr_bin_sync := gray_to_bin(rd_ptr_gray_sync2);
                
                -- AXIS handshake: write when valid and ready
                IF s_axis_tvalid = '1' AND tready_int = '1' THEN
                    -- Write data and TLAST to RAM
                    ram(to_integer(unsigned(wr_ptr_bin(ADDR_WIDTH-1 DOWNTO 0)))).data <= s_axis_tdata;
                    ram(to_integer(unsigned(wr_ptr_bin(ADDR_WIDTH-1 DOWNTO 0)))).last <= s_axis_tlast;
                    
                    -- Increment write pointer
                    wr_ptr_bin_next := std_logic_vector(unsigned(wr_ptr_bin) + 1);
                    wr_ptr_bin <= wr_ptr_bin_next;
                    wr_ptr_gray <= bin_to_gray(wr_ptr_bin_next);
                END IF;
                
                -- Full flag: write pointer caught up with read pointer
                IF wr_ptr_bin(ADDR_WIDTH) /= rd_ptr_bin_sync(ADDR_WIDTH) AND
                   wr_ptr_bin(ADDR_WIDTH-1 DOWNTO 0) = rd_ptr_bin_sync(ADDR_WIDTH-1 DOWNTO 0) THEN
                    full_int <= '1';
                    tready_int <= '0';
                ELSE
                    full_int <= '0';
                    tready_int <= '1';
                END IF;
                
                -- Programmable full: within 512 entries of full
                IF unsigned(wr_ptr_bin) + 512 >= unsigned(rd_ptr_bin_sync) + DEPTH THEN
                    prog_full <= '1';
                ELSE
                    prog_full <= '0';
                END IF;
            END IF;
        END IF;
    END PROCESS write_proc;

    ------------------------------------------------------------------------------
    -- Read Clock Domain (Symbol clock side)
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
                prog_empty <= '1';
                m_axis_tdata <= (OTHERS => '0');
                m_axis_tlast <= '0';
                
            ELSE
                -- Synchronize write pointer into read domain (2-stage)
                wr_ptr_gray_sync1 <= wr_ptr_gray;
                wr_ptr_gray_sync2 <= wr_ptr_gray_sync1;
                
                -- Convert synchronized gray to binary
                wr_ptr_bin_sync := gray_to_bin(wr_ptr_gray_sync2);
                
                -- AXIS handshake: read when valid and ready
                IF tvalid_int = '1' AND m_axis_tready = '1' THEN
                    -- Increment read pointer
                    rd_ptr_bin_next := std_logic_vector(unsigned(rd_ptr_bin) + 1);
                    rd_ptr_bin <= rd_ptr_bin_next;
                    rd_ptr_gray <= bin_to_gray(rd_ptr_bin_next);
                END IF;
                
                -- Always present data at output when not empty
                IF empty_int = '0' THEN
                    m_axis_tdata <= ram(to_integer(unsigned(rd_ptr_bin(ADDR_WIDTH-1 DOWNTO 0)))).data;
                    m_axis_tlast <= ram(to_integer(unsigned(rd_ptr_bin(ADDR_WIDTH-1 DOWNTO 0)))).last;
                    tvalid_int <= '1';
                ELSE
                    tvalid_int <= '0';
                END IF;
                
                -- Empty flag: read pointer caught up with write pointer
                IF rd_ptr_bin = wr_ptr_bin_sync THEN
                    empty_int <= '1';
                ELSE
                    empty_int <= '0';
                END IF;
                
                -- Programmable empty: 271 or fewer entries available (one frame)
                IF unsigned(wr_ptr_bin_sync) <= unsigned(rd_ptr_bin) + 271 THEN
                    prog_empty <= '1';
                ELSE
                    prog_empty <= '0';
                END IF;
            END IF;
        END IF;
    END PROCESS read_proc;

END ARCHITECTURE rtl;
