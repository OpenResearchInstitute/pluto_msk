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
-- This block provides a complete MSK Modulator, Demodulator, Data Interfaces, and Configuration/Status.
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

ENTITY msk_top IS 
	GENERIC (
		HASH_ID_LO 			: std_logic_vector := X"AAAA5555";
		HASH_ID_HI 			: std_logic_vector := X"FFFFCCCC";
		NCO_W 				: NATURAL := 32;
		ACC_W 				: NATURAL := 32;
		PHASE_W 			: NATURAL := 10;
		SINUSOID_W 			: NATURAL := 12;
		SAMPLE_W 			: NATURAL := 16;
		GAIN_W 				: NATURAL := 16;
		SYNC_W 				: NATURAL := 16;
		GENERATOR_W 		: NATURAL := 31;
		COUNTER_W 			: NATURAL := 32;
		DATA_W 				: NATURAL := 1;
		S_AXIS_DATA_W 		: NATURAL := 64;
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

		s_axis_aresetn 	: IN  std_logic;
		s_axis_aclk 	: IN  std_logic;
		s_axis_valid 	: IN  std_logic;
		s_axis_ready    : OUT std_logic;
		s_axis_data		: IN  std_logic_vector(S_AXIS_DATA_W -1 DOWNTO 0);

		tx_enable 		: IN std_logic;
		tx_valid 		: IN std_logic;
		tx_samples 		: OUT std_logic_vector(SAMPLE_W -1 DOWNTO 0);

		rx_enable 		: IN std_logic;
		rx_svalid 		: IN std_logic;
		rx_samples 		: IN  std_logic_vector(SAMPLE_W -1 DOWNTO 0);

		rx_dvalid 		: OUT std_logic;
		rx_data 		: OUT std_logic_vector(S_AXIS_DATA_W -1 DOWNTO 0)
	);
END ENTITY msk_top;


------------------------------------------------------------------------------------------------------
-- ╔═╗┬─┐┌─┐┬ ┬┬┌┬┐┌─┐┌─┐┌┬┐┬ ┬┬─┐┌─┐
-- ╠═╣├┬┘│  ├─┤│ │ ├┤ │   │ │ │├┬┘├┤ 
-- ╩ ╩┴└─└─┘┴ ┴┴ ┴ └─┘└─┘ ┴ └─┘┴└─└─┘
------------------------------------------------------------------------------------------------------
-- Architecture

ARCHITECTURE struct OF msk_top IS 

	SIGNAL tx_samples_int	: std_logic_vector(SAMPLE_W -1 DOWNTO 0);
	SIGNAL rx_samples_mux	: std_logic_vector(SAMPLE_W -1 DOWNTO 0);
	SIGNAL rx_samples_dec 	: std_logic_vector(11 DOWNTO 0);
	SIGNAL tx_req 		 	: std_logic;
	SIGNAL tclk 			: std_logic;
	SIGNAL tx_data_bit 		: std_logic;
	SIGNAL tx_data_bit_d1 	: std_logic;
	SIGNAL tx_data_bit_d2 	: std_logic;
	SIGNAL tx_data_bit_d3 	: std_logic;
	SIGNAL tx_data_bit_d4 	: std_logic;

	SIGNAL s_axis_tready_int: std_logic;
	SIGNAL rx_bit   		: std_logic;
	SIGNAL rx_bit_corr 		: std_logic;
	SIGNAL rx_bit_valid 	: std_logic;
	SIGNAL rx_bit_index 	: NATURAL RANGE 0 TO S_AXIS_DATA_W -1;
	SIGNAL rx_data_valid  	: std_logic;
	SIGNAL rx_data_int 		: std_logic_vector(S_AXIS_DATA_W -1 DOWNTO 0);
	SIGNAL rx_invert 		: std_logic;

	SIGNAL discard_rxsamples: std_logic_vector(7 DOWNTO 0);
	SIGNAL discard_rxnco  	: std_logic_vector(7 DOWNTO 0);

	SIGNAL rx_data_cmp 		: std_logic;
	SIGNAL data_error 		: std_logic;

	SIGNAL sent_data 		: std_logic;
	SIGNAL received_data 	: std_logic;
	SIGNAL sent_data_pipe 	: std_logic_vector(0 TO 3);

	SIGNAL bit_index 		: NATURAL RANGE 0 TO S_AXIS_DATA_W -1;
	SIGNAL tx_data 			: std_logic_vector(S_AXIS_DATA_W -1 DOWNTO 0);
	SIGNAL tx_data_axi		: std_logic_vector(S_AXIS_DATA_W -1 DOWNTO 0);

	SIGNAL ptt 				: std_logic;
	SIGNAL init 			: std_logic;

	SIGNAL tx_data_w 		: std_logic_vector(7 DOWNTO 0);
	SIGNAL rx_data_w 		: std_logic_vector(7 DOWNTO 0);

	SIGNAL loopback_ena 	: std_logic;

	SIGNAL freq_word_ft 	: std_logic_vector(NCO_W -1 DOWNTO 0);
	SIGNAL freq_word_tx_f1 	: std_logic_vector(NCO_W -1 DOWNTO 0);
	SIGNAL freq_word_tx_f2 	: std_logic_vector(NCO_W -1 DOWNTO 0);
	SIGNAL freq_word_rx_f1 	: std_logic_vector(NCO_W -1 DOWNTO 0);
	SIGNAL freq_word_rx_f2 	: std_logic_vector(NCO_W -1 DOWNTO 0);

	SIGNAL lpf_p_gain 		: std_logic_vector(GAIN_W -1 DOWNTO 0);
	SIGNAL lpf_i_gain 		: std_logic_vector(GAIN_W -1 DOWNTO 0);
	SIGNAL lpf_freeze 		: std_logic;
	SIGNAL lpf_zero   		: std_logic;
	SIGNAL lpf_alpha  		: std_logic_vector(GAIN_W -1 DOWNTO 0);

	SIGNAL lpf_accum_f1 	: std_logic_vector(ACC_W -1 DOWNTO 0);
	SIGNAL lpf_accum_f2 	: std_logic_vector(ACC_W -1 DOWNTO 0);

	SIGNAL demod_sync_lock  : std_logic;

	SIGNAL saxis_req 		: std_logic;
	SIGNAL saxis_req_meta	: std_logic;
	SIGNAL saxis_req_sync	: std_logic;
	SIGNAL saxis_req_d 		: std_logic;
	SIGNAL saxis_xfer_count : unsigned(COUNTER_W -1 DOWNTO 0);
	SIGNAL xfer_count 		: unsigned(COUNTER_W -1 DOWNTO 0);

	SIGNAL clear_counts 		: std_logic;
	SIGNAL discard_count		: unsigned(7 DOWNTO 0);

	SIGNAL tx_bit_counter 		: unsigned(COUNTER_W -1 DOWNTO 0);
	SIGNAL tx_ena_counter 		: unsigned(COUNTER_W -1 DOWNTO 0);

	SIGNAL tx_axis_valid_meta 	: std_logic;
	SIGNAL tx_axis_valid_sync 	: std_logic;

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
	SIGNAL prbs_sync_threshold : std_logic_vector(SYNC_W -1 DOWNTO 0);

BEGIN 

------------------------------------------------------------------------------------------------------
--  __                 __          ___  __  __   __       __  __ 
-- (_   __  /\  \_/ | (_    | |\ |  |  |_  |__) |_   /\  /   |_  
-- __)     /--\ / \ | __)   | | \|  |  |__ | \  |   /--\ \__ |__ 
--                                                               
------------------------------------------------------------------------------------------------------
-- S-AXIS Interface

	s_axis_ready	<= s_axis_tready_int;

	tx_samples 	<= tx_samples_int;

	rx_samples_mux <= std_logic_vector(resize(signed(tx_samples_int), 16)) WHEN loopback_ena = '1' ELSE rx_samples;

	saxis_cdc : PROCESS (s_axis_aclk)
		VARIABLE v_axi_req_ena : std_logic;
	BEGIN
		IF s_axis_aclk'EVENT AND s_axis_aclk = '1' THEN

			saxis_req_meta 	<= saxis_req;
			saxis_req_sync	<= saxis_req_meta;
			saxis_req_d 	<= saxis_req_sync;

			v_axi_req_ena 	:= saxis_req_sync XOR saxis_req_d;

			IF v_axi_req_ena = '1' THEN 
				s_axis_tready_int 	<= '1';
			END IF;

			IF s_axis_tready_int = '1' AND s_axis_valid = '1' THEN
				s_axis_tready_int 	<= '0';
				tx_data_axi 		<= s_axis_data;
				saxis_xfer_count 	<= saxis_xfer_count + 1;
			END IF;

			IF s_axis_aresetn = '0' THEN
				s_axis_tready_int	<= '0';
				tx_data_axi 		<= (OTHERS => '0');
				saxis_req_meta		<= '0';
				saxis_req_sync		<= '0';
				saxis_req_d 		<= '0';
				saxis_xfer_count 	<= (OTHERS => '0');
			END IF;

		END IF;
	END PROCESS saxis_cdc;

------------------------------------------------------------------------------------------------------
-- ___        __        __                __       ___  __     __  __  __             
--  |  \_/   |__)  /\  |__)  /\  |   |   |_  |      |  /  \   (_  |_  |__) |  /\  |   
--  |  / \   |    /--\ | \  /--\ |__ |__ |__ |__    |  \__/   __) |__ | \  | /--\ |__ 
--                                                                                    
------------------------------------------------------------------------------------------------------
-- Tx Parallel to Serial

	par2ser_proc : PROCESS (clk)
	BEGIN
		IF clk'EVENT AND clk = '1' THEN

			IF tx_req = '1' THEN

				IF bit_index = to_integer(unsigned(tx_data_w)) -1 THEN
					tx_data 	<= tx_data_axi;
					bit_index	<= 0;
					saxis_req 	<= NOT saxis_req;
					xfer_count 	<= saxis_xfer_count;
				ELSE
					bit_index <= bit_index + 1;
				END IF;
				
				tx_data_bit <= tx_data(bit_index);

				tx_data_bit_d1 <= prbs_data_bit;
				tx_data_bit_d2 <= tx_data_bit_d1;
				tx_data_bit_d3 <= tx_data_bit_d2;
				tx_data_bit_d4 <= tx_data_bit_d3;

				rx_data_cmp    <= rx_bit;

				data_error 	   <= rx_data_cmp XOR tx_data_bit_d2;

			END IF;

			IF init = '1' THEN
				saxis_req		<= '0';
				tx_data 		<= (OTHERS => '0');
				bit_index 		<= 0;
				tx_data_bit 	<= '0';
				tx_data_bit_d1	<= '0';
				tx_data_bit_d2	<= '0';
				tx_data_bit_d3	<= '0';
				xfer_count 		<= (OTHERS => '0');
			END IF;

		END IF;
	END PROCESS par2ser_proc;

	u_prbs_gen : ENTITY work.prbs_gen(rtl)
		GENERIC MAP (
			DATA_W 			=> DATA_W,
			GENERATOR_W		=> GENERATOR_W,
			TOGGLE_CONTROL  => True
		)
		PORT MAP (
			clk 			=> clk,
			init 			=> init,
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
--       __             __   __                ___  __   __  
-- |\/| (_  |_/   |\/| /  \ |  \ /  \ |    /\   |  /  \ |__) 
-- |  | __) | \   |  | \__/ |__/ \__/ |__ /--\  |  \__/ | \  
--                                                           
------------------------------------------------------------------------------------------------------
-- MSK Modulator

	u_mod : ENTITY work.msk_modulator(rtl)
		GENERIC MAP (
			NCO_W 			=> NCO_W,
			PHASE_W 		=> PHASE_W,
			SINUSOID_W 		=> SINUSOID_W,
			SAMPLE_W 		=> SAMPLE_W
		)
		PORT MAP (
			clk 			=> clk,
			init 			=> init,

			freq_word_tclk 	=> freq_word_ft,
			freq_word_f1 	=> freq_word_tx_f1,
			freq_word_f2	=> freq_word_tx_f2,

			ptt 			=> ptt,

			tx_data 		=> prbs_data_bit,
			tx_req 			=> tx_req,

			tx_enable 		=> tx_enable OR loopback_ena,
			tx_valid 		=> tx_valid OR loopback_ena,
			tx_samples	 	=> tx_samples_int
		);


------------------------------------------------------------------------------------------------------
--  __         __  __  __               ___  __     __        __                __     
-- |__) \_/   (_  |_  |__) |  /\  |      |  /  \   |__)  /\  |__)  /\  |   |   |_  |   
-- | \  / \   __) |__ | \  | /--\ |__    |  \__/   |    /--\ | \  /--\ |__ |__ |__ |__ 
--                                                                                     
------------------------------------------------------------------------------------------------------
-- Rx Serial To Parallel

	rx_bit_corr <= rx_bit WHEN rx_invert = '0' ELSE NOT rx_bit;

	ser2par_proc : PROCESS (clk)
		VARIABLE bit_width : INTEGER;
	BEGIN
		IF clk'EVENT AND clk = '1' THEN

			bit_width := to_integer(unsigned(rx_data_w));

			rx_dvalid <= '0';

			IF rx_bit_valid = '1' THEN

				rx_data_int(rx_bit_index) 	<= rx_bit_corr;
				rx_bit_index 				<= rx_bit_index + 1;

				IF rx_bit_index = bit_width -1 THEN
					rx_bit_index	<= 0;
					rx_data_valid	<= '1';
				END IF;

			END IF;

			IF rx_data_valid = '1' THEN

				rx_dvalid 		<= '1';
				rx_data 		<= rx_data_int;
				rx_data_int(bit_width -1 DOWNTO 1) <= (OTHERS => '0');
				rx_data_valid 	<= '0';

			END IF;

			IF init = '1' THEN
				rx_bit_index	<= 6;
				rx_data_int 	<= (OTHERS => '0');
				rx_data 		<= (OTHERS => '0');
				rx_dvalid 		<= '0';
				rx_data_valid 	<= '0';
			END IF;

		END IF;
	END PROCESS ser2par_proc;


------------------------------------------------------------------------------------------------------
--       __        __   __       __   __                ___  __   __  
-- |\/| (_  |_/   |  \ |_  |\/| /  \ |  \ /  \ |    /\   |  /  \ |__) 
-- |  | __) | \   |__/ |__ |  | \__/ |__/ \__/ |__ /--\  |  \__/ | \  
--                                                                                                                                     
------------------------------------------------------------------------------------------------------
-- MSK Demodulator

	u_discard : PROCESS (clk)
	BEGIN
		IF clk'EVENT AND clk = '1' THEN
			IF init = '1' THEN
				discard_count 	<= (OTHERS => '0');
				rx_samples_dec	<= (OTHERS => '0');
			ELSE
				IF rx_svalid = '1' OR loopback_ena = '1' THEN
					IF to_integer(discard_count) = 0 THEN 
						discard_count 	<= unsigned(discard_rxsamples);
						rx_samples_dec 	<= rx_samples_mux(11 DOWNTO 0);
					ELSE
						discard_count 	<= discard_count -1;
					END IF;
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
			SAMPLE_W 		=> 12
		)
		PORT MAP (
			clk 			=> clk,
			init 			=> init,
	
			rx_freq_word_f1 => freq_word_rx_f1,
			rx_freq_word_f2	=> freq_word_rx_f2,
			discard_rxnco 	=> discard_rxnco,
	
			lpf_p_gain 		=> lpf_p_gain,
			lpf_i_gain 		=> lpf_i_gain,
			lpf_freeze 	 	=> lpf_freeze,
			lpf_zero 		=> lpf_zero,
			lpf_alpha 		=> lpf_alpha,

			lpf_accum_f1 	=> lpf_accum_f1,
			lpf_accum_f2 	=> lpf_accum_f2,

			rx_enable 		=> rx_enable OR loopback_ena,
			rx_svalid 		=> '1',
			rx_samples 		=> rx_samples_dec(11 DOWNTO 0),

			rx_data 		=> rx_bit,
			rx_dvalid 		=> rx_bit_valid
		);


------------------------------------------------------------------------------------------------------
--  _   _   _   __          _       
-- |_) |_) |_) (_     |\/| / \ |\ | 
-- |   | \ |_) __)    |  | \_/ | \| 
------------------------------------------------------------------------------------------------------
-- PRBS GEN/MON

	u_prbs_mon : ENTITY work.prbs_mon(rtl)
		GENERIC MAP (
			DATA_W 			=> DATA_W,
			GENERATOR_W		=> GENERATOR_W,
			COUNTER_W 		=> COUNTER_W,
			TOGGLE_CONTROL  => True
		)
		PORT MAP (
			clk 			=> clk,
			init 			=> init,
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
--  __          ___     _  _        _ ___  __     __ ___    ___     __ 
-- (_ __ /\  \/  |     /  / \ |\ | |_  |  /__  / (_   |  /\  | | | (_  
-- __)  /--\ /\ _|_    \_ \_/ | \| |  _|_ \_| /  __)  | /--\ | |_| __) 
--                                                                                                                                  
------------------------------------------------------------------------------------------------------
-- Config/Status

	demod_sync_lock <= '0';

	stats_proc : PROCESS (clk)
	BEGIN
		IF clk'EVENT AND clk = '1' THEN 

			IF tx_enable = '1' THEN
				tx_bit_counter	<= tx_bit_counter + 1;
				tx_ena_counter 	<= tx_ena_counter + 1;
			ELSE
				tx_ena_counter 	<= tx_ena_counter - 1;
			END IF; 

			tx_axis_valid_meta <= s_axis_valid;
			tx_axis_valid_sync <= tx_axis_valid_meta;

			IF init = '1' THEN
				tx_bit_counter 		<= (OTHERS => '0');
				tx_ena_counter 		<= (OTHERS => '0');
				tx_axis_valid_meta 	<= '0';
				tx_axis_valid_sync 	<= '0';
			END IF;

		END IF;
	END PROCESS stats_proc;

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
		C_S_AXI_ADDR_WIDTH	=> C_S_AXI_ADDR_WIDTH
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
		tx_axis_valid 	=> tx_axis_valid_sync,
		xfer_count 		=> std_logic_vector(xfer_count),
		tx_bit_counter 	=> std_logic_vector(tx_bit_counter),
		tx_ena_counter 	=> std_logic_vector(tx_ena_counter),		
		prbs_bits		=> prbs_bits,
		prbs_errs		=> prbs_errs,
		lpf_accum_f1 	=> lpf_accum_f1,
		lpf_accum_f2 	=> lpf_accum_f2,

		init 				=> init,
		ptt 				=> ptt,
		loopback_ena 		=> loopback_ena,
		rx_invert 			=> rx_invert,
		clear_counts 		=> clear_counts,
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
		tx_data_w 			=> tx_data_w,
		rx_data_w 			=> rx_data_w,
		prbs_manual_sync	=> prbs_manual_sync,
		prbs_initial		=> prbs_initial,
		prbs_poly			=> prbs_poly,
		prbs_err_insert 	=> prbs_err_insert,
		prbs_err_mask 		=> prbs_err_mask,
		prbs_sel 			=> prbs_sel,
		prbs_clear 			=> prbs_clear,
		prbs_sync_threshold => prbs_sync_threshold

	);

END ARCHITECTURE struct;