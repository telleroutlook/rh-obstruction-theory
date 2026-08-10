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
