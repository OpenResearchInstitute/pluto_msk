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
-- CSR wrapper for PeakRDL-generated register block.
--
-- An internal AXI4-Lite CDC bridge crosses from the PS AXI clock (s_axi_aclk)
-- to the modem clock (clk). The register block and all modem-facing signals
-- run in the modem clock domain, eliminating per-signal CDC primitives.
--
------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------


------------------------------------------------------------------------------------------------------
-- Libraries
------------------------------------------------------------------------------------------------------

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.numeric_std.ALL;

USE work.axi4lite_intf_pkg.ALL;
USE work.msk_top_regs_pkg.ALL;

------------------------------------------------------------------------------------------------------
-- Entity
------------------------------------------------------------------------------------------------------

ENTITY msk_top_csr IS
	GENERIC (
		HASH_ID_LO 			: std_logic_vector := X"AAAA5555";
		HASH_ID_HI 			: std_logic_vector := X"5555AAAA";
		GAIN_W 				: NATURAL := 24;
		SHIFT_W 			: NATURAL := 8;
		NCO_W 				: NATURAL := 32;
		ACC_W 				: NATURAL := 32;
		GENERATOR_W 		: NATURAL := 32;
		COUNTER_W 			: NATURAL := 32;
		SYNC_W 				: NATURAL := 16;
		C_S_AXI_DATA_WIDTH	: NATURAL := 32;
		C_S_AXI_ADDR_WIDTH	: NATURAL := 32;
		SYNC_CNT_W 			: NATURAL := 24;
		FIFO_ADDR_WIDTH 	: NATURAL := 9
	);
	PORT (
		clk 				: IN  std_logic;

		s_axi_aclk			: in  std_logic;
		s_axi_aresetn		: in  std_logic;
		s_axi_awaddr		: in  std_logic_vector(C_S_AXI_ADDR_WIDTH-1 downto 0);
		s_axi_awvalid		: in  std_logic;
		s_axi_wdata			: in  std_logic_vector(C_S_AXI_DATA_WIDTH-1 downto 0);
		s_axi_wstrb			: in  std_logic_vector((C_S_AXI_DATA_WIDTH/8)-1 downto 0);
		s_axi_wvalid		: in  std_logic;
		s_axi_bready		: in  std_logic;
		s_axi_araddr		: in  std_logic_vector(C_S_AXI_ADDR_WIDTH-1 downto 0);
		s_axi_arvalid		: in  std_logic;
		s_axi_rready		: in  std_logic;
		s_axi_arready		: out std_logic;
		s_axi_rdata			: out std_logic_vector(C_S_AXI_DATA_WIDTH-1 downto 0);
		s_axi_rresp			: out std_logic_vector(1 downto 0);
		s_axi_rvalid		: out std_logic;
		s_axi_wready		: out std_logic;
		s_axi_bresp			: out std_logic_vector(1 downto 0);
		s_axi_bvalid		: out std_logic;
		s_axi_awready		: out std_logic;
		s_axi_awprot 		: in  std_logic_vector(2 DOWNTO 0);
		s_axi_arprot 		: in  std_logic_vector(2 DOWNTO 0);

		tx_enable 			: IN std_logic;
		rx_enable 			: IN std_logic;
		demod_sync_lock 	: IN std_logic;
		tx_req 				: IN std_logic;
		tx_axis_valid 		: IN std_logic;
		xfer_count 			: IN std_logic_vector(COUNTER_W -1 DOWNTO 0);
		tx_bit_counter 		: IN std_logic_vector(COUNTER_W -1 DOWNTO 0);
		tx_ena_counter 		: IN std_logic_vector(COUNTER_W -1 DOWNTO 0);
		prbs_bits			: IN std_logic_vector(COUNTER_W -1 DOWNTO 0);
		prbs_errs			: IN std_logic_vector(COUNTER_W -1 DOWNTO 0);
		lpf_accum_f1 		: IN std_logic_vector(ACC_W -1 DOWNTO 0);
		lpf_accum_f2 		: IN std_logic_vector(ACC_W -1 DOWNTO 0);
		f1_nco_adjust		: IN std_logic_vector(31 DOWNTO 0);
		f2_nco_adjust		: IN std_logic_vector(31 DOWNTO 0);
		f1_error			: IN std_logic_vector(31 DOWNTO 0);
		f2_error			: IN std_logic_vector(31 DOWNTO 0);
		pd_power			: IN std_logic_vector(22 DOWNTO 0);
		rx_frame_sync 		: IN std_logic;
		rx_frame_buffer_ovf : IN std_logic;
		rx_frame_count 		: IN std_logic_vector(23 DOWNTO 0);
		rx_frame_sync_err   : IN std_logic_vector( 5 DOWNTO 0);

		tx_async_fifo_wr_ptr		: IN  std_logic_vector(FIFO_ADDR_WIDTH DOWNTO 0);
		tx_async_fifo_rd_ptr 		: IN  std_logic_vector(FIFO_ADDR_WIDTH DOWNTO 0);
		tx_async_fifo_status_req 	: OUT std_logic;
		tx_async_fifo_status_ack 	: IN  std_logic;
		rx_async_fifo_wr_ptr		: IN  std_logic_vector(FIFO_ADDR_WIDTH DOWNTO 0);
		rx_async_fifo_rd_ptr 		: IN  std_logic_vector(FIFO_ADDR_WIDTH DOWNTO 0);
		rx_async_fifo_status_req 	: OUT std_logic;
		rx_async_fifo_status_ack 	: IN  std_logic;

		txinit 				: out std_logic;
		rxinit 				: out std_logic;
		ptt 				: out std_logic;
		loopback_ena 		: out std_logic;
		diff_encdec_lbk_ena : out std_logic;
		rx_invert 			: out std_logic;
		clear_counts 		: out std_logic;
		discard_rxsamples 	: out std_logic_vector(7 DOWNTO 0);
		discard_rxnco 		: out std_logic_vector(7 DOWNTO 0);
		freq_word_ft		: out std_logic_vector(NCO_W -1 DOWNTO 0);
		freq_word_tx_f1		: out std_logic_vector(NCO_W -1 DOWNTO 0);
		freq_word_tx_f2		: out std_logic_vector(NCO_W -1 DOWNTO 0);
		freq_word_rx_f1		: out std_logic_vector(NCO_W -1 DOWNTO 0);
		freq_word_rx_f2		: out std_logic_vector(NCO_W -1 DOWNTO 0);
		lpf_freeze 			: out std_logic;
		lpf_zero 			: out std_logic;
		lpf_alpha 			: out std_logic_vector(GAIN_W -1 DOWNTO 0);
		lpf_i_gain 			: out std_logic_vector(GAIN_W -1 DOWNTO 0);
		lpf_p_gain 			: out std_logic_vector(GAIN_W -1 DOWNTO 0);
		lpf_i_shift			: out std_logic_vector(SHIFT_W -1 DOWNTO 0);
		lpf_p_shift			: out std_logic_vector(SHIFT_W -1 DOWNTO 0);
		tx_data_w 			: out std_logic_vector(7 DOWNTO 0);
		rx_data_w 			: out std_logic_vector(7 DOWNTO 0);
		prbs_initial		: out std_logic_vector(GENERATOR_W -1 DOWNTO 0);
		prbs_poly			: out std_logic_vector(GENERATOR_W -1 DOWNTO 0);
		prbs_err_mask 		: out std_logic_vector(GENERATOR_W -1 DOWNTO 0);
		prbs_err_insert 	: out std_logic;
		prbs_sel 			: out std_logic;
		prbs_clear 			: out std_logic;
		prbs_manual_sync	: out std_logic;
		prbs_sync_threshold : out std_logic_vector(SYNC_W -1 DOWNTO 0);
		tx_sync_ena 		: out std_logic;
		tx_sync_cnt 		: out std_logic_vector(SYNC_CNT_W -1 DOWNTO 0);
		tx_sync_force		: out std_logic;
		tx_sync_f1			: out std_logic;
		tx_sync_f2			: out std_logic;
		pd_alpha1			: out std_logic_vector(17 DOWNTO 0);
		pd_alpha2			: out std_logic_vector(17 DOWNTO 0);

                -- Debug signals for TX path
                tx_debug_encoder_tvalid  : IN std_logic;
                tx_debug_encoder_tready  : IN std_logic;
                tx_debug_fifo_tvalid     : IN std_logic;
                tx_debug_fifo_tready     : IN std_logic;
                tx_debug_tx_req          : IN std_logic;
                tx_debug_encoder_tlast   : IN std_logic;
                tx_debug_encoder_state   : IN std_logic_vector(2 DOWNTO 0);

                -- Debug signals for RX path
                rx_debug_decoder_state   : IN std_logic_vector(3 DOWNTO 0);
                rx_debug_viterbi_start   : IN std_logic;
                rx_debug_viterbi_busy    : IN std_logic;
                rx_debug_viterbi_done    : IN std_logic;
                rx_debug_decoder_tvalid  : IN std_logic;
                rx_debug_decoder_tready  : IN std_logic;

        symbol_lock_count		: OUT std_logic_vector(9 DOWNTO 0);
        symbol_lock_threshold	: OUT std_logic_vector(15 DOWNTO 0);

        cst_lock_f1 			: IN  std_logic;
        cst_lock_f2				: IN  std_logic;
        cst_lock_time_f1  		: IN  std_logic_vector(15 DOWNTO 0);
        cst_lock_time_f2  		: IN  std_logic_vector(15 DOWNTO 0);
        cst_unlock_f1 			: IN  std_logic;
        cst_unlock_f2 			: IN  std_logic

	);
END ENTITY msk_top_csr;

ARCHITECTURE rtl OF msk_top_csr IS

	-- Bridge master-side AXI signals (modem clock domain)
	SIGNAL m_axi_awaddr   : std_logic_vector(C_S_AXI_ADDR_WIDTH-1 DOWNTO 0);
	SIGNAL m_axi_awprot   : std_logic_vector(2 DOWNTO 0);
	SIGNAL m_axi_awvalid  : std_logic;
	SIGNAL m_axi_awready  : std_logic;
	SIGNAL m_axi_wdata    : std_logic_vector(C_S_AXI_DATA_WIDTH-1 DOWNTO 0);
	SIGNAL m_axi_wstrb    : std_logic_vector(C_S_AXI_DATA_WIDTH/8-1 DOWNTO 0);
	SIGNAL m_axi_wvalid   : std_logic;
	SIGNAL m_axi_wready   : std_logic;
	SIGNAL m_axi_bresp    : std_logic_vector(1 DOWNTO 0);
	SIGNAL m_axi_bvalid   : std_logic;
	SIGNAL m_axi_bready   : std_logic;
	SIGNAL m_axi_araddr   : std_logic_vector(C_S_AXI_ADDR_WIDTH-1 DOWNTO 0);
	SIGNAL m_axi_arprot   : std_logic_vector(2 DOWNTO 0);
	SIGNAL m_axi_arvalid  : std_logic;
	SIGNAL m_axi_arready  : std_logic;
	SIGNAL m_axi_rdata    : std_logic_vector(C_S_AXI_DATA_WIDTH-1 DOWNTO 0);
	SIGNAL m_axi_rresp    : std_logic_vector(1 DOWNTO 0);
	SIGNAL m_axi_rvalid   : std_logic;
	SIGNAL m_axi_rready   : std_logic;
	SIGNAL m_axi_aresetn  : std_logic;

	-- Register block interface (modem clock domain)
	SIGNAL s_axil_i 		: axi4lite_slave_in_intf(
            AWADDR(7 downto 0),
            WDATA(31 downto 0),
            WSTRB(3 downto 0),
            ARADDR(7 downto 0)
        );
	SIGNAL s_axil_o 		: axi4lite_slave_out_intf(
            RDATA(31 downto 0)
     	);

	SIGNAL hwif_in 			: msk_top_regs_in_t;
	SIGNAL hwif_out 		: msk_top_regs_out_t;

	SIGNAL txrxinit 		: std_logic;

	-- Reset in active-high form for data_capture
	SIGNAL csr_init 		: std_logic;

	COMPONENT data_capture IS
		GENERIC (
			data_width 	: natural := 32
		);
		PORT (
			clk			: IN  std_logic;
			sync_reset	: IN  std_logic;

			capture 	: IN  std_logic;

			di 			: IN  std_logic_vector(data_width -1 DOWNTO 0);
			do 			: OUT std_logic_vector(data_width -1 DOWNTO 0)
		);
	END COMPONENT data_capture;

BEGIN

	csr_init <= NOT m_axi_aresetn;

	----------------------------------------------------------------------
	-- AXI4-Lite CDC Bridge: s_axi_aclk -> clk (modem clock)
	----------------------------------------------------------------------
	u_axi_cdc : ENTITY work.axi_lite_cdc
	GENERIC MAP (
		ADDR_WIDTH => C_S_AXI_ADDR_WIDTH,
		DATA_WIDTH => C_S_AXI_DATA_WIDTH
	)
	PORT MAP (
		-- Slave side (PS AXI clock)
		s_axi_aclk    => s_axi_aclk,
		s_axi_aresetn => s_axi_aresetn,
		s_axi_awaddr  => s_axi_awaddr,
		s_axi_awprot  => s_axi_awprot,
		s_axi_awvalid => s_axi_awvalid,
		s_axi_awready => s_axi_awready,
		s_axi_wdata   => s_axi_wdata,
		s_axi_wstrb   => s_axi_wstrb,
		s_axi_wvalid  => s_axi_wvalid,
		s_axi_wready  => s_axi_wready,
		s_axi_bresp   => s_axi_bresp,
		s_axi_bvalid  => s_axi_bvalid,
		s_axi_bready  => s_axi_bready,
		s_axi_araddr  => s_axi_araddr,
		s_axi_arprot  => s_axi_arprot,
		s_axi_arvalid => s_axi_arvalid,
		s_axi_arready => s_axi_arready,
		s_axi_rdata   => s_axi_rdata,
		s_axi_rresp   => s_axi_rresp,
		s_axi_rvalid  => s_axi_rvalid,
		s_axi_rready  => s_axi_rready,
		-- Master side (modem clock)
		m_axi_aclk    => clk,
		m_axi_aresetn => m_axi_aresetn,
		m_axi_awaddr  => m_axi_awaddr,
		m_axi_awprot  => m_axi_awprot,
		m_axi_awvalid => m_axi_awvalid,
		m_axi_awready => m_axi_awready,
		m_axi_wdata   => m_axi_wdata,
		m_axi_wstrb   => m_axi_wstrb,
		m_axi_wvalid  => m_axi_wvalid,
		m_axi_wready  => m_axi_wready,
		m_axi_bresp   => m_axi_bresp,
		m_axi_bvalid  => m_axi_bvalid,
		m_axi_bready  => m_axi_bready,
		m_axi_araddr  => m_axi_araddr,
		m_axi_arprot  => m_axi_arprot,
		m_axi_arvalid => m_axi_arvalid,
		m_axi_arready => m_axi_arready,
		m_axi_rdata   => m_axi_rdata,
		m_axi_rresp   => m_axi_rresp,
		m_axi_rvalid  => m_axi_rvalid,
		m_axi_rready  => m_axi_rready
	);

	----------------------------------------------------------------------
	-- Wire bridge master-side AXI to register block input record
	----------------------------------------------------------------------
	s_axil_i.AWVALID 	<= m_axi_awvalid;
	s_axil_i.AWADDR 	<= m_axi_awaddr(7 DOWNTO 0);
	s_axil_i.AWPROT  	<= m_axi_awprot;
	s_axil_i.WVALID  	<= m_axi_wvalid;
	s_axil_i.WDATA   	<= m_axi_wdata;
	s_axil_i.WSTRB 		<= m_axi_wstrb;
	s_axil_i.BREADY 	<= m_axi_bready;
	s_axil_i.ARVALID 	<= m_axi_arvalid;
	s_axil_i.ARADDR  	<= m_axi_araddr(7 DOWNTO 0);
	s_axil_i.ARPROT 	<= m_axi_arprot;
	s_axil_i.RREADY  	<= m_axi_rready;

	m_axi_awready		<= s_axil_o.AWREADY;
	m_axi_wready		<= s_axil_o.WREADY;
	m_axi_bvalid		<= s_axil_o.BVALID;
	m_axi_bresp			<= s_axil_o.BRESP;
	m_axi_arready		<= s_axil_o.ARREADY;
	m_axi_rvalid		<= s_axil_o.RVALID;
	m_axi_rdata			<= s_axil_o.RDATA;
	m_axi_rresp			<= s_axil_o.RRESP;

	----------------------------------------------------------------------
	-- Register block — now clocked by modem clock (clk)
	----------------------------------------------------------------------
	u_msk_regs : ENTITY work.msk_top_regs(rtl)
	PORT MAP (
    	clk 		=> clk,
    	rst 		=> csr_init,
    	s_axil_i  	=> s_axil_i,
    	s_axil_o 	=> s_axil_o,
    	hwif_in  	=> hwif_in,
    	hwif_out	=> hwif_out
  	);

    ----------------------------------------------------------------------
    -- Hash ID generics — driven from VHDL generics
    ----------------------------------------------------------------------
    hwif_in.Hash_ID_Low.hash_id_lo.next_q   <= HASH_ID_LO;
    hwif_in.Hash_ID_High.hash_id_hi.next_q  <= HASH_ID_HI;

    ----------------------------------------------------------------------
    -- Status inputs — direct connection (same clock domain)
    ----------------------------------------------------------------------
    hwif_in.MSK_Status.demod_sync_lock.next_q	<= '0';
    hwif_in.MSK_Status.tx_enable.next_q			<= tx_enable;
    hwif_in.MSK_Status.rx_enable.next_q			<= rx_enable;
    hwif_in.MSK_Status.tx_axis_valid.next_q		<= tx_axis_valid;
    hwif_in.rx_frame_sync_status.frame_sync_locked.next_q    <= rx_frame_sync;
    hwif_in.rx_frame_sync_status.frame_buffer_overflow.we    <= rx_frame_buffer_ovf;

    ----------------------------------------------------------------------
    -- Status capture (counters — snapshot on read via swmod)
    -- data_capture latches the value when swmod fires; we delay one cycle for we
    ----------------------------------------------------------------------
    utbc_c : data_capture PORT MAP (clk, csr_init, hwif_out.Tx_Bit_Count.data.swmod,        tx_bit_counter,    hwif_in.Tx_Bit_Count.data.next_q    );
    utbe_c : data_capture PORT MAP (clk, csr_init, hwif_out.Tx_Enable_Count.data.swmod,     tx_ena_counter,    hwif_in.Tx_Enable_Count.data.next_q );
    utatc_c: data_capture PORT MAP (clk, csr_init, hwif_out.axis_xfer_count.data.swmod,     xfer_count,        hwif_in.axis_xfer_count.data.next_q );
    utf1e_c: data_capture PORT MAP (clk, csr_init, hwif_out.f1_error.data.swmod,            f1_error,          hwif_in.f1_error.data.next_q        );
    utf2e_c: data_capture PORT MAP (clk, csr_init, hwif_out.f2_error.data.swmod,            f2_error,          hwif_in.f2_error.data.next_q        );
    utf1a_c: data_capture PORT MAP (clk, csr_init, hwif_out.f1_nco_adjust.data.swmod,       f1_nco_adjust,     hwif_in.f1_nco_adjust.data.next_q   );
    utf2a_c: data_capture PORT MAP (clk, csr_init, hwif_out.f2_nco_adjust.data.swmod,       f2_nco_adjust,     hwif_in.f2_nco_adjust.data.next_q   );
    utprb_c: data_capture PORT MAP (clk, csr_init, hwif_out.PRBS_Bit_Count.data.swmod,      prbs_bits,         hwif_in.PRBS_Bit_Count.data.next_q  );
    utpre_c: data_capture PORT MAP (clk, csr_init, hwif_out.PRBS_Error_Count.data.swmod,    prbs_errs,         hwif_in.PRBS_Error_Count.data.next_q);
    utlp1_c: data_capture PORT MAP (clk, csr_init, hwif_out.LPF_Accum_F1.data.swmod,        lpf_accum_f1,      hwif_in.LPF_Accum_F1.data.next_q   );
    utlp2_c: data_capture PORT MAP (clk, csr_init, hwif_out.LPF_Accum_F2.data.swmod,        lpf_accum_f2,      hwif_in.LPF_Accum_F2.data.next_q   );
    utpwr_c: data_capture GENERIC MAP (23)
    					  PORT MAP (clk, csr_init, hwif_out.rx_power.data.swmod,             pd_power,          hwif_in.rx_power.data.next_q        );
    utfsc_c: data_capture GENERIC MAP (24)
    					  PORT MAP (clk, csr_init, hwif_out.rx_frame_sync_status.frames_received.swmod,    rx_frame_count,    hwif_in.rx_frame_sync_status.frames_received.next_q    );
    utfse_c: data_capture GENERIC MAP (6)
    					  PORT MAP (clk, csr_init, hwif_out.rx_frame_sync_status.frame_sync_errors.swmod,  rx_frame_sync_err, hwif_in.rx_frame_sync_status.frame_sync_errors.next_q  );

    -- we pulse delayed one cycle so captured data is stable when loaded
    we_delay_proc : PROCESS (clk)
    BEGIN
        IF rising_edge(clk) THEN
            IF csr_init = '1' THEN
                hwif_in.Tx_Bit_Count.data.we       <= '0';
                hwif_in.Tx_Enable_Count.data.we     <= '0';
                hwif_in.axis_xfer_count.data.we     <= '0';
                hwif_in.f1_error.data.we             <= '0';
                hwif_in.f2_error.data.we             <= '0';
                hwif_in.f1_nco_adjust.data.we        <= '0';
                hwif_in.f2_nco_adjust.data.we        <= '0';
                hwif_in.PRBS_Bit_Count.data.we       <= '0';
                hwif_in.PRBS_Error_Count.data.we     <= '0';
                hwif_in.LPF_Accum_F1.data.we         <= '0';
                hwif_in.LPF_Accum_F2.data.we         <= '0';
                hwif_in.rx_power.data.we             <= '0';
                hwif_in.rx_frame_sync_status.frames_received.we  <= '0';
                hwif_in.rx_frame_sync_status.frame_sync_errors.we <= '0';
            ELSE
                hwif_in.Tx_Bit_Count.data.we       <= hwif_out.Tx_Bit_Count.data.swmod;
                hwif_in.Tx_Enable_Count.data.we     <= hwif_out.Tx_Enable_Count.data.swmod;
                hwif_in.axis_xfer_count.data.we     <= hwif_out.axis_xfer_count.data.swmod;
                hwif_in.f1_error.data.we             <= hwif_out.f1_error.data.swmod;
                hwif_in.f2_error.data.we             <= hwif_out.f2_error.data.swmod;
                hwif_in.f1_nco_adjust.data.we        <= hwif_out.f1_nco_adjust.data.swmod;
                hwif_in.f2_nco_adjust.data.we        <= hwif_out.f2_nco_adjust.data.swmod;
                hwif_in.PRBS_Bit_Count.data.we       <= hwif_out.PRBS_Bit_Count.data.swmod;
                hwif_in.PRBS_Error_Count.data.we     <= hwif_out.PRBS_Error_Count.data.swmod;
                hwif_in.LPF_Accum_F1.data.we         <= hwif_out.LPF_Accum_F1.data.swmod;
                hwif_in.LPF_Accum_F2.data.we         <= hwif_out.LPF_Accum_F2.data.swmod;
                hwif_in.rx_power.data.we             <= hwif_out.rx_power.data.swmod;
                hwif_in.rx_frame_sync_status.frames_received.we  <= hwif_out.rx_frame_sync_status.frames_received.swmod;
                hwif_in.rx_frame_sync_status.frame_sync_errors.we <= hwif_out.rx_frame_sync_status.frame_sync_errors.swmod;
            END IF;
        END IF;
    END PROCESS we_delay_proc;

    ----------------------------------------------------------------------
    -- FIFO status reads (same clock domain now)
    ----------------------------------------------------------------------
	rx_async_fifo_status_req <= hwif_out.rx_async_fifo_rd_wr_ptr.data.swmod;
	hwif_in.rx_async_fifo_rd_wr_ptr.data.we	<= rx_async_fifo_status_ack;

	-- Lock status

    usls1_a: pulse_detect PORT MAP (s_axi_aclk, NOT s_axi_aresetn, cst_unlock_f1, hwif_in.symbol_lock_status.unlock_f1.we);
    usls2_a: pulse_detect PORT MAP (s_axi_aclk, NOT s_axi_aresetn, cst_unlock_f2, hwif_in.symbol_lock_status.unlock_f2.we);
	hwif_in.symbol_lock_status.f1f2.next_q 		<= cst_lock_f1 AND cst_lock_f2;
	hwif_in.symbol_lock_status.f1.next_q 		<= cst_lock_f1;
	hwif_in.symbol_lock_status.f2.next_q 		<= cst_lock_f2;
	hwif_in.symbol_lock_status.unlock_f1.next_q	<= '1';
	hwif_in.symbol_lock_status.unlock_f2.next_q	<= '1';
	hwif_in.symbol_lock_time.f1.next_q			<= cst_lock_time_f1;
	hwif_in.symbol_lock_time.f2.next_q			<= cst_lock_time_f2;

    -- commented out by Abraxas3d to add more bits to the register to investigate receive failures
    --hwif_in.rx_async_fifo_rd_wr_ptr.data.next_q <= std_logic_vector(resize(unsigned(rx_async_fifo_wr_ptr), 16) & resize(unsigned(rx_async_fifo_rd_ptr), 16));

-- Experimental RX debug register setup (matching TX debug pattern)
-- Bit layout:
--   [31:28] decoder state (4 bits)
--   [27]    viterbi_start
--   [26]    viterbi_busy
--   [25]    viterbi_done
--   [24]    decoder_tvalid
--   [23]    decoder_tready
--   [22:13] rx_fifo_wr_ptr (10 bits)
--   [12:10] spare
--   [9:0]   rx_fifo_rd_ptr (10 bits)
hwif_in.rx_async_fifo_rd_wr_ptr.data.next_q <=
    rx_debug_decoder_state &            -- bits 31:28 (4 bits)
    rx_debug_viterbi_start &            -- bit 27
    rx_debug_viterbi_busy &             -- bit 26
    rx_debug_viterbi_done &             -- bit 25
    rx_debug_decoder_tvalid &           -- bit 24
    rx_debug_decoder_tready &           -- bit 23
    std_logic_vector(resize(unsigned(rx_async_fifo_wr_ptr), 10)) &  -- bits 22:13
    "000" &                             -- bits 12:10 spare
    std_logic_vector(resize(unsigned(rx_async_fifo_rd_ptr), 10));   -- bits 9:0

	tx_async_fifo_status_req <= hwif_out.tx_async_fifo_rd_wr_ptr.data.swmod;
	hwif_in.tx_async_fifo_rd_wr_ptr.data.we	<= tx_async_fifo_status_ack;

-- experimental register setup by Abraxas3d
hwif_in.tx_async_fifo_rd_wr_ptr.data.next_q <=
    tx_debug_encoder_tvalid &   -- bit 31
    tx_debug_encoder_tready &   -- bit 30
    tx_debug_fifo_tvalid &      -- bit 29
    tx_debug_fifo_tready &      -- bit 28
    tx_debug_tx_req &           -- bit 27
    tx_debug_encoder_tlast &    -- bit 26
    tx_debug_encoder_state &    -- bits 25:23
    std_logic_vector(resize(unsigned(tx_async_fifo_wr_ptr), 10)) &  -- bits 22:13
    "000" &                     -- bits 12:10 spare
    std_logic_vector(resize(unsigned(tx_async_fifo_rd_ptr), 10));   -- bits 9:0

    ----------------------------------------------------------------------
    -- Control outputs — direct connection (same clock domain)
    ----------------------------------------------------------------------
    txrxinit            <= hwif_out.MSK_Init.txrxinit.value;
    txinit              <= hwif_out.MSK_Init.txinit.value OR txrxinit;
    rxinit              <= hwif_out.MSK_Init.rxinit.value OR txrxinit;
    ptt                 <= hwif_out.MSK_Control.ptt.value;
    loopback_ena        <= hwif_out.MSK_Control.loopback_ena.value;
    diff_encdec_lbk_ena <= hwif_out.MSK_Control.diff_encoder_loopback.value;
    rx_invert           <= hwif_out.MSK_Control.rx_invert.value;
    clear_counts        <= hwif_out.MSK_Control.clear_counts.value;
    lpf_freeze          <= hwif_out.LPF_Config_0.lpf_freeze.value;
    lpf_zero            <= hwif_out.LPF_Config_0.lpf_zero.value;
    prbs_sel            <= hwif_out.PRBS_Control.prbs_sel.value;
    prbs_clear          <= hwif_out.PRBS_Control.prbs_clear.value;
    prbs_err_insert     <= hwif_out.PRBS_Control.prbs_error_insert.value;
    prbs_manual_sync    <= hwif_out.PRBS_Control.prbs_manual_sync.value;
    tx_sync_ena         <= hwif_out.Tx_Sync_Ctrl.tx_sync_ena.value;
    tx_sync_force       <= hwif_out.Tx_Sync_Ctrl.tx_sync_force.value;

    -- Static config signals (same clock domain — no CDC needed)
    freq_word_ft		<= hwif_out.Fb_FreqWord.config_data.value;
    freq_word_tx_f1		<= hwif_out.TX_F1_FreqWord.config_data.value;
    freq_word_tx_f2		<= hwif_out.TX_F2_FreqWord.config_data.value;
    freq_word_rx_f1		<= hwif_out.RX_F1_FreqWord.config_data.value;
    freq_word_rx_f2		<= hwif_out.RX_F2_FreqWord.config_data.value;

    lpf_alpha 			<= hwif_out.LPF_Config_0.lpf_alpha.value;
    lpf_i_gain 			<= hwif_out.LPF_Config_1.i_gain.value;
    lpf_i_shift 		<= hwif_out.LPF_Config_1.i_shift.value;
    lpf_p_gain 			<= hwif_out.LPF_Config_2.p_gain.value;
    lpf_p_shift 		<= hwif_out.LPF_Config_2.p_shift.value;

    tx_data_w 			<= hwif_out.Tx_Data_Width.data_width.value;
    rx_data_w 			<= hwif_out.Rx_Data_Width.data_width.value;
    discard_rxsamples 	<= hwif_out.Rx_Sample_Discard.rx_sample_discard.value;
    discard_rxnco  		<= hwif_out.Rx_Sample_Discard.rx_nco_discard.value;

	prbs_initial		<= hwif_out.PRBS_Initial_State.config_data.value;
	prbs_poly			<= hwif_out.PRBS_Polynomial.config_data.value;
	prbs_err_mask 		<= hwif_out.PRBS_Error_Mask.config_data.value;
	prbs_sync_threshold <= hwif_out.PRBS_Control.prbs_sync_threshold.value;

	tx_sync_cnt 		<= hwif_out.Tx_Sync_Cnt.tx_sync_cnt.value;

	pd_alpha1			<= hwif_out.lowpass_ema_alpha1.alpha.value;
	pd_alpha2			<= hwif_out.lowpass_ema_alpha2.alpha.value;

	symbol_lock_count 		<= hwif_out.symbol_lock_control.symbol_lock_count.value;
	symbol_lock_threshold 	<= hwif_out.symbol_lock_control.symbol_lock_threshold.value;


END ARCHITECTURE rtl;
