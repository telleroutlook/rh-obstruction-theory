# STATUS — RH Obstruction Theory (single source of truth)

**Last updated:** 2026-08-12 (after the OB-20..OB-32 Gate-A review round; all returned and
integrated). Tests: 86 passing. This file summarizes the *independently-reviewed* status of
every theorem. Per-theorem `statement.md` / `dependencies.yaml` remain authoritative; this is
the index.

**Reading the status.** Every theorem carries two axes (program §6.A.2): **mathematical**
{DEFINITION, CONJECTURE, PROOF-DRAFT, INDEPENDENTLY-CHECKED, REFEREED} and **computational**
{NONE, EXPLORATORY, REPRODUCIBLE, INDEPENDENT-CHECKER, FORMALIZED}. "Gate-A" = whole-theorem
independent mathematical review; status is the reviewer's verdict, never self-declared.

---

## Summary table

| Theorem | Math axis | Comp axis | Gate-A verdict | One-line |
|---|---|---|---|---|
| **B1**-finite-inequality | INDEPENDENTLY-CHECKED | INDEPENDENT-CHECKER | **PASS** (OB-23, after §7 mods) | no uniform separation margin; R-atom Σ′; checker `b1_ratom_certified_checker.py` |
| **B2**-exact-collision | INDEPENDENTLY-CHECKED | INDEPENDENT-CHECKER | **PASS** (OB-20) | exact Li-value collision; checker `b2_certified_checker.py` (OB-21/OB-13) |
| **G**-fredholm-certificate (G-info) | INDEPENDENTLY-CHECKED | INDEPENDENT-CHECKER | **PASS** (OB-22, 7 mods) | diagonal `G_d ≠ Ξ̂`; checker `diagonal_fredholm_interval_replay.py` (OB-17); G-hard stays CONJECTURE |
| **D**-spectral-asymptotic | INDEPENDENTLY-CHECKED | INDEPENDENT-CHECKER (Z_ζ side) | **PASS** (OB-25, 8 mods) | heat-trace leading-log for `𝒞_ell`; **positioned as scope-extension / corollary**, not standalone novelty |
| **C**-euler-tail | INDEPENDENTLY-CHECKED | N/A (analytic existence) | **PASS** (OB-26, mod1–6) | Helson finite-Euler non-forcing; **one-sided corollary of Andersson Thm 5** |
| **E**-compactness | PROOF-DRAFT | NONE | **BLOCKED** (OB-29) | `Ξ`-specific RH-free claim is circular (RH-via-divisor); survives as an abstract Laguerre–Pólya lemma |
| **E'**-prime-meromorphic | PROOF-DRAFT | NONE | **BLOCKED** (OB-30) | degree `z^{2J+3}` wrong; (A2) false for real `ξ/ξ'`; Suzuki entire ⇒ moving-pole incompatible; abstract lemma survives |
| **D'**-prime-logpoly | ESCAPE-ROUTE-REFINED | NONE | **BLOCKED** (OB-31) | Claim A universal false (needs ellipticity); narrowed to `𝒞_logpoly^{sub,ell}` (PENDING); B/C/D-analytic/E confirmed |
| **H**-information-hierarchy | PROOF-DRAFT | — | **BLOCKED** (OB-32) | ordinates-only oracle refuted own arrow; literal `O_theta` constant ⇒ comparable; incomparability NOT established |
| **F**-schur-complexity | REFUTED (as a complexity bound) | — | (OB-12) | retired; Schur-certificate complexity collapses; only a spectral-margin statement survives — **not a barrier** |
| E-prime / D-prime tables above supersede EXT scaffolds | | | | |

**Established (survived whole-theorem Gate-A): B1, B2, G-info, D, C** — five theorems. Four of
these (B1, B2, G, D) are double-axis (math + computational checker); C is analytic-existence
so has no finite certificate.

---

## Gate-A verdict history (OB-20 … OB-32)

- **PASS:** OB-20 (B2), OB-22 (G, conditional→7 mods), OB-23 (B1, conditional→§7 mods),
  OB-25 (D, conditional→8 mods), OB-26 (C, conditional→6 mods).
- **BLOCKED:** OB-29 (E), OB-30 (E'), OB-31 (D'), OB-32 (H).
- Computational checkers: OB-21/OB-13 (B2), OB-24/OB-18 (B1), OB-17 (G), OB-19 (D Z_ζ side).

**Discipline note.** The five PASSes all began as CONDITIONAL and required integrating real
corrections (Σ′ convention, citation numbers, normalization, scope). The four BLOCKs are
genuine: each package treated per-fragment-confirmed parts as whole-theorem-correct, but the
combination / definition-consistency / universal quantifier / numerical anchor had errors the
whole-theorem review caught. No theorem advanced by self-declaration.

---

## Minimal-repair path for each BLOCKED theorem (what a resend needs)

- **E (OB-29):** retarget away from `Ξ`. Either (Path B) state everything over an abstract
  Laguerre–Pólya `L` (RH-free, done in statement.md §0/§1' — this is a supporting lemma), or
  (Path C) prove a genuinely `Ξ`-specific RH-free finite-real-zero interpolation/realization
  theorem (substantial new math; not implied by `Ξ`'s genus or known critical-line zeros).
- **E' (OB-30):** (1) replace the fixed `z^{2J+3}` separation with "some nonzero Taylor
  coefficient of order ≥3" + a Cauchy bound at that degree; (2) keep (A1)–(A3) as *abstract*
  hypotheses (they cannot hold for the real `ξ/ξ'`), and drop the Suzuki-target claim (Suzuki
  is entire; moving poles are incompatible). Result is an abstract odd-meromorphic lemma.
- **D' (OB-31):** re-run the lemma over the narrowed `𝒞_logpoly^{sub,ell}` (positive elliptic
  classical principal symbol + strictly-lower-order finite log; reviewer gave the class def +
  Hörmander 1968 Thm 1.1 route). Rename `LEADING-SINGULARITY-COVERS-SUBPRINCIPAL-LOGPOLY`
  (already done); it stays PENDING until re-reviewed. Claims B/C/D-analytic/E already hold.
- **H (OB-32):** (1) define `O_oracle = 𝒵` (full multiset — done); (2) define a *nonconstant*
  `O_theta` (e.g. sampled counts `N_𝒵(d_m)` at fixed levels) and supply an **exact**
  same-`O_finite`/different-`O_theta` witness (the `ker DF` sketch is only first-order); (3)
  call it a refinement *preorder*, not a lattice. Then incomparability H'(i) could be re-attempted.

---

## What this repository does NOT claim (unchanged; program §3.3, §17)

No theorem here proves, disproves, or claims progress toward RH. The established results are
**no-go / obstruction theorems** for specific method classes; the BLOCKED items are honestly
recorded as such, and F is retired as a non-barrier. RH is `[OUT]`.
