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
------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------


------------------------------------------------------------------------------------------------------
-- Libraries
------------------------------------------------------------------------------------------------------

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.numeric_std.ALL;

USE work.pkg_msk_top_regs.ALL;

------------------------------------------------------------------------------------------------------
-- Entity
------------------------------------------------------------------------------------------------------

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
		------------
		-- framer --
		------------
		OV_FRAME_BYTES 		: NATURAL := 134;
		SYNC_BITS 			: NATURAL := 24;
		ENCODED_BITS 		: NATURAL := 2144;
		INTERLEAVER_DEPTH 	: NATURAL := 2144;
		--------------
		-- deframer --
		--------------
		M_AXIS_DATA_W		: NATURAL := 32;
		SYNC_THRESHOLD		: NATURAL := 3;
		FIFO_DEPTH			: NATURAL := 4
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
		s_axis_tlast	: IN  std_logic;
		s_axis_tkeep	: IN  std_logic_vector(S_AXIS_DATA_W/8-1 DOWNTO 0);

		tx_enable 		: IN std_logic;
		tx_valid 		: IN std_logic;
		tx_samples_I	: OUT std_logic_vector(SAMPLE_W -1 DOWNTO 0);
		tx_samples_Q	: OUT std_logic_vector(SAMPLE_W -1 DOWNTO 0);

		rx_enable 		: IN std_logic;
		rx_svalid 		: IN std_logic;
		rx_samples_I	: IN  std_logic_vector(SAMPLE_W -1 DOWNTO 0);
		rx_samples_Q	: IN  std_logic_vector(SAMPLE_W -1 DOWNTO 0);

		-- framer ports
		frame_start		: OUT std_logic;
		frame_active	: OUT std_logic; 
		frames_processed: OUT std_logic_vector(31 DOWNTO 0);

		-- deframer ports
		m_axis_tdata	: OUT std_logic_vector(M_AXIS_DATA_W-1 DOWNTO 0);
		m_axis_tvalid	: OUT std_logic;
		m_axis_tready	: IN  std_logic;
		m_axis_tlast	: OUT std_logic;

		sync_locked		: OUT std_logic;
		frames_received	: OUT std_logic_vector(31 DOWNTO 0);
		sync_errors		: OUT std_logic_vector(31 DOWNTO 0);
		fifo_overflow	: OUT std_logic
	);
END ENTITY msk_top;


------------------------------------------------------------------------------------------------------
-- Architecture
------------------------------------------------------------------------------------------------------

ARCHITECTURE struct OF msk_top IS 

	SIGNAL tx_samples_I_int	: std_logic_vector(SAMPLE_W -1 DOWNTO 0);
	SIGNAL tx_samples_Q_int	: std_logic_vector(SAMPLE_W -1 DOWNTO 0);
	SIGNAL rx_samples_mux	: std_logic_vector(SAMPLE_W -1 DOWNTO 0);
	SIGNAL rx_samples_dec	: std_logic_vector(11 DOWNTO 0);
	SIGNAL tx_req		: std_logic;
	SIGNAL tclk		: std_logic;
	SIGNAL tx_data_bit	: std_logic;
	SIGNAL tx_data_bit_d1	: std_logic;
	SIGNAL tx_data_bit_d2	: std_logic;
	SIGNAL tx_data_bit_d3	: std_logic;
	SIGNAL tx_data_bit_d4	: std_logic;

	SIGNAL rx_bit		: std_logic;
	SIGNAL rx_bit_corr	: std_logic;
	SIGNAL rx_bit_valid	: std_logic;
	SIGNAL rx_invert	: std_logic;

	SIGNAL rx_sample_clk	: std_logic;
	SIGNAL discard_rxsamples: std_logic_vector(7 DOWNTO 0);
	SIGNAL discard_rxnco	: std_logic_vector(7 DOWNTO 0);

	SIGNAL rx_data_cmp	: std_logic;
	SIGNAL data_error	: std_logic;

	SIGNAL ptt		: std_logic;
	SIGNAL txinit		: std_logic;
	SIGNAL rxinit		: std_logic;

	SIGNAL tx_data_w	: std_logic_vector(7 DOWNTO 0);
	SIGNAL rx_data_w	: std_logic_vector(7 DOWNTO 0);

	SIGNAL loopback_ena	: std_logic;

	SIGNAL freq_word_ft	: std_logic_vector(NCO_W -1 DOWNTO 0);
	SIGNAL freq_word_tx_f1	: std_logic_vector(NCO_W -1 DOWNTO 0);
	SIGNAL freq_word_tx_f2	: std_logic_vector(NCO_W -1 DOWNTO 0);
	SIGNAL freq_word_rx_f1	: std_logic_vector(NCO_W -1 DOWNTO 0);
	SIGNAL freq_word_rx_f2	: std_logic_vector(NCO_W -1 DOWNTO 0);

	SIGNAL lpf_p_gain	: std_logic_vector(GAIN_W -1 DOWNTO 0);
	SIGNAL lpf_i_gain	: std_logic_vector(GAIN_W -1 DOWNTO 0);
	SIGNAL lpf_p_shift	: std_logic_vector(SHIFT_W -1 DOWNTO 0);
	SIGNAL lpf_i_shift	: std_logic_vector(SHIFT_W -1 DOWNTO 0);
	SIGNAL lpf_freeze	: std_logic;
	SIGNAL lpf_zero		: std_logic;
	SIGNAL lpf_alpha	: std_logic_vector(GAIN_W -1 DOWNTO 0);

	SIGNAL lpf_accum_f1	: std_logic_vector(ACC_W -1 DOWNTO 0);
	SIGNAL lpf_accum_f2	: std_logic_vector(ACC_W -1 DOWNTO 0);
	SIGNAL f1_nco_adjust	: std_logic_vector(31 DOWNTO 0);
	SIGNAL f2_nco_adjust	: std_logic_vector(31 DOWNTO 0);
	SIGNAL f1_error		: std_logic_vector(31 DOWNTO 0);
	SIGNAL f2_error		: std_logic_vector(31 DOWNTO 0);

	SIGNAL demod_sync_lock  : std_logic;

	SIGNAL clear_counts	: std_logic;
	SIGNAL discard_count	: unsigned(7 DOWNTO 0);

	SIGNAL tx_bit_counter	: unsigned(COUNTER_W -1 DOWNTO 0);
	SIGNAL tx_ena_counter	: unsigned(COUNTER_W -1 DOWNTO 0);

	SIGNAL tx_axis_valid_meta	: std_logic;
	SIGNAL tx_axis_valid_sync	: std_logic;

	SIGNAL prbs_data_bit		: std_logic;
	SIGNAL prbs_sel			: std_logic;
	SIGNAL prbs_err_insert		: std_logic;
	SIGNAL prbs_poly		: std_logic_vector(31 DOWNTO 0);
	SIGNAL prbs_initial		: std_logic_vector(31 DOWNTO 0);
	SIGNAL prbs_err_mask		: std_logic_vector(31 DOWNTO 0);
	SIGNAL prbs_clear		: std_logic;
	SIGNAL prbs_manual_sync		: std_logic;
	SIGNAL prbs_bits		: std_logic_vector(31 DOWNTO 0);
	SIGNAL prbs_errs		: std_logic_vector(31 DOWNTO 0);
	SIGNAL prbs_sync_threshold	: std_logic_vector(SYNC_W -1 DOWNTO 0);

	SIGNAL tx_sync_ena		: std_logic;
	SIGNAL tx_sync_cnt		: std_logic_vector(SYNC_CNT_W -1 DOWNTO 0);
	SIGNAL tx_sync_force		: std_logic;
	SIGNAL tx_sync_f1		: std_logic;
	SIGNAL tx_sync_f2		: std_logic;

	SIGNAL pd_alpha1		: std_logic_vector(17 DOWNTO 0);
	SIGNAL pd_alpha2		: std_logic_vector(17 DOWNTO 0);
	SIGNAL pd_power			: std_logic_vector(22 DOWNTO 0);

	------------
	-- FIFO --
	------------
	SIGNAL fifo_wr_en		: std_logic;
	SIGNAL fifo_wr_data		: std_logic_vector(7 DOWNTO 0);
	SIGNAL fifo_full		: std_logic;
	SIGNAL fifo_almost_full	: std_logic;
	
	SIGNAL fifo_rd_en		: std_logic;
	SIGNAL fifo_rd_data		: std_logic_vector(7 DOWNTO 0);
	SIGNAL fifo_empty		: std_logic;
	SIGNAL fifo_almost_empty: std_logic;

	SIGNAL fifo_wr_tlast		: std_logic;
	SIGNAL fifo_rd_tlast		: std_logic;

	------------
	-- framer --
	------------
	SIGNAL tlast_detected		: std_logic;

	TYPE tx_state_t IS (IDLE, RECEIVING, RANDOMIZE, FEC_ENCODE, INTERLEAVE, SYNC_TX, DATA_TX);
	SIGNAL tx_state : tx_state_t := IDLE;

	TYPE frame_buffer_t IS ARRAY(0 TO OV_FRAME_BYTES-1) OF std_logic_vector(7 DOWNTO 0);
	SIGNAL ov_frame_buffer : frame_buffer_t;

	TYPE byte_buffer_t IS ARRAY(0 TO OV_FRAME_BYTES-1) OF std_logic_vector(7 DOWNTO 0);
	TYPE bit_buffer_t IS ARRAY(0 TO ENCODED_BITS-1) OF std_logic;
	SIGNAL input_buffer : byte_buffer_t;
	SIGNAL randomized_buffer : byte_buffer_t;
	SIGNAL fec_buffer : bit_buffer_t;
	SIGNAL interleaved_buffer : bit_buffer_t;

	-- 11 bit and 13 bit Barker Code concatenated to 24 bit sync word 0xE25F35 
	CONSTANT SYNC_PATTERN : std_logic_vector(SYNC_BITS-1 DOWNTO 0) := "000111011010000011001010";

	TYPE randomizer_t IS ARRAY(0 TO 133) OF std_logic_vector(7 DOWNTO 0);
	CONSTANT RANDOMIZER_SEQUENCE : randomizer_t := (
		x"A3", x"81", x"5C", x"C4", x"C9", x"08", x"0E", x"53",
		x"CC", x"A1", x"FB", x"29", x"9E", x"4F", x"16", x"E0",
		x"97", x"4E", x"2B", x"57", x"12", x"A7", x"3F", x"C2",
		x"4D", x"6B", x"0F", x"08", x"30", x"46", x"11", x"56",
		x"0D", x"1A", x"13", x"E7", x"50", x"97", x"61", x"F3",
		x"BE", x"E3", x"99", x"B0", x"64", x"39", x"22", x"2C",
		x"F0", x"09", x"E1", x"86", x"CF", x"73", x"59", x"C2",
		x"5C", x"8E", x"E3", x"D7", x"3F", x"70", x"D4", x"27",
		x"C2", x"E0", x"81", x"92", x"DA", x"FC", x"CA", x"5A",
		x"80", x"42", x"83", x"15", x"0F", x"A2", x"9E", x"15",
		x"9C", x"8B", x"DB", x"A4", x"46", x"1C", x"10", x"9F",
		x"B3", x"47", x"6C", x"5E", x"15", x"12", x"1F", x"AD",
		x"38", x"3D", x"03", x"BA", x"90", x"8D", x"BE", x"D3",
		x"65", x"23", x"32", x"B8", x"AB", x"10", x"62", x"7E",
		x"C6", x"26", x"7C", x"13", x"C9", x"65", x"3D", x"15",
		x"15", x"ED", x"35", x"F4", x"57", x"F5", x"58", x"11",
		x"9D", x"8E", x"E8", x"34", x"C9", x"59"
	);

	TYPE sync_state_t IS (HUNTING, LOCKED);
	SIGNAL sync_state           : sync_state_t := HUNTING;
	SIGNAL sync_shift_reg       : std_logic_vector(SYNC_BITS-1 DOWNTO 0);
	SIGNAL bit_counter          : NATURAL RANGE 0 TO ENCODED_BITS;
	
	SIGNAL bit_buffer           : bit_buffer_t;
	SIGNAL buffer_write_idx     : NATURAL RANGE 0 TO ENCODED_BITS-1;
	
	SIGNAL rx_fifo_wr_en           : std_logic;
	SIGNAL rx_fifo_full            : std_logic;
	SIGNAL frames_collected     : UNSIGNED(31 DOWNTO 0) := (OTHERS => '0');
	
	TYPE proc_state_t IS (IDLE, DEINTERLEAVE, FEC_DECODE, DERANDOMIZE, OUTPUT);
	SIGNAL proc_state           : proc_state_t := IDLE;
	
	SIGNAL encoded_buffer       : bit_buffer_t;
	SIGNAL deinterleaved_buffer : bit_buffer_t;
	SIGNAL fec_decoded_buffer   : byte_buffer_t;
	SIGNAL output_buffer        : byte_buffer_t;
	
	SIGNAL proc_bit_idx         : NATURAL RANGE 0 TO ENCODED_BITS;
	SIGNAL proc_byte_idx        : NATURAL RANGE 0 TO OV_FRAME_BYTES;
	
	SIGNAL rx_fifo_rd_en           : std_logic;
	SIGNAL rx_fifo_empty           : std_logic;
	SIGNAL rx_fifo_dout            : bit_buffer_t;
	SIGNAL rx_fifo_valid           : std_logic;
	
	SIGNAL frames_rx_count      : UNSIGNED(31 DOWNTO 0) := (OTHERS => '0');
	SIGNAL sync_err_count       : UNSIGNED(31 DOWNTO 0) := (OTHERS => '0');
	
	SIGNAL axi_valid_int        : std_logic := '0';
	SIGNAL axi_tlast_int        : std_logic := '0';

	SIGNAL framer_byte_index : NATURAL RANGE 0 TO OV_FRAME_BYTES;
	SIGNAL framer_bit_index : NATURAL RANGE 0 TO ENCODED_BITS;
	SIGNAL sync_index : NATURAL RANGE 0 TO SYNC_BITS;
	SIGNAL framer_frames_count : UNSIGNED(31 DOWNTO 0) := (OTHERS => '0');

	SIGNAL frame_ready : std_logic := '0';



        FUNCTION calc_hamming_distance(
                pattern1 : std_logic_vector;
                pattern2 : std_logic_vector
        ) RETURN NATURAL IS
                VARIABLE distance : NATURAL := 0;
        BEGIN   
                FOR i IN pattern1'RANGE LOOP
                        IF pattern1(i) /= pattern2(i) THEN
                                distance := distance + 1;
                        END IF;
                END LOOP;
                RETURN distance;
        END FUNCTION;  

	FUNCTION interleave_address(addr : NATURAL) RETURN NATURAL IS
		CONSTANT ROWS : NATURAL := 67;
		CONSTANT COLS : NATURAL := 32;
		VARIABLE row : NATURAL;
		VARIABLE col : NATURAL;
	BEGIN
		row := addr / COLS;
		col := addr MOD COLS;
		RETURN col * ROWS + row;
	END FUNCTION;

        FUNCTION deinterleave_address(addr : NATURAL) RETURN NATURAL IS
                CONSTANT ROWS : NATURAL := 67;
                CONSTANT COLS : NATURAL := 32;
                VARIABLE row : NATURAL;
                VARIABLE col : NATURAL;
        BEGIN
                row := addr MOD ROWS;                   
                col := addr / ROWS;
                RETURN row * COLS + col;
        END FUNCTION;
                        

BEGIN 

------------------------------------------------------------------------------------------------------
-- S-AXIS Interface with Async FIFO
------------------------------------------------------------------------------------------------------

	tx_samples_I 	<= tx_samples_I_int;
	tx_samples_Q 	<= tx_samples_Q_int;

	rx_samples_mux <= std_logic_vector(resize(signed(tx_samples_I_int), 16)) WHEN loopback_ena = '1' ELSE rx_samples_I;

	-- Async FIFO for clock domain crossing
	u_tx_fifo : ENTITY work.async_fifo
		GENERIC MAP (
			DATA_WIDTH => 8,
			ADDR_WIDTH => 8  -- up to 256 byte FIFO (almost 2 of current frame size)
		)
		PORT MAP (
			wr_clk => s_axis_aclk,
			wr_rst => NOT s_axis_aresetn,
			wr_en => fifo_wr_en,
			wr_data => fifo_wr_data,
			wr_tlast => fifo_wr_tlast,
			full => fifo_full,
			almost_full => fifo_almost_full,
			
			rd_clk => clk,
			rd_rst => txinit,
			rd_en => fifo_rd_en,
			rd_data => fifo_rd_data,
			rd_tlast => fifo_rd_tlast,
			empty => fifo_empty,
			almost_empty => fifo_almost_empty
		);

	-- Write side: simple AXI-Stream slave (s_axis_aclk domain)
	fifo_write_proc: PROCESS(s_axis_aclk)
	BEGIN
		IF rising_edge(s_axis_aclk) THEN
			IF s_axis_aresetn = '0' THEN
				s_axis_ready <= '0';
				fifo_wr_en <= '0';
				fifo_wr_data <= (OTHERS => '0');
				fifo_wr_tlast <= '0';
			ELSE
				-- Ready when FIFO not full
				s_axis_ready <= NOT fifo_full;
				
				-- Write to FIFO when valid data arrives
				IF s_axis_valid = '1' AND fifo_full = '0' THEN
					fifo_wr_en <=	 '1';
					fifo_wr_data <= s_axis_data(7 DOWNTO 0);  -- Take lowest byte
					fifo_wr_tlast <= s_axis_tlast; -- capture tlast
				ELSE
					fifo_wr_en <= '0';
					fifo_wr_tlast <= '0';
				END IF;
			END IF;
		END IF;
	END PROCESS;

------------------------------------------------------------------------------------------------------
-- Tx Framer State Machine (clk domain)
------------------------------------------------------------------------------------------------------

	tx_process : PROCESS(clk)
	BEGIN
		IF RISING_EDGE(clk) THEN
			IF txinit = '1' THEN
				tx_state <= IDLE;
				frame_start <= '0';
				frame_active <= '0';
				framer_frames_count <= (OTHERS => '0');
				framer_byte_index <= 0;
				framer_bit_index <= 0;
				sync_index <= 0;
				frame_ready <= '0';
				tlast_detected <= '0';
				fifo_rd_en <= '0';
				tx_data_bit <= '0';
				tx_data_bit_d1 <= '0';
				tx_data_bit_d2 <= '0';
				tx_data_bit_d3 <= '0';
				tx_data_bit_d4 <= '0';
			ELSE
				frame_start <= '0';
				fifo_rd_en <= '0';  -- Default
				
				CASE tx_state IS
					WHEN IDLE =>
						frame_active <= '0';
						framer_byte_index <= 0;
						tx_data_bit <= '0';
						
						IF fifo_empty = '0' THEN
							tx_state <= RECEIVING;
						END IF;



					WHEN RECEIVING =>
						tx_data_bit <= '0';  -- Keep this! Prevents spurious TX during processing
    
						-- Read from FIFO
						IF fifo_empty = '0' AND framer_byte_index < OV_FRAME_BYTES THEN
							fifo_rd_en <= '1';
							ov_frame_buffer(framer_byte_index) <= fifo_rd_data;
							framer_byte_index <= framer_byte_index + 1;
        
							-- Check for tlast indicating end of frame
							IF fifo_rd_tlast = '1' THEN
								-- Validate we got exactly the right number of bytes
								IF framer_byte_index + 1 = OV_FRAME_BYTES THEN
									-- Good frame!
									framer_byte_index <= 0;
									tx_state <= RANDOMIZE;
									frame_ready <= '1';
									frame_start <= '1';
									frame_active <= '1';
								ELSE
									-- Frame size mismatch - discard and start over
									framer_byte_index <= 0;
									tx_state <= IDLE;
									-- Could increment an error counter here
								END IF;
							END IF;
						END IF;



					WHEN RANDOMIZE =>
						tx_data_bit <= '0';
						
						IF framer_byte_index < OV_FRAME_BYTES THEN
							randomized_buffer(framer_byte_index) <= 
								ov_frame_buffer(framer_byte_index) XOR 
								RANDOMIZER_SEQUENCE(framer_byte_index);
							framer_byte_index <= framer_byte_index + 1;
						ELSE
							framer_byte_index <= 0;
							tx_state <= FEC_ENCODE;
						END IF;

					WHEN FEC_ENCODE =>
						tx_data_bit <= '0';
						
						IF framer_bit_index < OV_FRAME_BYTES * 8 THEN
							fec_buffer(framer_bit_index * 2) <= 
								randomized_buffer(framer_bit_index / 8)(framer_bit_index MOD 8);
							fec_buffer(framer_bit_index * 2 + 1) <= 
								randomized_buffer(framer_bit_index / 8)(framer_bit_index MOD 8);
							framer_bit_index <= framer_bit_index + 1;
						ELSE
							framer_bit_index <= 0;
							tx_state <= INTERLEAVE;
						END IF;

					WHEN INTERLEAVE =>
						tx_data_bit <= '0';
						
						IF framer_bit_index < ENCODED_BITS THEN
							interleaved_buffer(interleave_address(framer_bit_index)) <= 
								fec_buffer(framer_bit_index);
							framer_bit_index <= framer_bit_index + 1;
						ELSE
							framer_bit_index <= 0;
							tx_state <= SYNC_TX;
						END IF;

					WHEN SYNC_TX =>
						IF tx_req = '1' THEN
							tx_data_bit <= SYNC_PATTERN(SYNC_BITS - 1 - sync_index);
							
							tx_data_bit_d1 <= prbs_data_bit;
							tx_data_bit_d2 <= tx_data_bit_d1;
							tx_data_bit_d3 <= tx_data_bit_d2;
							tx_data_bit_d4 <= tx_data_bit_d3;
							
							rx_data_cmp <= rx_bit;
							data_error <= rx_data_cmp XOR tx_data_bit_d2;

							IF sync_index < SYNC_BITS - 1 THEN
								sync_index <= sync_index + 1;
							ELSE
								sync_index <= 0;
								framer_bit_index <= 0;
								tx_state <= DATA_TX;
							END IF;
						END IF;

					WHEN DATA_TX =>
						frame_active <= '0';
						
						IF tx_req = '1' THEN
							tx_data_bit <= interleaved_buffer(framer_bit_index);
							
							tx_data_bit_d1 <= prbs_data_bit;
							tx_data_bit_d2 <= tx_data_bit_d1;
							tx_data_bit_d3 <= tx_data_bit_d2;
							tx_data_bit_d4 <= tx_data_bit_d3;
							
							rx_data_cmp <= rx_bit;
							data_error <= rx_data_cmp XOR tx_data_bit_d2;

							IF framer_bit_index < ENCODED_BITS - 1 THEN
								framer_bit_index <= framer_bit_index + 1;
							ELSE
								framer_frames_count <= framer_frames_count + 1;
								framer_bit_index <= 0;
								tx_state <= IDLE;
							END IF;
						END IF;
				END CASE;
			END IF;
		END IF;
	END PROCESS tx_process;
	
	frames_processed <= std_logic_vector(framer_frames_count);

------------------------------------------------------------------------------------------------------
-- Rx Deframer
------------------------------------------------------------------------------------------------------

	sync_detector_proc: PROCESS(clk)
		VARIABLE hamming_dist : NATURAL RANGE 0 TO SYNC_BITS;
	BEGIN
		IF rising_edge(clk) THEN
			IF s_axis_aresetn = '0' THEN
				sync_state <= HUNTING;
				sync_shift_reg <= (OTHERS => '0');
				bit_counter <= 0;
				buffer_write_idx <= 0;
				rx_fifo_wr_en <= '0';
				frames_collected <= (OTHERS => '0');
				sync_locked <= '0';
			ELSE
				rx_fifo_wr_en <= '0';
				
				IF rx_bit_valid = '1' THEN
					sync_shift_reg <= sync_shift_reg(SYNC_BITS-2 DOWNTO 0) & rx_bit_corr;
					
					CASE sync_state IS
						WHEN HUNTING =>
							hamming_dist := calc_hamming_distance(sync_shift_reg, SYNC_PATTERN);
							
							IF hamming_dist <= SYNC_THRESHOLD THEN
								sync_state <= LOCKED;
								sync_locked <= '1';
								bit_counter <= 0;
								buffer_write_idx <= 0;
							END IF;
							
						WHEN LOCKED =>
							bit_buffer(buffer_write_idx) <= rx_bit_corr;
							
							IF buffer_write_idx < ENCODED_BITS - 1 THEN
								buffer_write_idx <= buffer_write_idx + 1;
							ELSE
								IF rx_fifo_full = '0' THEN
									rx_fifo_wr_en <= '1';
									frames_collected <= frames_collected + 1;
								ELSE
									sync_err_count <= sync_err_count + 1;
									fifo_overflow <= '1';
								END IF;
								
								sync_state <= HUNTING;
								sync_locked <= '0';
								buffer_write_idx <= 0;
							END IF;
					END CASE;
				END IF;
			END IF;
		END IF;
	END PROCESS;

	frame_fifo_proc: PROCESS(clk)
		TYPE fifo_array_t IS ARRAY(0 TO FIFO_DEPTH-1) OF bit_buffer_t;
		VARIABLE fifo_mem : fifo_array_t;
		VARIABLE wr_ptr : NATURAL RANGE 0 TO FIFO_DEPTH-1 := 0;
		VARIABLE rd_ptr : NATURAL RANGE 0 TO FIFO_DEPTH-1 := 0;
		VARIABLE count : NATURAL RANGE 0 TO FIFO_DEPTH := 0;
	BEGIN
		IF rising_edge(clk) THEN
			IF s_axis_aresetn = '0' THEN
				wr_ptr := 0;
				rd_ptr := 0;
				count := 0;
				rx_fifo_empty <= '1';
				rx_fifo_full <= '0';
				rx_fifo_valid <= '0';
			ELSE
				rx_fifo_valid <= '0';
				
				IF rx_fifo_wr_en = '1' AND count < FIFO_DEPTH THEN
					fifo_mem(wr_ptr) := bit_buffer;
					IF wr_ptr < FIFO_DEPTH-1 THEN
						wr_ptr := wr_ptr + 1;
					ELSE
						wr_ptr := 0;
					END IF;
					count := count + 1;
				END IF;
				
				IF rx_fifo_rd_en = '1' AND count > 0 THEN
					rx_fifo_dout <= fifo_mem(rd_ptr);
					rx_fifo_valid <= '1';
					IF rd_ptr < FIFO_DEPTH-1 THEN
						rd_ptr := rd_ptr + 1;
					ELSE
						rd_ptr := 0;
					END IF;
					count := count - 1;
				END IF;
				
				IF count = 0 THEN
					rx_fifo_empty <= '1';
				ELSE
					rx_fifo_empty <= '0';
				END IF;
				
				IF count = FIFO_DEPTH THEN
					rx_fifo_full <= '1';
				ELSE
					rx_fifo_full <= '0';
				END IF;
			END IF;
		END IF;
	END PROCESS;

	frame_processor_proc: PROCESS(clk)
	BEGIN
		IF rising_edge(clk) THEN
			IF s_axis_aresetn = '0' THEN
				proc_state <= IDLE;
				rx_fifo_rd_en <= '0';
				proc_bit_idx <= 0;
				proc_byte_idx <= 0;
				frames_rx_count <= (OTHERS => '0');
				axi_valid_int <= '0';
				axi_tlast_int <= '0';
			ELSE
				CASE proc_state IS
					WHEN IDLE =>
						rx_fifo_rd_en <= '0';
						
						IF rx_fifo_empty = '0' THEN
							rx_fifo_rd_en <= '1';
							proc_state <= DEINTERLEAVE;
							proc_bit_idx <= 0;
						END IF;
						
					WHEN DEINTERLEAVE =>
						IF rx_fifo_valid = '1' THEN
							encoded_buffer <= rx_fifo_dout;
							proc_bit_idx <= 0;
						END IF;
						
						IF proc_bit_idx < ENCODED_BITS THEN
							deinterleaved_buffer(deinterleave_address(proc_bit_idx)) <= 
								encoded_buffer(proc_bit_idx);
							proc_bit_idx <= proc_bit_idx + 1;
						ELSE
							proc_bit_idx <= 0;
							proc_state <= FEC_DECODE;
						END IF;
						
					WHEN FEC_DECODE =>
						IF proc_bit_idx < OV_FRAME_BYTES * 8 THEN
							fec_decoded_buffer(proc_bit_idx / 8)(proc_bit_idx MOD 8) <= 
								deinterleaved_buffer(proc_bit_idx * 2);
							proc_bit_idx <= proc_bit_idx + 1;
						ELSE
							proc_byte_idx <= 0;
							proc_state <= DERANDOMIZE;
						END IF;
						
					WHEN DERANDOMIZE =>
						IF proc_byte_idx < OV_FRAME_BYTES THEN
							output_buffer(proc_byte_idx) <= 
								fec_decoded_buffer(proc_byte_idx) XOR 
								RANDOMIZER_SEQUENCE(proc_byte_idx);
							proc_byte_idx <= proc_byte_idx + 1;
						ELSE
							proc_byte_idx <= 0;
							proc_state <= OUTPUT;
						END IF;
						
					WHEN OUTPUT =>
						IF m_axis_tready = '1' OR axi_valid_int = '0' THEN
							IF proc_byte_idx < OV_FRAME_BYTES THEN
								m_axis_tdata <= (OTHERS => '0');
								m_axis_tdata(7 DOWNTO 0) <= output_buffer(proc_byte_idx);
								axi_valid_int <= '1';
								
								IF proc_byte_idx = OV_FRAME_BYTES - 1 THEN
									axi_tlast_int <= '1';
								ELSE
									axi_tlast_int <= '0';
								END IF;
								
								proc_byte_idx <= proc_byte_idx + 1;
							ELSE
								axi_valid_int <= '0';
								axi_tlast_int <= '0';
								frames_rx_count <= frames_rx_count + 1;
								proc_state <= IDLE;
							END IF;
						END IF;
				END CASE;
			END IF;
		END IF;
	END PROCESS;

	m_axis_tvalid <= axi_valid_int;
	m_axis_tlast <= axi_tlast_int;
	frames_received <= std_logic_vector(frames_rx_count);
	sync_errors <= std_logic_vector(sync_err_count);

------------------------------------------------------------------------------------------------------
-- PRBS Generator
------------------------------------------------------------------------------------------------------

	u_prbs_gen : ENTITY work.prbs_gen(rtl)
		GENERIC MAP (
			DATA_W => DATA_W,
			GENERATOR_W => GENERATOR_W,
			TOGGLE_CONTROL => True
		)
		PORT MAP (
			clk => clk,
			init => txinit,
			initial_state => prbs_initial(GENERATOR_W -1 DOWNTO 0),
			polynomial => prbs_poly(GENERATOR_W -1 DOWNTO 0),
			error_insert => prbs_err_insert,
			error_mask => prbs_err_mask(1 -1 DOWNTO 0),
			prbs_sel => prbs_sel,
			data_in(0) => tx_data_bit,
			data_req => tx_req,
			data_out(0) => prbs_data_bit
		);

------------------------------------------------------------------------------------------------------
-- MSK Modulator
------------------------------------------------------------------------------------------------------

	u_mod : ENTITY work.msk_modulator(rtl)
		GENERIC MAP (
			NCO_W => NCO_W,
			PHASE_W => PHASE_W,
			SINUSOID_W => SINUSOID_W,
			SAMPLE_W => SAMPLE_W,
			SYNC_CNT_W => SYNC_CNT_W
		)
		PORT MAP (
			clk => clk,
			init => txinit,
			freq_word_tclk => freq_word_ft,
			freq_word_f1 => freq_word_tx_f1,
			freq_word_f2 => freq_word_tx_f2,
			ptt => ptt,
			tx_sync_ena => tx_sync_ena,
			tx_sync_cnt => tx_sync_cnt,
			tx_sync_force => tx_sync_force,
			tx_data => prbs_data_bit,
			tx_req => tx_req,
			tx_enable => tx_enable OR loopback_ena,
			tx_valid => tx_valid OR loopback_ena,
			tx_samples_I => tx_samples_I_int,
			tx_samples_Q => tx_samples_Q_int
		);

------------------------------------------------------------------------------------------------------
-- MSK Demodulator
------------------------------------------------------------------------------------------------------

	rx_bit_corr <= rx_bit WHEN rx_invert = '0' ELSE NOT rx_bit;

	u_discard : PROCESS (clk)
	BEGIN
		IF clk'EVENT AND clk = '1' THEN
			IF rxinit = '1' THEN
				discard_count <= (OTHERS => '0');
				rx_samples_dec <= (OTHERS => '0');
			ELSE
				IF to_integer(discard_count) = 0 AND (rx_svalid = '1' OR loopback_ena = '1') THEN 
					discard_count <= unsigned(discard_rxsamples);
					rx_samples_dec <= rx_samples_mux(11 DOWNTO 0);
					rx_sample_clk <= '1';
				ELSE
					discard_count <= discard_count -1;
					rx_sample_clk <= '0';
				END IF;
			END IF;
		END IF;
	END PROCESS u_discard;

	u_dem : ENTITY work.msk_demodulator(rtl)
		GENERIC MAP (
			NCO_W => NCO_W,
			ACC_W => ACC_W,
			PHASE_W => PHASE_W,
			SINUSOID_W => SINUSOID_W,
			GAIN_W => GAIN_W,
			SHIFT_W => SHIFT_W,
			SAMPLE_W => 12
		)
		PORT MAP (
			clk => clk,
			init => rxinit,
			rx_freq_word_f1 => freq_word_rx_f1,
			rx_freq_word_f2 => freq_word_rx_f2,
			discard_rxnco => discard_rxnco,
			lpf_p_gain => lpf_p_gain,
			lpf_i_gain => lpf_i_gain,
			lpf_i_shift => lpf_i_shift,
			lpf_p_shift => lpf_p_shift,
			lpf_freeze => lpf_freeze,
			lpf_zero => lpf_zero,
			lpf_alpha => lpf_alpha,
			lpf_accum_f1 => lpf_accum_f1,
			lpf_accum_f2 => lpf_accum_f2,
			f1_nco_adjust => f1_nco_adjust,
			f2_nco_adjust => f2_nco_adjust,
			f1_error => f1_error,
			f2_error => f2_error,
			rx_enable => rx_enable OR loopback_ena,
			rx_svalid => rx_sample_clk,
			rx_samples => rx_samples_dec(11 DOWNTO 0),
			rx_data => rx_bit,
			rx_dvalid => rx_bit_valid
		);

------------------------------------------------------------------------------------------------------
-- PRBS Monitor
------------------------------------------------------------------------------------------------------

	u_prbs_mon : ENTITY work.prbs_mon(rtl)
		GENERIC MAP (
			DATA_W => DATA_W,
			GENERATOR_W => GENERATOR_W,
			COUNTER_W => COUNTER_W,
			TOGGLE_CONTROL => True
		)
		PORT MAP (
			clk => clk,
			init => rxinit,
			sync_manual => prbs_manual_sync,
			sync_threshold => prbs_sync_threshold,
			initial_state => prbs_initial(GENERATOR_W -1 DOWNTO 0),
			polynomial => prbs_poly(GENERATOR_W -1 DOWNTO 0),
			count_reset => prbs_clear,
			data_count => prbs_bits,
			error_count => prbs_errs,
			data_in(0) => rx_bit_corr,
			data_in_valid => rx_bit_valid
		);

------------------------------------------------------------------------------------------------------
-- Power Detector
------------------------------------------------------------------------------------------------------

	u_power_det : ENTITY work.power_detector(rtl)
		GENERIC MAP (
			DATA_W => 12,
			ALPHA_W => 18,
			IQ_MOD => True,
			I_USED => False,
			Q_USED => False,
			EMA_CASCADE => False
		)
		PORT MAP (
			clk => clk,
			init => rxinit,
			alpha1 => pd_alpha1,
			alpha2 => pd_alpha2,
			data_I => rx_samples_I(15 DOWNTO 4),
			data_Q => rx_samples_Q(15 DOWNTO 4),
			data_ena => rx_svalid,
			power_squared => pd_power
		);

------------------------------------------------------------------------------------------------------
-- Config/Status
------------------------------------------------------------------------------------------------------

	demod_sync_lock <= '0';

	stats_proc : PROCESS (clk)
	BEGIN
		IF clk'EVENT AND clk = '1' THEN 
			IF tx_enable = '1' THEN
				tx_bit_counter <= tx_bit_counter + 1;
				tx_ena_counter <= tx_ena_counter + 1;
			ELSE
				tx_ena_counter <= tx_ena_counter - 1;
			END IF; 

			tx_axis_valid_meta <= fifo_wr_en;
			tx_axis_valid_sync <= tx_axis_valid_meta;

			IF txinit = '1' THEN
				tx_bit_counter <= (OTHERS => '0');
				tx_ena_counter <= (OTHERS => '0');
				tx_axis_valid_meta <= '0';
				tx_axis_valid_sync <= '0';
			END IF;
		END IF;
	END PROCESS stats_proc;

	u_msk_top_csr : ENTITY work.msk_top_csr(rtl)
		GENERIC MAP (
			HASH_ID_LO => HASH_ID_LO,
			HASH_ID_HI => HASH_ID_HI,
			GAIN_W => GAIN_W,
			NCO_W => NCO_W,
			ACC_W => ACC_W,
			COUNTER_W => 32,
			GENERATOR_W => 32,
			C_S_AXI_DATA_WIDTH => C_S_AXI_DATA_WIDTH,
			C_S_AXI_ADDR_WIDTH => C_S_AXI_ADDR_WIDTH,
			SYNC_CNT_W => SYNC_CNT_W
		)
		PORT MAP (
			clk => clk,
			s_axi_aclk => s_axi_aclk,
			s_axi_aresetn => s_axi_aresetn,
			s_axi_awaddr => s_axi_awaddr,
			s_axi_awvalid => s_axi_awvalid,
			s_axi_wdata => s_axi_wdata,
			s_axi_wstrb => s_axi_wstrb,
			s_axi_wvalid => s_axi_wvalid,
			s_axi_bready => s_axi_bready,
			s_axi_araddr => s_axi_araddr,
			s_axi_arvalid => s_axi_arvalid,
			s_axi_rready => s_axi_rready,
			s_axi_arready => s_axi_arready,
			s_axi_rdata => s_axi_rdata,
			s_axi_rresp => s_axi_rresp,
			s_axi_rvalid => s_axi_rvalid,
			s_axi_wready => s_axi_wready,
			s_axi_bresp => s_axi_bresp,
			s_axi_bvalid => s_axi_bvalid,
			s_axi_awready => s_axi_awready,
			s_axi_awprot => s_axi_awprot,
			s_axi_arprot => s_axi_arprot,
			tx_enable => tx_enable,
			rx_enable => rx_enable,
			demod_sync_lock => demod_sync_lock,
			tx_req => tx_req,
			tx_axis_valid => tx_axis_valid_sync,
			xfer_count => std_logic_vector(to_unsigned(0, COUNTER_W)),
			tx_bit_counter => std_logic_vector(tx_bit_counter),
			tx_ena_counter => std_logic_vector(tx_ena_counter),
			prbs_bits => prbs_bits,
			prbs_errs => prbs_errs,
			lpf_accum_f1 => lpf_accum_f1,
			lpf_accum_f2 => lpf_accum_f2,
			f1_nco_adjust => f1_nco_adjust,
			f2_nco_adjust => f2_nco_adjust,
			f1_error => f1_error,
			f2_error => f2_error,
			txinit => txinit,
			rxinit => rxinit,
			ptt => ptt,
			loopback_ena => loopback_ena,
			rx_invert => rx_invert,
			clear_counts => clear_counts,
			discard_rxsamples => discard_rxsamples,
			discard_rxnco => discard_rxnco,
			freq_word_ft => freq_word_ft,
			freq_word_tx_f1 => freq_word_tx_f1,
			freq_word_tx_f2 => freq_word_tx_f2,
			freq_word_rx_f1 => freq_word_rx_f1,
			freq_word_rx_f2 => freq_word_rx_f2,
			lpf_freeze => lpf_freeze,
			lpf_zero => lpf_zero,
			lpf_alpha => lpf_alpha,
			lpf_i_gain => lpf_i_gain,
			lpf_p_gain => lpf_p_gain,
			lpf_i_shift => lpf_i_shift,
			lpf_p_shift => lpf_p_shift,
			tx_data_w => tx_data_w,
			rx_data_w => rx_data_w,
			prbs_manual_sync => prbs_manual_sync,
			prbs_initial => prbs_initial,
			prbs_poly => prbs_poly,
			prbs_err_insert => prbs_err_insert,
			prbs_err_mask => prbs_err_mask,
			prbs_sel => prbs_sel,
			prbs_clear => prbs_clear,
			prbs_sync_threshold => prbs_sync_threshold,
			tx_sync_ena => tx_sync_ena,
			tx_sync_cnt => tx_sync_cnt,
			tx_sync_force => tx_sync_force,
			tx_sync_f1 => tx_sync_f1,
			tx_sync_f2 => tx_sync_f2,
			pd_alpha1 => pd_alpha1,
			pd_alpha2 => pd_alpha2,
			pd_power => pd_power
		);

END ARCHITECTURE struct;

