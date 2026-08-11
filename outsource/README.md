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
| OB-01 | `OB-01-D-heat-trace-log-singularity.md` | D | BGV/Gilkey no-log citation + log-poly exception | OPEN — send for review |
| OB-02 | `OB-02-B2-integer-collision.md` | B2 | Vandermonde rank + integer scaling construction | OPEN — send for review |
| OB-03 | `OB-03-E-tail-estimate.md` | E §3 | Hadamard growth + Vandermonde IFT non-uniqueness | OPEN — send for review |
| OB-04 | `OB-04-G-prop-G3-adversary.md` | G Prop. G.3 | `𝒵_smooth` adversary, O_θ indistinguishability | OPEN — send for review |

## Difficulty

- **OB-01:** Pure spectral theory / PDE citation check. **Low difficulty.** The result
  is classical; what is needed is exact theorem numbers from BGV and Gilkey, and
  confirmation of the log-polyhomogeneous exception. A PDE / heat-kernel specialist can
  answer in one pass.

- **OB-02:** Algebraic combinatorics (Vandermonde + integer programming). **Low–medium
  difficulty.** All steps are explicit and elementary; the hardest part is verifying that
  the scaling trick produces a valid multiset (Step 4).

- **OB-03:** Classical complex analysis (Hadamard factorization + IFT). **Medium
  difficulty.** The Vandermonde Jacobian structure requires careful verification, but
  involves no analytic number theory.

- **OB-04:** Analytic number theory. **Medium difficulty.** Requires knowledge of S(T),
  Backlund's theorem, and the Hadamard factorization for Ξ. The quantitative Step 4 is
  optional (discovery-tier) and can be deferred.

## What a returned verification should contain

- Statement: CONFIRMED, PARTIAL, or REFUTED for each numbered step.
- For PARTIAL or REFUTED: explicit gap description or counterexample.
- Any proof corrections needed.
- Citation verification for theorem numbers (especially OB-01).
