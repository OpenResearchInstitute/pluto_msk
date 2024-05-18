

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.numeric_std.ALL;

ENTITY msk_top IS 
	GENERIC (
		NCO_W 			: NATURAL := 32;
		PHASE_W 		: NATURAL := 10;
		SINUSOID_W 		: NATURAL := 12;
		SAMPLE_W 		: NATURAL := 12;
		GAIN_W 			: NATURAL := 16
	);
	PORT (
		clk 			: IN  std_logic;
		init 			: IN  std_logic;

		freq_word_ft 	: IN  std_logic_vector(NCO_W -1 DOWNTO 0);
		freq_word_fc 	: IN  std_logic_vector(NCO_W -1 DOWNTO 0);
		freq_word_f1 	: IN  std_logic_vector(NCO_W -1 DOWNTO 0);
		freq_word_f2 	: IN  std_logic_vector(NCO_W -1 DOWNTO 0);

		lpf_p_gain 		: IN  std_logic_vector(GAIN_W -1 DOWNTO 0);
		lpf_i_gain 		: IN  std_logic_vector(GAIN_W -1 DOWNTO 0);
		lpf_freeze 		: IN  std_logic;
		lpf_zero   		: IN  std_logic;
		lpf_alpha  		: IN  std_logic_vector(GAIN_W -1 DOWNTO 0);

		loopback_ena 	: IN  std_logic;

		ptt 			: IN  std_logic;

		tx_req 			: OUT std_logic;
		tx_data 		: IN  std_logic_vector(1 DOWNTO 0);

		tx_samples 		: OUT std_logic_vector(SAMPLE_W -1 DOWNTO 0);
		rx_samples 		: IN  std_logic_vector(SAMPLE_W -1 DOWNTO 0);

		rx_valid 		: OUT std_logic;
		rx_data 		: OUT std_logic
	);
END ENTITY msk_top;


ARCHITECTURE struct OF msk_top IS 

	SIGNAL tx_samples_int	: std_logic_vector(SAMPLE_W -1 DOWNTO 0);
	SIGNAL rx_samples_mux	: std_logic_vector(SAMPLE_W -1 DOWNTO 0);
	SIGNAL tx_req_int 		: std_logic;
	SIGNAL tclk 			: std_logic;

	SIGNAL tx_req_d 		: std_logic;
	SIGNAL rx_data_int 		: std_logic;
	SIGNAL rx_valid_int 	: std_logic;
	SIGNAL sent_data 		: std_logic;
	SIGNAL received_data 	: std_logic;
	SIGNAL sent_data_pipe 	: std_logic_vector(0 TO 3);

	SIGNAL bit_error 		: std_logic;

BEGIN 

	tx_req 		<= tx_req_int;
	tx_samples 	<= tx_samples_int;

	rx_data 	<= rx_data_int;
	rx_valid 	<= rx_valid_int;

	rx_samples_mux <= tx_samples_int WHEN loopback_ena = '1' ELSE rx_samples;

	data_check : PROCESS (clk)
	BEGIN
		IF clk'EVENT AND clk = '1' THEN

			tx_req_d <= tx_req_int;

			IF tx_req_d = '1' THEN
				sent_data_pipe <= tx_data(0) & sent_data_pipe(0 TO 2);
			END IF;

			IF rx_valid_int = '1' THEN
				sent_data <= sent_data_pipe(2);
				received_data <= rx_data_int;
			END IF;

			bit_error <= sent_data XOR received_data;

			ASSERT sent_data = received_data REPORT "Data Mismatch" SEVERITY WARNING;

		END IF;
	END PROCESS data_check;

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

			tx_data 		=> tx_data(0),
			tx_req 			=> tx_req_int,

			tx_samples	 	=> tx_samples_int		
		);


	u_dem : ENTITY work.msk_demodulator(rtl)
		GENERIC MAP (
			NCO_W 			=> NCO_W,
			PHASE_W 		=> PHASE_W,
			SINUSOID_W 		=> SINUSOID_W,
			SAMPLE_W 		=> SAMPLE_W
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

			rx_samples 		=> rx_samples_mux,

			rx_data 		=> rx_data_int,
			rx_valid 		=> rx_valid_int
		);


END ARCHITECTURE struct;