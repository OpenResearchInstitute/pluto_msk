------------------------------------------------------------------------------------------------------
-- Dual-Clock Asynchronous FIFO
------------------------------------------------------------------------------------------------------
-- A portable, platform-independent async FIFO using gray code pointers
-- for safe clock domain crossing.
------------------------------------------------------------------------------------------------------

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.numeric_std.ALL;

ENTITY async_fifo IS
    GENERIC (
        DATA_WIDTH  : NATURAL := 8;
        ADDR_WIDTH  : NATURAL := 8  -- 2^8 = 256 entries
    );
    PORT (
        -- Write clock domain
        wr_clk      : IN  std_logic;
        wr_rst      : IN  std_logic;
        wr_en       : IN  std_logic;
        wr_data     : IN  std_logic_vector(DATA_WIDTH-1 DOWNTO 0);
        full        : OUT std_logic;
        almost_full : OUT std_logic;
        wr_tlast    : IN  std_logic;

        
        -- Read clock domain
        rd_clk      : IN  std_logic;
        rd_rst      : IN  std_logic;
        rd_en       : IN  std_logic;
        rd_data     : OUT std_logic_vector(DATA_WIDTH-1 DOWNTO 0);
        empty       : OUT std_logic;
        almost_empty: OUT std_logic;
        rd_tlast    : OUT std_logic

    );
END ENTITY async_fifo;

ARCHITECTURE rtl OF async_fifo IS

    CONSTANT DEPTH : NATURAL := 2**ADDR_WIDTH;
    
    -- Dual-port RAM
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
    
    -- Binary to Gray conversion function
    FUNCTION bin_to_gray(bin : std_logic_vector) RETURN std_logic_vector IS
        VARIABLE gray : std_logic_vector(bin'RANGE);
    BEGIN
        gray := bin XOR ('0' & bin(bin'LEFT DOWNTO 1));
        RETURN gray;
    END FUNCTION;
    
    -- Gray to Binary conversion function
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

    -- Output assignments
    full <= full_int;
    empty <= empty_int;
    
    ------------------------------------------------------------------------------
    -- Write Clock Domain
    ------------------------------------------------------------------------------
    write_proc: PROCESS(wr_clk)
        VARIABLE wr_ptr_bin_next : std_logic_vector(ADDR_WIDTH DOWNTO 0);
        VARIABLE rd_ptr_bin_sync : std_logic_vector(ADDR_WIDTH DOWNTO 0);
    BEGIN
        IF rising_edge(wr_clk) THEN
            IF wr_rst = '1' THEN
                wr_ptr_bin <= (OTHERS => '0');
                wr_ptr_gray <= (OTHERS => '0');
                full_int <= '0';
                almost_full <= '0';
                
            ELSE
                -- Synchronize read pointer into write domain
                rd_ptr_gray_sync1 <= rd_ptr_gray;
                rd_ptr_gray_sync2 <= rd_ptr_gray_sync1;
                
                -- Convert synchronized gray to binary
                rd_ptr_bin_sync := gray_to_bin(rd_ptr_gray_sync2);
                
                -- Write operation
                IF wr_en = '1' AND full_int = '0' THEN
                    ram(to_integer(unsigned(wr_ptr_bin(ADDR_WIDTH-1 DOWNTO 0)))).data <= wr_data;
                    ram(to_integer(unsigned(wr_ptr_bin(ADDR_WIDTH-1 DOWNTO 0)))).last <= wr_tlast;                    

                    wr_ptr_bin_next := std_logic_vector(unsigned(wr_ptr_bin) + 1);
                    wr_ptr_bin <= wr_ptr_bin_next;
                    wr_ptr_gray <= bin_to_gray(wr_ptr_bin_next);
                END IF;
                
                -- Full flag: write pointer caught up with read pointer
                -- (MSB different, other bits same)
                IF wr_ptr_bin(ADDR_WIDTH) /= rd_ptr_bin_sync(ADDR_WIDTH) AND
                   wr_ptr_bin(ADDR_WIDTH-1 DOWNTO 0) = rd_ptr_bin_sync(ADDR_WIDTH-1 DOWNTO 0) THEN
                    full_int <= '1';
                ELSE
                    full_int <= '0';
                END IF;
                
                -- Almost full: within 2 entries of full
                IF unsigned(wr_ptr_bin) + 2 >= unsigned(rd_ptr_bin_sync) + DEPTH THEN
                    almost_full <= '1';
                ELSE
                    almost_full <= '0';
                END IF;
            END IF;
        END IF;
    END PROCESS;

    ------------------------------------------------------------------------------
    -- Read Clock Domain
    ------------------------------------------------------------------------------
    read_proc: PROCESS(rd_clk)
        VARIABLE rd_ptr_bin_next : std_logic_vector(ADDR_WIDTH DOWNTO 0);
        VARIABLE wr_ptr_bin_sync : std_logic_vector(ADDR_WIDTH DOWNTO 0);
    BEGIN
        IF rising_edge(rd_clk) THEN
            IF rd_rst = '1' THEN
                rd_ptr_bin <= (OTHERS => '0');
                rd_ptr_gray <= (OTHERS => '0');
                empty_int <= '1';
                almost_empty <= '1';
                rd_data <= (OTHERS => '0');
                rd_tlast <= '0';
                
            ELSE
                -- Synchronize write pointer into read domain
                wr_ptr_gray_sync1 <= wr_ptr_gray;
                wr_ptr_gray_sync2 <= wr_ptr_gray_sync1;
                
                -- Convert synchronized gray to binary
                wr_ptr_bin_sync := gray_to_bin(wr_ptr_gray_sync2);
                
                -- Read operation
                IF rd_en = '1' AND empty_int = '0' THEN
                    rd_data <= ram(to_integer(unsigned(rd_ptr_bin(ADDR_WIDTH-1 DOWNTO 0)))).data;
                    rd_tlast <= ram(to_integer(unsigned(rd_ptr_bin(ADDR_WIDTH-1 DOWNTO 0)))).last;
                    
                    rd_ptr_bin_next := std_logic_vector(unsigned(rd_ptr_bin) + 1);
                    rd_ptr_bin <= rd_ptr_bin_next;
                    rd_ptr_gray <= bin_to_gray(rd_ptr_bin_next);
                END IF;
                
                -- Empty flag: read pointer caught up with write pointer
                -- (all bits same)
                IF rd_ptr_bin = wr_ptr_bin_sync THEN
                    empty_int <= '1';
                ELSE
                    empty_int <= '0';
                END IF;
                
                -- Almost empty: 2 or fewer entries available
                IF unsigned(wr_ptr_bin_sync) <= unsigned(rd_ptr_bin) + 2 THEN
                    almost_empty <= '1';
                ELSE
                    almost_empty <= '0';
                END IF;
            END IF;
        END IF;
    END PROCESS;

END ARCHITECTURE rtl;
