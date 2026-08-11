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
| OB-11 | `OB-11-E-prime-pos-convergence-identification.md` | E' §5 | E'-pos: Montel-on-Ω convergence + identification G=W | RESOLVED — integrated 2026-08-11 |
| OB-12 | `OB-12-F-complexity-measure-welldefined.md` | F | Is the Schur-certificate complexity κ well-defined / non-collapsing? | RESOLVED — integrated 2026-08-11 |
| OB-13 | `OB-13-B2-independent-exact-reconstruction.md` | B2 | Independent exact-rational reconstruction of the collision | RESOLVED — integrated 2026-08-11 |
| OB-14 | `OB-14-E-pos-uniform-order-transfer.md` | E §4 | E-pos: is uniform Nevanlinna bound (H-order) necessary+sufficient for order transfer? | OPEN — send for review |
| OB-15 | `OB-15-D-leading-log-mellin.md` | D §4 | Leading heat-trace singularity of positive elliptic ΨDO is pure power (Mellin/no-log) | RESOLVED — integrated 2026-08-11 |
| OB-16 | `OB-16-Dprime-escape-class-weyl-law.md` | D' §6 | \|ξ\|/log\|ξ\| escape class: T·logT counting law, outside 𝒞_ell; Hilbert–Pólya frontier | RESOLVED — integrated 2026-08-11 |

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

## Difficulty / outcomes (OB-11..OB-13, all resolved 2026-08-11)

- **OB-11 (E'-pos convergence + identification):** REFUTED as stated. Two independent
  counterexamples: the growth gap (`F_n ≡ W·e^{z²−w₀²}` — a constant sequence meeting all
  hypotheses whose limit ≠ W, with `T(r,H) ≍ r²`), and the pole-cancellation gap (a
  rational-multiplier family that cancels a target pole while satisfying the original
  (PL)/(ZT)). Referee supplied a corrected theorem adding (ZT_ℂ) full-plane tail
  no-intrusion, (PL⁺) local pole matching without cancellation, and (UG) uniform
  Nevanlinna bound, with a complete §6 proof (Montel not Marty; contour/residue pole
  recovery; Ahlfors–Shimizu order transfer). Integrated into E-prime-meromorphic §5.

- **OB-12 (F complexity measure):** REFUTED — the most consequential outcome. Every
  well-defined Schur/congruence measure collapses (Model 1: {1,+∞}; Model 2 full-block:
  1; scalar: N; cap b: ⌈N/b⌉), and the orthogonal-invariance obstruction shows no
  invariant measure can detect eigenvector delocalization (it factors through the
  eigenvalue multiset). Explicit isospectral witness + a factor-width counterexample
  (`I−α N^{-1}𝟙𝟙^T` has flat min-eigenvector, factor width 2). **Theorem F is downgraded
  from a complexity barrier to a spectral-margin statement** (`M ≽ δI ⟺ λ_min ≥ δ`) and
  retired from Paper D. Integrated into F-schur-complexity §0.

- **OB-13 (B2 independent exact reconstruction):** CONFIRMED. Full m=2 rational table
  reproduced from φ_j in an independent implementation (Python stdlib `fractions`,
  SHA-256-pinned source, direct-φ and Chebyshev routes agree entry-by-entry); independent
  m=3 instance exact zero; mutation guard breaks it. **Fills the previously-empty
  INDEPENDENT-CHECKER computational axis for the B2 finite certificate.** Two definitions
  (global `O_j`, predicate `P`) made explicit. Validates only the finite identity, not any
  analytic statement. Integrated into B2-exact-collision (computational status upgraded).

## Open tasks OB-14..OB-16 (drafted 2026-08-11; lint-checked against PROMPT_LINT.md)

All three passed `outsource/PROMPT_LINT.md` before shipping (self-containment grep clean;
non-circularity stated; anchors script-verified and labeled "sanity only"; verdict space
includes INCONCLUSIVE + localization). Load-bearing anchors verified by script.

- **OB-14 (E-pos uniform order transfer):** the entire-target analogue of the OB-11
  finding. Claim A: `F_N ≡ Ξ·e^{z²−z₀²}` (constant sequence) is locally uniformly bounded,
  same divisor, `F_N(z₀)=Ξ(z₀)`, but order 2 ≠ Ξ — so (H-bound) alone cannot identify the
  limit. Claim B: a **uniform** Nevanlinna bound (H-order) closes it. Claim C: is (H-order)
  necessary? Surfaced by the PROMPT_LINT re-scan (L14) that already fixed E-compactness §4.

- **OB-15 (D leading-log Mellin):** verifies Theorem D's load-bearing citation (currently
  "modulo Grubb–Seeley/Lesch reference"). A positive classical elliptic ΨDO has pure-power
  leading heat-trace singularity `t^{-d/m}` (simple pole of `Γζ_H` at `d/m>0`, no double
  pole → no log), incompatible with `Z_ζ ~ (1/2π)log(1/t)/t`. Explicit scope caveat
  (L17): BGV/Gilkey cover only differential/Laplace-type; general ΨDO needs
  Seeley/Grubb–Seeley/Lesch.

- **OB-16 (D' escape-class Weyl law):** exploratory (INCONCLUSIVE is the expected outcome
  for its Claim D). Verifies the `|ξ|/log|ξ|` symbol gives `T·log T` counting (matching the
  RvM shape up to constant), leading heat-trace `t^{-1}log(1/t)`, and lies outside
  𝒞_ell/𝒞_logpoly — establishing the escape class is real — then honestly localizes the
  Hilbert–Pólya realization as open. Does NOT attempt RH or a Hilbert–Pólya construction.

## Resolved OB-15 / OB-16 outcomes (integrated 2026-08-11)

- **OB-15 (D leading-log Mellin):** REFUTED literally / CONFIRMED with ellipticity. The
  outsource task's restatement of `𝒞_ell` dropped "elliptic" (the theorem file
  `D-spectral-asymptotic/statement.md` keeps it, so the theorem itself is fine). Torus
  counterexample `1+D_x²+D_y⁴` (non-elliptic) gives exponent 3/4 ≠ d/m=1/2. Three
  substantive corrections integrated into D proof.md §4: (a) `ζ_H` NOT regular at all
  negative integers — `Res_{s=−k}=m⁻¹Wres(H^k)`, only s=0 regular, subleading `t^k log t`
  possible for k≥1 (witness `(1+D_x²)^{1/2}` on S¹, Wres=1); (b) `a_0=Γ(d/m)·Res`, not
  `a_0·m/Γ(d/m)`; (c) no-log needs BOTH Lesch simple-pole AND Γ regular at d/m>0. Citation
  pinned: Lesch 1999 Thm 3.7 + (3.18)–(3.22), extending Grubb–Seeley 1995 Thm 2.7; BGV/Gilkey
  (differential/Laplace-type only) explicitly NOT relied upon (L17).

- **OB-16 (D' escape class):** REFINED/PARTIAL. Claims A/B/C confirmed after moving the model
  to `S¹`/`ℓ²(ℕ)` (on `L²(ℝ)` the multiplier has continuous spectrum, not trace class — L-fix).
  Symbol `h_0 ∈ S¹_{1,0}` (Hörmander), precisely log-weighted `S^{1,-1}` — NOT "outside all
  calculi" as drafted. **Claim D: the exact `2πn/log(n+e)` model is REFUTED** (not merely
  open) — its normalized count differs from `N_ζ` by `≍ T log log T`. Only the broader
  Lambert-`W`-corrected `|ξ|/log|ξ|` class stays open (it matches the two-term smooth law;
  zero-independent spectral realization unknown). Integrated into D-prime-logpoly §4–§7.

## What a returned verification should contain

- Statement: CONFIRMED, PARTIAL, or REFUTED for each numbered step.
- For PARTIAL or REFUTED: explicit gap description or counterexample.
- Any proof corrections needed.
- Citation verification for theorem numbers (especially OB-01).
