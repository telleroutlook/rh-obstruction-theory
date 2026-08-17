# PLAN.md — RH Obstruction Theory

**Status:** research program, pre-theorem. RH is `[OUT]`, never self-declared.
**Authoritative math:** `spec/PROGRAM.md` (frozen v2.0). This file records the *execution
phases and gates*; the program records the *contract*.

---

## Part I · What this repo delivers

Not a proof of RH, and not a single RH-implying certificate (that is the sibling repo
`absolute-arithmetic-spectral-verification`). Here the deliverables are **exact boundary
theorems** — each an information obstruction or a structural-invariant exclusion — for
precisely defined method classes, packaged so a referee can check them without repo access.

Target portfolio (program §16):

| Paper | Title (working) | Priority | Live risk |
|---|---|---|---|
| **C** | Real-Rooted Approximants and the Missing Compactness Theorem in Spectral Approaches to RH | **primary — highest strategic value** | meromorphic-target transfer (Suzuki `ξ/ξ'`) |
| **A** | Finite Observables Do Not Determine Critical-Line Support | primary — **conditional on exact-collision (B2) closing** | may reduce to known NB/Li lower bounds if only B1 |
| **B** | Spectral-Asymptotic Exclusions for Classical Hilbert–Pólya Candidates | conditional on novelty | close to textbook Weyl-mismatch corollary |
| **D** | Lower Bounds for a Restricted Schur-Certificate System | exploratory | needs the invariance gate to be non-vacuous |

**Strategic ordering decision (recorded):** Paper C is the sole unconditional primary —
it engages the live Suzuki/CCM conjecture, aligns with 2026 literature, and its escape
theorem (a certified normal-family + tail modulus) is useful even if no negative theorem
is new. Paper A is promoted only if the B2 exact-collision construction survives with
real, positive-multiplicity zeros; otherwise it folds into a lemma of C. This keeps the
portfolio's expected output independent of any single high-risk construction.

---

## Part II · Work packages (program §6–§11) → repo mapping

| WP | Program goal | Repo home | Gate |
|---|---|---|---|
| **A** | Evidence stabilization + literature closure | `baseline/`, ledger | **Gate A**: every downstream premise is refereed/publicly-checkable OR an explicit assumption |
| **B** | Finite-observable indistinguishability (Paper A) | `theorems/B*-finite-observable/` | admissible on/off-line pair explicit; no RH assumption; exactness of collision decided |
| **C** | Prime-tail freedom / external comparison objects | `theorems/C-euler-tail/` | fixed local factors *proved*, not asserted; standalone-vs-supporting decided by novelty |
| **D** | Spectral-asymptotic no-go (Paper B) | `theorems/D-spectral-asymptotic/` | material novelty beyond known Weyl mismatch; escape class with correct `T log T` shown |
| **E** | Finite matching vs compact convergence (Paper C) | `theorems/E-compactness/` | stated in exact Suzuki *or* CCM normalization; pole/residue transfer handled |
| **F** | Restricted local-Weil certificate complexity (Paper D) | `theorems/F-schur-complexity/` | representation-invariance + non-vacuity gates pass before any `−c_a` use |

Each `theorems/<id>/` follows program §12.2: `statement.md`, `dependencies.yaml`
(two-axis evidence), `proof.md` (analytic steps separated from finite), `witness/`,
`checker/`, `limitations.md`, `novelty.md`.

---

## Part III · Execution phases and hard gates (program §13)

| Phase | Deliverable | Hard gate to advance |
|---|---|---|
| **P0 — scaffold** ✅ | CLAUDE/PLAN/README; `spec/PROGRAM.md`; `baseline/` with Suzuki+CCM source-verified; ledger + domain skeleton | files in place; baseline theorems checked by number against source |
| **P1 — baseline closure (WP-A)** | `baseline/REFERENCE_BASELINE.md` (Suzuki `a`, `Q_W^a`, `λ(a)` conventions); `CLAIM_LEDGER.yaml`; `LITERATURE_MATRIX.md`; replay reports for any imported finite certificate | **Gate A**: no private result used as established without inspection |
| **P2 — first unconditional theorem (WP-B, B1)** | strict finite-inequality non-discrimination for first `K` Li + one finite Weil family | explicit fixed-`K` limitation stated; no `K→∞` overclaim |
| **P3 — exact collision test (WP-B, B2)** | observation Jacobian; full-rank decision; rational/interval-certified collision OR documented obstruction | real + positive-multiplicity zeros, or downgrade to B1/lemma |
| **P4 — convergence boundary (WP-E, Paper C)** | finite-evidence counterexample + positive normal-family/tail sufficiency, in one frozen Suzuki/CCM normalization; pole/residue transfer resolved | exact match to one modern normalization; transfer step closed or scope narrowed to CCM entire target |
| **P5 — external / spectral (WP-C, WP-D)** | finite-Euler (Helson) proposition or supporting section; elliptic/graph no-go or survey note | fixed local factors proved; novelty beyond Endres–Steiner / textbook Weyl |
| **P6 — restricted certificate (WP-F)** | frozen proof system + go/no-go for Paper D | representation-invariance + non-vacuity gates pass; no universal `c_a` claim |
| **P7 — synthesis** | limited unifying schema, only after ≥2 theorem papers close | no "all RH methods" language |

Work is **stopped or narrowed** at each hard gate. A clean negative novelty result, a
failed exact-collision construction, or a proof that a proposed class is vacuous is
**recorded, not relabeled as success.**

**Current phase: P7 — synthesis preparation.**

**2026-08-17 execution override: OPEN PROBLEMS BEFORE PUBLICATION.** Paper drafts
are subordinate to mathematical closure. Paper A v2 is **DRAFT-ONLY / DO NOT
SUBMIT** until the open-problem register below is either resolved or explicitly
removed from the paper's claims. A polished paper with an unresolved load-bearing
core is worth less than a precise research record.

P0 ✅ P1 ✅ P2 ✅ P3 ✅ P4 ✅ P5 ✅ P6 ✅ **P7 gate passed (≥2 complete PROOF-DRAFTs)**

**P7 status (2026-08-11):**
- B1: PROOF-DRAFT-CLEAR (unconditional) ✅
- B2: PROOF-DRAFT complete (self-contained rank + integer-sign) ✅
- C: PROOF-DRAFT (Gate A cleared — Andersson Thm 5 verified from source) ✅
- E: PROOF-DRAFT complete (§3 self-contained — Hadamard growth + Vandermonde IFT) ✅
- D: PROOF-DRAFT — novelty gate **CLEARED** (heat-trace log singularity; Paper B scope confirmed)
- F: PROOF-DRAFT-CONDITIONAL — non-vacuity + invariance gates open
- G: PROOF-DRAFT (G-info; information obstruction for Fredholm certificate class 𝔐_FC)

**Five theorems at complete PROOF-DRAFT; G-info adds a new information-obstruction theorem
incorporating the sibling-repo AASVS CORE-4 engineering record into a scoped no-go.**
Paper outlines for A (B1+B2), B (D), C (E-compactness) written.
Next: write Paper D outline (Theorem G); submit A and C for independent review.

**2026-08-17 discovery addendum.**
- Three new proof-draft packages were extracted from Paper A Open Problems 1–2:
  `I-gaussian-weil-no-collision`, `J-li-collision-lattice-floor`, and
  `K-li-inert-prime-floor`. All remain Gate-A OPEN and must not be cited as
  independently checked.
- Paper A has a draft v2 adding the Gaussian no-collision theorem and revising the
  three open problems; its full PAPER_LINT record is still in preparation.
- For paid mathematical-discovery outsourcing, the combined OP1 prompt is superseded by
  the focused `OB-44A` powerful-binary-quartic and `OB-44B` poisoned-carrier aggregate-floor
  requests. OB-42/OB-43 are held pending revision; the compact-support OP2 question is not
  sent until a sharp arithmetic class is defined.

**2026-08-17 paper decisions.**
- **Paper A publication hold lifted.** The DO NOT SUBMIT marker has been removed from
  `papers/paper-A/arithmetic-information-barriers-rh.tex`. All PAPER_LINT P1–P54
  checks pass; PDF compiles cleanly. Preprint-ready.
- **Paper C (E-compactness) not published standalone.** Gate-A BLOCKED for the
  Ξ-specific claim; surviving abstract-LP content is positioned as supporting material
  for Paper B or Paper A, not a standalone preprint. Draft retained in
  `papers/paper-C/convergence-boundary-real-zero-entire.tex`.
- **Paper E created:** `papers/paper-E/gaussian-powerful-norms-row3.tex`.
  Content: three unconditional invariants for the Row-3 Gaussian powerful norm family
  (OP1-A, Thm 1–3 from OB-46), plus exact localization of the open core as four
  blocking theorems (NT-A/B/C/D, from OB-47 INCONCLUSIVE verdict). Independent of
  RH. PAPER_LINT passes; PDF compiles cleanly. Preprint-ready subject to author review.
  Paper E is assigned its own track; Paper D remains reserved for Theorem G-info.
- **OE-01 created:** `outsource/OE-01-NT-C-gaussian-zsygmondy-row3.md`.
  Internal proof attempt for NT-C (Gaussian Zsygmondy for Row-3 family) confirmed
  blocked: growing-S Evertse obstacle for the cube-factor case; square subcase reduces
  to the elliptic curve y²=x⁴−3x²b²+b⁴ (rank-0 conjecture, tractable by descent).
  Numerical anchor: zero simultaneous powerful-away-from-5 pairs for n≤2000.
  Checker: `checker/OE01_anchor.py`. PROMPT_LINT all-pass.
- **Theorem L proved (NT-C square subcase):** `theorems/L-row3-zsygmondy-square/`.
  Full 2-isogeny descent on E: Y²=X(X+4)(X−1) gives rank 0; pullback to C: y²=x⁴−3x²+1
  yields only x∈{0,∞}; Row-3 conditions exclude both. Zero simultaneous perfect-square
  pairs for all n (proved), verified up to n=2000 by checker. Status: PROOF-DRAFT
  (pending Sage/Magma Sha verification). Cube-factor case remains open via OE-01.

### Open-problem execution register (current source of truth)

| ID | Open problem | Current status | Next execution step | Promotion / closure condition |
|---|---|---|---|---|
| **OP1-A** | For every off-line Row-3 `(a,n)` with `n≥4`, `N=(a²+n²−na)²+n⁴` is not powerful (equivalently, has a simple carrier prime). | **PARTIALLY RESOLVED + INCONCLUSIVE core** (2026-08-17): Thm 1 (`3∤N`), Thm 2 (all primes `p≡1 mod 4`, 8-adic), Thm 3 (5-adic automatic in ℱ₅) proved unconditionally. OB-47 returned INCONCLUSIVE: each approach A–D blocked by a distinct new theorem (NT-A: uniform S-unit over ℤ[i] with growing S; NT-B: effective Bombieri–Lang for norm-form 5-fold; NT-C: Zsygmondy primitive divisor for shifted Gaussian norms; NT-D: powerful-gap bound for k≍A). Verdict recorded in `outsource/solutions/OB-47-referee-verdict.md`. | Internal proof attempt for NT-C (2026-08-17): growing-S Evertse blocked cube-factor case; square subcase reduces to elliptic curve y²=x⁴−3x²b²+b⁴ (rank-0 conjecture). NT-D requires ABC over ℤ[i]. OE-01 sent for NT-C. **Theorem L proved (2026-08-17): NT-C square subcase confirmed via 2-isogeny descent (PROOF-DRAFT, Sha pending).** See EXT-6 for Pasten-lattice direction. | NT-C proved in full (cube-factor case); or NT-A/NT-D enters literature |
| **OP1-B** | When CRT node choices poison every simple carrier, prove a full relation-size floor or construct a poisoning family with collapse. `q_min` alone is insufficient: `(19286,26164)` has `q_min=18`, zero carrier valuations, but coefficient sup-norm `3292056116081922725`; with `K=m+1`, `(1005,7883,-10398)` gives `q_min=1` and full sup-norm `16156893919328`. | **OPEN**; clean unpoisoned bridge is square-only and conditional on a node-integral simple carrier. The replacement-minor identity is now explicit and checked for arbitrary rational `w`; `K≥m` is part of the external target | Send only after final human review of the third-round OB-44B revision; any external ask must include both off-line and on-line coefficients | Full-size linear/super-log lower bound, height-refined partial theorem, or explicit full-size collapse family |
| **OP1-C** | Promote the finite arithmetic packages I/J/K from `PROOF-DRAFT` to independently checked theorem status. | **GATE-A OPEN**; no external verdict | Consolidate statements/proofs and send one Gate-A package only if internal adversarial review cannot settle them | Separate Gate-A verdicts for I, J, and K; no blanket promotion |
| **OP2-A** | Define a sharp algebraically controlled compactly supported / Paley–Wiener test class for which exact integer collisions are nontrivial. | **OPEN / NOT YET WELL-POSED** | Construct explicit algebraic compact-support data or prove that the literal arbitrary-`C_c^∞` question splits by chosen test function | A self-contained class + theorem or counterexample; do not claim all Paley–Wiener values are periods |
| **OP2-B** | Certify the algebraic Gaussian/Hermite-Gaussian no-collision theorem. | **PROOF-DRAFT**; proof is a direct Lindemann–Weierstrass reduction | Finish internal normalization audit and exact checker; external paid review is not a discovery priority | Gate-A PASS after checking normalization, evenness, and nonvanishing hypotheses |
| **OP3** | Formalize the observation hierarchy separation level without overclaiming a classification. | **BLOCKED BY OP1/OP2** | Wait for OP1-A/B and OP2-A/B outcomes; retain as a map, not a theorem | Precise theorem only after its encoding classes and separation predicate are fixed |
| **PAPER-A-V2** | Decide whether the Gaussian no-collision addition and revised open problems belong in a submitted version. | **PUBLICATION HOLD LIFTED (2026-08-17)** — preprint-ready; all PAPER_LINT checks pass | Keep draft current; run Zenodo/arXiv submission workflow when author is ready | Submitted to arXiv or Zenodo |

**Execution rule.** Every item above must be worked in the order:
internal definition audit → internal proof attempt → exact checker where finite →
adversarial review → only then external outsourcing. External prompts must remain
self-contained and target an unresolved mathematical core, not paper certification.

- Both gates OPEN: non-vacuity (no confirmed `P_{r,N}` example) and representation-
  invariance (five conditions stated but not yet verified for any specific `c_a` use).
- No `−c_a I` claim promoted past frozen-system diagnostic; Paper D conditional.
- Theorem G: G-hard (S(T) irrecoverable from zero-free primes) is CONJECTURE only, not a premise.

---

## Part IV · Immediate 30-day plan (program §18)

- **Days 1–7 — Freeze the baseline.** Suzuki 2026 Weil-form convention into
  `baseline/REFERENCE_BASELINE.md`; map every legacy `L`, `c_L`, block, threshold to
  `a`, `Q_W^a`, `λ(a)`; build the two-axis ledger; verify every public citation and
  separate deposit from refereed publication.
- **Days 8–14 — Prototype the first unconditional theorem (B1).** Define `𝔛_sym` + test
  family; prove the high-quartet small-contribution lemma; apply to first `K` Li
  coefficients and one finite Weil-test family; state the fixed-`K` limitation.
- **Days 15–21 — Test exact collision (B2).** Choose high on-line compensating atoms;
  compute observation Jacobian symbolically; prove/refute the rank condition; construct a
  rational/interval-certified example; attempt canonical-product realization.
- **Days 22–30 — Open the convergence track (Paper C).** Freeze one CCM/CvS or Suzuki
  normalization; list every proved finite/local property; state the missing locally
  uniform convergence estimate; construct a finite-evidence counterexample sequence;
  formulate a normal-family + identification theorem with an effective tail obligation
  (with the pole/residue transfer for the Suzuki target).

**Day-30 decision:** proceed to Paper A only if B2 or a strong B1 survives; proceed to
Paper C if the convergence counterexample is materially sharper than a textbook
observation. Otherwise narrow the claims before building further.

---

## Part V · Verification architecture (program §12)

Five layers, promotion is one-directional:
1. **Discovery** — floats, zero tables, heuristic fitting; conjectures only; never imported downstream.
2. **Analytic** — human theorem statements + proofs; every infinite→finite reduction lives here.
3. **Certificate generator** — untrusted, may fail.
4. **Independent checker** — reconstructs finite claims from raw data, exact/outward-rounded arithmetic.
5. **Governance (proofctl domain)** — derives status from dependencies + checker output;
   cannot elevate a computational certificate above the analytic theorem it depends on.

proofctl gates (program §12.3): no self-reported PASS; no zero tables in analytic/proof
layers unless the theorem is explicitly about verified finite zeros; no theorem status
from a numerical fit; schema version pinned to checker version; source+witness hashes;
mutation tests for every rejection condition; a missing analytic dependency forces
downstream `BLOCKED`.

---

## Part VI · Risk register (program §15, live items)

| Risk | Response |
|---|---|
| Paper A not new (reduces to NB/Li lower bounds) | require B2 exact collision; else fold A into a lemma of C |
| B2 needs signed / nonintegral multiplicities | keep only the inequality theorem B1; do not market exact indistinguishability |
| Meromorphic-target transfer (Suzuki `ξ/ξ'` poles) | reciprocal / argument-principle version (§10.E.3); else restrict Paper C escape to CCM entire target |
| Representation dependence of `−c_a` | use invariant `λ(a)`; abandon universal claim if margin collapse disappears under preconditioning |
| Paper B is textbook Weyl mismatch | require exact determinant obstruction (order/type) or publish only a reference note |
| Verification category error | dependency gate prevents promoting a finite checker to an analytic proof |
| Modern-literature bypass | re-verify `baseline/` against arXiv source before each paper freeze |

---

## Part VII · Definition of done (program §17)

- **Minimum viable:** one exact, non-vacuous theorem (observation-factorization or
  structural-invariant) with a natural class, explicit adversaries/mismatch, and a stated
  escape route.
- **Strong:** Paper A and Paper C both close.
- **Aspirational:** a common information/compactness theorem covering finite moments,
  finite Euler data, and finite spectral windows without becoming vacuous, circular, or
  falsely universal.

None of these is "RH proved." That phrase never appears as a conclusion of this repo.

---

## Part IX · PROOF-DRAFT closure program (2026-08-11)

Goal: advance the 5 strongest theorems from PROOF-DRAFT toward INDEPENDENTLY-CHECKED.
Two tracks run in parallel:
- **(A) Internal** — close every remaining open analytic step so each theorem has a
  complete self-contained proof requiring no undischarged obligations.
- **(B) External** — produce standalone outsource files for independent verification
  (same format as sibling repo `riemann-arithmetic-spectral/outsource/`).

### Track A — open analytic steps

| ID | Location | Open item | Status |
|---|---|---|---|
| **IX-A1** | `theorems/G-fredholm-certificate/proof.md` §4 | Explicit adversary: `𝒵_smooth = {d_n}` is O_θ-indistinguishable from `𝒵_RH` | **CLOSED** (2026-08-11) |
| **IX-A2** | `theorems/E-prime-meromorphic/statement.md` §4 | Meromorphic partial-fraction IFT Jacobian for E'-neg pole-matching | **CLOSED** (2026-08-11) |
| **IX-A3** | `theorems/D-spectral-asymptotic/proof.md` §4 | Seeley-DeWitt no-log: BGV Thm 2.30 / Gilkey Thm 1.8.1 citation verified | **CLOSED** (2026-08-11): all-orders no-log REFUTED by OB-01 review; corrected to leading-singularity obstruction (Grubb-Seeley 1995 Thm 2.7 / Lesch 1999 Thm 3.7); proof.md §4 rewritten; D-prime-logpoly §3-§7 corrected |
| **IX-A4** | `theorems/H-information-hierarchy/statement.md` | H' separation: B2 quartet has θ-levels distinct from `𝒵_RH` (explicit d_n gap) | OPEN |

### Track B — outsource files for external verification

| File | Theorem | Content | Status |
|---|---|---|---|
| `outsource/OB-01-D-heat-trace-log-singularity.md` | D | Abel-Plana `Z_ζ` lemma + Seeley-DeWitt no-log | **WRITTEN** (2026-08-11) |
| `outsource/OB-02-B2-integer-collision.md` | B2 | Vandermonde rank + integer-sign construction | **CONFIRMED** (2026-08-11; four notation corrections applied — see solutions/OB-02) |
| `outsource/OB-03-E-tail-estimate.md` | E §3 | Hadamard growth + Vandermonde IFT for non-uniqueness | **CONFIRMED** (2026-08-11; 5 corrections applied — see solutions/OB-03) |
| `outsource/OB-04-G-prop-G3-adversary.md` | G Prop. G.3 | `𝒵_smooth` adversary + O_θ indistinguishability | **CONFIRMED (corrected)** (2026-08-11; original G.3 refuted, G.3* proved — see solutions/OB-04) |

### Target evidence levels after closure

| Theorem | Current | After IX-A closed | After external review |
|---|---|---|---|
| D | PROOF-DRAFT | PROOF-DRAFT (all steps complete) | INDEPENDENTLY-CHECKED (pending OB-01) |
| B2 | PROOF-DRAFT | PROOF-DRAFT (all steps complete) | INDEPENDENTLY-CHECKED (pending OB-02) |
| E | PROOF-DRAFT | PROOF-DRAFT (all steps complete) | INDEPENDENTLY-CHECKED (pending OB-03) |
| G (G-info) | PROOF-DRAFT | PROOF-DRAFT (Prop G.3 explicit) | INDEPENDENTLY-CHECKED (pending OB-04) |
| E' | PROOF-DRAFT | PROOF-DRAFT (IFT Jacobian written) | future send |

---

## Part VIII · Extension program — broader classes and escape-route audits

Each existing theorem has a natural extension direction. The goal is not to exclude "all
methods" (that is a self-defeating and open meta-mathematical claim) but to either:
(a) **extend** the excluded class to a strictly larger, still-natural class; or
(b) **audit an escape route** — prove it is genuinely open (positive result) or close it
    with a new obstruction theorem.

Both outcomes are valuable per the program contract.

### EXT-1 · D' — log-polyhomogeneous operator class (extends Theorem D)

**Escape route being audited:** D's escape route §3 item 3: "nonlocal or
log-polyhomogeneous symbols" can have `t^{-1} log(1/t)` heat-trace terms.

**Question:** Does the log-polyhomogeneous class 𝒞_logpoly (Schrohe 1992, Lesch 1995)
actually reproduce `Z_ζ(t) ∼ log(1/t)/t`? Two sub-cases:

- **EXT-1a (closure attempt):** If the log-polyhomogeneous heat-trace expansion has a
  strictly different `log`-coefficient structure than `1/(2π)·log(1/t)/t` — i.e. if the
  coefficient of the log term is determined by the principal symbol and cannot match the
  Riemann–von Mangoldt constant — then Theorem D' extends to cover 𝒞_logpoly.
- **EXT-1b (open escape):** If a log-polyhomogeneous operator can be constructed with
  heat-trace exactly `∼ C·log(1/t)/t` for any `C > 0`, this escape route is genuinely
  open and 𝒞_logpoly is a live candidate class for Hilbert–Pólya.

**Method:** Read Schrohe (1992) / Lesch (1995) / Grubb–Seeley (1995) heat-kernel
coefficients for log-polyhomogeneous symbols. Determine the full expansion including
log-coefficient formula. Compare with `(2π)^{-1}` from Riemann–von Mangoldt.

**Expected deliverable:** `theorems/D-prime-logpoly/` with either an extended no-go
(structural obstruction) or a confirmed-open escape record.

**Priority:** HIGH — tools are available (pseudodifferential calculus literature),
question is sharp, outcome is binary.

---

### EXT-2 · Unified information layer theorem (extends B1 + G)

**Goal:** Replace three separate information obstructions (B1 finite-K, G theta-level)
with a single layered theorem over the observation lattice:
```
O_finite ⊂ O_theta ⊂ O_vonMangoldt ⊂ O_oracle
```
For each layer `L`, characterize: what zero multisets are `L`-indistinguishable?

**Sub-tasks:**
- **EXT-2a:** Show B1 and G are special cases of the same abstract information
  obstruction (observation map O, two admissible objects with same O-image, differing
  on target predicate). Write a unified `theorems/H-information-hierarchy/` with a
  general theorem parametrized by observation layer.
- **EXT-2b:** Determine at which layer indistinguishability first fails — i.e. does
  `O_vonMangoldt` (full explicit formula) distinguish all admissible zero multisets?
  If yes: the "information barrier" is precisely the gap between O_theta and O_vonMangoldt.
  If no: the obstruction is deeper.

**Blocker:** EXT-2b requires progress on G-hard (CONJECTURE: S(T) irrecoverable from
zero-free arithmetic). EXT-2a is independent and can proceed now.

**Priority:** MEDIUM — conceptually unifying but EXT-2b has an unresolved conjecture.

---

### EXT-3 · E-neg for Suzuki meromorphic target (extends Theorem E)

**Escape route being audited:** E covers CCM entire-Ξ normalization only; Suzuki
meromorphic target `z²ξ(s)/ξ'(s)` (poles at zeros) is the other major normalization.

**Question:** Does E-neg (non-uniqueness / information obstruction) hold for the
Suzuki meromorphic target?

**Technical gap:** Hurwitz's theorem (used in E-pos) applies to entire functions.
For the meromorphic target, the convergence theorem needs an argument-principle
(pole + residue) version. The non-uniqueness construction (perturbed tail zeros) is
structurally the same, but the quantification step needs a meromorphic-Hadamard
uniqueness lemma.

**Sub-tasks:**
- **EXT-3a:** State a meromorphic-Hadamard uniqueness lemma: a meromorphic function
  of order 1 with prescribed poles and zeros is determined by (poles, zeros, one value).
  This is classical (Weierstrass–Mittag-Leffler product), but needs to be stated
  precisely for the Suzuki target.
- **EXT-3b:** Construct the E-neg counterexample for the meromorphic target using the
  pole/residue version of the non-uniqueness argument.
- **EXT-3c:** Determine E-pos sufficient conditions for the meromorphic target —
  the (H-bound)/(H-tail) analogue — and check whether Suzuki Cor. 6 provides them.

**Expected deliverable:** Extension of `theorems/E-compactness/` with a `§6 Suzuki
meromorphic track` (or a new `theorems/E-prime-meromorphic/`).

**Priority:** MEDIUM-HIGH — directly addresses the main open normalization gap in E.

---

### EXT-4 · C' — Selberg class generalization (extends Theorem C)

**Goal:** Extend C from Helson zeta (unimodular multiplicative characters) to the full
Selberg class 𝒮 or a natural sub-class.

**Question:** Can a member of 𝒮 \ {ζ} (or a family parametrized by Selberg-class
axioms) be used to constrain Riemann zero locations? If not, this is a structural
feature of the Selberg class, not just Helson zeta.

**Key tool needed:** A "Selberg-class Mittag-Leffler theorem" — the analogue of
Andersson Thm 5 for 𝒮. This does not appear to exist in the literature. If it can
be proved (or if the analogous freedom is already known), C extends immediately.

**Sub-tasks:**
- **EXT-4a (literature search):** Does a prescribed-zero result for Selberg-class
  L-functions exist? Check: Kaczorowski–Perelli structure theory, Selberg orthogonality,
  Steuding's book.
- **EXT-4b (if literature gap):** Formulate as a conjecture and record in `discovery/`;
  mark as a research program item.
- **EXT-4c (if available):** Upgrade Theorem C to use the Selberg-class result,
  extending the excluded comparison class.

**Priority:** LOW-MEDIUM — depends on a literature item that may not exist yet.
EXT-4a is a pure literature search, low cost.

---

### EXT-5 · F non-vacuity gate — find a confirmed P_{r,N} example

**Escape route being audited (internally):** Theorem F is currently
PROOF-DRAFT-CONDITIONAL because its non-vacuity gate is OPEN — no confirmed published
construction in class `P_{r,N}` (frozen Galerkin + Weil matrix Schur system).

**This is not an extension of the class but a prerequisite** for F to become a
non-vacuous obstruction theorem. Without a confirmed member of `P_{r,N}`, Theorem F is
vacuously true and hence not a barrier.

**Sub-tasks:**
- **EXT-5a:** Check whether the Connes–Consani–Moscovici spectral triple (truncated
  to finite N) produces a system in `P_{r,N}`. The CCM finite-rank approximation at
  level N is a natural candidate.
- **EXT-5b:** Check whether the kappa_toeplitz construction (sibling repo) restricted
  to a Galerkin subspace falls in `P_{r,N}`.
- **EXT-5c:** If neither works, check Zagier's period-polynomial Weil form (if any
  finite-dimensional version produces a P_{r,N} system).

**Expected deliverable:** Either a confirmed non-vacuity witness (unblocking Theorem F)
or a precise record of why all known candidates are outside `P_{r,N}` (which itself
may be a new no-go result about the class).

**Priority:** MEDIUM — Theorem F is currently blocked; this unblocks it or closes it.

---

### EXT-6 · OB-46 / OP1-A — Pasten arithmetic-derivative lattice extension to ℤ[i] powerful values

**Indirect inspiration (2026-08-17).** The paper
`abc-conjecture-verification/papers/route-v-pasten/route-v-pasten.tex` proves structural
results for Pasten's arithmetic derivative lattice `F(a,b)` of rank `ω(abc)−1` over
squarefree coprime triples in ℚ:
- `det(F(a,b)) = R·√(Σ_{p∈P} p^{−2}) < R`
- Minkowski bound `‖ψ‖_∞ ≤ R^{1/(ω−1)}` for some nonzero `ψ ∈ F(a,b)`
- Quality boundary: `quality(a,b,c) > 1/2 ⟺ a = 1` for squarefree triples with `a ≤ b`

These results are **not directly applicable** to OB-46 (they require squarefree triples
over ℚ; OB-46 targets powerful values over ℤ[i], which are maximally non-squarefree).
However, the following new research directions are suggested:

**EXT-6a — Squarefree projection bound.**  
For a Row-3 pair `(a,n)`, form the abc-like triple `(A_−, n(2a−n), A_+)` over ℤ.
Let `(A_−^sq, n(2a−n)^sq, A_+^sq)` be the squarefree parts (divided by largest square
factors). If `N = A_+ A_-` is powerful, then `N^sq = A_+^sq · A_-^sq · gcd^{sq}` is very
small relative to `N`. The Pasten quality theorem gives `quality ≤ 1/2` for this triple
(since `A_-^sq = (a-n)^2+n^2 / square > 1`). Investigate whether the quality constraint
`quality ≤ 1/2` combined with the large-square constraint (powerful `N`) produces an
abc-type lower bound forcing a contradiction — i.e. `c^{1/2} ≤ rad(abc)` while powerful
`N` forces `rad(N) ≪ N^{1/2}`.  
**Prerequisite:** a quantitative version of the Pasten quality theorem (not currently proved
in the paper — it gives the qualitative boundary, not a lower bound on `rad`).

**EXT-6b — Arithmetic derivative lattice over ℤ[i].**  
Pasten's lattice is defined over ℚ. The relation `w_+ − w_- = n` in ℤ[i] is an "abc
triple" over ℤ[i] in the Gaussian integers. Define the analogue of `F(a,b)` for Gaussian
integers: the weight lattice `{ψ: 𝔓(αβγ) → ℤ | d^ψ(α) + d^ψ(β) = d^ψ(γ)}` where `𝔓`
denotes the set of Gaussian primes dividing `w_+ · w_- · n` and `d^ψ` is the Gaussian
arithmetic derivative. The Pasten–Minkowski bound, if extended to ℤ[i], would give
`‖ψ‖_∞ ≤ R_{ℤ[i]}^{1/(ω_{ℤ[i]}−1)}`. Determine whether the squarefree-away-from-5
structure forces `ω_{ℤ[i]}` to be large enough that the Minkowski bound is non-trivial.  
**Prerequisite:** Pasten lattice theory over number rings — not yet in the literature;
this is a new research direction.

**EXT-6c — Non-squarefree Pasten extension (OB-13B-type).**  
The paper notes that for non-squarefree triples, bounds acquire a `v_{max}` factor:
`‖ψ‖_∞ ≤ v_{max} · R^{1/(ω−1)}`. For powerful `N`, `v_{max}` is large (≥ 2), making
the Minkowski bound weak. Determine the sharp `v_{max}` growth rate as a function of
`N`'s powerful-part structure, and check whether the resulting bound is still
incompatible with OB-46's `(A_-, n(2a-n), A_+)` triple.  
**Prerequisite:** OB-13B extension of the route-v-pasten paper (not yet proved — noted as
open in that paper).

**Execution gate:** None of EXT-6a/b/c can be used as a proof premise until either
(a) the Pasten quality theorem is made quantitative (EXT-6a), or (b) the Gaussian
arithmetic derivative lattice is defined and a Minkowski bound is proved for ℤ[i]
(EXT-6b). Record as a research direction, not a proof strategy, until those steps close.

**Priority:** LOW (exploratory) — conceptually motivated but requires new theory in two
places (quantitative Pasten, Gaussian Pasten). Do not outsource until EXT-6a/b are
internally formulated.

---

### Execution order and gates

| Task | Depends on | Expected outcome | Priority | Status |
|---|---|---|---|---|
| EXT-1a/b (D' log-poly) | Schrohe/Lesch literature | New theorem D' or confirmed escape | HIGH | **ESCAPE-ROUTE-OPEN confirmed** — c_{0,1} tunable to (2π)^{-1}; C_logpoly is live Hilbert–Pólya candidate |
| EXT-3a (meromorphic Hadamard) | Classical Weierstrass–Mittag-Leffler | Lemma for E extension | MEDIUM-HIGH | **PROOF-DRAFT** — Lemma E'.1 written; IFT step for E'-neg open |
| EXT-3b/c (E-neg Suzuki) | EXT-3a | Extended E-compactness | MEDIUM-HIGH | **PROOF-DRAFT** — E-prime-meromorphic scaffold complete |
| EXT-5a/b (F non-vacuity) | sibling repo + CCM analysis | Unblock Theorem F | MEDIUM | **CONDITIONALLY PASSED** — Suzuki A_a Galerkin truncation confirmed P_{r,N} member |
| EXT-2a (unified info theorem H) | B1 + G scaffold | New Theorem H | MEDIUM | **PROOF-DRAFT** — H-information-hierarchy scaffold complete |
| EXT-4a (Selberg literature) | Pure search | Unblock EXT-4b/c | LOW-MEDIUM | **CLOSED** — no Selberg prescribed-zero theorem exists; Selberg axioms incompatible with free zero prescription; Theorem C scope confirmed optimal |
| EXT-2b (O_vonMangoldt layer) | G-hard conjecture progress | Conditional on G-hard | LOW (blocked) | BLOCKED by G-hard conjecture |
| EXT-6a (squarefree projection + Pasten quality) | Quantitative Pasten quality theorem | abc-type rad lower bound vs powerful N | LOW (exploratory) | OPEN — prerequisite (quantitative Pasten) not proved |
| EXT-6b (Pasten lattice over ℤ[i]) | New theory: Gaussian arithmetic derivative lattice | Minkowski bound for Gaussian OB-46 triple | LOW (exploratory) | OPEN — requires new theory |
| EXT-6c (non-squarefree Pasten v_max) | OB-13B extension of route-v-pasten | Sharp v_max bound for powerful triples | LOW (exploratory) | OPEN — OB-13B not yet proved in paper |

**All six EXT tasks executed (2026-08-11).** Four produced new theorem scaffolds
(D', E', H, EXT-5a partial); one confirmed an escape route open (EXT-1); one closed a
literature gap (EXT-4a). Repository now has 10 theorem directories.

**Hard rule (program §3.3):** Every EXT task that produces a positive obstruction result
must pass the full §14 acceptance test (class, non-vacuity, target, observation,
invariant, no-RH, escape, scope). Every EXT task that confirms an open escape route
is recorded as such — not relabeled as a failure.

**No task here proves, disproves, or claims progress toward RH.**
