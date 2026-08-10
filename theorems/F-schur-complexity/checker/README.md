# Checker Directory — Theorem F (F-schur-complexity)

**Status:** EMPTY — no checker implemented yet.

## What belongs here (when available)

A self-contained Python checker (stdlib + `python-flint` for interval arithmetic) that:

1. **Reads** raw witness data from `../witness/`.
2. **Independently computes** `λ_min(M_{a,N})` using interval arithmetic (outward
   rounding), for the exact rational Galerkin matrix entries.
3. **Verifies** the Schur pivot sequence: replay the rank-`r` certificate and confirm
   the residual is positive/indefinite as claimed.
4. **Reports** the eigenvector spread: compute `|〈v_min, e_j〉|²` using certified bounds.

## Implementation requirements

- Type annotations required (per CLAUDE.md).
- No imports from `discovery/`.
- Must be deterministic and offline (no network, no fitted zero tables).
- Must be independently invokable: `python3 theorems/F-schur-complexity/checker/check.py`.
- Must exit 0 on success, nonzero on failure — never self-report PASS via print alone.

## Dependencies

- Python stdlib
- `python-flint` (Arb interval arithmetic) for certified eigenvalue bounds
- `fractions.Fraction` for exact rational matrix entries

## Gate status

Checker implementation: PENDING (non-vacuity gate must close first).  
Per CLAUDE.md: certificates enter only after independent replay from raw data.
