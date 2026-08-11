# Theorem C — Finite Euler Factors Do Not Force Critical-Line Zeros

**Mathematical status:** PROOF-DRAFT (Andersson Thm 5 dependency source-verified /
Gate-A CLEARED; whole-theorem Gate-A review pending: OB-26)  
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
`ζ_χ̃ := ζ_χ · R(s)` with the finite-factor **ratio of Euler factors**
```
R(s) := Π_{p ≤ P₀} (1 − χ(p) p^{-s}) / (1 − p^{-s})       (χ̃(p) = 1 for p ≤ P₀),
```
which replaces the first `π(P₀)` Euler factors of `ζ_χ` by the standard ones
`(1 − p^{-s})^{-1}` (see proof.md §1 for the telescoping; verify by cancelling
`ζ_χ`'s own `p ≤ P₀` factors). Note the orientation: `R = Π L_p(s,1)/L_p(s,χ) =
Π (1 − χ(p)p^{-s})/(1 − p^{-s})` — the numerator carries `χ(p)`. `R` is a **ratio
of two finite Euler products**, meromorphic on `ℂ`; it is NOT a Dirichlet
polynomial (the denominator `(1 − p^{-s})` is inverted), so no "degree `≤ P₀^{1/2}`"
statement applies.

**Step 3 (Zero preservation — no cancellation possible).** Every factor of `R` has
its zeros (from `1 − χ(p)p^{-s} = 0`) and poles (from `1 − p^{-s} = 0`) on the line
`Re(s) = 0`, since `|χ(p)| = 1` forces `p^{-s} = χ(p)` or `p^{-s} = 1` to have
`Re(s) = 0` (see proof.md §3). Hence **`R` is holomorphic and nowhere zero on the
entire open strip `0 < Re(s) < 1`**. Therefore, for the prescribed `z_j` in the open
strip, `R(z_j) ≠ 0` **automatically** — there is no "critical issue" and no need to
push `Im(z_j)` large. The zero `z_j` of `ζ_χ` is preserved exactly in `ζ_χ̃`.

**Step 4 (P₀-standardness).** By construction, `χ̃(p) = 1` for `p ≤ P₀`, so
`ζ_χ̃` is `P₀`-standard, and it retains the prescribed off-line zero(s) `z_j`
(Step 3, unconditionally in the open strip). Moreover `ζ_χ̃` is itself a Helson
zeta function (its coefficient `χ̃` is completely multiplicative and unimodular:
`χ̃(p) = 1` for `p ≤ P₀`, `= χ(p)` for `p > P₀`), so `P(ζ_χ̃)` is well-defined and
equals `0`.

---

## Open items

| Item | Status |
|---|---|
| Andersson Thm verified by theorem number | CLEARED — Theorem 5 (LaTeX label `thm5`), source-verified in `baseline/andersson-2408.15713/` |
| Finite-Euler-factor zero preservation (Step 3) | PROOF-DRAFT — `R` holomorphic and zero-free on the whole open strip (zeros/poles on `Re(s)=0`); no "critical issue" |
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
