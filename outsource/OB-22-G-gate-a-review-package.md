# Problem OB-22 — G Gate-A package: independent review of the diagonal information-obstruction

**Type:** Gate-A independent mathematical review (whole-theorem inspection, scoped).

**What this is.** A request to **independently inspect the provable core of Theorem G** —
the diagonal Fredholm information-obstruction (`G-info` on the class `𝔐_d^{tr}`) — as a
coherent whole, and issue a **Gate-A verdict**: is it correct, self-contained, non-circular,
and RH-free? The finite core (Gram levels `d_n`, three-way separation, tail bound) is
already independently certified by a deposited interval-arithmetic checker (prior review
OB-17, re-run in-repo). This review targets the **analytic assembly** around that checker.

**Scope — READ CAREFULLY (what is IN and what is explicitly OUT):**
- **IN scope (please review):** the diagonal obstruction — for `(K_N) ∈ 𝔐_d^{tr}`,
  `det(I−z²K_N) → G_d` locally uniformly and `G_d ≠ Ξ̂` unconditionally; the supporting
  Lemmas G.4 (PSD Fredholm limits have all-real zeros) and G.5 (convergence to `Ξ̂` ⟹ RH);
  and Prop G.3* Item 2 (the multiset distinctness `{d_n} ≠ {γ_n}` via Littlewood).
- **OUT of scope (do NOT attempt to prove; confirm only that it is correctly quarantined):**
  the conjecture **G-hard** ("no `P ∈ 𝔐_FC` can recover the `S(T)` data from zero-free
  arithmetic without an RH-equivalent computation"). It is marked `[CONJECTURE]` and must
  **never** be used as a premise. Your job on G-hard is only to confirm that nothing in the
  IN-scope proof secretly depends on it.
- **Factorization condition (2.7):** confirm the weak/strong distinction is handled honestly
  (see Q3) — the obstruction may use only the weak/definitional reading.

**Non-circularity (mandatory).** RH is not assumed. `γ_n` (ζ ordinates) may appear ONLY as
an external comparison input with an error radius (as in the deposited checker, from a
published table ±3e-9), never in the construction of `d_n, κ_n, G_d`, or the tail bound.
Confirm no step imports RH or an RH-equivalent.

---

## All definitions (self-contained — everything is here)

### Theta levels and the diagonal operator
`θ(t) = Im log Γ(1/4 + it/2) − (t/2)log π` (continuous branch, `θ(0)=0`), strictly
increasing for `t ≳ 6.29`. The **archimedean levels** `d_n` are the unique positive
solutions of `θ(d_n) = (n−1)π` (`d_1 ≈ 17.846, d_2 ≈ 23.170, …`; transcendental in
general). Eigenvalues `κ_n = 1/(1/4 + d_n²)`; finite-rank diagonal `D_N = diag(κ_1,…,κ_N)`.

### Fredholm determinant (corrected formula)
For finite-rank PSD `K_N` with nonzero eigenvalues `λ_j`:
`det(I − z²K_N) = ∏_j (1 − z²λ_j)`, zeros at `z = ±λ_j^{-1/2}` (NOT `±λ_j^{1/2}`).
So `det(I − z²D_N) = ∏_{n≤N}(1 − z²κ_n)`, zeros at `±√(1/4+d_n²)`.

### The three functions (kept distinct)
- `G_d(z) = ∏_{n≥1}(1 − z²/(1/4+d_n²))` — limit of `det(I−z²D_N)`; zeros `±√(1/4+d_n²)`.
- `F_d(z) = ∏_{n≥1}(1 − z²/d_n²)` — zeros `±d_n`.
- `Ξ̂(z) = ξ(1/2+iz)/ξ(1/2)`, `Ξ̂(0)=1` — normalized Riemann xi.

### The method subclass under review
`𝔐_d^{tr}` = finite-rank PSD families `(K_N)` with `K_N = Φ_N(d_1,…,d_N)` and
`‖K_N − D_N‖_1 → 0` (trace-norm). Non-empty: `K_N = D_N` is a member.

### Littlewood bound (allowed premise, REFEREED)
`S(T) = (1/π)arg ζ(1/2+iT) = O(log T)` and `S_1(T) = ∫_0^T S = O(log T)` (Littlewood).
Riemann–von Mangoldt: `N(T) = (T/2π)log(T/2π) − T/2π + O(log T)`. These are counts /
classical bounds — no zero location is used.

### Lemma G.4 (allowed premise, CONFIRMED OB-10)
If `K_N ≥ 0` finite-rank and `det(I−z²K_N) → f` locally uniformly, then `f` is entire,
`f(0)=1`, and all zeros of `f` are real. (Proof: each `f_N` has zeros only at `±λ_j^{-1/2}
∈ ℝ`; Hurwitz zero-free corollary — Conway VII.§2 Cor. 2.6 — plus the identity theorem to
exclude `f≡0`.) **Corollary G.5:** if such a limit equals `Ξ̂`, then all zeros of `Ξ̂` are
real, i.e. RH; hence 𝔐_FC membership condition 3 ("claims det → Ξ̂") cannot be *verified*
without proving RH.

---

## The claimed theorem (G-info diagonal obstruction)

For every `(K_N) ∈ 𝔐_d^{tr}`:
1. `det(I − z²K_N) → G_d(z)` locally uniformly (trace-norm stability + `Σκ_n < ∞`);
2. `G_d ≠ Ξ̂` **unconditionally**.

And the reduction (Lemma G.5): no `P ∈ 𝔐_FC` can have a *verified* limit `= Ξ̂` without RH.

---

## Links to inspect

**Link A (convergence).** `Σ κ_n = Σ 1/(1/4+d_n²) < ∞` (since `d_n ∼ 2πn/log n`), so
`D = diag(κ_n)` is trace class, `‖D − D_N‖_1 → 0`, and by the Fredholm determinant
stability inequality `det(I−z²D_N) → G_d` locally uniformly. For general `(K_N) ∈ 𝔐_d^{tr}`,
`‖K_N − D_N‖_1 → 0` gives the same limit. **Confirm the trace-class + stability argument.**

**Link B (zeros of `G_d`).** The convergent product `G_d` has zeros exactly at
`±√(1/4+d_n²)` (and is nonzero off them). **Confirm.**

**Link C (`G_d ≠ Ξ̂` — direct value argument, NOT transitivity).** The least positive zero
of `G_d` is `λ_1 = √(1/4+d_1²) > 17.85`, so `G_d(z) ≠ 0` for `0 < z < λ_1`.
- If RH holds: `Ξ̂(γ_1) = 0` with `γ_1 ≈ 14.1347 < λ_1`, so `G_d(γ_1) ≠ 0 = Ξ̂(γ_1)`.
- If RH fails: `Ξ̂` has a non-real zero, `G_d` has only real zeros.
Either way `G_d ≠ Ξ̂`. **Confirm this is valid AND confirm it does NOT rely on the invalid
transitivity `G_d ≠ F_d` ∧ `F_d ≠ Ξ̂` ⟹ `G_d ≠ Ξ̂`.** (This uses one certified on-line
ordinate `γ_1` as external comparison input, not RH.)

**Link D (Prop G.3* Item 2 — multiset distinctness, unconditional).** `{d_n} ≠ {γ_n}` for
infinitely many `n`. Proof: if the symmetric difference were finite, `D(t) − N(t) = m`
(const integer) for large `t`, giving `S(t) = −{A(t)} − m` and (integrating, with
fractional-part averaging) `S_1(T) = −(m+1/2)T + O(1) = Ω(T)`, contradicting Littlewood's
`S_1(T) = O(log T)`. **Confirm this is a correct unconditional argument** (note it does NOT
use the discrepancy sign formula, and does NOT need any zero location).

**Link E (Lemma G.4 / G.5).** PSD ⟹ real determinant zeros ⟹ (Hurwitz + identity theorem)
limit has all-real zeros; hence a verified `det → Ξ̂` would prove RH. **Confirm the Hurwitz
citation (Conway VII.§2 Cor. 2.6) and the identity-theorem step excluding `f≡0`.**

---

## Gate-A questions (the deliverable)

### Q1 — Hidden gap / circularity / RH-import
Does any IN-scope step assume RH, an RH-equivalent, or a ζ-zero location as a premise?
(Expected: no — `d_n` come from `θ` alone; `γ_1` enters only as an external comparison
value in Link C; Link D uses only counting + Littlewood.) Confirm or exhibit the leak.

### Q2 — G-hard quarantine
Confirm that **none** of Links A–E depends on the conjecture G-hard. G-hard is a separate
claim about what prime-based constructions can compute; the diagonal obstruction (`G_d ≠ Ξ̂`
for `𝔐_d^{tr}`) must stand without it. Confirm the quarantine is clean, or show where
G-hard leaks in.

### Q3 — Factorization condition (2.7)
Confirm the obstruction uses only the **weak/definitional** reading of (2.7)
(`K_N = Φ_N((d_n), a_N)`), not the strong reading (`K_N = Ψ_N((d_n))` alone, which would
require `O_θ` constant to force all `K_N` equal). Confirm the writeup does not silently
upgrade weak→strong, and that "zero-free input ≠ zero-blind output" is correctly stated
(zero-free arithmetic can analytically determine zeros, so the strong reading is a genuine
extra hypothesis, not established).

### Q4 — Non-vacuity and scope honesty
Confirm `𝔐_d^{tr}` is genuinely non-empty (`K_N = D_N`) and that the scope/escape and
limitations are correct and complete: (a) the obstruction is about the class `𝔐_d^{tr}` /
`𝔐_FC` with the θ-level observation `O_θ`, not all Hilbert–Pólya operators; (b) it does not
assert kappa_toeplitz (the sibling-repo construction) is a valid member — that non-vacuity
is separately unverified; (c) it makes no claim about RH's truth.

### Q5 — Gate-A verdict
Given Links A–E and Q1–Q4: does the **G-info diagonal obstruction** (IN-scope part only)
constitute a correct, self-contained, non-circular theorem — i.e. should its status advance
from PROOF-DRAFT toward INDEPENDENTLY-CHECKED — with G-hard remaining an explicitly separate
`[CONJECTURE]`? Or does a specific gap block it?

---

## Numerical anchor (sanity only — already certified by the deposited checker)

`d_1 ≈ 17.8455995`, `√(1/4+d_1²) ≈ 17.8526027`, `γ_1 ≈ 14.1347`, so
`γ_1 < d_1 < √(1/4+d_1²)` (gaps `> 3.71` and `> 0.0070`); `Σ_{n>2048} κ_n < 10^{-3}`. These
are certified in exact interval arithmetic by
`theorems/G-fredholm-certificate/checker/diagonal_fredholm_interval_replay.py` (SHA-256
`e197f2bb…c8f4058b`, re-run in-repo). The Gate-A deliverable is the whole-theorem judgment
(Links A–E, Q1–Q5), not a re-run of this arithmetic.

---

## Acceptance criteria

1. **GATE-A PASS:** Links A–E confirmed, Q1–Q5 answered with no blocking gap, G-hard
   confirmed quarantined, (2.7) weak reading confirmed; verdict "advance G-info toward
   INDEPENDENTLY-CHECKED (G-hard remains CONJECTURE)." State any required conditions.

2. **GATE-A CONDITIONAL:** the chain is correct but a specific textual fix is required
   (e.g. tighten the (2.7) wording, or restate a scope limitation). Give the exact edit.

3. **GATE-A BLOCKED:** a genuine gap, circularity, RH-import, or G-hard leak exists in the
   IN-scope assembly. Identify the link/question, exhibit it, and give the minimal repair.

All outcomes decisive. A verdict of "PASS for G-info, with G-hard explicitly excluded" is
exactly the intended scope — do not treat the un-provable G-hard as a blocker for the
provable diagonal obstruction, and do not attempt to prove G-hard.
