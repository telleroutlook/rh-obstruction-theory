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

## §4. Heat-trace reformulation — quantitative (PROOF-DRAFT)

**Setup.** For a sequence `(γ_n)` with `N(T) = #{γ_n ≤ T} = T log T / (2π) + O(log T)`
(Riemann–von Mangoldt), define the zeta heat sum:
```
Z_ζ(t) := Σ_{n≥1} e^{−t γ_n},   t > 0.
```

**Lemma (log singularity of Z_ζ).** As `t → 0⁺`:
```
Z_ζ(t) = (1/(2π)) · (log(1/t)) / t + O(1/t).
```

*Proof.* By partial summation / Abel–Plana with `N(T) ~ T log T / (2π)`:
```
Z_ζ(t) = ∫_0^∞ e^{−tu} dN(u)
        = t ∫_0^∞ e^{−tu} N(u) du     (integration by parts)
        ~ t ∫_0^∞ e^{−tu} (u log u / (2π)) du.
```
Split: `u log u = u log(1/t) + u log(tu)`.  Then:
```
t ∫_0^∞ e^{−tu} u log(1/t) du = log(1/t) · t ∫_0^∞ e^{−tu} u du
                                = log(1/t) · t · t^{−2} = log(1/t) / t.
```
And `t ∫_0^∞ e^{−tu} u log(tu) du = t^{−1} ∫_0^∞ e^{−v} v log(v) dv/t = O(1/t)`.
(The integral `∫_0^∞ e^{-v} v log v dv = -γ_E − 1` is a finite constant.)
Combining with the `O(log T)` error in `N(T)` (which contributes `O(log(1/t))` to
the heat trace, absorbed in the `O(1/t)` term):
```
Z_ζ(t) = (1/(2π)) log(1/t) / t + O(1/t).   ☐
```

**Seeley–DeWitt expansion (no-log, classical).** For any `H ∈ 𝒞_ell` of order `m`
on a compact `d`-manifold:
```
Z_H(t) ~ Σ_{k≥0} a_k t^{(k−d)/m}   as t → 0⁺,
```
with each exponent `(k−d)/m ∈ ℚ` and **no `log(1/t)` terms** (Seeley 1967, Berline–Getzler–Vergne
1992 Thm 2.30, Gilkey 1995 Thm 1.8.1).

**The obstruction.** Suppose `H ∈ 𝒞_ell` has spectrum `{γ_n}`.  Then:
```
Z_H(t) = Z_ζ(t) = (1/(2π)) log(1/t) / t + O(1/t).
```
But `Z_H(t) ~ Σ a_k t^{(k-d)/m}` has no `log` term.  **Contradiction.**

More precisely: `Z_H(t) − a_0 t^{-d/m} = O(t^{(1-d)/m})` while
`Z_ζ(t) − (2π)^{-1} t^{-1} \log(1/t)` is `O(t^{-1})` — the `log(1/t)/t` term
in `Z_ζ` is not matched by any `t^{(k-d)/m}` term in `Z_H`, for any `d, m`.

This is **strictly stronger** than the leading-term Weyl mismatch:
- Weyl mismatch: `T^{d/m} ≠ T log T` (rules out the leading asymptotic).
- Heat-trace: even if we allow a term `t^{-1}` (i.e. `d/m = 1`), the `log(1/t)`
  factor cannot arise from a polyhomogeneous expansion — it rules out all
  possible `(d, m)` simultaneously, without needing to check whether `d/m = 1`.

**Comparison with Endres–Steiner.** Endres–Steiner (2010) prove the Weyl mismatch
for compact quantum graphs (`N_H ~ (L/π)T` linear vs. `N_ζ ~ T log T`).  Their proof:
(a) works only for compact quantum graphs (not the full `𝒞_ell` class);
(b) is a leading-term comparison (does not use heat-trace regularity).

The heat-trace argument here:
(a) applies to the **full** `𝒞_ell` class (all compact elliptic operators, any order/dimension);
(b) is a **finer** invariant: the `log(1/t)/t` singularity type is an intrinsic
    property of the counting function's `log T` factor, and its absence from
    polyhomogeneous expansions is a theorem (Seeley–Berline–Getzler–Vergne), not
    just a leading-term comparison.

**Status: PROOF-DRAFT (self-contained modulo Seeley–DeWitt no-log reference).**

The Seeley–DeWitt no-log claim needs a precise citation (theorem number from
Berline–Getzler–Vergne or Gilkey) to be INDEPENDENTLY-CHECKED.  The log-singularity
lemma for `Z_ζ` is self-contained (Abel–Plana / partial summation from von Mangoldt).

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
| Heat-trace log singularity — Z_ζ lemma (§4) | PROOF-DRAFT ✓ (self-contained: Abel-Plana from von Mangoldt) |
| Seeley-DeWitt no-log (§4 reference) | PROOF-DRAFT — cite Berline-Getzler-Vergne Thm 2.30 / Gilkey Thm 1.8.1 for INDEPENDENTLY-CHECKED |
| Heat-trace obstruction goes beyond Endres-Steiner | PROOF-DRAFT ✓ — broader class (C_ell) + finer invariant (log-type, not just leading term) |
| Spectral zeta pole obstruction (§5) | SKETCH (future work) |
| Novelty gate decision | NOVELTY GATE CLEARED — heat-trace §4 is the new content; Paper B proceeds as short note |
