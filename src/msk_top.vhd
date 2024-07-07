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


------------------------------------------------------------------------------------------------------
-- ╔═╗┌┐┌┌┬┐┬┌┬┐┬ ┬
-- ║╣ │││ │ │ │ └┬┘
-- ╚═╝┘└┘ ┴ ┴ ┴  ┴ 
------------------------------------------------------------------------------------------------------
-- Entity

ENTITY msk_top IS 
	GENERIC (
		HASH_ID 			: std_logic_vector := X"AAAA5555";
		NCO_W 				: NATURAL := 32;
		PHASE_W 			: NATURAL := 10;
		SINUSOID_W 			: NATURAL := 12;
		SAMPLE_W 			: NATURAL := 16;
		GAIN_W 				: NATURAL := 16;
		S_AXIS_DATA_W 		: NATURAL := 64;
		C_NUM_REG			: NATURAL := 32;
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

	TYPE reg_array IS ARRAY(0 TO C_NUM_REG -1) OF std_logic_vector(C_S_AXI_DATA_WIDTH -1 DOWNTO 0);
	SIGNAL csr_array 		: reg_array;
	SIGNAL csr_array_axi 	: reg_array;

	SIGNAL tx_samples_int	: std_logic_vector(SAMPLE_W -1 DOWNTO 0);
	SIGNAL rx_samples_mux	: std_logic_vector(SAMPLE_W -1 DOWNTO 0);
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
	SIGNAL freq_word_f1 	: std_logic_vector(NCO_W -1 DOWNTO 0);
	SIGNAL freq_word_f2 	: std_logic_vector(NCO_W -1 DOWNTO 0);

	SIGNAL lpf_p_gain 		: std_logic_vector(GAIN_W -1 DOWNTO 0);
	SIGNAL lpf_i_gain 		: std_logic_vector(GAIN_W -1 DOWNTO 0);
	SIGNAL lpf_freeze 		: std_logic;
	SIGNAL lpf_zero   		: std_logic;
	SIGNAL lpf_alpha  		: std_logic_vector(GAIN_W -1 DOWNTO 0);

	SIGNAL demod_sync_lock  : std_logic;

	SIGNAL saxis_req 		: std_logic;
	SIGNAL saxis_req_meta	: std_logic;
	SIGNAL saxis_req_sync	: std_logic;
	SIGNAL saxis_req_d 		: std_logic;

	SIGNAL csr_resetn 		: std_logic;
	SIGNAL csr_resetn_meta	: std_logic;

	TYPE axi_csr_states IS (IDLE, AXI_READ_VALID, AXI_READ_READY, AXI_WRITE_VALID, AXI_WRITE_DELAY, AXI_WRITE_RESP);
	SIGNAL axi_csr_state 		: axi_csr_states; 

	SIGNAL csr_rd_req_axi		: std_logic;
	SIGNAL csr_rd_req_meta 		: std_logic;
	SIGNAL csr_rd_req_sync 		: std_logic;
	SIGNAL csr_rd_req_d			: std_logic;

	SIGNAL csr_rd_ready 		: std_logic;
	SIGNAL csr_rd_ready_meta 	: std_logic;
	SIGNAL csr_rd_ready_sync 	: std_logic;
	SIGNAL csr_rd_ready_d		: std_logic;

	SIGNAL csr_rd_addr_axi 		: NATURAL RANGE 0 TO C_NUM_REG -1;
	SIGNAL csr_wr_addr_axi  	: NATURAL RANGE 0 TO C_NUM_REG -1;

	SIGNAL csr_rd_data		: std_logic_vector(C_S_AXI_DATA_WIDTH -1 DOWNTO 0);
	SIGNAL csr_wr_data_axi  : std_logic_vector(C_S_AXI_DATA_WIDTH -1 DOWNTO 0);

	SIGNAL csr_wr_stb_axi   : std_logic;
	SIGNAL csr_wr_stb_meta  : std_logic;
	SIGNAL csr_wr_stb_sync  : std_logic;
	SIGNAL csr_wr_stb_d		: std_logic;

	SIGNAL clear_counts 	: std_logic;

	SIGNAL prbs_data_bit	: std_logic;
	SIGNAL prbs_sel			: std_logic;
	SIGNAL prbs_err_insert 	: std_logic;
	SIGNAL prbs_poly		: std_logic_vector(31 DOWNTO 0);
	SIGNAL prbs_initial 	: std_logic_vector(31 DOWNTO 0);
	SIGNAL prbs_err_mask 	: std_logic_vector(31 DOWNTO 0);
	SIGNAL prbs_clear		: std_logic;
	SIGNAL prbs_sync 		: std_logic;
	SIGNAL prbs_bits 		: std_logic_vector(31 DOWNTO 0);
	SIGNAL prbs_errs 		: std_logic_vector(31 DOWNTO 0);

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
			END IF;

			IF s_axis_aresetn = '0' THEN
				s_axis_tready_int	<= '0';
				tx_data_axi 		<= (OTHERS => '0');
				saxis_req_meta		<= '0';
				saxis_req_sync		<= '0';
				saxis_req_d 		<= '0';
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
				ELSE
					bit_index <= bit_index + 1;
				END IF;
					
				tx_data_bit <= tx_data(bit_index);

				tx_data_bit_d1 <= tx_data_bit;
				tx_data_bit_d2 <= tx_data_bit_d1;
				tx_data_bit_d3 <= tx_data_bit_d2;
				tx_data_bit_d4 <= tx_data_bit_d3;

				rx_data_cmp    <= rx_bit;

				data_error 	   <= rx_data_cmp XOR tx_data_bit_d4;

			END IF;

			IF init = '1' THEN
				saxis_req		<= '0';
				tx_data 		<= (OTHERS => '0');
				bit_index 		<= 0;
				tx_data_bit 	<= '0';
				tx_data_bit_d1	<= '0';
				tx_data_bit_d2	<= '0';
				tx_data_bit_d3	<= '0';
			END IF;

		END IF;
	END PROCESS par2ser_proc;

	u_prbs_gen : ENTITY work.prbs_gen(rtl)
		GENERIC MAP (
			DATA_W 			=>  1,
			GENERATOR_W		=> 32,
			GENERATOR_BITS 	=>  5
		)
		PORT MAP (
			clk 			=> clk,
			init 			=> init,
			initial_state 	=> prbs_initial,
			polynomial 		=> prbs_poly,
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
			freq_word_f1 	=> freq_word_f1,
			freq_word_f2	=> freq_word_f2,

			ptt 			=> ptt,

			tx_data 		=> prbs_data_bit,
			tx_req 			=> tx_req,

			tx_enable 		=> tx_enable OR loopback_ena,
			tx_valid 		=> tx_valid,
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

	u_dem : ENTITY work.msk_demodulator(rtl)
		GENERIC MAP (
			NCO_W 			=> NCO_W,
			PHASE_W 		=> PHASE_W,
			SINUSOID_W 		=> SINUSOID_W,
			SAMPLE_W 		=> 12
		)
		PORT MAP (
			clk 			=> clk,
			init 			=> init,
	
			rx_freq_word_f1 => freq_word_f1,
			rx_freq_word_f2	=> freq_word_f2,
	
			lpf_p_gain 		=> lpf_p_gain,
			lpf_i_gain 		=> lpf_i_gain,
			lpf_freeze 	 	=> lpf_freeze,
			lpf_zero 		=> lpf_zero,
			lpf_alpha 		=> lpf_alpha,

			rx_enable 		=> rx_enable OR loopback_ena,
			rx_svalid 		=> rx_svalid,
			rx_samples 		=> rx_samples_mux(11 DOWNTO 0),

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
			DATA_W 			=>  1,
			GENERATOR_W		=> 32,
			GENERATOR_BITS 	=>  5
		)
		PORT MAP (
			clk 			=> clk,
			init 			=> init,
			sync 			=> prbs_sync,
			initial_state 	=> prbs_initial,
			polynomial 		=> prbs_poly,
			count_reset 	=> prbs_clear,
			data_count 		=> prbs_bits,
			error_count 	=> prbs_errs,
			data_in(0)		=> rx_bit,
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

	axi_proc : PROCESS (s_axi_aclk, s_axi_aresetn)
	BEGIN
		IF s_axi_aresetn = '0' THEN
			axi_csr_state 			<= IDLE;
			s_axi_arready			<= '0';
			s_axi_awready			<= '0';
			s_axi_wready			<= '0';
			s_axi_rvalid			<= '0';
			s_axi_bvalid			<= '0';
			s_axi_bresp   			<= "00";
			s_axi_rresp   			<= "00";
			s_axi_rdata   			<= (OTHERS => '0');
			csr_rd_req_axi 			<= '0';
			csr_rd_ready_meta 		<= '0';
			csr_rd_ready_sync 		<= '0';
			csr_rd_ready_d			<= '0';
			csr_wr_addr_axi 		<= 0;
			csr_wr_data_axi 		<= (OTHERS => '0');
			csr_wr_stb_axi 			<= '0';
		ELSIF s_axi_aclk'EVENT AND s_axi_aclk = '1' THEN

			csr_rd_ready_meta 	<= csr_rd_ready;
			csr_rd_ready_sync 	<= csr_rd_ready_meta;
			csr_rd_ready_d 		<= csr_rd_ready_sync;

			s_axi_rdata 		<= csr_rd_data;

			CASE axi_csr_state IS 

				WHEN IDLE =>

					s_axi_arready 	<= '0';
					s_axi_awready 	<= '0';
					s_axi_wready 	<= '0';
					s_axi_rvalid 	<= '0';
					s_axi_bvalid 	<= '0';

					IF s_axi_arvalid = '1' THEN 

						csr_rd_addr_axi 	<= to_integer(shift_right(unsigned(s_axi_araddr), 2));
						csr_rd_req_axi		<= NOT csr_rd_req_axi;
						s_axi_arready 		<= '1';
						axi_csr_state 		<= AXI_READ_VALID;

					END IF;

					IF s_axi_awvalid = '1' THEN 

						csr_wr_addr_axi 	<= to_integer(shift_right(unsigned(s_axi_awaddr), 2));
						s_axi_awready 		<= '1';
						axi_csr_state 		<= AXI_WRITE_VALID;

					END IF;

				WHEN AXI_READ_VALID => 

					s_axi_arready 		<= '0';

					IF (csr_rd_ready_sync XOR csr_rd_ready_d) = '1' THEN 

						s_axi_rvalid 	<= '1';
						axi_csr_state 	<= AXI_READ_READY;

					END IF;

				WHEN AXI_READ_READY => 

					IF s_axi_rready = '1' THEN 

						s_axi_rvalid 	<= '0';
						axi_csr_state 	<= IDLE;

					END IF;

				WHEN AXI_WRITE_VALID =>

					s_axi_awready <= '0';
					s_axi_wready  <= '1';

					IF s_axi_wvalid = '1' THEN 

						csr_wr_stb_axi 		<= NOT csr_wr_stb_axi;
						csr_wr_data_axi 	<= s_axi_wdata;
						s_axi_wready  		<= '0';
						axi_csr_state		<= AXI_WRITE_DELAY;

					END IF;

				WHEN AXI_WRITE_DELAY =>

					axi_csr_state	<= AXI_WRITE_RESP;

				WHEN AXI_WRITE_RESP => 

					IF s_axi_bready = '1' THEN
						s_axi_bvalid 	<= '1';
						axi_csr_state	<= IDLE;
					END IF;

				WHEN OTHERS => 

					axi_csr_state	<= IDLE;

			END CASE;

		END IF;
	END PROCESS axi_proc;


	csr_reset_proc : PROCESS (clk, s_axi_aresetn)
	BEGIN
		IF s_axi_aresetn = '0' THEN
			csr_resetn 		<= '0';
			csr_resetn_meta <= '0';
		ELSIF clk'EVENT AND clk = '1' THEN
			csr_resetn_meta <= '1';
			csr_resetn 		<= csr_resetn_meta;
		END IF;
	END PROCESS csr_reset_proc;

	csr_proc : PROCESS (clk)
	BEGIN
		IF csr_resetn = '0' THEN
			csr_wr_stb_meta	<= '0';
			csr_wr_stb_sync	<= '0';
			csr_wr_stb_d	<= '0';
			csr_rd_req_meta	<= '0';
			csr_rd_req_sync	<= '0';
			csr_rd_req_d	<= '0';
			csr_rd_data 	<= (OTHERS => '0');
			csr_array 		<= (OTHERS => (OTHERS => '0'));
			csr_rd_ready 	<= '0';
		ELSIF clk'EVENT AND clk = '1' THEN

			csr_wr_stb_meta <= csr_wr_stb_axi;
			csr_wr_stb_sync <= csr_wr_stb_meta;
			csr_wr_stb_d 	<= csr_wr_stb_sync;

			csr_rd_req_meta <= csr_rd_req_axi;
			csr_rd_req_sync <= csr_rd_req_meta;
			csr_rd_req_d 	<= csr_rd_req_sync;

			IF (csr_wr_stb_sync XOR csr_wr_stb_d) = '1'  THEN
				csr_array(csr_wr_addr_axi)	<= csr_wr_data_axi;
			END IF;

			IF (csr_rd_req_sync XOR csr_rd_req_d) = '1'  THEN
				csr_rd_data		<= csr_array(csr_rd_addr_axi);
				csr_rd_ready 	<= NOT csr_rd_ready;
			END IF;

			csr_array(0)		<= HASH_ID;
			csr_array(16)(0)	<= demod_sync_lock;
			csr_array(16)(1)	<= tx_enable;
			csr_array(16)(2) 	<= rx_enable;
			IF clear_counts = '1' THEN
				csr_array(17)		<= (OTHERS => '0');
				csr_array(18) 		<= (OTHERS => '0');
				csr_array(3)(31) 	<= '0';
			ELSE
				IF tx_req = '1' THEN
					csr_array(17)	<= std_logic_vector(unsigned(csr_array(17)) + 1);
				END IF;
				IF tx_enable = '1' THEN
					csr_array(18)	<= std_logic_vector(unsigned(csr_array(18)) + 1);
				ELSE
					csr_array(18)	<= std_logic_vector(unsigned(csr_array(19)) - 1);
				END IF;
			END IF;
			IF prbs_err_insert = '1' THEN
				csr_array(11)(1) <= '0';
			END IF;
			IF prbs_clear = '1' THEN
				csr_array(15)(0) <= '0';
			END IF;
			IF prbs_sync = '1' THEN
				csr_array(15)(1) <= '0';
			END IF;
			csr_array(19) <= prbs_bits;
			csr_array(20) <= prbs_errs;

		END IF;
	END PROCESS csr_proc;

	init 			<= csr_array(1)(0);
	ptt  			<= csr_array(2)(0);
	loopback_ena 	<= csr_array(3)(0);
	rx_invert 		<= csr_array(3)(1);
	clear_counts 	<= csr_array(3)(31);

	freq_word_ft 	<= csr_array(4);
	freq_word_f1 	<= csr_array(5);
	freq_word_f2 	<= csr_array(6);

	lpf_i_gain 		<= csr_array(7)(GAIN_W -1 DOWNTO 0);
	lpf_p_gain 		<= csr_array(7)(2*GAIN_W -1 DOWNTO GAIN_W);
	lpf_freeze 		<= csr_array(8)(0);
	lpf_zero   		<= csr_array(8)(1);
	lpf_alpha  		<= csr_array(8)(2*GAIN_W -1 DOWNTO GAIN_W);

	tx_data_w 		<= csr_array(9)(7 DOWNTO 0);
	rx_data_w 		<= csr_array(10)(7 DOWNTO 0);

	prbs_sel		<= csr_array(11)(0);
	prbs_err_insert <= csr_array(11)(1);

	prbs_poly		<= csr_array(12);
	prbs_initial 	<= csr_array(13);
	prbs_err_mask 	<= csr_array(14);

	prbs_clear		<= csr_array(15)(0);
	prbs_sync 		<= csr_array(15)(1);


END ARCHITECTURE struct;