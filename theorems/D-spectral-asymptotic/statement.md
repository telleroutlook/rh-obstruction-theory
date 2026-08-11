# Theorem D — Spectral-Asymptotic Exclusions for Classical Hilbert–Pólya Candidates

**Mathematical status:** PROOF-DRAFT (conditional on novelty gate)  
**Computational status:** INDEPENDENT-CHECKER (Z_ζ side: OB-19 external review 2026-08-11 — exact closed form Z_ζ,main(t)=(1/2πt)(log(1/t)−γ_E−log2π), leading coeff exactly 1/2π, symbolic + 110-digit replay; operator side remains analytic-only)  
**Theorem ID:** D-spectral-asymptotic  
**Program ref:** §9 (WP-D), §9.D.1–D.5  
**Paper target:** Paper B (conditional on novelty beyond Endres–Steiner)

---

## Setting

**Classical compact elliptic class `𝒞_ell`.**  An operator `H` belongs to
`𝒞_ell` if:

1. `H` is a positive elliptic pseudodifferential operator of order `m > 0` on a
   compact smooth `d`-dimensional Riemannian manifold `(M, g)` (with smooth
   boundary and standard elliptic boundary conditions if `∂M ≠ ∅`).
2. `H` has discrete spectrum `0 < λ₁ ≤ λ₂ ≤ …` (compact resolvent).
3. The perturbation class `ℙ(H)` consists of operators `H + V` where `V` is
   relatively compact with respect to `H` and preserves the leading Weyl law.

**Weyl law for `H ∈ 𝒞_ell`:**

```
N_H(T) := #{n : λ_n ≤ T} ~ C_H · T^{d/m}   as  T → ∞,
```

where `C_H = Vol(M) · ω_d / (2π)^d` (leading Weyl constant, from the principal
symbol; `ω_d` = volume of the unit ball in `ℝ^d`).  This is a **power law**.

**Zeta counting function:**

```
N_ζ(T) = #{ρ = 1/2 + iγ : 0 < γ ≤ T}
        = T/(2π) · log(T/2π) − T/(2π) + O(log T).
```

This is **`T log T`**, not a power law.

**Target predicate:**

```
P(H) = 1  ⟺  the spectrum of H (eigenvalues with multiplicity) equals
               {γ_n : n ≥ 1}  (positive ordinates of nontrivial ζ zeros).
```

---

## Theorem D (spectral-asymptotic exclusion)

**Theorem D.** No operator `H ∈ 𝒞_ell` has its spectrum equal to the set of
positive imaginary parts of nontrivial zeros of `ζ` (with multiplicity).

**Proof.** By the Weyl law, `N_H(T) ~ C_H T^{d/m}` for some `d, m > 0` and
`C_H > 0`.  If `H` had spectrum `{γ_n}`, then `N_H(T) = N_ζ(T) ~ T log T / 2π`.
But `T log T` is not of the form `C T^{d/m}` for any constants `C, d, m > 0` —
the logarithmic correction `log T` is not a power.  Contradiction.  ☐

**Scope:** the class `𝒞_ell` is named; the conclusion is vacuous outside this class.

---

## Extensions (Theorem D')

Let `𝒞_ell^+` be the extended class, adding:

- Finite direct sums of compact elliptic operators: `N_{H_1 ⊕ H_2}(T) = N_{H_1}(T) + N_{H_2}(T) ~ C T^{d/m}` still a power law.
- Compact or relatively bounded perturbations preserving the leading counting law:
  `N_{H+V}(T) = N_H(T) + O(T^{(d-1)/m})` (Courant–Weyl perturbation theory),
  still `~ C T^{d/m}`.
- Compact quantum graphs with local energy-independent vertex conditions:
  `N_H(T) ~ (L/π) T` (linear, not `T log T`) — excluded by the same argument.
- Fixed polynomial transforms `H' = p(H)`: `N_{H'}(T) ~ C T^{d/(m \cdot \deg p)}` — power law, excluded.

**Theorem D' (extended class).** No operator in `𝒞_ell^+` has spectrum `{γ_n}`.

---

## Escape route (explicit, program §9.D.4)

The theorem does not exclude:

1. **Noncompact or infinite-volume systems** with renormalized traces (e.g.,
   scattering operators, operators on `ℝ` or `ℝ^+`).
2. **Infinite quantum graphs** (Weyl law can have `T log T` corrections for
   infinite graphs).
3. **Nonlocal or log-polyhomogeneous symbols** (leading singularity of the heat
   trace can be `t^{-1} log(1/t)` instead of purely polyhomogeneous).
4. **Energy-dependent boundary conditions** (Krein–Langer / Pontryagin space).
5. **Arithmetic / noncommutative geometries** (Connes' trace formula, Bost–Connes
   system — outside the classical elliptic calculus).
6. **Schrödinger operators on ℝ with growing potential:** `H = −d²/dx² + V(x)`
   on `ℝ` with `V(x) → ∞` can have `N_H(T) ~ C T^{1/2}` (Lieb–Thirring) or
   other sub-power-law behavior; more exotic growth is possible.

An **escape example with `T log T`:** The Laplacian on a hyperbolic surface
of finite area (but cusp geometry, non-compact) has `N_H(T) ~ (Area/4π) T`
for the continuous spectrum contribution plus discrete eigenvalues — but the
total counting including continuous spectrum satisfies a `T log T` law from the
Selberg trace formula.  This is an explicit operator outside `𝒞_ell` (non-compact
manifold) with the correct leading law.

---

## Novelty gate (program §9.D.5)

**Prior art:** Endres–Steiner (J. Phys. A 43 (2010), 095204) prove a specific
no-go theorem for Berry–Keating operators on compact quantum graphs via Weyl
asymptotics.  This is the closest prior result.

**Theorem D is THIN** if it only restates the Weyl mismatch.  It is new only if:
- it provides a sharper invariant (not just Weyl leading term but also the
  next-order term or the heat-trace singularity class);
- it covers a materially broader class (e.g., the full Seeley–DeWitt expansion);
- it provides an exact determinant obstruction (order/type of the spectral
  determinant, not just eigenvalue counting).

**Current assessment:** Theorem D as stated is a standard Weyl-mismatch corollary,
very close to what Endres–Steiner already proved.  The program requires a novelty
gate before Paper B is pursued.  See novelty.md for the decision.
