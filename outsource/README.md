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
| OB-05 | `OB-05-E-pos-identification.md` | E §4 | Evenness pins G = Ξ (Hadamard + Hurwitz) | RESOLVED — integrated 2026-08-11 |
| OB-06 | `OB-06-E-prime-meromorphic-uniqueness.md` | E' | Meromorphic Hadamard uniqueness + Marty theorem | RESOLVED — integrated 2026-08-11 |
| OB-07 | `OB-07-B2-ambient-class-counting-law.md` | B2 / Paper A | Ambient class 𝔛_sym: counting-law requirement? | RESOLVED — integrated 2026-08-11 |
| OB-08 | `OB-08-G-factorization-condition.md` | G | Factorization condition (2.7) for 𝔐_FC | RESOLVED — integrated 2026-08-11 |
| OB-09 | `OB-09-E-prime-neg-IFT-odd-meromorphic.md` | E' §4 | IFT for odd meromorphic target: zero-perturbation Jacobian | RESOLVED — integrated 2026-08-11 |
| OB-10 | `OB-10-G-Hurwitz-real-zeros.md` | G §7 | Hurwitz: PSD Fredholm limit has all-real zeros | RESOLVED — integrated 2026-08-11 |
| OB-11 | `OB-11-E-prime-pos-convergence-identification.md` | E' §5 | E'-pos: Montel-on-Ω convergence + identification G=W | OPEN — send for review |
| OB-12 | `OB-12-F-complexity-measure-welldefined.md` | F | Is the Schur-certificate complexity κ well-defined / non-collapsing? | OPEN — send for review |
| OB-13 | `OB-13-B2-independent-exact-reconstruction.md` | B2 | Independent exact-rational reconstruction of the collision | OPEN — send for review |

Notes on the OB-09 / OB-10 outcomes:

- **OB-09:** REFUTED as originally stated (the power-sum matching system Φ_r controls
  the expansion at z=0, not the Taylor jet at a nonzero base point w₀; also: frozen
  first-k terms omitted, wrong tail denominator, and an even leading separation degree
  contradicting F−W odd). The referee supplied a complete corrected construction (§7):
  a **direct w₀-jet IFT system** with an explicit rational Wronskian–Vandermonde
  Jacobian, plus the mandatory non-collision assumption Z(B)∩ℝ={0} and the corrected
  odd leading degree z^{2J+3}. Integrated into E-prime-meromorphic proof.md §3.

- **OB-10:** CONFIRMED. PSD finite-rank Fredholm determinants have real zeros at
  ±λ_j^{-1/2}; the locally uniform limit inherits all-real zeros via Hurwitz's zero-free
  corollary (Conway VII.§2 Cor. 2.6) plus the identity theorem to exclude f≡0. Yields
  Corollary G.5: convergence to Ξ̂ ⟹ RH, so 𝔐_FC membership condition 3 is unverifiable
  without proving RH. Integrated into G-fredholm-certificate proof.md §5b.

## Difficulty (open tasks OB-11..OB-13)

- **OB-11 (E'-pos convergence + identification):** Complex analysis (Montel normal
  families on Ω, Hurwitz zero-transfer, meromorphic extension across poles). **Medium
  difficulty.** The one genuinely nontrivial step is the Nevanlinna-order bound on the
  extended limit (Step 4a); everything else is a careful assembly of standard theorems.
  Allows an honest "hypotheses insufficient for Step 4a + minimal fix" outcome.

- **OB-12 (F complexity measure well-defined):** Linear algebra / proof complexity.
  **Medium difficulty but decisive.** Resolves an internal contradiction in Theorem F's
  proof draft (Passage A says κ∈{1,+∞}; Passage B says κ=N). The task explicitly permits
  a REFUTED outcome: if every orthogonally-invariant Schur/congruence measure collapses
  to a spectral condition, Theorem F is not a genuine complexity lower bound and must be
  downgraded. This is the most consequential of the three.

- **OB-13 (B2 independent exact reconstruction):** Computational verification (exact
  rational arithmetic). **Low difficulty, high value.** Fills the currently-empty
  INDEPENDENT-CHECKER computational axis for the B2 finite certificate. The m=2 anchor
  table and a second m=3 instance were both verified by the producer's own script before
  sending (exact zero residual; mutation guard breaks it); the task is a genuinely
  independent cross-implementation replay.

## What a returned verification should contain

- Statement: CONFIRMED, PARTIAL, or REFUTED for each numbered step.
- For PARTIAL or REFUTED: explicit gap description or counterexample.
- Any proof corrections needed.
- Citation verification for theorem numbers (especially OB-01).
