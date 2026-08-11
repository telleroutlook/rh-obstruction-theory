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

**NOVELTY GATE CLEARED** for Paper B (short note).

The heat-trace `log(1/t)/t` singularity argument (proof.md §4) is:

1. **Strictly stronger than Endres–Steiner:** they prove Weyl mismatch for compact
   quantum graphs (one special case of `𝒞_ell`). The heat-trace argument:
   - applies to the **full `𝒞_ell` class** (all compact elliptic operators, any order/dimension);
   - is a **finer invariant**: `log(1/t)/t` singularity type cannot arise from
     polyhomogeneous Seeley–DeWitt expansion — this excludes all `(d,m)` simultaneously;
   - does NOT follow from Endres–Steiner + standard Weyl by a simple application.

2. **Self-contained computation:** The `Z_ζ(t) ~ log(1/t)/t` lemma follows from
   Abel–Plana / partial summation applied to the Riemann–von Mangoldt formula — no
   explicit formula or zero-sum needed.

**Novelty-gate citation status (RESOLVED by OB-15, 2026-08-11).** The leading-log
obstruction for the **full classical elliptic ΨDO class** is pinned to **Lesch 1999
Theorem 3.7** (Ann. Global Anal. Geom. 17, 151–187) + eqs (3.18)–(3.22) with `A=I`,
extending **Grubb–Seeley 1995 Theorem 2.7**. Scope caveat (PROMPT_LINT L17): **BGV
Thm 2.30** covers only Laplace-type (order-2 differential) operators and **Gilkey Lemma
1.8.2** (NOT "Thm 1.8.1") covers only differential operators — neither suffices for the
general ΨDO claim, and neither is the load-bearing citation. This is a standard result at
the pinned references, not a new mathematical claim; the citation is for Gate A compliance.

**Paper B strategy:** Short note (~10 pages). Primary contribution: the heat-trace
`log` singularity obstruction for the full `𝒞_ell` class. Secondary: Weyl-mismatch
corollary as context. The spectral zeta pole obstruction (proof.md §5) is deferred
to future work.

**Current action: novelty gate CLEARED (pending Seeley–DeWitt cite); proceed with Paper B outline.**
