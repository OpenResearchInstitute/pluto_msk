------------------------------------------------------------------------------------------------------
-- AXIS DMA to Byte Adapter
------------------------------------------------------------------------------------------------------
-- Role in the Transmit Chain:
--   Entry point from the Processing System (PS). Bridges the DMA interface to our
--   byte-oriented transmit pipeline (FIFO to frame assembler to serializer to modulator).
--
-- Why One Byte Per 32-bit Word?
--   The IIO subsystem and DMA infrastructure are designed for IQ sample
--   streaming: 16-bit I + 16-bit Q packed into 32-bit words. But in our design,
--   we're sending Opulent Voice baseband data frames through this same DMA path, 
--   and the MSK modulator generates IQ samples on the PL side.
--
--   We're repurposing IQ-oriented plumbing for byte transport, so we stuff one
--   data byte into bits [7:0] of each 32-bit word. Yes, 75% of the DMA bandwidth
--   goes unused, but it's the path of least resistance through the existing
--   IIO (Pluto SDR, Libre SDR) software stack.
--
-- Data Format Expectation:
--   Upstream must pack ONE valid chunk of data per DMA word, with the data 
--   in bits [BYTE_WIDTH-1:0]. The bits [DMA_WIDTH-1:8] are ignored. 
--   This is a 1:1 word-to-byte extraction, not a 4:1 unpacker. 
--   If you need to unpack 4 bytes from each 32-bit word, this is not that module.
--
-- Implementation:
--   Purely combinational passthrough. There are no registers, no state machine.
--   (aclk and aresetn are present for interface consistency but unused.)
--   Latency: zero clocks. Backpressure propagates directly.
--
-- TKEEP Handling:
--   TKEEP input has a default of all '1's, making it optional to connect.
--   We don't inspect or propagate TKEEP since we always extract bits [7:0]
--   and the downstream FIFO expects all bytes to be valid. Our particular setup sidesteps
--   partial deliveries of DMA transfers, and therefore TKEEP isn't needed.
--   It is included in case the re-use of this module requires other combinations 
--   of data words and DMA transfer widths, and those combinations do require TKEEP. 
--
-- Our Interfaces:
--   Input:  32-bit AXI-Stream from DMA (s_axis_*)
--   Output: 8-bit AXI-Stream to FIFO (m_axis_*)
--   TLAST is preserved to mark frame boundaries.
--
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
