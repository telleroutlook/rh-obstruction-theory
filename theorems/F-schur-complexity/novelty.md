# Novelty Assessment — Theorem F (F-schur-complexity)

## Prior art

### Proof complexity lower bounds for positivity certificates
- **Lovász–Schrijver / Sherali–Adams hierarchies:** lower bounds for LP/SDP relaxations
  of combinatorial problems. These apply to very different classes (finite optimization);
  the Weil quadratic form is an operator on an infinite-dimensional Hilbert space.
- **SOS-degree lower bounds (Grigoriev–Vorobjov 2001; Schoenebeck 2008):** lower bounds
  for the SOS degree needed to certify a polynomial is non-negative. Related in spirit but
  for polynomial certificates, not Galerkin-Schur certificates for the Weil form.
- **Endres–Steiner spectral theory:** (see Theorem D novelty assessment) addresses the
  spectrum of the Laplace operator, not certificate complexity for the Weil form.

### Weil-criterion computations
- **Li criterion computations** (Li, Voros, Bombieri-Lagarias): compute finitely many
  Li coefficients to check positivity. These are oracle computations, not certificate
  complexity lower bounds.
- **Keiper-Li coefficients (numerical):** discovery-tier computations; no certificate
  complexity argument.

## Novelty assessment: THIN

The specific claim — a lower bound on the Schur/pivot rank needed to certify `M_{a,N} ≽ δ I`
in the frozen system `P_{r,N}` — appears to have no direct prior art.

**However**, the novelty gate is NOT YET CLEARED because:
1. The proof has an OPEN step (eigenvector-spread + Schur-residual bound).
2. The non-vacuity gate is OPEN (no confirmed example in `P_{r,N}`).
3. Until both gates close, the theorem statement cannot be frozen, and the novelty
   comparison is provisional.

**Candidate novelty claim (conditional):** The first lower bound on the Galerkin-Schur
certificate complexity for the localized Weil quadratic form, expressed in terms of the
representation-invariant margin `λ(a)`.

## What the novelty does NOT claim
- Not a new construction of the Weil form (Suzuki 2026 handles that).
- Not a new spectral asymptotic (that is Theorem D's territory).
- Not a new example of a Helson function with prescribed zeros (Theorem C's territory).

## Gate status
- Novelty gate: OPEN  
- Paper D (conditional) — only if both gates close and novelty claim is verified.
