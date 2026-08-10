# Limitations — Theorem F (F-schur-complexity)

## What Theorem F does NOT say

### 1. Not a barrier for arbitrary proof methods
Theorem F applies only to the frozen system `P_{r,N}` with rank bound `r`.  
Methods outside this system — unbounded-rank Schur decompositions, analytic spectral
theory of the Friedrichs extension `A_a`, or non-Galerkin approaches — are entirely
unconstrained.

### 2. Not a claim that `λ(a) ≤ 0` or `Q_W^a` is indefinite
The certificate complexity growing does NOT imply that the Weil form is indefinite.
In fact, for small `a`, `λ(a) > 0` (Suzuki Thm 1.4), so rank-1 certificates exist
trivially. The lower bound regime is large `a` or large `N`, not small `a`.

### 3. Not an RH implication in either direction
The obstruction is to a restricted proof strategy, not to the truth of RH.
RH is `[OUT]` — neither asserted nor denied.

### 4. No universal `−c_a I` claim
A scalar shift `−c_a I` appearing in an unnormalized Schur decomposition is a
representation artifact (CLAUDE.md / REFERENCE_BASELINE §4). Any `−c_a I` use in
this theorem is a frozen-system diagnostic only, not a universal claim.  
**In particular:** the negative Schur shift `−c_L` observed in the LEGACY computations
is the same scale as the positive leading term `log(1/a)` of `λ(a)` in the invariant;
they are consistent, not contradictory.

### 5. Non-vacuity gate OPEN
If no serious published construction lies in `P_{r,N}` for the stated parameters,
the theorem is vacuous for those parameters. Gate status: OPEN (statement.md §3).

### 6. No fixed-parameter conclusion
A lower bound at a single fixed `(a₀, δ₀, N₀, r₀)` is a case study, not a theorem.
Theorem F requires a growing lower bound `r₀(a) → ∞` (or `r₀(N) → ∞`).
Fixed parameters alone fall under CLAUDE.md §3.3 non-success criterion 2.

### 7. No margin-tending-to-zero as a barrier
If the argument only shows `λ₁(a,N) → 0` (or `λ(a) → −∞` as `a → ∞`), that is
also explicitly NOT a barrier (program §3.3 criterion 3). Theorem F requires a
structural argument about the certificate, not just a margin argument.
