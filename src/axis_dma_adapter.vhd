------------------------------------------------------------------------------------------------------
-- AXIS DMA to Byte Adapter
------------------------------------------------------------------------------------------------------
-- Filters 32-bit DMA words to extract lowest 8 bits for byte-oriented FIFO
-- Preserves TLAST signal for frame boundary marking
-- TKEEP is optional - design works with or without it
------------------------------------------------------------------------------------------------------

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.numeric_std.ALL;

ENTITY axis_dma_adapter IS
    GENERIC (
        DMA_WIDTH : NATURAL := 32;
        BYTE_WIDTH : NATURAL := 8
    );
    PORT (
        -- Clock and Reset
        aclk            : IN  std_logic;
        aresetn         : IN  std_logic;
        
        -- AXIS Slave Interface (from DMA)
        s_axis_tdata    : IN  std_logic_vector(DMA_WIDTH-1 DOWNTO 0);
        s_axis_tvalid   : IN  std_logic;
        s_axis_tready   : OUT std_logic;
        s_axis_tlast    : IN  std_logic;
        s_axis_tkeep    : IN  std_logic_vector((DMA_WIDTH/8)-1 DOWNTO 0) := (OTHERS => '1');
        
        -- AXIS Master Interface (to FIFO)
        m_axis_tdata    : OUT std_logic_vector(BYTE_WIDTH-1 DOWNTO 0);
        m_axis_tvalid   : OUT std_logic;
        m_axis_tready   : IN  std_logic;
        m_axis_tlast    : OUT std_logic
    );
END ENTITY axis_dma_adapter;

ARCHITECTURE rtl OF axis_dma_adapter IS

BEGIN

    -- Direct passthrough of filtered data
    -- Extract lowest byte from 32-bit word (byte 0 = bits 7:0)
    -- This works regardless of TKEEP since we always use bits [7:0]
    m_axis_tdata <= s_axis_tdata(BYTE_WIDTH-1 DOWNTO 0);
    
    -- Flow control passthrough
    m_axis_tvalid <= s_axis_tvalid;
    s_axis_tready <= m_axis_tready;
    
    -- Frame boundary preserved
    m_axis_tlast <= s_axis_tlast;
    
    -- Note: TKEEP has a default value of all '1's, so if it's not connected,
    -- the design still works. We don't propagate TKEEP downstream since the
    -- FIFO expects all bytes to be valid (8-bit interface).
    -- Design is portable: works with or without TKEEP connected.

END ARCHITECTURE rtl;
