# Limitations — Theorem E (E-compactness)

**Theorem ID:** E-compactness  
**Program ref:** §10.E, §3.3, §10.E.3

---

## 1. CCM entire target only — Suzuki meromorphic target excluded

This theorem is stated and proved in the **CCM normalization** (entire target
`Ξ`).  The Suzuki normalization target `z² ξ/ξ'` is **meromorphic** (poles at
the zeros of `ξ`); the Hurwitz theorem does not apply to meromorphic limits.

For the Suzuki target, a separate pole/residue version is needed (program
§10.E.3): convergence of the reciprocal `1/F_N → ξ'/(z² ξ)`, or a
Rouché/argument-principle count on contours avoiding the poles.  This is a
genuine technical obligation NOT covered by E-compactness as stated.

**Consequence:** The escape theorem (E-pos) applies to CCM-like entire-function
sequences only.  Claiming E-pos for the Suzuki target requires a separate proof.

## 2. Condition (7) weakened in the basic E-neg

The basic E-neg construction (proof.md §2) does not enforce Taylor-coefficient
agreement beyond `j = 0` (normalization).  Enforcing finitely many Taylor
coefficients requires additional free parameters (proof.md §2 "Refinement").
The full E-neg with conditions 1–7 is a stronger result and is marked OPEN in
proof.md §3.

## 3. Quantitative non-convergence estimate open

The proof-draft E-neg establishes non-uniqueness (two sequences converging to
different limits) but does not yet give a quantitative lower bound
`|F_N − Ξ|_{|z|≤R} ≥ ε > 0` for a single sequence.  This is the goal of
proof.md §3 and is still OPEN.

## 4. Not a proof that no sequence can converge

E-neg shows that the finite evidence record **alone** is insufficient.
It does NOT show that **no** sequence satisfying `ℰ_N` converges to `Ξ`.
In fact, the CCM sequence `det_reg(𝔇_{λ,N} − z)` is conjectured (and
numerically supported) to converge after suitable normalization.  The theorem
says the normalization step is load-bearing — not that convergence is impossible.

## 5. Not about RH

The positive theorem (E-pos) says: IF (H-bound) + (H-tail), THEN convergence +
real zeros.  This is a conditional statement.  The condition (H-tail) is not
proved for the CCM sequence.  The theorem does not claim to prove RH or any
RH-equivalent.

## 6. Identification step uses Hadamard uniqueness

The identification `G = Ξ` in E-pos uses the Hadamard factorization uniqueness
theorem (an entire function of order 1 is determined by its zeros + normalization
up to a factor `e^{az+b}`).  The two conditions `G(z_0) = Ξ(z_0)` (from H-norm)
and evenness pin the remaining freedom.  If `Ξ` were not order 1, a different
argument would be needed.
