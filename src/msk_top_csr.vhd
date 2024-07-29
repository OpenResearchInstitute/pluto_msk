------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------
--  _______                             ________                                            ______
--  __  __ \________ _____ _______      ___  __ \_____ _____________ ______ ___________________  /_
--  _  / / /___  __ \_  _ \__  __ \     __  /_/ /_  _ \__  ___/_  _ \_  __ `/__  ___/_  ___/__  __ \
--  / /_/ / __  /_/ //  __/_  / / /     _  _, _/ /  __/_(__  ) /  __// /_/ / _  /    / /__  _  / / /
--  \____/  _  .___/ \___/ /_/ /_/      /_/ |_|  \___/ /____/  \___/ \__,_/  /_/     \___/  /_/ /_/
--          /_/
--                   ________                _____ _____ _____         _____
--                   ____  _/_______ __________  /____(_)__  /_____  ____  /______
--                    __  /  __  __ \__  ___/_  __/__  / _  __/_  / / /_  __/_  _ \
--                   __/ /   _  / / /_(__  ) / /_  _  /  / /_  / /_/ / / /_  /  __/
--                   /___/   /_/ /_/ /____/  \__/  /_/   \__/  \__,_/  \__/  \___/
--
------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------
-- Copyright
------------------------------------------------------------------------------------------------------
--
-- Copyright 2024 by M. Wishek <matthew@wishek.com>
--
------------------------------------------------------------------------------------------------------
-- License
------------------------------------------------------------------------------------------------------
--
-- This source describes Open Hardware and is licensed under the CERN-OHL-W v2.
--
-- You may redistribute and modify this source and make products using it under
-- the terms of the CERN-OHL-W v2 (https://ohwr.org/cern_ohl_w_v2.txt).
--
-- This source is distributed WITHOUT ANY EXPRESS OR IMPLIED WARRANTY, INCLUDING
-- OF MERCHANTABILITY, SATISFACTORY QUALITY AND FITNESS FOR A PARTICULAR PURPOSE.
-- Please see the CERN-OHL-W v2 for applicable conditions.
--
-- Source location: TBD
--
-- As per CERN-OHL-W v2 section 4.1, should You produce hardware based on this
-- source, You must maintain the Source Location visible on the external case of
-- the products you make using this source.
--
------------------------------------------------------------------------------------------------------
-- Block name and description
------------------------------------------------------------------------------------------------------
--
-- This is a wrapper block for the register module generated by DesyRDL.
--
-- Documentation location: TBD
--
------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------


------------------------------------------------------------------------------------------------------
-- ╦  ┬┌┐ ┬─┐┌─┐┬─┐┬┌─┐┌─┐
-- ║  │├┴┐├┬┘├─┤├┬┘│├┤ └─┐
-- ╩═╝┴└─┘┴└─┴ ┴┴└─┴└─┘└─┘
------------------------------------------------------------------------------------------------------
-- Libraries

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.numeric_std.ALL;

USE work.pkg_msk_top_regs.ALL;

------------------------------------------------------------------------------------------------------
-- ╔═╗┌┐┌┌┬┐┬┌┬┐┬ ┬
-- ║╣ │││ │ │ │ └┬┘
-- ╚═╝┘└┘ ┴ ┴ ┴  ┴ 
------------------------------------------------------------------------------------------------------
-- Entity

ENTITY msk_top_csr IS 
	GENERIC (
		HASH_ID_LO 			: std_logic_vector := X"AAAA5555";
		HASH_ID_HI 			: std_logic_vector := X"5555AAAA";
		GAIN_W 				: NATURAL := 16;
		NCO_W 				: NATURAL := 32;
		GENERATOR_W 		: NATURAL := 32;
		COUNTER_W 			: NATURAL := 32;
		C_S_AXI_DATA_WIDTH	: NATURAL := 32;
		C_S_AXI_ADDR_WIDTH	: NATURAL := 32
	);
	PORT (
		clk 			: IN  std_logic;

		s_axi_aclk		: in  std_logic;
		s_axi_aresetn	: in  std_logic;
		s_axi_awaddr	: in  std_logic_vector(C_S_AXI_ADDR_WIDTH-1 downto 0);
		s_axi_awvalid	: in  std_logic;
		s_axi_wdata		: in  std_logic_vector(C_S_AXI_DATA_WIDTH-1 downto 0);
		s_axi_wstrb		: in  std_logic_vector((C_S_AXI_DATA_WIDTH/8)-1 downto 0);
		s_axi_wvalid	: in  std_logic;
		s_axi_bready	: in  std_logic;
		s_axi_araddr	: in  std_logic_vector(C_S_AXI_ADDR_WIDTH-1 downto 0);
		s_axi_arvalid	: in  std_logic;
		s_axi_rready	: in  std_logic;
		s_axi_arready	: out std_logic;
		s_axi_rdata		: out std_logic_vector(C_S_AXI_DATA_WIDTH-1 downto 0);
		s_axi_rresp		: out std_logic_vector(1 downto 0);
		s_axi_rvalid	: out std_logic;
		s_axi_wready	: out std_logic;
		s_axi_bresp		: out std_logic_vector(1 downto 0);
		s_axi_bvalid	: out std_logic;
		s_axi_awready	: out std_logic;
		s_axi_awprot 	: in  std_logic_vector(2 DOWNTO 0);
		s_axi_arprot 	: in  std_logic_vector(2 DOWNTO 0);

		tx_enable 		: IN std_logic;
		rx_enable 		: IN std_logic;
		demod_sync_lock : IN std_logic;
		tx_req 			: IN std_logic;
		prbs_bits		: IN std_logic_vector(COUNTER_W -1 DOWNTO 0);
		prbs_errs		: IN std_logic_vector(COUNTER_W -1 DOWNTO 0);

		init 			: out std_logic;
		ptt 			: out std_logic;
		loopback_ena 	: out std_logic;
		rx_invert 		: out std_logic;
		clear_counts 	: out std_logic;
		freq_word_ft	: out std_logic_vector(NCO_W -1 DOWNTO 0);
		freq_word_f1	: out std_logic_vector(NCO_W -1 DOWNTO 0);
		freq_word_f2	: out std_logic_vector(NCO_W -1 DOWNTO 0);
		lpf_freeze 		: out std_logic;
		lpf_zero 		: out std_logic;
		lpf_alpha 		: out std_logic_vector(GAIN_W -1 DOWNTO 0);
		lpf_i_gain 		: out std_logic_vector(GAIN_W -1 DOWNTO 0);
		lpf_p_gain 		: out std_logic_vector(GAIN_W -1 DOWNTO 0);
		tx_data_w 		: out std_logic_vector(7 DOWNTO 0);
		rx_data_w 		: out std_logic_vector(7 DOWNTO 0);
		prbs_initial	: out std_logic_vector(GENERATOR_W -1 DOWNTO 0);
		prbs_poly		: out std_logic_vector(GENERATOR_W -1 DOWNTO 0);
		prbs_err_mask 	: out std_logic_vector(GENERATOR_W -1 DOWNTO 0);
		prbs_err_insert : out std_logic;
		prbs_sel 		: out std_logic;
		prbs_clear 		: out std_logic;
		prbs_sync 		: out std_logic

	);
END ENTITY msk_top_csr;

ARCHITECTURE rtl OF msk_top_csr IS 

	SIGNAL pi_s_top 		: t_msk_top_regs_m2s;
	SIGNAL po_s_top 		: t_msk_top_regs_s2m;

	SIGNAL pi_addrmap 		: t_addrmap_msk_top_regs_in;
	SIGNAL po_addrmap 		: t_addrmap_msk_top_regs_out;

BEGIN

	u_msk_regs : ENTITY work.msk_top_regs(arch)
	PORT MAP (
    	pi_clock 	=> s_axi_aclk,
    	pi_reset 	=> NOT s_axi_aresetn,
    	-- TOP subordinate memory mapped interface
    	pi_s_reset  => NOT s_axi_aresetn,
    	pi_s_top   	=> pi_s_top,
    	po_s_top    => po_s_top,
    	-- to logic interface
    	pi_addrmap  => pi_addrmap,
    	po_addrmap  => po_addrmap 
  	);

    -- write address channel signals---------------------------------------------
  	pi_s_top.awaddr 	<= s_axi_awaddr;
    pi_s_top.awprot		<= s_axi_awprot;
    pi_s_top.awvalid	<= s_axi_awvalid;
    -- write data channel signals---------------------------------------------
    pi_s_top.wdata      <= s_axi_wdata;
    pi_s_top.wstrb      <= s_axi_wstrb;
    pi_s_top.wvalid     <= s_axi_wvalid;
    -- write response channel signals
    pi_s_top.bready     <= s_axi_bready;
    -- read address channel signals ---------------------------------------------
    pi_s_top.araddr     <= s_axi_araddr;
    pi_s_top.arprot     <= s_axi_arprot;
    pi_s_top.arvalid    <= s_axi_arvalid;
    -- read data channel signals---------------------------------------------
    pi_s_top.rready     <= s_axi_rready;

    -- write address channel signals---------------------------------------------
    s_axi_awready 		<= po_s_top.awready;
    -- write data channel signals---------------------------------------------
    s_axi_wready 		<= po_s_top.wready;
    -- write response channel signals ---------------------------------------------
    s_axi_bresp		<= po_s_top.bresp;
    s_axi_bvalid 		<= po_s_top.bvalid;
    -- read address channel signals---------------------------------------------
    s_axi_arready 		<= po_s_top.arready;
    -- read data channel signals---------------------------------------------
    s_axi_rdata 		<= po_s_top.rdata;
    s_axi_rresp 		<= po_s_top.rresp;
    s_axi_rvalid 		<= po_s_top.rvalid;

    pi_addrmap.MSK_Status.demod_sync_lock.data(0) <= '0';
    pi_addrmap.MSK_Status.tx_enable.data(0) <= tx_enable;
    pi_addrmap.MSK_Status.rx_enable.data(0) <= rx_enable;
    pi_addrmap.Tx_Bit_Count.tx_bit_cntr.incr <= tx_req;
    pi_addrmap.Tx_Enable_Count.tx_ena_cntr.incr <= tx_enable;
    pi_addrmap.Tx_Enable_Count.tx_ena_cntr.decr <= NOT tx_enable;
    pi_addrmap.PRBS_Bit_Count.status_data.data <= prbs_bits;
    pi_addrmap.PRBS_Error_Count.status_data.data <= NOT prbs_errs;

    init 			<= po_addrmap.MSK_Init.init.data(0);
    ptt 			<= po_addrmap.MSK_Control.ptt_desc_209a923a.data(0);
    loopback_ena 	<= po_addrmap.MSK_Control.loopback_ena_desc_6617b8f3.data(0);
    rx_invert 		<= po_addrmap.MSK_Control.rx_invert_desc_643ee034.data(0);
    clear_counts 	<= po_addrmap.MSK_Control.clear_counts_desc_52baf732.data(0);
    freq_word_ft	<= po_addrmap.Fb_FreqWord.config_data.data;
    freq_word_f1	<= po_addrmap.F1_FreqWord.config_data.data;
    freq_word_f2	<= po_addrmap.F2_FreqWord.config_data.data;
    lpf_freeze 		<= po_addrmap.LPF_Config_0.lpf_freeze.data(0);
    lpf_zero 		<= po_addrmap.LPF_Config_0.lpf_zero.data(0);
    lpf_alpha 		<= po_addrmap.LPF_Config_0.lpf_alpha.data;
    lpf_i_gain 		<= po_addrmap.LPF_Config_1.i_gain.data;
    lpf_p_gain 		<= po_addrmap.LPF_Config_1.p_gain.data;
    tx_data_w 		<= po_addrmap.Tx_Data_Width.data_width.data;
    rx_data_w 		<= po_addrmap.Rx_Data_Width.data_width.data;

	prbs_initial	<= po_addrmap.PRBS_Initial_State.config_data.data;
	prbs_poly		<= po_addrmap.PRBS_Polynomial.config_data.data;
	prbs_err_mask 	<= po_addrmap.PRBS_Error_Mask.config_data.data;
	prbs_err_insert <= po_addrmap.PRBS_Control.prbs_error_insert.data(0);
	prbs_sel 		<= po_addrmap.PRBS_Control.prbs_sel.data(0);
	prbs_clear 		<= po_addrmap.PRBS_Control.prbs_clear.data(0);
	prbs_sync 		<= po_addrmap.PRBS_Control.prbs_sync.data(0);

END ARCHITECTURE rtl;
