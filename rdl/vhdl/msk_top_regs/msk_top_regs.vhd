------------------------------------------------------------------------------
--          ____  _____________  __                                         --
--         / __ \/ ____/ ___/\ \/ /                 _   _   _               --
--        / / / / __/  \__ \  \  /                 / \ / \ / \              --
--       / /_/ / /___ ___/ /  / /               = ( M | S | K )=            --
--      /_____/_____//____/  /_/                   \_/ \_/ \_/              --
--                                                                          --
------------------------------------------------------------------------------
--! @copyright Copyright 2021-2022 DESY
--! SPDX-License-Identifier: Apache-2.0
------------------------------------------------------------------------------
--! @date 2021-04-07
--! @author Michael Büchler <michael.buechler@desy.de>
--! @author Lukasz Butkowski <lukasz.butkowski@desy.de>
------------------------------------------------------------------------------
--! @brief
--! Top component of DesyRDL address space decoder for {node.type_name}
------------------------------------------------------------------------------

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

library desyrdl;
use desyrdl.common.all;

use work.pkg_msk_top_regs.all;

entity msk_top_regs is
  port (
    pi_clock : in std_logic;
    pi_reset : in std_logic;
    -- TOP subordinate memory mapped interface
    pi_s_reset : in std_logic := '0';
    pi_s_top   : in  t_msk_top_regs_m2s;
    po_s_top   : out t_msk_top_regs_s2m;
    -- to logic interface
    pi_addrmap : in  t_addrmap_msk_top_regs_in;
    po_addrmap : out t_addrmap_msk_top_regs_out
  );
end entity msk_top_regs;

architecture arch of msk_top_regs is

  type t_data_out is array (natural range<>) of std_logic_vector(C_DATA_WIDTH-1 downto 0) ;

  --
  signal reg_data_out_vect : t_data_out(26-1 downto 0);
  signal reg_rd_stb   : std_logic_vector(26-1 downto 0);
  signal reg_wr_stb   : std_logic_vector(26-1 downto 0);
  signal reg_data_in  : std_logic_vector(C_DATA_WIDTH-1 downto 0);
  signal reg_data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0) := (others => '0');
  --

begin

  ins_decoder_axi4l : entity work.msk_top_regs_decoder_axi4l
  generic map (
    g_addr_width    => C_ADDR_WIDTH,
    g_data_width    => C_DATA_WIDTH
  )
  port map (
    pi_clock      => pi_clock,
    pi_reset      => pi_reset,

    --
    po_reg_rd_stb => reg_rd_stb,
    po_reg_wr_stb => reg_wr_stb,
    po_reg_data   => reg_data_in,
    pi_reg_data   => reg_data_out,
    --
    --
    --
    --
    pi_s_reset  => pi_s_reset,
    pi_s_top    => pi_s_top,
    po_s_top    => po_s_top
  );
  --
  prs_reg_rd_mux: process(pi_clock)
  begin
    if rising_edge(pi_clock) then
      for idx in 0 to 26-1 loop
        if reg_rd_stb(idx) = '1' then
          reg_data_out <= reg_data_out_vect(idx);
        end if;
      end loop;
    end if;
  end process prs_reg_rd_mux;
  --
  --
  --

  -- ===========================================================================
  -- generated registers instances
  -- ---------------------------------------------------------------------------
  -- reg name: Hash_ID_Low  reg type: msk_hash_lo
  -- ---------------------------------------------------------------------------
  blk_Hash_ID_Low : block
  begin  --
    inst_Hash_ID_Low: entity work.msk_top_regs_msk_hash_lo
      port map(
        pi_clock        => pi_clock,
        pi_reset        => pi_reset,
        -- to/from adapter
        pi_decoder_rd_stb => reg_rd_stb(0),
        pi_decoder_wr_stb => reg_wr_stb(0),
        pi_decoder_data   => reg_data_in,
        po_decoder_data   => reg_data_out_vect(0),

        pi_reg  => pi_addrmap.Hash_ID_Low,
        po_reg  => po_addrmap.Hash_ID_Low
      ); --
  end block; --
  -- ---------------------------------------------------------------------------
  -- reg name: Hash_ID_High  reg type: msk_hash_hi
  -- ---------------------------------------------------------------------------
  blk_Hash_ID_High : block
  begin  --
    inst_Hash_ID_High: entity work.msk_top_regs_msk_hash_hi
      port map(
        pi_clock        => pi_clock,
        pi_reset        => pi_reset,
        -- to/from adapter
        pi_decoder_rd_stb => reg_rd_stb(1),
        pi_decoder_wr_stb => reg_wr_stb(1),
        pi_decoder_data   => reg_data_in,
        po_decoder_data   => reg_data_out_vect(1),

        pi_reg  => pi_addrmap.Hash_ID_High,
        po_reg  => po_addrmap.Hash_ID_High
      ); --
  end block; --
  -- ---------------------------------------------------------------------------
  -- reg name: MSK_Init  reg type: msk_init
  -- ---------------------------------------------------------------------------
  blk_MSK_Init : block
  begin  --
    inst_MSK_Init: entity work.msk_top_regs_msk_init
      port map(
        pi_clock        => pi_clock,
        pi_reset        => pi_reset,
        -- to/from adapter
        pi_decoder_rd_stb => reg_rd_stb(2),
        pi_decoder_wr_stb => reg_wr_stb(2),
        pi_decoder_data   => reg_data_in,
        po_decoder_data   => reg_data_out_vect(2),

        pi_reg  => pi_addrmap.MSK_Init,
        po_reg  => po_addrmap.MSK_Init
      ); --
  end block; --
  -- ---------------------------------------------------------------------------
  -- reg name: MSK_Control  reg type: msk_ctrl
  -- ---------------------------------------------------------------------------
  blk_MSK_Control : block
  begin  --
    inst_MSK_Control: entity work.msk_top_regs_msk_ctrl
      port map(
        pi_clock        => pi_clock,
        pi_reset        => pi_reset,
        -- to/from adapter
        pi_decoder_rd_stb => reg_rd_stb(3),
        pi_decoder_wr_stb => reg_wr_stb(3),
        pi_decoder_data   => reg_data_in,
        po_decoder_data   => reg_data_out_vect(3),

        pi_reg  => pi_addrmap.MSK_Control,
        po_reg  => po_addrmap.MSK_Control
      ); --
  end block; --
  -- ---------------------------------------------------------------------------
  -- reg name: MSK_Status  reg type: msk_stat_0
  -- ---------------------------------------------------------------------------
  blk_MSK_Status : block
  begin  --
    inst_MSK_Status: entity work.msk_top_regs_msk_stat_0
      port map(
        pi_clock        => pi_clock,
        pi_reset        => pi_reset,
        -- to/from adapter
        pi_decoder_rd_stb => reg_rd_stb(4),
        pi_decoder_wr_stb => reg_wr_stb(4),
        pi_decoder_data   => reg_data_in,
        po_decoder_data   => reg_data_out_vect(4),

        pi_reg  => pi_addrmap.MSK_Status,
        po_reg  => po_addrmap.MSK_Status
      ); --
  end block; --
  -- ---------------------------------------------------------------------------
  -- reg name: Tx_Bit_Count  reg type: msk_stat_1
  -- ---------------------------------------------------------------------------
  blk_Tx_Bit_Count : block
  begin  --
    inst_Tx_Bit_Count: entity work.msk_top_regs_msk_stat_1
      port map(
        pi_clock        => pi_clock,
        pi_reset        => pi_reset,
        -- to/from adapter
        pi_decoder_rd_stb => reg_rd_stb(5),
        pi_decoder_wr_stb => reg_wr_stb(5),
        pi_decoder_data   => reg_data_in,
        po_decoder_data   => reg_data_out_vect(5),

        pi_reg  => pi_addrmap.Tx_Bit_Count,
        po_reg  => po_addrmap.Tx_Bit_Count
      ); --
  end block; --
  -- ---------------------------------------------------------------------------
  -- reg name: Tx_Enable_Count  reg type: msk_stat_2
  -- ---------------------------------------------------------------------------
  blk_Tx_Enable_Count : block
  begin  --
    inst_Tx_Enable_Count: entity work.msk_top_regs_msk_stat_2
      port map(
        pi_clock        => pi_clock,
        pi_reset        => pi_reset,
        -- to/from adapter
        pi_decoder_rd_stb => reg_rd_stb(6),
        pi_decoder_wr_stb => reg_wr_stb(6),
        pi_decoder_data   => reg_data_in,
        po_decoder_data   => reg_data_out_vect(6),

        pi_reg  => pi_addrmap.Tx_Enable_Count,
        po_reg  => po_addrmap.Tx_Enable_Count
      ); --
  end block; --
  -- ---------------------------------------------------------------------------
  -- reg name: Fb_FreqWord  reg type: config_nco_fw
  -- ---------------------------------------------------------------------------
  blk_Fb_FreqWord : block
  begin  --
    inst_Fb_FreqWord: entity work.msk_top_regs_config_nco_fw
      port map(
        pi_clock        => pi_clock,
        pi_reset        => pi_reset,
        -- to/from adapter
        pi_decoder_rd_stb => reg_rd_stb(7),
        pi_decoder_wr_stb => reg_wr_stb(7),
        pi_decoder_data   => reg_data_in,
        po_decoder_data   => reg_data_out_vect(7),

        pi_reg  => pi_addrmap.Fb_FreqWord,
        po_reg  => po_addrmap.Fb_FreqWord
      ); --
  end block; --
  -- ---------------------------------------------------------------------------
  -- reg name: TX_F1_FreqWord  reg type: config_nco_fw
  -- ---------------------------------------------------------------------------
  blk_TX_F1_FreqWord : block
  begin  --
    inst_TX_F1_FreqWord: entity work.msk_top_regs_config_nco_fw
      port map(
        pi_clock        => pi_clock,
        pi_reset        => pi_reset,
        -- to/from adapter
        pi_decoder_rd_stb => reg_rd_stb(8),
        pi_decoder_wr_stb => reg_wr_stb(8),
        pi_decoder_data   => reg_data_in,
        po_decoder_data   => reg_data_out_vect(8),

        pi_reg  => pi_addrmap.TX_F1_FreqWord,
        po_reg  => po_addrmap.TX_F1_FreqWord
      ); --
  end block; --
  -- ---------------------------------------------------------------------------
  -- reg name: TX_F2_FreqWord  reg type: config_nco_fw
  -- ---------------------------------------------------------------------------
  blk_TX_F2_FreqWord : block
  begin  --
    inst_TX_F2_FreqWord: entity work.msk_top_regs_config_nco_fw
      port map(
        pi_clock        => pi_clock,
        pi_reset        => pi_reset,
        -- to/from adapter
        pi_decoder_rd_stb => reg_rd_stb(9),
        pi_decoder_wr_stb => reg_wr_stb(9),
        pi_decoder_data   => reg_data_in,
        po_decoder_data   => reg_data_out_vect(9),

        pi_reg  => pi_addrmap.TX_F2_FreqWord,
        po_reg  => po_addrmap.TX_F2_FreqWord
      ); --
  end block; --
  -- ---------------------------------------------------------------------------
  -- reg name: RX_F1_FreqWord  reg type: config_nco_fw
  -- ---------------------------------------------------------------------------
  blk_RX_F1_FreqWord : block
  begin  --
    inst_RX_F1_FreqWord: entity work.msk_top_regs_config_nco_fw
      port map(
        pi_clock        => pi_clock,
        pi_reset        => pi_reset,
        -- to/from adapter
        pi_decoder_rd_stb => reg_rd_stb(10),
        pi_decoder_wr_stb => reg_wr_stb(10),
        pi_decoder_data   => reg_data_in,
        po_decoder_data   => reg_data_out_vect(10),

        pi_reg  => pi_addrmap.RX_F1_FreqWord,
        po_reg  => po_addrmap.RX_F1_FreqWord
      ); --
  end block; --
  -- ---------------------------------------------------------------------------
  -- reg name: RX_F2_FreqWord  reg type: config_nco_fw
  -- ---------------------------------------------------------------------------
  blk_RX_F2_FreqWord : block
  begin  --
    inst_RX_F2_FreqWord: entity work.msk_top_regs_config_nco_fw
      port map(
        pi_clock        => pi_clock,
        pi_reset        => pi_reset,
        -- to/from adapter
        pi_decoder_rd_stb => reg_rd_stb(11),
        pi_decoder_wr_stb => reg_wr_stb(11),
        pi_decoder_data   => reg_data_in,
        po_decoder_data   => reg_data_out_vect(11),

        pi_reg  => pi_addrmap.RX_F2_FreqWord,
        po_reg  => po_addrmap.RX_F2_FreqWord
      ); --
  end block; --
  -- ---------------------------------------------------------------------------
  -- reg name: LPF_Config_0  reg type: lpf_config_0
  -- ---------------------------------------------------------------------------
  blk_LPF_Config_0 : block
  begin  --
    inst_LPF_Config_0: entity work.msk_top_regs_lpf_config_0
      port map(
        pi_clock        => pi_clock,
        pi_reset        => pi_reset,
        -- to/from adapter
        pi_decoder_rd_stb => reg_rd_stb(12),
        pi_decoder_wr_stb => reg_wr_stb(12),
        pi_decoder_data   => reg_data_in,
        po_decoder_data   => reg_data_out_vect(12),

        pi_reg  => pi_addrmap.LPF_Config_0,
        po_reg  => po_addrmap.LPF_Config_0
      ); --
  end block; --
  -- ---------------------------------------------------------------------------
  -- reg name: LPF_Config_1  reg type: lpf_config_1
  -- ---------------------------------------------------------------------------
  blk_LPF_Config_1 : block
  begin  --
    inst_LPF_Config_1: entity work.msk_top_regs_lpf_config_1
      port map(
        pi_clock        => pi_clock,
        pi_reset        => pi_reset,
        -- to/from adapter
        pi_decoder_rd_stb => reg_rd_stb(13),
        pi_decoder_wr_stb => reg_wr_stb(13),
        pi_decoder_data   => reg_data_in,
        po_decoder_data   => reg_data_out_vect(13),

        pi_reg  => pi_addrmap.LPF_Config_1,
        po_reg  => po_addrmap.LPF_Config_1
      ); --
  end block; --
  -- ---------------------------------------------------------------------------
  -- reg name: Tx_Data_Width  reg type: data_width
  -- ---------------------------------------------------------------------------
  blk_Tx_Data_Width : block
  begin  --
    inst_Tx_Data_Width: entity work.msk_top_regs_data_width
      port map(
        pi_clock        => pi_clock,
        pi_reset        => pi_reset,
        -- to/from adapter
        pi_decoder_rd_stb => reg_rd_stb(14),
        pi_decoder_wr_stb => reg_wr_stb(14),
        pi_decoder_data   => reg_data_in,
        po_decoder_data   => reg_data_out_vect(14),

        pi_reg  => pi_addrmap.Tx_Data_Width,
        po_reg  => po_addrmap.Tx_Data_Width
      ); --
  end block; --
  -- ---------------------------------------------------------------------------
  -- reg name: Rx_Data_Width  reg type: data_width
  -- ---------------------------------------------------------------------------
  blk_Rx_Data_Width : block
  begin  --
    inst_Rx_Data_Width: entity work.msk_top_regs_data_width
      port map(
        pi_clock        => pi_clock,
        pi_reset        => pi_reset,
        -- to/from adapter
        pi_decoder_rd_stb => reg_rd_stb(15),
        pi_decoder_wr_stb => reg_wr_stb(15),
        pi_decoder_data   => reg_data_in,
        po_decoder_data   => reg_data_out_vect(15),

        pi_reg  => pi_addrmap.Rx_Data_Width,
        po_reg  => po_addrmap.Rx_Data_Width
      ); --
  end block; --
  -- ---------------------------------------------------------------------------
  -- reg name: PRBS_Control  reg type: prbs_ctrl
  -- ---------------------------------------------------------------------------
  blk_PRBS_Control : block
  begin  --
    inst_PRBS_Control: entity work.msk_top_regs_prbs_ctrl
      port map(
        pi_clock        => pi_clock,
        pi_reset        => pi_reset,
        -- to/from adapter
        pi_decoder_rd_stb => reg_rd_stb(16),
        pi_decoder_wr_stb => reg_wr_stb(16),
        pi_decoder_data   => reg_data_in,
        po_decoder_data   => reg_data_out_vect(16),

        pi_reg  => pi_addrmap.PRBS_Control,
        po_reg  => po_addrmap.PRBS_Control
      ); --
  end block; --
  -- ---------------------------------------------------------------------------
  -- reg name: PRBS_Initial_State  reg type: config_prbs_seed
  -- ---------------------------------------------------------------------------
  blk_PRBS_Initial_State : block
  begin  --
    inst_PRBS_Initial_State: entity work.msk_top_regs_config_prbs_seed
      port map(
        pi_clock        => pi_clock,
        pi_reset        => pi_reset,
        -- to/from adapter
        pi_decoder_rd_stb => reg_rd_stb(17),
        pi_decoder_wr_stb => reg_wr_stb(17),
        pi_decoder_data   => reg_data_in,
        po_decoder_data   => reg_data_out_vect(17),

        pi_reg  => pi_addrmap.PRBS_Initial_State,
        po_reg  => po_addrmap.PRBS_Initial_State
      ); --
  end block; --
  -- ---------------------------------------------------------------------------
  -- reg name: PRBS_Polynomial  reg type: config_prbs_poly
  -- ---------------------------------------------------------------------------
  blk_PRBS_Polynomial : block
  begin  --
    inst_PRBS_Polynomial: entity work.msk_top_regs_config_prbs_poly
      port map(
        pi_clock        => pi_clock,
        pi_reset        => pi_reset,
        -- to/from adapter
        pi_decoder_rd_stb => reg_rd_stb(18),
        pi_decoder_wr_stb => reg_wr_stb(18),
        pi_decoder_data   => reg_data_in,
        po_decoder_data   => reg_data_out_vect(18),

        pi_reg  => pi_addrmap.PRBS_Polynomial,
        po_reg  => po_addrmap.PRBS_Polynomial
      ); --
  end block; --
  -- ---------------------------------------------------------------------------
  -- reg name: PRBS_Error_Mask  reg type: config_prbs_errmask
  -- ---------------------------------------------------------------------------
  blk_PRBS_Error_Mask : block
  begin  --
    inst_PRBS_Error_Mask: entity work.msk_top_regs_config_prbs_errmask
      port map(
        pi_clock        => pi_clock,
        pi_reset        => pi_reset,
        -- to/from adapter
        pi_decoder_rd_stb => reg_rd_stb(19),
        pi_decoder_wr_stb => reg_wr_stb(19),
        pi_decoder_data   => reg_data_in,
        po_decoder_data   => reg_data_out_vect(19),

        pi_reg  => pi_addrmap.PRBS_Error_Mask,
        po_reg  => po_addrmap.PRBS_Error_Mask
      ); --
  end block; --
  -- ---------------------------------------------------------------------------
  -- reg name: PRBS_Bit_Count  reg type: stat_32_bits
  -- ---------------------------------------------------------------------------
  blk_PRBS_Bit_Count : block
  begin  --
    inst_PRBS_Bit_Count: entity work.msk_top_regs_stat_32_bits
      port map(
        pi_clock        => pi_clock,
        pi_reset        => pi_reset,
        -- to/from adapter
        pi_decoder_rd_stb => reg_rd_stb(20),
        pi_decoder_wr_stb => reg_wr_stb(20),
        pi_decoder_data   => reg_data_in,
        po_decoder_data   => reg_data_out_vect(20),

        pi_reg  => pi_addrmap.PRBS_Bit_Count,
        po_reg  => po_addrmap.PRBS_Bit_Count
      ); --
  end block; --
  -- ---------------------------------------------------------------------------
  -- reg name: PRBS_Error_Count  reg type: stat_32_errs
  -- ---------------------------------------------------------------------------
  blk_PRBS_Error_Count : block
  begin  --
    inst_PRBS_Error_Count: entity work.msk_top_regs_stat_32_errs
      port map(
        pi_clock        => pi_clock,
        pi_reset        => pi_reset,
        -- to/from adapter
        pi_decoder_rd_stb => reg_rd_stb(21),
        pi_decoder_wr_stb => reg_wr_stb(21),
        pi_decoder_data   => reg_data_in,
        po_decoder_data   => reg_data_out_vect(21),

        pi_reg  => pi_addrmap.PRBS_Error_Count,
        po_reg  => po_addrmap.PRBS_Error_Count
      ); --
  end block; --
  -- ---------------------------------------------------------------------------
  -- reg name: LPF_Accum_F1  reg type: stat_32_lpf_acc
  -- ---------------------------------------------------------------------------
  blk_LPF_Accum_F1 : block
  begin  --
    inst_LPF_Accum_F1: entity work.msk_top_regs_stat_32_lpf_acc
      port map(
        pi_clock        => pi_clock,
        pi_reset        => pi_reset,
        -- to/from adapter
        pi_decoder_rd_stb => reg_rd_stb(22),
        pi_decoder_wr_stb => reg_wr_stb(22),
        pi_decoder_data   => reg_data_in,
        po_decoder_data   => reg_data_out_vect(22),

        pi_reg  => pi_addrmap.LPF_Accum_F1,
        po_reg  => po_addrmap.LPF_Accum_F1
      ); --
  end block; --
  -- ---------------------------------------------------------------------------
  -- reg name: LPF_Accum_F2  reg type: stat_32_lpf_acc
  -- ---------------------------------------------------------------------------
  blk_LPF_Accum_F2 : block
  begin  --
    inst_LPF_Accum_F2: entity work.msk_top_regs_stat_32_lpf_acc
      port map(
        pi_clock        => pi_clock,
        pi_reset        => pi_reset,
        -- to/from adapter
        pi_decoder_rd_stb => reg_rd_stb(23),
        pi_decoder_wr_stb => reg_wr_stb(23),
        pi_decoder_data   => reg_data_in,
        po_decoder_data   => reg_data_out_vect(23),

        pi_reg  => pi_addrmap.LPF_Accum_F2,
        po_reg  => po_addrmap.LPF_Accum_F2
      ); --
  end block; --
  -- ---------------------------------------------------------------------------
  -- reg name: axis_xfer_count  reg type: msk_stat_3
  -- ---------------------------------------------------------------------------
  blk_axis_xfer_count : block
  begin  --
    inst_axis_xfer_count: entity work.msk_top_regs_msk_stat_3
      port map(
        pi_clock        => pi_clock,
        pi_reset        => pi_reset,
        -- to/from adapter
        pi_decoder_rd_stb => reg_rd_stb(24),
        pi_decoder_wr_stb => reg_wr_stb(24),
        pi_decoder_data   => reg_data_in,
        po_decoder_data   => reg_data_out_vect(24),

        pi_reg  => pi_addrmap.axis_xfer_count,
        po_reg  => po_addrmap.axis_xfer_count
      ); --
  end block; --
  -- ---------------------------------------------------------------------------
  -- reg name: Rx_Sample_Discard  reg type: rx_sample_discard
  -- ---------------------------------------------------------------------------
  blk_Rx_Sample_Discard : block
  begin  --
    inst_Rx_Sample_Discard: entity work.msk_top_regs_rx_sample_discard
      port map(
        pi_clock        => pi_clock,
        pi_reset        => pi_reset,
        -- to/from adapter
        pi_decoder_rd_stb => reg_rd_stb(25),
        pi_decoder_wr_stb => reg_wr_stb(25),
        pi_decoder_data   => reg_data_in,
        po_decoder_data   => reg_data_out_vect(25),

        pi_reg  => pi_addrmap.Rx_Sample_Discard,
        po_reg  => po_addrmap.Rx_Sample_Discard
      ); --
  end block; --

  -- ===========================================================================
  -- generated registers instances in regfiles 

  -- ===========================================================================
  -- Generated Meme Instances
  --
  -- ---------------------------------------------------------------------------

  -- ===========================================================================
  -- External Busses

end architecture;
