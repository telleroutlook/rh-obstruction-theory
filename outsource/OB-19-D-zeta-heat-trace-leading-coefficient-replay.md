# Problem OB-19 — D: independent replay of the Z_ζ leading heat-trace singularity

**Type:** computational + symbolic verification (exact Laplace-integral identities;
independent reconstruction of the Riemann-side leading singularity)

**Non-circularity:** RH is not assumed and never used. The ONLY input from the Riemann
side is the unconditional Riemann–von Mangoldt counting law `N(T)` (a count, not any zero
location). No zero ordinate is read; nothing about the critical line is assumed. The task
replays a **finite/asymptotic analytic identity** for the leading singularity coefficient,
not the operator-side theorem it is compared against.

**Why this task exists (computational-axis gate).** Theorem D's obstruction compares the
pure-power leading heat-trace singularity of an elliptic ΨDO (operator side, OB-15) with
the `t^{-1}log(1/t)` singularity of `Z_ζ` (Riemann side). The Riemann-side leading
coefficient `1/2π` and its subleading constant are the finite analytic content; they have
had no independent certified replay. This task provides one, moving the Riemann-side
computation toward INDEPENDENT-CHECKER.

---

## All definitions (self-contained — everything is here)

### The counting law and the heat sum

Let `γ_n > 0` be the positive ordinates of the nontrivial zeros of ζ, with multiplicity,
and
```
N(T) = #{n : γ_n ≤ T}.
```
The **unconditional** Riemann–von Mangoldt formula (Titchmarsh, *Theory of the Riemann
Zeta-Function*, Thm 9.4 — used as a count only, no zero location):
```
N(T) = (T/2π) log(T/2π) − T/2π + O(log T).
```
Define the zeta heat sum
```
Z_ζ(t) = Σ_{n≥1} e^{−t γ_n}   (t > 0).
```

### The Abel/Stieltjes reduction

Since `N(0) = 0` and `e^{−tu}N(u) → 0` as `u → ∞` for fixed `t > 0`, Stieltjes
integration by parts gives
```
Z_ζ(t) = ∫_{[0,∞)} e^{−tu} dN(u) = t ∫_0^∞ e^{−tu} N(u) du.
```

### Exact Laplace-integral identities (the computational core)

Write `N(u) = N_main(u) + E(u)` with
```
N_main(u) = (u/2π)(log u − log(2π) − 1),   E(u) = O(log u).
```
The two exact Laplace transforms needed (standard; to be verified independently):
```
t ∫_0^∞ e^{−tu} u du       = 1/t,
t ∫_0^∞ e^{−tu} u log u du = (1/t)(1 − γ_E − log t),
```
where `γ_E` is the Euler–Mascheroni constant. (The second follows from
`∫_0^∞ e^{−v} v log v dv = Γ'(2) = 1 − γ_E` after substituting `v = tu`.)

### The target closed form

Combining, the main-term contribution is the **exact** closed form
```
t ∫_0^∞ e^{−tu} N_main(u) du = (1/(2π t)) ( log(1/t) − γ_E − log(2π) ),
```
so
```
Z_ζ(t) = (1/(2π t)) ( log(1/t) − γ_E − log(2π) ) + O(log(1/t))     as t → 0⁺,
```
whose **leading singularity** is `(1/2π) · log(1/t)/t`. The `O(log(1/t))` remainder is the
transform of `E(u) = O(log u)`, which is `log`-suppressed relative to the leading
`log(1/t)/t` term.

---

## The claims to be verified

### V1 — The two Laplace-integral identities (symbolic/exact)

Verify, symbolically or to ≥ 25 significant digits at several `t`:
```
t ∫_0^∞ e^{−tu} u du = 1/t,
t ∫_0^∞ e^{−tu} u log u du = (1/t)(1 − γ_E − log t).
```
(E.g. confirm `∫_0^∞ e^{−v} v log v dv = 1 − γ_E` to 25 digits, then rescale.)

### V2 — The exact main-term closed form

Verify, to ≥ 25 digits at `t = 10^{−3}, 10^{−6}, 10^{−9}`, that
```
t ∫_0^∞ e^{−tu} N_main(u) du = (1/(2π t)) ( log(1/t) − γ_E − log(2π) ),
```
by evaluating both sides independently (the left side by the identities in V1 applied to
`N_main(u) = (u/2π)(log u − log 2π − 1)`; the right side directly). Confirm agreement to
≥ 25 digits. (Sanity: at `t = 10^{−6}` both equal `≈ 1 814 432.850`.)

### V3 — The leading coefficient is exactly 1/2π

Confirm that the coefficient of `log(1/t)/t` in `Z_ζ(t)` is exactly `1/(2π)` (not, e.g.,
`1/π` or `1/(4π)`). Show the ratio `Z_ζ,main(t) / [(1/2π) log(1/t)/t] → 1` as `t → 0⁺`,
and explain (per OB-15) why this ratio converges **slowly** (the subleading
`−(γ_E+log 2π)/(2π t)` term is only `log`-suppressed relative to the leading term, so the
ratio is `1 − (γ_E+log 2π)/log(1/t) + …`). Report the ratio at `t = 10^{−3}, 10^{−6},
10^{−9}` and confirm it matches `1 − (γ_E+log 2π)/log(1/t)` to leading order.

### V4 — Remainder bound

Verify that the `E(u) = O(log u)` remainder contributes only `O(log(1/t))` to `Z_ζ(t)`,
i.e. is `o(1/t)` and hence does not affect the leading `log(1/t)/t` singularity: give a
certified bound
```
| t ∫_0^∞ e^{−tu} E(u) du | ≤ C · log(1/t)   for small t,
```
using `|E(u)| ≤ A log(u+2)` (with an explicit `A` for the RvM error) and
`t ∫_0^∞ e^{−tu} log(u+2) du = O(log(1/t))`. Report `C`.

### V5 — Adversarial mutation guard

(a) Replace `N_main(u)` by `(u/2π)·log u` only (drop the `−log 2π − 1` terms): the
    leading `log(1/t)/t` coefficient must stay `1/2π` (the dropped terms are `O(u)`, i.e.
    subleading) — confirm the leading coefficient is unchanged but the subleading constant
    changes. This shows the leading coefficient depends only on the `u log u` term.
(b) Replace the counting law by a pure power `N(u) = c·u^α` (α ≠ 1, no log): confirm
    `Z(t) ~ c Γ(α+1) t^{−α}` is a **pure power with no log** — the operator-side behavior.
    This certifies that the `log(1/t)` factor is specifically produced by the `u log u`
    (i.e. `T log T`) counting law, the crux of the D obstruction.

---

## Proof skeleton to be closed (verification steps)

### Step 1 — Laplace identities (V1)
Verify the two transforms symbolically or to ≥ 25 digits. **Acceptance:** both confirmed,
or the first that disagrees.

### Step 2 — Closed form + leading coefficient (V2, V3)
Confirm the exact main-term closed form and the `1/2π` coefficient; explain slow ratio
convergence. **Acceptance:** ≥ 25-digit agreement at three `t`; ratio matches
`1 − (γ_E+log2π)/log(1/t)`.

### Step 3 — Remainder + mutations (V4, V5)
Certified remainder bound; both mutation checks. **Acceptance:** explicit `C`; (a) leading
coeff unchanged; (b) pure-power law gives no log.

---

## Acceptance criteria

1. **CONFIRMED:** V1–V5 verified in an independent implementation (symbolic, e.g. sympy,
   and/or ≥ 25-digit `mpmath`; report which). This provides INDEPENDENT-CHECKER evidence
   for the Riemann-side leading singularity of `Z_ζ` — validating ONLY the finite/
   asymptotic identity, not the operator-side no-log theorem (OB-15) nor RH.

2. **DISCREPANCY:** a stated value/coefficient does not reproduce; report the computed
   value and whether the leading `(1/2π) log(1/t)/t` still holds.

3. **INCONCLUSIVE:** if a symbolic identity cannot be closed (e.g. the `u log u`
   transform), report the achievable precision and which step blocks.

All outcomes decisive. Because the leading coefficient is a specific rational multiple of
`1/π`, a float-only check that cannot distinguish `1/2π` from nearby constants is NOT
acceptable — use symbolic or ≥ 25-digit arithmetic.

---

## Numerical anchor (sanity only — this IS the reconstruction target)

Quickest checks (the deliverable is the exact/high-precision version):
- `∫_0^∞ e^{−v} v log v dv = 1 − γ_E ≈ 0.4227843351`.
- At `t = 10^{−6}`: `Z_ζ,main(t) = (1/(2π·10^{−6}))(log(10⁶) − γ_E − log 2π) ≈ 1 814 432.85`.
- Leading-only `(1/2π)log(1/t)/t ≈ 2 198 806.80`; ratio `≈ 0.825` — the gap is the
  `−(γ_E+log2π)` subleading constant, confirming slow ratio convergence (OB-15 remark).
These anchors sanity-check the coefficient `1/2π` and the subleading constant; the full
V1–V5 exact/high-precision replay is the target.
