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
		GAIN_W 				: NATURAL := 24;
		SHIFT_W 			: NATURAL := 8;
		SYNC_W 				: NATURAL := 16;
		GENERATOR_W 			: NATURAL := 31;
		COUNTER_W 			: NATURAL := 32;
		DATA_W 				: NATURAL := 1;
		S_AXIS_DATA_W 			: NATURAL := 32;	-- AXI stream width changed from 64 Abraxas3d(!!!)
		C_S_AXI_DATA_WIDTH		: NATURAL := 32;
		C_S_AXI_ADDR_WIDTH		: NATURAL := 32;
		SYNC_CNT_W 			: NATURAL := 24;
		OV_FRAME_BYTES 			: NATURAL := 134;	-- Opulent Voice frame size in bytes
		SYNC_BITS 			: NATURAL := 24;	-- Barker code sync length in bits
		ENCODED_BITS 			: NATURAL := 2144;	-- Number of encoded bits after rate 1/2 FEC encoding
		INTERLEAVER_DEPTH 		: NATURAL := 2144	-- Interleaver depth in bits


	);
	PORT (
		clk 			: IN  std_logic;

		s_axi_aclk		: in  std_logic;
		s_axi_aresetn		: in  std_logic;
		s_axi_awaddr		: in  std_logic_vector(C_S_AXI_ADDR_WIDTH-1 downto 0);
		s_axi_awvalid		: in  std_logic;
		s_axi_wdata		: in  std_logic_vector(C_S_AXI_DATA_WIDTH-1 downto 0);
		s_axi_wstrb		: in  std_logic_vector((C_S_AXI_DATA_WIDTH/8)-1 downto 0);
		s_axi_wvalid		: in  std_logic;
		s_axi_bready		: in  std_logic;
		s_axi_araddr		: in  std_logic_vector(C_S_AXI_ADDR_WIDTH-1 downto 0);
		s_axi_arvalid		: in  std_logic;
		s_axi_rready		: in  std_logic;
		s_axi_arready		: out std_logic;
		s_axi_rdata		: out std_logic_vector(C_S_AXI_DATA_WIDTH-1 downto 0);
		s_axi_rresp		: out std_logic_vector(1 downto 0);
		s_axi_rvalid		: out std_logic;
		s_axi_wready		: out std_logic;
		s_axi_bresp		: out std_logic_vector(1 downto 0);
		s_axi_bvalid		: out std_logic;
		s_axi_awready		: out std_logic;
		s_axi_awprot 		: in  std_logic_vector(2 DOWNTO 0);
		s_axi_arprot 		: in  std_logic_vector(2 DOWNTO 0);

		s_axis_aresetn 		: IN  std_logic;
		s_axis_aclk 		: IN  std_logic;
		s_axis_valid 		: IN  std_logic;
		s_axis_ready    	: OUT std_logic;
		s_axis_data		: IN  std_logic_vector(S_AXIS_DATA_W -1 DOWNTO 0);
		s_axis_tlast		: IN  std_logic; -- Frame boundary from Dialogus
		s_axis_tkeep		: IN  std_logic_vector(S_AXIS_DATA_W/8-1 DOWNTO 0);

		tx_enable 		: IN std_logic;
		tx_valid 		: IN std_logic;
		tx_samples_I		: OUT std_logic_vector(SAMPLE_W -1 DOWNTO 0);
		tx_samples_Q		: OUT std_logic_vector(SAMPLE_W -1 DOWNTO 0);

		rx_enable 		: IN std_logic;
		rx_svalid 		: IN std_logic;
		rx_samples_I		: IN  std_logic_vector(SAMPLE_W -1 DOWNTO 0);
		rx_samples_Q		: IN  std_logic_vector(SAMPLE_W -1 DOWNTO 0);

		rx_dvalid 		: OUT std_logic;
		rx_data 		: OUT std_logic_vector(S_AXIS_DATA_W -1 DOWNTO 0);

		frame_start		: OUT std_logic;
		frame_active		: OUT std_logic; 
		frames_processed	: OUT std_logic_vector(31 DOWNTO 0)

		
	);
END ENTITY msk_top;


------------------------------------------------------------------------------------------------------
-- ╔═╗┬─┐┌─┐┬ ┬┬┌┬┐┌─┐┌─┐┌┬┐┬ ┬┬─┐┌─┐
-- ╠═╣├┬┘│  ├─┤│ │ ├┤ │   │ │ │├┬┘├┤ 
-- ╩ ╩┴└─└─┘┴ ┴┴ ┴ └─┘└─┘ ┴ └─┘┴└─└─┘
------------------------------------------------------------------------------------------------------
-- Architecture

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

	SIGNAL s_axis_tready_int: std_logic;
	SIGNAL rx_bit		: std_logic;
	SIGNAL rx_bit_corr	: std_logic;
	SIGNAL rx_bit_valid	: std_logic;
	SIGNAL rx_bit_index	: NATURAL RANGE 0 TO S_AXIS_DATA_W -1;
	SIGNAL rx_data_valid	: std_logic;
	SIGNAL rx_data_int	: std_logic_vector(S_AXIS_DATA_W -1 DOWNTO 0);
	SIGNAL rx_invert	: std_logic;

	SIGNAL rx_sample_clk	: std_logic;
	SIGNAL discard_rxsamples: std_logic_vector(7 DOWNTO 0);
	SIGNAL discard_rxnco	: std_logic_vector(7 DOWNTO 0);

	SIGNAL rx_data_cmp	: std_logic;
	SIGNAL data_error	: std_logic;

	SIGNAL sent_data	: std_logic;
	SIGNAL received_data	: std_logic;
	SIGNAL sent_data_pipe	: std_logic_vector(0 TO 3);

	SIGNAL bit_index	: NATURAL RANGE 0 TO S_AXIS_DATA_W -1;
	SIGNAL tx_data		: std_logic_vector(S_AXIS_DATA_W -1 DOWNTO 0);
	SIGNAL tx_data_axi	: std_logic_vector(S_AXIS_DATA_W -1 DOWNTO 0);

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

	SIGNAL saxis_req	: std_logic;
	SIGNAL saxis_req_meta	: std_logic;
	SIGNAL saxis_req_sync	: std_logic;
	SIGNAL saxis_req_d	: std_logic;
	SIGNAL saxis_xfer_count : unsigned(COUNTER_W -1 DOWNTO 0);
	SIGNAL xfer_count	: unsigned(COUNTER_W -1 DOWNTO 0);

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

	SIGNAL s_axis_tlast_axi		: std_logic;
	SIGNAL s_axis_tlast_meta	: std_logic;
	SIGNAL s_axis_tlast_sync	: std_logic;


        -- State machine for frame processing
        TYPE tx_state_t IS (IDLE, RECEIVING, FEC_ENCODE, INTERLEAVE, RANDOMIZE, SYNC_TX, DATA_TX);
        SIGNAL tx_state : tx_state_t := IDLE;

        -- Frame buffers
        TYPE frame_buffer_t IS ARRAY(0 TO OV_FRAME_BYTES-1) OF std_logic_vector(7 DOWNTO 0);
        SIGNAL ov_frame_buffer : frame_buffer_t;

        -- Processing buffers - each sized for its stage
        TYPE byte_buffer_t IS ARRAY(0 TO OV_FRAME_BYTES-1) OF std_logic_vector(7 DOWNTO 0);
        TYPE bit_buffer_t IS ARRAY(0 TO ENCODED_BITS-1) OF std_logic;
        SIGNAL input_buffer : byte_buffer_t; -- 134 bytes frame input buffer
        SIGNAL randomized_buffer : byte_buffer_t; -- 134 bytes (after randomization)
        SIGNAL fec_buffer : bit_buffer_t; -- 2144 bits (after 1/2 rate forward error correction)
        SIGNAL interleaved_buffer : bit_buffer_t; -- 2144 bits (ready for TX)

        -- Sync pattern (E2 5F 35 hex = 11101001011111100110101 binary)
        CONSTANT SYNC_PATTERN : std_logic_vector(SYNC_BITS-1 DOWNTO 0) := "111010010111111001101101";

        -- Randomization sequence (134 bytes)
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


        -- Counters and indices
        SIGNAL byte_index : NATURAL RANGE 0 TO OV_FRAME_BYTES;
        SIGNAL framer_bit_index : NATURAL RANGE 0 TO ENCODED_BITS;
        SIGNAL sync_index : NATURAL RANGE 0 TO SYNC_BITS;
        SIGNAL frames_count : UNSIGNED(31 DOWNTO 0) := (OTHERS => '0');

        -- Control signals
        SIGNAL frame_ready : std_logic := '0';
        SIGNAL processing_done : std_logic := '0';

        -- FEC encoder signals (simplified - actual implementation will be more complex)
        SIGNAL fec_encode_active : std_logic := '0';
        SIGNAL fec_encode_done : std_logic := '0';

        -- Block interleaver: 67 rows × 32 cols = 2144 bits
        FUNCTION interleave_address(addr : NATURAL) RETURN NATURAL IS
                CONSTANT ROWS : NATURAL := 67;
                CONSTANT COLS : NATURAL := 32;
                VARIABLE row : NATURAL;
                VARIABLE col : NATURAL;
        BEGIN
                -- Write row-wise (normal order)
                row := addr / COLS;
                col := addr MOD COLS;
                -- Read column-wise (interleaved order)
                RETURN col * ROWS + row;
        END FUNCTION;

       -- Deinterleaver (for RX side)
        FUNCTION deinterleave_address(addr : NATURAL) RETURN NATURAL IS
                CONSTANT ROWS : NATURAL := 67;
                CONSTANT COLS : NATURAL := 32;
                VARIABLE row : NATURAL;
                VARIABLE col : NATURAL;
        BEGIN
                -- Reverse: what was read column-wise, write row-wise
                row := addr MOD ROWS;
                col := addr / ROWS;
                RETURN row * COLS + col;
        END FUNCTION;


        -- Data flow:
        --      [IDLE]
        -- ov_frame_buffer (134 bytes)
        --      [RANDOMIZE]
        -- randomized_buffer (134 bytes)
        --      [FEC_ENCODE]
        -- fec_buffer (2144 bits)
        --      [INTERLEAVE]
        -- interleaved_buffer (2144 bits)
        --      [SYNC_TX + DATA_TX]
        -- tx_data (1 bit at a time)
        --      [TX]






BEGIN 

------------------------------------------------------------------------------------------------------
--  __                 __          ___  __  __   __       __  __ 
-- (_   __  /\  \_/ | (_    | |\ |  |  |_  |__) |_   /\  /   |_  
-- __)     /--\ / \ | __)   | | \|  |  |__ | \  |   /--\ \__ |__ 
--                                                               
------------------------------------------------------------------------------------------------------
-- S-AXIS Interface

	s_axis_ready	<= s_axis_tready_int;

	tx_samples_I 	<= tx_samples_I_int;
	tx_samples_Q 	<= tx_samples_Q_int;

	rx_samples_mux <= std_logic_vector(resize(signed(tx_samples_I_int), 16)) WHEN loopback_ena = '1' ELSE rx_samples_I;

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
				s_axis_tlast_axi	<= s_axis_tlast;  -- Capture tlast
				saxis_xfer_count 	<= saxis_xfer_count + 1;
			END IF;

			IF s_axis_aresetn = '0' THEN
				s_axis_tready_int	<= '0';
				tx_data_axi 		<= (OTHERS => '0');
				s_axis_tlast_axi	<= '0';
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




	-- Main state machine
	tx_process : PROCESS(clk)
	BEGIN
		IF RISING_EDGE(clk) THEN
			-- two-stage synchonizer for tlast
			s_axis_tlast_meta <= s_axis_tlast_axi;
			s_axis_tlast_sync <= s_axis_tlast_meta;

			-- check for system reset
			IF s_axis_aresetn = '0' THEN
				tx_state <= IDLE;
				frame_start <= '0';
				frame_active <= '0';
				frames_count <= (OTHERS => '0');
				byte_index <= 0;
				framer_bit_index <= 0;
				sync_index <= 0;
				frame_ready <= '0';
				saxis_req <= '0';
				--processing_done <= '0';
				s_axis_tlast_meta <= '0';
				s_axis_tlast_sync <= '0';

			-- check for transmitter reset
			ELSIF txinit = '1' THEN
                                tx_state <= IDLE;
                                saxis_req <= '0';
                                frame_start <= '0';
                                frame_active <= '0';
                                frames_count <= (OTHERS => '0');
                                byte_index <= 0;
                                framer_bit_index <= 0;
				sync_index <= 0;
                                tx_data_bit <= '0';
                                tx_data_bit_d1 <= '0';
                                tx_data_bit_d2 <= '0';
                                tx_data_bit_d3 <= '0';
				tx_data_bit_d4 <= '0';
                                xfer_count <= (OTHERS => '0');
				s_axis_tlast_meta <= '0';
				s_axis_tlast_sync <= '0';
			-- default signal values
			ELSE
				frame_start <= '0';

				-- switch case structure implements state machine
				CASE tx_state IS
					WHEN IDLE =>
						frame_active <= '0';
						byte_index <= 0;

						-- request first word from AXI stream via CDC
						saxis_req <= NOT saxis_req;
						tx_state <= RECEIVING;

					WHEN RECEIVING =>
						-- Wait for synchronized data to arrive
						-- Only the lowest byte (7:0) contains valid data per transfer
    
						IF saxis_xfer_count /= xfer_count THEN
							-- New data has arrived in tx_data_axi
							xfer_count <= saxis_xfer_count;
        
							-- Extract only the lowest byte
							IF byte_index < OV_FRAME_BYTES THEN
								ov_frame_buffer(byte_index) <= tx_data_axi(7 DOWNTO 0);
								byte_index <= byte_index + 1;
							END IF;
        
							-- Check for frame completion via tlast
							IF s_axis_tlast_sync = '1' THEN
								-- Validate we got expected frame size
								IF byte_index = OV_FRAME_BYTES THEN
									-- Good frame! proceed to processing
									byte_index <= 0;
									tx_state <= RANDOMIZE;
									frame_ready <= '1';
									frame_start <= '1';
								ELSE
									-- Frame size mismatch - could add error handling here
									-- For now, just reset and try again
									byte_index <= 0;
									tx_state <= IDLE;
								END IF;
							ELSE
								-- Not done yet, request next byte
								saxis_req <= NOT saxis_req;
							END IF;
						END IF;

					WHEN RANDOMIZE =>
						-- XOR by predefined pseudorandom sequence
						-- This breaks up long strings of zeros or ones
						
						IF byte_index < OV_FRAME_BYTES THEN
							randomized_buffer(byte_index) <= ov_frame_buffer(byte_index) XOR RANDOMIZER_SEQUENCE(byte_index);
							byte_index <= byte_index + 1;
						ELSE
							byte_index <= 0;
							tx_state <= FEC_ENCODE; -- Next: add redundancy
						END IF;

					WHEN FEC_ENCODE =>
						-- Simplified FEC encoding (1/2 rate convolutional)
						-- In our implementation, this will be a separate module
						-- For now, just copy and duplicate bits (placeholder)
						
						IF framer_bit_index < OV_FRAME_BYTES * 8 THEN
							fec_buffer(framer_bit_index * 2) <= randomized_buffer(framer_bit_index / 8)(framer_bit_index MOD 8);
							fec_buffer(framer_bit_index * 2 + 1) <= randomized_buffer(framer_bit_index / 8)(framer_bit_index MOD 8);
							framer_bit_index <= framer_bit_index + 1;
						ELSE
							framer_bit_index <= 0;
							tx_state <= INTERLEAVE; -- Next: burst defense
						END IF;

					WHEN INTERLEAVE =>
						-- Apply block interleaver
						IF framer_bit_index < ENCODED_BITS THEN
							interleaved_buffer(interleave_address(framer_bit_index)) <= fec_buffer(framer_bit_index);
							framer_bit_index <= framer_bit_index + 1;
						ELSE
							framer_bit_index <= 0;
							tx_state <= SYNC_TX; -- Next: install lighthouse
						END IF;

					WHEN SYNC_TX =>
						-- Transmit sync pattern
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
								tx_state <= DATA_TX; -- Next: out the door
							END IF;
						END IF;

					WHEN DATA_TX =>
						-- Transmit processed data
						IF tx_req = '1' THEN
							tx_data_bit <= interleaved_buffer(framer_bit_index);

							tx_data_bit_d1 <= prbs_data_bit;
							tx_data_bit_d2 <= tx_data_bit_d1;
							tx_data_bit_d3 <= tx_data_bit_d2;
							tx_data_bit_d4 <= tx_data_bit_d3;

							rx_data_cmp    <= rx_bit;
							data_error         <= rx_data_cmp XOR tx_data_bit_d2;

							IF framer_bit_index < ENCODED_BITS - 1 THEN
								framer_bit_index <= framer_bit_index + 1;
							ELSE
								-- Frame transmission complete
								frames_count <= frames_count + 1;
								frame_active <= '0';
								tx_data <= tx_data_axi;
								framer_bit_index <= 0;
								saxis_req <= NOT saxis_req;
								xfer_count <= saxis_xfer_count;
								tx_state <= IDLE;
							END IF;
						END IF;
				END CASE; -- tx_state
			END IF; -- s_axis_aresetn
		END IF; -- rising edge of clock
	END PROCESS tx_process;
	
	-- Output assignments
	frames_processed <= std_logic_vector(frames_count);








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

			tx_enable 		=> tx_enable OR loopback_ena,
			tx_valid 		=> tx_valid OR loopback_ena,
			tx_samples_I	=> tx_samples_I_int,
			tx_samples_Q	=> tx_samples_Q_int
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

			IF rxinit = '1' THEN
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

			rx_enable 		=> rx_enable OR loopback_ena,
			rx_svalid 		=> rx_sample_clk,
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
--  __   __        ___  __      __   ___ ___  ___  __  ___  __   __  
-- |__) /  \ |  | |__  |__)    |  \ |__   |  |__  /  `  |  /  \ |__) 
-- |    \__/ |/\| |___ |  \    |__/ |___  |  |___ \__,  |  \__/ |  \ 
--                                                                  
------------------------------------------------------------------------------------------------------
-- PRBS GEN/MON

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

			IF txinit = '1' THEN
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
		tx_axis_valid 	=> tx_axis_valid_sync,
		xfer_count 		=> std_logic_vector(xfer_count),
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
