# Theorem C — Finite Euler Factors Do Not Force Critical-Line Zeros

**Mathematical status:** PROOF-DRAFT (conditional on Andersson + finite-Euler modification)  
**Computational status:** NONE  
**Theorem ID:** C-euler-tail  
**Program ref:** §8 (WP-C), §8.C.1–C.4  
**Paper target:** Paper A (supporting section) or standalone if materially new

---

## Setting

**Helson zeta functions.**  For a completely multiplicative function `χ: ℕ → ℂ`
with `|χ(p)| = 1` for all primes `p`, define:

```
ζ_χ(s) = Π_p (1 − χ(p) p^{-s})^{-1}   (formal Euler product),
```

with meromorphic continuation to some region (Helson class; see Andersson 2024).

**Finite prime cutoff.**  Fix `P₀ > 0`.  Say `χ` is **`P₀`-standard** if
`χ(p) = 1` for all primes `p ≤ P₀` (agrees with the Riemann ζ on the first
`π(P₀)` Euler factors).

**Target predicate:**
```
P(ζ_χ) = 1  ⟺  all nontrivial zeros of ζ_χ in the continuation region
                 lie on the critical line Re(s) = 1/2.
```

---

## Theorem C (finite Euler factors ⇏ critical-line zeros)

**Theorem C.** For every finite prime cutoff `P₀` and every bounded region
`Ω ⊂ {0 < Re(s) < 1}` with suitable boundary, there exists a Helson zeta function
`ζ_χ` with `χ` being `P₀`-standard such that `ζ_χ` has a prescribed off-critical-line
zero in `Ω`.

**Consequence:** No criterion depending only on the first `π(P₀)` Euler factors
can force all zeros of a Helson zeta function to lie on the critical line.

**Method.**  The proof reduces to Andersson's prescribed-zero theorem
(arXiv:2408.15713) for Helson zeta functions, plus a finite-Euler-factor
modification argument.

---

## Proof strategy (PROOF-DRAFT)

**Step 1 (Andersson's theorem).** By Andersson (2024), for any prescribed finite
set of desired zeros `z₁, …, z_k ∈ {0 < Re(s) < 1} \ {1/2}` in the continuation
region, there exists a Helson zeta function `ζ_χ` (with `|χ(p)| = 1`) that has
zeros at `z₁, …, z_k`.

**Step 2 (Finite-factor modification).** Given such `ζ_χ`, define
`ζ_χ̃ := ζ_χ · Π_{p ≤ P₀} (1 − χ̃(p) p^{-s}) / (1 − χ(p) p^{-s})`
where `χ̃(p) = 1` for `p ≤ P₀`.  This replaces the first `π(P₀)` Euler factors
with the standard ones.

The finite-factor ratio `R(s) = Π_{p ≤ P₀} (1 − p^{-s}) / (1 − χ(p) p^{-s})`
is a Dirichlet polynomial (finite product, holomorphic and nonzero on a region
that excludes the zeros and poles of the factors).

**Step 3 (Zero preservation).** The zeros of `ζ_χ̃ = ζ_χ · R` include:
- The zeros of `ζ_χ` that are not zeros of `1/R` (the original prescribed zeros,
  if `R(z_j) ≠ 0`).
- The zeros of `R` (known, bounded, from the Dirichlet polynomial part).

**Critical issue:** The factor `R(s)` may vanish at or near the prescribed zeros
`z_j`, canceling them.  This requires showing `R(z_j) ≠ 0` for the chosen `z_j`.

**Resolution:** Choose `z_j` in a region where the Dirichlet polynomial
`R(s) = Π_{p ≤ P₀} [(1 − p^{-s}) / (1 − χ(p) p^{-s})]` is bounded away from zero.
Since `R` is an explicit finite Dirichlet polynomial of degree `≤ P₀^{1/2}`, its
zeros are finitely many and explicitly bounded.  For `Im(z_j)` sufficiently large
(or in a suitable region), `|R(z_j)| ≥ c > 0` is guaranteed by standard Dirichlet
polynomial bounds.

**Step 4 (P₀-standardness).** By construction, `χ̃(p) = 1` for `p ≤ P₀`, so
`ζ_χ̃` is `P₀`-standard.  It has the prescribed off-line zeros (with the caveat of Step 3).

---

## Open items

| Item | Status |
|---|---|
| Andersson Thm verified by theorem number | PENDING (source not in baseline/) |
| Finite-Euler-factor zero preservation (Step 3) | PROOF-DRAFT — standard Dirichlet polynomial zero-free region argument |
| Scope: Helson class only | STATED — does not apply to Selberg class or ζ |
| Novelty check (standalone vs. lemma of A) | OPEN — see novelty.md |

---

## Escape route

The theorem applies to the Helson class.  It does NOT apply to:

1. **Selberg class:** functional equation + Euler product with additional axioms
   not present in the Helson class.
2. **ζ itself:** the exact Euler factors of ζ, the gamma factor, and the
   functional equation jointly constrain the zero set in ways the Helson class
   does not replicate.
3. **Combined axioms:** a method using both Euler product for `p ≤ P₀` AND
   the functional equation AND gamma factor may still force critical-line zeros
   in a larger class.

The escape route is: any proof using the full Selberg-class axioms (or ζ-specific
structure) is not limited by Theorem C.
