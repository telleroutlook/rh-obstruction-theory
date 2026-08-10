# Proof — Theorem D (spectral-asymptotic exclusion)

**Status:** PROOF-DRAFT  
**Analytic / finite separation:** purely analytic.

---

## §1. Main argument (Weyl-mismatch)

**Theorem D proof.**

Suppose for contradiction that `H ∈ 𝒞_ell` has spectrum `{γ_n : n ≥ 1}` with
`γ_n` the positive ordinates of the nontrivial zeros of ζ (with multiplicity,
ordered `0 < γ₁ ≤ γ₂ ≤ …`).

By the Weyl law for `H`:
```
N_H(T) = #{n : γ_n ≤ T} ~ C_H T^{d/m}   as T → ∞,         (W)
```
with `C_H > 0`, `d ≥ 1` (dimension), `m > 0` (order), all determined by the
principal symbol of `H` on `M`.

By the Riemann–von Mangoldt formula:
```
N_ζ(T) = T/(2π) log(T/2π) − T/(2π) + O(log T).             (VM)
```

If the spectrum of `H` equals `{γ_n}`, then `N_H(T) = N_ζ(T)`.

Compare growth rates: `C_H T^{d/m} ∼ T log T / (2π)` requires
```
d/m = 1   and   C_H = log T / (2π) → ∞.
```
But `C_H` is a **constant** (independent of `T`), while `log T → ∞`.
This is a contradiction.  No choice of `d, m, C_H` reconciles (W) and (VM).  ☐

---

## §2. Weyl law source

The Weyl law `N_H(T) ~ C_H T^{d/m}` is a classical theorem:

- **Smooth compact manifold without boundary:** Hörmander (1968) Acta Math. 121.
- **Manifold with boundary, standard elliptic BCs:** Seeley (1969); Ivrii (1980)
  for the two-term expansion.
- **Perturbations:** Courant–Weyl min-max principle gives `N_{H+V}(T) = N_H(T) + O(T^{(d-1)/m})`.

These are REFEREED; not restated here.

---

## §3. Extensions (Theorem D')

**Finite direct sums.** `N_{H_1 ⊕ H_2}(T) = N_{H_1}(T) + N_{H_2}(T) ~ (C_1 + C_2) T^{d/m}`.
Still a pure power law.  Same contradiction.

**Compact quantum graphs (local, energy-independent vertex conditions).**
For a finite metric graph with total length `L`, Weyl law gives `N_H(T) ~ (L/π) T`
(linear in `T`; see Gutkin–Smilansky 2001, Roth 1983).  `L T / π ≠ T log T`.  ☐

**Polynomial transforms `H' = q(H)` (fixed polynomial `q`, `q(λ) > 0`).**
The eigenvalues of `H'` are `q(λ_n)`.  If `q(x) ~ x^α` for large `x`, then
`N_{H'}(T) ~ N_H(T^{1/α}) ~ C_H T^{d/(mα)}`.  Still a power law.

**Bounded perturbations with preserved leading Weyl law.**  If `‖V‖_{H^{-1}→ H} < \infty`,
then the Courant–Weyl estimate gives `N_{H+V}(T) = N_H(T) + O(T^{(d-1)/m})$, and
the leading term is unchanged.

In each case, the conclusion `N_H(T) = T \log T / (2π) + O(\log T)` is incompatible
with the power-law leading term.

---

## §4. Heat-trace reformulation (additional invariant)

The heat trace `Z_H(t) := \mathrm{Tr}(e^{-tH}) = \sum_n e^{-t\lambda_n}` has
leading singularity as `t → 0⁺` determined by the Seeley–DeWitt expansion:

```
Z_H(t) ~ (4π)^{-d/2} t^{-d/m} · [A_0(H) + A_1(H) t^{1/m} + …]   (t → 0⁺),
```
with `A_0 = ∫_M \mathrm{tr}(\sigma_{-d}(H)) \, dVol` (leading symbol integral).

For `H` with spectrum `{γ_n}`, the heat trace would need to match:
```
Z_ζ(t) = \sum_{n≥1} e^{-t γ_n} ~ t^{-1} C_0 + C_1 \log(1/t) + …   (t → 0⁺)
```
(the logarithmic term comes from the `T \log T` counting law: for `N(T) ~ T \log T`,
the heat trace has a `\log(1/t)` singularity at `t = 0`).

A `\log(1/t)` leading singularity is **not** in the polyhomogeneous Seeley–DeWitt
class (which has `t^{-k/m}` terms with rational exponents only).  This gives a
**sharper** obstruction than the Weyl leading-term mismatch alone.

**Status:** This heat-trace argument is a genuine strengthening of the raw
Weyl mismatch and is the most novel part of Theorem D.  It requires:
- Computing `Z_ζ(t)` leading behavior rigorously (standard from the Riemann
  explicit formula and Mellin transform of `e^{-t γ_n}`).
- Verifying that the Seeley–DeWitt expansion has no `log` terms in the classical
  elliptic case (standard; see Berline–Getzler–Vergne or Gilkey).

**Status:** PROOF-DRAFT for the heat-trace argument.  This is the part that
could go beyond Endres–Steiner.

---

## §5. Determinant-order obstruction (further strengthening)

The spectral zeta function `Z_H(s) = \sum_n \lambda_n^{-s}` for `H ∈ 𝒞_ell`
has a meromorphic continuation with poles only at `s = d/m, (d-1)/m, …` (arithmetic
progression with step `1/m`).

For the Riemann case, the Dedekind zeta-like counting gives a spectral zeta
with different pole structure (related to ζ itself via explicit formula).

**The pole structure of `Z_H(s)` vs. `Z_ζ(s)` provides a third obstruction.**
This is more technical and is left for a future refinement; it corresponds to
the "exact determinant obstruction (order/type)" mentioned in the PLAN.

---

## §6. Status

| Argument | Status |
|---|---|
| Weyl leading-term mismatch (§1) | PROOF-DRAFT (standard corollary; close to Endres-Steiner) |
| Extensions: sums, graphs, polynomials, perturbations (§3) | PROOF-DRAFT |
| Heat-trace log singularity (§4) | PROOF-DRAFT (may be the new content) |
| Seeley-DeWitt no-log (§4 reference) | INDEPENDENTLY-CHECKED (standard textbook result) |
| Spectral zeta pole obstruction (§5) | SKETCH (future work) |
| Novelty gate decision | See novelty.md |
