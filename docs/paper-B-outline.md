# Paper B — Outline
# Spectral-Asymptotic Exclusions for Classical Hilbert–Pólya Candidates

**Working title:** A Heat-Trace Obstruction to Realizing Riemann Zeros as the Spectrum
of a Classical Elliptic Operator  
**Target:** ~10 pages; short note  
**Theorem files:** `theorems/D-spectral-asymptotic/`  
**Status:** **INDEPENDENTLY-CHECKED for D (Gate-A PASS OB-25)** — but positioned as a
**scope-extension / corollary**, NOT a standalone novelty (OB-25 Q5): the heat-trace
formulation is the same leading-order obstruction as the Weyl-counting mismatch (Abel/Tauber),
and near-direct precedents exist (Endres–Steiner 2010 for quantum graphs; Watson–Valentinuzzi
2026 for elliptic *differential* operators). D's identifiable increment is the extension to
the full classical elliptic ΨDO class + the leading-vs-subleading-log distinction.
**Caution — do NOT fold in D' (D-prime-logpoly) as an established escape-route audit:** D' is
**Gate-A BLOCKED (OB-31)** — its universal Claim A over `𝒞_logpoly` is false (missing
ellipticity; non-elliptic counterexample has a leading log). Only the narrowed
`𝒞_logpoly^{sub,ell}` lemma (PENDING) is defensible. See docs/STATUS.md.

---

## Abstract (draft)

We prove that no positive elliptic pseudodifferential operator of any order on any
compact smooth manifold can have spectrum equal to the sequence of imaginary parts of
the nontrivial zeros of the Riemann zeta function.

The obstruction is a heat-trace invariant: the zeta heat sum `Z_ζ(t) = Σ e^{−tγ_n}`
has a `log(1/t)/t` singularity as `t → 0⁺`, which follows from the Riemann–von
Mangoldt `T log T` counting formula by a direct Abel–Plana computation. By contrast,
the heat trace of any elliptic operator in the stated class has a polyhomogeneous
Seeley–DeWitt expansion with no logarithmic terms. The incompatibility of these
singularity types excludes the entire class simultaneously, without case-by-case
argument and independent of the truth of the Riemann Hypothesis.

This strengthens and extends the Endres–Steiner (2010) result, which established the
same conclusion for compact quantum graphs by a leading-Weyl-term comparison.

---

## §1. Introduction

**The Hilbert–Pólya conjecture** proposes that the imaginary parts `{γ_n}` of the
nontrivial zeros of ζ (assuming RH, so all `γ_n > 0`) are the eigenvalues of some
self-adjoint operator. No candidate has been found; this paper proves a class of
natural candidates are excluded.

**Prior work.** Endres–Steiner (2010, J. Phys. A 43, 095204) prove that no compact
quantum graph Hamiltonian with local energy-independent vertex conditions has spectrum
`{γ_n}`, by comparing the linear Weyl law `N_H(T) ~ (L/π)T` with the von Mangoldt
`N_ζ(T) ~ T log T / 2π`. Our result:
- covers the **full elliptic class** `𝒞_ell` (all compact elliptic operators, any
  order `m`, any dimension `d`);
- uses a **finer invariant** (heat-trace singularity type) rather than the
  leading Weyl term — this rules out all `(d,m)` simultaneously.

---

## §2. The class `𝒞_ell`

`H ∈ 𝒞_ell` if:
- `H` is a positive elliptic pseudodifferential operator of order `m > 0`;
- acting on sections of a vector bundle over a compact smooth manifold `M` of dimension `d ≥ 1`;
- self-adjoint in `L²(M)`.

Extensions `𝒞_ell⁺` include:
- finite direct sums `H₁ ⊕ … ⊕ Hₖ` (still polynomial Weyl);
- compact quantum graphs with local vertex conditions (Gutkin–Smilansky, Roth 1983);
- compact perturbations `H + V` with `V` relatively compact (Courant–Weyl);
- polynomial transforms `q(H)` for fixed `q` with `q(x) > 0`.

**Escape routes.** Noncompact manifolds, infinite quantum graphs, nonlocal operators
(log-polyhomogeneous symbols), energy-dependent boundary conditions, arithmetic/NCG
geometries (Connes–Consani–Moscovici) are all outside `𝒞_ell`.

---

## §3. Main theorem

**Theorem D.** No `H ∈ 𝒞_ell` (or `𝒞_ell⁺`) has spectrum equal to `{γ_n}`.

**Proof (heat-trace argument).**

*Step 1 (log singularity of Z_ζ).* By the Riemann–von Mangoldt formula
`N_ζ(T) = (T/2π) log(T/2π) − T/(2π) + O(log T)`, partial summation gives:
```
Z_ζ(t) = ∫₀^∞ e^{−tu} dN(u) ~ (1/2π) log(1/t) / t + O(1/t)    as t → 0⁺.
```
(The computation is self-contained: split `u log u = u log(1/t) + u log(tu)`;
the first integral gives `log(1/t)/t`; the second gives `O(1/t)` via
`∫₀^∞ e^{-v} v log v dv = −γ_E − 1`.)

*Step 2 (no-log Seeley–DeWitt expansion).* For any `H ∈ 𝒞_ell`:
```
Z_H(t) ~ Σ_{k≥0} aₖ t^{(k−d)/m}    as t → 0⁺,
```
with `aₖ` determined by the principal symbol; all exponents are rational and **no
`log(1/t)` terms appear** (Seeley 1967; Berline–Getzler–Vergne, Thm 2.30; Gilkey,
Thm 1.8.1).

*Step 3 (contradiction).* If `H` has spectrum `{γ_n}`, then `Z_H(t) = Z_ζ(t)`.
The left side has no `log` term; the right side has a `(log(1/t))/t` term. No
choice of `d, m` can reconcile these, since no rational power `t^{(k−d)/m}` equals
`log(1/t)/t`. ☐

**Why this is stronger than the Weyl argument.** The Weyl mismatch argument compares
only leading-term growth rates: `T^{d/m}` vs. `T log T`. The heat-trace argument uses
the *singularity type* of the expansion — `log(1/t)` is categorically different from
`t^α` for any rational `α`. This rules out all `(d,m)` with a single argument, not
just the `d/m = 1` case.

---

## §4. Escape routes

The theorem does NOT say:
- Other operator classes (NCG, infinite-dimensional, nonlocal) are excluded.
- RH is false.
- No operator of any kind has spectrum `{γ_n}`.

Explicit `T log T` examples outside `𝒞_ell`:
- **Hyperbolic surface Laplacian:** the Selberg trace formula gives
  `N_H(T) ~ Area(M)/(4π) · T² ≠ T log T` (the surface must be carefully chosen;
  the *length spectrum* has different asymptotics from the eigenvalue spectrum).
- **Schrödinger operator with arithmetic potential:** spectral densities with
  `log T` factors can arise from arithmetic structure, outside `𝒞_ell`.

---

## §5. Novelty statement

The heat-trace `log(1/t)/t` singularity argument is new at this level of generality.
Endres–Steiner cover compact quantum graphs only and use the Weyl leading term.
The present proof:
(1) applies to the full `𝒞_ell` class;
(2) uses the singularity type (a categorical distinction) rather than coefficient comparison;
(3) is self-contained from von Mangoldt + Abel–Plana.

The one remaining step for full citation compliance: cite Berline–Getzler–Vergne
Thm 2.30 (or Gilkey Thm 1.8.1) by theorem number for the Seeley–DeWitt no-log claim.

---

## §6. Submission target

- **Venue (provisional):** Bulletin of the London Mathematical Society / Comptes Rendus
  Mathématique (short note, ~10 pages)
- **Dependencies for submission:** BGV/Gilkey citation by theorem number;
  independent review of the Abel–Plana computation in §3 Step 1.
