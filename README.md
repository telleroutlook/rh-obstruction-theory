# RH Obstruction Theory

A research program to prove **exact boundary theorems** about classes of proof strategies
for the Riemann Hypothesis — *what precisely defined methods cannot see* — rather than to
prove or disprove RH.

> **Status:** research program, pre-theorem. This repository does **not** prove,
> disprove, or claim progress toward the Riemann Hypothesis. RH is `[OUT]` and is never
> self-declared here.

## What "obstruction" means here

Two theorem kinds are in scope:

1. **Information obstruction** — a method sees only an observation map `O`; two admissible
   objects with *different* zero-location behavior produce the *same* observation, so no
   `O`-local rule can decide critical-line support on the ambient class.
2. **Structural obstruction** — every candidate in a precisely defined operator /
   certificate class carries an invariant incompatible with the invariant an exact RH
   realization would require.

A theorem is called a **barrier** only when the method class, ambient class, observation
map, target predicate, **and** an escape route are all explicit. An RH-*equivalent*
criterion is **not** a barrier — proving it would simply prove RH.

## Why this framing (the correction that produced it)

An earlier draft proposed a universal "`c_L`-margin barrier": that a growing Weil-constant
shift bounds the certifiable margin of a whole method class. That is unsound as stated —
a certificate margin (pivot, Schur residual, scalar shift) is **not invariant** under
rescaling / congruence / preconditioning. The representation-invariant quantity is the
lowest Rayleigh quotient `λ(a)` of the localized Weil form. In it, the same `log(1/a)`
scale that looked like a *negative* shift is in fact the *positive* term carrying
small-`a` positivity (Suzuki 2026, Thm 1.4). The program therefore treats `c_a` as a
diagnostic inside one frozen certificate system, and attacks instead the boundaries that
current (2025–2026) constructions genuinely leave open.

## Portfolio

| Paper | Working title | Priority |
|---|---|---|
| **C** | Real-Rooted Approximants and the Missing Compactness Theorem in Spectral Approaches to RH | primary |
| **A** | Finite Observables Do Not Determine Critical-Line Support | primary, conditional on exact-collision |
| **B** | Spectral-Asymptotic Exclusions for Classical Hilbert–Pólya Candidates | conditional on novelty |
| **D** | Lower Bounds for a Restricted Schur-Certificate System for Local Weil Positivity | exploratory |

See `PLAN.md` for phases and gates, `spec/PROGRAM.md` for the authoritative program.

## Baseline (verified from source)

The program builds on current constructions, each checked against its arXiv source in
`baseline/` by theorem number:

- **M. Suzuki**, *Weil's quadratic form via the screw function*, arXiv:2606.09096 (2026) —
  lowest eigenvalue `λ(a)`: continuous (Thm 1.3), positive+simple for small `a` (Thm 1.4);
  entire real-zero characteristic function `W(a,θ;z)` (Thm 1.5); RH iff a uniform limit
  to the meromorphic `z²ξ/ξ'` holds (Cor 6).
- **A. Connes, C. Consani, H. Moscovici**, *Zeta Spectral Triples*, arXiv:2511.22755 (2025) —
  finite operators with `det_reg(𝔇−z) = −i λ^{−iz} ξ̂(z)`; open step = normalized
  determinants → `Ξ`.

## Layout

```
spec/PROGRAM.md    authoritative program (v2.0)
baseline/          source-verified reference literature + exact conventions
theorems/<id>/     one directory per theorem: statement, dependencies, proof, witness, checker, limitations, novelty
discovery/         untrusted exploration (never imported by proofs/checkers)
checker/           independent interval/exact-arithmetic checkers
domain/            proofctl domain adapter (per-theorem evidence gates)
schemas/ tests/ docs/ pilots/
```

## Verification

Five layers, one-directional promotion: discovery (untrusted) → analytic (human proofs) →
certificate generator (untrusted) → independent checker (exact/interval replay) →
governance (proofctl domain derives status). Every claim carries a **two-axis evidence
level** (mathematical × computational); a DOI is archival, not peer review; a finite
certificate never validates the analytic bridge that produced it.

## License / privacy

Private repository. No personal absolute paths, company names, or internal network hosts
appear in any file.

---

*This repository is engineering infrastructure for honest negative and boundary results.
Its value is an auditable boundary around RH proof strategies — not a solution to RH.*
