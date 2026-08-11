# Limitations — Theorem C (C-euler-tail)

**Theorem ID:** C-euler-tail

---

## 1. Helson class only — not Selberg class or ζ

Theorem C applies within the Helson class (|χ(p)| = 1, completely
multiplicative, Euler product).  It says nothing about:

- The **Selberg class** (Euler product + functional equation + Ramanujan +
  Euler product of degree-d L-functions with bounded conductor growth).
- **ζ itself**: the Riemann zeta function has an Euler product, a specific
  gamma factor, analytic continuation to all of ℂ, a functional equation
  `ξ(s) = ξ(1−s)`, and Dirichlet coefficients `a(n) = 1`. None of these
  are in the Helson class axioms.

**Theorem C must not be advertised as showing that finitely many Euler
factors of ζ cannot detect its zeros.**

**EXT-4a audit (2026-08-11): Selberg class extension is provably blocked.**
A "prescribed-zero theorem for the Selberg class" does not exist in the literature
and is incompatible with the Selberg axioms:
- The functional equation forces Re(s)=1/2 symmetry on zeros; arbitrary Z not realizable.
- The Euler product + Ramanujan condition ties zero density to N(T) ~ (d/2π)T log T.
- Kaczorowski-Perelli structure theory shows S is too rigid for free zero prescription.
- Such a theorem would likely require resolving GRH-equivalent inverse problems.

The escape route "full Selberg class" in Theorem C's statement is confirmed
**genuinely open and currently unbreachable by the Andersson construction method**.
Theorem C's scope at the Helson class is correct and optimal for this approach.

## 2. Functional equation kept separate (program §8.C.2)

The Davenport–Heilbronn comparison (functional equation without Euler product
→ off-line zeros) and Theorem C (finite Euler factors → off-line zeros) are
**logically separate**.  They must not be combined into a claim that "both
axioms together still permit off-line zeros" — this would require a single
function violating both, which is NOT constructed here.

## 3. Andersson Gate A — CLEARED

The load-bearing Andersson dependency is **source-verified**: arXiv:2408.15713,
**Theorem 5** (LaTeX label `thm5`), transcribed and checked against the source tarball
in `baseline/andersson-2408.15713/` (see `PROVENANCE.md` there and dependencies.yaml).
Theorem C is therefore **PROOF-DRAFT** (no longer CONDITIONAL on the citation). The
remaining gate is a whole-theorem Gate-A mathematical review (OB-26), which also decides
the novelty question in §5.

## 4. Prescribed zeros in a bounded region only

The statement gives a zero in a specific region `Ω`.  It does not claim a zero
with RH-like density or a prescribed infinite sequence of zeros.

## 5. Novelty: likely a section of Paper A, not standalone

Per LITERATURE_MATRIX.md, Theorem C is OPEN-ish: standalone only if it adds
a materially new refinement to Andersson.  If Andersson's result already implies
the finite-Euler conclusion directly, Theorem C becomes a one-paragraph corollary
and should be published as a section of Paper A (or a short note).
