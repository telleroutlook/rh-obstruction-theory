# Theorem F — Lower Bounds for a Restricted Schur-Certificate System

**Mathematical status:** PROOF-DRAFT (conditional on non-vacuity + invariance gates)  
**Computational status:** NONE  
**Theorem ID:** F-schur-complexity  
**Program ref:** §11 (WP-F), §11.F.1–F.4  
**Paper target:** Paper D (exploratory; conditional on both gates)

---

## §1. The frozen certificate proof system `P_{r,N}`

Fix parameters `a > 0`, `N ≥ 1`, `r ≥ 0`.

**Galerkin subspace.** Let `{e₁, …, e_N}` be an orthonormal basis of
`L²(−a, a)` (e.g., normalized Legendre polynomials on `[−a, a]`).

**Gram matrix.** `G_{a,N}` is the `N × N` identity matrix in this ONB
(since the basis is orthonormal): `G_{a,N} = I_N`.

**Weil matrix.** `M_{a,N}` is the `N × N` matrix with entries
`(M_{a,N})_{ij} = Q_W^a(e_i, e_j)` (the localized Weil quadratic form
evaluated at basis pairs).

**Invariant target (program §11.F.1).** For `δ > 0`:
```
M_{a,N} ≽ δ G_{a,N}  ⟺  M_{a,N} − δ I_N ≽ 0   (positive semidefiniteness).
```
This is equivalent to `λ_min(M_{a,N}) ≥ δ`, i.e., the smallest eigenvalue of
the Galerkin matrix is at least `δ`.  Note that as `N → ∞`, `λ_min(M_{a,N}) → λ(a)`
(the representation-invariant margin).

**Allowed operations.** The certificate proof system `P_{r,N}` allows:
- a change of ONB (orthogonal transformation `U ∈ O(N)`) applied to both
  `M_{a,N}` and `G_{a,N}` (congruence: `M ↦ U^T M U`, `G ↦ U^T G U = I`);
- a block decomposition of `M_{a,N}` into at most `r` non-overlapping blocks;
- within each block, a Schur-complement / pivot certificate;
- the maximum residual rank is `r` (number of pivot steps or Schur blocks).

**Certificate complexity `κ(a, δ, N, r)`.** The minimum `r` such that a
`P_{r,N}`-certificate witnesses `M_{a,N} ≽ δ I` (if one exists); or `+∞`
if no such certificate exists at rank `r`.

**Theorem F target.** A lower bound on `κ(a, δ, N, r)` as `a → ∞` with `N, δ`
fixed, or as `N → ∞` with `a` fixed — showing that the certificate system
requires growing complexity.

---

## §2. Representation-invariance gate (mandatory — program §11.F.3)

Any use of a decomposition `M = A − c_a I + B` (where `−c_a I` is a scalar
shift) as a certificate step must satisfy ALL FIVE conditions of §11.F.3:

1. **Exact identity in `Q_W^a` normalization:** the decomposition holds exactly
   in the standard `L²` inner product, not in a rescaled basis.

2. **Invariance under congruence:** if `M' = U^T M U` for `U ∈ O(N)`, the
   term `−c_a I` must still appear with the same coefficient (scalar shifts
   are congruence-invariant iff they are multiples of the identity).

3. **Upper bound on the compensating term:** `‖A + B − c_a I‖ ≤ C` in the
   standard norm, with `C` independent of the choice of `U`.

4. **Stronger than "margin → 0":** the claim must be that `κ(a, δ, N, r)` is
   bounded below by a specific function `f(a, δ, N, r) → ∞`, not merely that
   the margin tends to zero.

5. **Consistency with `λ(a)`:** the lower bound must be compatible with
   `λ(a) = log(1/a) + μ₁ − log(2π) + ψ(2) − 1 + O(a)` (Suzuki Thm 1.4).
   In particular, a `−c_a I` term claiming to dominate `λ(a)` is a
   representation artifact (REFERENCE_BASELINE §4) and must be resolved.

**Until these five conditions are verified, any `−c_a I` argument is a
frozen-system diagnostic only and must not be promoted to a universal barrier.**

---

## §3. Non-vacuity gate (mandatory — program §14)

The theorem is vacuous if `P_{r,N}` contains no natural constructions.

**Non-vacuity requirement.** At least one serious published construction must
lie in `P_{r,N}` for the stated `(a, N, r)`.  Candidates:

1. **Weil-window computations (LEGACY FP-0.35, LEGACY-SECOND-WINDOW).**
   These are Galerkin approximations of `Q_W^a` at small `a`.  However, they
   are LEGACY PENDING Gate A (CLAIM_LEDGER.yaml): the Schur residuals are
   basis-dependent and must be reconciled with `λ(a)` before use.

2. **Suzuki `A_a` finite-dimensional Galerkin approximation.**  Suzuki constructs
   `B_a = D_a^* G_a D_a` (Friedrichs extension); its Galerkin truncation at rank
   `N` gives `M_{a,N}`.  This is a natural member of `P_{r,N}` for large `N`.

3. **SOS / Positivstellensatz certificates for the Weil polynomial.**  A standard
   SOS decomposition of a truncated Weil polynomial is a rank-`r` certificate for
   a specific `r`.

**Gate status:** OPEN.  The non-vacuity must be confirmed with a specific
published example before Theorem F proceeds past SKETCH.

---

## §4. Theorem F (lower bound — conditional)

**Theorem F (conditional on gates).** Under the frozen system `P_{r,N}` (with
the allowed operations of §1) and given:

- (H-inv) the representation-invariance conditions of §2 hold;
- (H-nv) there exists a serious published construction in `P_{r,N}` (§3);

then for sufficiently large `a` (or `N`) and fixed `r`, there exists a vector
`v ∈ ℝ^N` such that:

```
v^T M_{a,N} v / v^T G_{a,N} v  ≥  δ  but  v is not certifiable by any
P_{r,N}-certificate of rank ≤ r₀(a),
```

where `r₀(a) → ∞` as `a → ∞`.

**Consequence:** The certificate complexity `κ(a, δ, N, r₀(a)) > r₀(a)` for
the stated system — the Schur/pivot rank must grow.

**Status:** PROOF-DRAFT (both gates open).

---

## §5. Escape route

Theorem F does **not** say:
- `Q_W^a < 0` or `λ(a) < 0` (the invariant margin may still be positive).
- Other proof methods (not using `P_{r,N}`) are limited.
- The full Weil criterion (unbounded rank) is limited.

The escape from Theorem F is: use a proof method outside `P_{r,N}`, e.g.,
- unbounded rank (let `r → ∞` with `a`);
- a different block structure not in `P_{r,N}`;
- a non-Galerkin argument (analytic, spectral theory of `A_a` directly).

---

## §6. Gate A status

- The representation-invariance gate (§2): conditions written; must be verified
  for any specific use of `−c_a I`.
- The non-vacuity gate (§3): OPEN — need a specific example.
- LEGACY PENDING items (FP-0.35, SECOND-WINDOW): cannot be used until Gate A
  re-inspection under the `a`/`Q_W^a`/`λ(a)` convention.
