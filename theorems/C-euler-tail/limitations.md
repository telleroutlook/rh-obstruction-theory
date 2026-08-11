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

**Scope honesty (OB-26 mod6 — narrowed).** Theorem C **neither constructs nor claims** a
Selberg-class member, and therefore **draws no conclusion** about the Selberg class, ζ, or
any combined "Euler product + gamma factor + functional equation" axiom class. The finite
Euler-factor ratio `R_a` does not preserve a functional equation, and completely
multiplicative unimodular coefficients do not supply a gamma factor — so the construction
simply does not reach these classes.

A stronger assertion — that a *prescribed-zero theorem for the Selberg class is provably
impossible* — is **plausible** (a functional equation forces `Re(s)=1/2` symmetry on the
completed function's zeros, obstructing Andersson-style free single-point prescription; cf.
Kaczorowski–Perelli structure theory) but is **NOT proved here and carries no precise
theorem/citation**, so it is recorded only as motivation, not as an established fact. The
escape route "full Selberg class" is therefore **genuinely open**: not breached by the
Andersson method, and not closed by any theorem in this repo.

## 2. Functional equation kept separate (program §8.C.2)

The Davenport–Heilbronn comparison (functional equation without Euler product
→ off-line zeros) and Theorem C (finite Euler factors → off-line zeros) are
**logically separate**.  They must not be combined into a claim that "both
axioms together still permit off-line zeros" — this would require a single
function violating both, which is NOT constructed here.

## 3. Andersson Gate A — CLEARED; whole-theorem Gate-A — PASS (OB-26)

The load-bearing Andersson dependency is **source-verified**: arXiv:2408.15713v1,
**Theorem 5** (LaTeX label `thm5`), checked against the source tarball in
`baseline/andersson-2408.15713/` (see `PROVENANCE.md`). The whole-theorem Gate-A review
(OB-26, 2026-08-11) returned **CONDITIONAL → PASS** after the mod1–mod6 textual fixes:
Links A–D and RH-non-circularity all CONFIRMED; target predicate redefined as `P_S` on the
open strip; the consequence restated (one-sided, plus the `R_a` all-fiber strengthening);
novelty downgraded to a **corollary of Andersson Theorem 5**. C is now INDEPENDENTLY-CHECKED
at that scope.

## 4. Per-`N`/one-sided scope; bounded region only

The theorem gives a zero at a chosen `z₁` in the open strip; it does not claim a zero with
RH-like density or a prescribed infinite sequence. The base consequence is **one-sided**
(`O=(1,…,1) ⇏ P_S=1`); the `R_a` version extends this to every realizable observation fiber
(no `O`-only condition true on some fiber is sufficient for `P_S=1`). A same-fiber `P_S=1`
companion is available via Andersson Corollary 3 but is not needed.

## 5. Novelty: corollary of Andersson Theorem 5 (Paper A remark), not standalone

OB-26 Q5 verdict: **option (a) — corollary.** The mathematical increment is Theorem 5 plus
a standard finite Euler-factor ratio and its one-line modulus argument. C should be
published as a **named corollary / remark in Paper A**, explicitly attributed to Andersson
Theorem 5 — **not** as a standalone note or standalone barrier. The quantified "finite
observation does not force the standard fiber" statement has expository value but is not a
materially broader zero-construction theorem.
