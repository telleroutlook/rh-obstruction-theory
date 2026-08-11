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
| OB-14 | `OB-14-E-pos-uniform-order-transfer.md` | E §4 | E-pos: is uniform Nevanlinna bound (H-order) necessary+sufficient for order transfer? | RESOLVED — integrated 2026-08-11 |
| OB-15 | `OB-15-D-leading-log-mellin.md` | D §4 | Leading heat-trace singularity of positive elliptic ΨDO is pure power (Mellin/no-log) | RESOLVED — integrated 2026-08-11 |
| OB-16 | `OB-16-Dprime-escape-class-weyl-law.md` | D' §6 | \|ξ\|/log\|ξ\| escape class: T·logT counting law, outside 𝒞_ell; Hilbert–Pólya frontier | RESOLVED — integrated 2026-08-11 |
| OB-17 | `OB-17-G-diagonal-fredholm-interval-replay.md` | G | INDEPENDENT-CHECKER: certified interval replay of diagonal Fredholm obstruction (Gram levels d_n, 3-way separation) | RESOLVED — integrated 2026-08-11 (checker deposited) |
| OB-20 | `OB-20-B2-gate-a-review-package.md` | B2 | **GATE-A**: independent inspection of the full analytic assembly (6 links + Q1–Q5 verdict) | RESOLVED — GATE-A PASS, integrated 2026-08-11 |
| OB-21 | `OB-21-B2-certified-checker-request.md` | B2 | Request for an independently-written deposit-ready certified checker (full pipeline C→β→R,n,M→collision) | RESOLVED — CONFIRMED, checker deposited 2026-08-11 |
| OB-22 | `OB-22-G-gate-a-review-package.md` | G | **GATE-A**: independent review of the diagonal G-info obstruction (Links A–E + Q1–Q5; G-hard explicitly OUT of scope) | RESOLVED — GATE-A CONDITIONAL, 7 mods integrated 2026-08-11 |
| OB-23 | `OB-23-B1-gate-a-review-package.md` | B1 | **GATE-A**: independent review of the finite-inequality non-discrimination (Links A–D + Q1–Q5; "no uniform margin", not exact collision) | RESOLVED — GATE-A CONDITIONAL, Σ′ convention + anchors corrected 2026-08-11 |
| OB-24 | `OB-24-B1-corrected-checker-request.md` | B1 | Corrected R-atom certified checker (δ_1(1)=608/425, T*=90, 2j²) superseding OB-18's doubled convention | RESOLVED — CONFIRMED (Gate-A CONDITIONAL), checker deposited 2026-08-11 |
| OB-25 | `OB-25-D-gate-a-review-package.md` | D | **GATE-A**: independent review of the spectral-asymptotic exclusion (Links A–E + Q1–Q6; heat-trace leading-log; novelty vs Endres–Steiner) | RESOLVED — GATE-A CONDITIONAL→PASS, 8 mods integrated 2026-08-11 (D → INDEPENDENTLY-CHECKED, scope-extension positioning) |
| OB-26 | `OB-26-C-gate-a-review-package.md` | C | **GATE-A**: independent review of the finite-Euler-factor non-forcing theorem (Links A–D + Q1–Q7; Andersson Thm 5 import + zero-free finite-factor ratio; crux Q5 = corollary vs standalone; Q3 = one-sided target framing) | RESOLVED — GATE-A CONDITIONAL→PASS, mod1–mod6 integrated 2026-08-11 (C → INDEPENDENTLY-CHECKED, one-sided corollary of Andersson Thm 5) |
| OB-29 | `OB-29-E-gate-a-review-package.md` | E | **GATE-A**: independent review of the compactness (finite-evidence) theorem (Links A–D + Q1–Q7; E-neg per-`N` non-identifiability via fixed-`N` IFT + E-pos sufficiency package; Ξ-not-ξ̂ normalization; per-`N`-not-sequence framing; H-uorder/H-div honesty) | OPEN — send for review |
| OB-30 | `OB-30-Eprime-gate-a-review-package.md` | E' | **GATE-A**: independent review of the meromorphic (Suzuki-target) compactness theorem (Links A–D + Q1–Q7; E'-neg per-`(k,J)` non-identifiability via `w₀`-jet IFT + E'-pos corrected sufficiency; W-odd parity + γ_n-are-zeros; Montel-not-Marty; T(r,W)≍r log r conventional-order envelope) | OPEN — send for review |
| OB-31 | `OB-31-Dprime-gate-a-review-package.md` | D' | **GATE-A**: independent review of the log-polyhomogeneous escape-route audit (Claims A–E + Q1–Q7; 𝒞_logpoly is covered by D not an escape; escape class is log-weighted S^{1,-1}; exact 2πn/log(n+e) refuted by T log log T; open HP frontier honesty) | OPEN — send for review |
| OB-32 | `OB-32-H-gate-a-review-package.md` | H | **GATE-A**: independent review of the information-obstruction partial order (Claims 1–4 + Q1–Q6; partial-order-not-chain OB-27; incomparability H'(i) O_finite ⋈ O_theta with 2 witnesses; coarsening inherits B2/G; L23 fixed-sequence subtlety) | OPEN — send for review |
| OB-18 | `OB-18-B1-approximate-collision-exact-replay.md` | B1 | INDEPENDENT-CHECKER: exact-rational replay of approximate-collision decay δ_j(T)→0 | RESOLVED — integrated 2026-08-11 |
| OB-19 | `OB-19-D-zeta-heat-trace-leading-coefficient-replay.md` | D | INDEPENDENT-CHECKER: replay of Z_ζ leading singularity coefficient 1/2π (Laplace identities) | RESOLVED — integrated 2026-08-11 |

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

## Resolved OB-14 outcome (integrated 2026-08-11)

- **OB-14 (E-pos uniform order transfer):** CONFIRMED after two corrections; necessity of
  (H-order) REFUTED. Claim A (witness `F_N ≡ Ξ·e^{z²−z₀²}` has order exactly 2,
  `T(r,e^{z²−z₀²})=r²/π+O(1)`) confirmed. Claim B: the literal one-sided (H-tail) is
  vacuous (constant `F_N ≡ Ξ(z₀)` satisfies it) → replaced by multiplicity-complete
  divisor convergence (H-div, disk/Rouché form). Claim C decided negatively: even Taylor
  polynomials of the order-2 `G` (each order 0) converge to `G` with divisor → Ξ, so a
  per-N order/type bound does NOT transfer. **Key correction (PROMPT_LINT L1 error I
  re-introduced):** my (H-order) `T(r,F_N)≤Cr+C₀` is a *finite-type* bound, incompatible
  with the real Ξ (infinite exponential type) — it makes the theorem vacuous. Fixed to
  **(H-uorder)** `T(r,F_N)≤C_ε r^{1+ε}+C_{0,ε}` (uniform *conventional* order ≤ 1), which
  admits Ξ. (H-order) sufficient but NOT necessary (`F_N=Ξ·e^{(z²−z₀²)/N}` → Ξ with each
  F_N order 2). Integrated into E-compactness proof.md §4 + statement.md table. PROMPT_LINT
  L14 refined (envelope-type caveat) and **L20 added** (Fourier multiplier on ℝ has
  continuous spectrum — from the OB-16 model error); re-scan clean.

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

## Open computational-replay batch OB-17..OB-19 (drafted 2026-08-11; lint-checked)

Goal: move more theorems' finite content to the **INDEPENDENT-CHECKER** computational
axis (as OB-13 did for B2 — currently the only theorem there). Each is a verification/
program task with script-verified exact/certified anchors, an independent-reconstruction
requirement, and an adversarial-mutation guard (V5). All pass PROMPT_LINT (self-contained;
non-circular; anchors labeled "sanity only, this IS the reconstruction target";
DISCREPANCY/INCONCLUSIVE verdicts admitted; exact/interval/≥25-digit required, floats-only
rejected).

- **OB-17 (G diagonal Fredholm):** certified **interval** replay (Arb/`python-flint` or
  rigorous `mpmath`). Enclose Gram levels `d_n` from `θ(d_n)=(n−1)π`, propagate to
  `κ_n=1/(1/4+d_n²)` and determinant zeros `√(1/4+d_n²)`, and certify the three-way
  disjoint separation `γ_n < d_n < √(1/4+d_n²)` — the finite core of `G_d ≠ Ξ̂`. `d_n`
  transcendental ⇒ interval arithmetic mandatory. Anchors verified by script: `d_1 ≈
  17.8456`, `√(1/4+d_1²) ≈ 17.8526`, `γ_1 ≈ 14.1347`.

- **OB-18 (B1 approximate collision):** exact-**rational** replay of the quartet-decay
  certificate `δ_j(T) = 4Re[φ_j(σ_0+iT)+φ_j(1−σ_0+iT)] → 0`. Anchors verified: `δ_1(1) =
  1216/425`, decay constant `δ_1(T)·T² → 4`. Moves B1 computational axis NONE →
  INDEPENDENT-CHECKER (analogue of OB-13 for B2).

- **OB-19 (D Z_ζ leading singularity):** symbolic/≥25-digit replay of the Riemann-side
  leading coefficient. Exact closed form verified to 25 digits: `Z_ζ,main(t) =
  (1/2πt)(log(1/t) − γ_E − log2π)`, leading coeff exactly `1/2π`; explains OB-15's
  slow-ratio remark (subleading constant only log-suppressed). Uses only RvM counting, no
  zero locations.

## Resolved OB-18 / OB-19 outcomes (integrated 2026-08-11)

- **OB-18 (B1 exact-rational replay):** CONFIRMED after two repairs. (V4) membership needs
  the added assumption `𝒵_+ ∈ 𝔛_sym` (not just `P(𝒵_+)=1` — that alone doesn't give
  conjugation/`1−ρ` closure). B1's precise meaning is **"no positive uniform separation
  margin," NOT "no exact discriminator"** (`δ_1(T)>0` for every finite T, so B1 is not an
  exact collision — that's B2). Bonus exact results: joint threshold `T*=127` (I'd
  estimated ~130; referee's exact integer cross-multiplication is right); decay generalizes
  to `δ_j(T)·T² → 4j²` (my task stated only `j=1`). B1 computational axis NONE →
  INDEPENDENT-CHECKER. Integrated into B1 proof.md §5.1–5.2 + statement.md.
  **[SUPERSEDED by OB-23, 2026-08-11]** The values `δ_1(1)=1216/425`, `T*=127`, `4j²` above
  were computed in **B2's doubled (R-symm) Σ′ convention**, but B1 uses R-atom (sum over
  atoms once). Correct B1 values: `δ_1(1)=608/425`, `T*=90`, `δ_j·T²→2j²`. The OB-18
  checker must be re-run under R-atom (requested as OB-24); B1's computational axis is
  therefore REPRODUCIBLE (not INDEPENDENT-CHECKER) until then. See the cross-theorem
  convention note in B1/B2 statement.md and PROMPT_LINT L21.

- **OB-19 (D Z_ζ leading coefficient):** main theorem CONFIRMED; V4 numerical certificate
  is a **DISCREPANCY**. Exact closed form `Z_ζ,main(t)=(1/2πt)(log(1/t)−γ_E−log2π)` verified
  to 110 digits; leading coeff exactly `1/2π`. Corrected a pre-existing constant error in
  D proof.md (`∫e^{−v}v log v dv = 1−γ_E = Γ'(2)`, not the `−γ_E−1` the draft had). V4's
  explicit `A,C` do NOT follow from bare `O(log T)`; only conditional `C=2A` given an
  explicit `|E(u)|≤A log(u+2)` (e.g. Trudgian 2014) — a stronger added premise, not an
  algebraic expansion of the `O`. V5(b) domain repair: `c≥0, α>0`; excluding `α=1`
  unnecessary. Z_ζ side → INDEPENDENT-CHECKER. Integrated into D proof.md §4 + statement.md.

## Resolved OB-17 outcome (integrated 2026-08-11 — first referee-supplied runnable checker)

- **OB-17 (G diagonal Fredholm interval replay):** literal DISCREPANCY → CONFIRMED after
  the referee's precise restatement. The referee supplied an actual **certified-interval
  checker** (pure `fractions.Fraction`, no float in any certificate; Machin π, Binet/
  Stirling log Γ with proved remainder `|R_8|<4.68e-22`). I **verified SHA-256 match and
  re-ran it in-repo** — prints `ALL_CERTIFIED_CHECKS_PASSED`. It encloses `d_1..d_5` to
  width `<6.83e-12`, certifies `γ_n<d_n<√(1/4+d_n²)` (n=1,2,3; γ_n from Odlyzko's table
  ±3e-9, comparison-only), passes both mutation guards, and certifies
  `Σ_{n>2048}κ_n<10⁻³`. Three corrections integrated: (1) V3 needs error-radius zero
  intervals (formalized as Odlyzko's printed values ±3e-9); (2) **my anchor was wrong** —
  `1/4+d_1²≈318.7154` and `√≈17.85260`, not the `318.706 / 17.8523` I wrote; (3) `G_d≠Ξ̂`
  must use the direct value argument `G_d(γ_1)≠0=Ξ̂(γ_1)`, NOT transitivity of `≠`.
  **Checker deposited at `theorems/G-fredholm-certificate/checker/diagonal_fredholm_interval_replay.py`;
  2 regression tests added (runs + no-float-in-certificate guard); G computational status
  REPRODUCIBLE → INDEPENDENT-CHECKER.**

## Gate-A push batch OB-20 / OB-21 (drafted 2026-08-11) — first "advance to established" attempt

Goal: move a theorem from PROOF-DRAFT toward INDEPENDENTLY-CHECKED on the **mathematical**
axis (Gate A) — the biggest remaining gap. B2 is the pilot (most mature: rank + integer
steps proved, finite core already INDEPENDENT-CHECKER via OB-13). Per the repository rule
"status is derived by the checker, never self-declared," this step is **necessarily
external** — the generator/editor cannot self-certify. Two complementary deliverables:

- **OB-20 (B2 Gate-A review package):** a *whole-theorem* independent inspection (not a
  fragment). Confirms the six links (quartet-decay/well-definedness, rank lemma,
  rationality, integer scaling, membership+predicate, exact collision) AND answers five
  Gate-A questions (hidden gap/circularity, non-vacuity incl. whether (NR) must be an
  explicit class condition, analytic/finite separation, scope honesty, and the verdict:
  advance toward INDEPENDENTLY-CHECKED or blocked). Verdict space: PASS / CONDITIONAL
  (with the exact required edit) / BLOCKED.

- **OB-21 (B2 certified-checker request):** asks for an **independently-written**,
  deposit-ready stdlib checker (exact `fractions`, no float in certificate) reconstructing
  the full pipeline `C→β→R,n,M→collision`, computing `O_j` per-definition and
  cross-checking Chebyshev, with two instances (m=2, m=3) and an adversarial mutation guard
  (K7). On CONFIRMED it will be deposited at `theorems/B2-exact-collision/checker/` and
  pinned in the test suite (like the G checker from OB-17) — turning B2's replay path from
  a one-off reconstruction into a permanent machine-re-verified checker.

Prerequisite cleanup done first: B2's `limitations.md` and `novelty.md` were **stale**
(still called the rank step "CONJECTURE tier / conditional" — contradicting proof.md,
statement.md, dependencies.yaml which have it PROVED since OB-02/OB-13). Both rewritten to
be internally consistent before the Gate-A package ships.

## Resolved OB-20 outcome (integrated 2026-08-11 — FIRST GATE-A PASS)

- **OB-20 (B2 Gate-A review):** **GATE-A PASS.** The referee independently re-derived every
  load-bearing fact from `φ_j` (SymPy exact rational/symbolic), confirmed all six links and
  their coherent composition, and answered Q1–Q5 with no blocking gap, no circularity, no
  RH-import. **B2 mathematical axis advances PROOF-DRAFT → INDEPENDENTLY-CHECKED** (first
  theorem to do so). Notable findings, all independently re-verified in-repo before
  integration:
  - **Stronger non-vacuity than stated:** `d_1(T) = 64(16T²+3)/(256T⁴+160T²+9) > 0` for all
    real T (no real zero — confirmed symbolically), so `β ≠ 0`, `M ≥ 1`, `R ≥ 1` always;
    predicate separation is structural, not a coincidence of a chosen instance. Integrated
    into statement.md as "Structural non-vacuity."
  - **(NR) is automatic:** since `t_k>0, T>0`, every atom is non-real, so the no-real-atom
    condition holds by construction (not an assumption to add).
  - **A verification-tool caveat worth recording:** `sympy.nsimplify` gave a false
    "det C = 0" at m=5 on large-denominator rationals; excluded by pure `Fraction` det.
    Recorded in dependencies.yaml (don't trust a simplifier's zero result).
  Integrated across B2 statement/proof/limitations/novelty/dependencies + contract; theorem
  restated **unconditional** (H-rank/H-real-mult now proved, not hypotheses); 2 new
  regression tests (status ≥ PROOF-DRAFT; Gate-A consistency guard). Tests 63 → 64.

- **OB-21 (B2 certified checker):** **CONFIRMED — checker deposited.** The referee supplied
  an independently-written stdlib checker (`b2_certified_checker.py`, exact `fractions`, no
  float in certificate; `O_j` computed per-definition AND cross-checked against a Chebyshev
  route; K1–K8 including the K7 mutation guard). **SHA-256 verified to match
  (`776eeab5…b64dc83`) and re-run in-repo** → `ALL_CERTIFIED_CHECKS_PASSED`. Deposited at
  `theorems/B2-exact-collision/checker/b2_certified_checker.py`; checker README documents
  B2-CHK-0; 2 regression tests added (runs + emits pass flag; no-float-in-certificate
  guard). Tests 64 → 66. **B2 now has BOTH a Gate-A math review (OB-20) AND a permanent,
  machine-re-verified computational checker (OB-21)** — the "draft → established" loop is
  fully closed for B2, and the checker is exercised on every `pytest`.

## Second Gate-A push OB-22 (drafted 2026-08-11) — G-info diagonal obstruction

Applies the B2 template to G (which already has a deposited certified checker from OB-17,
so a Gate-A math PASS would make it the second double-axis-established theorem). Scoped
carefully because G is more delicate than B2:
- **IN scope (review):** the diagonal obstruction `G_d ≠ Ξ̂` for `𝔐_d^{tr}`, Lemmas
  G.4/G.5, Prop G.3* Item 2. Five links (A convergence, B zeros of G_d, C direct
  value-argument `G_d(γ_1)≠0=Ξ̂(γ_1)` — NOT transitivity, D multiset distinctness via
  Littlewood, E Lemma G.4 Hurwitz) + Q1–Q5.
- **OUT of scope (must NOT be sent for proof):** the conjecture **G-hard** — the reviewer
  only confirms it is cleanly quarantined (no IN-scope step depends on it), never attempts
  to prove it. Also asks to confirm the factorization-condition (2.7) uses only the
  weak/definitional reading.
Uses REVIEW_PROMPT.md common header + Block A. Load-bearing facts (Σκ_n<∞, the three-way
separation, Prop G.3* Item 2) were already script/checker-verified (OB-17); the deliverable
is the whole-theorem judgment.

## Resolved OB-22 outcome (integrated 2026-08-11) — SECOND theorem toward double-axis established

- **OB-22 (G Gate-A review):** **GATE-A CONDITIONAL → integrated.** The referee found no
  reproof needed for the diagonal G-info obstruction (no gap, no circularity, no RH-import,
  G-hard cleanly quarantined, factorization (2.7) confirmed weak-reading-only), but required
  **7 textual/premise fixes** before advancing. All integrated into proof.md **§1a** (none
  changes the mathematics):
  (M1) common Hilbert space `H=ℓ²(ℕ)` + `ξ`/`γ_n`/`N`/`S`/`A` definitions;
  (M2) the **exact** RvM identity `N(T)=1+θ(T)/π+S(T)` as an allowed premise (Titchmarsh–
  Heath-Brown Thm 9.3) — stronger than the `O(log T)` asymptotic, which Link D genuinely
  needs; (M3) weak-factorization-only definition of `𝔐_d^{tr}` (proof uses only `K_N≥0` +
  trace-norm; "zero-free input ≠ zero-blind output"); (M4) explicit Link-D averaging lemma
  + "symmetric difference infinite"; (M5) Link-C `r_1` notation, drop the RH split, use a
  verified critical-line zero `γ_*` (Platt–Trudgian 2021); (M6) Lemma G.5 as a formal
  implication (not an epistemic "cannot verify"); (M7) exact θ-level existence/uniqueness on
  `[7,∞)`. **G-info diagonal obstruction (`𝔐_d^{tr}`) advances PROOF-DRAFT →
  INDEPENDENTLY-CHECKED; G-hard stays `[CONJECTURE]`.** Since G already has a deposited
  interval checker (OB-17), **G is now the second theorem established on both axes**
  (math INDEPENDENTLY-CHECKED + computational INDEPENDENT-CHECKER). Tail bound cross-checked
  (referee's `0.000932773` vs OB-17's `0.000932724`, both `<10⁻³`, different majorants).
  New regression test `test_g_gate_a_conditions_integrated`; tests 66 → 67.

## Third Gate-A push OB-23 (drafted 2026-08-11) — B1 finite-inequality non-discrimination

Applies the Gate-A template to B1 (which already has an exact-rational computational
checker via OB-18, so a math PASS would make it the third double-axis theorem). B1 is
analytically cleaner than G (no conjecture, no factorization subtlety), but has its own
delicate point built into the package:
- **Precise-meaning constraint (OB-18):** B1 must be judged as "**no positive uniform
  separation margin**", NOT "exact collision" (`δ_1(T) > 0` for every finite T; exact
  collision is B2). Link D and Q4 lock this in so the reviewer does not over- or
  under-credit the theorem.
- **W1/W2 convention split:** Q2 asks to confirm both the Li/arithmetic (W1) and Weil (W2)
  conventions are handled, and that the naive Weil evaluation at a *complex* point (which
  blows up like `e^{R_j T}`) is explicitly NOT used.
- Four links (A Σ' convergence, B quartet decay both conventions, C construction, D precise
  meaning) + Q1–Q5. Load-bearing anchors (`δ_1(1)=1216/425`, `δ_j·T²→4j²`, `T*=127`)
  already OB-18-certified. Uses REVIEW_PROMPT.md common header + Block A.

## Resolved OB-23 outcome (integrated 2026-08-11) — GATE-A CONDITIONAL; caught a cross-theorem convention bug

- **OB-23 (B1 Gate-A review):** **GATE-A CONDITIONAL.** Qualitative B1 core CONFIRMED
  (RH-free, non-circular, correct uniform-margin obstruction), but the referee independently
  recomputed the anchors and found a **cross-theorem Σ′ convention inconsistency (PROMPT_LINT
  L21, newly added)**: B1 defines `O_j = Σ'_ρ φ_j(ρ)` (R-atom, sum over atoms once), but its
  numeric anchors had been pasted from B2's `O_j = Σ_ρ[φ_j(ρ)+φ_j(1−ρ)]` (R-symm, doubles).
  Correct B1 values (independently re-verified in-repo, twice): **`δ_1(1) = 608/425`
  (not 1216/425), `T* = 90` (not 127), decay `δ_j·T² → 2j²` (not 4j²)**. Also: removed a
  ζ-example that risked an RH-semantic leak; tightened W1/W2 typing; corrected the W1 Link-A
  convergence argument (conjugate-pairing, not term domination); replaced "no exact collision"
  with the precise "no positive uniform separation margin, and W2/moment families may
  incidentally collide."
  **B2 is UNAFFECTED:** its collision `Cn+Rd=0` is scale-invariant (C→2C, d→2d leaves
  β,R,n,M,collision unchanged), so OB-20 Gate-A PASS and the OB-21 checker stay valid; only
  B2's displayed C,d are a factor 2 larger by its own convention. Integrated: B1
  statement.md (status → Gate-A CONDITIONAL; cross-theorem convention note) + proof.md
  §5.1–5.2 (R-atom values); B2 statement.md (convention note, corrected the false "same as
  B1" claim); PROMPT_LINT L21 + CLAUDE.md item-0; B1 computational axis
  INDEPENDENT-CHECKER → REPRODUCIBLE pending the corrected checker (OB-24). This is exactly
  the kind of latent cross-file inconsistency the lint re-scan exists to catch — surfaced
  here by an external referee applying the theorem's own definition.

## Fourth Gate-A push OB-25 (drafted 2026-08-11) — D spectral-asymptotic exclusion

Applies the Gate-A template to D, now that its Lesch citation is source-verified (in
baseline/) and its Z_ζ side is INDEPENDENT-CHECKER (OB-19). Five links (A Weyl-mismatch,
B heat-trace leading singularity via Lesch A=I j=0, C no-log-needs-both-facts, D Z_ζ side,
E incompatibility) + six Gate-A questions. D-specific delicate points built in:
- **Q2 (ellipticity mandatory):** the non-elliptic `1+D_x²+D_y⁴` counterexample (exponent
  3/4 ≠ 1/2, script-verified ratio→1) confirms ellipticity is load-bearing, not decorative.
- **Q3 (subleading logs OK):** the "no log at any order" claim is correctly withdrawn (Wres
  can give `t^k log t`, k≥1); only the LEADING term matters. Reviewer confirms the argument
  uses only the leading singularity.
- **Q4 (citation scope, L17):** Lesch 1999 (source-verified) is load-bearing; BGV/Gilkey
  (Laplace-type/differential only; Gilkey = Lemma 1.8.2) are scope-limited.
- **Q5 (novelty honesty):** explicitly asks whether D is materially stronger than
  Endres–Steiner 2010 (who did the Weyl-mismatch for compact quantum graphs) or a
  corollary — an honest "heat-trace part is new, Weyl part is context" is an acceptable
  verdict.
Non-circularity: operator side is pure spectral geometry; Riemann side uses only the RvM
count. Uses REVIEW_PROMPT.md common header + Block A.

## Fifth Gate-A push OB-26 (drafted 2026-08-11) — C finite-Euler-factor non-forcing

Applies the Gate-A template to C. C is structurally unlike B1/B2/D/G: it is **not
self-contained analysis** but an *import* of one external theorem (Andersson 2024, Thm 5)
plus a short finite-factor modification, so the review targets (a) whether the citation
covers the object used and (b) the honest novelty increment. Prerequisites done first:
- **Andersson Thm 5 source-verified** and a **PROVENANCE.md deposited** in
  `baseline/andersson-2408.15713/` (label `thm5`, line 203; `.gz` SHA
  `511fa800…f98a67c0`; statement transcribed verbatim; noted **unconditional**).
- **Load-bearing bug fixed before shipping (script-verified):** `statement.md` Step 2/§3
  had the finite-factor multiplier **inverted** — it defined `R = Π(1−p^{-s})/(1−χ(p)p^{-s})`
  whereas the correct `ζ_χ̃/ζ_χ = Π(1−χ(p)p^{-s})/(1−p^{-s})` (numerator carries `χ`;
  verified at `s=0.7+3i`, `P₀=3`: correct form matches to machine precision, inverted form
  gives a different value). `proof.md` §1 was already correct; only `statement.md` carried
  the inversion (a paste-orientation slip).
- **Pseudo-problem removed:** the old Step 3 "critical issue — `R` may vanish near `z_j`,
  push `Im(z_j)` large" is deleted; `R` is holomorphic and **nowhere zero on the whole
  open strip** (all zeros/poles on `Re(s)=0` since `|χ(p)|=1`), so `R(z₁)≠0` automatically.
  Also fixed the mischaracterization "Dirichlet polynomial of degree ≤ P₀^{1/2}" (`R` is a
  **ratio of finite Euler products**, not a polynomial).
- **Stale status fixed:** `limitations.md` §3 said C is "BLOCKED until Andersson
  source-verified" — reconciled to Gate-A CLEARED.

Four links (A citation-covers-object, B multiplier-orientation+telescoping, C
zero-freeness-no-cancellation, D `ζ_χ̃` stays Helson) + seven Gate-A questions. C-specific
delicate points built in:
- **Q3 (target framing — the subtle one):** C exhibits a `P₀`-standard object with `P=0`.
  A `P=1` fiber-mate produced *unconditionally* is not obviously available, and the tempting
  "`ζ` itself" has `P=1 ⟺ RH` (**forbidden**). Asks the reviewer to decide whether the
  **one-sided** non-forcing statement is logically sufficient, or whether a `P=1` companion
  is needed (and if so, whether Andersson Thm 5 with `𝒵 ⊂ {Re(s)=1/2}` supplies one
  without RH). This is the non-circularity crux for C.
- **Q5 (novelty honesty — the decisive question):** C = Andersson + a one-line zero-free
  ratio. Explicitly offers (a) one-paragraph corollary, (b) modest genuine increment, (c)
  materially broader — and asks for the honest publication verdict. An honest "corollary of
  Andersson Thm 5, publish as a remark in Paper A, not a standalone barrier" is a valid,
  first-class outcome.
- **Q4 (Andersson's own finite-set remark):** asks whether Andersson's construction already
  permits fixing finitely many `χ(p)=1` directly (which would make even Step 2 redundant).
- **Q6 (scope/escape, EXT-4a):** Helson-only; Selberg extension provably blocked; DH
  comparison kept logically separate.
Non-circularity: Andersson Thm 5 is unconditional; the obstruction is one-sided (a `P=0`
witness), no `P=1`-via-RH companion. Uses REVIEW_PROMPT.md common header + Block A. Passed
PROMPT_LINT (L5/L6/L18/L19/L21 + self-containment grep clean; the "critical line" hits are
all target-definition or RH-trap-warning context, none assert ζ-zero reality). 4 regression
tests added (`test_c_finite_factor_orientation_correct`,
`test_c_r_zero_free_pseudo_issue_removed`, `test_c_andersson_provenance_deposited`,
`test_c_no_stale_blocked_status`); tests 71 → 75.

## Resolved OB-24 outcome (integrated 2026-08-11) — B1 computational axis restored (R-atom)

- **OB-24 (B1 corrected checker):** **CONFIRMED (Gate-A CONDITIONAL) — checker deposited.**
  The referee supplied an independently-written R-atom checker; **SHA-256 verified
  (`199c7dad…7fe4bc8`) and re-run in-repo** → `ALL_CERTIFIED_CHECKS_PASSED`. It reproduces
  `δ_1(1)=608/425`, `T*=90`, `δ_j·T²→2j²` exactly, cross-checks four-atom traversal vs
  conjugate-pair form, and includes the K6 ×2 R-symm guard. Deposited at
  `theorems/B1-finite-inequality/checker/b1_ratom_certified_checker.py`; B1 computational
  axis REPRODUCIBLE → **INDEPENDENT-CHECKER** (under the correct R-atom convention). 3
  regression tests added; tests 67 → 70. The review also caught two issues in the OB-24
  task text itself, now fixed in B1 proof.md: (a) `δ_2` is NOT monotone over all real
  `T>0` (counterexample `δ_2(1/10) < δ_2(1/4)` — independently verified); the load-bearing
  monotonicity is on **positive integers `T≥1`** only, and the checker exhaustively
  searches `1≤T≤90`; (b) K3's three sample heights are regression anchors, not a limit
  proof — the limit `2j²` is proved from the exact rational forms' leading coefficients.
  B1 math advances to INDEPENDENTLY-CHECKED once the OB-23 §7 textual mods are fully folded
  in (this is the remaining CONDITIONAL item).
  **[DONE 2026-08-11]** All six OB-23 §7 mods are now integrated (7.1 RH-example made
  conditional; 7.2 W1/W2 real-valued typing + complex-point-evaluation excluded; 7.3
  Link-A conjugate-pairing convergence replacing the invalid term-domination; 7.4
  no-uniform-margin wording; 7.5 corrected R-atom anchors; 7.6 Rudin Thm 9.6 citation).
  **B1 math axis advances PROOF-DRAFT → INDEPENDENTLY-CHECKED.** With the OB-24 R-atom
  checker (INDEPENDENT-CHECKER), **B1 is the THIRD theorem established on both axes**
  (after B2 and G). Contract spec_status updated; regression test
  `test_b1_gate_a_mods_integrated` guards the §7 mods; tests 70 → 71.

## Resolved OB-25 outcome (integrated 2026-08-11) — D advances to INDEPENDENTLY-CHECKED

- **OB-25 (D Gate-A review):** **GATE-A CONDITIONAL → PASS.** The referee independently
  re-derived the whole chain: Links A–E CONFIRMED (both the Weyl-mismatch and heat-trace
  branches close, with the exact case-split `p≤1 → 0`, `p>1 → ∞` making the asymptotics
  rigorous), RH-non-circularity CONFIRMED (only the RvM *count* is used; no `Re ρ = 1/2`),
  Lesch scope CONFIRMED (covers the full classical elliptic ΨDO class, `A=I`). Verdict was
  CONDITIONAL pending **8 textual mods**, all now integrated:
  1. operator class + `d≥1`, **closed** manifold, `L²(M)` (scalar audited);
  2. target multiset `Γ_ζ^+ = ⨆{Im ρ}^{m(ρ)}` + RH-sentence fix (`Im ρ∈ℝ` by definition,
     no condition on `Re ρ`);
  3. **Lesch citation** → **Theorem 3.7 + published (3.18)/(3.19)/(3.20)** (= preprint
     `(3.9)`/`(3.10)`). The referee caught that "eq. (3.9)" is the *preprint* number; the
     *published* (3.9) is a different equation. Both numbering schemes now recorded in
     `baseline/lesch-dg-ga-9708010/PROVENANCE.md`; **new lint L22** added for this defect
     class (preprint-vs-published numbering) and the corpus re-scanned;
  4. **Weyl citation** → Hörmander 1968 **Theorem 4.4** applied to `H^{1/m}` via **Seeley
     1967** (not "Seeley 1969"); un-numbered "Ivrii 1980" removed;
  5. "**stronger**" → "**two mutually reinforcing formulations of the same obstruction**"
     (heat trace = Laplace–Stieltjes transform of the counting measure; Abel/Tauber — the
     heat-trace argument excludes nothing the Weyl mismatch misses within `𝒞_ell`);
  6. `H₀` "**order-four principal symbol** `ξ_y⁴`" (full symbol `1+ξ_x²+ξ_y⁴`);
  7. **novelty repositioned** as scope-extension/corollary; **Watson–Valentinuzzi 2026**
     (Bull. Sci. Math. 211, arXiv:2604.00052) disclosed as a near-direct precedent
     (existence/DOI/authors verified 2026-08-11), **not** imported (its v1 has a two-sided
     vs one-sided counting factor-2 mismatch and RH-style phrasing);
  8. explicit escape-route/scope statement.
  **D math axis PROOF-DRAFT → INDEPENDENTLY-CHECKED**, positioned as a classical-ΨDO
  **scope-extension/corollary** (NOT standalone novelty). With the Z_ζ-side INDEPENDENT-CHECKER
  (OB-19), **D is the FOURTH double-axis theorem** (after B2, G, B1). Regression test
  `test_d_gate_a_mods_integrated` added; new lint L22. Tests 75 → 76.

## Resolved OB-26 outcome (integrated 2026-08-11) — C advances to INDEPENDENTLY-CHECKED

- **OB-26 (C Gate-A review):** **GATE-A CONDITIONAL → PASS.** The referee independently
  confirmed the existence core, Links A–D, and RH-non-circularity — including re-deriving the
  finite-factor multiplier orientation (`8.6×10⁻²⁰` agreement) and the strip zero-freeness
  (correct continuous minimum `1−2^{-0.01}=0.006907…`, not the sample `≈0.0088`). Verdict was
  CONDITIONAL pending **6 textual mods**, all now integrated:
  1. **target predicate** redefined as `P_S` on `S={0<Re(s)<1}` (the old "nontrivial zeros in
     the continuation region" was undefined for a general Helson function — no gamma factor);
  2. Theorem C now states explicit meromorphic continuation to `ℂ` + a simple zero at `z₁`;
     homoglyph notation `ζ_χ̃=ζ_χ̃` fixed; analytic-continuation-uniqueness noted;
  3. **consequence narrowed to one-sided** (`O=(1,…,1) ⇏ P_S=1`), plus the reviewer's `R_a`
     **all-fiber strengthening** (every observation fiber has a `P_S=0` member ⇒ no `O`-only
     condition true on some fiber is sufficient for `P_S=1`); optional same-fiber `P_S=1`
     companion via **Andersson Corollary 3** (`cor3`, source-verified) recorded but not needed;
  4. **novelty downgraded** to a corollary of Andersson Theorem 5 (Q5 = option a): Paper A
     named remark, not a standalone barrier;
  5. **citations fixed**: Helson 1969 (Ark. Mat. 8, not "Helson 1954"); Andersson
     arXiv:2408.15713v1 Thm 5 label `thm5`; "faithfully transcribed with the source's `f→ζ_χ`
     typo corrected" (not "verbatim"); Bayart 2002 marked background;
  6. **numerical anchor** marked a grid sample-minimum (continuous exact min recorded);
     unsupported "EXT-4a provably blocked" Selberg claim **narrowed** to "C neither constructs
     nor claims Selberg members" (the impossibility is motivational, not proved here).
  **C math axis PROOF-DRAFT → INDEPENDENTLY-CHECKED**, scope = **one-sided non-forcing
  corollary of Andersson Theorem 5**. Computational axis stays NONE (analytic existence
  result). Added `ANDERSSON-COROLLARY-3` to the ledger (15 claims); 3 C regression tests;
  tests 82 → 85.

## Sixth Gate-A push OB-29 (drafted 2026-08-11) — E compactness / finite-evidence theorem

Applies the Gate-A template to E-compactness (Paper C primary). Two parts: E-neg (per-`N`
non-identifiability, fixed-`N` IFT — its §3 core already CONFIRMED by OB-03) + E-pos
(sufficiency package). Before shipping, two pre-send self-audits (same discipline as C's
R-inversion, H's total-chain, E's own OB-28 restatement):
- **OB-28 (done earlier):** E-neg restated as **per-`N` non-identifiability** (bad radius
  `R_N ≥ 2γ_{k_N+1} → ∞`), NOT "sequence `(F_N)` fails to converge" (PROMPT_LINT L24).
- **OB-29 pre-send fix:** the finite-evidence record's Taylor conditions were written against
  **`ξ̂`** (Fourier transform of ξ, what `det_reg` gives) while the target and the whole §3
  construction are about **`Ξ(z)=ξ(1/2+iz)`** (zeros `γ_n`). Baseline REFERENCE_BASELINE §5:
  `ξ̂` and `Ξ` are DISTINCT normalizations, "never conflate" — the suitably-normalized
  `det_reg → Ξ` is precisely the CCM open step E studies. Fixed: record + target both stated
  relative to `Ξ`; the `det_reg = −iλ^{−iz}ξ̂` identity kept as motivation only.
Four links + seven Gate-A questions, with E-specific delicate points built in: Q1
non-circularity (`γ_n` reality is motivation, never used); Q2 the `Ξ`/`ξ̂`/`z²ξ/ξ'`
normalization discipline; Q3 per-`N`-vs-sequence framing (L24); Q4 E-pos honesty
((H-uorder) must be `r^{1+ε}` not linear finite-type per L1/L14, (H-div) two-sided, both
unproved-for-CCM). Passed PROMPT_LINT (L1/L14/L17/L18/L19/L21/L24 + self-containment).

## Seventh Gate-A push OB-30 (drafted 2026-08-11) — E' meromorphic (Suzuki-target) companion

Applies the Gate-A template to E-prime-meromorphic (the Suzuki `W=z²ξ/ξ'` companion of E).
E' had already survived three targeted rounds (OB-06 parity/structure, OB-09 E'-neg, OB-11
E'-pos); this is the whole-chain verdict. Two pre-send self-audits before shipping:
- **Metadata cleanup:** reconciled stale status/dependency lines with the OB-06/09/11
  corrections — statement top status ("E'-pos open" → corrected PROOF-DRAFT); dependency
  roles for MARTY ("replaces Montel" → **Montel suffices, Marty not needed**, OB-11) and
  HADAMARD-PRODUCT-XI ("|W(iR)|→∞" → **REFUTED**, OB-09); limitations/novelty/checker-README
  all rewritten to the post-correction reality.
- **LOAD-BEARING fix (L1/L14, THIRD occurrence):** E' used a *linear* `T(r,F)=O(r)` /
  `Cr+C₀` characteristic for the meromorphic target `W`. But `W`'s poles are the zeros of
  `ξ'`, density `~(r/2π)log r`, so `T(r,W) ≍ r log r` — order 1 but **maximal type**, NOT
  `O(r)`; the linear bound excludes `W` itself and makes the class vacuous (the meromorphic
  analogue of the entire-`Ξ` error OB-14 fixed). Script-verified `N(r,∞)/r → ∞`
  (`0.65→1.01→1.38`). Fixed every occurrence to the conventional-order envelope
  `T(r,·) ≤ C_ε r^{1+ε}+C_{0,ε}` (method class, Lemma E'.1, (UG), order-transfer step,
  membership). **This was a re-scan miss** — the L14 fix from OB-14 (E) was never propagated
  to E'; PROMPT_LINT L14 now carries an explicit RE-SCAN OBLIGATION and the whole
  `theorems/*/` corpus was re-grepped (clean: only the corrective notes remain).
Four links + seven Gate-A questions: Q1 non-circularity, Q2 parity (W odd, γ_n are zeros),
Q3 `W`/`Ξ`/`ξ̂` normalization, Q4 per-`(k,J)` framing, Q5 E'-pos honesty (conventional-order
(UG), Suzuki ingredients OPEN), Q6 citations, Q7 verdict. Passed PROMPT_LINT
(L1/L2/L3/L9/L14/L17/L18/L19/L21/L24 + self-containment).

## Eighth Gate-A push OB-31 (drafted 2026-08-11) — D' log-polyhomogeneous escape-route audit

Applies the Gate-A template to D-prime-logpoly. **Unlike the others, D' is not a barrier or
a positive theorem — it is an escape-route audit** of Theorem D, reaching a *negative
refinement* (a hardening of D): (A) the leading-singularity obstruction of D **extends to
finite-log-degree `𝒞_logpoly`** (pure-power leading term; logs only subleading, witnessed on
`S¹` by `H_c e_n=(|n|+c log|n|)e_n` ⇒ `Z=2/t−2c log(1/t)+O(1)`), so `𝒞_logpoly` is **not** an
escape; (B) the genuine escape class is the log-weighted `S^{1,-1}` (`|ξ|/log|ξ|`) class,
inside Hörmander `S¹_{1,0}`, giving `N_H~cT log T`; (C) the Hilbert space must be `S¹`/`ℓ²`,
not `L²(ℝ)` (L20: continuous spectrum, not trace class); (D) the exact model
`2πn/log(n+e)` is **REFUTED** (count differs from `N_ζ` by `≍ T log log T` — script-verified:
gap grows, `gap/(T log log T)` bounded ≈ 1.8→1.14 at `T=10³…10⁶`); (E) the broader
Lambert-`W`-corrected class is an **honest open Hilbert–Pólya frontier**, not a theorem, with
matching-law-is-not-sufficient and tautological `diag(γ_n)` explicitly excluded. Load-bearing
Claim D re-verified by script before shipping. The Gate-A ask: confirm the audit is correct
and non-circular, and that the `LEADING-SINGULARITY-COVERS-LOGPOLY` lemma (currently PENDING)
may advance to INDEPENDENTLY-CHECKED while the document stays ESCAPE-ROUTE-REFINED with
Claim E an open frontier. Passed PROMPT_LINT (L17/L18/L19/L20/L21/L24 + self-containment; no
linear-characteristic issue — D' is a counting/heat-trace audit, not an approximant theorem).

## Ninth Gate-A push OB-32 (drafted 2026-08-11) — H information-obstruction partial order

Applies the Gate-A template to H-information-hierarchy. H is a **unification framework**; its
two instantiations are already Gate-A established and inherited unchanged (`O_finite` = B2,
PASS OB-20 + checker OB-21; `O_theta` = G-info, PASS OB-22 + checker OB-17), so OB-32 targets
**only H's own increment**. Pre-send self-audit fixed stale dependency metadata: the H
dependencies/contract still marked B2-RANK-RESULT and G-INFO-OBSTRUCTION as
`PROOF-DRAFT`/`usable_as_premise:false`/`gate_a OPEN` — reconciled to INDEPENDENTLY-CHECKED
(they are, since OB-20/OB-22). The Gate-A target is: (1) the observation structure is a
**PARTIAL order, not a total chain** (OB-27 corrected the false `O_finite⊂O_theta⊂O_vM⊂O_oracle`);
(2) **incomparability H'(i)**: `O_finite ⋈ O_theta`, two script-verified witnesses (same-Im
quartet pair `σ=3/4` vs `9/10` separated by `Li_1=0.019913` vs `0.019855` but not by `θ`; an
S(T) move separated by `θ` but not `Li`), with the L23 subtlety that G's `d_n=θ_level(n)` is
a fixed zero-free sequence, constant on multisets; (3) **coarsening H'(ii)**:
`O_finite,O_theta ≺ O_oracle` inherits the exact B2/G collisions. Non-circularity: H is about
which coordinates each map sees; inherited obstructions are RH-free. Ask: confirm the
incomparability increment may advance to INDEPENDENTLY-CHECKED and H is a correct unification
framework (organizing section, not a standalone barrier), adding no new analytic content
beyond B2/G. Passed PROMPT_LINT (L18/L19/L21/L23 + self-containment; witness values
re-verified consistent with statement.md).

## What a returned verification should contain

- Statement: CONFIRMED, PARTIAL, or REFUTED for each numbered step.
- For PARTIAL or REFUTED: explicit gap description or counterexample.
- Any proof corrections needed.
- Citation verification for theorem numbers (especially OB-01).
