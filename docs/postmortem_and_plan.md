# Haifuraiya — Real-Demod Revert & Complex-RX Postmortem

**Plan of attack / session re-entry anchor**
Target: solid real-demod RX for Friedrichshafen (HAM RADIO, June 2026).
Decision: revert Haifuraiya to the real (single-port) `msk_demodulator`. The
complex-baseband-rx demod goes back to the research plane until after the demo.

---

## 1. State snapshot (where we are right now)

**Nested submodule chain** (this is what tangled the rollback — three levels deep):

```
Mode-Dynamic-Transponder            branch: main
  └─ haifuraiya/third_party/pluto_msk        DETACHED HEAD @ 7115a8b
       └─ msk_demodulator                    @ 583faed   ← real demod, VERIFIED
```

- `msk_demodulator` is parked at `583faed` ("fix(symbol_lock): extend 16-bit
  threshold register to 32-bit comparison") — the exact commit pluto_msk's
  `tx_sample_scale` pins. Verified: `rx_samples : IN …`, no `rx_i/rx_q`.
- `pluto_msk` is **detached** at `7115a8b`; it has the `msk_demodulator` pointer
  change **staged**, plus an **unstaged** edit to `src/frame_sync_detector_soft.vhd`
  (our corr_prev / threshold soft-sync fix — keep it).
- `Mode-Dynamic-Transponder` (top) sees `pluto_msk` as "modified content" — it
  can't record a clean new pointer until pluto_msk's own changes are committed.

---

## 2. Bug Hunt Trophy Case — the complex-RX beat

**Symptom.** Periodic amplitude-modulated "diamond" on `f1/f2_nco_adjust`, a slow
bowl in `lpf_accum_f1/f2`, `rx_sync_correlation` sagging on the same period, and
bursts of corrupted frames between byte-perfect clean ones (~20-frame / ~300 ms beat).

**Ruled out by measurement (do not reopen):**

- **Missing Q** — Q is plumbed and live; `rx_samples_q_dec` carries a faithful
  scaled copy of `tx_samples_Q_int` (same sign, same ratio).
- **I/Q imbalance / image** — the modulator output is a **constant-envelope
  analytic signal**: at the cursor, |TX| = √(18368² + 27120²) ≈ 32 755 (full-scale
  16-bit) and |RX| = √(1116² + 1716²) ≈ 2 047 (full-scale 12-bit). Perfect balance
  ⇒ no imbalance image to suppress.
- **Handedness / sign on Q** — negating Q only conjugates an already-clean analytic
  signal (mirrors the spectrum); it can't remove a beat that isn't an imbalance image.
- **The complex mixer itself** — diffed real vs complex `costas_loop`:
  - Mixer computes `rx_cos = car_cos·rx_i − car_sin·rx_q`,
    `rx_sin = car_sin·rx_i + car_cos·rx_q` = exactly `(car_cos+j·car_sin)·(rx_i+j·rx_q)`.
    Both parts correct, **no sign wrong**. Reduces bit-exactly to the real mixer when `rx_q = 0`.
  - Phase detector (`rx_cos_slice`, `rx_error`): byte-identical.
  - NCO output to clock recovery (`cos_samples`/`sin_samples` = `car_cos`/`car_sin`): identical.
  - Symbol-clock cross products (`cos_f1·sin_f2 − cos_f2·sin_f1`): identical, line for line.

**Root-cause hypothesis (strongest; needs a targeted sim to confirm).**
Architectural mismatch, not a coding error. Hodgart's demodulator — dual
decision-switched Costas loops plus clock recovery built from φ_f2 − φ_f1 — is
designed for a **real, double-sideband** input, where both tones are always present
(symmetric spectrum) and both loops stay continuously fed. A clean **analytic
(single-sideband)** input is single-tone-per-symbol: during an f1 symbol the +13550
tone is genuinely absent, so the f2 loop sees nothing and freewheels (and vice
versa). The two loops take turns going blind, drift in relative phase while starved,
and the symbol clock that rides on their phase difference wobbles → the beat. This
is exactly Hodgart's own data-run caveat, amplified — the analytic input removed the
image energy the real loops were leaning on.

**Implication.** The real demod is the *architecturally correct* receiver for a
Hodgart design, not merely the working one. Reverting is the right call on the merits.

---

## 3. Remaining steps (ordered)

### A. Land the real-demod pin up the submodule chain

In `haifuraiya/third_party/pluto_msk` (currently detached):

```bash
git switch -c haifuraiya-real-demod          # anchor the floating commit on a branch
git add src/frame_sync_detector_soft.vhd     # keep the soft-sync fix
git diff --cached --stat                      # expect: msk_demodulator + frame_sync_detector_soft.vhd
git commit -F /tmp/msg.txt                    # heredoc msg, e.g. "Cast REMOVE CURSE: pin real msk_demodulator 583faed + soft-sync fix"
git push origin haifuraiya-real-demod         # make the pin reproducible (others clone need this commit)
```

Then in `Mode-Dynamic-Transponder` (top, on `main`):

```bash
git add haifuraiya/third_party/pluto_msk
git diff --cached --stat                       # expect: pluto_msk pointer moved
git commit -F /tmp/msg.txt
git push
```

- The untracked `haifuraiya/*.py` and `component_v0_4.xml` are unrelated — leave
  them or add deliberately. **Do not `git add -A`** (stages untracked files).

### B. Walk back Haifuraiya's own receive RTL  ⚠️ NOT DONE YET

This is the piece the submodule re-pin does **not** cover. Haifuraiya instantiates
`msk_demodulator` in its **own** receive chain (channelizer → demod), in the
`haifuraiya/` RTL — not pluto_msk's `msk_top`.

- The real demod exposes a single real `rx_samples` port; the complex one had
  `rx_i_samples`/`rx_q_samples`. The Haifuraiya instantiation must be reverted from
  the complex wiring to the single real port, feeding the channelized bin's **real
  part**.
- If a pre-complex Haifuraiya commit exists, diff/revert against it (cleanest).
  Otherwise rewire the instantiation by hand.
- **This must land together with the demod pin** — swapping the real demod under a
  complex instantiation is a hard port-mismatch compile error.
- → Paste the Haifuraiya receive top (where `msk_demodulator` is instantiated) and
  the exact rewire can be marked.

### C. Verify

1. Port check (done ✓): `grep "rx_samples : IN" …/msk_demodulator/src/msk_demodulator.vhd`.
2. Confirm the channelized bin presents the MSK as **distinct positive tones**
   (~96.56 / 123.7 kHz, centroid ~110 kHz) — that's a valid real-IF feed for the
   real demod's real-part input (not a ±pair about DC).
3. Rebuild Haifuraiya; run the RX sim/testbench. Green = flat `nco_adjust`,
   clean byte counter, no diamond.
4. On hardware: channelizer alive (`devmem 0x84A70000` → version), demod locks.

---

## 4. Parked (post-Friedrichshafen)

- **Complex-RX research.** Confirm the loop-starvation hypothesis with a targeted
  sim: watch each loop's integrate-dump arm energy fall to ~0 through the *other*
  tone's symbols, and watch φ_f2 − φ_f1 wobble on the beat period. If confirmed, the
  complex path needs a redesign that keeps both loops fed (e.g. continuous pilot, or
  a non-Hodgart complex demod) — it is not a sign patch.
- **Frame-ordering anomaly.** First LOCKED frame carries bytes buffered during
  HUNTING (circular-buffer read-pointer off-by-one). Mundane, parked.

---

## 5. Estimates vs. measurements

- **MEASURED:** real demod green on a clean input; complex mixer math correct (diff);
  input is constant-envelope analytic; phase detector / NCO / clock recovery identical
  between branches.
- **HYPOTHESIS (not yet measured):** loop-starvation from single-sideband input as the
  beat's root cause. Confirm by sim before acting on it.
