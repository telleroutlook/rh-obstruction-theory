# Limitations — Theorem B1

**Theorem ID:** B1-finite-inequality  
**Program ref:** §7.B.3, §7.B.4 (fail-fast tests), §3.3

This file records exactly what Theorem B1 does **not** conclude.  Readers and
checkers must verify that no published version exceeds these stated limitations.

---

## 1. Fixed finite order only

B1 applies to a **fixed** finite family `Φ = (φ₁, …, φ_m)` with `m` fixed.  It
does not exclude:

- a method using all `K → ∞` Li inequalities (full Li criterion);
- a method using all Weil test functions (the full Weil criterion);
- a method using arbitrarily many Hausdorff–Stieltjes moments;
- any method with an adaptive stopping rule based on online data.

**Title and abstract must not imply failure of an unbounded hierarchy.**

## 2. No Euler product, gamma factor, or functional equation

The ambient class `𝔛_sym` requires only conjugation + FE symmetry + convergence
exponent.  Members of `𝔛_sym` need not have:

- an Euler product factorization;
- an exact gamma factor;
- coefficient arithmetic (integers, multiplicativity);
- analytic continuation of the associated Dirichlet series outside the half-plane.

The escape routes in `statement.md` §Escape identify these as the additional
structure that an unrestricted B1 adversary lacks.

## 3. No counting-law requirement on `𝒵_−`

The constructed `𝒵_− = 𝒵_+ ∪ Q(σ₀, T_*)` adds 4 points to `𝒵_+`.  If `𝒵_+`
had a von Mangoldt counting law, `𝒵_−` now has an `O(1)` perturbation of it.
B1 does not claim that `𝒵_−` has an exact Riemann–von Mangoldt law; such a claim
would require the B2 compensating construction (on-line atoms at `T_*`).

## 4. No exact-collision claim

B1 produces `𝒵_−` with `|O_j(𝒵_−) − O_j(𝒵_+)| < ε_j`, not
`O_Φ(𝒵_−) = O_Φ(𝒵_+)`.  An exact collision (zero tolerance) requires B2.

## 5. Not about ζ directly

`𝒵_+` can be taken as the formal zero multiset of ζ, but the theorem says
nothing about proofs that use the Euler product of ζ, its functional equation,
or the analytic structure of the Riemann ξ function beyond symmetry.

## 6. Not a proof of complexity of Li/Weil criteria

B1 does not imply that the Li criterion is computationally hard, unprovable, or
"conserves difficulty."  It is a single-level information obstruction: a fixed
window cannot distinguish support.

## 7. Weil-test convention choice

The proof uses **Convention W2** (evaluation at imaginary parts) for Weil-type
tests.  Under Convention W1 (direct evaluation at complex point `ρ`), the Weil
test `ĥ(ρ)` grows exponentially in `|Im ρ|` for `Re(ρ) ≠ 0`, making the quartet
contribution large for large `T` — this would require a different construction or
a restricted subclass of `h_j`.  This is recorded as an open refinement; the B1
theorem is stated for W2.
