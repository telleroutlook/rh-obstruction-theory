# Problem OB-29 — E Gate-A package: independent review of the compactness (finite-evidence) theorem

**Type:** Gate-A independent mathematical review (whole-theorem inspection, scoped).

**What this is.** A request to **independently inspect Theorem E (E-compactness)** — a
two-part statement about approximating the Riemann `Ξ` by entire functions carrying only a
finite evidence record — and issue a **Gate-A verdict**. Part I (**E-neg**) is a per-`N`
non-identifiability result: for each `N`, the finite record `ℰ_N` does not pin down `Ξ` on a
large disk (its quantitative core, §3, is already independently CONFIRMED by prior review
OB-03). Part II (**E-pos**) is a sufficiency package: it names the exact extra hypotheses
that *would* force convergence, via Montel/Vitali/Hurwitz. The review targets the analytic
assembly, the CCM normalization, the non-circularity, and the honesty of the per-`N` framing
and the E-pos "missing ingredients".

**Non-circularity (mandatory).** RH is not assumed and not used. The zeros `γ_n` of `Ξ`
appear only as prescribed real numbers the construction pins zeros to; whether they are the
true ζ-ordinates, and whether they are all real (RH), is **never** used — E-neg constructs a
record-respecting `F` far from `Ξ` regardless. Confirm no step assumes RH, RH-equivalent, or
the reality/location of ζ zeros as a hypothesis. (The remark "zeros of `Ξ` are `±γ_n`, real
by RH" in proof.md §1 is explicitly flagged as *motivation only*.)

---

## All definitions (self-contained — everything is here)

### The target `Ξ` and the normalization discipline (READ FIRST)
```
Ξ(z) = ξ(1/2 + iz)        (entire, even, order 1; zeros ±γ_n).
```
The Connes–Consani–Moscovici determinant identity (arXiv:2511.22755) is
`det_reg(𝔇_{λ,N} − z) = −i·λ^{−iz}·ξ̂(z)`, where `ξ̂` is the **Fourier transform of `ξ`**
(entire, zeros real = spectrum of `𝔇_{λ,N}`). **`ξ̂` and `Ξ` are DISTINCT normalizations**
(REFERENCE_BASELINE §5); the CCM **open step** is that a *suitably normalized* `det_reg`
(equivalently a suitable normalization of `ξ̂`) converges to `Ξ` — the phase `λ^{−iz}`
preserves zeros but not the locally uniform limit. **Theorem E studies exactly this open
step, so its record and target are both stated relative to `Ξ`** (a pre-send fix, OB-29:
earlier drafts wrote the record's Taylor conditions against `ξ̂` — a conflation now
corrected). The Suzuki meromorphic target `z²ξ/ξ'` is a *different* normalization and is out
of scope. **Confirm the package never conflates `ξ̂`, `Ξ`, and `z²ξ/ξ'`.**

### The finite evidence record `ℰ_N` (relative to `Ξ`)
An entire function `F` satisfies `ℰ_N` if:
1. `F` is entire of order 1; 2. even; 3. real on `ℝ`; 4. all zeros real;
5. the first `k_N` zeros of `F` equal `γ_1 ≤ … ≤ γ_{k_N}` (the first `k_N` zeros of `Ξ`);
6. `F(0) = Ξ(0)·c` for some `c > 0` (`Ξ(0) = ξ(1/2) > 0`);
7. the first `J_N` even Taylor coefficients agree: `F^{(2j)}(0) = Ξ^{(2j)}(0)`, `j = 0,…,J_N`.
The record carries **no tail envelope**: `F(z)` for large `|z|` is uncontrolled.

### Reciprocal-square variables (for §3)
`a_m := γ_{k+m}^{-2}` (`m ≥ 1`), so `a_1 > a_2 > … > 0`, `Σ a_m < ∞` (Ξ has genus 1).

---

## Part I — Theorem E-neg (finite record does not identify `Ξ`)

**Statement (per-`N` non-identifiability).** For every `N` (record `ℰ_N`: `k = k_N` zeros
pinned, `J = J_N` Taylor coefficients matched) there exist `ε_N > 0`, `R_N ≥ 2γ_{k+1}`, and
an entire `F` **satisfying `ℰ_N`** with
```
sup_{|z| ≤ R_N} |F(z) − Ξ(z)| ≥ ε_N .
```
So the fiber `{F : F satisfies ℰ_N}` is not contained in any `ε`-neighborhood of `Ξ` on the
disk `|z| ≤ R_N`. **This is per-`N`, NOT a claim that a sequence `(F_N)` fails to converge**
(the witness radius `R_N ≥ 2γ_{k_N+1} → ∞`, so it is consistent with locally-uniform
convergence on fixed compacts). It is the exact analogue of B1's "no uniform separation
margin".

**Construction (fixed `N`; §3, CONFIRMED by OB-03).**
- Freeze a one-parameter tail: `b_m(c) := a_m(1+c/m)^{-2}` for `m > J` (zeros pushed to
  `μ_{k+m}(c) = γ_{k+m}(1+c/m)`).
- Match the record by IFT: with `u = (u_1,…,u_J)` the free reciprocal squares, impose the
  **log-power-sum** system `Φ_r(u,c) = Σ_{ℓ≤J} u_ℓ^r + Σ_{m>J} b_m(c)^r − Σ_{m≥1} a_m^r = 0`
  (`r = 1,…,J`), which is exactly `P_r(F_c) = P_r(Ξ)`, i.e. Taylor-match `j = 0,…,J`. At
  `(u^0,0) = ((a_1,…,a_J),0)`, `Φ = 0`, and the Jacobian `∂Φ_r/∂u_ℓ = r·a_ℓ^{r-1}` is an
  exact scaled Vandermonde (`det ≠ 0`). IFT gives a `C¹` branch `u(c)`, `Φ(u(c),c)=0`, for
  `0 < c < δ`. Define
  `F_c(z) = C·Π_{n≤k}(1−z²/γ_n²)·Π_{ℓ≤J}(1−u_ℓ(c)z²)·Π_{m>J}(1−b_m(c)z²)` — entire order 1,
  even, real, all zeros real, first `k` zeros `γ_1,…,γ_k`, `F_c(0)=C`, Taylor-matched: `ℰ_N`
  holds.
- Separate by the first unmatched coefficient: `Δ_{J+1}(c)` has `Δ_{J+1}'(0) =
  −(J+1)Σ_{m>J} d_m q(a_m) ≠ 0` (`d_m = 2a_m/m`, `q(x)=Π_ℓ(x−a_ℓ)`, all `q(a_m)` of one
  sign `(−1)^J`), so `Δ_{J+1}(c) ≠ 0` for small `c>0`, and
  `F_c(z) − Ξ(z) = −C·Δ_{J+1}(c)/(J+1)·z^{2J+2} + O(z^{2J+4})`. Cauchy's estimate gives
  `sup_{|z|≤R}|F_c − Ξ| ≥ A_c R^{2J+2}` (`A_c = C|Δ_{J+1}(c)|/(J+1) > 0`); take
  `R_N = max{2γ_{k+1}, (ε_N/A_c)^{1/(2J+2)}}`. **No `N→∞` is used.**

**Why the naive `δ_n = c/n` sketch was abandoned (§2).** A hand-picked summable perturbation
makes the tail log-difference *converge* to 0, so it witnesses nothing; the IFT route matches
the record exactly for fixed `N` and separates via the first unmatched coefficient.

---

## Part II — Theorem E-pos (sufficient package → convergence)

**Statement.** Let `(F_N)` satisfy `ℰ_N` and additionally:
- **(H-norm)** `F_N(z_0) → Ξ(z_0) ≠ 0` for some `z_0`;
- **(H-bound)** locally uniform bound: `∀R ∃M_R: sup_N sup_{|z|≤R}|F_N| ≤ M_R`;
- **(H-uorder)** uniform *conventional-order* envelope `T(r,F_N) ≤ C_ε r^{1+ε} + C_{0,ε}`
  (constants independent of `N`);
- **(H-div)** multiplicity-complete two-sided divisor convergence (zeros of `F_N` in `|z|<R`
  converge to those of `Ξ` with multiplicity and no others, all large `N`).
Then `F_N → Ξ` locally uniformly, and by Hurwitz all zeros of `Ξ` are real limits of zeros
of `F_N`.

**Proof (standard).** (H-bound)+Montel ⇒ normal family; any subsequential limit `G` is even,
order ≤ 1 by (H-uorder) (`T(r,·)` continuous under l.u. convergence), has `Ξ`'s complete zero
divisor by (H-div)+Rouché, and `G(z_0)=Ξ(z_0)≠0` by (H-norm). Then `H := G/Ξ` is zero-free of
order ≤ 1, so `H = e^{az+b}`; evenness ⇒ `a=0`; `H(z_0)=1` ⇒ `H≡1`; `G = Ξ`. Hurwitz
transfers real zeros.

**These are the identified MISSING ingredients, not proved facts.** The CCM sequence is
**not** known to satisfy (H-bound)/(H-uorder)/(H-div); Part III records their CCM status as
OPEN. Confirm E-pos is honestly a *conditional* (sufficiency) theorem, not a convergence
proof.

**Two corrections already baked in (prior reviews OB-05/OB-14 — confirm they hold):**
- **(H-uorder) must be `r^{1+ε}`, NOT linear `Cr+C_0`.** A uniform *linear* bound forces
  finite exponential type, incompatible with the real `Ξ` (infinite type,
  `log|Ξ(iy)| ∼ (y/2)log(y/2)`) — that would make the hypothesis vacuous. Counterexample to
  "(H-bound) alone ⇒ order": `F_N ≡ Ξ·e^{z²−z_0²}` is a bounded constant sequence with `Ξ`'s
  divisor and `F_N(z_0)=Ξ(z_0)`, but limit order 2 ≠ 1.
- **(H-div) must be two-sided + multiplicity-complete.** A one-sided "no-intrusion" clause is
  vacuous for zero-free approximants (`Ξ(z_0)·e^{z²−z_0²}` satisfies it).

---

## Links to inspect

**Link A (E-neg IFT construction).** `Φ_r` system, exact Vandermonde Jacobian
`∂Φ_r/∂u_ℓ = r·a_ℓ^{r-1}`, IFT branch `u(c)`. **Confirm** `F_c` satisfies `ℰ_N` 1–7 and the
Jacobian is nonsingular (scaled Vandermonde with distinct `a_ℓ`).

**Link B (E-neg separation).** `Δ_{J+1}'(0) ≠ 0` from the one-signed `q(a_m)` series;
`F_c − Ξ = −C Δ_{J+1}(c)/(J+1) z^{2J+2} + O(z^{2J+4})`; Cauchy estimate ⇒ `sup ≥ A_c R^{2J+2}`.
**Confirm** the leading-coefficient sign argument and that the bad radius `R_N ≥ 2γ_{k+1}`
grows with `N` (⇒ per-`N`, not sequence).

**Link C (per-`N` framing honesty).** **Confirm** the theorem is correctly stated as per-`N`
non-identifiability (not "sequence `(F_N)` fails to converge"), and that this does not
contradict locally-uniform convergence on fixed compacts (PROMPT_LINT L24).

**Link D (E-pos sufficiency).** Montel ⇒ normal family; (H-uorder) ⇒ order ≤ 1; (H-div) ⇒
complete divisor; identity `G = Ξ`; Hurwitz. **Confirm** the four hypotheses are exactly what
the argument consumes, that `r^{1+ε}` (not linear) and two-sided (H-div) are both required,
and that E-pos is honestly conditional.

---

## Gate-A questions (the deliverable)

### Q1 — Hidden gap / circularity / RH-import
Does any step assume RH, an RH-equivalent, or the reality/location of ζ zeros? (E-neg pins
zeros to prescribed reals `γ_n` but never uses their being the true ζ-ordinates or their
reality; E-pos *derives* real-rootedness of the limit, it does not assume it.) Confirm or
exhibit the leak.

### Q2 — Normalization (`Ξ` vs `ξ̂` vs `z²ξ/ξ'`)
Confirm the record and target are consistently the CCM **entire** target `Ξ(z)=ξ(1/2+iz)`,
that the `det_reg = −iλ^{−iz}ξ̂` identity is used only as motivation for the open step
(`ξ̂` ≠ `Ξ`), and that the Suzuki meromorphic `z²ξ/ξ'` is not conflated. (This was a pre-send
fix, OB-29; verify no residue of the old `ξ̂`-record remains.)

### Q3 — Per-`N` vs sequence (the framing crux)
Confirm E-neg is a genuine per-`N` non-identifiability statement (bad radius `→∞`), correctly
NOT marketed as sequence non-convergence, and that this is a non-vacuous information
obstruction (analogous to B1's no-uniform-margin), clear of the "margin → 0" non-barrier
label.

### Q4 — E-pos is conditional, ingredients honest
Confirm E-pos is a sufficiency theorem whose hypotheses (H-uorder)/(H-div) are **not** proved
for the CCM sequence (Part III marks them OPEN), that `r^{1+ε}` (not linear finite-type) is
mandatory, and that (H-div) two-sided is mandatory. Confirm the two counterexamples
(`Ξ·e^{z²−z_0²}`) correctly motivate these.

### Q5 — Non-vacuity and class membership
Confirm the ambient class (order-1 entire functions with record `ℰ_N`) is non-empty and that
`Ξ` itself and the CCM `det_reg` sequence are serious members; confirm the record conditions
are checkable and representation-independent.

### Q6 — Novelty honesty
"Finite real-zero matching does not force global convergence" is folklore. Is E's increment
— the **quantified per-`N` witness in the exact CCM normalization** (IFT + Vandermonde +
Cauchy) plus the **sufficiency package** naming (H-uorder)/(H-div) as the precise missing
ingredients — a genuine, sharply-defined contribution for Paper C, or a routine corollary?
State honestly (a standalone-note vs supporting-section verdict is acceptable either way).

### Q7 — Gate-A verdict
Given Links A–D and Q1–Q6: is Theorem E a correct, self-contained, non-circular, RH-free
result (E-neg per-`N` obstruction + E-pos conditional sufficiency)? Should its mathematical
status advance from PROOF-DRAFT toward INDEPENDENTLY-CHECKED? Or does a specific gap block it?

---

## Numerical anchor (sanity only — not an input)

- Witness-radius growth: `γ_{N+1} ~ 2πN/log N → ∞`, so `R_N ≥ 2γ_{k_N+1} → ∞`
  (script-checked: `N=10 → R_N≳54`, `N=10^4 → R_N≳1.4·10^4`), confirming the per-`N` framing.
- `Ξ(0) = ξ(1/2) > 0` (standard).
- The order-2 counterexample `Ξ·e^{z²−z_0²}`: `T(r, e^{z²−z_0²}) = r²/π + O(1)`, order 2 ≠ 1,
  yet locally uniformly bounded on every disk with `Ξ`'s divisor — motivating (H-uorder).
The Gate-A deliverable is the whole-theorem judgment (Links A–D, Q1–Q7), not a re-run of §3
(already OB-03-confirmed).

---

## Acceptance criteria (all outcomes decisive)

1. **GATE-A PASS:** Links A–D confirmed, Q1–Q7 answered with no blocking gap; verdict
   "advance E toward INDEPENDENTLY-CHECKED", with the Q6 novelty ruling (standalone vs
   supporting section). State any required textual conditions.

2. **GATE-A CONDITIONAL:** the chain is correct but a specific textual fix is required (e.g.
   sharpen a hypothesis statement, restate a scope line). Give the exact edit.

3. **GATE-A BLOCKED:** a genuine gap, circularity, RH-import, or normalization conflation
   exists. Identify it, exhibit it, give the minimal repair.

An honest "E-neg per-`N` obstruction is correct and RH-free; E-pos is a correct conditional
sufficiency theorem with (H-uorder)/(H-div) as unproved-for-CCM hypotheses; publish as the
Paper C negative+sufficiency pair" is a valid, first-class outcome. The goal is a truthful
judgment of what E establishes.
