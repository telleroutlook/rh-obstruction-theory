# Witness Directory — Theorem F (F-schur-complexity)

**Status:** EMPTY — no witness data yet.

## What belongs here (when available)

1. **Raw Galerkin matrix data:** exact rational entries of `M_{a,N}` for specific
   `(a, N)` in the Legendre ONB. Must be exact (symbolic/rational), not floating-point.

2. **Eigenvalue certificates:** exact interval-arithmetic certificates of
   `λ_min(M_{a,N})` for specific `(a, N)`, using `python-flint`/Arb with outward rounding.

3. **Schur decomposition data:** for specific `(a, N, r)`, a Schur-pivot sequence
   and the residual matrix, showing rank `r` does/does not certify `M_{a,N} ≽ δ I`.

4. **Eigenvector spread data:** for the lower bound argument, the inner products
   `|〈v_min, e_j〉|²` for all `j`, showing the minimum eigenvector is spread.

## What does NOT belong here

- `discovery/` output files — those are EXPLORATORY tier only.
- Float computations without interval certificates.
- Any file computed from zero ordinates of the Riemann zeta function.

## Gate status

Witness evidence gate: OPEN (no data deposited).  
Per CLAUDE.md: certificates enter only after independent replay.  
Per program §12.2: witness/ must contain raw data, not producer summaries.
