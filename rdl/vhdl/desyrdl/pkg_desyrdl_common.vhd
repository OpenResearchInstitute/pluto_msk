-------------------------------------------------------------------------------
--          ____  _____________  __                                          --
--         / __ \/ ____/ ___/\ \/ /                 _   _   _                --
--        / / / / __/  \__ \  \  /                 / \ / \ / \               --
--       / /_/ / /___ ___/ /  / /               = ( M | S | K )=             --
--      /_____/_____//____/  /_/                   \_/ \_/ \_/               --
--                                                                           --
-------------------------------------------------------------------------------
--! @copyright Copyright 2021-2022 DESY
--! SPDX-License-Identifier: Apache-2.0
-------------------------------------------------------------------------------
--! @date 2021-08-04
--! @author Michael Büchler <michael.buechler@desy.de>
--! @author Lukasz Butkowski <lukasz.butkowski@desy.de>
-------------------------------------------------------------------------------
--! @brief Package with common DesyRDL components
-------------------------------------------------------------------------------

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

-- library desy;
-- use desy.common_types.all;
-- use desy.common_axi.all;

package common is

  constant C_AXI4L_ADDR_WIDTH : natural := 32;
  constant C_AXI4L_DATA_WIDTH : natural := 32;

  ---------------------------------------------------------------------------
  -- common type definitions
  -- type t_4b_slv_array  is array (integer range<>) of std_logic_vector( 3 downto 0) ;
  -- type t_32b_slv_array is array (integer range<>) of std_logic_vector(31 downto 0) ;
  -- type t_integer_array is array (integer range<>) of integer ;

  --============================================================================
  -- AXI4-Lite
  --============================================================================
  type t_axi4l_m2s is record
    -- write address channel signals---------------------------------------------
    awaddr      : std_logic_vector(C_AXI4L_ADDR_WIDTH-1 downto 0);
    awprot      : std_logic_vector(2 downto 0);
    awvalid     : std_logic;
    -- write data channel signals---------------------------------------------
    wdata       : std_logic_vector(C_AXI4L_DATA_WIDTH-1 downto 0);
    wstrb       : std_logic_vector(C_AXI4L_DATA_WIDTH/8-1 downto 0);
    wvalid      : std_logic;
    -- write response channel signals
    bready      : std_logic;
    -- read address channel signals ---------------------------------------------
    araddr      : std_logic_vector(C_AXI4L_ADDR_WIDTH-1 downto 0);
    arprot      : std_logic_vector(2 downto 0);
    arvalid     : std_logic;
    -- read data channel signals---------------------------------------------
    rready      : std_logic;
  end record t_axi4l_m2s;

  type t_axi4l_s2m is record
    -- write address channel signals---------------------------------------------
    awready     : std_logic;
    -- write data channel signals---------------------------------------------
    wready      : std_logic;
    -- write response channel signals ---------------------------------------------
    bresp       : std_logic_vector(1 downto 0);
    bvalid      : std_logic;
    -- read address channel signals---------------------------------------------
    arready     : std_logic;
    -- read data channel signals---------------------------------------------
    rdata       : std_logic_vector(C_AXI4L_DATA_WIDTH-1 downto 0);
    rresp       : std_logic_vector(1 downto 0);
    rvalid      : std_logic;
  end record t_axi4l_s2m;

  type t_axi4l_m2s_vector is array (integer range <>) of t_axi4l_m2s;
  type t_axi4l_s2m_vector is array (integer range <>) of t_axi4l_s2m;

  constant  C_AXI4L_S2M_DEFAULT : t_axi4l_s2m := (
    awready     => '0',
    wready      => '0',
    bresp       => (others => '0'),
    bvalid      => '0',
    arready     => '0' ,
    rdata       => (others => '0'),
    rresp       => (others => '0'),
    rvalid      => '0'
  );
  constant  C_AXI4L_M2S_DEFAULT : t_axi4l_m2s := (
    awaddr        => (others => '0'),
    awprot        => (others => '0'),
    awvalid       => '0',
    wdata         => (others => '0'),
    wstrb         => (others => '0'),
    wvalid        => '0',
    bready        => '0',
    araddr        => (others => '0'),
    arprot        => (others => '0'),
    arvalid       => '0',
    rready        => '0'
  );

  ---------------------------------------------------------------------------
  -- Interface definitions for IBUS
  -- Internal BUS (IBUS) is the internal bus used in the applications of MSK Firmware
  -- repository.

  -- Output signals of IBUS. Through this record the application send data/commands to the bus
  type t_ibus_m2s is record
    addr   : std_logic_vector(31 downto 0);
    data   : std_logic_vector(31 downto 0);
    rena   : std_logic;
    wena   : std_logic;
  end record t_ibus_m2s;

  -- Output signals of IBUS. Through this record the application send data/commands to the bus
  type t_ibus_s2m is record
    data   : std_logic_vector(31 downto 0);
    rack   : std_logic;
    wack   : std_logic;
  end record t_ibus_s2m;

  -- Array of IBUS outputs
  type t_ibus_m2s_vector is array (integer range<>) of t_ibus_m2s;

  -- Array of IBUS inputs
  type t_ibus_s2m_vector is array (integer range<>) of t_ibus_s2m;

  -- Default IBUS connections for the output (All entries equals 0)
  constant C_IBUS_M2S_DEFAULT : t_ibus_m2s := (
    addr => (others => '0'),
    data => (others => '0'),
    rena => '0',
    wena => '0'
  );
  -- Default IBUS connections for the input (All entries equals 0)
  constant C_IBUS_S2M_DEFAULT : t_ibus_s2m := (
    data => (others => '0'),
    rack => '0',
    wack => '0'
  );


  ---------------------------------------------------------------------------
  -- SystemRDL-specific definitions
  --type t_field_access is (R, W, RW, NA);
  subtype t_access_type is integer;
  constant C_NA  : integer := 1;
  constant C_RW  : integer := 2;
  constant C_R   : integer := 3;
  constant C_W   : integer := 4;
  constant C_RW1 : integer := 5;
  constant C_W1  : integer := 6;

  type t_field_type is (STORAGE, WIRE, COUNTER, INTERRUPT);

  type t_field_info is record
    ftype     : t_field_type;
    len       : integer;
    upper     : integer;
    lower     : integer;
    sw        : t_access_type;
    hw        : t_access_type;
    we        : integer;
    incrwidth : integer;
    decrwidth : integer;
    defval    : integer;
  end record;

  type t_field_info_vector is array (integer range <>) of t_field_info;

  constant C_FIELD_NONE : t_field_info := (WIRE, 0, 0, 0, C_NA, C_NA, 0, 0, 0, 0);

  type t_reg_info is record
    -- index    : integer;
    address  : unsigned(C_AXI4L_ADDR_WIDTH-1 downto 0);
    elements : integer;
    index    : integer;
    fields   : t_field_info_vector(31 downto 0);
    --dim         : natural;
    dim_n    : positive;
    dim_m    : positive;
  end record;

  type t_reg_info_vector is array (integer range <>) of t_reg_info;

  constant C_REG_NONE : t_reg_info := (x"0000_0000", 0, 0,(others => C_FIELD_NONE),1,1);

  type t_mem_info is record
    -- index      : integer;
    address    : unsigned(C_AXI4L_ADDR_WIDTH-1 downto 0);
    addrwidth  : integer;
    datawidth  : integer;
    entries    : integer;
    sw         : t_access_type;
  end record;

  type t_mem_info_vector is array (integer range <>) of t_mem_info;

  constant C_MEM_NONE : t_mem_info := (x"0000_0000", 0, 0, 0, C_NA);

  type t_ext_info is record
    -- index      : integer;
    address    : unsigned(C_AXI4L_ADDR_WIDTH-1 downto 0);
    addrwidth  : integer;
    size       : integer;
  end record;

  type t_ext_info_vector is array (integer range <>) of t_ext_info;

  constant C_EXT_NONE : t_ext_info := (x"0000_0000", 0, 0);

  -- interface types
  type t_if_type Is (DPM, AXI4, AXI4L, IBUS, WISHBONE, AVALON, NONE);
  type t_if_type_vector is array (integer range <>) of t_if_type;

  -----------------------------------------------------------------------------
  -- bus converter components
  component axi4l_to_axi4l is
    port (
      pi_reset       : in  std_logic;
      pi_clock       : in  std_logic;
      pi_s_decoder : in  t_axi4l_m2s;
      po_s_decoder : out t_axi4l_s2m;
      po_m_ext     : out t_axi4l_m2s;
      pi_m_ext     : in  t_axi4l_s2m);
  end component axi4l_to_axi4l;

  component axi4l_to_ibus is
    port (
      pi_reset       : in  std_logic;
      pi_clock       : in  std_logic;
      pi_s_decoder : in  t_axi4l_m2s;
      po_s_decoder : out t_axi4l_s2m;
      po_m_ext     : out t_ibus_m2s;
      pi_m_ext     : in  t_ibus_s2m);
  end component axi4l_to_ibus;

  component ibus_to_axi4l is
    port (
      pi_reset       : in  std_logic;
      pi_clock       : in  std_logic;
      pi_s_decoder : in  t_ibus_m2s;
      po_s_decoder : out t_ibus_s2m;
      po_m_ext     : out t_axi4l_m2s;
      pi_m_ext     : in  t_axi4l_s2m);
  end component ibus_to_axi4l;

end package common;

--==============================================================================
package body common is
end package body;