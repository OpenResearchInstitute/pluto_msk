

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.numeric_std.ALL;

ENTITY msk_top IS 
	GENERIC (
		NCO_W 			: NATURAL := 32;
		PHASE_W 		: NATURAL := 10;
		SINUSOID_W 		: NATURAL := 12;
		SAMPLE_W 		: NATURAL := 12
	);
	PORT (
		clk 			: IN  std_logic;
		init 			: IN  std_logic;

		tx_freq_word_ft : IN  std_logic_vector(NCO_W -1 DOWNTO 0);
		tx_freq_word_fc : IN  std_logic_vector(NCO_W -1 DOWNTO 0);
		rx_freq_word_f1 : IN  std_logic_vector(NCO_W -1 DOWNTO 0);
		rx_freq_word_f2 : IN  std_logic_vector(NCO_W -1 DOWNTO 0);

		tx_req 			: OUT std_logic;
		tx_data 		: IN  std_logic_vector(1 DOWNTO 0);

		tx_samples 		: OUT std_logic_vector(SAMPLE_W -1 DOWNTO 0);
		--rx_samples 		: IN  std_logic_vector(SAMPLE_W -1 DOWNTO 0);

		rx_valid 		: OUT std_logic;
		rx_data 		: OUT std_logic_vector(1 DOWNTO 0)
	);
END ENTITY msk_top;


ARCHITECTURE struct OF msk_top IS 

	SIGNAL txrx_samples		: std_logic_vector(SAMPLE_W -1 DOWNTO 0);
	SIGNAL tx_req_int 		: std_logic;
	SIGNAL tclk 			: std_logic;

BEGIN 

	tx_req <= tx_req_int;
	tx_samples <= txrx_samples;

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

			tclk 			=> tclk,

			mod_freq_word 	=> tx_freq_word_ft,
			car_freq_word	=> tx_freq_word_fc,

			tx_data 		=> tx_data,
			tx_req 			=> tx_req_int,

			tx_samples	 	=> txrx_samples		
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

			tclk 			=> tclk,
	
			rx_freq_word_f1 => rx_freq_word_f1,
			rx_freq_word_f2	=> rx_freq_word_f2,
	
			rx_samples 		=> txrx_samples,
	
			rx_data 		=> rx_data,
			rx_valid 		=> rx_valid
		);


END ARCHITECTURE struct;