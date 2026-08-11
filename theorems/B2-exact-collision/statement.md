# Theorem B2 — Exact Finite-Observation Collision

**Mathematical status:** PROOF-DRAFT (CONFIRMED by OB-02 external review 2026-08-11 — integer-sign step resolved; four notation corrections applied; see proof.md)  
**Computational status:** REPRODUCIBLE (rational m=2 sanity check in proof.md §4.5: t₁=1, t₂=2, T=1, exact rational arithmetic ✓)  
**Theorem ID:** B2-exact-collision  
**Program ref:** §7.B.2.B2, §7.B.3  
**Paper target:** Paper A (primary, if rank condition holds)

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

**Theorem B2 (conditional on rank).** Assume:

(H-rank) The Jacobian `J` has full column rank over `ℝ` (i.e. `rank J = n`),
which requires `m ≥ n`. More precisely, there exist heights `t₁, …, t_n` such that
`J_{jk}` is non-singular in the appropriate sense for the solution step.

(H-real-mult) The compensating adjustments `α_k` can be taken as positive integers
(multiplicity additions), not just signs.

Then there exist heights `t₁ < … < t_n`, a choice of `n`, and `T_* > t_n` such
that the multiset `𝒵_−` defined above satisfies:

1. `𝒵_− ∈ 𝔛_sym`.
2. `P(𝒵_−) = 0` (off-line zeros `σ₀ ± iT_*`).
3. `O_Φ(𝒵_−) = O_Φ(𝒵_+)` (exact collision, no tolerance).

**Scope.**  The conclusion applies to `𝔛_sym` with the stated finite `Φ`.  It does
not apply to methods using the full Euler product, gamma factor, or infinite test
hierarchy (escape routes identical to B1).

---

## Rank and integer-sign status (RESOLVED, OB-02 2026-08-11)

The rank condition and integer-sign condition are both resolved in proof.md §4:

| Step | Status | Result |
|---|---|---|
| Rank of Li Jacobian C (§4.3) | PROOF-DRAFT ✓ | det C ≠ 0 by Chebyshev + lower-triangular + Vandermonde |
| Rank of moment Jacobian (§4.4) | PROOF-DRAFT ✓ | cosine-Vandermonde argument |
| Integer solution via scaling (§4.5) | PROOF-DRAFT ✓ | β = −C⁻¹d(T) ∈ ℚᵐ; scale by lcm-denominator R → n ∈ ℤᵐ |
| Nonneg multiplicity via buffer M | PROOF-DRAFT ✓ | M = max_k|n_k|, then M+n_k ≥ 0 |
| m=2 rational sanity check | CONFIRMED ✓ | t₁=1, t₂=2, T=1: exact rational arithmetic |

---

## Escape route (program §3.2)

Same five escape routes as B1, plus:

6. **Multiplicity constraint:** if exact collision requires signed or nonintegral
   multiplicities (fractional zero counts), the theorem is retracted; B1 remains.
   (This is resolved: the integer-sign step in proof.md §4.5 gives nonneg integer
   multiplicities via the scaling and buffer construction.)

---

## Paper A theorem (B2 confirmed — PROOF-DRAFT)

B2 is confirmed with nonneg integer multiplicities (proof.md §4.5, OB-02 2026-08-11).
The Paper A theorem is:

> For any fixed finite test family `Φ` of Li-type or moment-type tests, there exist
> `𝒵_+ ∈ 𝔛_sym` with `P=1` and `𝒵_− ∈ 𝔛_sym` with `P=0` such that
> `O_Φ(𝒵_−) = O_Φ(𝒵_+)` exactly (not just approximately).

Open refinement question: whether the ambient class 𝔛_sym should additionally
require the Riemann–von Mangoldt counting law (see outsource OB-07).
