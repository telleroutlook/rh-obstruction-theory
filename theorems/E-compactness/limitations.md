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

## 2. Condition (7) is enforced by the IFT construction (not weakened)

The fixed-`N` witness (proof.md §3) matches the first `J_N` even Taylor coefficients
**exactly**, via the log-power-sum system `Φ_r(u,c)=0` (`r=1,…,J_N`) solved by the implicit
function theorem — so conditions 1–7 of `ℰ_N` all hold. (An earlier draft used a
hand-picked `δ_n=c/n` tail that only handled `j=0`; that sketch was abandoned — see
proof.md §2 for why summable hand-picked perturbations self-defeat.)

## 3. E-neg is a per-`N` statement, quantitatively CONFIRMED (not open)

The quantitative lower bound `sup_{|z|≤R_N}|F − Ξ| ≥ ε_N` for a record-respecting `F`
(fixed `N`, `R_N ≥ 2γ_{k_N+1}`) is **CONFIRMED** (OB-03 external review, 2026-08-11), via
the exact Vandermonde Jacobian and a Cauchy coefficient estimate on the first unmatched
log-power-sum. It is a **per-`N` non-identifiability** result and uses **no** `N→∞` passage.

## 4. Not a claim that a sequence fails to converge (per-`N`, like B1's "no uniform margin")

E-neg shows the finite record `ℰ_N` **alone** does not identify `Ξ` within its fiber, for
each `N`. It does **NOT** assert that some particular sequence `(F_N)` fails to converge
locally uniformly — the witness discrepancy sits at radius `R_N ≥ 2γ_{k_N+1} → ∞`, so it is
consistent with locally-uniform convergence on every fixed compact (this is exactly why the
positive package E-pos is not in conflict). Nor does it show that **no** sequence converges:
the CCM sequence `det_reg(𝔇_{λ,N} − z)` is conjectured (numerically supported) to converge
after suitable normalization. The theorem says the normalization/tail-control step is
load-bearing — not that convergence is impossible. (This mirrors B1's "no uniform separation
margin," and keeps E-neg clear of the "margin → 0" non-barrier label: the claim is a
per-`N` fiber non-identifiability, not a shrinking positive margin.)

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
