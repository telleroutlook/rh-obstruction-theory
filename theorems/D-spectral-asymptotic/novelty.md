# Novelty — Theorem D (D-spectral-asymptotic)

**Theorem ID:** D-spectral-asymptotic  
**Program ref:** §9.D.5, LITERATURE_MATRIX.md §Paper B

---

## Prior art landscape

### Endres–Steiner (2010), J. Phys. A 43, 095204

Proves that no compact quantum graph Hamiltonian with local energy-independent
vertex conditions can have spectrum `{γ_n}`, by comparing `N_H(T) ~ (L/π) T`
(linear) with `N_ζ(T) ~ T log T / 2π`.  This is exactly the Weyl-mismatch
argument for compact quantum graphs.

**Delta from Theorem D (main):** Theorem D covers the broader `𝒞_ell` class
(all compact elliptic operators of order `m` on compact `d`-manifolds) and the
extensions including compact quantum graphs as a special case.  The argument is
the same, the class is broader.

### Program §9.D.5 judgment

> "The raw Weyl mismatch is close to a standard corollary.  Before claiming a
> new paper, complete a theorem-by-theorem prior-art audit.  A paper is justified
> only if it supplies a materially broader, sharply defined invariant class or
> an exact determinant obstruction not already in the literature."

## New content assessment

| Aspect | Novel? | Notes |
|---|---|---|
| Weyl leading term for C_ell | NO | Standard corollary of classical Weyl theorem |
| Extensions: sums, polynomials, perturbations | THIN | Routine from Courant-Weyl |
| Compact quantum graphs | NO | Endres-Steiner already proved this |
| Heat-trace log singularity (proof.md §4) | POSSIBLY YES | Seeley-DeWitt no-log vs. Z_zeta log term — needs quantitative statement |
| Spectral zeta pole obstruction (proof.md §5) | POSSIBLY YES | Pole structure of Z_H(s) vs. Riemann zeta; need careful formulation |

## Verdict and publication strategy

**THIN at the Weyl-leading-term level.**  Paper B is justified only if:

1. The heat-trace `log(1/t)` obstruction (proof.md §4) is stated quantitatively
   and covers a broader class than what follows from Endres–Steiner + standard Weyl.
2. OR the spectral zeta pole obstruction (proof.md §5) is completed and shown
   to cover classes not already in the literature.

**Current action:**
- Complete proof.md §4 (heat-trace log argument) and check whether it is new.
- If YES → Paper B proceeds as a short note with the heat-trace invariant as
  the primary contribution.
- If NO → Theorem D is published as a supporting reference note or an appendix
  of Paper A/C.

**The novelty gate (program §9.D.5) is NOT yet cleared.**
