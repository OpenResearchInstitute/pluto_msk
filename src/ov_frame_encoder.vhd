------------------------------------------------------------------------------------------------------
-- Opulent Voice Protocol Frame Encoder - DUAL MODE (Bit-level or Byte-level Interleaver)
------------------------------------------------------------------------------------------------------
-- Supports both interleaver modes via generic parameter:
--   USE_BIT_INTERLEAVER = TRUE  : 67x32 bit-level (correct protocol, requires large FPGA)
--   USE_BIT_INTERLEAVER = FALSE : 67x4 byte-level (fits PlutoSDR, breaks protocol compatibility)
------------------------------------------------------------------------------------------------------
-- CRITICAL DESIGN PRINCIPLE: TLAST-DRIVEN FRAME COLLECTION
------------------------------------------------------------------------------------------------------
-- This encoder uses AXI-Stream TLAST signal to detect frame boundaries, NOT fixed byte counting!
--
-- WHY THIS MATTERS:
--   When data flows continuously (e.g., FIFO buffering multiple frames), counting to a fixed
--   number of bytes and ignoring tlast causes the encoder to "steal" bytes from the next frame.
--   This creates cascading byte loss:
--     Frame 3: Missing byte 0 (stolen during Frame 2 collection)
--     Frame 4: Missing bytes 0-1 (stolen during Frame 3 collection)
--     Frame 5: Missing bytes 0-2 (stolen during Frame 4 collection)
--     ... continues until no more data available
--
-- CORRECT APPROACH (implemented here):
--   1. IDLE state: Wait for first byte
--   2. COLLECT state: Accept bytes until s_axis_tlast = '1' (frame boundary marker)
--   3. Validate we got exactly PAYLOAD_BYTES (134)
--   4. Process the complete frame through randomization, FEC, interleaving
--   5. Pre-set s_axis_tready = '1' before returning to IDLE for next frame
--
-- This approach:
--   Respects AXI-Stream protocol (tlast marks frame boundaries)
--   Works with continuous data streams (FIFO buffering)
--   Prevents byte stealing across frame boundaries
--   Validates frame size for error detection
--   Works for BOTH bit-level and byte-level interleaving modes
--
-- NEVER count to a fixed byte number and ignore tlast - this violates AXI-Stream protocol!
------------------------------------------------------------------------------------------------------

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.numeric_std.ALL;

ENTITY ov_frame_encoder IS
    GENERIC (
        PAYLOAD_BYTES       : NATURAL := 134;
        ENCODED_BYTES       : NATURAL := 268;
        COLLECT_SIZE        : NATURAL := 4;      -- DEPRECATED: No longer used (kept for compatibility)
        ENCODED_BITS        : NATURAL := 2144;   -- Kept for compatibility
        BYTE_WIDTH          : NATURAL := 8;      -- Kept for compatibility
        USE_BIT_INTERLEAVER : BOOLEAN := TRUE    -- TRUE=bit-level(67x32), FALSE=byte-level(67x4)
    );
    PORT (
        clk          : IN  std_logic;
        aresetn      : IN  std_logic;
        
        -- AXI-Stream Input (from application)
        s_axis_tdata  : IN  std_logic_vector(BYTE_WIDTH-1 DOWNTO 0);
        s_axis_tvalid : IN  std_logic;
        s_axis_tready : OUT std_logic;
        s_axis_tlast  : IN  std_logic;
        
        -- AXI-Stream Output (to modulator)
        m_axis_tdata  : OUT std_logic_vector(BYTE_WIDTH-1 DOWNTO 0);
        m_axis_tvalid : OUT std_logic;
        m_axis_tready : IN  std_logic;
        m_axis_tlast  : OUT std_logic;
        
        -- Status outputs
        frames_encoded : OUT std_logic_vector(31 DOWNTO 0);
        encoder_active : OUT std_logic;
        debug_state : OUT std_logic_vector(2 DOWNTO 0)
    );
END ENTITY ov_frame_encoder;

ARCHITECTURE rtl OF ov_frame_encoder IS

    -- Randomizer sequence from protocol specification
    TYPE randomizer_t IS ARRAY(0 TO PAYLOAD_BYTES-1) OF std_logic_vector(7 DOWNTO 0);
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

    ------------------------------------------------------------------------------
    -- STATE MACHINE DESIGN PHILOSOPHY
    ------------------------------------------------------------------------------
    -- CRITICAL: This encoder uses TLAST-DRIVEN frame detection, NOT fixed byte counting!
    --
    -- WHY: AXI-Stream protocol uses tlast to mark frame boundaries. Ignoring tlast
    --      causes the encoder to "steal" bytes from the next frame when data is
    --      continuously available (e.g., from a buffering FIFO). This creates
    --      cascading byte loss errors across multiple frames.
    --
    -- COLLECT state strategy:
    --   1. Accept bytes one at a time
    --   2. Store each byte in input_buffer[collect_idx]
    --   3. Watch for s_axis_tlast = '1' (frame boundary)
    --   4. When tlast seen, validate we got PAYLOAD_BYTES (134), then process
    --
    -- This works for BOTH byte-level and bit-level interleaving modes because:
    --   - Collection only fills input_buffer
    --   - Interleaving happens later (INTERLEAVE state) on FEC-encoded bits
    --   - Interleaver type doesn't affect how we collect input bytes
    --
    -- NEVER count to a fixed number and ignore tlast - this violates AXI protocol!
    ------------------------------------------------------------------------------
    TYPE state_t IS (
        IDLE,       -- Wait for first byte of frame
        COLLECT,    -- Gather bytes until tlast (AXI-Stream frame boundary marker)
        RANDOMIZE,  -- XOR with randomizer sequence
        PREP_FEC,   -- Prepare for convolutional encoding
        FEC_ENCODE, -- Apply K=7 convolutional code
        INTERLEAVE, -- Shuffle bits (bit-level) or bytes (byte-level) per generic
        OUTPUT      -- Stream encoded frame to modulator
    );
    SIGNAL state : state_t := IDLE;

    TYPE byte_buffer_t IS ARRAY(0 TO PAYLOAD_BYTES-1) OF std_logic_vector(7 DOWNTO 0);
    TYPE bit_buffer_t IS ARRAY(0 TO ENCODED_BITS-1) OF std_logic;
    
    SIGNAL input_buffer       : byte_buffer_t;
    SIGNAL randomized_buffer  : byte_buffer_t;
    SIGNAL fec_buffer         : bit_buffer_t := (OTHERS => '0');
    SIGNAL interleaved_buffer : bit_buffer_t := (OTHERS => '0');

    -- Index counters
    SIGNAL collect_idx : NATURAL RANGE 0 TO PAYLOAD_BYTES;  -- Now collects all bytes until tlast
    SIGNAL byte_idx    : NATURAL RANGE 0 TO ENCODED_BYTES;
    SIGNAL bit_idx     : NATURAL RANGE 0 TO ENCODED_BITS;
    SIGNAL out_idx     : NATURAL RANGE 0 TO ENCODED_BYTES;
    
    -- AXI-Stream control
    SIGNAL s_axis_tready_reg : std_logic := '0';
    SIGNAL m_axis_tdata_reg  : std_logic_vector(BYTE_WIDTH-1 DOWNTO 0) := (OTHERS => '0');
    SIGNAL m_axis_tvalid_reg : std_logic := '0';
    SIGNAL m_axis_tlast_reg  : std_logic := '0';
    
    -- Status counters
    SIGNAL frames_encoded_reg : unsigned(31 DOWNTO 0) := (OTHERS => '0');
    SIGNAL encoder_active_reg : std_logic := '0';

    -- Convolutional encoder signals
    SIGNAL encoder_start      : std_logic := '0';
    SIGNAL encoder_busy       : std_logic;
    SIGNAL encoder_done       : std_logic;
    SIGNAL encoder_input_buf  : std_logic_vector(1071 DOWNTO 0);
    SIGNAL encoder_output_buf : std_logic_vector(2143 DOWNTO 0);

    -- preserve the output registers from synthesis optimization
    ATTRIBUTE dont_touch : STRING;
    ATTRIBUTE dont_touch OF m_axis_tvalid_reg : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF m_axis_tdata_reg : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF m_axis_tlast_reg : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF s_axis_tready_reg : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF input_buffer : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF randomized_buffer : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF fec_buffer : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF interleaved_buffer : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF encoder_input_buf : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF encoder_output_buf : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF state : SIGNAL IS "true";
    -- adding these stalled the FIFO from draining past two frames
    --ATTRIBUTE dont_touch OF out_idx : SIGNAL IS "true";
    --ATTRIBUTE dont_touch OF byte_idx : SIGNAL IS "true";
    --ATTRIBUTE dont_touch OF collect_idx : SIGNAL IS "true";

    -- Protect conv_encoder_k7 interface signals (prevent optimization)
    ATTRIBUTE dont_touch OF encoder_start : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF encoder_busy : SIGNAL IS "true";
    ATTRIBUTE dont_touch OF encoder_done : SIGNAL IS "true";
    -- Protect the conv_encoder_k7 instance itself
    ATTRIBUTE dont_touch OF U_ENCODER : LABEL IS "true";

    -- Also force BRAM on the large buffers 
    ATTRIBUTE ram_style : STRING;
    ATTRIBUTE ram_style OF interleaved_buffer : SIGNAL IS "block";
    ATTRIBUTE ram_style OF input_buffer : SIGNAL IS "block";
    ATTRIBUTE ram_style OF randomized_buffer : SIGNAL IS "block";
    ATTRIBUTE ram_style OF fec_buffer : SIGNAL IS "block";


    
    ----------------------------------------------------------------------------
    -- BIT-LEVEL INTERLEAVER (67x32) - For large FPGAs, correct protocol
    ----------------------------------------------------------------------------
--    TYPE address_lut_t IS ARRAY(0 TO 2143) OF NATURAL RANGE 0 TO 2143;
--    CONSTANT INTERLEAVE_LUT_BIT : address_lut_t := (
--           0,   67,  134,  201,  268,  335,  402,  469,  536,  603,  670,  737,  804,  871,  938, 1005,
--        1072, 1139, 1206, 1273, 1340, 1407, 1474, 1541, 1608, 1675, 1742, 1809, 1876, 1943, 2010, 2077,
--           1,   68,  135,  202,  269,  336,  403,  470,  537,  604,  671,  738,  805,  872,  939, 1006,
--        1073, 1140, 1207, 1274, 1341, 1408, 1475, 1542, 1609, 1676, 1743, 1810, 1877, 1944, 2011, 2078,
--           2,   69,  136,  203,  270,  337,  404,  471,  538,  605,  672,  739,  806,  873,  940, 1007,
--        1074, 1141, 1208, 1275, 1342, 1409, 1476, 1543, 1610, 1677, 1744, 1811, 1878, 1945, 2012, 2079,
--           3,   70,  137,  204,  271,  338,  405,  472,  539,  606,  673,  740,  807,  874,  941, 1008,
--        1075, 1142, 1209, 1276, 1343, 1410, 1477, 1544, 1611, 1678, 1745, 1812, 1879, 1946, 2013, 2080,
--           4,   71,  138,  205,  272,  339,  406,  473,  540,  607,  674,  741,  808,  875,  942, 1009,
--        1076, 1143, 1210, 1277, 1344, 1411, 1478, 1545, 1612, 1679, 1746, 1813, 1880, 1947, 2014, 2081,
--           5,   72,  139,  206,  273,  340,  407,  474,  541,  608,  675,  742,  809,  876,  943, 1010,
--        1077, 1144, 1211, 1278, 1345, 1412, 1479, 1546, 1613, 1680, 1747, 1814, 1881, 1948, 2015, 2082,
--           6,   73,  140,  207,  274,  341,  408,  475,  542,  609,  676,  743,  810,  877,  944, 1011,
--        1078, 1145, 1212, 1279, 1346, 1413, 1480, 1547, 1614, 1681, 1748, 1815, 1882, 1949, 2016, 2083,
--           7,   74,  141,  208,  275,  342,  409,  476,  543,  610,  677,  744,  811,  878,  945, 1012,
--        1079, 1146, 1213, 1280, 1347, 1414, 1481, 1548, 1615, 1682, 1749, 1816, 1883, 1950, 2017, 2084,
--           8,   75,  142,  209,  276,  343,  410,  477,  544,  611,  678,  745,  812,  879,  946, 1013,
--        1080, 1147, 1214, 1281, 1348, 1415, 1482, 1549, 1616, 1683, 1750, 1817, 1884, 1951, 2018, 2085,
--           9,   76,  143,  210,  277,  344,  411,  478,  545,  612,  679,  746,  813,  880,  947, 1014,
--        1081, 1148, 1215, 1282, 1349, 1416, 1483, 1550, 1617, 1684, 1751, 1818, 1885, 1952, 2019, 2086,
--          10,   77,  144,  211,  278,  345,  412,  479,  546,  613,  680,  747,  814,  881,  948, 1015,
--        1082, 1149, 1216, 1283, 1350, 1417, 1484, 1551, 1618, 1685, 1752, 1819, 1886, 1953, 2020, 2087,
--          11,   78,  145,  212,  279,  346,  413,  480,  547,  614,  681,  748,  815,  882,  949, 1016,
--        1083, 1150, 1217, 1284, 1351, 1418, 1485, 1552, 1619, 1686, 1753, 1820, 1887, 1954, 2021, 2088,
--          12,   79,  146,  213,  280,  347,  414,  481,  548,  615,  682,  749,  816,  883,  950, 1017,
--        1084, 1151, 1218, 1285, 1352, 1419, 1486, 1553, 1620, 1687, 1754, 1821, 1888, 1955, 2022, 2089,
--          13,   80,  147,  214,  281,  348,  415,  482,  549,  616,  683,  750,  817,  884,  951, 1018,
--        1085, 1152, 1219, 1286, 1353, 1420, 1487, 1554, 1621, 1688, 1755, 1822, 1889, 1956, 2023, 2090,
--          14,   81,  148,  215,  282,  349,  416,  483,  550,  617,  684,  751,  818,  885,  952, 1019,
--        1086, 1153, 1220, 1287, 1354, 1421, 1488, 1555, 1622, 1689, 1756, 1823, 1890, 1957, 2024, 2091,
--          15,   82,  149,  216,  283,  350,  417,  484,  551,  618,  685,  752,  819,  886,  953, 1020,
--        1087, 1154, 1221, 1288, 1355, 1422, 1489, 1556, 1623, 1690, 1757, 1824, 1891, 1958, 2025, 2092,
--          16,   83,  150,  217,  284,  351,  418,  485,  552,  619,  686,  753,  820,  887,  954, 1021,
--        1088, 1155, 1222, 1289, 1356, 1423, 1490, 1557, 1624, 1691, 1758, 1825, 1892, 1959, 2026, 2093,
--          17,   84,  151,  218,  285,  352,  419,  486,  553,  620,  687,  754,  821,  888,  955, 1022,
--        1089, 1156, 1223, 1290, 1357, 1424, 1491, 1558, 1625, 1692, 1759, 1826, 1893, 1960, 2027, 2094,
--          18,   85,  152,  219,  286,  353,  420,  487,  554,  621,  688,  755,  822,  889,  956, 1023,
--        1090, 1157, 1224, 1291, 1358, 1425, 1492, 1559, 1626, 1693, 1760, 1827, 1894, 1961, 2028, 2095,
--          19,   86,  153,  220,  287,  354,  421,  488,  555,  622,  689,  756,  823,  890,  957, 1024,
--        1091, 1158, 1225, 1292, 1359, 1426, 1493, 1560, 1627, 1694, 1761, 1828, 1895, 1962, 2029, 2096,
--          20,   87,  154,  221,  288,  355,  422,  489,  556,  623,  690,  757,  824,  891,  958, 1025,
--        1092, 1159, 1226, 1293, 1360, 1427, 1494, 1561, 1628, 1695, 1762, 1829, 1896, 1963, 2030, 2097,
--          21,   88,  155,  222,  289,  356,  423,  490,  557,  624,  691,  758,  825,  892,  959, 1026,
--        1093, 1160, 1227, 1294, 1361, 1428, 1495, 1562, 1629, 1696, 1763, 1830, 1897, 1964, 2031, 2098,
--          22,   89,  156,  223,  290,  357,  424,  491,  558,  625,  692,  759,  826,  893,  960, 1027,
--        1094, 1161, 1228, 1295, 1362, 1429, 1496, 1563, 1630, 1697, 1764, 1831, 1898, 1965, 2032, 2099,
--          23,   90,  157,  224,  291,  358,  425,  492,  559,  626,  693,  760,  827,  894,  961, 1028,
--        1095, 1162, 1229, 1296, 1363, 1430, 1497, 1564, 1631, 1698, 1765, 1832, 1899, 1966, 2033, 2100,
--          24,   91,  158,  225,  292,  359,  426,  493,  560,  627,  694,  761,  828,  895,  962, 1029,
--        1096, 1163, 1230, 1297, 1364, 1431, 1498, 1565, 1632, 1699, 1766, 1833, 1900, 1967, 2034, 2101,
--          25,   92,  159,  226,  293,  360,  427,  494,  561,  628,  695,  762,  829,  896,  963, 1030,
--        1097, 1164, 1231, 1298, 1365, 1432, 1499, 1566, 1633, 1700, 1767, 1834, 1901, 1968, 2035, 2102,
--          26,   93,  160,  227,  294,  361,  428,  495,  562,  629,  696,  763,  830,  897,  964, 1031,
--        1098, 1165, 1232, 1299, 1366, 1433, 1500, 1567, 1634, 1701, 1768, 1835, 1902, 1969, 2036, 2103,
--          27,   94,  161,  228,  295,  362,  429,  496,  563,  630,  697,  764,  831,  898,  965, 1032,
--        1099, 1166, 1233, 1300, 1367, 1434, 1501, 1568, 1635, 1702, 1769, 1836, 1903, 1970, 2037, 2104,
--          28,   95,  162,  229,  296,  363,  430,  497,  564,  631,  698,  765,  832,  899,  966, 1033,
--        1100, 1167, 1234, 1301, 1368, 1435, 1502, 1569, 1636, 1703, 1770, 1837, 1904, 1971, 2038, 2105,
--          29,   96,  163,  230,  297,  364,  431,  498,  565,  632,  699,  766,  833,  900,  967, 1034,
--        1101, 1168, 1235, 1302, 1369, 1436, 1503, 1570, 1637, 1704, 1771, 1838, 1905, 1972, 2039, 2106,
--          30,   97,  164,  231,  298,  365,  432,  499,  566,  633,  700,  767,  834,  901,  968, 1035,
--        1102, 1169, 1236, 1303, 1370, 1437, 1504, 1571, 1638, 1705, 1772, 1839, 1906, 1973, 2040, 2107,
--          31,   98,  165,  232,  299,  366,  433,  500,  567,  634,  701,  768,  835,  902,  969, 1036,
--        1103, 1170, 1237, 1304, 1371, 1438, 1505, 1572, 1639, 1706, 1773, 1840, 1907, 1974, 2041, 2108,
--          32,   99,  166,  233,  300,  367,  434,  501,  568,  635,  702,  769,  836,  903,  970, 1037,
--        1104, 1171, 1238, 1305, 1372, 1439, 1506, 1573, 1640, 1707, 1774, 1841, 1908, 1975, 2042, 2109,
--          33,  100,  167,  234,  301,  368,  435,  502,  569,  636,  703,  770,  837,  904,  971, 1038,
--        1105, 1172, 1239, 1306, 1373, 1440, 1507, 1574, 1641, 1708, 1775, 1842, 1909, 1976, 2043, 2110,
--          34,  101,  168,  235,  302,  369,  436,  503,  570,  637,  704,  771,  838,  905,  972, 1039,
--        1106, 1173, 1240, 1307, 1374, 1441, 1508, 1575, 1642, 1709, 1776, 1843, 1910, 1977, 2044, 2111,
--          35,  102,  169,  236,  303,  370,  437,  504,  571,  638,  705,  772,  839,  906,  973, 1040,
--        1107, 1174, 1241, 1308, 1375, 1442, 1509, 1576, 1643, 1710, 1777, 1844, 1911, 1978, 2045, 2112,
--          36,  103,  170,  237,  304,  371,  438,  505,  572,  639,  706,  773,  840,  907,  974, 1041,
--        1108, 1175, 1242, 1309, 1376, 1443, 1510, 1577, 1644, 1711, 1778, 1845, 1912, 1979, 2046, 2113,
--          37,  104,  171,  238,  305,  372,  439,  506,  573,  640,  707,  774,  841,  908,  975, 1042,
--        1109, 1176, 1243, 1310, 1377, 1444, 1511, 1578, 1645, 1712, 1779, 1846, 1913, 1980, 2047, 2114,
--          38,  105,  172,  239,  306,  373,  440,  507,  574,  641,  708,  775,  842,  909,  976, 1043,
--        1110, 1177, 1244, 1311, 1378, 1445, 1512, 1579, 1646, 1713, 1780, 1847, 1914, 1981, 2048, 2115,
--          39,  106,  173,  240,  307,  374,  441,  508,  575,  642,  709,  776,  843,  910,  977, 1044,
--        1111, 1178, 1245, 1312, 1379, 1446, 1513, 1580, 1647, 1714, 1781, 1848, 1915, 1982, 2049, 2116,
--          40,  107,  174,  241,  308,  375,  442,  509,  576,  643,  710,  777,  844,  911,  978, 1045,
--        1112, 1179, 1246, 1313, 1380, 1447, 1514, 1581, 1648, 1715, 1782, 1849, 1916, 1983, 2050, 2117,
--          41,  108,  175,  242,  309,  376,  443,  510,  577,  644,  711,  778,  845,  912,  979, 1046,
--        1113, 1180, 1247, 1314, 1381, 1448, 1515, 1582, 1649, 1716, 1783, 1850, 1917, 1984, 2051, 2118,
--          42,  109,  176,  243,  310,  377,  444,  511,  578,  645,  712,  779,  846,  913,  980, 1047,
--        1114, 1181, 1248, 1315, 1382, 1449, 1516, 1583, 1650, 1717, 1784, 1851, 1918, 1985, 2052, 2119,
--          43,  110,  177,  244,  311,  378,  445,  512,  579,  646,  713,  780,  847,  914,  981, 1048,
--        1115, 1182, 1249, 1316, 1383, 1450, 1517, 1584, 1651, 1718, 1785, 1852, 1919, 1986, 2053, 2120,
--          44,  111,  178,  245,  312,  379,  446,  513,  580,  647,  714,  781,  848,  915,  982, 1049,
--        1116, 1183, 1250, 1317, 1384, 1451, 1518, 1585, 1652, 1719, 1786, 1853, 1920, 1987, 2054, 2121,
--          45,  112,  179,  246,  313,  380,  447,  514,  581,  648,  715,  782,  849,  916,  983, 1050,
--        1117, 1184, 1251, 1318, 1385, 1452, 1519, 1586, 1653, 1720, 1787, 1854, 1921, 1988, 2055, 2122,
--          46,  113,  180,  247,  314,  381,  448,  515,  582,  649,  716,  783,  850,  917,  984, 1051,
--        1118, 1185, 1252, 1319, 1386, 1453, 1520, 1587, 1654, 1721, 1788, 1855, 1922, 1989, 2056, 2123,
--          47,  114,  181,  248,  315,  382,  449,  516,  583,  650,  717,  784,  851,  918,  985, 1052,
--        1119, 1186, 1253, 1320, 1387, 1454, 1521, 1588, 1655, 1722, 1789, 1856, 1923, 1990, 2057, 2124,
--          48,  115,  182,  249,  316,  383,  450,  517,  584,  651,  718,  785,  852,  919,  986, 1053,
--        1120, 1187, 1254, 1321, 1388, 1455, 1522, 1589, 1656, 1723, 1790, 1857, 1924, 1991, 2058, 2125,
--          49,  116,  183,  250,  317,  384,  451,  518,  585,  652,  719,  786,  853,  920,  987, 1054,
--        1121, 1188, 1255, 1322, 1389, 1456, 1523, 1590, 1657, 1724, 1791, 1858, 1925, 1992, 2059, 2126,
--          50,  117,  184,  251,  318,  385,  452,  519,  586,  653,  720,  787,  854,  921,  988, 1055,
--        1122, 1189, 1256, 1323, 1390, 1457, 1524, 1591, 1658, 1725, 1792, 1859, 1926, 1993, 2060, 2127,
--          51,  118,  185,  252,  319,  386,  453,  520,  587,  654,  721,  788,  855,  922,  989, 1056,
--        1123, 1190, 1257, 1324, 1391, 1458, 1525, 1592, 1659, 1726, 1793, 1860, 1927, 1994, 2061, 2128,
--          52,  119,  186,  253,  320,  387,  454,  521,  588,  655,  722,  789,  856,  923,  990, 1057,
--        1124, 1191, 1258, 1325, 1392, 1459, 1526, 1593, 1660, 1727, 1794, 1861, 1928, 1995, 2062, 2129,
--          53,  120,  187,  254,  321,  388,  455,  522,  589,  656,  723,  790,  857,  924,  991, 1058,
--        1125, 1192, 1259, 1326, 1393, 1460, 1527, 1594, 1661, 1728, 1795, 1862, 1929, 1996, 2063, 2130,
--          54,  121,  188,  255,  322,  389,  456,  523,  590,  657,  724,  791,  858,  925,  992, 1059,
--        1126, 1193, 1260, 1327, 1394, 1461, 1528, 1595, 1662, 1729, 1796, 1863, 1930, 1997, 2064, 2131,
--          55,  122,  189,  256,  323,  390,  457,  524,  591,  658,  725,  792,  859,  926,  993, 1060,
--        1127, 1194, 1261, 1328, 1395, 1462, 1529, 1596, 1663, 1730, 1797, 1864, 1931, 1998, 2065, 2132,
--          56,  123,  190,  257,  324,  391,  458,  525,  592,  659,  726,  793,  860,  927,  994, 1061,
--        1128, 1195, 1262, 1329, 1396, 1463, 1530, 1597, 1664, 1731, 1798, 1865, 1932, 1999, 2066, 2133,
--          57,  124,  191,  258,  325,  392,  459,  526,  593,  660,  727,  794,  861,  928,  995, 1062,
--        1129, 1196, 1263, 1330, 1397, 1464, 1531, 1598, 1665, 1732, 1799, 1866, 1933, 2000, 2067, 2134,
--          58,  125,  192,  259,  326,  393,  460,  527,  594,  661,  728,  795,  862,  929,  996, 1063,
--        1130, 1197, 1264, 1331, 1398, 1465, 1532, 1599, 1666, 1733, 1800, 1867, 1934, 2001, 2068, 2135,
--          59,  126,  193,  260,  327,  394,  461,  528,  595,  662,  729,  796,  863,  930,  997, 1064,
--        1131, 1198, 1265, 1332, 1399, 1466, 1533, 1600, 1667, 1734, 1801, 1868, 1935, 2002, 2069, 2136,
--          60,  127,  194,  261,  328,  395,  462,  529,  596,  663,  730,  797,  864,  931,  998, 1065,
--        1132, 1199, 1266, 1333, 1400, 1467, 1534, 1601, 1668, 1735, 1802, 1869, 1936, 2003, 2070, 2137,
--          61,  128,  195,  262,  329,  396,  463,  530,  597,  664,  731,  798,  865,  932,  999, 1066,
--        1133, 1200, 1267, 1334, 1401, 1468, 1535, 1602, 1669, 1736, 1803, 1870, 1937, 2004, 2071, 2138,
--          62,  129,  196,  263,  330,  397,  464,  531,  598,  665,  732,  799,  866,  933, 1000, 1067,
--        1134, 1201, 1268, 1335, 1402, 1469, 1536, 1603, 1670, 1737, 1804, 1871, 1938, 2005, 2072, 2139,
--          63,  130,  197,  264,  331,  398,  465,  532,  599,  666,  733,  800,  867,  934, 1001, 1068,
--        1135, 1202, 1269, 1336, 1403, 1470, 1537, 1604, 1671, 1738, 1805, 1872, 1939, 2006, 2073, 2140,
--          64,  131,  198,  265,  332,  399,  466,  533,  600,  667,  734,  801,  868,  935, 1002, 1069,
--        1136, 1203, 1270, 1337, 1404, 1471, 1538, 1605, 1672, 1739, 1806, 1873, 1940, 2007, 2074, 2141,
--          65,  132,  199,  266,  333,  400,  467,  534,  601,  668,  735,  802,  869,  936, 1003, 1070,
--        1137, 1204, 1271, 1338, 1405, 1472, 1539, 1606, 1673, 1740, 1807, 1874, 1941, 2008, 2075, 2142,
--          66,  133,  200,  267,  334,  401,  468,  535,  602,  669,  736,  803,  870,  937, 1004, 1071,
--        1138, 1205, 1272, 1339, 1406, 1473, 1540, 1607, 1674, 1741, 1808, 1875, 1942, 2009, 2076, 2143
--    );

    ----------------------------------------------------------------------------
    -- BIT-LEVEL INTERLEAVER (67x4) - For LibreSDR, etc.
    -- Consecutive input bits end up 67 positions apart in output.
    ----------------------------------------------------------------------------
    FUNCTION interleave_address_bit(bit_addr : NATURAL) RETURN NATURAL IS
        -- 67 rows × 32 columns = 2144 bits
        -- Write by rows, read by columns
        CONSTANT NUM_ROWS : NATURAL := 67;
        CONSTANT NUM_COLS : NATURAL := 32;
        VARIABLE row, col : NATURAL;
    BEGIN
        -- Input bit_addr is linear (row-major order: row 0 bits, then row 1, etc.)
        row := bit_addr / NUM_COLS;
        col := bit_addr MOD NUM_COLS;
        
        -- Output in column-major order (column 0 bits, then column 1, etc.)
        RETURN col * NUM_ROWS + row;
    END FUNCTION;

    ----------------------------------------------------------------------------
    -- BYTE-LEVEL INTERLEAVER (67x4) - For PlutoSDR, fits in xc7z010
    ----------------------------------------------------------------------------
    FUNCTION interleave_address_byte(addr : NATURAL) RETURN NATURAL IS
        CONSTANT ROWS : NATURAL := 67;
        CONSTANT COLS : NATURAL := 4;
        VARIABLE row : NATURAL;
        VARIABLE col : NATURAL;
    BEGIN
        row := addr / COLS;
        col := addr MOD COLS;
        RETURN col * ROWS + row;
    END FUNCTION;





BEGIN 

    -- to find the state of the state machine for debug
    debug_state <= "000" WHEN state = IDLE ELSE
               "001" WHEN state = COLLECT ELSE
               "010" WHEN state = RANDOMIZE ELSE
               "011" WHEN state = PREP_FEC ELSE
               "100" WHEN state = FEC_ENCODE ELSE
               "101" WHEN state = INTERLEAVE ELSE
               "110" WHEN state = OUTPUT ELSE
               "111";

    -- Convolutional Encoder Instantiation
    U_ENCODER : ENTITY work.conv_encoder_k7
        GENERIC MAP (
            PAYLOAD_BYTES => PAYLOAD_BYTES,
            ENCODED_BYTES => ENCODED_BYTES
        )
        PORT MAP (
            clk           => clk,
            aresetn       => aresetn,
            start         => encoder_start,
            busy          => encoder_busy,
            done          => encoder_done,
            input_buffer  => encoder_input_buf,
            output_buffer => encoder_output_buf
        );

    -- AXI-Stream output assignments
    s_axis_tready  <= s_axis_tready_reg;
    m_axis_tdata   <= m_axis_tdata_reg;
    m_axis_tvalid  <= m_axis_tvalid_reg;
    m_axis_tlast   <= m_axis_tlast_reg;
    
    -- Status outputs
    frames_encoded <= std_logic_vector(frames_encoded_reg);
    encoder_active <= encoder_active_reg;

    -- Main State Machine
    PROCESS(clk, aresetn)
        VARIABLE out_bit_idx : NATURAL RANGE 0 TO 7;
    BEGIN
        IF aresetn = '0' THEN
            state <= IDLE;
            collect_idx <= 0;
            byte_idx <= 0;
            bit_idx <= 0;
            out_idx <= 0;
            s_axis_tready_reg <= '0';
            m_axis_tdata_reg <= (OTHERS => '0');
            m_axis_tvalid_reg <= '0';
            m_axis_tlast_reg <= '0';
            encoder_start <= '0';
            frames_encoded_reg <= (OTHERS => '0');
            encoder_active_reg <= '0';
            
        ELSIF rising_edge(clk) THEN
            encoder_start <= '0';
            
            CASE state IS
                
                ----------------------------------------------------------------------
                -- IDLE: Wait for first byte of frame
                ----------------------------------------------------------------------
                -- Ready to accept data. When valid data arrives, capture first byte
                -- and check for tlast (single-byte frame, unlikely but possible).
                ----------------------------------------------------------------------
                WHEN IDLE =>
                    s_axis_tready_reg <= '1';  -- Always ready in IDLE
                    m_axis_tvalid_reg <= '0';
                    m_axis_tlast_reg <= '0';
                    encoder_active_reg <= '0';
                    
                    IF s_axis_tvalid = '1' AND s_axis_tready_reg = '1' THEN
                        -- Capture first byte
                        input_buffer(0) <= s_axis_tdata;
                        collect_idx <= 1;
                        encoder_active_reg <= '1';
                        
                        -- Check for single-byte frame (shouldn't happen for 134-byte frames)
                        IF s_axis_tlast = '1' THEN
                            s_axis_tready_reg <= '0';
                            REPORT "Single-byte frame detected (unexpected)" SEVERITY WARNING;
                            byte_idx <= 0;
                            state <= RANDOMIZE;
                        ELSE
                            state <= COLLECT;
                        END IF;
                    END IF;


                ----------------------------------------------------------------------
                -- COLLECT: Gather bytes until tlast (AXI-Stream frame boundary)
                ----------------------------------------------------------------------
                -- This is the CRITICAL state that prevents byte loss!
                --
                -- Strategy:
                --   - Keep s_axis_tready = 1 (accept data)
                --   - Capture each byte to input_buffer[collect_idx]
                --   - Increment collect_idx
                --   - WATCH FOR TLAST (frame boundary marker)
                --   - When tlast seen, validate frame size and proceed to encoding
                --
                -- Why not count to 134 and ignore tlast?
                --   Because when FIFO has next frame buffered, we'd keep accepting
                --   bytes past the frame boundary, "stealing" from the next frame.
                --   This causes cascading byte loss (Frame 3 missing byte 0, 
                --   Frame 4 missing bytes 0-1, etc.)
                --
                -- TLAST is the ONLY reliable frame boundary in AXI-Stream protocol!
                ----------------------------------------------------------------------
                WHEN COLLECT =>
                    s_axis_tready_reg <= '1';  -- Keep accepting data
                    
                    IF s_axis_tvalid = '1' AND s_axis_tready_reg = '1' THEN
                        -- Capture byte
                        input_buffer(collect_idx) <= s_axis_tdata;
                        
                        -- Check for frame boundary (tlast = end of frame)
                        IF s_axis_tlast = '1' THEN
                            -- Frame complete! Stop accepting data
                            s_axis_tready_reg <= '0';
                            
                            -- Validate frame size (collect_idx is 0-indexed, so +1 for count)
                            IF collect_idx + 1 /= PAYLOAD_BYTES THEN
                                REPORT "Frame size mismatch: expected " & 
                                       INTEGER'IMAGE(PAYLOAD_BYTES) & " bytes, got " & 
                                       INTEGER'IMAGE(collect_idx + 1) & " bytes" 
                                       SEVERITY WARNING;
                            END IF;
                            
                            -- Proceed to randomization (even if size is wrong, try to process)
                            byte_idx <= 0;
                            state <= RANDOMIZE;
                        ELSE
                            -- Not end of frame yet, continue collecting
                            collect_idx <= collect_idx + 1;
                            
                            -- Safety check: prevent buffer overflow
                            IF collect_idx >= PAYLOAD_BYTES - 1 THEN
                                REPORT "Collected " & INTEGER'IMAGE(PAYLOAD_BYTES) & 
                                       " bytes but tlast not seen yet! Frame too large!" 
                                       SEVERITY ERROR;
                                s_axis_tready_reg <= '0';
                                byte_idx <= 0;
                                state <= RANDOMIZE;  -- Try to process what we have
                            END IF;
                        END IF;
                    END IF;

                -- RANDOMIZE: XOR with randomizer sequence
                WHEN RANDOMIZE =>
                    IF byte_idx < PAYLOAD_BYTES THEN
                        randomized_buffer(byte_idx) <= 
                            input_buffer(byte_idx) XOR RANDOMIZER_SEQUENCE(byte_idx);
                        byte_idx <= byte_idx + 1;
                    ELSE
                        byte_idx <= 0;
                        state <= PREP_FEC;
                    END IF;

                -- PREP_FEC: Pack randomized bytes into encoder input buffer
                WHEN PREP_FEC =>
                    IF byte_idx < PAYLOAD_BYTES THEN
                        FOR j IN 0 TO 7 LOOP
                            encoder_input_buf(byte_idx*8 + j) <= randomized_buffer(byte_idx)(j);
                        END LOOP;
                        byte_idx <= byte_idx + 1;
                    ELSE
                        encoder_start <= '1';
                        state <= FEC_ENCODE;
                    END IF;

                -- FEC_ENCODE: Wait for convolutional encoder to complete
                WHEN FEC_ENCODE =>
                    encoder_start <= '0';
                    IF encoder_done = '1' THEN
                        -- Copy encoder output to fec_buffer (MSB-first to bit-buffer)
                        FOR i IN 0 TO ENCODED_BITS-1 LOOP
                            fec_buffer(i) <= encoder_output_buf(ENCODED_BITS - 1 - i);
                        END LOOP;
                        
                        IF USE_BIT_INTERLEAVER THEN
                            bit_idx <= 0;
                        ELSE
                            byte_idx <= 0;
                        END IF;
                        state <= INTERLEAVE;
                    END IF;

                ------------------------------------------------------------------------
                -- INTERLEAVE: Dual-mode implementation
                ------------------------------------------------------------------------

WHEN INTERLEAVE =>
    IF USE_BIT_INTERLEAVER THEN
        -- BIT-LEVEL mode: Process 1 bit per clock (2144 clocks)
        IF bit_idx < ENCODED_BITS THEN
            interleaved_buffer(interleave_address_bit(bit_idx)) <= fec_buffer(bit_idx);
            bit_idx <= bit_idx + 1;
        ELSE
            out_idx <= 0;
            state <= OUTPUT;
            m_axis_tvalid_reg <= '0';
        END IF;
    ELSE
        -- BYTE-LEVEL mode: Process 1 byte per clock (268 clocks)
        IF byte_idx < ENCODED_BYTES THEN
            FOR j IN 0 TO 7 LOOP
                interleaved_buffer(interleave_address_byte(byte_idx)*8 + j) <= 
                    fec_buffer(byte_idx*8 + j);
            END LOOP;
            byte_idx <= byte_idx + 1;
        ELSE
            out_idx <= 0;
            state <= OUTPUT;
            m_axis_tvalid_reg <= '0';
        END IF;
    END IF;




                ----------------------------------------------------------------------
                -- OUTPUT: Stream interleaved bytes to modulator
                ----------------------------------------------------------------------
                -- Send encoded frame one byte at a time via AXI-Stream.
                -- Assert tlast on final byte to mark frame boundary.
                ----------------------------------------------------------------------
                WHEN OUTPUT =>
                    IF out_idx < ENCODED_BYTES THEN
                        IF m_axis_tready = '1' OR m_axis_tvalid_reg = '0' THEN
                            -- Pack 8 bits from interleaved_buffer into output byte
                            FOR j IN 0 TO 7 LOOP
                                out_bit_idx := out_idx*8 + j;
                                m_axis_tdata_reg(j) <= interleaved_buffer(out_bit_idx);
                            END LOOP;
                            m_axis_tvalid_reg <= '1';
                            
                            -- Assert tlast on final byte (AXI-Stream frame boundary)
                            IF out_idx = ENCODED_BYTES - 1 THEN
                                m_axis_tlast_reg <= '1';
                            ELSE
                                m_axis_tlast_reg <= '0';
                            END IF;
                            
                            out_idx <= out_idx + 1;
                        END IF;
                    ELSE

                        -- Frame output complete
                        IF m_axis_tready = '1' THEN
                            m_axis_tvalid_reg <= '0';
                            m_axis_tlast_reg <= '0';
                            
                            -- Pre-set ready for next frame BEFORE going to IDLE
                            -- This ensures s_axis_tready is already high when we
                            -- enter IDLE, preventing one-clock delay in handshake
                            s_axis_tready_reg <= '1';
                            
                            frames_encoded_reg <= frames_encoded_reg + 1;
                            collect_idx <= 0;
                            state <= IDLE;
                        END IF;
                    END IF;
                    
            END CASE;

        END IF;
    END PROCESS;

END ARCHITECTURE rtl;
