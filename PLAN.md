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

**All six EXT tasks executed (2026-08-11).** Four produced new theorem scaffolds
(D', E', H, EXT-5a partial); one confirmed an escape route open (EXT-1); one closed a
literature gap (EXT-4a). Repository now has 10 theorem directories.

**Hard rule (program §3.3):** Every EXT task that produces a positive obstruction result
must pass the full §14 acceptance test (class, non-vacuity, target, observation,
invariant, no-RH, escape, scope). Every EXT task that confirms an open escape route
is recorded as such — not relabeled as a failure.

**No task here proves, disproves, or claims progress toward RH.**
