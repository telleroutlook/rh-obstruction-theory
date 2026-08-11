# Theorem D — Spectral-Asymptotic Exclusions for Classical Hilbert–Pólya Candidates

**Mathematical status:** INDEPENDENTLY-CHECKED (Gate-A: OB-25 2026-08-11 — math chain,
RH-non-circularity, and Lesch scope CONFIRMED; verdict CONDITIONAL→PASS after its 8 textual
mods were integrated. Positioned as a **scope-extension / corollary**, not standalone
novelty — see novelty.md)  
**Computational status:** INDEPENDENT-CHECKER (Z_ζ side: OB-19 external review 2026-08-11 — exact closed form Z_ζ,main(t)=(1/2πt)(log(1/t)−γ_E−log2π), leading coeff exactly 1/2π, symbolic + 110-digit replay; operator side remains analytic-only)  
**Theorem ID:** D-spectral-asymptotic  
**Program ref:** §9 (WP-D), §9.D.1–D.5  
**Paper target:** Paper B (as a scope-extension/corollary — ΨDO-class + leading-vs-subleading-log increment over Endres–Steiner / Watson–Valentinuzzi)

---

## Setting

**Classical compact elliptic class `𝒞_ell`.**  An operator `H` belongs to
`𝒞_ell` if:

1. `H` is a **strictly positive, self-adjoint, classical (polyhomogeneous) elliptic**
   pseudodifferential operator of order `m > 0` acting on `L²(M)`, where `M` is a
   **closed** (compact, boundaryless) smooth Riemannian manifold of dimension `d ≥ 1`.
   (For a finite-rank Hermitian bundle `E → M`, read `L²(M;E)`; Lesch's expansion covers
   this version, and the Weyl citation then needs its bundle/system form. The audited
   statement is the scalar `L²(M)` case.)
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
N_ζ(T) := Σ_{ρ: ζ(ρ)=0, 0<Re ρ<1, 0<Im ρ ≤ T} m(ρ)
        = T/(2π) · log(T/2π) − T/(2π) + O(log T),
```

the multiplicity-counted number of nontrivial zeros with imaginary part in `(0, T]`
(Riemann–von Mangoldt; Titchmarsh–Heath-Brown 2nd ed. Thm 9.4). This is **`T log T`**,
not a power law. No assumption is placed on `Re ρ`.

**Target predicate:**

```
Γ_ζ^+ := ⨆_{ρ: ζ(ρ)=0, 0<Re ρ<1, Im ρ>0} {Im ρ}^{m(ρ)}      (multiset, with multiplicity),

P(H) = 1  ⟺  spec(H) = Γ_ζ^+  as multisets.
```

Here `Im ρ ∈ ℝ` by definition; **no condition is imposed on `Re ρ`, and RH is not
assumed** (RH would be the statement `Re ρ = 1/2`, which is never used).

---

## Theorem D (spectral-asymptotic exclusion)

**Theorem D.** No operator `H ∈ 𝒞_ell` has `spec(H) = Γ_ζ^+` (the multiset of positive
imaginary parts of nontrivial zeros of `ζ`, with multiplicity). Equivalently `P(H) = 0`
for all `H ∈ 𝒞_ell`. The conclusion is unconditional (RH is neither assumed nor used).

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

**Theorem D' (extended class).** No operator in `𝒞_ell^+` has spectrum `Γ_ζ^+`.

---

## Escape route (explicit, program §9.D.4)

**Scope (OB-25 mod 8).** Theorem D excludes **only** strictly positive, self-adjoint,
finite positive-order, classical polyhomogeneous, **elliptic** ΨDOs on **closed**
positive-dimensional smooth manifolds. It does **not** exclude nonelliptic, hypoelliptic,
anisotropic, nonclassical / log-polyhomogeneous, noncompact, boundary, singular, or
quantum-graph models, nor an abstract self-adjoint operator with compact resolvent (any
positive sequence `λ_n → ∞` is realizable as a diagonal operator on `ℓ²`), nor a nonclassical
functional-calculus model engineered to give `N(T) ~ T log T`. It makes **no** assertion
about RH. In detail, the theorem does not exclude:

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

**Prior art.**
- **Endres–Steiner** (J. Phys. A 43 (2010), 095204), **Theorems 15.4–15.6**: a Weyl-law
  no-go for the two Berry–Keating families `H_BK`, `H_BK²` on **compact metric graphs**
  (not all compact quantum-graph operators; graphs are not closed smooth manifolds).
- **Watson–Valentinuzzi** (Bull. Sci. Math. 211 (2026), 103824; arXiv:2604.00052),
  **Thm 1.4 / Prop 6.2 / Thm 7.2**: a closely related leading-log obstruction for elliptic
  **differential** operators on compact manifolds, via a Tauberian
  `N(λ)~λL(λ) ⟹ Θ(t)~t⁻¹L(1/t)` argument. (Disclosed as a near-direct precedent; **not**
  imported — its accessible arXiv v1 uses two-sided `|γ|≤T` counting with the one-sided
  `1/2π` coefficient and RH-style `1/2+iγ_n` phrasing, so it is not a clean RH-free source.)

**Verdict (OB-25 Q5): scope-extension / corollary, not standalone novelty.**
Within `𝒞_ell` the heat-trace and Weyl-counting formulations are the **same**
leading-order obstruction in two languages (Abel/Tauber transform of the counting measure;
see proof.md §4), so the heat-trace argument is not "stronger". D's honest, identifiable
increment over the prior art is:
- extending the exclusion from elliptic **differential** operators (Watson–Valentinuzzi)
  and quantum graphs (Endres–Steiner) to the **full classical elliptic ΨDO class** on a
  closed manifold, via Lesch's `Tr(A e^{-tP})` expansion (Thm 3.7); and
- cleanly separating the **impossible leading** `t^{-d/m}log(1/t)` from **permissible
  subleading** `t^k log t` (`k≥1`, from `Wres(H^k)≠0`).

**Positioning:** D is a correct classical-ΨDO **scope-extension / corollary**, suitable as
a proposition/appendix/short note inside a larger paper — **not** marketed as an
otherwise-unprecedented standalone obstruction. See novelty.md for the full decision. (A
finite literature search cannot prove global novelty; this only records that D's current
positive claim is the scope increment, with the 2026 precedent disclosed.)
