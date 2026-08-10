# Proof — Theorem F (restricted Schur-certificate complexity lower bound)

**Status:** PROOF-DRAFT (conditional on non-vacuity + representation-invariance gates)  
**Analytic / finite separation:** purely analytic; no finite certificate.

---

## §1. Setup

Let `a > 0`, `N ≥ 1`, `δ ∈ (0, λ(a))` (note: `λ(a) > 0` for small `a` by Suzuki Thm 1.4,
and `λ(a) = log(1/a) + μ₁ − log(2π) + ψ(2) − 1 + O(a)` as `a → 0⁺`).

The Weil matrix `M_{a,N}` is symmetric positive definite (since `Q_W^a` is positive for
small `a` by Suzuki Thm 1.3/1.4). Its eigenvalues satisfy:
```
λ₁(a,N) ≤ λ₂(a,N) ≤ … ≤ λ_N(a,N),
```
with `λ₁(a,N) → λ(a)` as `N → ∞` (Galerkin convergence of the lowest eigenvalue).

---

## §2. Structure of a `P_{r,N}`-certificate

A rank-`r` certificate in `P_{r,N}` is:
1. An orthogonal change of basis `U ∈ O(N)`.
2. A block decomposition of `U^T M_{a,N} U − δ I` into blocks `B₁, …, B_k` with
   `k ≤ r`, each certified positive semidefinite.

**Observation.** Each block `B_i` is a principal submatrix of `U^T M_{a,N} U − δ I`.
The certificate works if and only if `U^T M_{a,N} U − δ I ≽ 0`, which is equivalent to
`λ_min(M_{a,N}) ≥ δ` (a scalar statement, independent of `U`).

**Consequence.** For any fixed `δ > 0`:
- If `δ < λ₁(a,N)`, a rank-1 certificate exists (the full matrix itself), so `κ = 1`.
- If `δ ≈ λ₁(a,N)` and the eigenvector corresponding to `λ₁` is spread across all
  coordinates, no rank-`r` certificate with `r < N` can avoid the minimal eigenvalue.

**For the lower bound**, the key is that the minimum eigenvalue `λ₁(a,N)` is approached
by a vector spread across all `N` components, requiring at most `N` Schur steps to certify.

---

## §3. Lower bound argument (conditional sketch)

**Claim F.LB (PROOF-DRAFT):** For fixed `N` and `δ ∈ (0, λ(a))`, as `a → ∞`:

`κ(a, δ, N, r) = N` (full rank needed) for all sufficiently large `a` with fixed `N, δ`.

**Proof sketch.** As `a → ∞`, the form `Q_W^a` becomes increasingly dominated by the
high-frequency components of `L²(−a, a)`. The matrix `M_{a,N}` (in the fixed Legendre
ONB) spreads the minimum eigenspace across all `N` coordinates. A rank-`r < N` Schur
certificate corresponds to a partial pivoting that leaves a positive residual; but the
minimum eigenvector has nontrivial projection on every coordinate (generically), so the
residual after `r` pivots still has a direction with eigenvalue `< δ`.

**Gap.** This sketch requires:
(a) A quantitative lower bound on the "spread" of the minimum eigenvector of `M_{a,N}`
    as `a → ∞`, i.e., `|〈v_min, e_j〉|² ≥ c/N` for all `j` for some `c > 0`.
(b) A Schur-complement argument that partial pivoting cannot avoid this direction.

Both are plausible but not yet proved. This is the OPEN step.

---

## §4. Representation-invariance check

**Before any `−c_a` use is valid:**

The program (CLAUDE.md §"Representation-invariance discipline") identifies the key issue:
a scalar shift `−c_a I` in an unnormalized Schur decomposition can read as a negative shift
while being the positive leading term `log(1/a)` of `λ(a)` in the invariant.

For Theorem F, the quantity `κ(a, δ, N, r)` is defined relative to the Galerkin matrix
`M_{a,N}` in the ONB, and the positivity target is `M_{a,N} − δ I ≽ 0`. This is an
invariant statement (it depends on `δ` and the eigenvalues of `M_{a,N}`, not the basis).

Any argument that uses `M_{a,N} = A + c_a I − (c_a − δ)I + …` as a Schur decomposition
step must verify that `c_a` is the same constant appearing in `λ(a)`, not a
representation artifact of an unnormalized `Q_W^a` evaluation. See statement.md §2 for
the five conditions.

---

## §5. Consistency with `λ(a)`

Since `λ(a) = log(1/a) + μ₁ − log(2π) + ψ(2) − 1 + O(a)` is positive for small `a`:
- For small `a` and `δ < λ(a)`, the certificate complexity is `κ = 1` (full `N×N` block
  works, as `M_{a,N} ≽ δ I` is witnessed by the trivial rank-1 block `B₁ = M_{a,N} − δ I`).
- The interesting regime is large `a` (where `λ(a) → −∞`) or the limit as `N → ∞` for
  the Galerkin approximation, where `λ₁(a,N) → λ(a)` and large-N effects appear.

---

## §6. Status table

| Step | Status |
|---|---|
| Representation-invariance gate (§4) | CONDITIONS STATED — must be verified for any specific `c_a` use |
| Non-vacuity gate (statement.md §3) | OPEN — no specific example confirmed |
| Certificate structure (§2) | PROOF-DRAFT ✓ |
| Lower bound argument (§3) | PROOF-DRAFT (conditional — OPEN: eigenvector spread + Schur residual bound) |
| Consistency with `λ(a)` (§5) | PROOF-DRAFT ✓ (small-a regime clear) |
| No `−c_a I` overclaim | VERIFIED — no universal claim made; `c_a` use is frozen-system diagnostic only |
