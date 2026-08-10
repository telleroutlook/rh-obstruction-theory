# Limitations — Theorem D (D-spectral-asymptotic)

**Theorem ID:** D-spectral-asymptotic

---

## 1. Classical compact elliptic class only

Theorem D applies to `𝒞_ell` and its declared extensions `𝒞_ell^+`.  It does
not exclude any operator outside this class.  The explicit escape class
(noncompact systems, infinite graphs, nonlocal symbols, energy-dependent BCs,
arithmetic/NCG) is listed in statement.md §Escape route.

## 2. Close to prior art (THIN risk)

The raw Weyl-mismatch argument is extremely close to Endres–Steiner (2010) for
compact quantum graphs, and to a standard corollary of the Weyl law for
pseudodifferential operators.  Theorem D is not a new result at this level.

**What might be genuinely new:**
- The heat-trace `log(1/t)` singularity obstruction (proof.md §4) — a sharper
  invariant class.
- The spectral zeta pole obstruction (proof.md §5, sketch only).

Until these are completed, Theorem D is a **reference note** or a **supporting
section**, not a standalone paper.

## 3. Not about RH — no RH hypothesis

Theorem D excludes a class of operators from realizing the zeta spectrum.  It
says nothing about whether RH is true or false, and uses no RH-equivalent among
its hypotheses.

## 4. Eigenvalue map vs. self-adjoint construction

The theorem requires H to have spectrum equal to `{γ_n}` (the positive zeta
ordinates).  An operator that merely approximates finitely many ordinates is
not excluded.

## 5. Escape example required

The program requires an explicit escape example outside `𝒞_ell` with `T log T`
counting.  The hyperbolic surface (Selberg trace formula) is noted in statement.md
as a candidate.  This must be made precise before Paper B is submitted.
