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
| OB-22 | `OB-22-G-gate-a-review-package.md` | G | **GATE-A**: independent review of the diagonal G-info obstruction (Links A–E + Q1–Q5; G-hard explicitly OUT of scope) | OPEN — send for review |
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

## What a returned verification should contain

- Statement: CONFIRMED, PARTIAL, or REFUTED for each numbered step.
- For PARTIAL or REFUTED: explicit gap description or counterexample.
- Any proof corrections needed.
- Citation verification for theorem numbers (especially OB-01).
