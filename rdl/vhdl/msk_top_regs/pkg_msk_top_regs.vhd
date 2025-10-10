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
--! VHDL package of DesyRDL for address space decoder for msk_top_regs
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
  constant C_ADDR_WIDTH : integer := 8;
  constant C_DATA_WIDTH : integer := 32;

  -- ===========================================================================
  -- ---------------------------------------------------------------------------
  -- registers
  -- ---------------------------------------------------------------------------

  -- ===========================================================================
  -- REGISTERS interface
  -- ---------------------------------------------------------------------------
  -- register type: msk_hash_lo
  -----------------------------------------------
  type t_field_signals_msk_hash_lo_hash_id_lo_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_msk_hash_lo_hash_id_lo_out is record
    -- no data if field cannot be written from hw
    dummy : std_logic; --
  end record; --

  -- The actual register types
  type t_reg_msk_hash_lo_in is record--
    hash_id_lo : t_field_signals_msk_hash_lo_hash_id_lo_in; --
  end record;
  type t_reg_msk_hash_lo_out is record--
    hash_id_lo : t_field_signals_msk_hash_lo_hash_id_lo_out; --
  end record;
  type t_reg_msk_hash_lo_2d_in is array (integer range <>) of t_reg_msk_hash_lo_in;
  type t_reg_msk_hash_lo_2d_out is array (integer range <>) of t_reg_msk_hash_lo_out;
  type t_reg_msk_hash_lo_3d_in is array (integer range <>, integer range <>) of t_reg_msk_hash_lo_in;
  type t_reg_msk_hash_lo_3d_out is array (integer range <>, integer range <>) of t_reg_msk_hash_lo_out;
  -----------------------------------------------
  -- register type: msk_hash_hi
  -----------------------------------------------
  type t_field_signals_msk_hash_hi_hash_id_hi_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_msk_hash_hi_hash_id_hi_out is record
    -- no data if field cannot be written from hw
    dummy : std_logic; --
  end record; --

  -- The actual register types
  type t_reg_msk_hash_hi_in is record--
    hash_id_hi : t_field_signals_msk_hash_hi_hash_id_hi_in; --
  end record;
  type t_reg_msk_hash_hi_out is record--
    hash_id_hi : t_field_signals_msk_hash_hi_hash_id_hi_out; --
  end record;
  type t_reg_msk_hash_hi_2d_in is array (integer range <>) of t_reg_msk_hash_hi_in;
  type t_reg_msk_hash_hi_2d_out is array (integer range <>) of t_reg_msk_hash_hi_out;
  type t_reg_msk_hash_hi_3d_in is array (integer range <>, integer range <>) of t_reg_msk_hash_hi_in;
  type t_reg_msk_hash_hi_3d_out is array (integer range <>, integer range <>) of t_reg_msk_hash_hi_out;
  -----------------------------------------------
  -- register type: msk_init
  -----------------------------------------------
  type t_field_signals_msk_init_txrxinit_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_msk_init_txrxinit_out is record
    data : std_logic_vector(1-1 downto 0); --
  end record; --
  type t_field_signals_msk_init_txinit_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_msk_init_txinit_out is record
    data : std_logic_vector(1-1 downto 0); --
  end record; --
  type t_field_signals_msk_init_rxinit_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_msk_init_rxinit_out is record
    data : std_logic_vector(1-1 downto 0); --
  end record; --

  -- The actual register types
  type t_reg_msk_init_in is record--
    txrxinit : t_field_signals_msk_init_txrxinit_in; --
    txinit : t_field_signals_msk_init_txinit_in; --
    rxinit : t_field_signals_msk_init_rxinit_in; --
  end record;
  type t_reg_msk_init_out is record--
    txrxinit : t_field_signals_msk_init_txrxinit_out; --
    txinit : t_field_signals_msk_init_txinit_out; --
    rxinit : t_field_signals_msk_init_rxinit_out; --
  end record;
  type t_reg_msk_init_2d_in is array (integer range <>) of t_reg_msk_init_in;
  type t_reg_msk_init_2d_out is array (integer range <>) of t_reg_msk_init_out;
  type t_reg_msk_init_3d_in is array (integer range <>, integer range <>) of t_reg_msk_init_in;
  type t_reg_msk_init_3d_out is array (integer range <>, integer range <>) of t_reg_msk_init_out;
  -----------------------------------------------
  -- register type: msk_ctrl
  -----------------------------------------------
  type t_field_signals_msk_ctrl_ptt_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_msk_ctrl_ptt_out is record
    data : std_logic_vector(1-1 downto 0); --
  end record; --
  type t_field_signals_msk_ctrl_loopback_ena_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_msk_ctrl_loopback_ena_out is record
    data : std_logic_vector(1-1 downto 0); --
  end record; --
  type t_field_signals_msk_ctrl_rx_invert_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_msk_ctrl_rx_invert_out is record
    data : std_logic_vector(1-1 downto 0); --
  end record; --
  type t_field_signals_msk_ctrl_clear_counts_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_msk_ctrl_clear_counts_out is record
    data : std_logic_vector(1-1 downto 0); --
  end record; --
  type t_field_signals_msk_ctrl_diff_encoder_loopback_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_msk_ctrl_diff_encoder_loopback_out is record
    data : std_logic_vector(1-1 downto 0); --
  end record; --

  -- The actual register types
  type t_reg_msk_ctrl_in is record--
    ptt : t_field_signals_msk_ctrl_ptt_in; --
    loopback_ena : t_field_signals_msk_ctrl_loopback_ena_in; --
    rx_invert : t_field_signals_msk_ctrl_rx_invert_in; --
    clear_counts : t_field_signals_msk_ctrl_clear_counts_in; --
    diff_encoder_loopback : t_field_signals_msk_ctrl_diff_encoder_loopback_in; --
  end record;
  type t_reg_msk_ctrl_out is record--
    ptt : t_field_signals_msk_ctrl_ptt_out; --
    loopback_ena : t_field_signals_msk_ctrl_loopback_ena_out; --
    rx_invert : t_field_signals_msk_ctrl_rx_invert_out; --
    clear_counts : t_field_signals_msk_ctrl_clear_counts_out; --
    diff_encoder_loopback : t_field_signals_msk_ctrl_diff_encoder_loopback_out; --
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
    dummy : std_logic; --
  end record; --
  type t_field_signals_msk_stat_0_tx_enable_in is record
    data : std_logic_vector(1-1 downto 0); --
  end record;

  type t_field_signals_msk_stat_0_tx_enable_out is record
    -- no data if field cannot be written from hw
    dummy : std_logic; --
  end record; --
  type t_field_signals_msk_stat_0_rx_enable_in is record
    data : std_logic_vector(1-1 downto 0); --
  end record;

  type t_field_signals_msk_stat_0_rx_enable_out is record
    -- no data if field cannot be written from hw
    dummy : std_logic; --
  end record; --
  type t_field_signals_msk_stat_0_tx_axis_valid_in is record
    data : std_logic_vector(1-1 downto 0); --
  end record;

  type t_field_signals_msk_stat_0_tx_axis_valid_out is record
    -- no data if field cannot be written from hw
    dummy : std_logic; --
  end record; --

  -- The actual register types
  type t_reg_msk_stat_0_in is record--
    demod_sync_lock : t_field_signals_msk_stat_0_demod_sync_lock_in; --
    tx_enable : t_field_signals_msk_stat_0_tx_enable_in; --
    rx_enable : t_field_signals_msk_stat_0_rx_enable_in; --
    tx_axis_valid : t_field_signals_msk_stat_0_tx_axis_valid_in; --
  end record;
  type t_reg_msk_stat_0_out is record--
    demod_sync_lock : t_field_signals_msk_stat_0_demod_sync_lock_out; --
    tx_enable : t_field_signals_msk_stat_0_tx_enable_out; --
    rx_enable : t_field_signals_msk_stat_0_rx_enable_out; --
    tx_axis_valid : t_field_signals_msk_stat_0_tx_axis_valid_out; --
  end record;
  type t_reg_msk_stat_0_2d_in is array (integer range <>) of t_reg_msk_stat_0_in;
  type t_reg_msk_stat_0_2d_out is array (integer range <>) of t_reg_msk_stat_0_out;
  type t_reg_msk_stat_0_3d_in is array (integer range <>, integer range <>) of t_reg_msk_stat_0_in;
  type t_reg_msk_stat_0_3d_out is array (integer range <>, integer range <>) of t_reg_msk_stat_0_out;
  -----------------------------------------------
  -- register type: msk_stat_1
  -----------------------------------------------
  type t_field_signals_msk_stat_1_tx_bit_counter_in is record
    data : std_logic_vector(32-1 downto 0); --
  end record;

  type t_field_signals_msk_stat_1_tx_bit_counter_out is record
    -- no data if field cannot be written from hw
    dummy : std_logic; --
  end record; --

  -- The actual register types
  type t_reg_msk_stat_1_in is record--
    tx_bit_counter : t_field_signals_msk_stat_1_tx_bit_counter_in; --
  end record;
  type t_reg_msk_stat_1_out is record--
    tx_bit_counter : t_field_signals_msk_stat_1_tx_bit_counter_out; --
  end record;
  type t_reg_msk_stat_1_2d_in is array (integer range <>) of t_reg_msk_stat_1_in;
  type t_reg_msk_stat_1_2d_out is array (integer range <>) of t_reg_msk_stat_1_out;
  type t_reg_msk_stat_1_3d_in is array (integer range <>, integer range <>) of t_reg_msk_stat_1_in;
  type t_reg_msk_stat_1_3d_out is array (integer range <>, integer range <>) of t_reg_msk_stat_1_out;
  -----------------------------------------------
  -- register type: msk_stat_2
  -----------------------------------------------
  type t_field_signals_msk_stat_2_tx_ena_counter_in is record
    data : std_logic_vector(32-1 downto 0); --
  end record;

  type t_field_signals_msk_stat_2_tx_ena_counter_out is record
    -- no data if field cannot be written from hw
    dummy : std_logic; --
  end record; --

  -- The actual register types
  type t_reg_msk_stat_2_in is record--
    tx_ena_counter : t_field_signals_msk_stat_2_tx_ena_counter_in; --
  end record;
  type t_reg_msk_stat_2_out is record--
    tx_ena_counter : t_field_signals_msk_stat_2_tx_ena_counter_out; --
  end record;
  type t_reg_msk_stat_2_2d_in is array (integer range <>) of t_reg_msk_stat_2_in;
  type t_reg_msk_stat_2_2d_out is array (integer range <>) of t_reg_msk_stat_2_out;
  type t_reg_msk_stat_2_3d_in is array (integer range <>, integer range <>) of t_reg_msk_stat_2_in;
  type t_reg_msk_stat_2_3d_out is array (integer range <>, integer range <>) of t_reg_msk_stat_2_out;
  -----------------------------------------------
  -- register type: config_nco_fw
  -----------------------------------------------
  type t_field_signals_config_nco_fw_config_data_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_config_nco_fw_config_data_out is record
    data : std_logic_vector(32-1 downto 0); --
  end record; --

  -- The actual register types
  type t_reg_config_nco_fw_in is record--
    config_data : t_field_signals_config_nco_fw_config_data_in; --
  end record;
  type t_reg_config_nco_fw_out is record--
    config_data : t_field_signals_config_nco_fw_config_data_out; --
  end record;
  type t_reg_config_nco_fw_2d_in is array (integer range <>) of t_reg_config_nco_fw_in;
  type t_reg_config_nco_fw_2d_out is array (integer range <>) of t_reg_config_nco_fw_out;
  type t_reg_config_nco_fw_3d_in is array (integer range <>, integer range <>) of t_reg_config_nco_fw_in;
  type t_reg_config_nco_fw_3d_out is array (integer range <>, integer range <>) of t_reg_config_nco_fw_out;
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
  type t_field_signals_lpf_config_0_prbs_reserved_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_lpf_config_0_prbs_reserved_out is record
    data : std_logic_vector(6-1 downto 0); --
  end record; --
  type t_field_signals_lpf_config_0_lpf_alpha_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_lpf_config_0_lpf_alpha_out is record
    data : std_logic_vector(24-1 downto 0); --
  end record; --

  -- The actual register types
  type t_reg_lpf_config_0_in is record--
    lpf_freeze : t_field_signals_lpf_config_0_lpf_freeze_in; --
    lpf_zero : t_field_signals_lpf_config_0_lpf_zero_in; --
    prbs_reserved : t_field_signals_lpf_config_0_prbs_reserved_in; --
    lpf_alpha : t_field_signals_lpf_config_0_lpf_alpha_in; --
  end record;
  type t_reg_lpf_config_0_out is record--
    lpf_freeze : t_field_signals_lpf_config_0_lpf_freeze_out; --
    lpf_zero : t_field_signals_lpf_config_0_lpf_zero_out; --
    prbs_reserved : t_field_signals_lpf_config_0_prbs_reserved_out; --
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
    data : std_logic_vector(24-1 downto 0); --
  end record; --
  type t_field_signals_lpf_config_1_i_shift_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_lpf_config_1_i_shift_out is record
    data : std_logic_vector(8-1 downto 0); --
  end record; --

  -- The actual register types
  type t_reg_lpf_config_1_in is record--
    i_gain : t_field_signals_lpf_config_1_i_gain_in; --
    i_shift : t_field_signals_lpf_config_1_i_shift_in; --
  end record;
  type t_reg_lpf_config_1_out is record--
    i_gain : t_field_signals_lpf_config_1_i_gain_out; --
    i_shift : t_field_signals_lpf_config_1_i_shift_out; --
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
  type t_field_signals_prbs_ctrl_prbs_manual_sync_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_prbs_ctrl_prbs_manual_sync_out is record
    data : std_logic_vector(1-1 downto 0); --
  end record; --
  type t_field_signals_prbs_ctrl_prbs_reserved_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_prbs_ctrl_prbs_reserved_out is record
    data : std_logic_vector(12-1 downto 0); --
  end record; --
  type t_field_signals_prbs_ctrl_prbs_sync_threshold_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_prbs_ctrl_prbs_sync_threshold_out is record
    data : std_logic_vector(16-1 downto 0); --
  end record; --

  -- The actual register types
  type t_reg_prbs_ctrl_in is record--
    prbs_sel : t_field_signals_prbs_ctrl_prbs_sel_in; --
    prbs_error_insert : t_field_signals_prbs_ctrl_prbs_error_insert_in; --
    prbs_clear : t_field_signals_prbs_ctrl_prbs_clear_in; --
    prbs_manual_sync : t_field_signals_prbs_ctrl_prbs_manual_sync_in; --
    prbs_reserved : t_field_signals_prbs_ctrl_prbs_reserved_in; --
    prbs_sync_threshold : t_field_signals_prbs_ctrl_prbs_sync_threshold_in; --
  end record;
  type t_reg_prbs_ctrl_out is record--
    prbs_sel : t_field_signals_prbs_ctrl_prbs_sel_out; --
    prbs_error_insert : t_field_signals_prbs_ctrl_prbs_error_insert_out; --
    prbs_clear : t_field_signals_prbs_ctrl_prbs_clear_out; --
    prbs_manual_sync : t_field_signals_prbs_ctrl_prbs_manual_sync_out; --
    prbs_reserved : t_field_signals_prbs_ctrl_prbs_reserved_out; --
    prbs_sync_threshold : t_field_signals_prbs_ctrl_prbs_sync_threshold_out; --
  end record;
  type t_reg_prbs_ctrl_2d_in is array (integer range <>) of t_reg_prbs_ctrl_in;
  type t_reg_prbs_ctrl_2d_out is array (integer range <>) of t_reg_prbs_ctrl_out;
  type t_reg_prbs_ctrl_3d_in is array (integer range <>, integer range <>) of t_reg_prbs_ctrl_in;
  type t_reg_prbs_ctrl_3d_out is array (integer range <>, integer range <>) of t_reg_prbs_ctrl_out;
  -----------------------------------------------
  -- register type: config_prbs_seed
  -----------------------------------------------
  type t_field_signals_config_prbs_seed_config_data_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_config_prbs_seed_config_data_out is record
    data : std_logic_vector(32-1 downto 0); --
  end record; --

  -- The actual register types
  type t_reg_config_prbs_seed_in is record--
    config_data : t_field_signals_config_prbs_seed_config_data_in; --
  end record;
  type t_reg_config_prbs_seed_out is record--
    config_data : t_field_signals_config_prbs_seed_config_data_out; --
  end record;
  type t_reg_config_prbs_seed_2d_in is array (integer range <>) of t_reg_config_prbs_seed_in;
  type t_reg_config_prbs_seed_2d_out is array (integer range <>) of t_reg_config_prbs_seed_out;
  type t_reg_config_prbs_seed_3d_in is array (integer range <>, integer range <>) of t_reg_config_prbs_seed_in;
  type t_reg_config_prbs_seed_3d_out is array (integer range <>, integer range <>) of t_reg_config_prbs_seed_out;
  -----------------------------------------------
  -- register type: config_prbs_poly
  -----------------------------------------------
  type t_field_signals_config_prbs_poly_config_data_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_config_prbs_poly_config_data_out is record
    data : std_logic_vector(32-1 downto 0); --
  end record; --

  -- The actual register types
  type t_reg_config_prbs_poly_in is record--
    config_data : t_field_signals_config_prbs_poly_config_data_in; --
  end record;
  type t_reg_config_prbs_poly_out is record--
    config_data : t_field_signals_config_prbs_poly_config_data_out; --
  end record;
  type t_reg_config_prbs_poly_2d_in is array (integer range <>) of t_reg_config_prbs_poly_in;
  type t_reg_config_prbs_poly_2d_out is array (integer range <>) of t_reg_config_prbs_poly_out;
  type t_reg_config_prbs_poly_3d_in is array (integer range <>, integer range <>) of t_reg_config_prbs_poly_in;
  type t_reg_config_prbs_poly_3d_out is array (integer range <>, integer range <>) of t_reg_config_prbs_poly_out;
  -----------------------------------------------
  -- register type: config_prbs_errmask
  -----------------------------------------------
  type t_field_signals_config_prbs_errmask_config_data_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_config_prbs_errmask_config_data_out is record
    data : std_logic_vector(32-1 downto 0); --
  end record; --

  -- The actual register types
  type t_reg_config_prbs_errmask_in is record--
    config_data : t_field_signals_config_prbs_errmask_config_data_in; --
  end record;
  type t_reg_config_prbs_errmask_out is record--
    config_data : t_field_signals_config_prbs_errmask_config_data_out; --
  end record;
  type t_reg_config_prbs_errmask_2d_in is array (integer range <>) of t_reg_config_prbs_errmask_in;
  type t_reg_config_prbs_errmask_2d_out is array (integer range <>) of t_reg_config_prbs_errmask_out;
  type t_reg_config_prbs_errmask_3d_in is array (integer range <>, integer range <>) of t_reg_config_prbs_errmask_in;
  type t_reg_config_prbs_errmask_3d_out is array (integer range <>, integer range <>) of t_reg_config_prbs_errmask_out;
  -----------------------------------------------
  -- register type: stat_32_bits
  -----------------------------------------------
  type t_field_signals_stat_32_bits_status_data_in is record
    data : std_logic_vector(32-1 downto 0); --
  end record;

  type t_field_signals_stat_32_bits_status_data_out is record
    -- no data if field cannot be written from hw
    dummy : std_logic; --
  end record; --

  -- The actual register types
  type t_reg_stat_32_bits_in is record--
    status_data : t_field_signals_stat_32_bits_status_data_in; --
  end record;
  type t_reg_stat_32_bits_out is record--
    status_data : t_field_signals_stat_32_bits_status_data_out; --
  end record;
  type t_reg_stat_32_bits_2d_in is array (integer range <>) of t_reg_stat_32_bits_in;
  type t_reg_stat_32_bits_2d_out is array (integer range <>) of t_reg_stat_32_bits_out;
  type t_reg_stat_32_bits_3d_in is array (integer range <>, integer range <>) of t_reg_stat_32_bits_in;
  type t_reg_stat_32_bits_3d_out is array (integer range <>, integer range <>) of t_reg_stat_32_bits_out;
  -----------------------------------------------
  -- register type: stat_32_errs
  -----------------------------------------------
  type t_field_signals_stat_32_errs_status_data_in is record
    data : std_logic_vector(32-1 downto 0); --
  end record;

  type t_field_signals_stat_32_errs_status_data_out is record
    -- no data if field cannot be written from hw
    dummy : std_logic; --
  end record; --

  -- The actual register types
  type t_reg_stat_32_errs_in is record--
    status_data : t_field_signals_stat_32_errs_status_data_in; --
  end record;
  type t_reg_stat_32_errs_out is record--
    status_data : t_field_signals_stat_32_errs_status_data_out; --
  end record;
  type t_reg_stat_32_errs_2d_in is array (integer range <>) of t_reg_stat_32_errs_in;
  type t_reg_stat_32_errs_2d_out is array (integer range <>) of t_reg_stat_32_errs_out;
  type t_reg_stat_32_errs_3d_in is array (integer range <>, integer range <>) of t_reg_stat_32_errs_in;
  type t_reg_stat_32_errs_3d_out is array (integer range <>, integer range <>) of t_reg_stat_32_errs_out;
  -----------------------------------------------
  -- register type: stat_32_lpf_acc
  -----------------------------------------------
  type t_field_signals_stat_32_lpf_acc_status_data_in is record
    data : std_logic_vector(32-1 downto 0); --
  end record;

  type t_field_signals_stat_32_lpf_acc_status_data_out is record
    -- no data if field cannot be written from hw
    dummy : std_logic; --
  end record; --

  -- The actual register types
  type t_reg_stat_32_lpf_acc_in is record--
    status_data : t_field_signals_stat_32_lpf_acc_status_data_in; --
  end record;
  type t_reg_stat_32_lpf_acc_out is record--
    status_data : t_field_signals_stat_32_lpf_acc_status_data_out; --
  end record;
  type t_reg_stat_32_lpf_acc_2d_in is array (integer range <>) of t_reg_stat_32_lpf_acc_in;
  type t_reg_stat_32_lpf_acc_2d_out is array (integer range <>) of t_reg_stat_32_lpf_acc_out;
  type t_reg_stat_32_lpf_acc_3d_in is array (integer range <>, integer range <>) of t_reg_stat_32_lpf_acc_in;
  type t_reg_stat_32_lpf_acc_3d_out is array (integer range <>, integer range <>) of t_reg_stat_32_lpf_acc_out;
  -----------------------------------------------
  -- register type: msk_stat_3
  -----------------------------------------------
  type t_field_signals_msk_stat_3_xfer_count_in is record
    data : std_logic_vector(32-1 downto 0); --
  end record;

  type t_field_signals_msk_stat_3_xfer_count_out is record
    -- no data if field cannot be written from hw
    dummy : std_logic; --
  end record; --

  -- The actual register types
  type t_reg_msk_stat_3_in is record--
    xfer_count : t_field_signals_msk_stat_3_xfer_count_in; --
  end record;
  type t_reg_msk_stat_3_out is record--
    xfer_count : t_field_signals_msk_stat_3_xfer_count_out; --
  end record;
  type t_reg_msk_stat_3_2d_in is array (integer range <>) of t_reg_msk_stat_3_in;
  type t_reg_msk_stat_3_2d_out is array (integer range <>) of t_reg_msk_stat_3_out;
  type t_reg_msk_stat_3_3d_in is array (integer range <>, integer range <>) of t_reg_msk_stat_3_in;
  type t_reg_msk_stat_3_3d_out is array (integer range <>, integer range <>) of t_reg_msk_stat_3_out;
  -----------------------------------------------
  -- register type: rx_sample_discard
  -----------------------------------------------
  type t_field_signals_rx_sample_discard_rx_sample_discard_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_rx_sample_discard_rx_sample_discard_out is record
    data : std_logic_vector(8-1 downto 0); --
  end record; --
  type t_field_signals_rx_sample_discard_rx_nco_discard_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_rx_sample_discard_rx_nco_discard_out is record
    data : std_logic_vector(8-1 downto 0); --
  end record; --

  -- The actual register types
  type t_reg_rx_sample_discard_in is record--
    rx_sample_discard : t_field_signals_rx_sample_discard_rx_sample_discard_in; --
    rx_nco_discard : t_field_signals_rx_sample_discard_rx_nco_discard_in; --
  end record;
  type t_reg_rx_sample_discard_out is record--
    rx_sample_discard : t_field_signals_rx_sample_discard_rx_sample_discard_out; --
    rx_nco_discard : t_field_signals_rx_sample_discard_rx_nco_discard_out; --
  end record;
  type t_reg_rx_sample_discard_2d_in is array (integer range <>) of t_reg_rx_sample_discard_in;
  type t_reg_rx_sample_discard_2d_out is array (integer range <>) of t_reg_rx_sample_discard_out;
  type t_reg_rx_sample_discard_3d_in is array (integer range <>, integer range <>) of t_reg_rx_sample_discard_in;
  type t_reg_rx_sample_discard_3d_out is array (integer range <>, integer range <>) of t_reg_rx_sample_discard_out;
  -----------------------------------------------
  -- register type: lpf_config_2
  -----------------------------------------------
  type t_field_signals_lpf_config_2_p_gain_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_lpf_config_2_p_gain_out is record
    data : std_logic_vector(24-1 downto 0); --
  end record; --
  type t_field_signals_lpf_config_2_p_shift_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_lpf_config_2_p_shift_out is record
    data : std_logic_vector(8-1 downto 0); --
  end record; --

  -- The actual register types
  type t_reg_lpf_config_2_in is record--
    p_gain : t_field_signals_lpf_config_2_p_gain_in; --
    p_shift : t_field_signals_lpf_config_2_p_shift_in; --
  end record;
  type t_reg_lpf_config_2_out is record--
    p_gain : t_field_signals_lpf_config_2_p_gain_out; --
    p_shift : t_field_signals_lpf_config_2_p_shift_out; --
  end record;
  type t_reg_lpf_config_2_2d_in is array (integer range <>) of t_reg_lpf_config_2_in;
  type t_reg_lpf_config_2_2d_out is array (integer range <>) of t_reg_lpf_config_2_out;
  type t_reg_lpf_config_2_3d_in is array (integer range <>, integer range <>) of t_reg_lpf_config_2_in;
  type t_reg_lpf_config_2_3d_out is array (integer range <>, integer range <>) of t_reg_lpf_config_2_out;
  -----------------------------------------------
  -- register type: observation_data
  -----------------------------------------------
  type t_field_signals_observation_data_data32_in is record
    data : std_logic_vector(32-1 downto 0); --
  end record;

  type t_field_signals_observation_data_data32_out is record
    -- no data if field cannot be written from hw
    dummy : std_logic; --
  end record; --

  -- The actual register types
  type t_reg_observation_data_in is record--
    data : t_field_signals_observation_data_data32_in; --
  end record;
  type t_reg_observation_data_out is record--
    data : t_field_signals_observation_data_data32_out; --
  end record;
  type t_reg_observation_data_2d_in is array (integer range <>) of t_reg_observation_data_in;
  type t_reg_observation_data_2d_out is array (integer range <>) of t_reg_observation_data_out;
  type t_reg_observation_data_3d_in is array (integer range <>, integer range <>) of t_reg_observation_data_in;
  type t_reg_observation_data_3d_out is array (integer range <>, integer range <>) of t_reg_observation_data_out;
  -----------------------------------------------
  -- register type: tx_sync_ctrl
  -----------------------------------------------
  type t_field_signals_tx_sync_ctrl_tx_sync_ena_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_tx_sync_ctrl_tx_sync_ena_out is record
    data : std_logic_vector(1-1 downto 0); --
  end record; --
  type t_field_signals_tx_sync_ctrl_tx_sync_force_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_tx_sync_ctrl_tx_sync_force_out is record
    data : std_logic_vector(1-1 downto 0); --
  end record; --
  type t_field_signals_tx_sync_ctrl_tx_sync_f1_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_tx_sync_ctrl_tx_sync_f1_out is record
    data : std_logic_vector(1-1 downto 0); --
  end record; --
  type t_field_signals_tx_sync_ctrl_tx_sync_f2_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_tx_sync_ctrl_tx_sync_f2_out is record
    data : std_logic_vector(1-1 downto 0); --
  end record; --

  -- The actual register types
  type t_reg_tx_sync_ctrl_in is record--
    tx_sync_ena : t_field_signals_tx_sync_ctrl_tx_sync_ena_in; --
    tx_sync_force : t_field_signals_tx_sync_ctrl_tx_sync_force_in; --
    tx_sync_f1 : t_field_signals_tx_sync_ctrl_tx_sync_f1_in; --
    tx_sync_f2 : t_field_signals_tx_sync_ctrl_tx_sync_f2_in; --
  end record;
  type t_reg_tx_sync_ctrl_out is record--
    tx_sync_ena : t_field_signals_tx_sync_ctrl_tx_sync_ena_out; --
    tx_sync_force : t_field_signals_tx_sync_ctrl_tx_sync_force_out; --
    tx_sync_f1 : t_field_signals_tx_sync_ctrl_tx_sync_f1_out; --
    tx_sync_f2 : t_field_signals_tx_sync_ctrl_tx_sync_f2_out; --
  end record;
  type t_reg_tx_sync_ctrl_2d_in is array (integer range <>) of t_reg_tx_sync_ctrl_in;
  type t_reg_tx_sync_ctrl_2d_out is array (integer range <>) of t_reg_tx_sync_ctrl_out;
  type t_reg_tx_sync_ctrl_3d_in is array (integer range <>, integer range <>) of t_reg_tx_sync_ctrl_in;
  type t_reg_tx_sync_ctrl_3d_out is array (integer range <>, integer range <>) of t_reg_tx_sync_ctrl_out;
  -----------------------------------------------
  -- register type: tx_sync_cnt
  -----------------------------------------------
  type t_field_signals_tx_sync_cnt_tx_sync_cnt_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_tx_sync_cnt_tx_sync_cnt_out is record
    data : std_logic_vector(24-1 downto 0); --
  end record; --

  -- The actual register types
  type t_reg_tx_sync_cnt_in is record--
    tx_sync_cnt : t_field_signals_tx_sync_cnt_tx_sync_cnt_in; --
  end record;
  type t_reg_tx_sync_cnt_out is record--
    tx_sync_cnt : t_field_signals_tx_sync_cnt_tx_sync_cnt_out; --
  end record;
  type t_reg_tx_sync_cnt_2d_in is array (integer range <>) of t_reg_tx_sync_cnt_in;
  type t_reg_tx_sync_cnt_2d_out is array (integer range <>) of t_reg_tx_sync_cnt_out;
  type t_reg_tx_sync_cnt_3d_in is array (integer range <>, integer range <>) of t_reg_tx_sync_cnt_in;
  type t_reg_tx_sync_cnt_3d_out is array (integer range <>, integer range <>) of t_reg_tx_sync_cnt_out;
  -----------------------------------------------
  -- register type: lowpass_ema_alpha
  -----------------------------------------------
  type t_field_signals_lowpass_ema_alpha_alpha_in is record
    -- no data if field cannot be written from hw
    data : std_logic_vector(-1 downto 0); --
  end record;

  type t_field_signals_lowpass_ema_alpha_alpha_out is record
    data : std_logic_vector(18-1 downto 0); --
  end record; --

  -- The actual register types
  type t_reg_lowpass_ema_alpha_in is record--
    alpha : t_field_signals_lowpass_ema_alpha_alpha_in; --
  end record;
  type t_reg_lowpass_ema_alpha_out is record--
    alpha : t_field_signals_lowpass_ema_alpha_alpha_out; --
  end record;
  type t_reg_lowpass_ema_alpha_2d_in is array (integer range <>) of t_reg_lowpass_ema_alpha_in;
  type t_reg_lowpass_ema_alpha_2d_out is array (integer range <>) of t_reg_lowpass_ema_alpha_out;
  type t_reg_lowpass_ema_alpha_3d_in is array (integer range <>, integer range <>) of t_reg_lowpass_ema_alpha_in;
  type t_reg_lowpass_ema_alpha_3d_out is array (integer range <>, integer range <>) of t_reg_lowpass_ema_alpha_out;
  -----------------------------------------------
  -- register type: rx_power
  -----------------------------------------------
  type t_field_signals_rx_power_rx_power_in is record
    data : std_logic_vector(23-1 downto 0); --
  end record;

  type t_field_signals_rx_power_rx_power_out is record
    -- no data if field cannot be written from hw
    dummy : std_logic; --
  end record; --

  -- The actual register types
  type t_reg_rx_power_in is record--
    rx_power : t_field_signals_rx_power_rx_power_in; --
  end record;
  type t_reg_rx_power_out is record--
    rx_power : t_field_signals_rx_power_rx_power_out; --
  end record;
  type t_reg_rx_power_2d_in is array (integer range <>) of t_reg_rx_power_in;
  type t_reg_rx_power_2d_out is array (integer range <>) of t_reg_rx_power_out;
  type t_reg_rx_power_3d_in is array (integer range <>, integer range <>) of t_reg_rx_power_in;
  type t_reg_rx_power_3d_out is array (integer range <>, integer range <>) of t_reg_rx_power_out;
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
    Hash_ID_Low : t_reg_msk_hash_lo_in; --
    Hash_ID_High : t_reg_msk_hash_hi_in; --
    MSK_Init : t_reg_msk_init_in; --
    MSK_Control : t_reg_msk_ctrl_in; --
    MSK_Status : t_reg_msk_stat_0_in; --
    Tx_Bit_Count : t_reg_msk_stat_1_in; --
    Tx_Enable_Count : t_reg_msk_stat_2_in; --
    Fb_FreqWord : t_reg_config_nco_fw_in; --
    TX_F1_FreqWord : t_reg_config_nco_fw_in; --
    TX_F2_FreqWord : t_reg_config_nco_fw_in; --
    RX_F1_FreqWord : t_reg_config_nco_fw_in; --
    RX_F2_FreqWord : t_reg_config_nco_fw_in; --
    LPF_Config_0 : t_reg_lpf_config_0_in; --
    LPF_Config_1 : t_reg_lpf_config_1_in; --
    Tx_Data_Width : t_reg_data_width_in; --
    Rx_Data_Width : t_reg_data_width_in; --
    PRBS_Control : t_reg_prbs_ctrl_in; --
    PRBS_Initial_State : t_reg_config_prbs_seed_in; --
    PRBS_Polynomial : t_reg_config_prbs_poly_in; --
    PRBS_Error_Mask : t_reg_config_prbs_errmask_in; --
    PRBS_Bit_Count : t_reg_stat_32_bits_in; --
    PRBS_Error_Count : t_reg_stat_32_errs_in; --
    LPF_Accum_F1 : t_reg_stat_32_lpf_acc_in; --
    LPF_Accum_F2 : t_reg_stat_32_lpf_acc_in; --
    axis_xfer_count : t_reg_msk_stat_3_in; --
    Rx_Sample_Discard : t_reg_rx_sample_discard_in; --
    LPF_Config_2 : t_reg_lpf_config_2_in; --
    f1_nco_adjust : t_reg_observation_data_in; --
    f2_nco_adjust : t_reg_observation_data_in; --
    f1_error : t_reg_observation_data_in; --
    f2_error : t_reg_observation_data_in; --
    Tx_Sync_Ctrl : t_reg_tx_sync_ctrl_in; --
    Tx_Sync_Cnt : t_reg_tx_sync_cnt_in; --
    lowpass_ema_alpha1 : t_reg_lowpass_ema_alpha_in; --
    lowpass_ema_alpha2 : t_reg_lowpass_ema_alpha_in; --
    rx_power : t_reg_rx_power_in; --
    --
    --
    --
  end record;

  type t_addrmap_msk_top_regs_out is record
    --
    Hash_ID_Low : t_reg_msk_hash_lo_out; --
    Hash_ID_High : t_reg_msk_hash_hi_out; --
    MSK_Init : t_reg_msk_init_out; --
    MSK_Control : t_reg_msk_ctrl_out; --
    MSK_Status : t_reg_msk_stat_0_out; --
    Tx_Bit_Count : t_reg_msk_stat_1_out; --
    Tx_Enable_Count : t_reg_msk_stat_2_out; --
    Fb_FreqWord : t_reg_config_nco_fw_out; --
    TX_F1_FreqWord : t_reg_config_nco_fw_out; --
    TX_F2_FreqWord : t_reg_config_nco_fw_out; --
    RX_F1_FreqWord : t_reg_config_nco_fw_out; --
    RX_F2_FreqWord : t_reg_config_nco_fw_out; --
    LPF_Config_0 : t_reg_lpf_config_0_out; --
    LPF_Config_1 : t_reg_lpf_config_1_out; --
    Tx_Data_Width : t_reg_data_width_out; --
    Rx_Data_Width : t_reg_data_width_out; --
    PRBS_Control : t_reg_prbs_ctrl_out; --
    PRBS_Initial_State : t_reg_config_prbs_seed_out; --
    PRBS_Polynomial : t_reg_config_prbs_poly_out; --
    PRBS_Error_Mask : t_reg_config_prbs_errmask_out; --
    PRBS_Bit_Count : t_reg_stat_32_bits_out; --
    PRBS_Error_Count : t_reg_stat_32_errs_out; --
    LPF_Accum_F1 : t_reg_stat_32_lpf_acc_out; --
    LPF_Accum_F2 : t_reg_stat_32_lpf_acc_out; --
    axis_xfer_count : t_reg_msk_stat_3_out; --
    Rx_Sample_Discard : t_reg_rx_sample_discard_out; --
    LPF_Config_2 : t_reg_lpf_config_2_out; --
    f1_nco_adjust : t_reg_observation_data_out; --
    f2_nco_adjust : t_reg_observation_data_out; --
    f1_error : t_reg_observation_data_out; --
    f2_error : t_reg_observation_data_out; --
    Tx_Sync_Ctrl : t_reg_tx_sync_ctrl_out; --
    Tx_Sync_Cnt : t_reg_tx_sync_cnt_out; --
    lowpass_ema_alpha1 : t_reg_lowpass_ema_alpha_out; --
    lowpass_ema_alpha2 : t_reg_lowpass_ema_alpha_out; --
    rx_power : t_reg_rx_power_out; --
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
-- register type: msk_hash_lo
-----------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

library desyrdl;
use desyrdl.common.all;

use work.pkg_msk_top_regs.all;

entity msk_top_regs_msk_hash_lo is
  port (
    pi_clock        : in  std_logic;
    pi_reset        : in  std_logic;
    -- to/from adapter
    pi_decoder_rd_stb : in  std_logic;
    pi_decoder_wr_stb : in  std_logic;
    pi_decoder_data   : in  std_logic_vector(C_DATA_WIDTH-1 downto 0);
    po_decoder_data   : out std_logic_vector(C_DATA_WIDTH-1 downto 0);

    pi_reg  : in t_reg_msk_hash_lo_in ;
    po_reg  : out t_reg_msk_hash_lo_out
  );
end entity msk_top_regs_msk_hash_lo;

architecture rtl of msk_top_regs_msk_hash_lo is

  -- assign slices of data_out for each field, but force the rest to constant zeros
  function fun_set_data_out ( --
    field_reg_hash_id_lo : std_logic_vector(32-1 downto 0)) --
    return std_logic_vector is
    variable v_data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0);
  begin
    v_data_out := (others => '0');
    --
    v_data_out(31 downto 0) := field_reg_hash_id_lo; --
    return v_data_out;
  end function fun_set_data_out;

  signal data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0) := (others => '0');
   --
  signal field_reg_hash_id_lo : std_logic_vector(32-1 downto 0)
    := std_logic_vector(to_signed(-1431677611,32)); --
begin

  data_out <= fun_set_data_out( --
    field_reg_hash_id_lo --
  );

  -- resize field data out to the register bus width
  -- do only if 1 field and signed--
  po_decoder_data <= data_out; --
  ------------------------------------------------------------WIRE
  hash_id_lo_wire : block --
  begin
    --
    field_reg_hash_id_lo <= std_logic_vector(to_signed(-1431677611,32)); --
    --no signal to read by HW
    po_reg.hash_id_lo.dummy <= '0'; --
  end block; --
end rtl;
-----------------------------------------------
-- register type: msk_hash_hi
-----------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

library desyrdl;
use desyrdl.common.all;

use work.pkg_msk_top_regs.all;

entity msk_top_regs_msk_hash_hi is
  port (
    pi_clock        : in  std_logic;
    pi_reset        : in  std_logic;
    -- to/from adapter
    pi_decoder_rd_stb : in  std_logic;
    pi_decoder_wr_stb : in  std_logic;
    pi_decoder_data   : in  std_logic_vector(C_DATA_WIDTH-1 downto 0);
    po_decoder_data   : out std_logic_vector(C_DATA_WIDTH-1 downto 0);

    pi_reg  : in t_reg_msk_hash_hi_in ;
    po_reg  : out t_reg_msk_hash_hi_out
  );
end entity msk_top_regs_msk_hash_hi;

architecture rtl of msk_top_regs_msk_hash_hi is

  -- assign slices of data_out for each field, but force the rest to constant zeros
  function fun_set_data_out ( --
    field_reg_hash_id_hi : std_logic_vector(32-1 downto 0)) --
    return std_logic_vector is
    variable v_data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0);
  begin
    v_data_out := (others => '0');
    --
    v_data_out(31 downto 0) := field_reg_hash_id_hi; --
    return v_data_out;
  end function fun_set_data_out;

  signal data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0) := (others => '0');
   --
  signal field_reg_hash_id_hi : std_logic_vector(32-1 downto 0)
    := std_logic_vector(to_signed(1431677610,32)); --
begin

  data_out <= fun_set_data_out( --
    field_reg_hash_id_hi --
  );

  -- resize field data out to the register bus width
  -- do only if 1 field and signed--
  po_decoder_data <= data_out; --
  ------------------------------------------------------------WIRE
  hash_id_hi_wire : block --
  begin
    --
    field_reg_hash_id_hi <= std_logic_vector(to_signed(1431677610,32)); --
    --no signal to read by HW
    po_reg.hash_id_hi.dummy <= '0'; --
  end block; --
end rtl;
-----------------------------------------------
-- register type: msk_init
-----------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

library desyrdl;
use desyrdl.common.all;

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

  -- assign slices of data_out for each field, but force the rest to constant zeros
  function fun_set_data_out ( --
    field_reg_txrxinit : std_logic_vector(1-1 downto 0); --
    field_reg_txinit : std_logic_vector(1-1 downto 0); --
    field_reg_rxinit : std_logic_vector(1-1 downto 0)) --
    return std_logic_vector is
    variable v_data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0);
  begin
    v_data_out := (others => '0');
    --
    v_data_out(0 downto 0) := field_reg_txrxinit; --
    v_data_out(1 downto 1) := field_reg_txinit; --
    v_data_out(2 downto 2) := field_reg_rxinit; --
    return v_data_out;
  end function fun_set_data_out;

  signal data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0) := (others => '0');
   --
  signal field_reg_txrxinit : std_logic_vector(1-1 downto 0)
    := std_logic_vector(to_signed(1,1)); --
  signal field_reg_txinit : std_logic_vector(1-1 downto 0)
    := std_logic_vector(to_signed(1,1)); --
  signal field_reg_rxinit : std_logic_vector(1-1 downto 0)
    := std_logic_vector(to_signed(1,1)); --
begin

  data_out <= fun_set_data_out( --
    field_reg_txrxinit, --
    field_reg_txinit, --
    field_reg_rxinit --
  );

  -- resize field data out to the register bus width
  -- do only if 1 field and signed--
  po_decoder_data <= data_out; --
  ------------------------------------------------------------STORAGE
  txrxinit_storage: block
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          field_reg_txrxinit <= std_logic_vector(to_signed(1,1));
        else
          -- HW --
          -- SW --
          if pi_decoder_wr_stb = '1' then
            field_reg_txrxinit <= pi_decoder_data(0 downto 0);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.txrxinit.data <= field_reg_txrxinit; --
  end block txrxinit_storage;
  ------------------------------------------------------------STORAGE
  txinit_storage: block
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          field_reg_txinit <= std_logic_vector(to_signed(1,1));
        else
          -- HW --
          -- SW --
          if pi_decoder_wr_stb = '1' then
            field_reg_txinit <= pi_decoder_data(1 downto 1);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.txinit.data <= field_reg_txinit; --
  end block txinit_storage;
  ------------------------------------------------------------STORAGE
  rxinit_storage: block
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          field_reg_rxinit <= std_logic_vector(to_signed(1,1));
        else
          -- HW --
          -- SW --
          if pi_decoder_wr_stb = '1' then
            field_reg_rxinit <= pi_decoder_data(2 downto 2);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.rxinit.data <= field_reg_rxinit; --
  end block rxinit_storage;
  ----------------------------------------------------------
end rtl;
-----------------------------------------------
-- register type: msk_ctrl
-----------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

library desyrdl;
use desyrdl.common.all;

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

  -- assign slices of data_out for each field, but force the rest to constant zeros
  function fun_set_data_out ( --
    field_reg_ptt : std_logic_vector(1-1 downto 0); --
    field_reg_loopback_ena : std_logic_vector(1-1 downto 0); --
    field_reg_rx_invert : std_logic_vector(1-1 downto 0); --
    field_reg_clear_counts : std_logic_vector(1-1 downto 0); --
    field_reg_diff_encoder_loopback : std_logic_vector(1-1 downto 0)) --
    return std_logic_vector is
    variable v_data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0);
  begin
    v_data_out := (others => '0');
    --
    v_data_out(0 downto 0) := field_reg_ptt; --
    v_data_out(1 downto 1) := field_reg_loopback_ena; --
    v_data_out(2 downto 2) := field_reg_rx_invert; --
    v_data_out(3 downto 3) := field_reg_clear_counts; --
    v_data_out(4 downto 4) := field_reg_diff_encoder_loopback; --
    return v_data_out;
  end function fun_set_data_out;

  signal data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0) := (others => '0');
   --
  signal field_reg_ptt : std_logic_vector(1-1 downto 0)
    := std_logic_vector(to_signed(0,1)); --
  signal field_reg_loopback_ena : std_logic_vector(1-1 downto 0)
    := std_logic_vector(to_signed(0,1)); --
  signal field_reg_rx_invert : std_logic_vector(1-1 downto 0)
    := std_logic_vector(to_signed(0,1)); --
  signal field_reg_clear_counts : std_logic_vector(1-1 downto 0)
    := std_logic_vector(to_signed(0,1)); --
  signal field_reg_diff_encoder_loopback : std_logic_vector(1-1 downto 0)
    := std_logic_vector(to_signed(0,1)); --
begin

  data_out <= fun_set_data_out( --
    field_reg_ptt, --
    field_reg_loopback_ena, --
    field_reg_rx_invert, --
    field_reg_clear_counts, --
    field_reg_diff_encoder_loopback --
  );

  -- resize field data out to the register bus width
  -- do only if 1 field and signed--
  po_decoder_data <= data_out; --
  ------------------------------------------------------------STORAGE
  ptt_storage: block
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          field_reg_ptt <= std_logic_vector(to_signed(0,1));
        else
          -- HW --
          -- SW --
          if pi_decoder_wr_stb = '1' then
            field_reg_ptt <= pi_decoder_data(0 downto 0);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.ptt.data <= field_reg_ptt; --
  end block ptt_storage;
  ------------------------------------------------------------STORAGE
  loopback_ena_storage: block
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          field_reg_loopback_ena <= std_logic_vector(to_signed(0,1));
        else
          -- HW --
          -- SW --
          if pi_decoder_wr_stb = '1' then
            field_reg_loopback_ena <= pi_decoder_data(1 downto 1);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.loopback_ena.data <= field_reg_loopback_ena; --
  end block loopback_ena_storage;
  ------------------------------------------------------------STORAGE
  rx_invert_storage: block
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          field_reg_rx_invert <= std_logic_vector(to_signed(0,1));
        else
          -- HW --
          -- SW --
          if pi_decoder_wr_stb = '1' then
            field_reg_rx_invert <= pi_decoder_data(2 downto 2);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.rx_invert.data <= field_reg_rx_invert; --
  end block rx_invert_storage;
  ------------------------------------------------------------STORAGE
  clear_counts_storage: block
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          field_reg_clear_counts <= std_logic_vector(to_signed(0,1));
        else
          -- HW --
          -- This is a "singlepulse" register - clear on each clock,
          -- unless it is written to with a 1 (see below)
          field_reg_clear_counts <= (others => '0');
          -- SW --
          if pi_decoder_wr_stb = '1' then
            field_reg_clear_counts <= pi_decoder_data(3 downto 3);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.clear_counts.data <= field_reg_clear_counts; --
  end block clear_counts_storage;
  ------------------------------------------------------------STORAGE
  diff_encoder_loopback_storage: block
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          field_reg_diff_encoder_loopback <= std_logic_vector(to_signed(0,1));
        else
          -- HW --
          -- SW --
          if pi_decoder_wr_stb = '1' then
            field_reg_diff_encoder_loopback <= pi_decoder_data(4 downto 4);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.diff_encoder_loopback.data <= field_reg_diff_encoder_loopback; --
  end block diff_encoder_loopback_storage;
  ----------------------------------------------------------
end rtl;
-----------------------------------------------
-- register type: msk_stat_0
-----------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

library desyrdl;
use desyrdl.common.all;

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

  -- assign slices of data_out for each field, but force the rest to constant zeros
  function fun_set_data_out ( --
    field_reg_demod_sync_lock : std_logic_vector(1-1 downto 0); --
    field_reg_tx_enable : std_logic_vector(1-1 downto 0); --
    field_reg_rx_enable : std_logic_vector(1-1 downto 0); --
    field_reg_tx_axis_valid : std_logic_vector(1-1 downto 0)) --
    return std_logic_vector is
    variable v_data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0);
  begin
    v_data_out := (others => '0');
    --
    v_data_out(0 downto 0) := field_reg_demod_sync_lock; --
    v_data_out(1 downto 1) := field_reg_tx_enable; --
    v_data_out(2 downto 2) := field_reg_rx_enable; --
    v_data_out(3 downto 3) := field_reg_tx_axis_valid; --
    return v_data_out;
  end function fun_set_data_out;

  signal data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0) := (others => '0');
   --
  signal field_reg_demod_sync_lock : std_logic_vector(1-1 downto 0)
    := std_logic_vector(to_signed(0,1)); --
  signal field_reg_tx_enable : std_logic_vector(1-1 downto 0)
    := std_logic_vector(to_signed(0,1)); --
  signal field_reg_rx_enable : std_logic_vector(1-1 downto 0)
    := std_logic_vector(to_signed(0,1)); --
  signal field_reg_tx_axis_valid : std_logic_vector(1-1 downto 0)
    := std_logic_vector(to_signed(0,1)); --
begin

  data_out <= fun_set_data_out( --
    field_reg_demod_sync_lock, --
    field_reg_tx_enable, --
    field_reg_rx_enable, --
    field_reg_tx_axis_valid --
  );

  -- resize field data out to the register bus width
  -- do only if 1 field and signed--
  po_decoder_data <= data_out; --
  ------------------------------------------------------------WIRE
  demod_sync_lock_wire : block --
  begin
    --
    field_reg_demod_sync_lock <= pi_reg.demod_sync_lock.data(1-1 downto 0); --
    --no signal to read by HW
    po_reg.demod_sync_lock.dummy <= '0'; --
  end block; ----WIRE
  tx_enable_wire : block --
  begin
    --
    field_reg_tx_enable <= pi_reg.tx_enable.data(1-1 downto 0); --
    --no signal to read by HW
    po_reg.tx_enable.dummy <= '0'; --
  end block; ----WIRE
  rx_enable_wire : block --
  begin
    --
    field_reg_rx_enable <= pi_reg.rx_enable.data(1-1 downto 0); --
    --no signal to read by HW
    po_reg.rx_enable.dummy <= '0'; --
  end block; ----WIRE
  tx_axis_valid_wire : block --
  begin
    --
    field_reg_tx_axis_valid <= pi_reg.tx_axis_valid.data(1-1 downto 0); --
    --no signal to read by HW
    po_reg.tx_axis_valid.dummy <= '0'; --
  end block; --
end rtl;
-----------------------------------------------
-- register type: msk_stat_1
-----------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

library desyrdl;
use desyrdl.common.all;

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

  -- assign slices of data_out for each field, but force the rest to constant zeros
  function fun_set_data_out ( --
    field_reg_tx_bit_counter : std_logic_vector(32-1 downto 0)) --
    return std_logic_vector is
    variable v_data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0);
  begin
    v_data_out := (others => '0');
    --
    v_data_out(31 downto 0) := field_reg_tx_bit_counter; --
    return v_data_out;
  end function fun_set_data_out;

  signal data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0) := (others => '0');
   --
  signal field_reg_tx_bit_counter : std_logic_vector(32-1 downto 0)
    := std_logic_vector(to_signed(0,32)); --
begin

  data_out <= fun_set_data_out( --
    field_reg_tx_bit_counter --
  );

  -- resize field data out to the register bus width
  -- do only if 1 field and signed--
  po_decoder_data <= data_out; --
  ------------------------------------------------------------WIRE
  tx_bit_counter_wire : block --
  begin
    --
    field_reg_tx_bit_counter <= pi_reg.tx_bit_counter.data(32-1 downto 0); --
    --no signal to read by HW
    po_reg.tx_bit_counter.dummy <= '0'; --
  end block; --
end rtl;
-----------------------------------------------
-- register type: msk_stat_2
-----------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

library desyrdl;
use desyrdl.common.all;

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

  -- assign slices of data_out for each field, but force the rest to constant zeros
  function fun_set_data_out ( --
    field_reg_tx_ena_counter : std_logic_vector(32-1 downto 0)) --
    return std_logic_vector is
    variable v_data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0);
  begin
    v_data_out := (others => '0');
    --
    v_data_out(31 downto 0) := field_reg_tx_ena_counter; --
    return v_data_out;
  end function fun_set_data_out;

  signal data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0) := (others => '0');
   --
  signal field_reg_tx_ena_counter : std_logic_vector(32-1 downto 0)
    := std_logic_vector(to_signed(0,32)); --
begin

  data_out <= fun_set_data_out( --
    field_reg_tx_ena_counter --
  );

  -- resize field data out to the register bus width
  -- do only if 1 field and signed--
  po_decoder_data <= data_out; --
  ------------------------------------------------------------WIRE
  tx_ena_counter_wire : block --
  begin
    --
    field_reg_tx_ena_counter <= pi_reg.tx_ena_counter.data(32-1 downto 0); --
    --no signal to read by HW
    po_reg.tx_ena_counter.dummy <= '0'; --
  end block; --
end rtl;
-----------------------------------------------
-- register type: config_nco_fw
-----------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

library desyrdl;
use desyrdl.common.all;

use work.pkg_msk_top_regs.all;

entity msk_top_regs_config_nco_fw is
  port (
    pi_clock        : in  std_logic;
    pi_reset        : in  std_logic;
    -- to/from adapter
    pi_decoder_rd_stb : in  std_logic;
    pi_decoder_wr_stb : in  std_logic;
    pi_decoder_data   : in  std_logic_vector(C_DATA_WIDTH-1 downto 0);
    po_decoder_data   : out std_logic_vector(C_DATA_WIDTH-1 downto 0);

    pi_reg  : in t_reg_config_nco_fw_in ;
    po_reg  : out t_reg_config_nco_fw_out
  );
end entity msk_top_regs_config_nco_fw;

architecture rtl of msk_top_regs_config_nco_fw is

  -- assign slices of data_out for each field, but force the rest to constant zeros
  function fun_set_data_out ( --
    field_reg_config_data : std_logic_vector(32-1 downto 0)) --
    return std_logic_vector is
    variable v_data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0);
  begin
    v_data_out := (others => '0');
    --
    v_data_out(31 downto 0) := field_reg_config_data; --
    return v_data_out;
  end function fun_set_data_out;

  signal data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0) := (others => '0');
   --
  signal field_reg_config_data : std_logic_vector(32-1 downto 0)
    := std_logic_vector(to_signed(0,32)); --
begin

  data_out <= fun_set_data_out( --
    field_reg_config_data --
  );

  -- resize field data out to the register bus width
  -- do only if 1 field and signed--
  po_decoder_data <= data_out; --
  ------------------------------------------------------------STORAGE
  config_data_storage: block
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          field_reg_config_data <= std_logic_vector(to_signed(0,32));
        else
          -- HW --
          -- SW --
          if pi_decoder_wr_stb = '1' then
            field_reg_config_data <= pi_decoder_data(31 downto 0);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.config_data.data <= field_reg_config_data; --
  end block config_data_storage;
  ----------------------------------------------------------
end rtl;
-----------------------------------------------
-- register type: lpf_config_0
-----------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

library desyrdl;
use desyrdl.common.all;

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

  -- assign slices of data_out for each field, but force the rest to constant zeros
  function fun_set_data_out ( --
    field_reg_lpf_freeze : std_logic_vector(1-1 downto 0); --
    field_reg_lpf_zero : std_logic_vector(1-1 downto 0); --
    field_reg_prbs_reserved : std_logic_vector(6-1 downto 0); --
    field_reg_lpf_alpha : std_logic_vector(24-1 downto 0)) --
    return std_logic_vector is
    variable v_data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0);
  begin
    v_data_out := (others => '0');
    --
    v_data_out(0 downto 0) := field_reg_lpf_freeze; --
    v_data_out(1 downto 1) := field_reg_lpf_zero; --
    v_data_out(7 downto 2) := field_reg_prbs_reserved; --
    v_data_out(31 downto 8) := field_reg_lpf_alpha; --
    return v_data_out;
  end function fun_set_data_out;

  signal data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0) := (others => '0');
   --
  signal field_reg_lpf_freeze : std_logic_vector(1-1 downto 0)
    := std_logic_vector(to_signed(0,1)); --
  signal field_reg_lpf_zero : std_logic_vector(1-1 downto 0)
    := std_logic_vector(to_signed(0,1)); --
  signal field_reg_prbs_reserved : std_logic_vector(6-1 downto 0)
    := std_logic_vector(to_signed(0,6)); --
  signal field_reg_lpf_alpha : std_logic_vector(24-1 downto 0)
    := std_logic_vector(to_signed(0,24)); --
begin

  data_out <= fun_set_data_out( --
    field_reg_lpf_freeze, --
    field_reg_lpf_zero, --
    field_reg_prbs_reserved, --
    field_reg_lpf_alpha --
  );

  -- resize field data out to the register bus width
  -- do only if 1 field and signed--
  po_decoder_data <= data_out; --
  ------------------------------------------------------------STORAGE
  lpf_freeze_storage: block
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          field_reg_lpf_freeze <= std_logic_vector(to_signed(0,1));
        else
          -- HW --
          -- SW --
          if pi_decoder_wr_stb = '1' then
            field_reg_lpf_freeze <= pi_decoder_data(0 downto 0);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.lpf_freeze.data <= field_reg_lpf_freeze; --
  end block lpf_freeze_storage;
  ------------------------------------------------------------STORAGE
  lpf_zero_storage: block
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          field_reg_lpf_zero <= std_logic_vector(to_signed(0,1));
        else
          -- HW --
          -- SW --
          if pi_decoder_wr_stb = '1' then
            field_reg_lpf_zero <= pi_decoder_data(1 downto 1);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.lpf_zero.data <= field_reg_lpf_zero; --
  end block lpf_zero_storage;
  ------------------------------------------------------------STORAGE
  prbs_reserved_storage: block
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          field_reg_prbs_reserved <= std_logic_vector(to_signed(0,6));
        else
          -- HW --
          -- SW --
          if pi_decoder_wr_stb = '1' then
            field_reg_prbs_reserved <= pi_decoder_data(7 downto 2);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.prbs_reserved.data <= field_reg_prbs_reserved; --
  end block prbs_reserved_storage;
  ------------------------------------------------------------STORAGE
  lpf_alpha_storage: block
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          field_reg_lpf_alpha <= std_logic_vector(to_signed(0,24));
        else
          -- HW --
          -- SW --
          if pi_decoder_wr_stb = '1' then
            field_reg_lpf_alpha <= pi_decoder_data(31 downto 8);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.lpf_alpha.data <= field_reg_lpf_alpha; --
  end block lpf_alpha_storage;
  ----------------------------------------------------------
end rtl;
-----------------------------------------------
-- register type: lpf_config_1
-----------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

library desyrdl;
use desyrdl.common.all;

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

  -- assign slices of data_out for each field, but force the rest to constant zeros
  function fun_set_data_out ( --
    field_reg_i_gain : std_logic_vector(24-1 downto 0); --
    field_reg_i_shift : std_logic_vector(8-1 downto 0)) --
    return std_logic_vector is
    variable v_data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0);
  begin
    v_data_out := (others => '0');
    --
    v_data_out(23 downto 0) := field_reg_i_gain; --
    v_data_out(31 downto 24) := field_reg_i_shift; --
    return v_data_out;
  end function fun_set_data_out;

  signal data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0) := (others => '0');
   --
  signal field_reg_i_gain : std_logic_vector(24-1 downto 0)
    := std_logic_vector(to_signed(0,24)); --
  signal field_reg_i_shift : std_logic_vector(8-1 downto 0)
    := std_logic_vector(to_signed(0,8)); --
begin

  data_out <= fun_set_data_out( --
    field_reg_i_gain, --
    field_reg_i_shift --
  );

  -- resize field data out to the register bus width
  -- do only if 1 field and signed--
  po_decoder_data <= data_out; --
  ------------------------------------------------------------STORAGE
  i_gain_storage: block
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          field_reg_i_gain <= std_logic_vector(to_signed(0,24));
        else
          -- HW --
          -- SW --
          if pi_decoder_wr_stb = '1' then
            field_reg_i_gain <= pi_decoder_data(23 downto 0);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.i_gain.data <= field_reg_i_gain; --
  end block i_gain_storage;
  ------------------------------------------------------------STORAGE
  i_shift_storage: block
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          field_reg_i_shift <= std_logic_vector(to_signed(0,8));
        else
          -- HW --
          -- SW --
          if pi_decoder_wr_stb = '1' then
            field_reg_i_shift <= pi_decoder_data(31 downto 24);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.i_shift.data <= field_reg_i_shift; --
  end block i_shift_storage;
  ----------------------------------------------------------
end rtl;
-----------------------------------------------
-- register type: data_width
-----------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

library desyrdl;
use desyrdl.common.all;

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

  -- assign slices of data_out for each field, but force the rest to constant zeros
  function fun_set_data_out ( --
    field_reg_data_width : std_logic_vector(8-1 downto 0)) --
    return std_logic_vector is
    variable v_data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0);
  begin
    v_data_out := (others => '0');
    --
    v_data_out(7 downto 0) := field_reg_data_width; --
    return v_data_out;
  end function fun_set_data_out;

  signal data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0) := (others => '0');
   --
  signal field_reg_data_width : std_logic_vector(8-1 downto 0)
    := std_logic_vector(to_signed(8,8)); --
begin

  data_out <= fun_set_data_out( --
    field_reg_data_width --
  );

  -- resize field data out to the register bus width
  -- do only if 1 field and signed--
  po_decoder_data <= data_out; --
  ------------------------------------------------------------STORAGE
  data_width_storage: block
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          field_reg_data_width <= std_logic_vector(to_signed(8,8));
        else
          -- HW --
          -- SW --
          if pi_decoder_wr_stb = '1' then
            field_reg_data_width <= pi_decoder_data(7 downto 0);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.data_width.data <= field_reg_data_width; --
  end block data_width_storage;
  ----------------------------------------------------------
end rtl;
-----------------------------------------------
-- register type: prbs_ctrl
-----------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

library desyrdl;
use desyrdl.common.all;

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

  -- assign slices of data_out for each field, but force the rest to constant zeros
  function fun_set_data_out ( --
    field_reg_prbs_sel : std_logic_vector(1-1 downto 0); --
    field_reg_prbs_error_insert : std_logic_vector(1-1 downto 0); --
    field_reg_prbs_clear : std_logic_vector(1-1 downto 0); --
    field_reg_prbs_manual_sync : std_logic_vector(1-1 downto 0); --
    field_reg_prbs_reserved : std_logic_vector(12-1 downto 0); --
    field_reg_prbs_sync_threshold : std_logic_vector(16-1 downto 0)) --
    return std_logic_vector is
    variable v_data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0);
  begin
    v_data_out := (others => '0');
    --
    v_data_out(0 downto 0) := field_reg_prbs_sel; --
    v_data_out(1 downto 1) := field_reg_prbs_error_insert; --
    v_data_out(2 downto 2) := field_reg_prbs_clear; --
    v_data_out(3 downto 3) := field_reg_prbs_manual_sync; --
    v_data_out(15 downto 4) := field_reg_prbs_reserved; --
    v_data_out(31 downto 16) := field_reg_prbs_sync_threshold; --
    return v_data_out;
  end function fun_set_data_out;

  signal data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0) := (others => '0');
   --
  signal field_reg_prbs_sel : std_logic_vector(1-1 downto 0)
    := std_logic_vector(to_signed(0,1)); --
  signal field_reg_prbs_error_insert : std_logic_vector(1-1 downto 0)
    := std_logic_vector(to_signed(0,1)); --
  signal field_reg_prbs_clear : std_logic_vector(1-1 downto 0)
    := std_logic_vector(to_signed(0,1)); --
  signal field_reg_prbs_manual_sync : std_logic_vector(1-1 downto 0)
    := std_logic_vector(to_signed(0,1)); --
  signal field_reg_prbs_reserved : std_logic_vector(12-1 downto 0)
    := std_logic_vector(to_signed(0,12)); --
  signal field_reg_prbs_sync_threshold : std_logic_vector(16-1 downto 0)
    := std_logic_vector(to_signed(0,16)); --
begin

  data_out <= fun_set_data_out( --
    field_reg_prbs_sel, --
    field_reg_prbs_error_insert, --
    field_reg_prbs_clear, --
    field_reg_prbs_manual_sync, --
    field_reg_prbs_reserved, --
    field_reg_prbs_sync_threshold --
  );

  -- resize field data out to the register bus width
  -- do only if 1 field and signed--
  po_decoder_data <= data_out; --
  ------------------------------------------------------------STORAGE
  prbs_sel_storage: block
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          field_reg_prbs_sel <= std_logic_vector(to_signed(0,1));
        else
          -- HW --
          -- SW --
          if pi_decoder_wr_stb = '1' then
            field_reg_prbs_sel <= pi_decoder_data(0 downto 0);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.prbs_sel.data <= field_reg_prbs_sel; --
  end block prbs_sel_storage;
  ------------------------------------------------------------STORAGE
  prbs_error_insert_storage: block
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          field_reg_prbs_error_insert <= std_logic_vector(to_signed(0,1));
        else
          -- HW --
          -- This is a "singlepulse" register - clear on each clock,
          -- unless it is written to with a 1 (see below)
          field_reg_prbs_error_insert <= (others => '0');
          -- SW --
          if pi_decoder_wr_stb = '1' then
            field_reg_prbs_error_insert <= pi_decoder_data(1 downto 1);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.prbs_error_insert.data <= field_reg_prbs_error_insert; --
  end block prbs_error_insert_storage;
  ------------------------------------------------------------STORAGE
  prbs_clear_storage: block
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          field_reg_prbs_clear <= std_logic_vector(to_signed(0,1));
        else
          -- HW --
          -- This is a "singlepulse" register - clear on each clock,
          -- unless it is written to with a 1 (see below)
          field_reg_prbs_clear <= (others => '0');
          -- SW --
          if pi_decoder_wr_stb = '1' then
            field_reg_prbs_clear <= pi_decoder_data(2 downto 2);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.prbs_clear.data <= field_reg_prbs_clear; --
  end block prbs_clear_storage;
  ------------------------------------------------------------STORAGE
  prbs_manual_sync_storage: block
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          field_reg_prbs_manual_sync <= std_logic_vector(to_signed(0,1));
        else
          -- HW --
          -- This is a "singlepulse" register - clear on each clock,
          -- unless it is written to with a 1 (see below)
          field_reg_prbs_manual_sync <= (others => '0');
          -- SW --
          if pi_decoder_wr_stb = '1' then
            field_reg_prbs_manual_sync <= pi_decoder_data(3 downto 3);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.prbs_manual_sync.data <= field_reg_prbs_manual_sync; --
  end block prbs_manual_sync_storage;
  ------------------------------------------------------------STORAGE
  prbs_reserved_storage: block
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          field_reg_prbs_reserved <= std_logic_vector(to_signed(0,12));
        else
          -- HW --
          -- SW --
          if pi_decoder_wr_stb = '1' then
            field_reg_prbs_reserved <= pi_decoder_data(15 downto 4);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.prbs_reserved.data <= field_reg_prbs_reserved; --
  end block prbs_reserved_storage;
  ------------------------------------------------------------STORAGE
  prbs_sync_threshold_storage: block
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          field_reg_prbs_sync_threshold <= std_logic_vector(to_signed(0,16));
        else
          -- HW --
          -- SW --
          if pi_decoder_wr_stb = '1' then
            field_reg_prbs_sync_threshold <= pi_decoder_data(31 downto 16);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.prbs_sync_threshold.data <= field_reg_prbs_sync_threshold; --
  end block prbs_sync_threshold_storage;
  ----------------------------------------------------------
end rtl;
-----------------------------------------------
-- register type: config_prbs_seed
-----------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

library desyrdl;
use desyrdl.common.all;

use work.pkg_msk_top_regs.all;

entity msk_top_regs_config_prbs_seed is
  port (
    pi_clock        : in  std_logic;
    pi_reset        : in  std_logic;
    -- to/from adapter
    pi_decoder_rd_stb : in  std_logic;
    pi_decoder_wr_stb : in  std_logic;
    pi_decoder_data   : in  std_logic_vector(C_DATA_WIDTH-1 downto 0);
    po_decoder_data   : out std_logic_vector(C_DATA_WIDTH-1 downto 0);

    pi_reg  : in t_reg_config_prbs_seed_in ;
    po_reg  : out t_reg_config_prbs_seed_out
  );
end entity msk_top_regs_config_prbs_seed;

architecture rtl of msk_top_regs_config_prbs_seed is

  -- assign slices of data_out for each field, but force the rest to constant zeros
  function fun_set_data_out ( --
    field_reg_config_data : std_logic_vector(32-1 downto 0)) --
    return std_logic_vector is
    variable v_data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0);
  begin
    v_data_out := (others => '0');
    --
    v_data_out(31 downto 0) := field_reg_config_data; --
    return v_data_out;
  end function fun_set_data_out;

  signal data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0) := (others => '0');
   --
  signal field_reg_config_data : std_logic_vector(32-1 downto 0)
    := std_logic_vector(to_signed(0,32)); --
begin

  data_out <= fun_set_data_out( --
    field_reg_config_data --
  );

  -- resize field data out to the register bus width
  -- do only if 1 field and signed--
  po_decoder_data <= data_out; --
  ------------------------------------------------------------STORAGE
  config_data_storage: block
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          field_reg_config_data <= std_logic_vector(to_signed(0,32));
        else
          -- HW --
          -- SW --
          if pi_decoder_wr_stb = '1' then
            field_reg_config_data <= pi_decoder_data(31 downto 0);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.config_data.data <= field_reg_config_data; --
  end block config_data_storage;
  ----------------------------------------------------------
end rtl;
-----------------------------------------------
-- register type: config_prbs_poly
-----------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

library desyrdl;
use desyrdl.common.all;

use work.pkg_msk_top_regs.all;

entity msk_top_regs_config_prbs_poly is
  port (
    pi_clock        : in  std_logic;
    pi_reset        : in  std_logic;
    -- to/from adapter
    pi_decoder_rd_stb : in  std_logic;
    pi_decoder_wr_stb : in  std_logic;
    pi_decoder_data   : in  std_logic_vector(C_DATA_WIDTH-1 downto 0);
    po_decoder_data   : out std_logic_vector(C_DATA_WIDTH-1 downto 0);

    pi_reg  : in t_reg_config_prbs_poly_in ;
    po_reg  : out t_reg_config_prbs_poly_out
  );
end entity msk_top_regs_config_prbs_poly;

architecture rtl of msk_top_regs_config_prbs_poly is

  -- assign slices of data_out for each field, but force the rest to constant zeros
  function fun_set_data_out ( --
    field_reg_config_data : std_logic_vector(32-1 downto 0)) --
    return std_logic_vector is
    variable v_data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0);
  begin
    v_data_out := (others => '0');
    --
    v_data_out(31 downto 0) := field_reg_config_data; --
    return v_data_out;
  end function fun_set_data_out;

  signal data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0) := (others => '0');
   --
  signal field_reg_config_data : std_logic_vector(32-1 downto 0)
    := std_logic_vector(to_signed(0,32)); --
begin

  data_out <= fun_set_data_out( --
    field_reg_config_data --
  );

  -- resize field data out to the register bus width
  -- do only if 1 field and signed--
  po_decoder_data <= data_out; --
  ------------------------------------------------------------STORAGE
  config_data_storage: block
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          field_reg_config_data <= std_logic_vector(to_signed(0,32));
        else
          -- HW --
          -- SW --
          if pi_decoder_wr_stb = '1' then
            field_reg_config_data <= pi_decoder_data(31 downto 0);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.config_data.data <= field_reg_config_data; --
  end block config_data_storage;
  ----------------------------------------------------------
end rtl;
-----------------------------------------------
-- register type: config_prbs_errmask
-----------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

library desyrdl;
use desyrdl.common.all;

use work.pkg_msk_top_regs.all;

entity msk_top_regs_config_prbs_errmask is
  port (
    pi_clock        : in  std_logic;
    pi_reset        : in  std_logic;
    -- to/from adapter
    pi_decoder_rd_stb : in  std_logic;
    pi_decoder_wr_stb : in  std_logic;
    pi_decoder_data   : in  std_logic_vector(C_DATA_WIDTH-1 downto 0);
    po_decoder_data   : out std_logic_vector(C_DATA_WIDTH-1 downto 0);

    pi_reg  : in t_reg_config_prbs_errmask_in ;
    po_reg  : out t_reg_config_prbs_errmask_out
  );
end entity msk_top_regs_config_prbs_errmask;

architecture rtl of msk_top_regs_config_prbs_errmask is

  -- assign slices of data_out for each field, but force the rest to constant zeros
  function fun_set_data_out ( --
    field_reg_config_data : std_logic_vector(32-1 downto 0)) --
    return std_logic_vector is
    variable v_data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0);
  begin
    v_data_out := (others => '0');
    --
    v_data_out(31 downto 0) := field_reg_config_data; --
    return v_data_out;
  end function fun_set_data_out;

  signal data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0) := (others => '0');
   --
  signal field_reg_config_data : std_logic_vector(32-1 downto 0)
    := std_logic_vector(to_signed(0,32)); --
begin

  data_out <= fun_set_data_out( --
    field_reg_config_data --
  );

  -- resize field data out to the register bus width
  -- do only if 1 field and signed--
  po_decoder_data <= data_out; --
  ------------------------------------------------------------STORAGE
  config_data_storage: block
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          field_reg_config_data <= std_logic_vector(to_signed(0,32));
        else
          -- HW --
          -- SW --
          if pi_decoder_wr_stb = '1' then
            field_reg_config_data <= pi_decoder_data(31 downto 0);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.config_data.data <= field_reg_config_data; --
  end block config_data_storage;
  ----------------------------------------------------------
end rtl;
-----------------------------------------------
-- register type: stat_32_bits
-----------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

library desyrdl;
use desyrdl.common.all;

use work.pkg_msk_top_regs.all;

entity msk_top_regs_stat_32_bits is
  port (
    pi_clock        : in  std_logic;
    pi_reset        : in  std_logic;
    -- to/from adapter
    pi_decoder_rd_stb : in  std_logic;
    pi_decoder_wr_stb : in  std_logic;
    pi_decoder_data   : in  std_logic_vector(C_DATA_WIDTH-1 downto 0);
    po_decoder_data   : out std_logic_vector(C_DATA_WIDTH-1 downto 0);

    pi_reg  : in t_reg_stat_32_bits_in ;
    po_reg  : out t_reg_stat_32_bits_out
  );
end entity msk_top_regs_stat_32_bits;

architecture rtl of msk_top_regs_stat_32_bits is

  -- assign slices of data_out for each field, but force the rest to constant zeros
  function fun_set_data_out ( --
    field_reg_status_data : std_logic_vector(32-1 downto 0)) --
    return std_logic_vector is
    variable v_data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0);
  begin
    v_data_out := (others => '0');
    --
    v_data_out(31 downto 0) := field_reg_status_data; --
    return v_data_out;
  end function fun_set_data_out;

  signal data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0) := (others => '0');
   --
  signal field_reg_status_data : std_logic_vector(32-1 downto 0)
    := std_logic_vector(to_signed(0,32)); --
begin

  data_out <= fun_set_data_out( --
    field_reg_status_data --
  );

  -- resize field data out to the register bus width
  -- do only if 1 field and signed--
  po_decoder_data <= data_out; --
  ------------------------------------------------------------WIRE
  status_data_wire : block --
  begin
    --
    field_reg_status_data <= pi_reg.status_data.data(32-1 downto 0); --
    --no signal to read by HW
    po_reg.status_data.dummy <= '0'; --
  end block; --
end rtl;
-----------------------------------------------
-- register type: stat_32_errs
-----------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

library desyrdl;
use desyrdl.common.all;

use work.pkg_msk_top_regs.all;

entity msk_top_regs_stat_32_errs is
  port (
    pi_clock        : in  std_logic;
    pi_reset        : in  std_logic;
    -- to/from adapter
    pi_decoder_rd_stb : in  std_logic;
    pi_decoder_wr_stb : in  std_logic;
    pi_decoder_data   : in  std_logic_vector(C_DATA_WIDTH-1 downto 0);
    po_decoder_data   : out std_logic_vector(C_DATA_WIDTH-1 downto 0);

    pi_reg  : in t_reg_stat_32_errs_in ;
    po_reg  : out t_reg_stat_32_errs_out
  );
end entity msk_top_regs_stat_32_errs;

architecture rtl of msk_top_regs_stat_32_errs is

  -- assign slices of data_out for each field, but force the rest to constant zeros
  function fun_set_data_out ( --
    field_reg_status_data : std_logic_vector(32-1 downto 0)) --
    return std_logic_vector is
    variable v_data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0);
  begin
    v_data_out := (others => '0');
    --
    v_data_out(31 downto 0) := field_reg_status_data; --
    return v_data_out;
  end function fun_set_data_out;

  signal data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0) := (others => '0');
   --
  signal field_reg_status_data : std_logic_vector(32-1 downto 0)
    := std_logic_vector(to_signed(0,32)); --
begin

  data_out <= fun_set_data_out( --
    field_reg_status_data --
  );

  -- resize field data out to the register bus width
  -- do only if 1 field and signed--
  po_decoder_data <= data_out; --
  ------------------------------------------------------------WIRE
  status_data_wire : block --
  begin
    --
    field_reg_status_data <= pi_reg.status_data.data(32-1 downto 0); --
    --no signal to read by HW
    po_reg.status_data.dummy <= '0'; --
  end block; --
end rtl;
-----------------------------------------------
-- register type: stat_32_lpf_acc
-----------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

library desyrdl;
use desyrdl.common.all;

use work.pkg_msk_top_regs.all;

entity msk_top_regs_stat_32_lpf_acc is
  port (
    pi_clock        : in  std_logic;
    pi_reset        : in  std_logic;
    -- to/from adapter
    pi_decoder_rd_stb : in  std_logic;
    pi_decoder_wr_stb : in  std_logic;
    pi_decoder_data   : in  std_logic_vector(C_DATA_WIDTH-1 downto 0);
    po_decoder_data   : out std_logic_vector(C_DATA_WIDTH-1 downto 0);

    pi_reg  : in t_reg_stat_32_lpf_acc_in ;
    po_reg  : out t_reg_stat_32_lpf_acc_out
  );
end entity msk_top_regs_stat_32_lpf_acc;

architecture rtl of msk_top_regs_stat_32_lpf_acc is

  -- assign slices of data_out for each field, but force the rest to constant zeros
  function fun_set_data_out ( --
    field_reg_status_data : std_logic_vector(32-1 downto 0)) --
    return std_logic_vector is
    variable v_data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0);
  begin
    v_data_out := (others => '0');
    --
    v_data_out(31 downto 0) := field_reg_status_data; --
    return v_data_out;
  end function fun_set_data_out;

  signal data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0) := (others => '0');
   --
  signal field_reg_status_data : std_logic_vector(32-1 downto 0)
    := std_logic_vector(to_signed(0,32)); --
begin

  data_out <= fun_set_data_out( --
    field_reg_status_data --
  );

  -- resize field data out to the register bus width
  -- do only if 1 field and signed--
  po_decoder_data <= data_out; --
  ------------------------------------------------------------WIRE
  status_data_wire : block --
  begin
    --
    field_reg_status_data <= pi_reg.status_data.data(32-1 downto 0); --
    --no signal to read by HW
    po_reg.status_data.dummy <= '0'; --
  end block; --
end rtl;
-----------------------------------------------
-- register type: msk_stat_3
-----------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

library desyrdl;
use desyrdl.common.all;

use work.pkg_msk_top_regs.all;

entity msk_top_regs_msk_stat_3 is
  port (
    pi_clock        : in  std_logic;
    pi_reset        : in  std_logic;
    -- to/from adapter
    pi_decoder_rd_stb : in  std_logic;
    pi_decoder_wr_stb : in  std_logic;
    pi_decoder_data   : in  std_logic_vector(C_DATA_WIDTH-1 downto 0);
    po_decoder_data   : out std_logic_vector(C_DATA_WIDTH-1 downto 0);

    pi_reg  : in t_reg_msk_stat_3_in ;
    po_reg  : out t_reg_msk_stat_3_out
  );
end entity msk_top_regs_msk_stat_3;

architecture rtl of msk_top_regs_msk_stat_3 is

  -- assign slices of data_out for each field, but force the rest to constant zeros
  function fun_set_data_out ( --
    field_reg_xfer_count : std_logic_vector(32-1 downto 0)) --
    return std_logic_vector is
    variable v_data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0);
  begin
    v_data_out := (others => '0');
    --
    v_data_out(31 downto 0) := field_reg_xfer_count; --
    return v_data_out;
  end function fun_set_data_out;

  signal data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0) := (others => '0');
   --
  signal field_reg_xfer_count : std_logic_vector(32-1 downto 0)
    := std_logic_vector(to_signed(0,32)); --
begin

  data_out <= fun_set_data_out( --
    field_reg_xfer_count --
  );

  -- resize field data out to the register bus width
  -- do only if 1 field and signed--
  po_decoder_data <= data_out; --
  ------------------------------------------------------------WIRE
  xfer_count_wire : block --
  begin
    --
    field_reg_xfer_count <= pi_reg.xfer_count.data(32-1 downto 0); --
    --no signal to read by HW
    po_reg.xfer_count.dummy <= '0'; --
  end block; --
end rtl;
-----------------------------------------------
-- register type: rx_sample_discard
-----------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

library desyrdl;
use desyrdl.common.all;

use work.pkg_msk_top_regs.all;

entity msk_top_regs_rx_sample_discard is
  port (
    pi_clock        : in  std_logic;
    pi_reset        : in  std_logic;
    -- to/from adapter
    pi_decoder_rd_stb : in  std_logic;
    pi_decoder_wr_stb : in  std_logic;
    pi_decoder_data   : in  std_logic_vector(C_DATA_WIDTH-1 downto 0);
    po_decoder_data   : out std_logic_vector(C_DATA_WIDTH-1 downto 0);

    pi_reg  : in t_reg_rx_sample_discard_in ;
    po_reg  : out t_reg_rx_sample_discard_out
  );
end entity msk_top_regs_rx_sample_discard;

architecture rtl of msk_top_regs_rx_sample_discard is

  -- assign slices of data_out for each field, but force the rest to constant zeros
  function fun_set_data_out ( --
    field_reg_rx_sample_discard : std_logic_vector(8-1 downto 0); --
    field_reg_rx_nco_discard : std_logic_vector(8-1 downto 0)) --
    return std_logic_vector is
    variable v_data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0);
  begin
    v_data_out := (others => '0');
    --
    v_data_out(7 downto 0) := field_reg_rx_sample_discard; --
    v_data_out(15 downto 8) := field_reg_rx_nco_discard; --
    return v_data_out;
  end function fun_set_data_out;

  signal data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0) := (others => '0');
   --
  signal field_reg_rx_sample_discard : std_logic_vector(8-1 downto 0)
    := std_logic_vector(to_signed(0,8)); --
  signal field_reg_rx_nco_discard : std_logic_vector(8-1 downto 0)
    := std_logic_vector(to_signed(0,8)); --
begin

  data_out <= fun_set_data_out( --
    field_reg_rx_sample_discard, --
    field_reg_rx_nco_discard --
  );

  -- resize field data out to the register bus width
  -- do only if 1 field and signed--
  po_decoder_data <= data_out; --
  ------------------------------------------------------------STORAGE
  rx_sample_discard_storage: block
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          field_reg_rx_sample_discard <= std_logic_vector(to_signed(0,8));
        else
          -- HW --
          -- SW --
          if pi_decoder_wr_stb = '1' then
            field_reg_rx_sample_discard <= pi_decoder_data(7 downto 0);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.rx_sample_discard.data <= field_reg_rx_sample_discard; --
  end block rx_sample_discard_storage;
  ------------------------------------------------------------STORAGE
  rx_nco_discard_storage: block
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          field_reg_rx_nco_discard <= std_logic_vector(to_signed(0,8));
        else
          -- HW --
          -- SW --
          if pi_decoder_wr_stb = '1' then
            field_reg_rx_nco_discard <= pi_decoder_data(15 downto 8);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.rx_nco_discard.data <= field_reg_rx_nco_discard; --
  end block rx_nco_discard_storage;
  ----------------------------------------------------------
end rtl;
-----------------------------------------------
-- register type: lpf_config_2
-----------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

library desyrdl;
use desyrdl.common.all;

use work.pkg_msk_top_regs.all;

entity msk_top_regs_lpf_config_2 is
  port (
    pi_clock        : in  std_logic;
    pi_reset        : in  std_logic;
    -- to/from adapter
    pi_decoder_rd_stb : in  std_logic;
    pi_decoder_wr_stb : in  std_logic;
    pi_decoder_data   : in  std_logic_vector(C_DATA_WIDTH-1 downto 0);
    po_decoder_data   : out std_logic_vector(C_DATA_WIDTH-1 downto 0);

    pi_reg  : in t_reg_lpf_config_2_in ;
    po_reg  : out t_reg_lpf_config_2_out
  );
end entity msk_top_regs_lpf_config_2;

architecture rtl of msk_top_regs_lpf_config_2 is

  -- assign slices of data_out for each field, but force the rest to constant zeros
  function fun_set_data_out ( --
    field_reg_p_gain : std_logic_vector(24-1 downto 0); --
    field_reg_p_shift : std_logic_vector(8-1 downto 0)) --
    return std_logic_vector is
    variable v_data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0);
  begin
    v_data_out := (others => '0');
    --
    v_data_out(23 downto 0) := field_reg_p_gain; --
    v_data_out(31 downto 24) := field_reg_p_shift; --
    return v_data_out;
  end function fun_set_data_out;

  signal data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0) := (others => '0');
   --
  signal field_reg_p_gain : std_logic_vector(24-1 downto 0)
    := std_logic_vector(to_signed(0,24)); --
  signal field_reg_p_shift : std_logic_vector(8-1 downto 0)
    := std_logic_vector(to_signed(0,8)); --
begin

  data_out <= fun_set_data_out( --
    field_reg_p_gain, --
    field_reg_p_shift --
  );

  -- resize field data out to the register bus width
  -- do only if 1 field and signed--
  po_decoder_data <= data_out; --
  ------------------------------------------------------------STORAGE
  p_gain_storage: block
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          field_reg_p_gain <= std_logic_vector(to_signed(0,24));
        else
          -- HW --
          -- SW --
          if pi_decoder_wr_stb = '1' then
            field_reg_p_gain <= pi_decoder_data(23 downto 0);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.p_gain.data <= field_reg_p_gain; --
  end block p_gain_storage;
  ------------------------------------------------------------STORAGE
  p_shift_storage: block
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          field_reg_p_shift <= std_logic_vector(to_signed(0,8));
        else
          -- HW --
          -- SW --
          if pi_decoder_wr_stb = '1' then
            field_reg_p_shift <= pi_decoder_data(31 downto 24);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.p_shift.data <= field_reg_p_shift; --
  end block p_shift_storage;
  ----------------------------------------------------------
end rtl;
-----------------------------------------------
-- register type: observation_data
-----------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

library desyrdl;
use desyrdl.common.all;

use work.pkg_msk_top_regs.all;

entity msk_top_regs_observation_data is
  port (
    pi_clock        : in  std_logic;
    pi_reset        : in  std_logic;
    -- to/from adapter
    pi_decoder_rd_stb : in  std_logic;
    pi_decoder_wr_stb : in  std_logic;
    pi_decoder_data   : in  std_logic_vector(C_DATA_WIDTH-1 downto 0);
    po_decoder_data   : out std_logic_vector(C_DATA_WIDTH-1 downto 0);

    pi_reg  : in t_reg_observation_data_in ;
    po_reg  : out t_reg_observation_data_out
  );
end entity msk_top_regs_observation_data;

architecture rtl of msk_top_regs_observation_data is

  -- assign slices of data_out for each field, but force the rest to constant zeros
  function fun_set_data_out ( --
    field_reg_data32 : std_logic_vector(32-1 downto 0)) --
    return std_logic_vector is
    variable v_data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0);
  begin
    v_data_out := (others => '0');
    --
    v_data_out(31 downto 0) := field_reg_data32; --
    return v_data_out;
  end function fun_set_data_out;

  signal data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0) := (others => '0');
   --
  signal field_reg_data32 : std_logic_vector(32-1 downto 0)
    := std_logic_vector(to_signed(0,32)); --
begin

  data_out <= fun_set_data_out( --
    field_reg_data32 --
  );

  -- resize field data out to the register bus width
  -- do only if 1 field and signed--
  po_decoder_data <= data_out; --
  ------------------------------------------------------------WIRE
  data32_wire : block --
  begin
    --
    field_reg_data32 <= pi_reg.data.data(32-1 downto 0); --
    --no signal to read by HW
    po_reg.data.dummy <= '0'; --
  end block; --
end rtl;
-----------------------------------------------
-- register type: tx_sync_ctrl
-----------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

library desyrdl;
use desyrdl.common.all;

use work.pkg_msk_top_regs.all;

entity msk_top_regs_tx_sync_ctrl is
  port (
    pi_clock        : in  std_logic;
    pi_reset        : in  std_logic;
    -- to/from adapter
    pi_decoder_rd_stb : in  std_logic;
    pi_decoder_wr_stb : in  std_logic;
    pi_decoder_data   : in  std_logic_vector(C_DATA_WIDTH-1 downto 0);
    po_decoder_data   : out std_logic_vector(C_DATA_WIDTH-1 downto 0);

    pi_reg  : in t_reg_tx_sync_ctrl_in ;
    po_reg  : out t_reg_tx_sync_ctrl_out
  );
end entity msk_top_regs_tx_sync_ctrl;

architecture rtl of msk_top_regs_tx_sync_ctrl is

  -- assign slices of data_out for each field, but force the rest to constant zeros
  function fun_set_data_out ( --
    field_reg_tx_sync_ena : std_logic_vector(1-1 downto 0); --
    field_reg_tx_sync_force : std_logic_vector(1-1 downto 0); --
    field_reg_tx_sync_f1 : std_logic_vector(1-1 downto 0); --
    field_reg_tx_sync_f2 : std_logic_vector(1-1 downto 0)) --
    return std_logic_vector is
    variable v_data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0);
  begin
    v_data_out := (others => '0');
    --
    v_data_out(0 downto 0) := field_reg_tx_sync_ena; --
    v_data_out(1 downto 1) := field_reg_tx_sync_force; --
    v_data_out(2 downto 2) := field_reg_tx_sync_f1; --
    v_data_out(3 downto 3) := field_reg_tx_sync_f2; --
    return v_data_out;
  end function fun_set_data_out;

  signal data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0) := (others => '0');
   --
  signal field_reg_tx_sync_ena : std_logic_vector(1-1 downto 0)
    := std_logic_vector(to_signed(0,1)); --
  signal field_reg_tx_sync_force : std_logic_vector(1-1 downto 0)
    := std_logic_vector(to_signed(0,1)); --
  signal field_reg_tx_sync_f1 : std_logic_vector(1-1 downto 0)
    := std_logic_vector(to_signed(0,1)); --
  signal field_reg_tx_sync_f2 : std_logic_vector(1-1 downto 0)
    := std_logic_vector(to_signed(0,1)); --
begin

  data_out <= fun_set_data_out( --
    field_reg_tx_sync_ena, --
    field_reg_tx_sync_force, --
    field_reg_tx_sync_f1, --
    field_reg_tx_sync_f2 --
  );

  -- resize field data out to the register bus width
  -- do only if 1 field and signed--
  po_decoder_data <= data_out; --
  ------------------------------------------------------------STORAGE
  tx_sync_ena_storage: block
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          field_reg_tx_sync_ena <= std_logic_vector(to_signed(0,1));
        else
          -- HW --
          -- SW --
          if pi_decoder_wr_stb = '1' then
            field_reg_tx_sync_ena <= pi_decoder_data(0 downto 0);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.tx_sync_ena.data <= field_reg_tx_sync_ena; --
  end block tx_sync_ena_storage;
  ------------------------------------------------------------STORAGE
  tx_sync_force_storage: block
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          field_reg_tx_sync_force <= std_logic_vector(to_signed(0,1));
        else
          -- HW --
          -- SW --
          if pi_decoder_wr_stb = '1' then
            field_reg_tx_sync_force <= pi_decoder_data(1 downto 1);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.tx_sync_force.data <= field_reg_tx_sync_force; --
  end block tx_sync_force_storage;
  ------------------------------------------------------------STORAGE
  tx_sync_f1_storage: block
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          field_reg_tx_sync_f1 <= std_logic_vector(to_signed(0,1));
        else
          -- HW --
          -- SW --
          if pi_decoder_wr_stb = '1' then
            field_reg_tx_sync_f1 <= pi_decoder_data(2 downto 2);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.tx_sync_f1.data <= field_reg_tx_sync_f1; --
  end block tx_sync_f1_storage;
  ------------------------------------------------------------STORAGE
  tx_sync_f2_storage: block
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          field_reg_tx_sync_f2 <= std_logic_vector(to_signed(0,1));
        else
          -- HW --
          -- SW --
          if pi_decoder_wr_stb = '1' then
            field_reg_tx_sync_f2 <= pi_decoder_data(3 downto 3);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.tx_sync_f2.data <= field_reg_tx_sync_f2; --
  end block tx_sync_f2_storage;
  ----------------------------------------------------------
end rtl;
-----------------------------------------------
-- register type: tx_sync_cnt
-----------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

library desyrdl;
use desyrdl.common.all;

use work.pkg_msk_top_regs.all;

entity msk_top_regs_tx_sync_cnt is
  port (
    pi_clock        : in  std_logic;
    pi_reset        : in  std_logic;
    -- to/from adapter
    pi_decoder_rd_stb : in  std_logic;
    pi_decoder_wr_stb : in  std_logic;
    pi_decoder_data   : in  std_logic_vector(C_DATA_WIDTH-1 downto 0);
    po_decoder_data   : out std_logic_vector(C_DATA_WIDTH-1 downto 0);

    pi_reg  : in t_reg_tx_sync_cnt_in ;
    po_reg  : out t_reg_tx_sync_cnt_out
  );
end entity msk_top_regs_tx_sync_cnt;

architecture rtl of msk_top_regs_tx_sync_cnt is

  -- assign slices of data_out for each field, but force the rest to constant zeros
  function fun_set_data_out ( --
    field_reg_tx_sync_cnt : std_logic_vector(24-1 downto 0)) --
    return std_logic_vector is
    variable v_data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0);
  begin
    v_data_out := (others => '0');
    --
    v_data_out(23 downto 0) := field_reg_tx_sync_cnt; --
    return v_data_out;
  end function fun_set_data_out;

  signal data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0) := (others => '0');
   --
  signal field_reg_tx_sync_cnt : std_logic_vector(24-1 downto 0)
    := std_logic_vector(to_signed(0,24)); --
begin

  data_out <= fun_set_data_out( --
    field_reg_tx_sync_cnt --
  );

  -- resize field data out to the register bus width
  -- do only if 1 field and signed--
  po_decoder_data <= data_out; --
  ------------------------------------------------------------STORAGE
  tx_sync_cnt_storage: block
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          field_reg_tx_sync_cnt <= std_logic_vector(to_signed(0,24));
        else
          -- HW --
          -- SW --
          if pi_decoder_wr_stb = '1' then
            field_reg_tx_sync_cnt <= pi_decoder_data(23 downto 0);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.tx_sync_cnt.data <= field_reg_tx_sync_cnt; --
  end block tx_sync_cnt_storage;
  ----------------------------------------------------------
end rtl;
-----------------------------------------------
-- register type: lowpass_ema_alpha
-----------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

library desyrdl;
use desyrdl.common.all;

use work.pkg_msk_top_regs.all;

entity msk_top_regs_lowpass_ema_alpha is
  port (
    pi_clock        : in  std_logic;
    pi_reset        : in  std_logic;
    -- to/from adapter
    pi_decoder_rd_stb : in  std_logic;
    pi_decoder_wr_stb : in  std_logic;
    pi_decoder_data   : in  std_logic_vector(C_DATA_WIDTH-1 downto 0);
    po_decoder_data   : out std_logic_vector(C_DATA_WIDTH-1 downto 0);

    pi_reg  : in t_reg_lowpass_ema_alpha_in ;
    po_reg  : out t_reg_lowpass_ema_alpha_out
  );
end entity msk_top_regs_lowpass_ema_alpha;

architecture rtl of msk_top_regs_lowpass_ema_alpha is

  -- assign slices of data_out for each field, but force the rest to constant zeros
  function fun_set_data_out ( --
    field_reg_alpha : std_logic_vector(18-1 downto 0)) --
    return std_logic_vector is
    variable v_data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0);
  begin
    v_data_out := (others => '0');
    --
    v_data_out(17 downto 0) := field_reg_alpha; --
    return v_data_out;
  end function fun_set_data_out;

  signal data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0) := (others => '0');
   --
  signal field_reg_alpha : std_logic_vector(18-1 downto 0)
    := std_logic_vector(to_signed(0,18)); --
begin

  data_out <= fun_set_data_out( --
    field_reg_alpha --
  );

  -- resize field data out to the register bus width
  -- do only if 1 field and signed--
  po_decoder_data <= data_out; --
  ------------------------------------------------------------STORAGE
  alpha_storage: block
  begin
    prs_write : process(pi_clock)
    begin
      if rising_edge(pi_clock) then
        if pi_reset = '1' then
          field_reg_alpha <= std_logic_vector(to_signed(0,18));
        else
          -- HW --
          -- SW --
          if pi_decoder_wr_stb = '1' then
            field_reg_alpha <= pi_decoder_data(17 downto 0);
          end if;
        end if;
      end if;
    end process;
    --
    po_reg.alpha.data <= field_reg_alpha; --
  end block alpha_storage;
  ----------------------------------------------------------
end rtl;
-----------------------------------------------
-- register type: rx_power
-----------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

library desyrdl;
use desyrdl.common.all;

use work.pkg_msk_top_regs.all;

entity msk_top_regs_rx_power is
  port (
    pi_clock        : in  std_logic;
    pi_reset        : in  std_logic;
    -- to/from adapter
    pi_decoder_rd_stb : in  std_logic;
    pi_decoder_wr_stb : in  std_logic;
    pi_decoder_data   : in  std_logic_vector(C_DATA_WIDTH-1 downto 0);
    po_decoder_data   : out std_logic_vector(C_DATA_WIDTH-1 downto 0);

    pi_reg  : in t_reg_rx_power_in ;
    po_reg  : out t_reg_rx_power_out
  );
end entity msk_top_regs_rx_power;

architecture rtl of msk_top_regs_rx_power is

  -- assign slices of data_out for each field, but force the rest to constant zeros
  function fun_set_data_out ( --
    field_reg_rx_power : std_logic_vector(23-1 downto 0)) --
    return std_logic_vector is
    variable v_data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0);
  begin
    v_data_out := (others => '0');
    --
    v_data_out(22 downto 0) := field_reg_rx_power; --
    return v_data_out;
  end function fun_set_data_out;

  signal data_out : std_logic_vector(C_DATA_WIDTH-1 downto 0) := (others => '0');
   --
  signal field_reg_rx_power : std_logic_vector(23-1 downto 0)
    := std_logic_vector(to_signed(0,23)); --
begin

  data_out <= fun_set_data_out( --
    field_reg_rx_power --
  );

  -- resize field data out to the register bus width
  -- do only if 1 field and signed--
  po_decoder_data <= data_out; --
  ------------------------------------------------------------WIRE
  rx_power_wire : block --
  begin
    --
    field_reg_rx_power <= pi_reg.rx_power.data(23-1 downto 0); --
    --no signal to read by HW
    po_reg.rx_power.dummy <= '0'; --
  end block; --
end rtl;
-----------------------------------------------

--------------------------------------------------------------------------------
-- Register types in regfiles
--------------------------------------------------------------------------------
--