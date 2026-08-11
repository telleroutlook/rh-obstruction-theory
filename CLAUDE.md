# CLAUDE.md — RH Obstruction Theory

## Project identity

This repository executes the research program in `spec/PROGRAM.md` (= the frozen v2.0
plan): **prove several exact boundary / no-go theorems about classes of RH proof
strategies**, not to prove or disprove RH itself.

Two theorem kinds are in scope:
1. **information obstructions** — a precisely defined method sees only an observation
   map `O`, while two admissible objects with different zero-location behavior share the
   same observation;
2. **structural obstructions** — every candidate in a precisely defined operator /
   certificate class has an invariant incompatible with the invariant an exact RH
   realization would need.

**Mathematical status:** research program. No theorem here proves, disproves, or claims
to be "near" RH. RH is `[OUT]`, never self-declared.

`spec/PROGRAM.md` is authoritative on mathematics. This file wins on process. Where the
program and a convenient shortcut conflict, the program wins.

---

## The one hard boundary: an RH-equivalence is NOT a barrier

An RH-equivalent criterion (`C ⟺ RH`) **locates** difficulty; it does not prove
impossibility. A theorem may be called a *barrier* only when **all five** are explicit:
method class, ambient object class, observation map, target predicate, escape route.

The minimum success is **one non-vacuous no-go theorem for one natural, externally
recognizable class.** The following are explicitly **not** success (program §3.3, §17):

1. another RH-equivalent reformulation;
2. finite failure of one sufficient inequality at fixed parameters;
3. a margin tending to zero (strictly positive quantities can → 0 and stay provable);
4. a synthetic off-line configuration outside the declared ambient class;
5. a negative literature search (novelty signal, not a theorem);
6. machine-verified finite arithmetic without a proved analytic bridge;
7. a broad "RH conserves difficulty" philosophical claim.

If a result reduces to one of these, it is labeled as such and **not** marketed as a barrier.

---

## Representation-invariance discipline (the correction that motivated v2.0)

A scalar shift (`−c_a I`), a raw pivot, a matrix eigenvalue in an unnormalized basis, or
a Schur residual is **not** a method-class invariant — it changes under rescaling,
congruence, and preconditioning. **The default margin is the generalized Rayleigh
quotient `λ(a)` relative to a fixed Hilbert / Gram norm** (Suzuki's lowest eigenvalue of
the localized Weil form). Any alternative margin must *prove* its invariance under every
transformation the method class allows, or it is a case-study diagnostic only.

Documented precedent this matters: Suzuki Thm 1.4 gives `λ(a) = log(1/a) + const + O(a)`
as `a→0⁺` — the same `log` scale that read as a *negative* shift `−c_L` in an
unnormalized Schur decomposition is the *positive* leading term carrying small-`a`
positivity in the invariant. Same scale, opposite effect. Never promote a `−c_a`
observation past a frozen-system diagnosis without reconciling it with `λ(a)`.

---

## Baseline literature is load-bearing — verify from source, never from memory

The program stands on 2025–2026 constructions. **Every cited theorem used as a premise
must be checked against the arXiv source (`baseline/`), by theorem number, before it
supports any claim here.** Verified so far (source-checked, tarballs in `baseline/`):

- **Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096** (2026-06-08):
  Thm 1.3 `λ(a)` continuous; Thm 1.4 `λ(a)` positive+simple for small `a`, even
  eigenfunction, `λ(a)=log(1/a)+μ₁−log(2π)+ψ(2)−1+O(a)`; Thm 1.5 `W(a,θ;z)` entire, all
  zeros real, = operator spectrum; **Cor 6**: RH follows *if*
  `e^{φ(a,z)}W(a,θ;z) → z²ξ(1/2−iz)/ξ'(1/2−iz)` uniformly on compacts. Target is
  **meromorphic** (poles at the zeros).
- **Connes–Consani–Moscovici, *Zeta Spectral Triples*, arXiv:2511.22755** (2025-11-27):
  `det_reg(𝔇 − z) = −i λ^{−iz} ξ̂(z)` (entire target, all zeros real = spectrum);
  open step = "suitably normalized" determinants → Riemann `Ξ`. The `λ^{−iz}` phase
  **preserves zeros but not the locally uniform limit** — "suitably normalized" is
  load-bearing (a normalization trap for the convergence track).

Suzuki (`ξ/ξ'`, meromorphic) and CCM (`ξ̂`/`Ξ`, entire) are **distinct normalizations**;
never conflate them. Hurwitz real-zero transfer is automatic only for the entire target;
the Suzuki meromorphic target needs a pole/residue (reciprocal / argument-principle) version.

---

## Two-axis evidence ledger (program §6.A.2) — non-negotiable

Every imported or produced claim carries **both** a mathematical and a computational status.

| Axis | Allowed values |
|---|---|
| Mathematical | `DEFINITION`, `CONJECTURE`, `PROOF-DRAFT`, `INDEPENDENTLY-CHECKED`, `REFEREED` |
| Computational | `NONE`, `EXPLORATORY`, `REPRODUCIBLE`, `INDEPENDENT-CHECKER`, `FORMALIZED` |

- A repository deposit / DOI is **archival publication, not peer review.**
- "Lean-ready" is **not** "Lean-formalized."
- A finite Arb certificate validates only the finite statement replayed — never the
  analytic theorem that produced the finite object.
- Status is **derived by the checker**, never self-declared by a generator or editor.

No private or machine-verified result enters a published theorem as an established
premise until Gate A closes (statement + analytic proof + normalization + witness
independently inspectable), or it is restated as an explicit assumption.

---

## Acceptance tests every claimed barrier must pass (program §14)

Formal: **class** (membership checkable), **non-vacuity** (a serious published
construction is in the class), **target** (the two adversaries genuinely differ on the
predicate), **observation** (equality is exact, not numerical coincidence), **invariant**
(obstruction survives all allowed equivalences), **no-RH** (no RH / RH-equivalent among
hypotheses), **escape** (an explicit route outside the class), **scope** (conclusion
names ambient class + resource bound).

Computational: exact rational / interval replay; independent reconstruction from raw
data; precision-escalation + conditioning report; adversarial mutation of every witness
field; deterministic offline checker; cross-implementation agreement on ≥1 nontrivial
instance.

---

## Repository layout

```
spec/PROGRAM.md         Authoritative frozen program (v2.0). Math wins here.
baseline/               Source-verified reference literature (arXiv tarballs +
                        REFERENCE_BASELINE.md exact defs/conventions; Suzuki a/Q_W^a/λ(a) baseline).
theorems/<id>/          One directory per theorem (program §12.2):
    statement.md          all quantifiers + definitions
    dependencies.yaml     two-axis evidence level per dependency
    proof.md              analytic steps SEPARATED from finite steps
    witness/              raw data, not producer summaries
    checker/              independent replay path
    limitations.md        the exact non-conclusions
    novelty.md            theorem vs prior art
discovery/              Untrusted: floats, zero tables, heuristic fitting. Conjectures only.
                        NEVER imported by theorems/*/checker or by any proof step.
checker/                Independent checkers (interval / exact arithmetic, stdlib).
domain/                 proofctl domain adapter: policy + contracts (evidence gates, not CORE gates).
schemas/                JSON Schemas (additionalProperties:false).
tests/                  Regression + adversarial suite (mutation of every rejection condition).
docs/                   Architecture, methodology, handoff (HANDOFF.md gitignored).
pilots/                 Replayed finite certificates (JSON).
```

---

## proofctl integration (this repo is a proofctl DOMAIN, not a fork)

proofctl lives at `~/github/proofctl` (Go, `github.com/telleroutlook/proofctl`); binary
not on PATH — `go build ./cmd/proofctl` and `./cmd/proofverify` there. **Reuse, do not
re-implement:** status state machine, acyclic-DAG check, import policy, forbidden-input
audit, offline replay (`cmd/proofverify`), claim/attestation schemas. Domain specifics
live only in `domain/policy-v2.json` + `domain/contracts/*.json`, modeled on
`~/github/proofctl/domains/weil/` and the AASVS sibling repo. proofctl `internal/` stays
domain-agnostic; kernel changes go upstream with their own tests.

Unlike the AASVS sibling (which gates a single RH-implying certificate via CORE-0..5),
this domain gates **per-theorem evidence**: each `theorems/<id>` must satisfy the §14
acceptance tests, and its status is `BLOCKED` if any analytic dependency is missing or
any premise is above its inspected evidence level.

---

## Engineering conventions (inherited, hard-won)

- **Long computations (>30s):** observable (`flush=True` progress lines), pausable
  (catch `KeyboardInterrupt`, checkpoint to `pilots/<ts>-<label>.checkpoint.json`),
  resumable (`--resume`). For blocking long runs use
  `~/.local/bin/run_and_wait.sh -t <sec> -- <cmd>`.
- **Certified bounds:** interval arithmetic, outward rounding (`python-flint`/Arb).
  `mpmath`/floats are discovery-tier only.
- **Verify load-bearing claims by script, not memory** — identities, bounds, sign facts,
  and especially every cited baseline theorem (against `baseline/` source).
- **Type annotations required** in `checker/` and any `theorems/*/checker`.
- **Commit messages in English.** `git status` before commit. Never stage `discovery/`
  outputs as theorem witnesses. Certificates enter only after independent replay.
- **No PASS self-report anywhere.** Status is the checker's output.
- **Privacy:** no personal absolute paths, company names, or internal hosts in any file
  (proxy/host may appear only in a shell command, never written to a file).

## Outsource-prompt pre-send checklist (mandatory)

Before sending any `outsource/` problem, self-check these failure modes (each has
already caused a rejected/rewritten prompt). Verify load-bearing claims with a quick
script, not from memory.

0. **Run `outsource/PROMPT_LINT.md` on every new or edited prompt before it ships** —
   the standing adversarial checklist built from every past audit (OB-01..13): order ≠
   exponential type, target parity from the functional equation, zero-vs-pole role,
   canonical-product genus, RH-imported-via-divisor, vacuous real atoms, counting-law
   factors, global observation map, growth-derived-not-assumed, power-sum ≠ jet, dropped
   frozen terms, discrepancy-degree parity, Fredholm zero locations, per-n ≠ uniform
   bound (+ envelope must match the target's type: conventional-order r^{1+ε}, not linear
   finite-type), zeros-in-Ω ≠ zeros-in-ℂ, representation-invariance/measure-collapse,
   Fourier-multiplier-on-ℝ has continuous spectrum (discrete/trace-class needs a compact
   manifold or ℓ² model), cross-theorem Σ′/normalization convention (never paste a δ/C/d
   numeric anchor between theorems — B1 R-atom vs B2 R-symm differ by ×2), cited
   black-box exact-number-and-scope, script-verified anchors, honest inconclusive
   verdict. Each item is a check you actually RUN (script/grep/derivation). When a
   referee surfaces a new defect class, add it to the lint and **re-scan every active
   prompt AND every `theorems/*/statement.md|proof.md`** — the defect is never assumed
   independent.

1. **No vacuous target.** The goal must not be satisfiable by inflating a free
   parameter. Pin comparison scales to a fixed arithmetic quantity (e.g. `o(log λ)`,
   not `o(g(N))` with free `N`); cap schedules (`N_j ≤ λ^A`).

2. **No dropped term.** Any assembly/reduction identity you state must be numerically
   verified end-to-end. Watch boundary terms (`S_τ→2‖f‖²` as `τ→0`, not 0) and coupling
   terms (2×2 block bound keeps `η`: `b=(ℓ+h−√((h−ℓ)²+4η²))/2`, positive iff
   `η²<(ℓ−u)(h−u)`).

3. **Cite only what is proved.** Label each "black box" with its proof source
   (`Problem NN`, verified); confirm it actually covers the object used. `PLAN.md`
   statuses can be stale — trust the verified `solutions/` note.

4. **No false dichotomy.** If offering "prove X / prove obstruction", also allow an
   honest "inconclusive + precise partial localization" outcome.

5. **Self-contained.** Every symbol defined in-file; inline full formulas (`r''`, `H_n`,
   `V_{00}`, constants like `R_L`), not just point values. No "see other file".
   Any numerical anchor labeled "sanity only, not an input" and verified by script.

### Minimum outsource file structure

```
# Problem OB-NN — Short title

**Type:** [pure analysis / combinatorics / PDE / etc.]
**Non-circularity:** [explicit statement that RH, zero locations, fitted ordinates are
  not assumed — or explanation of why this problem does not touch RH at all]

## All definitions (self-contained — everything is here)
[Every symbol defined, every formula written out in full]

## The theorem / claim to be verified
[Complete statement]

## Proof skeleton to be closed
### Step 1 — [name]
[Draft with "What to close for Step 1:" subsection]
### Step 2 — ...

## Acceptance criteria
[Numbered list; allow CONFIRMED / PARTIAL / REFUTED / inconclusive outcomes]

## Numerical anchor (sanity only)
[One concrete computable example the reviewer can sanity-check]
```

---

## What this repository does NOT do

- Does not prove, disprove, or claim progress toward RH. Titles/abstracts must not imply it.
- Does not label an RH-equivalence, a fixed-parameter failure, or a margin→0 as a barrier.
- Does not promote a representation-dependent margin (`−c_a`) to a universal claim.
- Does not treat a finite Arb certificate as validation of its analytic bridge.
- Does not use a private/unrefereed result as an established premise past Gate A.
