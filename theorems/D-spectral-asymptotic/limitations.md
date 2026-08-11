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

**What is genuinely new (corrected 2026-08-11):**

The **corrected** §4 argument (leading-singularity obstruction via Mellin inversion)
is the new content.  Specifically:

- The leading pole of `ζ_H(s) = Tr(H^{-s})` at `s = d/m > 0` cannot coincide with
  a pole of `Γ(s)` (since `d, m > 0` implies `d/m > 0`, while `Γ` poles are at
  non-positive integers).  Therefore Mellin inversion gives a *simple* pole at `s = d/m`,
  producing a pure power `t^{-d/m}`, never `t^{-d/m}·log(1/t)`.
- This argument applies to the **full** `𝒞_ell` class (all positive classical elliptic
  pseudodifferential operators, any order/dimension), using Grubb–Seeley 1995 Thm 2.7 /
  Lesch 1999 Theorem 3.7 — not limited to differential operators.

**What is NOT new (retracted 2026-08-11):**

The *all-orders no-log* claim (previous §4) was refuted by external review (OB-01).
The reviewer provided an explicit counterexample: on `S¹`, the classical elliptic
multiplier `He_n = (|n| + a/|n|)e_n` has `Z_H(t) = 2/t − 2a·t·log(1/t) + O(t)`,
violating the all-orders no-log claim.  The BGV Thm 2.30 and Gilkey Lemma 1.8.2
citations were scope-limited to differential operators only and did not support the
wider pseudodifferential claim.

The heat-trace `log(1/t)/t` obstruction is present but relies only on the *leading*
singularity (the corrected argument), not on absence of logs at all orders.

Until proof.md §5 (spectral zeta pole obstruction) is completed, Theorem D is a
**reference note** or a **supporting section**, not a standalone paper.

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
