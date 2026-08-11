# Theorem B2 — Exact Finite-Observation Collision

**Mathematical status:** INDEPENDENTLY-CHECKED (Gate-A PASS by OB-20 external review 2026-08-11: whole-theorem inspection of all six links + Q1–Q5, no blocking gap / circularity / RH-import; every load-bearing fact independently re-derived from φ_j and cross-computed. Earlier: PROOF-DRAFT confirmed by OB-02.)  
**Computational status:** INDEPENDENT-CHECKER (OB-13 external review 2026-08-11: the exact-rational collision was reconstructed from φ_j in an independent implementation — Python stdlib `fractions`, SHA-256-pinned source, two routes agree, adversarial mutation breaks it; m=2 and m=3 instances both give exact zero residual)  
**Theorem ID:** B2-exact-collision  
**Program ref:** §7.B.2.B2, §7.B.3  
**Paper target:** Paper A (primary — Gate-A PASS 2026-08-11)

---

## Definitional clarifications (OB-13 external review, 2026-08-11)

The finite-observation collision was independently reconstructed in exact rational
arithmetic (OB-13, CONFIRMED). Two definitions, implicit in the B1-inherited setup, are
made explicit here (they add no analytic assumption; they fix the normalization the
numerical claim depends on):

1. **Global observation map.** For a finite multiset `𝒵` of nonzero complex numbers
   avoiding `{0,1}`, with multiplicity,
   ```
   O_j(𝒵) := Σ_{ρ ∈ 𝒵} [φ_j(ρ) + φ_j(1−ρ)].
   ```
   **Convention note (OB-23 correction).** This is B2's OWN convention (call it R-symm);
   it is NOT identical to B1's `Σ'` — B1 sums `φ_j` over atoms once (R-atom), whereas this
   doubles on a multiset closed under `ρ↦1−ρ`. The two differ by a factor of 2 (see the
   cross-theorem convention note below). B2's exact collision `Cn + Rd = 0` is
   **scale-invariant** (C→2C, d→2d leaves β,R,n,M and the collision identity unchanged), so
   B2's construction, Gate-A PASS (OB-20), and checker (OB-21) are all valid under this
   convention; only the displayed `C, d, δ` values are a factor 2 larger than B1's. It is
   additive under multiset union. On one on-line pair `L(t)` the reflection `ρ ↦ 1−ρ` swaps the two
   atoms, so `O_j(L(t)) = 4 Re φ_j(1/2+it)`; on the quartet `Q(3/4,T)`,
   `O_j(Q) = 4 Re[φ_j(3/4+iT) + φ_j(1/4+iT)]`. (The factor 4 in both proof.md formulas
   is forced by this global definition; the ordinary atomwise sum would halve C and d.)

2. **Predicate.** `P(𝒵) = 1` iff every atom `ρ ∈ 𝒵` has `Re ρ = 1/2`, else `P(𝒵) = 0`.

With these, OB-13 verified (exact rational arithmetic, no floating point):
V1 the full m=2 table (x, C, det C, d, β, R, n, M, `Cn+Rd=0`); V2 nonneg multiplicities
`(M+n₁, M+n₂)=(7388,0)`; V3 predicate separation; V4 an independent m=3 instance
(`t=(1,2,3), T=2`) with exact zero residual; V5 adversarial mutation `n₁ ↦ n₁+1` giving
nonzero residual `(8/5, 128/25)`. The nonsingularity `det C ≠ 0` for distinct positive
heights was proved in closed form (OB-13 Lemma 2.3: scaled Vandermonde). This validates
**only the finite identity** — it asserts nothing about any analytic function or RH.

---

## Setting (inherits from B1)

Use the same `𝔛_sym`, `O_Φ`, `P` as in `B1-finite-inequality/statement.md`.
Additionally, fix:

- `Φ = (φ₁, …, φ_m)` with `m ≥ 1` specific test functions;
- a "base" multiset `𝒵_+ ∈ 𝔛_sym` with `P(𝒵_+) = 1` (reference on-line set);
- `n ≥ 1` **on-line compensating atoms** at heights `t₁ < t₂ < … < t_n` (to be
  chosen), meaning we add/remove pairs `{1/2 + it_k, 1/2 − it_k}` to/from `𝒵_+`;
- one **off-line symmetric quartet** `Q(σ₀, T)` with `σ₀ ∈ (1/2, 1)`, `T > t_n`.

Denote by `α_k ∈ {+1, −1}` the sign of the `k`-th on-line adjustment (add
or remove). The perturbed multiset is

```
𝒵_−(α, T) := (𝒵_+ ∖ {removed on-line atoms}) ∪ {added on-line atoms} ∪ Q(σ₀, T).
```

---

## Observation Jacobian

Define the observation **difference vector** `Δ ∈ ℝ^m`:

```
Δ_j := O_j(𝒵_−) − O_j(𝒵_+)
      = Σ_{k=1}^{n} α_k · [φ_j(1/2+it_k) + φ_j(1/2−it_k)]
        + δ_j^{off}(T),
```

where `δ_j^{off}(T) = φ_j(σ₀+iT) + φ_j(1−σ₀+iT) + φ_j(σ₀−iT) + φ_j(1−σ₀−iT)`
is the quartet contribution (tends to `0` as `T → ∞` by Lemma §2 of proof.md,
or its analogue here).

Define the **on-line Jacobian matrix** `J ∈ ℝ^{m×n}`:

```
J_{jk} := φ_j(1/2+it_k) + φ_j(1/2−it_k)     (j=1,…,m;  k=1,…,n).
```

The system we must solve for exact collision `Δ = 0` is:

```
J · α = −δ^{off}(T),      α ∈ {±1}^n  or  α ∈ ℤ^n  (depending on model).
```

---

## Theorem B2 (exact finite-observation collision)

**Theorem B2 (unconditional; Gate-A PASS OB-20).** For any fixed finite Li-type or
moment-type test family `Φ = (φ_1,…,φ_m)`, there exist distinct rational heights
`t_1 < … < t_m`, a rational `T > 0`, and nonneg integer multiplicities such that the
multisets `𝒵_+, 𝒵_−` constructed above satisfy:

1. `𝒵_+, 𝒵_− ∈ 𝔛_sym`;
2. `P(𝒵_+) = 1` and `P(𝒵_−) = 0` (the off-line quartet `Q(3/4,T)` puts atoms at
   `Re = 3/4 ≠ 1/2`);
3. `O_Φ(𝒵_−) = O_Φ(𝒵_+)` (exact collision, no tolerance).

The two former hypotheses are now **proved**, not assumed:
- **(H-rank) — PROVED.** The Jacobian `C` (Li) / moment matrix has full rank: `det C ≠ 0`
  for distinct positive rational `t_k`, by the self-contained Chebyshev + lower-triangular
  + Vandermonde argument (proof.md §4.3–§4.4; Gate-A re-verified, OB-20).
- **(H-real-mult) — PROVED.** The adjustments are nonneg integers: `β = −C⁻¹d(T) ∈ ℚᵐ`,
  scaled by `R = lcm(denominators)` to `n ∈ ℤᵐ`, with buffer `M = max_k|n_k|` giving
  `M + n_k ≥ 0` (proof.md §4.5).

**Scope.**  The conclusion applies to `𝔛_sym` with the stated finite `Φ`.  It does
not apply to methods using the full Euler product, gamma factor, or infinite test
hierarchy (escape routes identical to B1).

**Structural non-vacuity (OB-20 Gate-A review, 2026-08-11 — independently verified).**
The predicate separation `P(𝒵_+)=1 ≠ 0=P(𝒵_−)` is not a coincidence of a particular
`(m, t_k, T)`; it holds for **every** admissible input. Reason:
```
d_1(T) = 4 Re[φ_1(3/4+iT) + φ_1(1/4+iT)] = 64(16T²+3)/(256T⁴+160T²+9) > 0  for all real T
```
(numerator and denominator are sums of positive terms; no real zero — verified symbolically).
Hence `β = −C⁻¹d(T) ≠ 0` always, so `n = Rβ` has a nonzero component, `M = max_k|n_k| ≥ 1`,
and `R = lcm(denominators) ≥ 1` always. Therefore `𝒵_+` is never empty and `𝒵_−` always
contains at least one copy of the off-line quartet `Q(3/4,T)`. Moreover, since `t_k > 0`
and `T > 0`, every atom of `L(t_k)` and `Q(3/4,T)` is **non-real** (imaginary part ≠ 0),
so the no-real-atom condition (NR) is **automatically satisfied** by the construction — it
is not an assumption that must be added (the earlier concern that invisible real atoms
`{1/4, 3/4}` could trivialize the obstruction does not arise, since `T = 0` is excluded by
definition).

---

## Rank and integer-sign status (PROVED; Gate-A PASS OB-20 2026-08-11)

The rank condition and integer-sign condition are both resolved in proof.md §4, and the
full assembly passed independent Gate-A review (OB-20):

| Step | Status | Result |
|---|---|---|
| Rank of Li Jacobian C (§4.3) | PROVED ✓ (Gate-A checked) | det C ≠ 0 by Chebyshev + lower-triangular + Vandermonde |
| Rank of moment Jacobian (§4.4) | PROVED ✓ (Gate-A checked) | cosine-Vandermonde argument |
| Integer solution via scaling (§4.5) | PROVED ✓ (Gate-A checked) | β = −C⁻¹d(T) ∈ ℚᵐ; scale by lcm-denominator R → n ∈ ℤᵐ |
| Nonneg multiplicity via buffer M | PROVED ✓ (Gate-A checked) | M = max_k|n_k|, then M+n_k ≥ 0 |
| m=2 rational sanity check | CONFIRMED ✓ | t₁=1, t₂=2, T=1: exact rational arithmetic |
| Full six-link assembly | INDEPENDENTLY-CHECKED ✓ | OB-20 whole-theorem Gate-A review: no gap / circularity / RH-import |

---

## Escape route (program §3.2)

Same five escape routes as B1, plus:

6. **Multiplicity constraint:** if exact collision requires signed or nonintegral
   multiplicities (fractional zero counts), the theorem is retracted; B1 remains.
   (This is resolved: the integer-sign step in proof.md §4.5 gives nonneg integer
   multiplicities via the scaling and buffer construction.)

---

## Paper A theorem (B2 — INDEPENDENTLY-CHECKED, Gate-A PASS)

B2 is confirmed with nonneg integer multiplicities (proof.md §4.5, OB-02 2026-08-11).
The Paper A theorem is:

> For any fixed finite test family `Φ` of Li-type or moment-type tests satisfying (R)
> and (OD) (see §7 below), there exist `𝒵_+ ∈ 𝔛_sym^{(*),nr}` with `P=1` and
> `𝒵_− ∈ 𝔛_sym^{(*),nr}` with `P=0` such that `O_Φ(𝒵_−) = O_Φ(𝒵_+)` exactly.

**Counting-law lift (OB-07 referee Theorem 8.1, 2026-08-11).** Assuming the finite
collision premise (FC) below, the Paper A theorem holds for the augmented ambient class
`𝔛_sym^{(*),nr}` — the subclass of `𝔛_sym` satisfying:
- **(NR):** `𝒵 ∩ ℝ = ∅` (no real atoms);
- **(*):** `N_𝒵(T) = (T/2π)log(T/2π) − T/2π + O(log T)`.

**Construction (unconditional background, OB-07 §6).** Define `F(T) = (T/2π)log(T/2π) − T/2π`
and let `γ_n^{bg}` be the unique solution to `F(γ_n^{bg}) = n` for each `n ≥ 1`.  Set
`𝒟 = ⊔_{n≥1} L(γ_n^{bg})`.  Then `N_𝒟(T) = F(T) + O(1)`, `𝒟` satisfies (NR) and all
three conditions of `𝔛_sym`, and no zeta zero or RH hypothesis is used.

Set `𝒵_+ = 𝒟 ⊔ A_+` and `𝒵_− = 𝒟 ⊔ A_−` where `A_+, A_−` are the finite B2 blocks.
Then `𝒵_±  ∈ 𝔛_sym^{(*),nr}`, `P(𝒵_+) = 1`, `P(𝒵_−) = 0`, and `O_Φ(𝒵_+) = O_Φ(𝒵_−)`
(using (OD) for absolute convergence and additivity of `O_Φ` under the finite adjunction,
plus the finite-collision premise (FC)).

**Finite-collision premise (FC).** The lift is a complete proof from (FC):
> For the specified B2 test family Φ satisfying (R) and (OD), there are finite
> symmetric nonreal multisets `A_+, A_−` such that every point of `A_+` is on
> `Re s = 1/2`, `A_−` contains an off-line quartet, and `O_Φ(A_+) = O_Φ(A_−)`.

(FC) is proved in proof.md §4 (OB-02, 2026-08-11). The lift above is independent of (FC)'s
proof; it converts (FC) into the full Paper A theorem for the augmented class.

**Non-vacuity note (OB-07 referee §4).** Without (NR), the class `𝔛_sym` admits real
atoms `{1/4, 3/4}` which are invisible to both `N_𝒵` and `O_Φ`, making the obstruction
vacuous.  (NR) is therefore mandatory for a non-trivial theorem.

**Test-class restriction.** "Any fixed finite test family" must be qualified: the test
functions must satisfy (R) (`φ_j(z̄) = φ_j(z)̄`) for `O_j` to be real-valued, and (OD)
(uniform orbit-decay `|B_j(β+it)| ≤ C_j(1+t)^{−1−δ_j}`) for absolute convergence on
infinite multisets.  The standard Li test family `φ_r(z) = 1−(1−z^{−1})^r` satisfies
both (OD holds with `δ_r = 1`; see OB-07 referee §7).

Open refinement question: whether the ambient class `𝔛_sym` should additionally
require the Riemann–von Mangoldt counting law (now answered affirmatively by OB-07).

---

## §7. Counting-function formulas — CORRECTED (OB-07 referee §2.1)

The formulas for `N_{A_+}` and `N_{A_-}` in proof.md had sign errors. The correct
formulas are:

For `T_* = max(t_1,…,t_m, T)` (height above all atoms):
```
N_{A_+}(T_*) = mM          (M pairs for each of m on-line heights).
N_{A_-}(T_*) = mM + Σ_k n_k + 2R    (n_k on-line adjustments; Q contributes 2 upper-half points).
```

Note: one copy of `L(t)` contributes exactly ONE point with `Im > 0` (not two); one copy
of `Q(3/4,T)` contributes exactly TWO points with `Im > 0`.  The original formulas `2mM`
and `2Σ n_k + R` were incorrect.

Also: `Σ_k n_k + 2R` need not be positive (n_k can be negative); the buffer M ≥ max|n_k|
ensures nonneg multiplicities but does not force N_{A_-} > N_{A_+}.
