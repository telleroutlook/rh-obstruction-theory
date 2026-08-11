# Theorem E — Real-Rooted Approximants and the Missing Compactness Theorem

**Mathematical status:** PROOF-DRAFT — **Gate-A BLOCKED for the `Ξ`-specific RH-free claim
(OB-29, 2026-08-11).** The independent review found a genuine circularity: the E-neg IFT
construction and the E-pos (H-div) hypothesis both require `Ξ(z)=Ξ(0)∏(1−z²/γ_n²)` with the
`γ_n` **real** — i.e. all zeros of `Ξ` on the line — which **is RH** (PROMPT_LINT L5,
RH-imported-via-divisor; a re-scan miss). What survives is stated over an **abstract
Laguerre–Pólya real-zero target `L`** (RH-free); specializing to `Ξ` is explicitly
RH-conditional. See §0 (reframing) and limitations.md.  
**Computational status:** NONE  
**Theorem ID:** E-compactness  
**Program ref:** §10 (WP-E), §10.E.1–E.5  
**Paper target:** Paper C — supporting section (abstract real-zero non-identifiability lemma), NOT a standalone RH-free `Ξ`-theorem

---

## §0. Reframing after OB-29 (Gate-A BLOCKED) — READ FIRST

The originally-submitted Theorem E claimed a **`Ξ`-specific, RH-free** per-`N`
non-identifiability result. OB-29 **BLOCKED** it: the construction is genuinely circular.

- **The circularity (L5).** E-neg matches the log-power-sums `P_r(F_c)=P_r(Ξ)` by writing
  `Ξ(z)=Ξ(0)∏_{n≥1}(1−z²/γ_n²)` as a product **over real zeros `γ_n`**. If the `γ_n` are the
  *complete* zero set of `Ξ` and real, that product **is RH**. If instead the `γ_n` are
  merely "prescribed reals" (or the known critical-line zeros only), the product is **not**
  `Ξ`, and `P_r(F_c)=P_r(Ξ)` no longer holds. There is no RH-free reading that both (a)
  identifies the product with `Ξ` and (b) matches its Taylor data. E-pos's (H-div) has the
  same defect: it forces every `Ξ`-zero to be a real-limit of real zeros of `F_N`, i.e. RH,
  *before* Montel/Hurwitz.

- **What is withdrawn:** the `Ξ`-specific RH-free claim; the assertion that `Ξ` and the CCM
  `det_reg` sequence are known members of the record class; and "(H-div) is a harmless
  compactness condition, not RH". Also withdrawn: the "`R_N → ∞`" radius-escape (it needs the
  never-stated `k_N → ∞`), and the leading-asymptotic radius anchors used in the OB-29
  package (`4πN/log N ≈ 54.6, 13644` at `N=10,10⁴` were leading-asymptotic, not certified
  `2γ_{k+1}`; the true values via Odlyzko are `2γ_11 ≈ 105.9`, `2γ_10001 ≈ 19757` — OB-29 §5).

- **What survives (RH-free), and is the actual content of this file:** the same IFT / scaled-
  Vandermonde / Cauchy machinery, stated over an **abstract Laguerre–Pólya target**
  `L(z) = C∏_{n≥1}(1 − z²/λ_n²)` with a *given* real, simple, summable-`λ_n^{-2}` zero set
  (a benchmark real-zero entire function of order 1) — see §1'. This is a genuine RH-free
  non-identifiability lemma about finite records of real-zero entire functions. It does **not**
  specialize to `Ξ` without separately assuming RH (which the program forbids as a premise).
  The finite-dimensional core (Links A/B) was CONFIRMED by OB-29 *given such a benchmark*; the
  meromorphic uniqueness lemma (E-pos identification) is CONFIRMED as an abstract lemma once
  (H-uorder)/(H-div) are made precise — but (H-div) over `Ξ` is RH and must be labelled so.

Everything below Part I is retained for record; read every `Ξ` in the construction as the
abstract `L` unless RH is explicitly assumed.

---

## Part I — Negative theorem (finite evidence ⇏ compact convergence)

### Setting

**Normalization (CCM entire target — `Ξ`, frozen for this theorem).**  
The convergence target is the shifted completed zeta
```
Ξ(z) = ξ(1/2 + iz)         (entire, even, order 1; zeros ±γ_n, the ζ-ordinates).
```
The **CCM determinant identity** (Connes–Consani–Moscovici, arXiv:2511.22755) is
```
det_reg(𝔇_{λ,N} − z) = −i · λ^{−iz} · ξ̂(z),
```
where `ξ̂` is the Fourier transform of `ξ` (entire, zeros real = spectrum of `𝔇_{λ,N}`).
**`ξ̂` and `Ξ` are DISTINCT normalizations** (REFERENCE_BASELINE §5): the CCM **open step**
is precisely that a *suitably normalized* `det_reg` (equivalently, a suitable normalization
of `ξ̂`) converges to `Ξ` — the phase `λ^{−iz}` preserves zeros but not the locally uniform
limit. **Theorem E studies exactly this open step**, so its finite-evidence record and its
convergence target are both stated relative to the **target `Ξ`** (not `ξ̂`); the CCM
identity above is the motivation, not the record. The Suzuki meromorphic target `z²ξ/ξ'` is
kept separate (REFERENCE_BASELINE §5) — never conflated.

**Finite evidence record.**  An approximating entire function sequence `(F_N)_{N≥1}`
satisfies the **finite evidence record** `ℰ_N` (relative to the target `Ξ`) if:

1. `F_N` is an entire function of order one.
2. `F_N` is even: `F_N(−z) = F_N(z)`.
3. `F_N` is real on the real axis: `F_N(z̄) = F_N(z)̄`.
4. All zeros of `F_N` are **real** (real-rootedness).
5. The first `k_N → ∞` zeros of `F_N` (ordered by size) agree with
   the ordinates `γ₁ ≤ γ₂ ≤ …` (the zeros of `Ξ`).
6. Base-point normalization: `F_N(0) = Ξ(0) · c_N` for a constant `c_N > 0`
   (`Ξ(0) = ξ(1/2) > 0`).
7. Finitely many Taylor coefficients agree:
   `F_N^{(2j)}(0) = Ξ^{(2j)}(0)` for `j = 0, 1, …, J_N`.

The record `ℰ_N` contains **no proved tail envelope**: the behavior of `F_N(z)`
for `|z|` large is uncontrolled.

**Convergence target:** locally uniform convergence
```
F_N(z) → Ξ(z)   as  N → ∞,   uniformly on every compact  K ⊂ ℂ.
```

### §1'. The RH-free abstract target `L` (the actual object of the surviving theorem)

To state the surviving RH-free content, replace `Ξ` throughout by an **abstract benchmark**:
```
L(z) = C · ∏_{n≥1} (1 − z²/λ_n²),    C > 0,   0 < λ_1 < λ_2 < …,   Σ λ_n^{-2} < ∞,
```
i.e. `L` is any **Laguerre–Pólya** entire function of order 1 with a *given*, real, simple,
summable-reciprocal-square zero set `{±λ_n}` (even, real on `ℝ`). The record `ℰ_N` and the
theorems below are stated with `L` in place of `Ξ`. **No claim is made that `Ξ` is such an
`L`** — that identification is exactly RH and is never assumed. (When the literature has
`Ξ = L` unconditionally we could specialize; it does not, so E stays an abstract-`L`
statement. The `a_n := λ_n^{-2}` are the reciprocal-square variables used in §3; simplicity
`λ_i ≠ λ_j` gives the distinct `a_n` the Vandermonde step needs — for `Ξ` this simplicity is
itself unproven, another reason the specialization fails, OB-29 §1.2.)

---

### Theorem E-neg (finite evidence ⇏ compact convergence)

**Theorem E-neg (finite record does not identify Ξ — per-`N` non-identifiability).**
*(RH-free form: read `L` for `Ξ` throughout, per §0/§1'. The `Ξ`-specialization is RH — BLOCKED, OB-29.)*
For every `N ≥ 1` (pinning the first `k_N` zeros and matching the first `J_N` even Taylor
coefficients, i.e. the full record `ℰ_N`) there exist `ε_N > 0`, `R_N ≥ 2λ_{k_N+1}`, and an
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
converge locally uniformly. The per-`N` witness sits at radius `R_N ≥ 2λ_{k_N+1}`; **this
radius escapes to ∞ only if one additionally assumes `k_N → ∞`** (OB-29 §1.4 — the bare
per-`N` statement does not include that quantifier, so "`R_N → ∞`" is asserted only under
`k_N → ∞`). Under that assumption it does not contradict locally-uniform convergence on any
fixed compact. The content is that `ℰ_N` **alone** leaves an uncontrolled tail degree of
freedom; the escape (E-pos) is the extra data that removes it.

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
