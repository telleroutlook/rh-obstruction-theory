# Theorem E — Real-Rooted Approximants and the Missing Compactness Theorem

**Mathematical status:** PROOF-DRAFT (E-neg = per-`N` non-identifiability, quantitative §3 CONFIRMED by OB-03; E-pos = sufficiency package, standard Montel/Vitali/Hurwitz. Self-audit OB-28 2026-08-11: E-neg restated as per-`N`, not sequence non-convergence)  
**Computational status:** NONE  
**Theorem ID:** E-compactness  
**Program ref:** §10 (WP-E), §10.E.1–E.5  
**Paper target:** Paper C (primary, unconditional)

---

## Part I — Negative theorem (finite evidence ⇏ compact convergence)

### Setting

**Normalization (CCM entire-target, frozen for this theorem).**  
Following Connes–Consani–Moscovici (arXiv:2511.22755), the target is:

```
Ξ(z) = ξ(1/2 + iz)         (entire, even, all zeros real by RH)
```

with the CCM determinant identity:

```
det_reg(𝔇_{λ,N} − z) = −i · λ^{−iz} · ξ̂(z),
```

where `ξ̂` is the Fourier transform of `ξ` (entire, all zeros real = spectrum
of `𝔇_{λ,N}`).  The **open CCM step** is:
`suitably normalized det_reg → Ξ` as `N, λ → ∞`.

**This theorem works with the CCM entire target.**  The Suzuki meromorphic
target `z² ξ/ξ'` is kept separate (REFERENCE_BASELINE §5).

**Finite evidence record.**  An approximating entire function sequence `(F_N)_{N≥1}`
satisfies the **CCM finite evidence record** `ℰ_N` if:

1. `F_N` is an entire function of order one.
2. `F_N` is even: `F_N(−z) = F_N(z)`.
3. `F_N` is real on the real axis: `F_N(z̄) = F_N(z)̄`.
4. All zeros of `F_N` are **real** (real-rootedness).
5. The first `k_N → ∞` zeros of `F_N` (ordered by size) agree with
   the verified ordinates `γ₁ ≤ γ₂ ≤ …` of `ζ`.
6. A finite-dimensional determinant identity holds:
   `F_N(0) = ξ̂(0) · c_N` for a normalization constant `c_N > 0`.
7. Finitely many Taylor coefficients agree:
   `F_N^{(2j)}(0) = ξ̂^{(2j)}(0)` for `j = 0, 1, …, J_N`.

The record `ℰ_N` contains **no proved tail envelope**: the behavior of `F_N(z)`
for `|z|` large is uncontrolled.

**Convergence target:** locally uniform convergence
```
F_N(z) → Ξ(z)   as  N → ∞,   uniformly on every compact  K ⊂ ℂ.
```

---

### Theorem E-neg (finite evidence ⇏ compact convergence)

**Theorem E-neg (finite record does not identify Ξ — per-`N` non-identifiability).**
For every `N ≥ 1` (pinning the first `k_N` zeros and matching the first `J_N` even Taylor
coefficients, i.e. the full record `ℰ_N`) there exist `ε_N > 0`, `R_N ≥ 2γ_{k_N+1}`, and an
entire function `F` **satisfying `ℰ_N`** with

```
sup_{|z| ≤ R_N} |F(z) − Ξ(z)| ≥ ε_N .
```

Equivalently: the fiber `{F : F satisfies ℰ_N}` is **not** contained in any
`ε`-neighborhood of `Ξ` on the disk `|z| ≤ R_N` — the finite record does not pin the
function down, even on a large disk that already contains all `k_N` matched zeros.

**Scope of the claim (what E-neg does and does NOT say — OB-28 correction).**
This is a **per-`N` non-identifiability** statement, exactly analogous to B1's "no uniform
separation margin." It does **not** assert that a *particular sequence* `(F_N)` fails to
converge locally uniformly: the witness discrepancy sits at radius `R_N ≥ 2γ_{k_N+1} → ∞`,
so it does not contradict locally-uniform convergence on any fixed compact (that is why the
positive package E-pos, with its extra hypotheses, is not in conflict). The content is that
`ℰ_N` **alone** leaves an uncontrolled tail degree of freedom; the escape (E-pos) is exactly
the extra data that removes it.

---

### Construction of the witness (matches proof.md §3 — fixed `N`, OB-03-confirmed)

Fix `N`; write `k := k_N`, `J := J_N`. Work in reciprocal-square variables
`a_m := γ_{k+m}^{-2}` (`m ≥ 1`, so `a_1 > a_2 > … > 0`, `Σ a_m < ∞`).

**Step 1 (freeze a one-parameter tail).** For `m > J` set
`b_m(c) := a_m (1 + c/m)^{-2}` — i.e. push the tail zero to `μ_{k+m}(c) = γ_{k+m}(1+c/m)`.

**Step 2 (match the record by IFT, not by a hand-picked `δ_n`).** Let `u = (u_1,…,u_J)` be
the first `J` free reciprocal squares. Impose the **log-power-sum** matching system
```
Φ_r(u,c) := Σ_{ℓ=1}^{J} u_ℓ^r + Σ_{m>J} b_m(c)^r − Σ_{m≥1} a_m^r = 0,   r = 1,…,J,
```
which is exactly `P_r(F_c) = P_r(Ξ)`, hence `F_c^{(2j)}(0) = Ξ^{(2j)}(0)` for `j = 0,…,J`
(record conditions 6–7). At `(u^0,0) = ((a_1,…,a_J),0)` we have `Φ = 0`, and the Jacobian
`∂Φ_r/∂u_ℓ = r·a_ℓ^{r-1}` is an exact scaled Vandermonde, `det ≠ 0`. The implicit function
theorem gives `δ > 0` and a `C¹` branch `u(c)`, `Φ(u(c),c)=0`, for `0 < c < δ`. Define
```
F_c(z) := C · Π_{n=1}^{k}(1 − z²/γ_n²) · Π_{ℓ=1}^{J}(1 − u_ℓ(c) z²) · Π_{m>J}(1 − b_m(c) z²).
```
Then `F_c` is entire of order 1, even, real on `ℝ`, all zeros real, first `k` positive zeros
`= γ_1,…,γ_k`, `F_c(0)=C`, and the first `J` even Taylor coefficients match — so `F_c`
satisfies `ℰ_N` (conditions 1–7).

**Step 3 (`F_c ≠ Ξ`, quantified by a Cauchy estimate — no `N→∞`).** The first unmatched
log-power-sum `Δ_{J+1}(c)` has `Δ_{J+1}'(0) = −(J+1)Σ_{m>J} d_m q(a_m) ≠ 0`
(`d_m = 2a_m/m`, `q(x) = Π_{ℓ}(x−a_ℓ)`, every `q(a_m)` of sign `(−1)^J`), so shrinking `δ`
gives `Δ_{J+1}(c) ≠ 0` and
`F_c(z) − Ξ(z) = −C·Δ_{J+1}(c)/(J+1)·z^{2J+2} + O(z^{2J+4})`. Cauchy's coefficient estimate
then yields, with `A_c := C|Δ_{J+1}(c)|/(J+1) > 0`,
`sup_{|z|≤R}|F_c − Ξ| ≥ A_c R^{2J+2}` for every `R`; taking
`R_N := max{2γ_{k+1}, (ε_N/A_c)^{1/(2J+2)}}` gives the theorem. (Full detail: proof.md §3.)

**Why the earlier `δ_n = c/n` sketch was dropped.** A hand-picked summable perturbation
makes the tail difference *converge* to 0 (so it fails to witness anything); the IFT route
above matches the record *exactly* for a fixed `N` and separates via the first unmatched
coefficient. See proof.md §2 for why the naive perturbations fail.

---

## Part II — Positive escape theorem (sufficient convergence package)

### Theorem E-pos (normal-family sufficiency)

**Theorem E-pos.** Let `(F_N)_{N≥1}` be a sequence of entire functions satisfying
the CCM finite evidence record `ℰ_N`, and additionally:

(H-norm) A base-point normalization: `F_N(z₀) → Ξ(z₀) ≠ 0` for some `z₀ ∈ ℂ`.

(H-bound) Local uniform boundedness: for every `R > 0`, there exists `M_R > 0`
with `sup_N sup_{|z| ≤ R} |F_N(z)| ≤ M_R`.

(H-tail) Summable tail control: there exist coefficients `a_{n,N} ∈ ℝ` such that
`Σ_n |a_{n,N} − γ_n^{-2}| < C` uniformly in `N`, and `F_N` has Hadamard
representation with zero sequence `(±r_{n,N})` satisfying
`Σ_n |r_{n,N}^{-2} − γ_n^{-2}| < C`.

(H-modulus) Effective convergence: there exists a computable `N(R, ε)` such that
`|F_N(z) − Ξ(z)| < ε` for `|z| ≤ R` and `N ≥ N(R, ε)`.

Then `F_N → Ξ` locally uniformly, and by Hurwitz's theorem the zeros of `F_N`
converge (with multiplicity) to the zeros of `Ξ`.

**Proof sketch.** (H-bound) gives a normal family (Montel).  Any subsequential
limit `G` satisfies conditions 1–4 by uniform convergence; (H-norm) forces `G ≠ 0`
and identifies `G = Ξ` uniquely (by (H-tail) + the identification-via-Taylor-jet
or Hadamard-product uniqueness).  Hurwitz then transfers real-zero location. ☐

---

## Part III — Application checklist

**For CCM truncations (`𝔇_{λ,N}`):**

| Condition | Status in CCM literature |
|---|---|
| (1) entire | PROVED (CCM det identity) |
| (2–3) even, real on ℝ | PROVED (symmetry of 𝔇) |
| (4) real-rootedness | PROVED (CCM Thm, real zeros = spectrum) |
| (5) first k_N zeros agree with ζ zeros | OPEN (numerical evidence; analytic proof missing) |
| (6) normalization at 0 | PARTIAL (λ^{−iz} phase is the obstacle) |
| (H-norm) F_N(z₀) → Ξ(z₀) | OPEN (the "suitably normalized" step) |
| (H-bound) local uniform bound M_R | OPEN (no tail envelope in CCM 2511.22755) |
| (H-uorder) uniform conventional-order envelope T(r,F_N) ≤ C_ε r^{1+ε}+C_{0,ε}, constants independent of N | OPEN — REQUIRED for the order of the limit; (H-bound) alone insufficient (PROMPT_LINT L14; counterexample F_N≡Ξ·e^{z²−z₀²} has order 2). Must use the r^{1+ε} envelope, NOT a linear Cr+C₀: a uniform *linear* bound forces finite exponential type, incompatible with the real Ξ (infinite type) — OB-14 §4.3, PROMPT_LINT L1 |
| (H-div) multiplicity-complete divisor convergence | OPEN — two-sided disk condition (zeros of F_N in \|z\|<R converge to those of Ξ with multiplicity, no others); the one-sided no-intrusion clause alone is vacuous for zero-free approximants (OB-14 §1.2, §4.1) |

**The theorem identifies (H-bound), (H-uorder), and (H-div) as the exact missing
ingredients.** (H-uorder) is distinct from (H-bound): local uniform boundedness does not
transfer an order bound to the limit — a *uniform-in-N conventional-order* envelope
(`r^{1+ε}`, not linear) is required (corrected 2026-08-11: PROMPT_LINT re-scan from OB-11,
then OB-14 fixed the finite-type/conventional-order confusion per L1).

**For Suzuki W(a, θ; z):**

The Suzuki target is `z² ξ/ξ'` (meromorphic).  The CCM entire-target theorem does
not apply directly.  The pole/residue version is needed (see limitations.md).

---

## Escape route

An `F_N` satisfying the full positive package (H-norm + H-bound + H-tail + H-modulus)
is NOT excluded by the negative theorem.  The escape condition is precisely the
addition of a proved tail envelope.  A bound of the form
```
Σ_{n > k_N} |r_{n,N}^{-2} − γ_n^{-2}| ≤ C(N) → 0   as  N → ∞
```
is sufficient; it converts the finite zero-agreement into a global one.

Methods that are NOT excluded:
1. Any proof supplying a certified `M_R` (e.g. via operator norm bounds on `𝔇_{λ,N}`).
2. Any proof of (H-tail) via spectral theory of `A_a` (Suzuki's `λ(a)` bounds).
3. Infinite-order methods (full Weil criterion, all Li tests, exact Hadamard product).
