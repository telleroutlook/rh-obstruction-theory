# Finite Observables Do Not Determine Critical-Line Support

*Draft manuscript (Paper A). Generated from the theorem files
`theorems/{B1-finite-inequality, B2-exact-collision, G-fredholm-certificate}/`, all
Gate-A-established (independent whole-theorem review) and carrying deposited independent
checkers. This draft matches the reviewed status exactly; see `docs/STATUS.md` and the
per-theorem `statement.md` for the authoritative record.*

**Status of this draft:** manuscript skeleton with full statements and proofs of the three
theorems; proof prose is complete for B1 and B2 and complete-modulo-inheritance for G-info.
Editorial passes remaining: reference formatting, figure of the observation preorder,
final prior-art comparison.

---

## Abstract

We prove three information-theoretic *obstruction theorems* for methods that decide the
predicate "all zeros lie on the critical line" using only a finite or archimedean-level
observation of a zeta-like zero multiset. Let `𝔛_sym` be the class of locally finite zero
multisets in the critical strip, symmetric under conjugation and `ρ ↦ 1−ρ`, with an
admissibility exponent bound.

- **Theorem B1 (no uniform separation margin).** For any finite test family
  `Φ = (φ_1,…,φ_m)` (Li, Weil-W2, or moment type) and any tolerance, there are
  `𝒵_+, 𝒵_- ∈ 𝔛_sym` with `P(𝒵_+)=1`, `P(𝒵_-)=0`, whose observation vectors satisfy
  `|O_Φ(𝒵_+) − O_Φ(𝒵_-)| < ε` coordinate-wise; the infimum over the construction of the
  observation gap between the `P=1` and `P=0` classes is `0`.
- **Theorem B2 (exact observation collision).** Under the same hypotheses one can take
  `O_Φ(𝒵_+) = O_Φ(𝒵_-)` **exactly** (zero tolerance, integer multiplicities), with
  `𝒵_+` on-line and `𝒵_-` additionally carrying an off-line quartet.
- **Theorem G-info (diagonal Fredholm obstruction).** For every method in a natural
  archimedean-level class `𝔐_d^{tr}`, the locally uniform limit of the associated
  finite-rank Fredholm determinant is a fixed function `G_d` that is unconditionally
  **not** the target `Ξ̂`.

All three exhibit a method class whose observation map does not determine the target
predicate. **These are no-go theorems for a class of methods; they do not prove, disprove,
or make progress toward the Riemann Hypothesis, and they hold regardless of its truth.**

---

## 1. Introduction

### 1.1 What this paper does and does not claim

The Riemann Hypothesis (RH) is equivalent to a great many criteria — positivity of the Li
coefficients [Li 1997], positivity of the Weil functional [Weil 1952; Bombieri 2000],
reality of the spectrum of various conjectural operators [Berry–Keating 1999;
Connes 1999]. Each such criterion *locates* the difficulty of RH in a particular object;
none of them, by itself, is a barrier to any proof strategy.

This paper proves the complementary kind of statement: for three precisely delimited
*method classes*, the data the method observes **does not determine** whether all zeros
lie on the critical line. We emphasize at the outset, and repeat in the conclusion:

> **This paper does not prove, disprove, or approach RH.** Its theorems are no-go results
> for method classes — statements of the form "a method seeing only `O` cannot decide the
> predicate `P`", proved by exhibiting two admissible objects that agree on `O` but differ
> on `P`. RH itself is never assumed, and no result here is an RH-equivalent reformulation.

Following the discipline of the underlying research program, we call such a theorem a
**barrier** for a method class only when all five of the following are explicit: the method
class, the ambient object class, the observation map, the target predicate, and an escape
route (a strictly larger class or richer observation to which the obstruction does not
apply). We are careful to distinguish a genuine obstruction from the non-results the program
explicitly excludes (another RH-equivalence; a finite failure of one sufficient inequality;
a positive margin tending to zero; a synthetic configuration outside the ambient class).

### 1.2 Relation to prior work

That finite real-zero data cannot certify an infinite positivity criterion is folklore, and
finite-Li limitations were noted by Bombieri–Lagarias [1999]. Our contribution is (i) to make
the obstruction **exact** — zero tolerance and integer multiplicities (Theorem B2) — in a
precisely defined ambient class with an explicit escape-route list; (ii) to prove the
companion **no uniform margin** statement (Theorem B1) that keeps the result clear of the
"margin → 0" non-barrier; and (iii) to give the analogous archimedean-level obstruction
(Theorem G-info) for the diagonal Fredholm-determinant approach in the sense of
Connes–Consani–Moscovici [2025]. Each theorem has been checked by an independent
whole-theorem review and, where a finite certificate exists, by an independently written
exact/interval-arithmetic checker.

### 1.3 The honesty ledger

Every claim in this paper carries a mathematical status (up to INDEPENDENTLY-CHECKED, meaning
whole-theorem independent review with no self-declared success) and, where applicable, a
computational status (up to INDEPENDENT-CHECKER, an independently written offline replay). A
finite certificate validates only the finite statement it replays, never the analytic theorem
that produced it. The three theorems below are at INDEPENDENTLY-CHECKED; B1, B2, and G-info
additionally have deposited independent checkers.

---

## 2. Setup

**Ambient class.** `𝔛_sym` is the set of locally finite multisets `𝒵` of points in the open
critical strip `{0 < Re s < 1}`, symmetric under `ρ ↦ ρ̄` and `ρ ↦ 1−ρ`, with a fixed
admissibility exponent: `Σ_{ρ∈𝒵} |ρ|^{-(1+ε)} < ∞` for some `ε > 0`. Membership is checkable,
and any finite symmetric multiset is a member.

**Target predicate.** `P(𝒵) = 1` iff every atom `ρ ∈ 𝒵` has `Re ρ = 1/2`; else `P(𝒵) = 0`.

**Test families (for B1/B2).** We use three interchangeable families of test functions:
- *Li-type:* `φ_j(ρ) = 1 − (1 − 1/ρ)^j`;
- *Weil-W2:* `φ_j(ρ) = ĥ_j(Im ρ)`, `h_j ∈ C_c^∞(ℝ; ℝ)` even, `ĥ_j(ξ)=∫h_j(x)e^{iξx}dx`
  (evaluation at the imaginary part only — the "even test" convention; complex-point Weil
  evaluation is excluded, as `ĥ` has exponential type and need not decay);
- *moment:* `φ_j(ρ) = ρ^{-j}`, `j ≥ 1`.

**Observation maps and the Σ′ convention (read carefully).** The two finite-observation
theorems use *different* summation conventions, differing by a factor of 2; the reader must
not transport a numerical anchor between them.
- **B1 uses the R-atom convention** `O_j(𝒵) = Σ'_{ρ∈𝒵} φ_j(ρ)` — each atom counted once, the
  prime denoting a symmetric-height regularization for convergence, **not** doubling.
- **B2 uses the R-symm convention** `O_j(𝒵) = Σ_{ρ∈𝒵} [φ_j(ρ) + φ_j(1−ρ)]` — which doubles on
  a multiset closed under `ρ ↦ 1−ρ`.
Both give `O_j ∈ ℝ` for the real-coefficient families above. B2's collision identity is
scale-invariant (see §4), so the factor is harmless there; B1's decay anchors are stated in
the R-atom convention and are **not** the R-symm values.

**Off-line quartet.** For `σ_0 ∈ (0,1)\{1/2}` and `T>0`,
`Q(σ_0,T) := {σ_0+iT, 1−σ_0+iT, σ_0−iT, 1−σ_0−iT}` — a symmetric member of `𝔛_sym` with
`P(Q)=0`. We fix `σ_0 = 3/4` throughout.

---

## 3. Theorem B1 — no uniform separation margin

**Theorem B1.** Let `Φ = (φ_1,…,φ_m)` be any finite test family of the above types, let
`𝒵_+ ∈ 𝔛_sym` with `P(𝒵_+)=1` satisfy strict inequalities `(O_Φ(𝒵_+))_j > c_j`
(`j=1,…,m`), and let `ε_j > 0`. Then there exists `𝒵_- ∈ 𝔛_sym` with `P(𝒵_-)=0` and
`|(O_Φ(𝒵_-))_j − (O_Φ(𝒵_+))_j| < ε_j` for all `j`; in particular `(O_Φ(𝒵_-))_j > c_j`
whenever `ε_j < (O_Φ(𝒵_+))_j − c_j`. Consequently the infimum, over admissible constructions,
of the coordinatewise observation gap between the `P=1` and `P=0` classes is `0`: **no fixed
positive coordinate margin separates the two classes.**

*(`𝒵_+` ranges over abstract `P=1` members — e.g. explicit finite on-line multisets. The
instantiation "`𝒵_+` = the ζ zero multiset" is conditional on RH and is not used.)*

### 3.1 Off-line quartet lemma

**Lemma B1.1.** For `φ` of any of the three types and `σ_0 ∈ (0,1)\{1/2}`, the quartet
contribution `δ_j(T) := φ_j(σ_0+iT)+φ_j(1−σ_0+iT)+φ_j(σ_0−iT)+φ_j(1−σ_0−iT)` is continuous in
`T>0` and `δ_j(T) → 0` as `T → ∞`.

*Proof.* Li-type: `|1/ρ| ≤ (T²+σ_0²)^{-1/2} → 0`, so `φ_j(σ_0±iT) → 0` and likewise for
`1−σ_0±iT`. Weil-W2: `h_j ∈ C_c^∞` gives, by `N`-fold integration by parts,
`|ĥ_j(T)| ≤ C_N(1+|T|)^{-N}`; with `h_j` even, `δ_j(T)=4ĥ_j(T) → 0` (Riemann–Lebesgue,
[Rudin 1987, Thm 9.6]). Moment: `|φ_j(ρ)| = |ρ|^{-k} = O(T^{-k}) → 0`. Continuity is immediate
from continuity of `φ_j` in `ρ` and of the quartet points in `T`. ∎

**Convergence of `Σ'` (R-atom).** The Li terms are only `O(|ρ|^{-1})`, not dominated by the
admissibility series `Σ|ρ|^{-(1+η)}` (`1<1+η`). Grouping each `ρ=σ+it` with its conjugate, the
real-coefficient pair contributes `2Re φ_j`; the leading term gives
`2Re(1/ρ)=2σ/(σ²+t²)=O(|Im ρ|^{-2})`, and every higher inverse power is also `O(|Im ρ|^{-2})`;
since `1+η<2`, the grouped sum converges absolutely. (Weil-W2 by the same comparison via the
`(1+|t|)^{-N}` bound.)

### 3.2 Proof of Theorem B1

By Lemma B1.1 choose `T_*` so large that `|δ_j(T_*)| < ε_j` for all `j=1,…,m` (possible since
`m` is finite). Set `𝒵_- := 𝒵_+ ∪ Q(3/4, T_*)`. Then `𝒵_- ∈ 𝔛_sym` (union of admissible
members); `P(𝒵_-)=0` (the atoms `3/4 ± iT_*` are off-line); and
`|(O_Φ(𝒵_-))_j − (O_Φ(𝒵_+))_j| = |δ_j(T_*)| < ε_j`. ∎

### 3.3 Precise strength (what B1 is and is not)

B1 asserts that the observation-gap **infimum** between the classes is `0` — there is no
positive uniform margin. It does **not** assert an exact discriminator failure at fixed
inputs; distinguishing the two classes by an exact discontinuous rule on precise real inputs
is not excluded by B1 (that is B2's job). The quartet contribution is strictly positive for
each finite `T` (e.g. `δ_1(T)=2[σ/(σ²+T²)+(1−σ)/((1−σ)²+T²)] > 0` for the Li first
coordinate), so this is a statement about the observation-separation infimum, **not** a
shrinking positivity margin of a sufficient inequality — keeping B1 clear of the "margin → 0"
non-barrier label. In the R-atom convention the exact decay anchors are `δ_1(1)=608/425`,
threshold `T_* = 90` (for `σ_0=3/4, m=2, ε=10^{-3}`), and `δ_j(T)·T² → 2j²`; these are
independently machine-checked (Appendix A).

---

## 4. Theorem B2 — exact observation collision

**Theorem B2.** For any finite test family `Φ = (φ_1,…,φ_m)` of Li or moment type there exist
`𝒵_+, 𝒵_- ∈ 𝔛_sym` with `P(𝒵_+)=1`, `P(𝒵_-)=0`, **all multiplicities integers**, and
`O_Φ(𝒵_+) = O_Φ(𝒵_-)` **exactly**. Here `𝒵_+` consists of on-line pairs and `𝒵_-` differs by
adding an off-line quartet and adjusting on-line multiplicities.

We use the R-symm convention `O_j(𝒵) = Σ_ρ[φ_j(ρ)+φ_j(1−ρ)]`, additive under multiset union;
on one on-line pair `L(t)={1/2±it}` it gives `O_j(L(t)) = 4 Re φ_j(1/2+it)`, and on the quartet
`O_j(Q(3/4,T)) = 4 Re[φ_j(3/4+iT)+φ_j(1/4+iT)]`.

### 4.1 Nonsingular Jacobian (self-contained Vandermonde)

Fix distinct rational heights `t_1 < … < t_m > 0`. For the Li family, with
`x_k = (4t_k²−1)/(4t_k²+1) ∈ ℚ` and Chebyshev `T_j`,
```
C_{jk} := O_j(L(t_k)) = 4(1 − T_j(x_k)),      j,k = 1,…,m.
```
Writing `1−T_j(x) = (1−x)Q_{j-1}(x)` with `deg Q_{j-1}=j-1` and leading coefficient `2^{j-1}`,
the matrix `[Q_{j-1}(x_k)]` equals `U·V(x_1,…,x_m)` for an upper-triangular `U`
(Chebyshev-to-monomial change of basis) and the Vandermonde `V`. Hence
```
det C = 4^m · (∏_k (1−x_k)) · 2^{m(m-1)/2} · ∏_{k<l}(x_l − x_k) ≠ 0,
```
all factors nonzero (`1−x_k>0`; `x_k` distinct and increasing). For rational `t_k`, `x_k ∈ ℚ`,
so `C ∈ ℚ^{m×m}` and `det C ∈ ℚ\{0}`. (The moment family gives the analogous cosine-Vandermonde
`[cos(jφ_k)]`, nonsingular by the same reduction; see the theorem file §4.4.)

### 4.2 Exact collision with integer multiplicities

Let `d(T)_j := O_j(Q(3/4,T)) ∈ ℚ^m` (rational for rational `T`) and solve
`C α^ℚ = −d(T)`, `α^ℚ ∈ ℚ^m`. Put `R := lcm(\text{denominators of } α^ℚ)` and
`n_k := R·α^ℚ_k ∈ ℤ`. Scaling by `R` gives the **exact integer identity**
```
C·n + R·d(T) = 0.
```
This identity is scale-invariant (`C → 2C, d → 2d` leaves `n, R` and the identity unchanged),
so the R-symm-vs-R-atom factor is immaterial here. Set the multiplicity buffer
`M := max_k |n_k|` and define
```
𝒵_+ := ⊔_{k=1}^m M·L(t_k),        𝒵_- := ⊔_{k=1}^m (M+n_k)·L(t_k) ⊔ R·Q(3/4,T).
```
Both are in `𝔛_sym`; `M+n_k ≥ 0` so `𝒵_-` is a valid multiset; `P(𝒵_+)=1`, `P(𝒵_-)=0`. Since
`O_Φ` is additive,
```
O_j(𝒵_-) − O_j(𝒵_+) = Σ_k n_k·O_j(L(t_k)) + R·O_j(Q(3/4,T)) = (C·n)_j + R·d(T)_j = 0. ∎
```

### 4.3 Non-vacuity and scope

Both adversaries are **constructed** finite members of `𝔛_sym`; B2 does **not** assert that
ζ's zeros are indistinguishable from an off-line configuration. A structural non-vacuity check
(the quartet's first coordinate `d_1(T) = 64(16T²+3)/(256T⁴+160T²+9) > 0` for all real `T`)
confirms the target vector is nonzero, so the solve is non-trivial. The exact-rational
collision has been independently reconstructed from the definition (two agreeing routes,
adversarial mutation guard); see Appendix A.

---

## 5. Theorem G-info — diagonal Fredholm obstruction

We now pass one observation layer up, to the archimedean levels used in
Connes–Consani–Moscovici-style spectral determinant approaches [CCM 2025].

**Observation.** `O_θ(n) = d_n := θ_level(n)`, the zero-free Riemann–Siegel unfolding levels
(`θ(t) = Im log Γ(1/4+it/2) − t log π /2`), a sequence determined by the Γ-function alone.
**Method class `𝔐_d^{tr}`.** Finite-rank positive semidefinite families `(K_N)` with
`K_N = Φ_N(d_1,…,d_N)` and `‖K_N − D_N‖_1 → 0`, where `D_N = diag(κ_1,…,κ_N)`,
`κ_n = 1/(1/4+d_n²)`. Non-empty (witness `K_N = D_N`).

**Target.** The predicate is "the locally uniform limit of `det(I − z²K_N)` equals `Ξ̂`", the
entire CCM target (`Ξ̂` = normalized so `Ξ̂(0)=1`), whose zeros are real iff RH holds.

**Theorem G-info.** For every `(K_N) ∈ 𝔐_d^{tr}`,
```
det(I − z²K_N) → G_d(z) = ∏_{n≥1} (1 − z²/(1/4 + d_n²))
```
locally uniformly (trace-norm stability of Fredholm determinants + `‖K_N−D_N‖_1 → 0`), and
```
G_d ≠ Ξ̂    unconditionally.
```

*Proof of `G_d ≠ Ξ̂`.* Two cases. If RH holds, `Ξ̂ = C∏(1−z²/γ_n²)` has zeros `{±γ_n}`, while
`G_d` has zeros `{±√(1/4+d_n²)}`; these differ because `√(1/4+d_n²) > d_n` and `d_n ≠ γ_n` for
infinitely many `n` (the arithmetic-fluctuation gap `γ_n − d_n ~ S(γ_n)/A'(γ_n)`,
`A'(t)=θ'(t)/π`; Prop. G.3*, proved unconditionally). If RH fails, `Ξ̂` has a non-real zero
while every zero of `G_d` is real. Either way `G_d ≠ Ξ̂`. ∎

**Two independent separations** are visible: (i) a spectral-parameter shift
`d_n ↦ √(1/4+d_n²)` (the diagonal determinant's zeros are not at `±d_n`), and (ii) the `S(T)`
gap `{d_n} ≠ {γ_n}`. The first survives even if one corrects the `1/4` shift.

**Scope: G-info vs G-hard.** G-info (above) is the diagonal obstruction, INDEPENDENTLY-CHECKED.
The general claim "no method in the larger class `𝔐_FC` can supply the `S(T)` data without
reading zero ordinates or computing an RH-equivalent quantity" is a separate **conjecture
(G-hard)** and is **not** claimed here. This paper asserts only the diagonal G-info theorem.

**Why convergence would be RH-strength.** If some `(K_N)` in the class had
`det(I−z²K_N) → Ξ̂` locally uniformly, then by Hurwitz the real zeros of the approximants would
force `Ξ̂` to have all real zeros — i.e. RH. So a convergence claim in this class cannot be a
zero-independent input; it would *imply* RH. G-info shows the diagonal limit is a different
function, `G_d`, so the approach does not even converge to the target.

---

## 6. Escape routes

The obstructions apply exactly to the stated observation. Each theorem names a strictly larger
class or richer observation to which it does **not** apply:

1. **Infinite test hierarchy** (`K → ∞`, all Li/Weil data).
2. **Euler product / multiplicative structure** (Selberg-class axioms).
3. **Gamma factor and analytic continuation** — archimedean data beyond `O_Φ`.
4. **Coefficient arithmetic** (integrality/positivity of Dirichlet coefficients).
5. For G-info: methods supplying genuine `S(T)` data (the G-hard frontier), or non-diagonal
   `K_N` outside `𝔐_d^{tr}`.

These are the honest boundaries: the theorems locate difficulty at the finite/archimedean
observation layer and say nothing about methods that cross it.

---

## 7. Limitations and honest boundaries

- **Not RH.** No theorem here proves, disproves, or approaches RH; RH is neither assumed nor
  concluded. B1/B2 construct adversary multisets, not ζ; G-info's `𝒵_RH` appears only as a
  hypothetical target and its reality is never used.
- **B1 is "no uniform margin", not an exact-discriminator failure** (§3.3).
- **B2's adversaries are constructed**, not ζ's zeros (§4.3).
- **G-info is the diagonal obstruction only; G-hard is a conjecture** (§5).
- **Finite certificates validate finite statements.** The Appendix A checkers replay the
  finite decay/collision/interval facts; they do not certify the analytic theorems.

---

## Appendix A. Deposited independent checkers

All are pure-standard-library, exact-rational or outward-rounded interval, with no floating
point in the certificate path; each re-runs to `ALL_CERTIFIED_CHECKS_PASSED` and is pinned by
SHA-256.

| Checker | Theorem | Validates | SHA-256 (prefix) |
|---|---|---|---|
| `b1_ratom_certified_checker.py` | B1 | R-atom decay `δ_1(1)=608/425`, `T_*=90`, `δ_j T² → 2j²` | `199c7dad…` |
| `b2_certified_checker.py` | B2 | exact collision `Cn+Rd=0`, two agreeing routes, mutation guard | `776eeab5…` |
| `diagonal_fredholm_interval_replay.py` | G-info | Gram levels `d_n`, separation `γ_n<d_n<√(1/4+d_n²)`, tail bound | `e197f2bb…` |

A finite certificate validates only the finite replayed statement, never the analytic theorem
that produced it.

---

## References (to be completed)

- E. Bombieri, *The Riemann Hypothesis*, Clay Mathematics Institute problem description, 2000.
- E. Bombieri, J. Lagarias, *Complements to Li's criterion…*, J. Number Theory 77 (1999).
- M. Berry, J. Keating, *H = xp and the Riemann zeros*, SIAM Review 41 (1999).
- A. Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta
  function*, Selecta Math. 5 (1999).
- A. Connes, C. Consani, H. Moscovici, *Zeta spectral triples*, arXiv:2511.22755 (2025).
- X.-J. Li, *The positivity of a sequence of numbers and the Riemann Hypothesis*,
  J. Number Theory 65 (1997).
- W. Rudin, *Real and Complex Analysis*, 3rd ed., McGraw-Hill, 1987 (Thm 9.6).
- A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*, 1952.
