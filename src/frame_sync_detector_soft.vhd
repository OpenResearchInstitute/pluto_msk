------------------------------------------------------------------------------------------------------
-- Frame Sync Detector with Soft Decision Support
-- frame_sync_detector_soft.vhd
------------------------------------------------------------------------------------------------------
-- Open Research Institute - Opulent Voice Protocol
--
-- ROLE IN RECEIVE CHAIN:
--   This module sits between the MSK demodulator and the OV frame decoder. Inputs are a stream of
--   hard decision bits along with the soft decision data. There is a soft correlator, formed by a
--   24-tap finite impulse response filter. There is a byte buffer, a state machine, a soft quantizer,
--   and handshaking for frame delivery. The frame sync word is discarded after detection.
--
------------------------------------------------------------------------------------------------------
-- WHY SOFT DECISIONS MATTER:
--
--   Hard decision:  Each bit is '0' or '1' - confidence information discarded
--   Soft decision:  Each bit carries magnitude (how sure are we of the value?)
--
--   The MSK demodulator outputs rx_data_soft = F1_energy - F2_energy:
--     - Large positive is confident '0'
--     - Large negative is confident '1'
--     - Near zero is an uncertain value (this is often set to be an erasure)
--
--   By preserving this confidence through to the Viterbi decoder, we gain
--   approximately 2-3 dB in effective SNR. In D&D terms: instead of the
--   demodulator making a DC 15 check and accepting the result as a success
--   or a failure, the Viterbi gets to see the die roll in advance of the decision
--   and can use additional information from other characters in order to decide
--   what to do in battle.
--
------------------------------------------------------------------------------------------------------
-- BYTE ASSEMBLY ARCHITECTURE NOTE (why byte_v is a variable, not a signal):
--
--   Previous versions used a byte_sr signal updated in shift_proc and read in fsm_proc.
--   This caused a one-clock cross-process dependency: on the HUNTING->LOCKED transition
--   clock, shift_proc schedules the P(0) shift but fsm_proc reads the *old* byte_sr
--   (signal updates are deferred until process completion). SYNC bits contaminated bit 7
--   of the first assembled byte on every LOCKED entry.
--
--   The fix: declare byte_v as a VARIABLE inside fsm_proc. Variables update immediately
--   within a single process execution, so byte_v always reflects the current clock's
--   decision. There is no cross-process dependency, no pending-assignment ambiguity,
--   and no sync bit contamination possible.
--
--   Path                  | byte_v init                   | bit_count init
--   ----------------------|-------------------------------|---------------
--   HUNTING  -> LOCKED    | "0000000" & rx_bit_r (= P(0)) | 1
--   VSYNC OK -> LOCKED    | (others => '0')               | 0
--   VSYNC FLY-> LOCKED    | (others => '0')               | 0
--   reset                 | := (others => '0')            | 0
--
--   In the HUNTING->LOCKED path, P(0) arrives on the transition clock while the
--   state is still HUNTING. It is captured directly into byte_v on that clock.
--   bit_count is initialised to 1 to reflect this pre-loaded bit. P(0)'s soft
--   value is also captured to soft_frame_buf(0) and frame_soft_idx advanced to 1.
--
--   In the VERIFYING_SYNC->LOCKED path, the transition clock has rx_bit_r = SYNC[0]
--   (the 24th sync bit). P(0) arrives on the first LOCKED clock. byte_v is cleared
--   and bit_count starts at 0, so the first LOCKED clock loads P(0) cleanly.
--
------------------------------------------------------------------------------------------------------
-- 3-PROCESS PIPELINE (registered input architecture):
--
--   Stage 1  input_reg_proc  : Registers rx_bit, rx_bit_valid, s_axis_soft_tdata
--                              -> rx_bit_r, rx_bit_valid_r, soft_r  (1 clock latency)
--
--   Stage 2  shift_proc      : Shifts soft_sr on rx_bit_valid_r.
--                              By the time fsm_proc reads soft_sr it is fully settled.
--                              NOTE: byte_sr has been removed from this process entirely.
--
--   Stage 3  fsm_proc        : State machine + byte assembly via byte_v variable.
--                              Reads only _r and soft_sr signals - all fully settled.
--                              byte_v is a local variable: no cross-process dependency.
--
------------------------------------------------------------------------------------------------------
-- SOFT CORRELATION (the clever part):
--
--   Traditional sync detection counts bit mismatches (Hamming distance)
--   Soft correlation uses a weighted sum using confidence values
--
--   For sync word 0x02B8DB (24 bits), we compute:
--
--     correlation = sum over all values of i of (soft_sample[i] x bipolar_sync[i])
--
--   Where bipolar_sync[i] = +1 if sync bit is '0', and -1 if sync bit is '1'
--   (accounting for demodulator polarity: negative soft is '1')
--
--   Result: Sharp correlation peak when sync word aligns, with sidelobes
--   suppressed by 8:1 ratio. The Opulent Voice sync word was exhaustively searched for
--   and has an optimal Peak-to-Sidelobe Ratio. Much better detection at low SNR than hard decision.
--
------------------------------------------------------------------------------------------------------
-- STATE MACHINE:
--
--   HUNTING:        Correlate every bit. Peak detection: transition to LOCKED when
--                   corr_prev >= HUNTING_THRESHOLD and current corr is falling.
--                   On the transition clock, rx_bit_r = P(0) (first payload bit).
--   LOCKED:         Collecting PAYLOAD_BYTES bytes + PAYLOAD_BITS soft values.
--   VERIFYING_SYNC: At expected sync position, count 24 bits and check correlation.
--                   Go to LOCKED on good correlation, flywheel or hunt on miss.
--
------------------------------------------------------------------------------------------------------
-- FLYWHEEL MECHANISM:
--
--   FLYWHEEL_TOLERANCE = 2 (default): can miss 2 consecutive syncs without losing lock.
--
------------------------------------------------------------------------------------------------------
-- LOCK ACQUISITION:
--
--   LOCK_FRAMES = 3 (default): need 3 consecutive good frames before asserting lock.
--
------------------------------------------------------------------------------------------------------
-- THRESHOLD CALIBRATION:
--
--   CALIBRATION PROCEDURE:
--   1. Monitor debug_corr_peak via ILA or CSR
--   2. Transmit known frames and observe peak correlation
--   3. Set HUNTING_THRESHOLD to 70-80% of peak (conservative)
--   4. Set LOCKED_THRESHOLD to 40-50% of peak (allow flywheel margin)
--
------------------------------------------------------------------------------------------------------
-- SYNC WORD: 0x02B8DB (24 bits, MSB-first transmission)
--   PSLR 8:1, exhaustively searched, balanced 0/1 count.
--
------------------------------------------------------------------------------------------------------
-- VERSION HISTORY:
--   v1: Initial soft correlation (from frame_sync_detector.vhd)
--   v2: Added soft value buffering and m_axis_soft_bit output stream
--   v3: Calibrated quantization thresholds for loopback simulation
--   v4: Split into 3-process registered-input architecture (input_reg, shift, fsm)
--   v5: Removed byte_sr signal from shift_proc. Byte assembly moved entirely into
--       fsm_proc using a local VARIABLE (byte_v). Eliminates cross-process signal
--       latency that contaminated bit 7 of the first assembled byte on every LOCKED
--       entry. Also fixed soft_frame_buf alignment on HUNTING->LOCKED path (P(0)
--       soft value is now captured on the transition clock).
--   v6: Revised quantizer after Case of the Missing 24 dB
--
------------------------------------------------------------------------------------------------------

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.numeric_std.ALL;


ENTITY frame_sync_detector_soft IS
    GENERIC (
        SYNC_WORD          : std_logic_vector(23 DOWNTO 0) := x"02B8DB";
        PAYLOAD_BYTES      : NATURAL := 268;
        -- PERCENTAGES now, 0..100, not absolute correlation counts.
        -- 85 -> 4.2 sigma against random data;  70 -> 3.4 sigma.
        -- 0.85 admits one wrong-signed sync symbol of 24 (ratio 1 - 2p/24 = 0.917);
        -- 0.70 admits three (0.750). Hunt strictly, hold loosely.
        HUNTING_THRESHOLD  : INTEGER := 85;
        LOCKED_THRESHOLD   : INTEGER := 70;

        -- Minimum sum|soft| over the 24-tap window for the normalised
        -- correlation to mean anything. A ratio is undefined when its
        -- denominator is ~0: on a dead or squelched channel, 24 near-zero softs
        -- give corr/energy = 1.0 and the detector would hunt on nothing.
        --
        -- DERIVATION. Measured mean|soft| at the normalised operating point
        -- (GAIN_TARGET = 16000, SOFT_SHIFT = 21):
        --      21879 noiseless,  17740 at Eb/N0 = 8 dB
        -- so energy = 24 * mean|soft| = 425,760 .. 525,096.
        -- 24 * 512 = 12288 requires mean|soft| >= 512: 30.8 dB of margin.
        --
        -- ONE FLOOR IS ENOUGH. Acceptance requires corr >= 0.85*energy, so
        -- energy >= MIN implies corr >= 0.85*MIN = 10,444. The raw-correlation
        -- floor is subsumed. opv_demod.hpp carries two constants
        -- (MIN_SYNC_ENERGY = 100, RAW_SYNC_HUNTING_THRESHOLD = 5000) only
        -- because the first is mis-scaled: 100 implies a raw floor of 85, so
        -- 5000 does the real work. One properly-scaled floor replaces both.
        --
        -- Normalising a matched-filter output by the received energy is the
        -- GLRT for a signal of unknown amplitude and is CFAR in amplitude.
        -- (Robey, Fuhrmann, Kelly & Nitzberg, "A CFAR adaptive matched filter
        -- detector", IEEE Trans. AES 28(1), 1992.)
        MIN_SYNC_ENERGY    : INTEGER := 24*512;
        FLYWHEEL_TOLERANCE : NATURAL := 2;
        LOCK_FRAMES        : NATURAL := 3;
        BUFFER_DEPTH       : NATURAL := 11;
        SOFT_WIDTH         : NATURAL := 3
    );
    PORT (
        clk               : IN  std_logic;
        reset             : IN  std_logic;

        -- Input bit stream
        rx_bit            : IN  std_logic;
        rx_bit_valid      : IN  std_logic;
        s_axis_soft_tdata : IN  signed(15 DOWNTO 0);

        -- Output byte stream (268 bytes per frame, sync stripped)
        m_axis_tdata      : OUT std_logic_vector(7 DOWNTO 0);
        m_axis_tvalid     : OUT std_logic;
        m_axis_tready     : IN  std_logic;
        m_axis_tlast      : OUT std_logic;

        -- Output soft bit stream (2144 values per frame)
        m_axis_soft_bit_tdata  : OUT std_logic_vector(SOFT_WIDTH-1 DOWNTO 0);
        m_axis_soft_bit_tvalid : OUT std_logic;
        m_axis_soft_bit_tready : IN  std_logic;
        m_axis_soft_bit_tlast  : OUT std_logic;

        -- Status
        frame_sync_locked     : OUT std_logic;
        frames_received       : OUT std_logic_vector(31 DOWNTO 0);
        frame_sync_errors     : OUT std_logic_vector(31 DOWNTO 0);
        frame_buffer_overflow : OUT std_logic;

        -- Control
        demod_sync_lock       : IN std_logic;
        hunting_threshold_i   : IN std_logic_vector(31 DOWNTO 0) := std_logic_vector(to_signed(HUNTING_THRESHOLD, 32));
        locked_threshold_i    : IN std_logic_vector(31 DOWNTO 0) := std_logic_vector(to_signed(LOCKED_THRESHOLD, 32));

        -- Soft quantizer bin edges (positive magnitudes, applied symmetrically).
        -- Defaults reproduce the previously-hardcoded quantize() literals exactly,
        -- so behavior is bit-identical until a register overrides them. Live-tunable
        -- against the real hardware soft distribution (was the -12 dBFS sim calibration).
        quant_thr_1_i         : IN std_logic_vector(15 DOWNTO 0) := std_logic_vector(to_signed(500, 16));
        quant_thr_2_i         : IN std_logic_vector(15 DOWNTO 0) := std_logic_vector(to_signed(1400, 16));
        quant_thr_3_i         : IN std_logic_vector(15 DOWNTO 0) := std_logic_vector(to_signed(2800, 16));

        -- Debug
        debug_state           : OUT std_logic_vector(2 DOWNTO 0);
        debug_correlation     : OUT signed(31 DOWNTO 0);
        debug_corr_peak       : OUT signed(31 DOWNTO 0);
        debug_bit_count       : OUT std_logic_vector(31 DOWNTO 0);
        debug_missed_syncs    : OUT std_logic_vector(3 DOWNTO 0);
        debug_consecutive_good: OUT std_logic_vector(3 DOWNTO 0);
        debug_soft_current    : OUT signed(15 DOWNTO 0);
        debug_soft_quantized  : OUT std_logic_vector(SOFT_WIDTH-1 DOWNTO 0);

        -- debug_byte_v: last complete byte written to circ_buffer.
        -- byte_v is a variable inside fsm_proc and therefore invisible to
        -- simulation waveforms. This register captures byte_v at the moment
        -- bit_count = 7, giving the waveform viewer a visible proxy.
        -- Updates once per byte (every 8 valid bits in LOCKED state).
        debug_byte_v          : OUT std_logic_vector(7 DOWNTO 0);

        -- Correlator fill: number of real (post-clear) taps in the window that
        -- corr_prev/energy_prev describe. HUNTING is gated on this reaching
        -- SYNC_BITS, so during the partial-fill window after a demod_sync_lock
        -- clear this reads < SYNC_BITS and no lock can be declared. Diagnostic
        -- for the insta-lock defect: it reads 1 at the moment the old code fired.
        debug_sync_fill       : OUT std_logic_vector(4 DOWNTO 0)
    );
END ENTITY frame_sync_detector_soft;


ARCHITECTURE rtl OF frame_sync_detector_soft IS

    ----------------------------------------------------------------------------
    -- Stage 1 outputs: registered inputs (one clock delay)
    ----------------------------------------------------------------------------
    SIGNAL rx_bit_r        : std_logic := '0';
    SIGNAL rx_bit_valid_r  : std_logic := '0';
    SIGNAL soft_r          : signed(15 DOWNTO 0) := (OTHERS => '0');

    ----------------------------------------------------------------------------
    -- Stage 2: soft decision shift register (24 taps, driven by shift_proc)
    -- NOTE: byte_sr has been intentionally removed. Byte assembly is now done
    --       entirely inside fsm_proc via a local VARIABLE (byte_v). This
    --       eliminates all cross-process signal dependency for byte assembly.
    ----------------------------------------------------------------------------
    TYPE soft_array_t IS ARRAY(0 TO 23) OF signed(15 DOWNTO 0);
    SIGNAL soft_sr : soft_array_t := (OTHERS => (OTHERS => '0'));

    ----------------------------------------------------------------------------
    -- Correlation
    ----------------------------------------------------------------------------
    SIGNAL corr       : signed(31 DOWNTO 0) := (OTHERS => '0');
    -- energy = sum|soft| over the same 24 taps. corr/energy is bounded [-1,+1].
    -- 24 * 32767 = 786,408 fits in 21 bits; 100 * that fits in 27. No overflow
    -- in the 32-bit comparison below.
    SIGNAL energy      : signed(31 DOWNTO 0) := (OTHERS => '0');
    SIGNAL energy_prev : signed(31 DOWNTO 0) := (OTHERS => '0');
    CONSTANT MIN_ENERGY : signed(31 DOWNTO 0) := to_signed(MIN_SYNC_ENERGY, 32);

    -- SYNC_BITS: taps in the correlation window = width of the sync word.
    -- The normalised correlation corr/energy is only defined over a FULL window;
    -- over a partially-filled window (single non-zero tap) it is trivially 1.0.
    -- The C++ golden reference guards this: "if (total_symbols_ < SYNC_BITS)".
    CONSTANT SYNC_BITS : natural := SYNC_WORD'length;

    -- fill_prev: real-tap count of the window corr_prev/energy_prev summarise,
    -- registered in lockstep with them so all three describe the SAME window.
    -- HUNTING requires fill_prev = SYNC_BITS before it may declare a lock.
    SIGNAL fill_prev : unsigned(4 DOWNTO 0) := (OTHERS => '0');

    -- Sync-quality divider. debug_corr_peak used to be an UNGATED running
    -- maximum of the RAW correlation, so against noise (rms|soft| ~ 20000,
    -- corr std = sqrt(24)*rms = 98,000) it latched a 4-sigma excursion and
    -- reported it as a peak. It is the number a human reads.
    --
    -- It now reports the NORMALISED quality of the last ACCEPTED sync, in
    -- percent: floor(100*corr/energy), 85..100. That is opv_demod.hpp's
    --      sync_quality_ = prev_norm_corr_;   // quality of the PEAK
    --
    -- 7-iteration restoring divide; quotient <= 100 so 7 bits suffice. A symbol
    -- is 1845 clocks at 100 MHz; this takes 7. It is the ONLY divide in the
    -- block, it is debug-only, and it never gates a decision.
    SIGNAL dv_busy : std_logic := '0';
    SIGNAL dv_num  : signed(33 DOWNTO 0) := (OTHERS => '0');
    SIGNAL dv_den  : signed(33 DOWNTO 0) := (OTHERS => '0');
    SIGNAL dv_q    : unsigned(6 DOWNTO 0) := (OTHERS => '0');
    SIGNAL dv_i    : integer RANGE 0 TO 6 := 6;
    SIGNAL corr_prev  : signed(31 DOWNTO 0) := (OTHERS => '0');
    SIGNAL corr_peak  : signed(31 DOWNTO 0) := (OTHERS => '0');

    -- Bit count (State machine)
    SIGNAL bit_count      : unsigned(2 DOWNTO 0) := (OTHERS => '0');

    -- Sync verification counter
    SIGNAL sync_bit_count : unsigned(4 DOWNTO 0) := (OTHERS => '0');

    -- State machine
    TYPE state_t IS (HUNTING, LOCKED, VERIFYING_SYNC);
    SIGNAL state : state_t := HUNTING;

    -- Frame buffer (byte circular buffer)
    CONSTANT BUFFER_SIZE : NATURAL := 2**BUFFER_DEPTH;
    CONSTANT PAYLOAD_BITS : NATURAL := PAYLOAD_BYTES * 8;
    TYPE byte_buffer_t IS ARRAY(0 TO BUFFER_SIZE-1) OF std_logic_vector(7 DOWNTO 0);
    SIGNAL circ_buffer : byte_buffer_t;
    ATTRIBUTE ram_style : STRING;
    ATTRIBUTE ram_style OF circ_buffer : SIGNAL IS "block";

    -- Soft frame buffer (one frame: PAYLOAD_BITS x SOFT_WIDTH bits)
    TYPE soft_buffer_t IS ARRAY(0 TO PAYLOAD_BITS-1) OF
        std_logic_vector(SOFT_WIDTH-1 DOWNTO 0);
    SIGNAL soft_frame_buf : soft_buffer_t := (OTHERS => (OTHERS => '0'));
    ATTRIBUTE ram_style OF soft_frame_buf : SIGNAL IS "block";

    SIGNAL wr_ptr          : unsigned(BUFFER_DEPTH-1 DOWNTO 0) := (OTHERS => '0');
    SIGNAL rd_ptr          : unsigned(BUFFER_DEPTH-1 DOWNTO 0) := (OTHERS => '0');
    SIGNAL frame_start_ptr : unsigned(BUFFER_DEPTH-1 DOWNTO 0) := (OTHERS => '0');
    SIGNAL frame_byte_count : natural range 0 to PAYLOAD_BYTES := 0;
    SIGNAL frame_soft_idx   : natural range 0 to PAYLOAD_BITS  := 0;

    -- Frame handshake
    SIGNAL frame_ready  : std_logic := '0';
    SIGNAL frame_ack    : std_logic := '0';
    SIGNAL frame_rd_ptr : unsigned(BUFFER_DEPTH-1 DOWNTO 0) := (OTHERS => '0');

    -- Output state
    SIGNAL output_active      : std_logic := '0';
    SIGNAL output_count       : natural range 0 to PAYLOAD_BYTES := 0;
    SIGNAL soft_output_active : std_logic := '0';
    SIGNAL soft_output_count  : natural range 0 to PAYLOAD_BITS := 0;
    SIGNAL tvalid_int         : std_logic := '0';
    SIGNAL tlast_int          : std_logic := '0';
    SIGNAL soft_tvalid_int    : std_logic := '0';
    SIGNAL soft_tlast_int     : std_logic := '0';

    -- Status
    SIGNAL lock_status       : std_logic := '0';
    SIGNAL acquiring_lock    : std_logic := '1';
    SIGNAL consecutive_good  : natural range 0 to LOCK_FRAMES := 0;
    SIGNAL missed_sync_count : natural range 0 to FLYWHEEL_TOLERANCE+1 := 0;
    SIGNAL frames_count      : unsigned(31 DOWNTO 0) := (OTHERS => '0');
    SIGNAL errors_count      : unsigned(31 DOWNTO 0) := (OTHERS => '0');

    -- Control
    SIGNAL demod_sync_lock_d : std_logic := '0';

    -- Debug
    SIGNAL bits_received : unsigned(31 DOWNTO 0) := (OTHERS => '0');
    SIGNAL debug_byte_v_reg : std_logic_vector(7 DOWNTO 0) := (OTHERS => '0');

    ----------------------------------------------------------------------------
    -- calc_corr: correlation over the 24-tap soft shift register.
    --
    -- IMPORTANT: soft_sr is updated in shift_proc on the same clock that
    -- fsm_proc runs. Because these are separate processes, fsm_proc sees
    -- soft_sr(0..22) from the *previous* clock's shift. The current clock's
    -- new sample has not yet settled into soft_sr(0). We therefore pass the
    -- current registered soft value (soft_r) explicitly as 'newest' and use
    -- it for position 0, with soft_sr(0..22) covering positions 1..23.
    --
    -- After the pipeline settles:
    --   newest   = soft_r             = sample for the bit arriving this clock
    --   sr(0)    = soft_sr(0)         = sample from one clock ago
    --   sr(i)    = soft_sr(i)         = sample from i+1 clocks ago
    --   sr(22)   = soft_sr(22)        = sample for SYNC_WORD(23) at peak
    --
    -- MSB-first transmission: SYNC_WORD(23) is transmitted first and shifts to
    -- position 23; SYNC_WORD(0) is transmitted last and arrives at position 0.
    ----------------------------------------------------------------------------
    FUNCTION calc_corr(sr : soft_array_t; newest : signed(15 DOWNTO 0)) RETURN signed IS
        VARIABLE sum    : signed(31 DOWNTO 0) := (OTHERS => '0');
        VARIABLE sample : signed(15 DOWNTO 0);
    BEGIN
        FOR i IN 0 TO 23 LOOP
            IF i = 0 THEN
                sample := newest;
            ELSE
                sample := sr(i-1);
            END IF;
            IF SYNC_WORD(i) = '1' THEN
                sum := sum - resize(sample, 32);  -- expect negative soft
            ELSE
                sum := sum + resize(sample, 32);  -- expect positive soft
            END IF;
        END LOOP;
        RETURN sum;
    END FUNCTION;

    ----------------------------------------------------------------------------
    -- calc_energy: sum of |soft| over the SAME 24 taps calc_corr uses.
    --
    -- WHY THIS EXISTS
    --   corr = sum(soft * pattern) is an ABSOLUTE number. It scales with the
    --   signal level AND with the SNR, so a fixed threshold cannot be right at
    --   more than one operating point. Measured on real frames at Eb/N0 = 8 dB:
    --
    --     five consecutive sync peaks: 463464 352119 350869 477890 369486
    --     spread 32% frame to frame.
    --
    --   Only the FIRST peak has to clear HUNT; once LOCKED the detector verifies
    --   at the expected position. FS_HUNT = 425554 demanded a ratio of 0.918 --
    --   ZERO wrong-signed sync symbols out of 24. At Eb/N0 = 8 dB (raw BER 3.8%)
    --   that is 39% of sync words, so acquisition took 2.5 frames instead of the
    --   1.3 that 0.85 gives. Every PTT pays that, twice over.
    --
    --   Dividing by the energy normalises the NOISE as well as the peak:
    --
    --     at perfect alignment   corr = sum|soft| = energy      -> ratio = 1.0
    --     against random data    E[corr] = 0, std = energy/sqrt(24)
    --
    --   so a threshold expressed as a FRACTION of the energy is a constant
    --   number of sigma at every signal level and every SNR:
    --
    --     0.85 -> 4.2 sigma -> 0.20 false alarms per 13,000-offset frame
    --     0.70 -> 3.4 sigma
    --
    --   These are exactly opv_demod.hpp's SOFT_SYNC_HUNTING_THRESHOLD and
    --   SOFT_SYNC_LOCKED_THRESHOLD, and they are why the C++ demodulator locks
    --   over 65 dB of attenuation with no threshold ever being retuned.
    --
    -- NO DIVIDER IS NEEDED. corr >= k*energy is a comparison:
    --     100 * corr  >=  PCT * energy
    ----------------------------------------------------------------------------
    FUNCTION calc_energy(sr : soft_array_t; newest : signed(15 DOWNTO 0)) RETURN signed IS
        VARIABLE sum    : signed(31 DOWNTO 0) := (OTHERS => '0');
        VARIABLE sample : signed(15 DOWNTO 0);
    BEGIN
        FOR i IN 0 TO 23 LOOP
            IF i = 0 THEN
                sample := newest;
            ELSE
                sample := sr(i-1);
            END IF;
            IF sample < 0 THEN
                sum := sum - resize(sample, 32);
            ELSE
                sum := sum + resize(sample, 32);
            END IF;
        END LOOP;
        RETURN sum;
    END FUNCTION;

    ----------------------------------------------------------------------------
    -- quantize: 16-bit signed soft -> 3-bit unsigned for Viterbi decoder
    --
    -- Polarity: negative soft = '1', positive soft = '0'.
    -- Thresholds calibrated for loopback simulation (~+/- 3340 nominal soft range).
    -- Adjust for hardware deployment based on observed rx_data_soft distribution.
    --
    --   Code | Meaning       | Soft range
    --   -----|---------------|--------------------
    --   111  | Strong '1'    | soft < -2800
    --   101  | Medium '1'    | -2800 <= soft < -1400
    --   100  | Weak '1'      | -1400 <= soft < -500
    --   011  | Uncertain     | -500 <= soft < +500
    --   010  | Weak '0'      |  500 <= soft < +1400
    --   001  | Medium '0'    |  1400 <= soft < +2800
    --   000  | Strong '0'    | soft >= +2800
    --
    -- Thresholds for -6 dBFS (~±5,766 nominal soft range)
    --IF    soft < -4840 THEN RETURN "111";
    --ELSIF soft < -2420 THEN RETURN "101";
    --ELSIF soft <  -860 THEN RETURN "100";
    --ELSIF soft <   860 THEN RETURN "011";
    --ELSIF soft <  2420 THEN RETURN "010";
    --ELSIF soft <  4840 THEN RETURN "001";
    --ELSE                    RETURN "000";
    ----------------------------------------------------------------------------

    -- Soft quantizer. Bin edges are now ARGUMENTS (was hardcoded ±500/1400/2800,
    -- the -12 dBFS / ±3340 sim calibration). Pass the live register values so the
    -- edges track the real hardware soft distribution. With thr1/2/3 = 500/1400/2800
    -- this is bit-identical to the original function.
    --   thr1 = innermost (erasure edge), thr3 = outermost (strong edge).
    FUNCTION quantize(soft : signed(15 DOWNTO 0);
                      thr1 : signed(15 DOWNTO 0);
                      thr2 : signed(15 DOWNTO 0);
                      thr3 : signed(15 DOWNTO 0)) RETURN std_logic_vector IS
    BEGIN
        IF    soft <= -thr3 THEN RETURN "111";   -- 7
        ELSIF soft <= -thr2 THEN RETURN "110";   -- 6  (was 5; 6 was unreachable)
        ELSIF soft <= -thr1 THEN RETURN "101";   -- 5  (was 4)
        ELSIF soft <=  0    THEN RETURN "100";   -- 4  (was 3 -- WRONG SIGN)
        ELSIF soft <   thr1 THEN RETURN "011";   -- 3
        ELSIF soft <   thr2 THEN RETURN "010";   -- 2
        ELSIF soft <   thr3 THEN RETURN "001";   -- 1
        ELSE                     RETURN "000";   -- 0
        END IF;
    END FUNCTION;

BEGIN

    -- Static output connections
    frame_sync_locked <= lock_status;
    frames_received   <= std_logic_vector(frames_count);
    frame_sync_errors <= std_logic_vector(errors_count);
    m_axis_tvalid     <= tvalid_int;
    m_axis_tlast      <= tlast_int;
    m_axis_soft_bit_tvalid <= soft_tvalid_int;
    m_axis_soft_bit_tlast  <= soft_tlast_int;

    WITH state SELECT debug_state <=
        "001" WHEN HUNTING,
        "010" WHEN LOCKED,
        "011" WHEN VERIFYING_SYNC,
        "000" WHEN OTHERS;

    debug_correlation <= corr;
    debug_corr_peak   <= corr_peak;
    debug_bit_count   <= std_logic_vector(bits_received);
    debug_missed_syncs      <= std_logic_vector(to_unsigned(missed_sync_count, 4));
    debug_consecutive_good  <= std_logic_vector(to_unsigned(consecutive_good, 4));
    debug_soft_current      <= soft_r;
    debug_soft_quantized    <= quantize(soft_r, signed(quant_thr_1_i), signed(quant_thr_2_i), signed(quant_thr_3_i));
    debug_byte_v            <= debug_byte_v_reg;
    debug_sync_fill         <= std_logic_vector(fill_prev);

    ----------------------------------------------------------------------------
    -- Stage 1: Input registration
    -- Runs every clock. Produces rx_bit_r, rx_bit_valid_r, soft_r.
    -- One clock delay; all downstream stages read only these settled signals.
    ----------------------------------------------------------------------------
    input_reg_proc : PROCESS(clk)
    BEGIN
        IF rising_edge(clk) THEN
            IF reset = '1' THEN
                rx_bit_r       <= '0';
                rx_bit_valid_r <= '0';
                soft_r         <= (OTHERS => '0');
            ELSE
                rx_bit_r       <= rx_bit;
                rx_bit_valid_r <= rx_bit_valid;
                soft_r         <= s_axis_soft_tdata;
            END IF;
        END IF;
    END PROCESS input_reg_proc;

    ----------------------------------------------------------------------------
    -- Stage 2: Soft shift register
    -- Runs on every rx_bit_valid_r pulse.
    -- soft_sr is fully settled by the time fsm_proc reads it (same clock, but
    -- fsm_proc uses soft_sr(0..22) for positions 1..23 and soft_r for position 0,
    -- so there is no dependency on this clock's soft_sr update - see calc_corr).
    --
    -- NOTE: byte_sr has been removed from this process. Byte assembly is
    --       performed entirely by the byte_v variable inside fsm_proc.
    ----------------------------------------------------------------------------
    shift_proc : PROCESS(clk)
    BEGIN
        IF rising_edge(clk) THEN
            IF reset = '1' THEN
                FOR i IN 0 TO 23 LOOP
                    soft_sr(i) <= (OTHERS => '0');
                END LOOP;
                bits_received <= (OTHERS => '0');
            ELSIF demod_sync_lock = '1' AND demod_sync_lock_d = '0' THEN
                FOR i IN 0 TO 23 LOOP
                    soft_sr(i) <= (OTHERS => '0');
                END LOOP;
            ELSIF rx_bit_valid_r = '1' THEN
                -- Shift soft register: position 0 = most recently registered sample
                FOR i IN 23 DOWNTO 1 LOOP
                    soft_sr(i) <= soft_sr(i-1);
                END LOOP;
                soft_sr(0)    <= soft_r;
                bits_received <= bits_received + 1;
            END IF;
        END IF;
    END PROCESS shift_proc;

    ----------------------------------------------------------------------------
    -- Stage 3: State machine + byte assembly
    --
    -- Reads only: rx_bit_r, rx_bit_valid_r, soft_r, soft_sr (all settled).
    -- Writes: circ_buffer, soft_frame_buf, frame control signals, status.
    --
    -- byte_v is declared as a VARIABLE so updates take effect IMMEDIATELY
    -- within this process execution. There is no pending-assignment ambiguity
    -- and no cross-process signal dependency.
    --
    -- Byte assembly invariant:
    --   bit_count tells how many bits are already in byte_v at process entry.
    --   We always shift rx_bit_r into byte_v first, then check bit_count.
    --   When the old bit_count equals 7 (i.e., byte_v just received its 8th
    --   bit via the shift), byte_v holds a complete, clean byte ready to write.
    --
    -- bit_count initialisation summary:
    --   HUNTING->LOCKED  : byte_v pre-loaded with P(0); bit_count <= 1.
    --                      First LOCKED clock has rx_bit_r = P(1).
    --                      Byte write fires when bit_count = 7 (after P(7)).
    --   VSYNC->LOCKED    : byte_v cleared; bit_count <= 0.
    --                      First LOCKED clock has rx_bit_r = P(0).
    --                      Byte write fires when bit_count = 7 (after P(7)).
    --
    -- Total payload bits per LOCKED session is always PAYLOAD_BITS (2144):
    --   HUNTING path:  1 (P(0) in HUNTING) + 7 (P(1)..P(7)) + 267*8 = 2144
    --   VSYNC path:    8 (P(0)..P(7)) + 267*8 = 2144
    ----------------------------------------------------------------------------
    fsm_proc : PROCESS(clk)
        VARIABLE corr_v : signed(31 DOWNTO 0);
        VARIABLE engy_v   : signed(31 DOWNTO 0);   -- sum|soft| over the same 24 taps
        -- byte_v: local shift register for byte assembly.
        -- MSB-first: newest bit enters at bit 0, oldest is at bit 7.
        -- After 8 shifts, byte_v(7) = first received bit (MSB), byte_v(0) = last.
        -- Variable persists between process executions (retains value across clocks).
        VARIABLE byte_v : std_logic_vector(7 DOWNTO 0) := (OTHERS => '0');
        VARIABLE dv_t   : signed(33 DOWNTO 0);
        -- fill_v: real taps in THIS clock's corr_v window (includes soft_r).
        -- Persists across clocks (like byte_v). Reset to 0 on the clear event;
        -- saturates at SYNC_BITS. fill_prev is registered from this.
        VARIABLE fill_v : natural range 0 TO 24 := 0;
    BEGIN
        IF rising_edge(clk) THEN
            ------------------------------------------------------------------
            -- Sync-quality divider: corr_peak <= floor(100*corr/energy), 0..100.
            -- Started only on an ACCEPTED sync. Debug only; gates nothing.
            -- It lives in this process because corr_peak may have one driver.
            ------------------------------------------------------------------
            IF reset = '1' THEN
                dv_busy <= '0';
                dv_i    <= 6;
                dv_q    <= (OTHERS => '0');
            ELSIF dv_busy = '1' THEN
                dv_t := dv_num - shift_left(dv_den, dv_i);
                IF dv_t >= 0 THEN
                    dv_num     <= dv_t;
                    dv_q(dv_i) <= '1';
                END IF;
                IF dv_i = 0 THEN
                    dv_busy <= '0';
                    -- dv_q(0) was just written by the loop body above on this same
                    -- clock if dv_t >= 0, so the finished quotient is simply dv_q.
                    IF dv_t >= 0 THEN
                        corr_peak <= resize(signed('0' & (dv_q(6 DOWNTO 1) & '1')), 32);
                    ELSE
                        corr_peak <= resize(signed('0' & dv_q), 32);
                    END IF;
                ELSE
                    dv_i <= dv_i - 1;
                END IF;
            END IF;

            IF reset = '1' THEN
                state            <= HUNTING;
                bit_count        <= (OTHERS => '0');
                sync_bit_count   <= (OTHERS => '0');
                wr_ptr           <= (OTHERS => '0');
                frame_start_ptr  <= (OTHERS => '0');
                frame_byte_count <= 0;
                frame_soft_idx   <= 0;
                frame_ready      <= '0';
                frames_count     <= (OTHERS => '0');
                errors_count     <= (OTHERS => '0');
                lock_status      <= '0';
                acquiring_lock   <= '1';
                consecutive_good <= 0;
                missed_sync_count <= 0;
                corr             <= (OTHERS => '0');
                corr_prev        <= (OTHERS => '0');
                corr_peak        <= (OTHERS => '0');
                frame_buffer_overflow <= '0';
                byte_v           := (OTHERS => '0');  -- variable initialisation on reset
                fill_v           := 0;
                fill_prev        <= (OTHERS => '0');
            ELSE
                frame_buffer_overflow <= '0';
                demod_sync_lock_d <= demod_sync_lock;
                IF demod_sync_lock = '1' AND demod_sync_lock_d = '0' THEN
                    corr_prev   <= (OTHERS => '0');
                    energy_prev <= (OTHERS => '0');
                    corr <= (OTHERS => '0');
                    corr_peak <= (OTHERS => '0');
                    -- Correlator window (soft_sr) is zeroed by shift_proc on this
                    -- same edge; the real-tap count must restart with it.
                    fill_v      := 0;
                    fill_prev   <= (OTHERS => '0');
                END IF;
                IF frame_ack = '1' THEN
                    frame_ready <= '0';
                END IF;

                IF rx_bit_valid_r = '1' THEN

                    -- Correlation over settled soft_sr + current soft_r
                    corr_v := calc_corr(soft_sr, soft_r);
                    engy_v := calc_energy(soft_sr, soft_r);
                    corr   <= corr_v;
                    energy <= engy_v;

                    -- Account this sample in the window fill. soft_r is tap 0 of
                    -- corr_v, so after this increment fill_v is exactly the real
                    -- tap count of corr_v. Skip on the clear edge (soft_sr was
                    -- just zeroed and fill_v reset to 0 above).
                    IF NOT (demod_sync_lock = '1' AND demod_sync_lock_d = '0') THEN
                        IF fill_v < SYNC_BITS THEN
                            fill_v := fill_v + 1;
                        END IF;
                    END IF;

                    -- Start the sync-quality divide ONLY on a genuine accept, and
                    -- ONLY once the demodulator is symbol-locked. corr_peak is the
                    -- quality of an ACCEPTED sync; before symbol lock there is no
                    -- sync to have quality, and letting the divider free-run on
                    -- preamble noise pins it at 100 from t=0 (debug lies, gates
                    -- nothing, but lies). This mirrors the lock decision, which
                    -- reads corr_prev/energy_prev -- both gated to zero unless
                    -- demod_sync_lock has been high for two clocks.
                    IF dv_busy = '0' AND demod_sync_lock = '1' AND demod_sync_lock_d = '1' AND
                       fill_v = SYNC_BITS AND
                       engy_v >= MIN_ENERGY AND
                       to_signed(100, 32) * corr_v >= signed(hunting_threshold_i) * engy_v THEN
                        dv_num  <= resize(to_signed(100, 32) * corr_v, 34);
                        dv_den  <= resize(engy_v, 34);
                        dv_q    <= (OTHERS => '0');
                        dv_i    <= 6;
                        dv_busy <= '1';
                    END IF;

                    CASE state IS

                        --------------------------------------------------------
                        -- HUNTING
                        -- Peak detection: corr_prev was the peak when it was
                        -- above threshold and the current corr has fallen.
                        --
                        -- On the transition clock:
                        --   corr_prev = peak correlation (sync word aligned)
                        --   rx_bit_r  = P(0) (first payload bit)
                        --   soft_r    = soft value for P(0)
                        --
                        -- P(0) is captured into byte_v here (in the HUNTING branch)
                        -- because this clock's state is still HUNTING. The LOCKED
                        -- branch will not execute until the next clock.
                        -- bit_count is initialised to 1 to account for P(0).
                        --------------------------------------------------------
                        WHEN HUNTING =>
                            acquiring_lock <= '1';
                            IF demod_sync_lock = '1' AND
                                demod_sync_lock_d = '1' AND
                                -- FILL GUARD: corr_prev/energy_prev are only a valid
                                -- normalised statistic over a FULL window. After a
                                -- demod_sync_lock clear the window refills one tap per
                                -- symbol; a single-tap window gives corr_prev =
                                -- energy_prev = |soft|, ratio 1.0, and would insta-lock
                                -- on noise 34 ms before the real sync word. Mirrors the
                                -- C++ reference: if (total_symbols_ < SYNC_BITS) break.
                                fill_prev = SYNC_BITS AND
                                -- NORMALISED: corr_prev >= (PCT/100) * energy_prev.
                                -- hunting_threshold_i is now a PERCENT (0..100), not a
                                -- count. 85 = 4.2 sigma against random data, at every
                                -- signal level and every SNR. See calc_energy above.
                                energy_prev >= MIN_ENERGY AND
                                to_signed(100, 32) * corr_prev >=
                                    signed(hunting_threshold_i) * energy_prev AND
                                corr_v    <=  corr_prev THEN
                                state <= LOCKED;

                                -- Capture P(0) into byte_v (variable: immediate effect)
                                byte_v        := "0000000" & rx_bit_r;
                                bit_count     <= to_unsigned(1, 3);

                                -- Capture P(0) soft value; advance soft index past slot 0

                                --soft_frame_buf(0) <= quantize(soft_r); -- P(0) soft value intentionally not captured here.
                                -- Position 0 is pre-initialized to "000" (strong '0' / erasure) in both simulation and
                                -- hardware. Writing soft_frame_buf(0) here creates a dual-write-port pattern (hardcoded
                                -- address 0 here + variable address frame_soft_idx in LOCKED) that prevents Vivado from
                                -- inferring soft_frame_buf as BRAM, costing ~4000 LUTs. One erasure out of 2144 soft
                                -- values has negligible impact on Viterbi performance (~0.01 dB coding gain loss).

                                --soft_frame_buf(0) <= quantize(soft_r);
                                frame_soft_idx    <= 1;

                                frame_byte_count <= 0;
                                frame_start_ptr  <= wr_ptr;

                                IF consecutive_good < LOCK_FRAMES - 1 THEN
                                    consecutive_good <= consecutive_good + 1;
                                ELSE
                                    lock_status    <= '1';
                                    acquiring_lock <= '0';
                                END IF;
                            END IF;

                        --------------------------------------------------------
                        -- LOCKED
                        -- Collect PAYLOAD_BYTES bytes and PAYLOAD_BITS soft values.
                        --
                        -- Byte assembly using byte_v (local variable):
                        --   1. Shift rx_bit_r into byte_v. Because byte_v is a
                        --      variable, this takes effect immediately (no clock delay).
                        --   2. Increment bit_count (signal; new value visible next clock).
                        --   3. When old bit_count = 7, byte_v now holds 8 complete bits.
                        --      Write byte_v to circ_buffer.
                        --
                        -- Soft capture: frame_soft_idx was pre-advanced to 1 in the
                        -- HUNTING->LOCKED path (P(0) captured there), so this block
                        -- correctly stores P(1) at index 1 on the first LOCKED clock.
                        -- For the VSYNC->LOCKED path frame_soft_idx = 0, so P(0) is
                        -- stored at index 0 on the first LOCKED clock. Both paths are
                        -- correctly aligned.
                        --------------------------------------------------------
                        WHEN LOCKED =>

                            -- Shift new bit into byte_v immediately (variable update)
                            byte_v    := byte_v(6 DOWNTO 0) & rx_bit_r;
                            bit_count <= bit_count + 1;

                            -- Soft value capture (arrival order; decoder handles ordering)
                            IF frame_soft_idx < PAYLOAD_BITS THEN
                                soft_frame_buf(frame_soft_idx) <= quantize(soft_r, signed(quant_thr_1_i), signed(quant_thr_2_i), signed(quant_thr_3_i));
                                frame_soft_idx <= frame_soft_idx + 1;
                            END IF;

                            IF bit_count = 7 THEN
                                -- byte_v just received its 8th bit; it is complete.
                                -- Write to circular buffer.
                                circ_buffer(to_integer(wr_ptr)) <= byte_v;
                                -- Mirror to debug signal so the waveform viewer can see it.
                                -- (byte_v is a variable and is otherwise invisible.)
                                debug_byte_v_reg <= byte_v;
                                wr_ptr    <= wr_ptr + 1;
                                bit_count <= (OTHERS => '0');

                                IF wr_ptr + 1 = rd_ptr THEN
                                    frame_buffer_overflow <= '1';
                                    errors_count <= errors_count + 1;
                                END IF;

                                IF frame_byte_count < PAYLOAD_BYTES - 1 THEN
                                    frame_byte_count <= frame_byte_count + 1;
                                ELSE
                                    -- All PAYLOAD_BYTES bytes collected.
                                    frame_byte_count <= 0;
                                    frame_soft_idx   <= 0;
                                    sync_bit_count   <= (OTHERS => '0');
                                    state            <= VERIFYING_SYNC;

                                    IF frame_ready = '0' THEN
                                        frame_ready  <= '1';
                                        frame_rd_ptr <= frame_start_ptr;
                                        frames_count <= frames_count + 1;
                                    ELSE
                                        -- Output process hasn't consumed the previous frame.
                                        errors_count <= errors_count + 1;
                                    END IF;
                                END IF;
                            END IF;

                        --------------------------------------------------------
                        -- VERIFYING_SYNC
                        -- Wait for 24 bits and check soft correlation.
                        --
                        -- sync_bit_count starts at 0 when entering this state.
                        -- On the clock where sync_bit_count = 23 (24th bit):
                        --   rx_bit_r = SYNC[0] (last bit of the 24-bit sync word)
                        --   soft_r / soft_sr are aligned with the full sync window.
                        -- The NEXT clock after transition to LOCKED has rx_bit_r = P(0).
                        --
                        -- On all transitions to LOCKED from this state, byte_v is
                        -- cleared and bit_count is set to 0, so the first LOCKED clock
                        -- (rx_bit_r = P(0)) loads cleanly into byte_v position 0.
                        --------------------------------------------------------
                        WHEN VERIFYING_SYNC =>
                            sync_bit_count <= sync_bit_count + 1;

                            IF sync_bit_count = 23 THEN
                                -- corr_v already computed above for this clock.
                                -- IF corr_v >= to_signed(LOCKED_THRESHOLD, 32) THEN -- previously a generic
                                -- NORMALISED: corr_v >= (PCT/100) * engy_v.
                                -- locked_threshold_i is now a PERCENT (0..100). 70 = 3.4 sigma.
                                IF engy_v >= MIN_ENERGY AND
                                   to_signed(100, 32) * corr_v >=
                                       signed(locked_threshold_i) * engy_v THEN
                                    -- Sync found at expected position.
                                    missed_sync_count <= 0;

                                    IF acquiring_lock = '1' THEN
                                        IF consecutive_good < LOCK_FRAMES - 1 THEN
                                            consecutive_good <= consecutive_good + 1;
                                        ELSE
                                            lock_status      <= '1';
                                            acquiring_lock   <= '0';
                                            consecutive_good <= LOCK_FRAMES;
                                        END IF;
                                    ELSE
                                        consecutive_good <= LOCK_FRAMES;
                                    END IF;

                                    state            <= LOCKED;
                                    -- rx_bit_r = SYNC[0] now; P(0) arrives next clock.
                                    -- Clear byte_v so first LOCKED clock loads P(0) cleanly.
                                    byte_v           := (OTHERS => '0');
                                    bit_count        <= (OTHERS => '0');
                                    frame_start_ptr  <= wr_ptr;
                                    frame_byte_count <= 0;
                                    frame_soft_idx   <= 0;

                                ELSE
                                    -- Missed expected sync.
                                    IF lock_status = '1' THEN
                                        IF missed_sync_count < FLYWHEEL_TOLERANCE THEN
                                            -- Flywheel: stay locked, skip this sync.
                                            missed_sync_count <= missed_sync_count + 1;
                                            state             <= LOCKED;
                                            byte_v            := (OTHERS => '0');
                                            bit_count         <= (OTHERS => '0');
                                            frame_byte_count  <= 0;
                                            frame_soft_idx    <= 0;
                                            -- FLYWHEEL FIX: re-anchor the frame start.
                                            -- Every other LOCKED entry sets frame_start_ptr;
                                            -- this branch did not, so the byte-path frame
                                            -- delivered after a flywheel was a verbatim
                                            -- REPLAY of the previous frame (frame_rd_ptr
                                            -- still pointed at the old region). The soft
                                            -- path (indexed from 0 each frame) was correct,
                                            -- which is why opv-decode -3 never saw it.
                                            -- Found by tb_fsync flywheel regression.
                                            frame_start_ptr   <= wr_ptr;
                                            errors_count      <= errors_count + 1;
                                        ELSE
                                            -- Too many misses; lose lock.
                                            lock_status       <= '0';
                                            consecutive_good  <= 0;
                                            missed_sync_count <= 0;
                                            state             <= HUNTING;
                                            errors_count      <= errors_count + 1;
                                        END IF;
                                    ELSE
                                        -- Still acquiring; any miss restarts count.
                                        consecutive_good <= 0;
                                        state            <= HUNTING;
                                        errors_count     <= errors_count + 1;
                                    END IF;
                                END IF;
                            END IF;

                        WHEN OTHERS =>
                            state <= HUNTING;

                    END CASE;

                    -- Update corr_prev at end of every valid bit for peak detection.
                    -- Gated on the demod_sync_lock signal
                    IF demod_sync_lock = '1' AND demod_sync_lock_d = '1' THEN
                        corr_prev   <= corr_v;
                        energy_prev <= engy_v;
                        fill_prev   <= to_unsigned(fill_v, fill_prev'length);
                    ELSE
                        corr_prev   <= (OTHERS => '0');
                        energy_prev <= (OTHERS => '0');
                        fill_prev   <= (OTHERS => '0');
                    END IF;
                END IF;
            END IF;
        END IF;
    END PROCESS fsm_proc;

    ----------------------------------------------------------------------------
    -- Output process: stream bytes then soft values to AXI-Stream interfaces.
    -- Unchanged from original design.
    ----------------------------------------------------------------------------
    output_proc : PROCESS(clk)
    BEGIN
        IF rising_edge(clk) THEN
            IF reset = '1' THEN
                m_axis_tdata    <= (OTHERS => '0');
                tvalid_int      <= '0';
                tlast_int       <= '0';
                output_count    <= 0;
                output_active   <= '0';
                soft_output_active <= '0';
                soft_output_count  <= 0;
                soft_tvalid_int <= '0';
                soft_tlast_int  <= '0';
                frame_ack       <= '0';
                rd_ptr          <= (OTHERS => '0');
                m_axis_soft_bit_tdata <= (OTHERS => '0');
            ELSE
                frame_ack <= '0';

                IF frame_ready = '1' AND
                   output_active = '0' AND
                   soft_output_active = '0' THEN
                    output_active <= '1';
                    rd_ptr        <= frame_rd_ptr;
                    output_count  <= 0;
                    frame_ack     <= '1';
                END IF;

                IF output_active = '1' THEN
                    IF m_axis_tready = '1' OR tvalid_int = '0' THEN
                        m_axis_tdata <= circ_buffer(to_integer(rd_ptr));
                        tvalid_int   <= '1';
                        rd_ptr       <= rd_ptr + 1;
                        IF output_count = PAYLOAD_BYTES - 1 THEN
                            tlast_int          <= '1';
                            output_active      <= '0';
                            output_count       <= 0;
                            soft_output_active <= '1';
                            soft_output_count  <= 0;
                        ELSE
                            tlast_int    <= '0';
                            output_count <= output_count + 1;
                        END IF;
                    END IF;
                ELSE
                    IF m_axis_tready = '1' THEN
                        tvalid_int <= '0';
                        tlast_int  <= '0';
                    END IF;
                END IF;

                IF soft_output_active = '1' THEN
                    IF m_axis_soft_bit_tready = '1' OR soft_tvalid_int = '0' THEN
                        m_axis_soft_bit_tdata <= soft_frame_buf(soft_output_count);
                        soft_tvalid_int <= '1';
                        IF soft_output_count = PAYLOAD_BITS - 1 THEN
                            soft_tlast_int     <= '1';
                            soft_output_active <= '0';
                            soft_output_count  <= 0;
                        ELSE
                            soft_tlast_int    <= '0';
                            soft_output_count <= soft_output_count + 1;
                        END IF;
                    END IF;
                ELSE
                    IF m_axis_soft_bit_tready = '1' THEN
                        soft_tvalid_int <= '0';
                        soft_tlast_int  <= '0';
                    END IF;
                END IF;
            END IF;
        END IF;
    END PROCESS output_proc;

END ARCHITECTURE rtl;
