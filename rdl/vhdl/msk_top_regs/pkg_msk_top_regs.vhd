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
--! @date 2021-10-01
--! @author Michael Büchler <michael.buechler@desy.de>
--! @author Lukasz Butkowski <lukasz.butkowski@desy.de>
------------------------------------------------------------------------------
--! @brief
--! VHDL package of DesyRDL for address space decoder for {node.orig_type_name}
------------------------------------------------------------------------------

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

library desyrdl;
use desyrdl.common.all;

-- library desy;
-- use desy.common_axi.all;

package pkg_msk_top_regs is

  -----------------------------------------------
  -- per addrmap / module
  -----------------------------------------------
  constant C_ADDR_WIDTH : integer := 7;
  constant C_DATA_WIDTH : integer := 32;

  -- ===========================================================================
  -- ---------------------------------------------------------------------------
  -- registers
  -- ---------------------------------------------------------------------------

  -- ===========================================================================
  -- REGISTERS interface
  -- ---------------------------------------------------------------------------
  -- register type: msk_hash_lo_desc_3fd0e28e
  -----------------------------------------------
  type t_field_signals_msk_hash_lo_desc_3fd0e28e_hash_id_lo_desc_876ef6a2_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_msk_hash_lo_desc_3fd0e28e_hash_id_lo_desc_876ef6a2_out is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record; --

  -- The actual register types
  type t_reg_msk_hash_lo_desc_3fd0e28e_in is record--
    hash_id_lo_desc_876ef6a2 : t_field_signals_msk_hash_lo_desc_3fd0e28e_hash_id_lo_desc_876ef6a2_in; --
  end record;
  type t_reg_msk_hash_lo_desc_3fd0e28e_out is record--
    hash_id_lo_desc_876ef6a2 : t_field_signals_msk_hash_lo_desc_3fd0e28e_hash_id_lo_desc_876ef6a2_out; --
  end record;
  type t_reg_msk_hash_lo_desc_3fd0e28e_2d_in is array (integer range <>) of t_reg_msk_hash_lo_desc_3fd0e28e_in;
  type t_reg_msk_hash_lo_desc_3fd0e28e_2d_out is array (integer range <>) of t_reg_msk_hash_lo_desc_3fd0e28e_out;
  type t_reg_msk_hash_lo_desc_3fd0e28e_3d_in is array (integer range <>, integer range <>) of t_reg_msk_hash_lo_desc_3fd0e28e_in;
  type t_reg_msk_hash_lo_desc_3fd0e28e_3d_out is array (integer range <>, integer range <>) of t_reg_msk_hash_lo_desc_3fd0e28e_out;
  -----------------------------------------------
  -- register type: msk_hash_hi_desc_3fd0e28e
  -----------------------------------------------
  type t_field_signals_msk_hash_hi_desc_3fd0e28e_hash_id_hi_desc_74f3badc_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_msk_hash_hi_desc_3fd0e28e_hash_id_hi_desc_74f3badc_out is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record; --

  -- The actual register types
  type t_reg_msk_hash_hi_desc_3fd0e28e_in is record--
    hash_id_hi_desc_74f3badc : t_field_signals_msk_hash_hi_desc_3fd0e28e_hash_id_hi_desc_74f3badc_in; --
  end record;
  type t_reg_msk_hash_hi_desc_3fd0e28e_out is record--
    hash_id_hi_desc_74f3badc : t_field_signals_msk_hash_hi_desc_3fd0e28e_hash_id_hi_desc_74f3badc_out; --
  end record;
  type t_reg_msk_hash_hi_desc_3fd0e28e_2d_in is array (integer range <>) of t_reg_msk_hash_hi_desc_3fd0e28e_in;
  type t_reg_msk_hash_hi_desc_3fd0e28e_2d_out is array (integer range <>) of t_reg_msk_hash_hi_desc_3fd0e28e_out;
  type t_reg_msk_hash_hi_desc_3fd0e28e_3d_in is array (integer range <>, integer range <>) of t_reg_msk_hash_hi_desc_3fd0e28e_in;
  type t_reg_msk_hash_hi_desc_3fd0e28e_3d_out is array (integer range <>, integer range <>) of t_reg_msk_hash_hi_desc_3fd0e28e_out;
  -----------------------------------------------
  -- register type: msk_init
  -----------------------------------------------
  type t_field_signals_msk_init_init_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_msk_init_init_out is record
    data : std_logic_vector(1-1 downto 0); --
  end record; --

  -- The actual register types
  type t_reg_msk_init_in is record--
    init : t_field_signals_msk_init_init_in; --
  end record;
  type t_reg_msk_init_out is record--
    init : t_field_signals_msk_init_init_out; --
  end record;
  type t_reg_msk_init_2d_in is array (integer range <>) of t_reg_msk_init_in;
  type t_reg_msk_init_2d_out is array (integer range <>) of t_reg_msk_init_out;
  type t_reg_msk_init_3d_in is array (integer range <>, integer range <>) of t_reg_msk_init_in;
  type t_reg_msk_init_3d_out is array (integer range <>, integer range <>) of t_reg_msk_init_out;
  -----------------------------------------------
  -- register type: msk_ctrl
  -----------------------------------------------
  type t_field_signals_msk_ctrl_ptt_desc_209a923a_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_msk_ctrl_ptt_desc_209a923a_out is record
    data : std_logic_vector(1-1 downto 0); --
  end record; --
  type t_field_signals_msk_ctrl_loopback_ena_desc_6617b8f3_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_msk_ctrl_loopback_ena_desc_6617b8f3_out is record
    data : std_logic_vector(1-1 downto 0); --
  end record; --
  type t_field_signals_msk_ctrl_rx_invert_desc_643ee034_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_msk_ctrl_rx_invert_desc_643ee034_out is record
    data : std_logic_vector(1-1 downto 0); --
  end record; --
  type t_field_signals_msk_ctrl_clear_counts_desc_52baf732_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_msk_ctrl_clear_counts_desc_52baf732_out is record
    data : std_logic_vector(1-1 downto 0); --
  end record; --

  -- The actual register types
  type t_reg_msk_ctrl_in is record--
    ptt_desc_209a923a : t_field_signals_msk_ctrl_ptt_desc_209a923a_in; --
    loopback_ena_desc_6617b8f3 : t_field_signals_msk_ctrl_loopback_ena_desc_6617b8f3_in; --
    rx_invert_desc_643ee034 : t_field_signals_msk_ctrl_rx_invert_desc_643ee034_in; --
    clear_counts_desc_52baf732 : t_field_signals_msk_ctrl_clear_counts_desc_52baf732_in; --
  end record;
  type t_reg_msk_ctrl_out is record--
    ptt_desc_209a923a : t_field_signals_msk_ctrl_ptt_desc_209a923a_out; --
    loopback_ena_desc_6617b8f3 : t_field_signals_msk_ctrl_loopback_ena_desc_6617b8f3_out; --
    rx_invert_desc_643ee034 : t_field_signals_msk_ctrl_rx_invert_desc_643ee034_out; --
    clear_counts_desc_52baf732 : t_field_signals_msk_ctrl_clear_counts_desc_52baf732_out; --
  end record;
  type t_reg_msk_ctrl_2d_in is array (integer range <>) of t_reg_msk_ctrl_in;
  type t_reg_msk_ctrl_2d_out is array (integer range <>) of t_reg_msk_ctrl_out;
  type t_reg_msk_ctrl_3d_in is array (integer range <>, integer range <>) of t_reg_msk_ctrl_in;
  type t_reg_msk_ctrl_3d_out is array (integer range <>, integer range <>) of t_reg_msk_ctrl_out;
  -----------------------------------------------
  -- register type: msk_stat_0
  -----------------------------------------------
  type t_field_signals_msk_stat_0_demod_sync_lock_in is record
    data : std_logic_vector(1-1 downto 0); --
  end record;

  type t_field_signals_msk_stat_0_demod_sync_lock_out is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record; --
  type t_field_signals_msk_stat_0_tx_enable_in is record
    data : std_logic_vector(1-1 downto 0); --
  end record;

  type t_field_signals_msk_stat_0_tx_enable_out is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record; --
  type t_field_signals_msk_stat_0_rx_enable_in is record
    data : std_logic_vector(1-1 downto 0); --
  end record;

  type t_field_signals_msk_stat_0_rx_enable_out is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record; --

  -- The actual register types
  type t_reg_msk_stat_0_in is record--
    demod_sync_lock : t_field_signals_msk_stat_0_demod_sync_lock_in; --
    tx_enable : t_field_signals_msk_stat_0_tx_enable_in; --
    rx_enable : t_field_signals_msk_stat_0_rx_enable_in; --
  end record;
  type t_reg_msk_stat_0_out is record--
    demod_sync_lock : t_field_signals_msk_stat_0_demod_sync_lock_out; --
    tx_enable : t_field_signals_msk_stat_0_tx_enable_out; --
    rx_enable : t_field_signals_msk_stat_0_rx_enable_out; --
  end record;
  type t_reg_msk_stat_0_2d_in is array (integer range <>) of t_reg_msk_stat_0_in;
  type t_reg_msk_stat_0_2d_out is array (integer range <>) of t_reg_msk_stat_0_out;
  type t_reg_msk_stat_0_3d_in is array (integer range <>, integer range <>) of t_reg_msk_stat_0_in;
  type t_reg_msk_stat_0_3d_out is array (integer range <>, integer range <>) of t_reg_msk_stat_0_out;
  -----------------------------------------------
  -- register type: msk_stat_1
  -----------------------------------------------
  type t_field_signals_msk_stat_1_tx_bit_cntr_in is record
    data : std_logic_vector(32-1 downto 0); --
    incr : std_logic; --
  end record;

  type t_field_signals_msk_stat_1_tx_bit_cntr_out is record
    data : std_logic_vector(32-1 downto 0); --
  end record; --

  -- The actual register types
  type t_reg_msk_stat_1_in is record--
    tx_bit_cntr : t_field_signals_msk_stat_1_tx_bit_cntr_in; --
  end record;
  type t_reg_msk_stat_1_out is record--
    tx_bit_cntr : t_field_signals_msk_stat_1_tx_bit_cntr_out; --
  end record;
  type t_reg_msk_stat_1_2d_in is array (integer range <>) of t_reg_msk_stat_1_in;
  type t_reg_msk_stat_1_2d_out is array (integer range <>) of t_reg_msk_stat_1_out;
  type t_reg_msk_stat_1_3d_in is array (integer range <>, integer range <>) of t_reg_msk_stat_1_in;
  type t_reg_msk_stat_1_3d_out is array (integer range <>, integer range <>) of t_reg_msk_stat_1_out;
  -----------------------------------------------
  -- register type: msk_stat_2
  -----------------------------------------------
  type t_field_signals_msk_stat_2_tx_ena_cntr_in is record
    data : std_logic_vector(32-1 downto 0); --
    incr : std_logic; --
    decr : std_logic; --
  end record;

  type t_field_signals_msk_stat_2_tx_ena_cntr_out is record
    data : std_logic_vector(32-1 downto 0); --
  end record; --

  -- The actual register types
  type t_reg_msk_stat_2_in is record--
    tx_ena_cntr : t_field_signals_msk_stat_2_tx_ena_cntr_in; --
  end record;
  type t_reg_msk_stat_2_out is record--
    tx_ena_cntr : t_field_signals_msk_stat_2_tx_ena_cntr_out; --
  end record;
  type t_reg_msk_stat_2_2d_in is array (integer range <>) of t_reg_msk_stat_2_in;
  type t_reg_msk_stat_2_2d_out is array (integer range <>) of t_reg_msk_stat_2_out;
  type t_reg_msk_stat_2_3d_in is array (integer range <>, integer range <>) of t_reg_msk_stat_2_in;
  type t_reg_msk_stat_2_3d_out is array (integer range <>, integer range <>) of t_reg_msk_stat_2_out;
  -----------------------------------------------
  -- register type: config_32
  -----------------------------------------------
  type t_field_signals_config_32_config_data_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_config_32_config_data_out is record
    data : std_logic_vector(32-1 downto 0); --
  end record; --

  -- The actual register types
  type t_reg_config_32_in is record--
    config_data : t_field_signals_config_32_config_data_in; --
  end record;
  type t_reg_config_32_out is record--
    config_data : t_field_signals_config_32_config_data_out; --
  end record;
  type t_reg_config_32_2d_in is array (integer range <>) of t_reg_config_32_in;
  type t_reg_config_32_2d_out is array (integer range <>) of t_reg_config_32_out;
  type t_reg_config_32_3d_in is array (integer range <>, integer range <>) of t_reg_config_32_in;
  type t_reg_config_32_3d_out is array (integer range <>, integer range <>) of t_reg_config_32_out;
  -----------------------------------------------
  -- register type: lpf_config_0
  -----------------------------------------------
  type t_field_signals_lpf_config_0_lpf_freeze_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_lpf_config_0_lpf_freeze_out is record
    data : std_logic_vector(1-1 downto 0); --
  end record; --
  type t_field_signals_lpf_config_0_lpf_zero_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_lpf_config_0_lpf_zero_out is record
    data : std_logic_vector(1-1 downto 0); --
  end record; --
  type t_field_signals_lpf_config_0_lpf_alpha_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_lpf_config_0_lpf_alpha_out is record
    data : std_logic_vector(16-1 downto 0); --
  end record; --

  -- The actual register types
  type t_reg_lpf_config_0_in is record--
    lpf_freeze : t_field_signals_lpf_config_0_lpf_freeze_in; --
    lpf_zero : t_field_signals_lpf_config_0_lpf_zero_in; --
    lpf_alpha : t_field_signals_lpf_config_0_lpf_alpha_in; --
  end record;
  type t_reg_lpf_config_0_out is record--
    lpf_freeze : t_field_signals_lpf_config_0_lpf_freeze_out; --
    lpf_zero : t_field_signals_lpf_config_0_lpf_zero_out; --
    lpf_alpha : t_field_signals_lpf_config_0_lpf_alpha_out; --
  end record;
  type t_reg_lpf_config_0_2d_in is array (integer range <>) of t_reg_lpf_config_0_in;
  type t_reg_lpf_config_0_2d_out is array (integer range <>) of t_reg_lpf_config_0_out;
  type t_reg_lpf_config_0_3d_in is array (integer range <>, integer range <>) of t_reg_lpf_config_0_in;
  type t_reg_lpf_config_0_3d_out is array (integer range <>, integer range <>) of t_reg_lpf_config_0_out;
  -----------------------------------------------
  -- register type: lpf_config_1
  -----------------------------------------------
  type t_field_signals_lpf_config_1_i_gain_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_lpf_config_1_i_gain_out is record
    data : std_logic_vector(16-1 downto 0); --
  end record; --
  type t_field_signals_lpf_config_1_p_gain_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_lpf_config_1_p_gain_out is record
    data : std_logic_vector(16-1 downto 0); --
  end record; --

  -- The actual register types
  type t_reg_lpf_config_1_in is record--
    i_gain : t_field_signals_lpf_config_1_i_gain_in; --
    p_gain : t_field_signals_lpf_config_1_p_gain_in; --
  end record;
  type t_reg_lpf_config_1_out is record--
    i_gain : t_field_signals_lpf_config_1_i_gain_out; --
    p_gain : t_field_signals_lpf_config_1_p_gain_out; --
  end record;
  type t_reg_lpf_config_1_2d_in is array (integer range <>) of t_reg_lpf_config_1_in;
  type t_reg_lpf_config_1_2d_out is array (integer range <>) of t_reg_lpf_config_1_out;
  type t_reg_lpf_config_1_3d_in is array (integer range <>, integer range <>) of t_reg_lpf_config_1_in;
  type t_reg_lpf_config_1_3d_out is array (integer range <>, integer range <>) of t_reg_lpf_config_1_out;
  -----------------------------------------------
  -- register type: data_width
  -----------------------------------------------
  type t_field_signals_data_width_data_width_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_data_width_data_width_out is record
    data : std_logic_vector(8-1 downto 0); --
  end record; --

  -- The actual register types
  type t_reg_data_width_in is record--
    data_width : t_field_signals_data_width_data_width_in; --
  end record;
  type t_reg_data_width_out is record--
    data_width : t_field_signals_data_width_data_width_out; --
  end record;
  type t_reg_data_width_2d_in is array (integer range <>) of t_reg_data_width_in;
  type t_reg_data_width_2d_out is array (integer range <>) of t_reg_data_width_out;
  type t_reg_data_width_3d_in is array (integer range <>, integer range <>) of t_reg_data_width_in;
  type t_reg_data_width_3d_out is array (integer range <>, integer range <>) of t_reg_data_width_out;
  -----------------------------------------------
  -- register type: prbs_ctrl
  -----------------------------------------------
  type t_field_signals_prbs_ctrl_prbs_sel_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_prbs_ctrl_prbs_sel_out is record
    data : std_logic_vector(1-1 downto 0); --
  end record; --
  type t_field_signals_prbs_ctrl_prbs_error_insert_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_prbs_ctrl_prbs_error_insert_out is record
    data : std_logic_vector(1-1 downto 0); --
  end record; --
  type t_field_signals_prbs_ctrl_prbs_clear_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_prbs_ctrl_prbs_clear_out is record
    data : std_logic_vector(1-1 downto 0); --
  end record; --
  type t_field_signals_prbs_ctrl_prbs_sync_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_prbs_ctrl_prbs_sync_out is record
    data : std_logic_vector(1-1 downto 0); --
  end record; --

  -- The actual register types
  type t_reg_prbs_ctrl_in is record--
    prbs_sel : t_field_signals_prbs_ctrl_prbs_sel_in; --
    prbs_error_insert : t_field_signals_prbs_ctrl_prbs_error_insert_in; --
    prbs_clear : t_field_signals_prbs_ctrl_prbs_clear_in; --
    prbs_sync : t_field_signals_prbs_ctrl_prbs_sync_in; --
  end record;
  type t_reg_prbs_ctrl_out is record--
    prbs_sel : t_field_signals_prbs_ctrl_prbs_sel_out; --
    prbs_error_insert : t_field_signals_prbs_ctrl_prbs_error_insert_out; --
    prbs_clear : t_field_signals_prbs_ctrl_prbs_clear_out; --
    prbs_sync : t_field_signals_prbs_ctrl_prbs_sync_out; --
  end record;
  type t_reg_prbs_ctrl_2d_in is array (integer range <>) of t_reg_prbs_ctrl_in;
  type t_reg_prbs_ctrl_2d_out is array (integer range <>) of t_reg_prbs_ctrl_out;
  type t_reg_prbs_ctrl_3d_in is array (integer range <>, integer range <>) of t_reg_prbs_ctrl_in;
  type t_reg_prbs_ctrl_3d_out is array (integer range <>, integer range <>) of t_reg_prbs_ctrl_out;
  -----------------------------------------------
  -- register type: stat_32
  -----------------------------------------------
  type t_field_signals_stat_32_status_data_in is record
    data : std_logic_vector(32-1 downto 0); --
  end record;

  type t_field_signals_stat_32_status_data_out is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record; --

  -- The actual register types
  type t_reg_stat_32_in is record--
    status_data : t_field_signals_stat_32_status_data_in; --
  end record;
  type t_reg_stat_32_out is record--
    status_data : t_field_signals_stat_32_status_data_out; --
  end record;
  type t_reg_stat_32_2d_in is array (integer range <>) of t_reg_stat_32_in;
  type t_reg_stat_32_2d_out is array (integer range <>) of t_reg_stat_32_out;
  type t_reg_stat_32_3d_in is array (integer range <>, integer range <>) of t_reg_stat_32_in;
  type t_reg_stat_32_3d_out is array (integer range <>, integer range <>) of t_reg_stat_32_out;
  -----------------------------------------------

  ------------------------------------------------------------------------------
  -- Register types in regfiles --

  -- ===========================================================================
  -- REGFILE interface
  -- -----------------------------------------------------------------------------

  -- ===========================================================================
  -- MEMORIES interface
  -- ---------------------------------------------------------------------------

  -- ===========================================================================
  -- msk_top_regs : Top module address map interface
  -- ---------------------------------------------------------------------------
  type t_addrmap_msk_top_regs_in is record
    --
    Hash_ID_Low : t_reg_msk_hash_lo_desc_3fd0e28e_in; --
    Hash_ID_High : t_reg_msk_hash_hi_desc_3fd0e28e_in; --
    MSK_Init : t_reg_msk_init_in; --
    MSK_Control : t_reg_msk_ctrl_in; --
    MSK_Status : t_reg_msk_stat_0_in; --
    Tx_Bit_Count : t_reg_msk_stat_1_in; --
    Tx_Enable_Count : t_reg_msk_stat_2_in; --
    Fb_FreqWord : t_reg_config_32_in; --
    F1_FreqWord : t_reg_config_32_in; --
    F2_FreqWord : t_reg_config_32_in; --
    LPF_Config_0 : t_reg_lpf_config_0_in; --
    LPF_Config_1 : t_reg_lpf_config_1_in; --
    Tx_Data_Width : t_reg_data_width_in; --
    Rx_Data_Width : t_reg_data_width_in; --
    PRBS_Control : t_reg_prbs_ctrl_in; --
    PRBS_Initial_State : t_reg_config_32_in; --
    PRBS_Polynomial : t_reg_config_32_in; --
    PRBS_Error_Mask : t_reg_config_32_in; --
    PRBS_Bit_Count : t_reg_stat_32_in; --
    PRBS_Error_Count : t_reg_stat_32_in; --
    --
    --
    --
  end record;

  type t_addrmap_msk_top_regs_out is record
    --
    Hash_ID_Low : t_reg_msk_hash_lo_desc_3fd0e28e_out; --
    Hash_ID_High : t_reg_msk_hash_hi_desc_3fd0e28e_out; --
    MSK_Init : t_reg_msk_init_out; --
    MSK_Control : t_reg_msk_ctrl_out; --
    MSK_Status : t_reg_msk_stat_0_out; --
    Tx_Bit_Count : t_reg_msk_stat_1_out; --
    Tx_Enable_Count : t_reg_msk_stat_2_out; --
    Fb_FreqWord : t_reg_config_32_out; --
    F1_FreqWord : t_reg_config_32_out; --
    F2_FreqWord : t_reg_config_32_out; --
    LPF_Config_0 : t_reg_lpf_config_0_out; --
    LPF_Config_1 : t_reg_lpf_config_1_out; --
    Tx_Data_Width : t_reg_data_width_out; --
    Rx_Data_Width : t_reg_data_width_out; --
    PRBS_Control : t_reg_prbs_ctrl_out; --
    PRBS_Initial_State : t_reg_config_32_out; --
    PRBS_Polynomial : t_reg_config_32_out; --
    PRBS_Error_Mask : t_reg_config_32_out; --
    PRBS_Bit_Count : t_reg_stat_32_out; --
    PRBS_Error_Count : t_reg_stat_32_out; --
    --
    --
    --
  end record;

  -- ===========================================================================
  -- top level component declaration
  -- must come after defining the interfaces
  -- ---------------------------------------------------------------------------
  subtype t_msk_top_regs_m2s is t_axi4l_m2s;
  subtype t_msk_top_regs_s2m is t_axi4l_s2m;

  component msk_top_regs is
      port (
        pi_clock : in std_logic;
        pi_reset : in std_logic;
        -- TOP subordinate memory mapped interface
        pi_s_top  : in  t_msk_top_regs_m2s;
        po_s_top  : out t_msk_top_regs_s2m;
        -- to logic interface
        pi_addrmap : in  t_addrmap_msk_top_regs_in;
        po_addrmap : out t_addrmap_msk_top_regs_out
      );
  end component msk_top_regs;

end package pkg_msk_top_regs;
--------------------------------------------------------------------------------
package body pkg_msk_top_regs is
end package body;

--==============================================================================


--------------------------------------------------------------------------------
-- Register types directly in addmap
--------------------------------------------------------------------------------
--
-- register type: msk_hash_lo_desc_3fd0e28e
-----------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

use work.pkg_msk_top_regs.all;

entity msk_top_regs_msk_hash_lo_desc_3fd0e28e is
  port (
    pi_clock        : in  std_logic;
    pi_reset        : in  std_logic;
    -- to/from adapter
    pi_decoder_rd_stb : in  std_logic;
    pi_decoder_wr_stb : in  std_logic;
    pi_decoder_data   : in  std_logic_vector(C_DATA_WIDTH-1 downto 0);
    po_decoder_data   : out std_logic_vector(C_DATA_WIDTH-1 downto 0);

    pi_reg  : in t_reg_msk_hash_lo_desc_3fd0e28e_in ;
    po_reg  : out t_reg_msk_hash_lo_desc_3fd0e28e_out
  );
end entity msk_top_regs_msk_hash_lo_desc_3fd0e28e;

architecture rtl of msk_top_regs_msk_hash_lo_desc_3fd0e28e is
  signal data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0) := (others => '0');
begin
  --

  -- resize field data out to the register bus width
  -- do only if 1 field and signed--
  po_decoder_data <= data_out; --

  ------------------------------------------------------------WIRE
  hash_id_lo_desc_876ef6a2_wire : block--
  begin
    --
    data_out(31 downto 0) <= std_logic_vector(to_signed(-1431677611,32)); --
    --no signal to read by HW
    po_reg.hash_id_lo_desc_876ef6a2.data <= (others => '0'); --
  end block; --
end rtl;
-----------------------------------------------
-- register type: msk_hash_hi_desc_3fd0e28e
-----------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

use work.pkg_msk_top_regs.all;

entity msk_top_regs_msk_hash_hi_desc_3fd0e28e is
  port (
    pi_clock        : in  std_logic;
    pi_reset        : in  std_logic;
    -- to/from adapter
    pi_decoder_rd_stb : in  std_logic;
    pi_decoder_wr_stb : in  std_logic;
    pi_decoder_data   : in  std_logic_vector(C_DATA_WIDTH-1 downto 0);
    po_decoder_data   : out std_logic_vector(C_DATA_WIDTH-1 downto 0);

    pi_reg  : in t_reg_msk_hash_hi_desc_3fd0e28e_in ;
    po_reg  : out t_reg_msk_hash_hi_desc_3fd0e28e_out
  );
end entity msk_top_regs_msk_hash_hi_desc_3fd0e28e;

architecture rtl of msk_top_regs_msk_hash_hi_desc_3fd0e28e is
  signal data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0) := (others => '0');
begin
  --

  -- resize field data out to the register bus width
  -- do only if 1 field and signed--
  po_decoder_data <= data_out; --

  ------------------------------------------------------------WIRE
  hash_id_hi_desc_74f3badc_wire : block--
  begin
    --
    data_out(31 downto 0) <= std_logic_vector(to_signed(1431677610,32)); --
    --no signal to read by HW
    po_reg.hash_id_hi_desc_74f3badc.data <= (others => '0'); --
  end block; --
end rtl;
-----------------------------------------------
-- register type: msk_init
-----------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

use work.pkg_msk_top_regs.all;

entity msk_top_regs_msk_init is
  port (
    pi_clock        : in  std_logic;
    pi_reset        : in  std_logic;
    -- to/from adapter
    pi_decoder_rd_stb : in  std_logic;
    pi_decoder_wr_stb : in  std_logic;
    pi_decoder_data   : in  std_logic_vector(C_DATA_WIDTH-1 downto 0);
    po_decoder_data   : out std_logic_vector(C_DATA_WIDTH-1 downto 0);

    pi_reg  : in t_reg_msk_init_in ;
    po_reg  : out t_reg_msk_init_out
  );
end entity msk_top_regs_msk_init;

architecture rtl of msk_top_regs_msk_init is
  signal data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0) := (others => '0');
begin
  --
  data_out(C_DATA_WIDTH-1 downto 1) <= (others => '0'); --

  -- resize field data out to the register bus width
  -- do only if 1 field and signed--
  po_decoder_data <= data_out; --

  ------------------------------------------------------------STORAGE
  init_storage: block
    signal l_field_reg   : std_logic_vector(1-1 downto 0) :=
                           std_logic_vector(to_signed(1,1));
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          l_field_reg <= std_logic_vector(to_signed(1,1));
        else
          -- HW --
          -- SW -- TODO: handle software access side effects (rcl/rset, woclr/woset, swacc/swmod)
          if pi_decoder_wr_stb = '1' then
            l_field_reg <= pi_decoder_data(0 downto 0);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.init.data <= l_field_reg; --
    data_out(0 downto 0) <= l_field_reg;

  end block init_storage;
  ----------------------------------------------------------
end rtl;
-----------------------------------------------
-- register type: msk_ctrl
-----------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

use work.pkg_msk_top_regs.all;

entity msk_top_regs_msk_ctrl is
  port (
    pi_clock        : in  std_logic;
    pi_reset        : in  std_logic;
    -- to/from adapter
    pi_decoder_rd_stb : in  std_logic;
    pi_decoder_wr_stb : in  std_logic;
    pi_decoder_data   : in  std_logic_vector(C_DATA_WIDTH-1 downto 0);
    po_decoder_data   : out std_logic_vector(C_DATA_WIDTH-1 downto 0);

    pi_reg  : in t_reg_msk_ctrl_in ;
    po_reg  : out t_reg_msk_ctrl_out
  );
end entity msk_top_regs_msk_ctrl;

architecture rtl of msk_top_regs_msk_ctrl is
  signal data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0) := (others => '0');
begin
  --
  data_out(C_DATA_WIDTH-1 downto 4) <= (others => '0'); --

  -- resize field data out to the register bus width
  -- do only if 1 field and signed--
  po_decoder_data <= data_out; --

  ------------------------------------------------------------STORAGE
  ptt_desc_209a923a_storage: block
    signal l_field_reg   : std_logic_vector(1-1 downto 0) :=
                           std_logic_vector(to_signed(0,1));
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          l_field_reg <= std_logic_vector(to_signed(0,1));
        else
          -- HW --
          -- SW -- TODO: handle software access side effects (rcl/rset, woclr/woset, swacc/swmod)
          if pi_decoder_wr_stb = '1' then
            l_field_reg <= pi_decoder_data(0 downto 0);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.ptt_desc_209a923a.data <= l_field_reg; --
    data_out(0 downto 0) <= l_field_reg;

  end block ptt_desc_209a923a_storage;
  ------------------------------------------------------------STORAGE
  loopback_ena_desc_6617b8f3_storage: block
    signal l_field_reg   : std_logic_vector(1-1 downto 0) :=
                           std_logic_vector(to_signed(0,1));
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          l_field_reg <= std_logic_vector(to_signed(0,1));
        else
          -- HW --
          -- SW -- TODO: handle software access side effects (rcl/rset, woclr/woset, swacc/swmod)
          if pi_decoder_wr_stb = '1' then
            l_field_reg <= pi_decoder_data(1 downto 1);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.loopback_ena_desc_6617b8f3.data <= l_field_reg; --
    data_out(1 downto 1) <= l_field_reg;

  end block loopback_ena_desc_6617b8f3_storage;
  ------------------------------------------------------------STORAGE
  rx_invert_desc_643ee034_storage: block
    signal l_field_reg   : std_logic_vector(1-1 downto 0) :=
                           std_logic_vector(to_signed(0,1));
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          l_field_reg <= std_logic_vector(to_signed(0,1));
        else
          -- HW --
          -- SW -- TODO: handle software access side effects (rcl/rset, woclr/woset, swacc/swmod)
          if pi_decoder_wr_stb = '1' then
            l_field_reg <= pi_decoder_data(2 downto 2);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.rx_invert_desc_643ee034.data <= l_field_reg; --
    data_out(2 downto 2) <= l_field_reg;

  end block rx_invert_desc_643ee034_storage;
  ------------------------------------------------------------STORAGE
  clear_counts_desc_52baf732_storage: block
    signal l_field_reg   : std_logic_vector(1-1 downto 0) :=
                           std_logic_vector(to_signed(0,1));
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          l_field_reg <= std_logic_vector(to_signed(0,1));
        else
          -- HW --
          -- SW -- TODO: handle software access side effects (rcl/rset, woclr/woset, swacc/swmod)
          if pi_decoder_wr_stb = '1' then
            l_field_reg <= pi_decoder_data(3 downto 3);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.clear_counts_desc_52baf732.data <= l_field_reg; --
    data_out(3 downto 3) <= l_field_reg;

  end block clear_counts_desc_52baf732_storage;
  ----------------------------------------------------------
end rtl;
-----------------------------------------------
-- register type: msk_stat_0
-----------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

use work.pkg_msk_top_regs.all;

entity msk_top_regs_msk_stat_0 is
  port (
    pi_clock        : in  std_logic;
    pi_reset        : in  std_logic;
    -- to/from adapter
    pi_decoder_rd_stb : in  std_logic;
    pi_decoder_wr_stb : in  std_logic;
    pi_decoder_data   : in  std_logic_vector(C_DATA_WIDTH-1 downto 0);
    po_decoder_data   : out std_logic_vector(C_DATA_WIDTH-1 downto 0);

    pi_reg  : in t_reg_msk_stat_0_in ;
    po_reg  : out t_reg_msk_stat_0_out
  );
end entity msk_top_regs_msk_stat_0;

architecture rtl of msk_top_regs_msk_stat_0 is
  signal data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0) := (others => '0');
begin
  --
  data_out(C_DATA_WIDTH-1 downto 3) <= (others => '0'); --

  -- resize field data out to the register bus width
  -- do only if 1 field and signed--
  po_decoder_data <= data_out; --

  ------------------------------------------------------------WIRE
  demod_sync_lock_wire : block--
  begin
    --
    data_out(0 downto 0) <= pi_reg.demod_sync_lock.data(1-1 downto 0); --
    --no signal to read by HW
    po_reg.demod_sync_lock.data <= (others => '0'); --
  end block; ----WIRE
  tx_enable_wire : block--
  begin
    --
    data_out(1 downto 1) <= pi_reg.tx_enable.data(1-1 downto 0); --
    --no signal to read by HW
    po_reg.tx_enable.data <= (others => '0'); --
  end block; ----WIRE
  rx_enable_wire : block--
  begin
    --
    data_out(2 downto 2) <= pi_reg.rx_enable.data(1-1 downto 0); --
    --no signal to read by HW
    po_reg.rx_enable.data <= (others => '0'); --
  end block; --
end rtl;
-----------------------------------------------
-- register type: msk_stat_1
-----------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

use work.pkg_msk_top_regs.all;

entity msk_top_regs_msk_stat_1 is
  port (
    pi_clock        : in  std_logic;
    pi_reset        : in  std_logic;
    -- to/from adapter
    pi_decoder_rd_stb : in  std_logic;
    pi_decoder_wr_stb : in  std_logic;
    pi_decoder_data   : in  std_logic_vector(C_DATA_WIDTH-1 downto 0);
    po_decoder_data   : out std_logic_vector(C_DATA_WIDTH-1 downto 0);

    pi_reg  : in t_reg_msk_stat_1_in ;
    po_reg  : out t_reg_msk_stat_1_out
  );
end entity msk_top_regs_msk_stat_1;

architecture rtl of msk_top_regs_msk_stat_1 is
  signal data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0) := (others => '0');
begin
  --

  -- resize field data out to the register bus width
  -- do only if 1 field and signed--
  po_decoder_data <= data_out; --

  ------------------------------------------------------------STORAGE
  tx_bit_cntr_storage: block
    signal l_field_reg   : std_logic_vector(32-1 downto 0) :=
                           std_logic_vector(to_signed(0,32));
    signal l_incrvalue   : natural;
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          l_field_reg <= std_logic_vector(to_signed(0,32));
        else
          -- HW --
          l_field_reg <= pi_reg.tx_bit_cntr.data;
          -- counter
          if  pi_reg.tx_bit_cntr.incr = '1' then
            l_field_reg <= std_logic_vector(unsigned(l_field_reg) + to_unsigned(l_incrvalue, 32));
          end if;
          -- SW -- TODO: handle software access side effects (rcl/rset, woclr/woset, swacc/swmod)
        end if;
      end if;
    end process;
    --
    po_reg.tx_bit_cntr.data <= l_field_reg; --
    data_out(31 downto 0) <= l_field_reg;

    l_incrvalue <= 1;
  end block tx_bit_cntr_storage;
  ----------------------------------------------------------
end rtl;
-----------------------------------------------
-- register type: msk_stat_2
-----------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

use work.pkg_msk_top_regs.all;

entity msk_top_regs_msk_stat_2 is
  port (
    pi_clock        : in  std_logic;
    pi_reset        : in  std_logic;
    -- to/from adapter
    pi_decoder_rd_stb : in  std_logic;
    pi_decoder_wr_stb : in  std_logic;
    pi_decoder_data   : in  std_logic_vector(C_DATA_WIDTH-1 downto 0);
    po_decoder_data   : out std_logic_vector(C_DATA_WIDTH-1 downto 0);

    pi_reg  : in t_reg_msk_stat_2_in ;
    po_reg  : out t_reg_msk_stat_2_out
  );
end entity msk_top_regs_msk_stat_2;

architecture rtl of msk_top_regs_msk_stat_2 is
  signal data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0) := (others => '0');
begin
  --

  -- resize field data out to the register bus width
  -- do only if 1 field and signed--
  po_decoder_data <= data_out; --

  ------------------------------------------------------------STORAGE
  tx_ena_cntr_storage: block
    signal l_field_reg   : std_logic_vector(32-1 downto 0) :=
                           std_logic_vector(to_signed(0,32));
    signal l_incrvalue   : natural;
    signal l_decrvalue   : natural;
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          l_field_reg <= std_logic_vector(to_signed(0,32));
        else
          -- HW --
          l_field_reg <= pi_reg.tx_ena_cntr.data;
          -- counter
          if  pi_reg.tx_ena_cntr.incr = '1' then
            l_field_reg <= std_logic_vector(unsigned(l_field_reg) + to_unsigned(l_incrvalue, 32));
          end if;
          if  pi_reg.tx_ena_cntr.decr = '1' then
            l_field_reg <= std_logic_vector(unsigned(l_field_reg) - to_unsigned(l_decrvalue, 32));
          end if;
          -- SW -- TODO: handle software access side effects (rcl/rset, woclr/woset, swacc/swmod)
        end if;
      end if;
    end process;
    --
    po_reg.tx_ena_cntr.data <= l_field_reg; --
    data_out(31 downto 0) <= l_field_reg;

    l_incrvalue <= 1;
    l_decrvalue <= 1;
  end block tx_ena_cntr_storage;
  ----------------------------------------------------------
end rtl;
-----------------------------------------------
-- register type: config_32
-----------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

use work.pkg_msk_top_regs.all;

entity msk_top_regs_config_32 is
  port (
    pi_clock        : in  std_logic;
    pi_reset        : in  std_logic;
    -- to/from adapter
    pi_decoder_rd_stb : in  std_logic;
    pi_decoder_wr_stb : in  std_logic;
    pi_decoder_data   : in  std_logic_vector(C_DATA_WIDTH-1 downto 0);
    po_decoder_data   : out std_logic_vector(C_DATA_WIDTH-1 downto 0);

    pi_reg  : in t_reg_config_32_in ;
    po_reg  : out t_reg_config_32_out
  );
end entity msk_top_regs_config_32;

architecture rtl of msk_top_regs_config_32 is
  signal data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0) := (others => '0');
begin
  --

  -- resize field data out to the register bus width
  -- do only if 1 field and signed--
  po_decoder_data <= data_out; --

  ------------------------------------------------------------STORAGE
  config_data_storage: block
    signal l_field_reg   : std_logic_vector(32-1 downto 0) :=
                           std_logic_vector(to_signed(0,32));
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          l_field_reg <= std_logic_vector(to_signed(0,32));
        else
          -- HW --
          -- SW -- TODO: handle software access side effects (rcl/rset, woclr/woset, swacc/swmod)
          if pi_decoder_wr_stb = '1' then
            l_field_reg <= pi_decoder_data(31 downto 0);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.config_data.data <= l_field_reg; --
    data_out(31 downto 0) <= l_field_reg;

  end block config_data_storage;
  ----------------------------------------------------------
end rtl;
-----------------------------------------------
-- register type: lpf_config_0
-----------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

use work.pkg_msk_top_regs.all;

entity msk_top_regs_lpf_config_0 is
  port (
    pi_clock        : in  std_logic;
    pi_reset        : in  std_logic;
    -- to/from adapter
    pi_decoder_rd_stb : in  std_logic;
    pi_decoder_wr_stb : in  std_logic;
    pi_decoder_data   : in  std_logic_vector(C_DATA_WIDTH-1 downto 0);
    po_decoder_data   : out std_logic_vector(C_DATA_WIDTH-1 downto 0);

    pi_reg  : in t_reg_lpf_config_0_in ;
    po_reg  : out t_reg_lpf_config_0_out
  );
end entity msk_top_regs_lpf_config_0;

architecture rtl of msk_top_regs_lpf_config_0 is
  signal data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0) := (others => '0');
begin
  --
  data_out(C_DATA_WIDTH-1 downto 18) <= (others => '0'); --

  -- resize field data out to the register bus width
  -- do only if 1 field and signed--
  po_decoder_data <= data_out; --

  ------------------------------------------------------------STORAGE
  lpf_freeze_storage: block
    signal l_field_reg   : std_logic_vector(1-1 downto 0) :=
                           std_logic_vector(to_signed(0,1));
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          l_field_reg <= std_logic_vector(to_signed(0,1));
        else
          -- HW --
          -- SW -- TODO: handle software access side effects (rcl/rset, woclr/woset, swacc/swmod)
          if pi_decoder_wr_stb = '1' then
            l_field_reg <= pi_decoder_data(0 downto 0);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.lpf_freeze.data <= l_field_reg; --
    data_out(0 downto 0) <= l_field_reg;

  end block lpf_freeze_storage;
  ------------------------------------------------------------STORAGE
  lpf_zero_storage: block
    signal l_field_reg   : std_logic_vector(1-1 downto 0) :=
                           std_logic_vector(to_signed(0,1));
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          l_field_reg <= std_logic_vector(to_signed(0,1));
        else
          -- HW --
          -- SW -- TODO: handle software access side effects (rcl/rset, woclr/woset, swacc/swmod)
          if pi_decoder_wr_stb = '1' then
            l_field_reg <= pi_decoder_data(1 downto 1);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.lpf_zero.data <= l_field_reg; --
    data_out(1 downto 1) <= l_field_reg;

  end block lpf_zero_storage;
  ------------------------------------------------------------STORAGE
  lpf_alpha_storage: block
    signal l_field_reg   : std_logic_vector(16-1 downto 0) :=
                           std_logic_vector(to_signed(0,16));
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          l_field_reg <= std_logic_vector(to_signed(0,16));
        else
          -- HW --
          -- SW -- TODO: handle software access side effects (rcl/rset, woclr/woset, swacc/swmod)
          if pi_decoder_wr_stb = '1' then
            l_field_reg <= pi_decoder_data(31 downto 16);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.lpf_alpha.data <= l_field_reg; --
    data_out(31 downto 16) <= l_field_reg;

  end block lpf_alpha_storage;
  ----------------------------------------------------------
end rtl;
-----------------------------------------------
-- register type: lpf_config_1
-----------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

use work.pkg_msk_top_regs.all;

entity msk_top_regs_lpf_config_1 is
  port (
    pi_clock        : in  std_logic;
    pi_reset        : in  std_logic;
    -- to/from adapter
    pi_decoder_rd_stb : in  std_logic;
    pi_decoder_wr_stb : in  std_logic;
    pi_decoder_data   : in  std_logic_vector(C_DATA_WIDTH-1 downto 0);
    po_decoder_data   : out std_logic_vector(C_DATA_WIDTH-1 downto 0);

    pi_reg  : in t_reg_lpf_config_1_in ;
    po_reg  : out t_reg_lpf_config_1_out
  );
end entity msk_top_regs_lpf_config_1;

architecture rtl of msk_top_regs_lpf_config_1 is
  signal data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0) := (others => '0');
begin
  --

  -- resize field data out to the register bus width
  -- do only if 1 field and signed--
  po_decoder_data <= data_out; --

  ------------------------------------------------------------STORAGE
  i_gain_storage: block
    signal l_field_reg   : std_logic_vector(16-1 downto 0) :=
                           std_logic_vector(to_signed(0,16));
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          l_field_reg <= std_logic_vector(to_signed(0,16));
        else
          -- HW --
          -- SW -- TODO: handle software access side effects (rcl/rset, woclr/woset, swacc/swmod)
          if pi_decoder_wr_stb = '1' then
            l_field_reg <= pi_decoder_data(15 downto 0);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.i_gain.data <= l_field_reg; --
    data_out(15 downto 0) <= l_field_reg;

  end block i_gain_storage;
  ------------------------------------------------------------STORAGE
  p_gain_storage: block
    signal l_field_reg   : std_logic_vector(16-1 downto 0) :=
                           std_logic_vector(to_signed(0,16));
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          l_field_reg <= std_logic_vector(to_signed(0,16));
        else
          -- HW --
          -- SW -- TODO: handle software access side effects (rcl/rset, woclr/woset, swacc/swmod)
          if pi_decoder_wr_stb = '1' then
            l_field_reg <= pi_decoder_data(31 downto 16);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.p_gain.data <= l_field_reg; --
    data_out(31 downto 16) <= l_field_reg;

  end block p_gain_storage;
  ----------------------------------------------------------
end rtl;
-----------------------------------------------
-- register type: data_width
-----------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

use work.pkg_msk_top_regs.all;

entity msk_top_regs_data_width is
  port (
    pi_clock        : in  std_logic;
    pi_reset        : in  std_logic;
    -- to/from adapter
    pi_decoder_rd_stb : in  std_logic;
    pi_decoder_wr_stb : in  std_logic;
    pi_decoder_data   : in  std_logic_vector(C_DATA_WIDTH-1 downto 0);
    po_decoder_data   : out std_logic_vector(C_DATA_WIDTH-1 downto 0);

    pi_reg  : in t_reg_data_width_in ;
    po_reg  : out t_reg_data_width_out
  );
end entity msk_top_regs_data_width;

architecture rtl of msk_top_regs_data_width is
  signal data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0) := (others => '0');
begin
  --
  data_out(C_DATA_WIDTH-1 downto 8) <= (others => '0'); --

  -- resize field data out to the register bus width
  -- do only if 1 field and signed--
  po_decoder_data <= data_out; --

  ------------------------------------------------------------STORAGE
  data_width_storage: block
    signal l_field_reg   : std_logic_vector(8-1 downto 0) :=
                           std_logic_vector(to_signed(8,8));
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          l_field_reg <= std_logic_vector(to_signed(8,8));
        else
          -- HW --
          -- SW -- TODO: handle software access side effects (rcl/rset, woclr/woset, swacc/swmod)
          if pi_decoder_wr_stb = '1' then
            l_field_reg <= pi_decoder_data(7 downto 0);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.data_width.data <= l_field_reg; --
    data_out(7 downto 0) <= l_field_reg;

  end block data_width_storage;
  ----------------------------------------------------------
end rtl;
-----------------------------------------------
-- register type: prbs_ctrl
-----------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

use work.pkg_msk_top_regs.all;

entity msk_top_regs_prbs_ctrl is
  port (
    pi_clock        : in  std_logic;
    pi_reset        : in  std_logic;
    -- to/from adapter
    pi_decoder_rd_stb : in  std_logic;
    pi_decoder_wr_stb : in  std_logic;
    pi_decoder_data   : in  std_logic_vector(C_DATA_WIDTH-1 downto 0);
    po_decoder_data   : out std_logic_vector(C_DATA_WIDTH-1 downto 0);

    pi_reg  : in t_reg_prbs_ctrl_in ;
    po_reg  : out t_reg_prbs_ctrl_out
  );
end entity msk_top_regs_prbs_ctrl;

architecture rtl of msk_top_regs_prbs_ctrl is
  signal data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0) := (others => '0');
begin
  --
  data_out(C_DATA_WIDTH-1 downto 4) <= (others => '0'); --

  -- resize field data out to the register bus width
  -- do only if 1 field and signed--
  po_decoder_data <= data_out; --

  ------------------------------------------------------------STORAGE
  prbs_sel_storage: block
    signal l_field_reg   : std_logic_vector(1-1 downto 0) :=
                           std_logic_vector(to_signed(0,1));
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          l_field_reg <= std_logic_vector(to_signed(0,1));
        else
          -- HW --
          -- SW -- TODO: handle software access side effects (rcl/rset, woclr/woset, swacc/swmod)
          if pi_decoder_wr_stb = '1' then
            l_field_reg <= pi_decoder_data(0 downto 0);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.prbs_sel.data <= l_field_reg; --
    data_out(0 downto 0) <= l_field_reg;

  end block prbs_sel_storage;
  ------------------------------------------------------------STORAGE
  prbs_error_insert_storage: block
    signal l_field_reg   : std_logic_vector(1-1 downto 0) :=
                           std_logic_vector(to_signed(0,1));
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          l_field_reg <= std_logic_vector(to_signed(0,1));
        else
          -- HW --
          -- SW -- TODO: handle software access side effects (rcl/rset, woclr/woset, swacc/swmod)
          if pi_decoder_wr_stb = '1' then
            l_field_reg <= pi_decoder_data(1 downto 1);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.prbs_error_insert.data <= l_field_reg; --
    data_out(1 downto 1) <= l_field_reg;

  end block prbs_error_insert_storage;
  ------------------------------------------------------------STORAGE
  prbs_clear_storage: block
    signal l_field_reg   : std_logic_vector(1-1 downto 0) :=
                           std_logic_vector(to_signed(0,1));
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          l_field_reg <= std_logic_vector(to_signed(0,1));
        else
          -- HW --
          -- SW -- TODO: handle software access side effects (rcl/rset, woclr/woset, swacc/swmod)
          if pi_decoder_wr_stb = '1' then
            l_field_reg <= pi_decoder_data(2 downto 2);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.prbs_clear.data <= l_field_reg; --
    data_out(2 downto 2) <= l_field_reg;

  end block prbs_clear_storage;
  ------------------------------------------------------------STORAGE
  prbs_sync_storage: block
    signal l_field_reg   : std_logic_vector(1-1 downto 0) :=
                           std_logic_vector(to_signed(0,1));
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          l_field_reg <= std_logic_vector(to_signed(0,1));
        else
          -- HW --
          -- SW -- TODO: handle software access side effects (rcl/rset, woclr/woset, swacc/swmod)
          if pi_decoder_wr_stb = '1' then
            l_field_reg <= pi_decoder_data(3 downto 3);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.prbs_sync.data <= l_field_reg; --
    data_out(3 downto 3) <= l_field_reg;

  end block prbs_sync_storage;
  ----------------------------------------------------------
end rtl;
-----------------------------------------------
-- register type: stat_32
-----------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

use work.pkg_msk_top_regs.all;

entity msk_top_regs_stat_32 is
  port (
    pi_clock        : in  std_logic;
    pi_reset        : in  std_logic;
    -- to/from adapter
    pi_decoder_rd_stb : in  std_logic;
    pi_decoder_wr_stb : in  std_logic;
    pi_decoder_data   : in  std_logic_vector(C_DATA_WIDTH-1 downto 0);
    po_decoder_data   : out std_logic_vector(C_DATA_WIDTH-1 downto 0);

    pi_reg  : in t_reg_stat_32_in ;
    po_reg  : out t_reg_stat_32_out
  );
end entity msk_top_regs_stat_32;

architecture rtl of msk_top_regs_stat_32 is
  signal data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0) := (others => '0');
begin
  --

  -- resize field data out to the register bus width
  -- do only if 1 field and signed--
  po_decoder_data <= data_out; --

  ------------------------------------------------------------WIRE
  status_data_wire : block--
  begin
    --
    data_out(31 downto 0) <= pi_reg.status_data.data(32-1 downto 0); --
    --no signal to read by HW
    po_reg.status_data.data <= (others => '0'); --
  end block; --
end rtl;
-----------------------------------------------

--------------------------------------------------------------------------------
-- Register types in regfiles
--------------------------------------------------------------------------------
--