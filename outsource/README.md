# outsource/ — self-contained proof-verification requests

Each file here is a standalone mathematical problem extracted from this RH Obstruction
Theory repository. A reviewer needs **nothing else from this repo** to evaluate the
problem.

## Format contract (same as sibling repo `riemann-arithmetic-spectral/outsource/`)

- Self-contained: all definitions, claims, and proof strategies are in the file.
- Falsifiable: if a step is wrong, the reviewer should return an explicit counterexample
  or gap description, not just "cannot prove."
- No RH circularity: no problem assumes RH or uses Riemann zero numerical tables as
  analytic input (numerical anchors for sanity checks are allowed in Step 4 type
  quantitative questions, labeled as such).

## Status board

| # | File | Theorem | Content | Status |
|---|---|---|---|---|
| OB-01 | `OB-01-D-heat-trace-log-singularity.md` | D | BGV/Gilkey no-log citation + log-poly exception | RESOLVED — integrated 2026-08-11 |
| OB-02 | `OB-02-B2-integer-collision.md` | B2 | Vandermonde rank + integer scaling construction | RESOLVED — integrated 2026-08-11 |
| OB-03 | `OB-03-E-tail-estimate.md` | E §3 | Hadamard growth + Vandermonde IFT non-uniqueness | RESOLVED — integrated 2026-08-11 |
| OB-04 | `OB-04-G-prop-G3-adversary.md` | G Prop. G.3 | `𝒵_smooth` adversary, O_θ indistinguishability | RESOLVED — integrated 2026-08-11 |
| OB-05 | `OB-05-E-pos-identification.md` | E §4 | Evenness pins G = Ξ (Hadamard + Hurwitz) | OPEN — send for review |
| OB-06 | `OB-06-E-prime-meromorphic-uniqueness.md` | E' | Meromorphic Hadamard uniqueness + Marty theorem | OPEN — send for review |
| OB-07 | `OB-07-B2-ambient-class-counting-law.md` | B2 / Paper A | Ambient class 𝔛_sym: counting-law requirement? | OPEN — send for review |
| OB-08 | `OB-08-G-factorization-condition.md` | G | Factorization condition (2.7) for 𝔐_FC | OPEN — send for review |

## Difficulty

- **OB-01–04:** RESOLVED (referee reports integrated 2026-08-11).

- **OB-05:** Complex analysis (Hadamard factorization for even entire functions,
  Hurwitz theorem for zero convergence). **Low–medium difficulty.** Claim A (evenness
  pins G=Ξ) is elementary; Claim B (Hurwitz zero-set convergence) requires careful
  attention to hypotheses.

- **OB-06:** Complex analysis (meromorphic Hadamard uniqueness, normal families).
  **Medium difficulty.** Three separate claims: meromorphic factorization citation,
  Marty vs Montel decision, and simplicity-of-zeros scope.

- **OB-07:** Analytic number theory / design question (ambient class definition).
  **Low–medium difficulty.** Primarily a conceptual question: does the ambient class
  𝔛_sym need the Riemann–von Mangoldt counting law for the obstruction to be
  non-trivial? Requires checking whether finite multisets make the theorem vacuous.

- **OB-08:** Operator theory / spectral theory (Fredholm determinants, method class
  verification). **Medium difficulty.** Requires understanding of Fredholm determinants
  and the factorization condition; the normalization sanity check (numerical anchor) is
  elementary and decisive.

## What a returned verification should contain

- Statement: CONFIRMED, PARTIAL, or REFUTED for each numbered step.
- For PARTIAL or REFUTED: explicit gap description or counterexample.
- Any proof corrections needed.
- Citation verification for theorem numbers (especially OB-01).
