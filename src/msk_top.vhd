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
-- Copyright 2024-5 by M. Wishek <matthew@wishek.com>
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
-- This block provides a complete MSK Modulator, Demodulator, Data Interfaces, and Configuration/Status.
--
-- Documentation location: TBD
--
------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------


------------------------------------------------------------------------------------------------------
-- MSK Top with Opulent Voice Frame Support
------------------------------------------------------------------------------------------------------
-- Modified from original msk_top.vhd to add AXIS FIFO for frame-based operation
-- Preserves all existing functionality while adding async FIFO between DMA and modulator
------------------------------------------------------------------------------------------------------
-- MODIFIED FOR MSB-FIRST: Updated sync word from 0xACFA47/0xE25F35 to 0xE25F35/0xE25F35
-- Both TX and RX now use the same sync word pattern (no bit reversal)
------------------------------------------------------------------------------------------------------

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.numeric_std.ALL;

ENTITY msk_top IS 
	GENERIC (
		HASH_ID_LO 			: std_logic_vector := X"AAAA5555";
		HASH_ID_HI 			: std_logic_vector := X"FFFFCCCC";
		NCO_W 				: NATURAL := 32;
		ACC_W 				: NATURAL := 32;
		PHASE_W 			: NATURAL := 10;
		SINUSOID_W 			: NATURAL := 12;
		SAMPLE_W 			: NATURAL := 16;
		GAIN_W 				: NATURAL := 24;
		SHIFT_W 			: NATURAL := 8;
		SYNC_W 				: NATURAL := 16;
		GENERATOR_W 		: NATURAL := 31;
		COUNTER_W 			: NATURAL := 32;
		DATA_W 				: NATURAL := 1;
		S_AXIS_DATA_W 		: NATURAL := 32;
		C_S_AXI_DATA_WIDTH	: NATURAL := 32;
		C_S_AXI_ADDR_WIDTH	: NATURAL := 32;
		SYNC_CNT_W 			: NATURAL := 24;
		FIFO_ADDR_WIDTH 	: NATURAL := 11  -- 2048 byte FIFO (used in both tx and rx)
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

		s_axis_aresetn 	: IN  std_logic;
		s_axis_aclk 	: IN  std_logic;
		s_axis_tvalid 	: IN  std_logic;
		s_axis_tready    : OUT std_logic;
		s_axis_tdata		: IN  std_logic_vector(S_AXIS_DATA_W -1 DOWNTO 0);
		s_axis_tlast 	: IN  std_logic;  -- Frame boundary marker
		s_axis_tkeep    : IN  std_logic_vector((S_AXIS_DATA_W/8) -1 DOWNTO 0);  -- Byte enables

		tx_enable 		: IN std_logic;
		tx_valid 		: IN std_logic;
		tx_samples_I	: OUT std_logic_vector(SAMPLE_W -1 DOWNTO 0);
		tx_samples_Q	: OUT std_logic_vector(SAMPLE_W -1 DOWNTO 0);

		rx_enable 		: IN std_logic;
		rx_svalid 		: IN std_logic;
		rx_samples_I	: IN  std_logic_vector(SAMPLE_W -1 DOWNTO 0);
		rx_samples_Q	: IN  std_logic_vector(SAMPLE_W -1 DOWNTO 0);

		m_axis_tdata	: OUT std_logic_vector(S_AXIS_DATA_W -1 DOWNTO 0);
		m_axis_tvalid	: OUT std_logic;
		m_axis_tready	: IN std_logic;
		m_axis_tlast	: OUT std_logic;

		frame_sync_locked	: OUT std_logic;
		frames_received	: OUT std_logic_vector(31 DOWNTO 0);
		frame_sync_errors	: OUT std_logic_vector(31 DOWNTO 0);
		fifo_overflow	: OUT std_logic

	);
END ENTITY msk_top;

ARCHITECTURE struct OF msk_top IS 

	-- Existing signals (preserved from original)
	SIGNAL tx_samples_I_int	: std_logic_vector(SAMPLE_W -1 DOWNTO 0);
	SIGNAL tx_samples_Q_int	: std_logic_vector(SAMPLE_W -1 DOWNTO 0);
	SIGNAL rx_samples_mux	: std_logic_vector(SAMPLE_W -1 DOWNTO 0);
	SIGNAL rx_samples_dec 	: std_logic_vector(11 DOWNTO 0);
	SIGNAL tx_req 		 	: std_logic;
	SIGNAL tclk 			: std_logic;
	SIGNAL tx_data_bit 		: std_logic;
	SIGNAL tx_data_bit_d1 	: std_logic;
	SIGNAL tx_data_bit_d2 	: std_logic;
	SIGNAL tx_data_bit_d3 	: std_logic;
	SIGNAL tx_data_bit_d4 	: std_logic;

	-- TX chain signals
	SIGNAL adapter_tdata    : std_logic_vector(7 DOWNTO 0);
	SIGNAL adapter_tvalid   : std_logic;
	SIGNAL adapter_tready   : std_logic;
	SIGNAL adapter_tlast    : std_logic;
	
	SIGNAL fifo_tdata       : std_logic_vector(7 DOWNTO 0);
	SIGNAL fifo_tvalid      : std_logic;
	SIGNAL fifo_tready      : std_logic;
	SIGNAL fifo_tlast       : std_logic;
	
	SIGNAL frame_complete   : std_logic;
	SIGNAL fifo_prog_full   : std_logic;
	SIGNAL fifo_prog_empty  : std_logic;

	-- RX chain signals
	SIGNAL rx_byte              : std_logic_vector(7 DOWNTO 0);
	SIGNAL rx_byte_valid        : std_logic;
    
	SIGNAL sync_det_tdata       : std_logic_vector(7 DOWNTO 0);
	SIGNAL sync_det_tvalid      : std_logic;
	SIGNAL sync_det_tready      : std_logic;
	SIGNAL sync_det_tlast       : std_logic;
    
	SIGNAL rx_fifo_overflow     : std_logic;
	SIGNAL rx_frame_sync_locked       : std_logic;
	SIGNAL rx_frames_count      : std_logic_vector(31 DOWNTO 0);
	SIGNAL rx_frame_sync_errors       : std_logic_vector(31 DOWNTO 0);

	SIGNAL rx_bit   		: std_logic;
	SIGNAL rx_bit_corr 		: std_logic;
	SIGNAL rx_bit_valid 	: std_logic;
	SIGNAL rx_bit_index 	: NATURAL RANGE 0 TO S_AXIS_DATA_W -1;
	SIGNAL rx_data_valid  	: std_logic;
	SIGNAL rx_data_int 		: std_logic_vector(S_AXIS_DATA_W -1 DOWNTO 0);
	SIGNAL rx_invert 		: std_logic;

	SIGNAL rx_sample_clk 	: std_logic;
	SIGNAL discard_rxsamples: std_logic_vector(7 DOWNTO 0);
	SIGNAL discard_rxnco  	: std_logic_vector(7 DOWNTO 0);

	SIGNAL rx_data_cmp 		: std_logic;
	SIGNAL data_error 		: std_logic;

	SIGNAL sent_data 		: std_logic;
	SIGNAL received_data 	: std_logic;
	SIGNAL sent_data_pipe 	: std_logic_vector(0 TO 3);

	SIGNAL ptt 				: std_logic;
	SIGNAL ptt_d 			: std_logic;
	SIGNAL ptt_start 		: std_logic;
	SIGNAL txinit 			: std_logic;
	SIGNAL rxinit 			: std_logic;

	SIGNAL tx_data_w 		: std_logic_vector(7 DOWNTO 0);
	SIGNAL rx_data_w 		: std_logic_vector(7 DOWNTO 0);

	SIGNAL loopback_ena 	: std_logic;

	SIGNAL diff_encdec_lbk_ena 	: std_logic;
	SIGNAL diff_encdec_lbk_tclk : std_logic;
	SIGNAL diff_encdec_lbk_f1   : std_logic_vector(1 DOWNTO 0);
	SIGNAL diff_encdec_lbk_f2   : std_logic_vector(1 DOWNTO 0);

	SIGNAL freq_word_ft 	: std_logic_vector(NCO_W -1 DOWNTO 0);
	SIGNAL freq_word_tx_f1 	: std_logic_vector(NCO_W -1 DOWNTO 0);
	SIGNAL freq_word_tx_f2 	: std_logic_vector(NCO_W -1 DOWNTO 0);
	SIGNAL freq_word_rx_f1 	: std_logic_vector(NCO_W -1 DOWNTO 0);
	SIGNAL freq_word_rx_f2 	: std_logic_vector(NCO_W -1 DOWNTO 0);

	SIGNAL lpf_p_gain 		: std_logic_vector(GAIN_W -1 DOWNTO 0);
	SIGNAL lpf_i_gain 		: std_logic_vector(GAIN_W -1 DOWNTO 0);
	SIGNAL lpf_p_shift 		: std_logic_vector(SHIFT_W -1 DOWNTO 0);
	SIGNAL lpf_i_shift 		: std_logic_vector(SHIFT_W -1 DOWNTO 0);
	SIGNAL lpf_freeze 		: std_logic;
	SIGNAL lpf_zero   		: std_logic;
	SIGNAL lpf_alpha  		: std_logic_vector(GAIN_W -1 DOWNTO 0);

	SIGNAL lpf_accum_f1 	: std_logic_vector(ACC_W -1 DOWNTO 0);
	SIGNAL lpf_accum_f2 	: std_logic_vector(ACC_W -1 DOWNTO 0);
	SIGNAL f1_nco_adjust	: std_logic_vector(31 DOWNTO 0);
	SIGNAL f2_nco_adjust	: std_logic_vector(31 DOWNTO 0);
	SIGNAL f1_error			: std_logic_vector(31 DOWNTO 0);
	SIGNAL f2_error			: std_logic_vector(31 DOWNTO 0);

	SIGNAL demod_sync_lock  : std_logic;

	SIGNAL clear_counts 		: unsigned(COUNTER_W -1 DOWNTO 0);
	SIGNAL discard_count		: unsigned(7 DOWNTO 0);

	SIGNAL tx_bit_counter 		: unsigned(COUNTER_W -1 DOWNTO 0);
	SIGNAL tx_ena_counter 		: unsigned(COUNTER_W -1 DOWNTO 0);

	SIGNAL prbs_data_bit		: std_logic;
	SIGNAL prbs_sel				: std_logic;
	SIGNAL prbs_err_insert 		: std_logic;
	SIGNAL prbs_poly			: std_logic_vector(31 DOWNTO 0);
	SIGNAL prbs_initial 		: std_logic_vector(31 DOWNTO 0);
	SIGNAL prbs_err_mask 		: std_logic_vector(31 DOWNTO 0);
	SIGNAL prbs_clear			: std_logic;
	SIGNAL prbs_manual_sync		: std_logic;
	SIGNAL prbs_bits 			: std_logic_vector(31 DOWNTO 0);
	SIGNAL prbs_errs 			: std_logic_vector(31 DOWNTO 0);
	SIGNAL prbs_sync_threshold 	: std_logic_vector(SYNC_W -1 DOWNTO 0);

	SIGNAL tx_sync_ena 			: std_logic;
	SIGNAL tx_sync_cnt 			: std_logic_vector(SYNC_CNT_W -1 DOWNTO 0);
	SIGNAL tx_sync_force		: std_logic;
	SIGNAL tx_sync_f1			: std_logic;
	SIGNAL tx_sync_f2			: std_logic;

	SIGNAL pd_alpha1			: std_logic_vector(17 DOWNTO 0);
	SIGNAL pd_alpha2			: std_logic_vector(17 DOWNTO 0);
	SIGNAL pd_power 			: std_logic_vector(22 DOWNTO 0);

BEGIN 

------------------------------------------------------------------------------------------------------
-- OPULENT VOICE TX FIFO CHAIN
------------------------------------------------------------------------------------------------------

	-- Stage 1: DMA Adapter (32-bit to 8-bit)
	u_dma_adapter : ENTITY work.axis_dma_adapter
		GENERIC MAP (
			DMA_WIDTH   => S_AXIS_DATA_W,
			BYTE_WIDTH  => 8
		)
		PORT MAP (
			aclk            => s_axis_aclk,
			aresetn         => s_axis_aresetn,
			
			s_axis_tdata    => s_axis_tdata,
			s_axis_tvalid   => s_axis_tvalid,
			s_axis_tready   => s_axis_tready,
			s_axis_tlast    => s_axis_tlast,
			s_axis_tkeep    => s_axis_tkeep,
			
			m_axis_tdata    => adapter_tdata,
			m_axis_tvalid   => adapter_tvalid,
			m_axis_tready   => adapter_tready,
			m_axis_tlast    => adapter_tlast
		);

	-- Stage 2: Async FIFO (Clock Domain Crossing)
	u_async_fifo : ENTITY work.axis_async_fifo
		GENERIC MAP (
			DATA_WIDTH  => 8,
			ADDR_WIDTH  => FIFO_ADDR_WIDTH
		)
		PORT MAP (
			wr_aclk         => s_axis_aclk,
			wr_aresetn      => s_axis_aresetn,
			
			s_axis_tdata    => adapter_tdata,
			s_axis_tvalid   => adapter_tvalid,
			s_axis_tready   => adapter_tready,
			s_axis_tlast    => adapter_tlast,
			
			rd_aclk         => clk,
			rd_aresetn      => NOT txinit,
			
			m_axis_tdata    => fifo_tdata,
			m_axis_tvalid   => fifo_tvalid,
			m_axis_tready   => fifo_tready,
			m_axis_tlast    => fifo_tlast,
			
			prog_full       => fifo_prog_full,
			prog_empty      => fifo_prog_empty
		);

	-- Stage 3: Byte-to-Bit De-serializer (MSB-FIRST VERSION)
	u_deserializer : ENTITY work.byte_to_bit_deserializer
		GENERIC MAP (
			BYTE_WIDTH => 8
		)
		PORT MAP (
			clk             => clk,
			init            => txinit,
			
			s_axis_tdata    => fifo_tdata,
			s_axis_tvalid   => fifo_tvalid,
			s_axis_tready   => fifo_tready,
			s_axis_tlast    => fifo_tlast,
			
			tx_data         => tx_data_bit,
			tx_req          => tx_req,
			
			frame_complete  => frame_complete
		);

------------------------------------------------------------------------------------------------------
-- Pipeline for tx_data_bit
------------------------------------------------------------------------------------------------------

	tx_samples_I 	<= tx_samples_I_int;
	tx_samples_Q 	<= tx_samples_Q_int;

	rx_samples_mux <= std_logic_vector(resize(signed(tx_samples_I_int), 16)) WHEN loopback_ena = '1' ELSE rx_samples_I;

	-- Delay pipeline for tx_data_bit
	tx_delay_proc : PROCESS (clk)
	BEGIN
		IF clk'EVENT AND clk = '1' THEN
			IF tx_req = '1' THEN
				tx_data_bit_d1 <= prbs_data_bit;
				tx_data_bit_d2 <= tx_data_bit_d1;
				tx_data_bit_d3 <= tx_data_bit_d2;
				tx_data_bit_d4 <= tx_data_bit_d3;

				rx_data_cmp    <= rx_bit;
				data_error 	   <= rx_data_cmp XOR tx_data_bit_d2;
			END IF;

			IF txinit = '1' THEN
				tx_data_bit_d1	<= '0';
				tx_data_bit_d2	<= '0';
				tx_data_bit_d3	<= '0';
				tx_data_bit_d4	<= '0';
			END IF;
		END IF;
	END PROCESS tx_delay_proc;

------------------------------------------------------------------------------------------------------
-- PRBS Generator
------------------------------------------------------------------------------------------------------

	-- PRBS Generator
	u_prbs_gen : ENTITY work.prbs_gen(rtl)
		GENERIC MAP (
			DATA_W 			=> DATA_W,
			GENERATOR_W		=> GENERATOR_W,
			TOGGLE_CONTROL  => True
		)
		PORT MAP (
			clk 			=> clk,
			init 			=> txinit,
			initial_state 	=> prbs_initial(GENERATOR_W -1 DOWNTO 0),
			polynomial 		=> prbs_poly(GENERATOR_W -1 DOWNTO 0),
			error_insert 	=> prbs_err_insert,
			error_mask 		=> prbs_err_mask(1 -1 DOWNTO 0),
			prbs_sel 		=> prbs_sel,
			data_in(0)		=> tx_data_bit,
			data_req		=> tx_req,
			data_out(0)		=> prbs_data_bit
		);

------------------------------------------------------------------------------------------------------
-- MSK MODULATOR
------------------------------------------------------------------------------------------------------

	u_mod : ENTITY work.msk_modulator(rtl)
		GENERIC MAP (
			NCO_W 			=> NCO_W,
			PHASE_W 		=> PHASE_W,
			SINUSOID_W 		=> SINUSOID_W,
			SAMPLE_W 		=> SAMPLE_W,
			SYNC_CNT_W		=> SYNC_CNT_W
		)
		PORT MAP (
			clk 			=> clk,
			init 			=> txinit,

			freq_word_tclk 	=> freq_word_ft,
			freq_word_f1 	=> freq_word_tx_f1,
			freq_word_f2	=> freq_word_tx_f2,

			ptt 			=> ptt,
			tx_sync_ena 	=> tx_sync_ena,
			tx_sync_cnt 	=> tx_sync_cnt,
			tx_sync_force	=> tx_sync_force,

			tx_data 		=> prbs_data_bit,
			tx_req 			=> tx_req,

			tx_enc_lbk_tclk		=> diff_encdec_lbk_tclk,
			tx_enc_lbk_f1		=> diff_encdec_lbk_f1,
			tx_enc_lbk_f2		=> diff_encdec_lbk_f2,

			tx_enable 		=> tx_enable OR loopback_ena,
			tx_valid 		=> tx_valid OR loopback_ena,
			tx_samples_I	=> tx_samples_I_int,
			tx_samples_Q	=> tx_samples_Q_int
		);







    
    ------------------------------------------------------------------------------
    -- RX Stage 2: Frame Sync Detector (MSB-FIRST VERSION)
    -- MODIFIED: Sync word changed from 0xE25F35 to 0xE25F35 (matches TX now!)
    ------------------------------------------------------------------------------
    u_rx_frame_sync : ENTITY work.frame_sync_detector
        GENERIC MAP (
            SYNC_WORD      => x"E25F35",  -- MSB-first sync word (same as TX!)
            PAYLOAD_BYTES  => 268,
            SYNC_THRESHOLD => 3,
            BUFFER_DEPTH   => 11,         -- 2048 bytes
            LOCK_FRAMES    => 3
        )
        PORT MAP (
            clk             => clk,
            reset           => rxinit,
            
            rx_bit          => rx_bit_corr,
            rx_bit_valid    => rx_bit_valid,
            
            m_axis_tdata    => sync_det_tdata,
            m_axis_tvalid   => sync_det_tvalid,
            m_axis_tready   => sync_det_tready,
            m_axis_tlast    => sync_det_tlast,
	    frame_sync_locked => rx_frame_sync_locked,            
            frames_received => rx_frames_count,
            frame_sync_errors     => rx_frame_sync_errors,
            buffer_overflow => rx_fifo_overflow
        );
    
    ------------------------------------------------------------------------------
    -- RX Stage 3: Async FIFO (Clock Domain Crossing)
    -- Reuses existing axis_async_fifo component!
    ------------------------------------------------------------------------------
    u_rx_async_fifo : ENTITY work.axis_async_fifo
        GENERIC MAP (
            DATA_WIDTH  => 8,
            ADDR_WIDTH  => FIFO_ADDR_WIDTH  -- Reuse generic (11 = 2048 bytes)
        )
        PORT MAP (
            -- Write side (symbol clock domain)
            wr_aclk         => clk,
            wr_aresetn      => NOT rxinit,
            
            s_axis_tdata    => sync_det_tdata,
            s_axis_tvalid   => sync_det_tvalid,
            s_axis_tready   => sync_det_tready,
            s_axis_tlast    => sync_det_tlast,
            
            -- Read side (AXI clock domain)
            rd_aclk         => s_axis_aclk,  -- Use system AXI clock
            rd_aresetn      => s_axis_aresetn,
            
            m_axis_tdata    => m_axis_tdata(7 DOWNTO 0),
            m_axis_tvalid   => m_axis_tvalid,
            m_axis_tready   => m_axis_tready,
            m_axis_tlast    => m_axis_tlast,
            
            prog_full       => OPEN,
            prog_empty      => OPEN
        );
    
    -- Zero-pad upper bits of m_axis_tdata if wider than 8 bits
    m_axis_tdata(S_AXIS_DATA_W-1 DOWNTO 8) <= (OTHERS => '0');
    
    -- Connect status outputs to top-level ports
    frame_sync_locked     <= rx_frame_sync_locked;
    frames_received       <= rx_frames_count;
    frame_sync_errors     <= rx_frame_sync_errors;
    fifo_overflow         <= rx_fifo_overflow;




















        rx_bit_corr <= rx_bit WHEN rx_invert = '0' ELSE NOT rx_bit;


------------------------------------------------------------------------------------------------------
-- MSK DEMODULATOR
------------------------------------------------------------------------------------------------------

	u_discard : PROCESS (clk)
	BEGIN
		IF clk'EVENT AND clk = '1' THEN
			IF rxinit = '1' THEN
				discard_count 	<= (OTHERS => '0');
				rx_samples_dec	<= (OTHERS => '0');
			ELSE
				IF to_integer(discard_count) = 0 AND (rx_svalid = '1' OR loopback_ena = '1') THEN 
					discard_count 	<= unsigned(discard_rxsamples);
					rx_samples_dec 	<= rx_samples_mux(11 DOWNTO 0);
					rx_sample_clk 	<= '1';
				ELSE
					discard_count 	<= discard_count -1;
					rx_sample_clk 	<= '0';
				END IF;
			END IF;
		END IF;
	END PROCESS u_discard;

	u_dem : ENTITY work.msk_demodulator(rtl)
		GENERIC MAP (
			NCO_W 			=> NCO_W,
			ACC_W 			=> ACC_W,
			PHASE_W 		=> PHASE_W,
			SINUSOID_W 		=> SINUSOID_W,
			GAIN_W 			=> GAIN_W,
			SHIFT_W 		=> SHIFT_W,
			SAMPLE_W 		=> 12
		)
		PORT MAP (
			clk 			=> clk,
			init 			=> rxinit,
	
			rx_freq_word_f1 => freq_word_rx_f1,
			rx_freq_word_f2	=> freq_word_rx_f2,
			discard_rxnco 	=> discard_rxnco,
	
			lpf_p_gain 		=> lpf_p_gain,
			lpf_i_gain 		=> lpf_i_gain,
			lpf_i_shift		=> lpf_i_shift,
			lpf_p_shift		=> lpf_p_shift,
			lpf_freeze 	 	=> lpf_freeze,
			lpf_zero 		=> lpf_zero,
			lpf_alpha 		=> lpf_alpha,

			lpf_accum_f1 	=> lpf_accum_f1,
			lpf_accum_f2 	=> lpf_accum_f2,
			f1_nco_adjust	=> f1_nco_adjust,
			f2_nco_adjust	=> f2_nco_adjust,
			f1_error		=> f1_error,
			f2_error		=> f2_error,

			rx_dec_lbk_ena		=> diff_encdec_lbk_ena,
			rx_dec_lbk_tclk		=> diff_encdec_lbk_tclk,
			rx_dec_lbk_f1		=> diff_encdec_lbk_f1,
			rx_dec_lbk_f2		=> diff_encdec_lbk_f2,

			rx_enable 		=> rx_enable OR loopback_ena,
			rx_svalid 		=> rx_sample_clk,
			rx_samples 		=> rx_samples_dec(11 DOWNTO 0),

			rx_data 		=> rx_bit,
			rx_dvalid 		=> rx_bit_valid
		);

------------------------------------------------------------------------------------------------------
-- PRBS MONITOR (preserved)
------------------------------------------------------------------------------------------------------

	u_prbs_mon : ENTITY work.prbs_mon(rtl)
		GENERIC MAP (
			DATA_W 			=> DATA_W,
			GENERATOR_W		=> GENERATOR_W,
			COUNTER_W 		=> COUNTER_W,
			TOGGLE_CONTROL  => True
		)
		PORT MAP (
			clk 			=> clk,
			init 			=> rxinit,
			sync_manual		=> prbs_manual_sync,
			sync_threshold  => prbs_sync_threshold,
			initial_state 	=> prbs_initial(GENERATOR_W -1 DOWNTO 0),
			polynomial 		=> prbs_poly(GENERATOR_W -1 DOWNTO 0),
			count_reset 	=> prbs_clear,
			data_count 		=> prbs_bits,
			error_count 	=> prbs_errs,
			data_in(0)		=> rx_bit_corr,
			data_in_valid	=> rx_bit_valid
		);

------------------------------------------------------------------------------------------------------
-- POWER DETECTOR (preserved)
------------------------------------------------------------------------------------------------------

	u_power_det : ENTITY work.power_detector(rtl)
		GENERIC MAP (
			DATA_W 			=> 12,
			ALPHA_W 		=> 18,
			IQ_MOD 			=> True,
			I_USED 			=> False,
			Q_USED 			=> False,
			EMA_CASCADE 	=> False
		)
		PORT MAP (
			clk 			=> clk,
			init 			=> rxinit,
			alpha1			=> pd_alpha1,
			alpha2			=> pd_alpha2,
			data_I 			=> rx_samples_I(15 DOWNTO 4),
			data_Q 			=> rx_samples_Q(15 DOWNTO 4),
			data_ena		=> rx_svalid,
			power_squared 	=> pd_power
		);

------------------------------------------------------------------------------------------------------
-- CONFIG/STATUS (preserved)
------------------------------------------------------------------------------------------------------

	demod_sync_lock <= '0';
	ptt_start <= ptt AND NOT ptt_d;

	stats_proc : PROCESS (clk)
	BEGIN
		IF clk'EVENT AND clk = '1' THEN 
			ptt_d <= ptt;

			IF ptt_start = '1' THEN
				tx_bit_counter <= (OTHERS => '0');
			ELSIF tx_req = '1' THEN
				tx_bit_counter	<= tx_bit_counter + 1;
			END IF;

			IF tx_enable = '1' THEN
				tx_ena_counter 	<= tx_ena_counter + 1;
			ELSE
				tx_ena_counter 	<= tx_ena_counter - 1;
			END IF; 

			IF txinit = '1' THEN
				tx_bit_counter 		<= (OTHERS => '0');
				tx_ena_counter 		<= (OTHERS => '0');
			END IF;
		END IF;
	END PROCESS stats_proc;

	-- CSR block instantiation (preserved, would need full original code)
	u_msk_top_csr : ENTITY work.msk_top_csr(rtl)
	GENERIC MAP (
		HASH_ID_LO 			=> HASH_ID_LO,
		HASH_ID_HI 			=> HASH_ID_HI,
		GAIN_W 				=> GAIN_W,
		NCO_W 				=> NCO_W,
		ACC_W 				=> ACC_W,
		COUNTER_W 			=> 32,
		GENERATOR_W 		=> 32,
		C_S_AXI_DATA_WIDTH	=> C_S_AXI_DATA_WIDTH,
		C_S_AXI_ADDR_WIDTH	=> C_S_AXI_ADDR_WIDTH,
		SYNC_CNT_W 			=> SYNC_CNT_W
	)
	PORT MAP (
		clk 			=> clk,
		s_axi_aclk		=> s_axi_aclk,
		s_axi_aresetn	=> s_axi_aresetn,
		s_axi_awaddr	=> s_axi_awaddr,
		s_axi_awvalid	=> s_axi_awvalid,
		s_axi_wdata		=> s_axi_wdata,
		s_axi_wstrb		=> s_axi_wstrb,
		s_axi_wvalid	=> s_axi_wvalid,
		s_axi_bready	=> s_axi_bready,
		s_axi_araddr	=> s_axi_araddr,
		s_axi_arvalid	=> s_axi_arvalid,
		s_axi_rready	=> s_axi_rready,
		s_axi_arready	=> s_axi_arready,
		s_axi_rdata		=> s_axi_rdata,
		s_axi_rresp		=> s_axi_rresp,
		s_axi_rvalid	=> s_axi_rvalid,
		s_axi_wready	=> s_axi_wready,
		s_axi_bresp		=> s_axi_bresp,
		s_axi_bvalid	=> s_axi_bvalid,
		s_axi_awready	=> s_axi_awready,
		s_axi_awprot 	=> s_axi_awprot,
		s_axi_arprot 	=> s_axi_arprot,
		tx_enable 		=> tx_enable,
		rx_enable 		=> rx_enable,
		demod_sync_lock => demod_sync_lock,
		tx_req 			=> tx_req,
		tx_axis_valid 	=> s_axis_tvalid,
		xfer_count 		=> std_logic_vector(tx_bit_counter),
		tx_bit_counter 	=> std_logic_vector(tx_bit_counter),
		tx_ena_counter 	=> std_logic_vector(tx_ena_counter),		
		prbs_bits		=> prbs_bits,
		prbs_errs		=> prbs_errs,
		lpf_accum_f1 	=> lpf_accum_f1,
		lpf_accum_f2 	=> lpf_accum_f2,
		f1_nco_adjust	=> f1_nco_adjust,
		f2_nco_adjust	=> f2_nco_adjust,
		f1_error		=> f1_error,
		f2_error		=> f2_error,
		txinit 				=> txinit,
		rxinit 				=> rxinit,
		ptt 				=> ptt,
		loopback_ena 		=> loopback_ena,
		diff_encdec_lbk_ena => diff_encdec_lbk_ena,
		rx_invert 			=> rx_invert,
		clear_counts 		=> open,
		discard_rxsamples	=> discard_rxsamples,
		discard_rxnco 		=> discard_rxnco,
		freq_word_ft		=> freq_word_ft,
		freq_word_tx_f1		=> freq_word_tx_f1,
		freq_word_tx_f2		=> freq_word_tx_f2,
		freq_word_rx_f1		=> freq_word_rx_f1,
		freq_word_rx_f2		=> freq_word_rx_f2,
		lpf_freeze 			=> lpf_freeze,
		lpf_zero 			=> lpf_zero,
		lpf_alpha 			=> lpf_alpha,
		lpf_i_gain 			=> lpf_i_gain,
		lpf_p_gain 			=> lpf_p_gain,
		lpf_i_shift			=> lpf_i_shift,
		lpf_p_shift			=> lpf_p_shift,
		tx_data_w 			=> tx_data_w,
		rx_data_w 			=> rx_data_w,
		prbs_manual_sync	=> prbs_manual_sync,
		prbs_initial		=> prbs_initial,
		prbs_poly			=> prbs_poly,
		prbs_err_insert 	=> prbs_err_insert,
		prbs_err_mask 		=> prbs_err_mask,
		prbs_sel 			=> prbs_sel,
		prbs_clear 			=> prbs_clear,
		prbs_sync_threshold => prbs_sync_threshold,
		tx_sync_ena 		=> tx_sync_ena,
		tx_sync_cnt 		=> tx_sync_cnt,
		tx_sync_force		=> tx_sync_force,
		tx_sync_f1			=> tx_sync_f1,
		tx_sync_f2			=> tx_sync_f2,
		pd_alpha1			=> pd_alpha1,
		pd_alpha2			=> pd_alpha2,
		pd_power 			=> pd_power
	);

END ARCHITECTURE struct;
