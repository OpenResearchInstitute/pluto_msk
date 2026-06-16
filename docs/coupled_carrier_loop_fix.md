# Coupled Carrier Loop — kill the complex-demod beat

**Goal:** stop the two Costas loops drifting apart on a clean analytic input.
Replace the two independent carrier integrators with **one shared integrator**
that tracks the common carrier offset and steers **both** NCOs identically.
The tone spacing (`freq_word_f2 − freq_word_f1`) is fixed by the modulation, so
once both NCOs move together, `φ_f2 − φ_f1` is pinned and the symbol clock
(`dclk = sign(sin(φ_f2 − φ_f1))`) can no longer walk. The beat dies by construction.

This is a contained, **default-preserving** change. `costas_loop` gains an opt-in
generic; with it `False` (the default) the block is bit-exact to today, so the
real demod and every other user are untouched.

---

## Why this also fixes the starvation

Today each loop updates only on its own decision-switched symbols
(`error_valid_f1` on data=0, `error_valid_f2` on data=1), so each integrator
free-wheels ~half the time and the two wander relative to each other. With one
shared integrator fed by *whichever* loop is valid this symbol, the carrier loop
gets an update **every** symbol — full rate, no free-wheeling.

---

## Change 1 of 2 — `costas_loop.vhd`

### 1a. New generic (after `SAMPLE_GATED_NCO`, ~line 89)

```vhdl
        SAMPLE_GATED_NCO    : BOOLEAN := False;
        -- FALSE (default): the loop's own PI integrator drives its NCO. Bit-exact
        --   to every existing use. TRUE: the NCO is driven by an EXTERNAL common
        --   adjust (ext_adjust/ext_adjust_valid) so two loops share one carrier
        --   integrator and cannot drift apart. The internal PI is frozen (it still
        --   feeds loop_error, but no longer steers the NCO or winds up).
        EXTERNAL_NCO_ADJUST : BOOLEAN := False
```

### 1b. New ports (in the PORT list, e.g. just after `loop_error`, ~line 109)

```vhdl
        ext_adjust          : IN  std_logic_vector(NCO_W -1 DOWNTO 0) := (OTHERS => '0');
        ext_adjust_valid    : IN  std_logic := '0';
```

### 1c. New signals (architecture declarations, near `lpf_adjust`, ~line 195)

```vhdl
    SIGNAL nco_adj          : std_logic_vector(NCO_W -1 DOWNTO 0);
    SIGNAL nco_adj_valid    : std_logic;
    SIGNAL int_pi_freeze    : std_logic;
```

### 1d. Select NCO source + freeze the internal PI when external (architecture body)

```vhdl
    -- NCO is driven by the shared external adjust when coupled, else by this
    -- loop's own PI (original behavior). Default generic = original behavior.
    nco_adj       <= ext_adjust       WHEN EXTERNAL_NCO_ADJUST ELSE lpf_adjust;
    nco_adj_valid <= ext_adjust_valid WHEN EXTERNAL_NCO_ADJUST ELSE lpf_adj_valid;

    -- Freeze the internal integrator when coupled so it can't wind up to the rails
    -- (its output is unused; loop_error is computed independently of the PI).
    int_pi_freeze <= '1' WHEN EXTERNAL_NCO_ADJUST ELSE lpf_freeze;
```

### 1e. Point the internal PI's freeze at the gated signal (in `u_loopfilter` PORT MAP, ~line 471)

```vhdl
        lpf_freeze       => int_pi_freeze,   -- was: lpf_freeze
```

### 1f. Point the NCO at the selected adjust (in `U_carrier_nco` PORT MAP, ~lines 528–530)

```vhdl
        freq_adj_zero   => '0',
        freq_adj_valid  => nco_adj_valid,    -- was: lpf_adj_valid
        freq_adjust     => nco_adj,          -- was: lpf_adjust
```

That is the entire `costas_loop` change. With `EXTERNAL_NCO_ADJUST => False`,
`nco_adj = lpf_adjust`, `int_pi_freeze = lpf_freeze` — identical to today.

---

## Change 2 of 2 — `msk_demodulator.vhd`

### 2a. New signals (architecture declarations)

```vhdl
    SIGNAL ev_f1_d, ev_f2_d  : std_logic;                          -- error_valid delayed 1 clk
    SIGNAL common_err        : std_logic_vector(31 DOWNTO 0);
    SIGNAL common_err_valid  : std_logic;
    SIGNAL common_adjust     : std_logic_vector(NCO_W -1 DOWNTO 0);
    SIGNAL common_adj_valid  : std_logic;
```

### 2b. Combine the two loop errors into one stream (architecture body)

`f1_error`/`f2_error` are registered one clock after their `error_valid`
(see `obs_proc` in `costas_loop`), so align the select with a 1-clk delay of the
valids. The valids are one-hot per symbol, so this is a clean select, not a sum.

```vhdl
    err_align : PROCESS (clk)
    BEGIN
        IF rising_edge(clk) THEN
            ev_f1_d <= error_valid_f1;
            ev_f2_d <= error_valid_f2;
            IF rx_init = '1' THEN
                ev_f1_d <= '0';
                ev_f2_d <= '0';
            END IF;
        END IF;
    END PROCESS;

    -- whichever loop produced a valid error this symbol drives the shared loop
    common_err       <= f1_error WHEN ev_f1_d = '1' ELSE f2_error;
    common_err_valid <= ev_f1_d OR ev_f2_d;
```

> **Sign note (the one knob to check in sim):** a common carrier offset should
> produce the *same* error sign in both loops, so the select above is correct.
> If the beat does not collapse and the loops appear to fight, negate the f2 arm:
> `common_err <= f1_error WHEN ev_f1_d='1' ELSE std_logic_vector(-signed(f2_error));`
> That is the only sign degree of freedom in this change.

### 2c. One shared carrier integrator (architecture body)

Reuse the same `pi_controller` and the same gains the loops already use.

```vhdl
    u_carrier_filter : ENTITY work.pi_controller(rtl)
    GENERIC MAP (
        NCO_W      => NCO_W,
        ERR_W      => ERR_W,
        GAIN_W     => GAIN_W,
        ASSERT_ENA => False
    )
    PORT MAP (
        clk            => clk,
        init           => rx_init,
        enable         => rx_enable,
        lpf_p_gain     => lpf_p_gain,
        lpf_i_gain     => lpf_i_gain,
        lpf_i_shift    => lpf_i_shift,
        lpf_p_shift    => lpf_p_shift,
        lpf_freeze     => lpf_freeze,
        lpf_zero       => lpf_zero,
        lpf_err_valid  => common_err_valid,
        lpf_err        => common_err,
        lpf_adj_valid  => common_adj_valid,
        lpf_adjust     => common_adjust,
        lpf_accum      => OPEN          -- (optionally route to a debug port)
    );
```

### 2d. Drive both loops from the shared adjust (in `U_f1` and `U_f2` PORT MAPs)

Add the generic and the two new ports to **both** instances:

```vhdl
        -- in the GENERIC MAP of BOTH U_f1 and U_f2:
            EXTERNAL_NCO_ADJUST => True,

        -- in the PORT MAP of BOTH U_f1 and U_f2:
            ext_adjust       => common_adjust,
            ext_adjust_valid => common_adj_valid,
```

`rx_freq_word_f1`/`rx_freq_word_f2` stay exactly as they are — they set the fixed
tone spacing, which is the whole point. Both NCOs now = (their own seed) + (shared
adjust), so the spacing is constant and `φ_f2 − φ_f1` is pinned.

> The per-loop `f1_nco_adjust`/`f2_nco_adjust` outputs now reflect the frozen
> internal PIs and are no longer meaningful as carrier corrections. For an ILA
> trace of the *real* correction, route `common_adjust` out to a debug port.

---

## What you should see in simulation

Run `tb_msk_modem_134byte` on the complex branch with these changes.

- **`f1_nco_adjust` vs `f2_nco_adjust`** were the smoking-gun diamond/beat. With
  the shared integrator they no longer exist as independent signals; instead
  `common_adjust` should settle to a single steady CFO value with no slow envelope.
- **`dclk_slv`** (= sin(φ_f2 − φ_f1)) zero-crossing spacing should be rock-steady
  across all frames — no breathing.
- **Frames decode clean across the whole run**, not in clean/corrupted bursts.

If the beat persists *and* the two arms look like they're fighting (common_adjust
hunting hard, never settling) → flip the f2 error sign per the note in 2b and rerun.
That is the first and only thing to try before digging deeper.

---

## Rollback / safety

- The `costas_loop` change is gated entirely by `EXTERNAL_NCO_ADJUST` (default
  `False`). The real demod and all other instantiations are unaffected and remain
  bit-exact.
- To revert the complex demod to independent loops: set both instances'
  `EXTERNAL_NCO_ADJUST => False`, remove the shared `u_carrier_filter`, and restore
  `nco_adjust => f1_nco_adjust/f2_nco_adjust`. Nothing else changes.
