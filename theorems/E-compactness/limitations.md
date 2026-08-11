# Limitations — Theorem E (E-compactness)

**Theorem ID:** E-compactness  
**Program ref:** §10.E, §3.3, §10.E.3

---

## 0. GATE-A BLOCKED for the `Ξ`-specific RH-free claim (OB-29, 2026-08-11) — primary limitation

The independent Gate-A review **BLOCKED** the submitted theorem. The `Ξ`-specific, RH-free
claim is **circular** (PROMPT_LINT L5, RH-imported-via-divisor):

- **E-neg.** Matching the log-power-sums `P_r(F_c) = P_r(Ξ)` requires
  `Ξ(z) = Ξ(0)∏_{n≥1}(1 − z²/γ_n²)` as a product over **real** `γ_n`. If the `γ_n` are the
  complete real zero set of `Ξ`, that product **is RH**; if they are only "prescribed reals",
  the product is not `Ξ` and the Taylor match fails. No RH-free reading gives both.
- **E-pos.** (H-div) forces every `Ξ`-zero to be a real-limit of real zeros of `F_N`, i.e.
  RH, *before* Montel/Hurwitz — (H-div) is an RH-strong hypothesis, not a harmless
  compactness input.
- **Also refuted:** "`Ξ` and the CCM `det_reg` sequence are known members of the record
  class" (`Ξ`-membership = RH; the CCM phase `−iλ^{−iz}` is not even/real and no exact
  `k_N`/`J_N` match is proven); and "`R_N → ∞`" (needs the unstated `k_N → ∞`).

**What survives (RH-free)** — the actual content — is over an **abstract Laguerre–Pólya
target** `L(z) = C∏(1 − z²/λ_n²)` with a *given* real, simple, summable-`λ_n^{-2}` zero set:
the IFT / scaled-Vandermonde / Cauchy machinery (Links A/B, CONFIRMED given `L`) and the
finite-order complete-divisor uniqueness lemma (Link D, conditional). **Specializing `L = Ξ`
is exactly RH and is not claimed.** See statement.md §0/§1'. Positioned as a Paper C
**supporting section** (abstract real-zero non-identifiability), not a standalone RH-free
`Ξ`-theorem.

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

## 3. E-neg is a per-`N` statement over the abstract target `L` (CONFIRMED given `L`)

The quantitative lower bound `sup_{|z|≤R_N}|F − L| ≥ ε_N` for a record-respecting `F`
(fixed `N`, `R_N ≥ 2λ_{k_N+1}`, over the abstract Laguerre–Pólya `L`) is CONFIRMED (OB-03
construction; OB-29 Link A/B given `L`), via the exact scaled-Vandermonde Jacobian and a
Cauchy coefficient estimate on the first unmatched log-power-sum. It uses **no** `N→∞`
passage. **Over `Ξ` specifically it is BLOCKED** (§0): identifying the divisor with `Ξ` is RH.

## 4. Not a claim that a sequence fails to converge (per-`N`)

E-neg (over `L`) shows the finite record `ℰ_N` **alone** does not identify `L` within its
fiber, for each `N`. It does **NOT** assert that some sequence `(F_N)` fails to converge
locally uniformly. The witness sits at radius `R_N ≥ 2λ_{k_N+1}`, which escapes to ∞ **only
under the extra assumption `k_N → ∞`** (OB-29 §1.4) — the bare per-`N` statement omits that
quantifier. Nor does it show that **no** sequence converges: the CCM sequence is conjectured
(numerically supported) to converge after suitable normalization. (This mirrors B1's "no
uniform separation margin," clear of the "margin → 0" non-barrier label.)

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
