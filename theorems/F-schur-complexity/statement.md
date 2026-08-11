# Theorem F — Lower Bounds for a Restricted Schur-Certificate System

**Mathematical status:** REFUTED as a complexity lower bound (OB-12 external review
2026-08-11). Downgraded to a spectral-margin statement. See §0 below.  
**Computational status:** NONE  
**Theorem ID:** F-schur-complexity  
**Program ref:** §11 (WP-F), §11.F.1–F.4  
**Paper target:** NONE — not publishable as a complexity barrier (see §0)

---

## §0. Downgrade notice (OB-12 external review, 2026-08-11)

**The complexity-lower-bound claim of Theorem F is REFUTED.** The proof draft contained
an internal contradiction (a certificate is either cost 1 or cost +∞ under one reading,
yet claimed to be cost N under another), traced to an ill-defined complexity measure.
The external review (OB-12) resolved it decisively:

1. **Model 1** (orthogonal congruence + whole-matrix PSD test): `κ₁(S) = 1` if
   `S ≽ 0`, else `+∞`. Orthogonal congruence preserves the spectrum, so this is a pure
   spectral condition — it cannot grow with the scaling parameter `a`.

2. **Model 2** (Schur elimination, fixed basis): `κ = 1` with a full-block atom, `κ = N`
   with scalar pivots, `κ = ⌈N/b⌉` with a fixed block cap `b`, **on every PD matrix** —
   none varies with `a`. Every admissible pivot succeeds on a PD matrix (Haynsworth
   inertia additivity), so the cost charges only the partition shape, not the matrix.

3. **Orthogonal-invariance obstruction (the core no-go):** any orthogonally invariant
   matrix measure `K_N(U^T S U) = K_N(S)` factors through the **eigenvalue multiset**
   alone (spectral theorem). Delocalization of the minimum eigenvector in a chosen basis
   carries **no eigenvalue information**, so it cannot force any invariant cost to grow.
   Explicit witness (OB-12 Prop. 4.4): an isospectral family `S(a) = V(a) D V(a)^T` with
   `V(a)` rotating the min-eigenvector to the flat vector `N^{-1/2}(1,…,1)` — fully
   delocalized in the limit — on which **every** invariant measure is constant.

4. Even a genuine fixed-basis non-collapsing measure (**factor width**) does not obey the
   proposed bound: `S_α = I − α w w^T` with `w = N^{-1/2}(1,…,1)` has an exactly flat
   minimum eigenvector yet factor width exactly 2 for all `N ≥ 2` (OB-12 §6, eq. 6.2).

**Conclusion.** "Delocalization forces Schur-certificate complexity to grow" is false.
What survives is only the spectral-margin equivalence
```
M ≽ δ I_N  ⟺  λ_min(M) ≥ δ,
```
plus the model-dependent constant-cost formulas above. This is an eigenvalue statement,
NOT a proof-complexity lower bound. Per CLAUDE.md ("a margin → 0 is not a barrier"; "a
representation-dependent margin must not be promoted"), Theorem F **must not be marketed
as a barrier** and is retired from Paper D.

**What a genuine future theorem would require (OB-12 §7, not currently available):**
a semantically fixed representation (forbidding general orthogonal congruence), a
checkable atomic witness with a charged resource (factor width / clique size / fill-in /
bit complexity), and a structural lower bound on *that resource* — not eigenvector
delocalization. Published fixed-basis frameworks exist (factor width: Boman–Chen–Parekh–
Toledo 2005; DSOS/SDSOS: Ahmadi–Majumdar 2019; chordal sparsity: Agler–Helton–McCullough–
Rodman 1988, Fukuda et al. 2001), but none yields the claimed growth from delocalization.

The sections below are retained for the record; §4's "Theorem F (lower bound)" is
**withdrawn** as a complexity claim and reinterpreted as the spectral-margin statement.

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

2. **Suzuki `A_a` Galerkin truncation — EXT-5 audit result (PROOF-DRAFT).**
   Suzuki (arXiv:2606.09096, Thm 1.1, EQ_101/EQ_106) defines `A_a` as the
   Friedrichs extension of `B_a = D*G_a D` on `L²(−a,a)`.  The quadratic form is
   `Q_W^a(v) = ⟨A_a v, v⟩` (REFERENCE_BASELINE §2).  Taking the Galerkin truncation:
   choose `{e₁,…,e_N}` = normalized Legendre polynomials on `(−a,a)` as ONB, then
   `M_{a,N}` = the `N×N` matrix with `(M_{a,N})_{ij} = Q_W^a(e_i, e_j)`.
   This is **exactly the `P_{r,N}` construction** of §1 (same ONB, same Weil form,
   same allowed Schur-block operations).

   **Conclusion (EXT-5a, PROOF-DRAFT):** The Suzuki `A_a` Galerkin truncation is a
   member of `P_{r,N}` for any `N` and for `r` up to `N`. This is a **published,
   source-verified construction** (baseline/suzuki-2606.09096 tarball, Thm 1.1).

   **Non-vacuity gate: CONDITIONALLY PASSED** (pending representation-invariance
   gate — see §2 conditions; both gates must pass together).

3. **SOS / Positivstellensatz certificates for the Weil polynomial.**  A standard
   SOS decomposition of a truncated Weil polynomial is a rank-`r` certificate for
   a specific `r`.  Backup witness if Suzuki Galerkin fails the invariance gate.

**Gate status:** NON-VACUITY GATE CONDITIONALLY PASSED (Suzuki Galerkin truncation
confirmed as P_{r,N} member, PROOF-DRAFT).  Full gate opens when representation-
invariance gate (§2) is also passed.

---

## §4. Theorem F (lower bound — WITHDRAWN; reinterpreted as spectral margin)

**[WITHDRAWN as a complexity lower bound — OB-12 external review 2026-08-11. See §0.]**

The original conditional claim — that a spread minimum eigenvector forces
`κ(a, δ, N, r) > r₀(a) → ∞` — is false: the complexity measure collapses to a
constant (1, N, or ⌈N/b⌉) or to a spectral condition under every well-defined reading,
and no orthogonally invariant measure can detect eigenvector delocalization (§0.3).

**What survives (spectral-margin statement, PROOF-DRAFT ✓).** For the frozen system
`P_{r,N}` with the allowed operations of §1, the certifiability of `M_{a,N} ≽ δ I` is
governed entirely by the least eigenvalue:
```
M_{a,N} ≽ δ I_N   ⟺   λ_min(M_{a,N}) ≥ δ,
```
and, as N → ∞, `λ_min(M_{a,N}) → λ(a)` (the representation-invariant Suzuki margin,
`λ(a) = log(1/a) + μ₁ − log(2π) + ψ(2) − 1 + O(a)` as a → 0⁺). This is an eigenvalue /
margin fact; it is NOT a certificate-complexity lower bound, and it is not a barrier.

**No barrier is claimed.** By CLAUDE.md's one hard boundary and §3.3 of the program,
a margin statement (even one with `λ(a) → −∞` as a grows) locates difficulty but does
not prove impossibility for any method class. Theorem F therefore makes no barrier claim.

**Status:** REFUTED as complexity lower bound; spectral-margin statement retained.

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
