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
------------------------------------------------------------------------------------------------------
-- Block name and description
------------------------------------------------------------------------------------------------------
--
-- AXI4-Lite Clock Domain Crossing Bridge
--
-- Transfers AXI4-Lite read/write transactions between two asynchronous clock
-- domains using a toggle-handshake protocol. One outstanding transaction is
-- supported per channel (read and write are independent).
--
-- Slave side accepts AXI4-Lite transactions in s_axi_aclk domain.
-- Master side drives AXI4-Lite transactions in m_axi_aclk domain.
-- m_axi_aresetn is a synchronized version of s_axi_aresetn (async assert,
-- sync deassert).
--
------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;

ENTITY axi_lite_cdc IS
	GENERIC (
		ADDR_WIDTH : NATURAL := 32;
		DATA_WIDTH : NATURAL := 32
	);
	PORT (
		-- Slave side (PS / AXI interconnect clock domain)
		s_axi_aclk      : IN  std_logic;
		s_axi_aresetn    : IN  std_logic;

		s_axi_awaddr     : IN  std_logic_vector(ADDR_WIDTH-1 DOWNTO 0);
		s_axi_awprot     : IN  std_logic_vector(2 DOWNTO 0);
		s_axi_awvalid    : IN  std_logic;
		s_axi_awready    : OUT std_logic;

		s_axi_wdata      : IN  std_logic_vector(DATA_WIDTH-1 DOWNTO 0);
		s_axi_wstrb      : IN  std_logic_vector(DATA_WIDTH/8-1 DOWNTO 0);
		s_axi_wvalid     : IN  std_logic;
		s_axi_wready     : OUT std_logic;

		s_axi_bresp      : OUT std_logic_vector(1 DOWNTO 0);
		s_axi_bvalid     : OUT std_logic;
		s_axi_bready     : IN  std_logic;

		s_axi_araddr     : IN  std_logic_vector(ADDR_WIDTH-1 DOWNTO 0);
		s_axi_arprot     : IN  std_logic_vector(2 DOWNTO 0);
		s_axi_arvalid    : IN  std_logic;
		s_axi_arready    : OUT std_logic;

		s_axi_rdata      : OUT std_logic_vector(DATA_WIDTH-1 DOWNTO 0);
		s_axi_rresp      : OUT std_logic_vector(1 DOWNTO 0);
		s_axi_rvalid     : OUT std_logic;
		s_axi_rready     : IN  std_logic;

		-- Master side (modem clock domain)
		m_axi_aclk       : IN  std_logic;
		m_axi_aresetn    : OUT std_logic;

		m_axi_awaddr     : OUT std_logic_vector(ADDR_WIDTH-1 DOWNTO 0);
		m_axi_awprot     : OUT std_logic_vector(2 DOWNTO 0);
		m_axi_awvalid    : OUT std_logic;
		m_axi_awready    : IN  std_logic;

		m_axi_wdata      : OUT std_logic_vector(DATA_WIDTH-1 DOWNTO 0);
		m_axi_wstrb      : OUT std_logic_vector(DATA_WIDTH/8-1 DOWNTO 0);
		m_axi_wvalid     : OUT std_logic;
		m_axi_wready     : IN  std_logic;

		m_axi_bresp      : IN  std_logic_vector(1 DOWNTO 0);
		m_axi_bvalid     : IN  std_logic;
		m_axi_bready     : OUT std_logic;

		m_axi_araddr     : OUT std_logic_vector(ADDR_WIDTH-1 DOWNTO 0);
		m_axi_arprot     : OUT std_logic_vector(2 DOWNTO 0);
		m_axi_arvalid    : OUT std_logic;
		m_axi_arready    : IN  std_logic;

		m_axi_rdata      : IN  std_logic_vector(DATA_WIDTH-1 DOWNTO 0);
		m_axi_rresp      : IN  std_logic_vector(1 DOWNTO 0);
		m_axi_rvalid     : IN  std_logic;
		m_axi_rready     : OUT std_logic
	);
END ENTITY axi_lite_cdc;

ARCHITECTURE rtl OF axi_lite_cdc IS

	-- Reset synchronizer (async assert, sync deassert into m_axi_aclk)
	SIGNAL rst_meta  : std_logic := '1';
	SIGNAL rst_sync  : std_logic := '1';

	-- Write path signals --

	-- Slave side
	TYPE s_wr_state_t IS (S_WR_IDLE, S_WR_WAIT_ACK, S_WR_RESP);
	SIGNAL s_wr_state    : s_wr_state_t := S_WR_IDLE;
	SIGNAL s_wr_addr     : std_logic_vector(ADDR_WIDTH-1 DOWNTO 0);
	SIGNAL s_wr_prot     : std_logic_vector(2 DOWNTO 0);
	SIGNAL s_wr_data     : std_logic_vector(DATA_WIDTH-1 DOWNTO 0);
	SIGNAL s_wr_strb     : std_logic_vector(DATA_WIDTH/8-1 DOWNTO 0);
	SIGNAL s_wr_bresp    : std_logic_vector(1 DOWNTO 0);
	SIGNAL wr_req_toggle : std_logic := '0';
	SIGNAL wr_ack_sync1  : std_logic := '0';
	SIGNAL wr_ack_sync2  : std_logic := '0';
	SIGNAL wr_ack_sync3  : std_logic := '0';

	-- Master side
	TYPE m_wr_state_t IS (ST_MWR_IDLE, ST_MWR_ADDR, ST_MWR_DATA, ST_MWR_RESP);
	SIGNAL m_wr_state    : m_wr_state_t := ST_MWR_IDLE;
	SIGNAL m_wr_addr     : std_logic_vector(ADDR_WIDTH-1 DOWNTO 0);
	SIGNAL m_wr_prot     : std_logic_vector(2 DOWNTO 0);
	SIGNAL m_wr_data     : std_logic_vector(DATA_WIDTH-1 DOWNTO 0);
	SIGNAL m_wr_strb     : std_logic_vector(DATA_WIDTH/8-1 DOWNTO 0);
	SIGNAL m_wr_bresp    : std_logic_vector(1 DOWNTO 0);
	SIGNAL wr_ack_toggle : std_logic := '0';
	SIGNAL wr_req_sync1  : std_logic := '0';
	SIGNAL wr_req_sync2  : std_logic := '0';
	SIGNAL wr_req_last   : std_logic := '0';

	-- Read path signals --

	-- Slave side
	TYPE s_rd_state_t IS (S_RD_IDLE, S_RD_WAIT_ACK, S_RD_RESP);
	SIGNAL s_rd_state    : s_rd_state_t := S_RD_IDLE;
	SIGNAL s_rd_addr     : std_logic_vector(ADDR_WIDTH-1 DOWNTO 0);
	SIGNAL s_rd_prot     : std_logic_vector(2 DOWNTO 0);
	SIGNAL s_rd_rdata    : std_logic_vector(DATA_WIDTH-1 DOWNTO 0);
	SIGNAL s_rd_rresp    : std_logic_vector(1 DOWNTO 0);
	SIGNAL rd_req_toggle : std_logic := '0';
	SIGNAL rd_ack_sync1  : std_logic := '0';
	SIGNAL rd_ack_sync2  : std_logic := '0';
	SIGNAL rd_ack_sync3  : std_logic := '0';

	-- Master side
	TYPE m_rd_state_t IS (ST_MRD_IDLE, ST_MRD_ADDR, ST_MRD_RESP);
	SIGNAL m_rd_state    : m_rd_state_t := ST_MRD_IDLE;
	SIGNAL m_rd_addr     : std_logic_vector(ADDR_WIDTH-1 DOWNTO 0);
	SIGNAL m_rd_prot     : std_logic_vector(2 DOWNTO 0);
	SIGNAL m_rd_rdata    : std_logic_vector(DATA_WIDTH-1 DOWNTO 0);
	SIGNAL m_rd_rresp    : std_logic_vector(1 DOWNTO 0);
	SIGNAL rd_ack_toggle : std_logic := '0';
	SIGNAL rd_req_sync1  : std_logic := '0';
	SIGNAL rd_req_sync2  : std_logic := '0';
	SIGNAL rd_req_last   : std_logic := '0';

BEGIN

	----------------------------------------------------------------------
	-- Reset synchronizer: async assert, synchronous deassert into m_axi_aclk
	----------------------------------------------------------------------
	reset_sync_proc : PROCESS (m_axi_aclk, s_axi_aresetn)
	BEGIN
		IF s_axi_aresetn = '0' THEN
			rst_meta <= '1';
			rst_sync <= '1';
		ELSIF rising_edge(m_axi_aclk) THEN
			rst_meta <= '0';
			rst_sync <= rst_meta;
		END IF;
	END PROCESS reset_sync_proc;

	m_axi_aresetn <= NOT rst_sync;

	----------------------------------------------------------------------
	-- WRITE PATH — Slave side FSM (s_axi_aclk domain)
	----------------------------------------------------------------------
	s_wr_fsm : PROCESS (s_axi_aclk)
	BEGIN
		IF rising_edge(s_axi_aclk) THEN
			IF s_axi_aresetn = '0' THEN
				s_wr_state    <= S_WR_IDLE;
				wr_req_toggle <= '0';
				wr_ack_sync1  <= '0';
				wr_ack_sync2  <= '0';
				wr_ack_sync3  <= '0';
			ELSE
				-- 2-FF synchronizer for ack toggle from master
				wr_ack_sync1 <= wr_ack_toggle;
				wr_ack_sync2 <= wr_ack_sync1;
				wr_ack_sync3 <= wr_ack_sync2;

				CASE s_wr_state IS
					WHEN S_WR_IDLE =>
						IF s_axi_awvalid = '1' AND s_axi_wvalid = '1' THEN
							s_wr_addr     <= s_axi_awaddr;
							s_wr_prot     <= s_axi_awprot;
							s_wr_data     <= s_axi_wdata;
							s_wr_strb     <= s_axi_wstrb;
							wr_req_toggle <= NOT wr_req_toggle;
							s_wr_state    <= S_WR_WAIT_ACK;
						END IF;

					WHEN S_WR_WAIT_ACK =>
						IF wr_ack_sync2 /= wr_ack_sync3 THEN
							s_wr_bresp <= m_wr_bresp;
							s_wr_state <= S_WR_RESP;
						END IF;

					WHEN S_WR_RESP =>
						IF s_axi_bready = '1' THEN
							s_wr_state <= S_WR_IDLE;
						END IF;
				END CASE;
			END IF;
		END IF;
	END PROCESS s_wr_fsm;

	s_axi_awready <= '1' WHEN s_wr_state = S_WR_IDLE ELSE '0';
	s_axi_wready  <= '1' WHEN s_wr_state = S_WR_IDLE ELSE '0';
	s_axi_bvalid  <= '1' WHEN s_wr_state = S_WR_RESP ELSE '0';
	s_axi_bresp   <= s_wr_bresp;

	----------------------------------------------------------------------
	-- WRITE PATH — Master side FSM (m_axi_aclk domain)
	----------------------------------------------------------------------
	m_wr_fsm : PROCESS (m_axi_aclk)
	BEGIN
		IF rising_edge(m_axi_aclk) THEN
			IF rst_sync = '1' THEN
				m_wr_state    <= ST_MWR_IDLE;
				wr_ack_toggle <= '0';
				wr_req_sync1  <= '0';
				wr_req_sync2  <= '0';
				wr_req_last   <= '0';
				m_axi_awvalid <= '0';
				m_axi_wvalid  <= '0';
				m_axi_bready  <= '0';
			ELSE
				-- 2-FF synchronizer for req toggle from slave
				wr_req_sync1 <= wr_req_toggle;
				wr_req_sync2 <= wr_req_sync1;

				CASE m_wr_state IS
					WHEN ST_MWR_IDLE =>
						m_axi_awvalid <= '0';
						m_axi_wvalid  <= '0';
						m_axi_bready  <= '0';
						IF wr_req_sync2 /= wr_req_last THEN
							wr_req_last   <= wr_req_sync2;
							m_wr_addr     <= s_wr_addr;
							m_wr_prot     <= s_wr_prot;
							m_wr_data     <= s_wr_data;
							m_wr_strb     <= s_wr_strb;
							m_axi_awvalid <= '1';
							m_axi_wvalid  <= '1';
							m_wr_state    <= ST_MWR_ADDR;
						END IF;

					WHEN ST_MWR_ADDR =>
						IF m_axi_awready = '1' THEN
							m_axi_awvalid <= '0';
						END IF;
						IF m_axi_wready = '1' THEN
							m_axi_wvalid <= '0';
						END IF;
						IF (m_axi_awready = '1' OR m_axi_awvalid = '0') AND
						   (m_axi_wready = '1' OR m_axi_wvalid = '0') THEN
							m_axi_bready <= '1';
							m_wr_state   <= ST_MWR_RESP;
						END IF;

					WHEN ST_MWR_RESP =>
						IF m_axi_bvalid = '1' THEN
							m_wr_bresp    <= m_axi_bresp;
							m_axi_bready  <= '0';
							wr_ack_toggle <= NOT wr_ack_toggle;
							m_wr_state    <= ST_MWR_IDLE;
						END IF;

					WHEN OTHERS =>
						m_wr_state <= ST_MWR_IDLE;
				END CASE;
			END IF;
		END IF;
	END PROCESS m_wr_fsm;

	m_axi_awaddr <= m_wr_addr;
	m_axi_awprot <= m_wr_prot;
	m_axi_wdata  <= m_wr_data;
	m_axi_wstrb  <= m_wr_strb;

	----------------------------------------------------------------------
	-- READ PATH — Slave side FSM (s_axi_aclk domain)
	----------------------------------------------------------------------
	s_rd_fsm : PROCESS (s_axi_aclk)
	BEGIN
		IF rising_edge(s_axi_aclk) THEN
			IF s_axi_aresetn = '0' THEN
				s_rd_state    <= S_RD_IDLE;
				rd_req_toggle <= '0';
				rd_ack_sync1  <= '0';
				rd_ack_sync2  <= '0';
				rd_ack_sync3  <= '0';
			ELSE
				-- 2-FF synchronizer for ack toggle from master
				rd_ack_sync1 <= rd_ack_toggle;
				rd_ack_sync2 <= rd_ack_sync1;
				rd_ack_sync3 <= rd_ack_sync2;

				CASE s_rd_state IS
					WHEN S_RD_IDLE =>
						IF s_axi_arvalid = '1' THEN
							s_rd_addr     <= s_axi_araddr;
							s_rd_prot     <= s_axi_arprot;
							rd_req_toggle <= NOT rd_req_toggle;
							s_rd_state    <= S_RD_WAIT_ACK;
						END IF;

					WHEN S_RD_WAIT_ACK =>
						IF rd_ack_sync2 /= rd_ack_sync3 THEN
							s_rd_rdata <= m_rd_rdata;
							s_rd_rresp <= m_rd_rresp;
							s_rd_state <= S_RD_RESP;
						END IF;

					WHEN S_RD_RESP =>
						IF s_axi_rready = '1' THEN
							s_rd_state <= S_RD_IDLE;
						END IF;
				END CASE;
			END IF;
		END IF;
	END PROCESS s_rd_fsm;

	s_axi_arready <= '1' WHEN s_rd_state = S_RD_IDLE ELSE '0';
	s_axi_rvalid  <= '1' WHEN s_rd_state = S_RD_RESP ELSE '0';
	s_axi_rdata   <= s_rd_rdata;
	s_axi_rresp   <= s_rd_rresp;

	----------------------------------------------------------------------
	-- READ PATH — Master side FSM (m_axi_aclk domain)
	----------------------------------------------------------------------
	m_rd_fsm : PROCESS (m_axi_aclk)
	BEGIN
		IF rising_edge(m_axi_aclk) THEN
			IF rst_sync = '1' THEN
				m_rd_state    <= ST_MRD_IDLE;
				rd_ack_toggle <= '0';
				rd_req_sync1  <= '0';
				rd_req_sync2  <= '0';
				rd_req_last   <= '0';
				m_axi_arvalid <= '0';
				m_axi_rready  <= '0';
			ELSE
				-- 2-FF synchronizer for req toggle from slave
				rd_req_sync1 <= rd_req_toggle;
				rd_req_sync2 <= rd_req_sync1;

				CASE m_rd_state IS
					WHEN ST_MRD_IDLE =>
						m_axi_arvalid <= '0';
						m_axi_rready  <= '0';
						IF rd_req_sync2 /= rd_req_last THEN
							rd_req_last   <= rd_req_sync2;
							m_rd_addr     <= s_rd_addr;
							m_rd_prot     <= s_rd_prot;
							m_axi_arvalid <= '1';
							m_rd_state    <= ST_MRD_ADDR;
						END IF;

					WHEN ST_MRD_ADDR =>
						IF m_axi_arready = '1' THEN
							m_axi_arvalid <= '0';
							m_axi_rready  <= '1';
							m_rd_state    <= ST_MRD_RESP;
						END IF;

					WHEN ST_MRD_RESP =>
						IF m_axi_rvalid = '1' THEN
							m_rd_rdata    <= m_axi_rdata;
							m_rd_rresp    <= m_axi_rresp;
							m_axi_rready  <= '0';
							rd_ack_toggle <= NOT rd_ack_toggle;
							m_rd_state    <= ST_MRD_IDLE;
						END IF;

					WHEN OTHERS =>
						m_rd_state <= ST_MRD_IDLE;
				END CASE;
			END IF;
		END IF;
	END PROCESS m_rd_fsm;

	m_axi_araddr <= m_rd_addr;
	m_axi_arprot <= m_rd_prot;

END ARCHITECTURE rtl;
