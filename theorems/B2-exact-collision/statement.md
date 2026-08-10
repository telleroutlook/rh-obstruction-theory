# Theorem B2 — Exact Finite-Observation Collision

**Mathematical status:** PROOF-DRAFT (conditional — see §Rank condition below)  
**Computational status:** NONE (analytic; no certified witness yet)  
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

## Rank condition status

The rank condition (H-rank) is the central open item of P3 (Days 15–21).  Three
outcomes are possible:

| Outcome | Status | Consequence |
|---|---|---|
| `rank J = n` proved for some `n`, heights `t₁,…,t_n` | OPEN | B2 holds; Paper A proceeds |
| `rank J < n` for all natural choices | OPEN | B2 fails; keep B1 only |
| `rank J = n` requires signed/noninteger `α` | OPEN | B2 fails; H-real-mult violated; keep B1 |

The rank analysis occupies `proof.md §3` (to be completed).

---

## Escape route (program §3.2)

Same five escape routes as B1, plus:

6. **Multiplicity constraint:** if exact collision requires signed or nonintegral
   multiplicities (fractional zero counts), the theorem is retracted; B1 remains.

---

## Conditional on B2 closing: Paper A upgrading

If B2 closes with real, positive-multiplicity zeros, then the paper-A theorem is:

> For any fixed finite test family `Φ`, there exist `𝒵_+ ∈ 𝔛_sym` with `P=1`
> and `𝒵_− ∈ 𝔛_sym` with `P=0` such that `O_Φ(𝒵_−) = O_Φ(𝒵_+)` exactly.

Otherwise Paper A reduces to B1 (strict inequality, not exact equality), and the
convergence track (Paper C) becomes the primary.
