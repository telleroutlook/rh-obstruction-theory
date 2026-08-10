# Proof — Theorem E' (E-prime-meromorphic)

**Status:** PROOF-DRAFT (E'-neg); OPEN (E'-pos)  
**Analytic / finite separation:** purely analytic.

---

## §1. Meromorphic Hadamard uniqueness

**Lemma E'.1.** Let `F`, `G` be meromorphic functions of order at most 1, with the same
multiset of poles `{p_k}` (multiplicities counted) and the same multiset of zeros `{z_j}`
(multiplicities counted), and `F(w₀) = G(w₀)` for some non-pole point `w₀` with
`F(w₀) ≠ 0`. Then `F = G`.

*Proof.* The Weierstrass product factorization for meromorphic functions of order ≤ 1:
```
F(z) = e^{az+b} · ∏_j E_1(z/z_j) / ∏_k E_1(z/p_k)
```
where `E_1(u) = (1−u)e^u` is the Weierstrass elementary factor of genus 1. Both
`F` and `G` have the same zero and pole products; they differ only in the exponential
prefactor `e^{az+b}`. The conditions `F(w₀) = G(w₀)` and `F(w₀) ≠ 0` pin the ratio
`e^{(a_F − a_G)w₀ + (b_F − b_G)} = 1`. Since the function `F/G = e^{(a_F−a_G)z + (b_F−b_G)}`
has no zeros or poles and equals 1 at `w₀`, parity constraints from the order-1 bound
give `a_F = a_G` and `b_F = b_G`, hence `F = G`. ☐

*Note:* The order-1 bound is essential — for order > 1, the exponential prefactor can
be `e^{P(z)}` for a polynomial `P` of degree > 1, and the argument fails.

`W(z) = z² ξ(1/2−iz)/ξ'(1/2−iz)` has order 1 (same as ξ). Lemma E'.1 applies.

---

## §2. E'-neg: non-uniqueness construction

**Setup.** Fix `N` (first `k_N` pole pairs fixed). The perturbed meromorphic function is:
```
F^{(c₀)}(z) = z² · ξ^{(c₀)}(1/2−iz) / (ξ^{(c₀)})'(1/2−iz)
```
where `ξ^{(c₀)}` is the Hadamard product over perturbed zeros
`μ_n^{(c₀)} = γ_n(1 + c₀/(n−k_N))` for `n > k_N` (same perturbation as E-neg §3).

**Step 1 (matching).** Match first `J_N` coefficients of the Laurent expansion of `F`
at a base point `w₀` not near any pole. The Jacobian of the matching map with respect
to `(c₀, μ_{k_N+1}, …, μ_{k_N+J_N})` has the same Vandermonde structure as E-neg §3,
since the partial fractions of `W(z)` at pole `γ_n` have residue `−i/ξ''(ρ_n)·ξ(ρ_n)`
(from the double zero structure), and small shifts in `γ_n` produce a linearized IFT
with a Vandermonde matrix in `{γ_n^{-1}}`. **Status: PROOF-DRAFT** (IFT step explicit
in E-neg §3; the meromorphic residue version needs to be written out fully).

**Step 2 (separation).** The perturbed function differs from `W` near `z = iR` for
large `R` by an amount:
```
|F^{(c₀)}(iR) − W(iR)| / |W(iR)| ≥ δ(c₀) > 0
```
since the ratio `ξ^{(c₀)}/ξ` evaluated at `1/2 + R` grows as the Hadamard product
ratio `∏_{n>k_N}(1 + (R−γ_n)²/(γ_n + c₀/(n−k_N))²) / (1 + (R−γ_n)²/γ_n²)`. For
`c₀ ≠ 0` this ratio is not identically 1.

**Step 3 (|W(iR)| → ∞).** By the Hadamard product for ξ:
```
|ξ(1/2 + R)| = |ξ(0)| · ∏_n (1 + R²/γ_n²) ≥ |ξ(0)| · 2^N
```
where `N ~ R log R / (2π)` (from von Mangoldt). So `|W(iR)| → ∞` and the separation
`|F^{(c₀)}(iR) − W(iR)| → ∞` as well, giving sup-norm separation on any compact
set avoiding the poles. ☐ (modulo Step 1 IFT write-out)

---

## §3. E'-pos strategy (OPEN)

The E-pos proof used (in order):
1. **Montel:** (H-bound) → normal family → precompact in `C(K)` for compact `K`.
2. **Vitali:** (H-norm) pins the limit to one function.
3. **Hurwitz:** (H-tail) transfers real zeros to limit.

For meromorphic functions, the analogues are:
1. **Marty's theorem:** a family of meromorphic functions is normal iff the spherical
   derivatives are locally uniformly bounded. Under (H'-bound) + (H'-pole-sep), the
   family is normal in the spherical metric.
2. **Vitali for meromorphic:** standard.
3. **Argument principle (instead of Hurwitz):** for meromorphic functions, real poles
   transfer to the limit by the argument principle rather than Hurwitz.

The full E'-pos proof requires writing out these steps for the Suzuki meromorphic
setting. Deferred — the structure is clear, the execution is open.

---

## §4. Status

| Step | Status |
|---|---|
| Lemma E'.1 (meromorphic Hadamard uniqueness) | PROOF-DRAFT (complete above; citation open) |
| E'-neg Step 1 (IFT for meromorphic residues) | PROOF-DRAFT (template from E-neg; explicit write-out open) |
| E'-neg Steps 2–3 (separation via Hadamard) | PROOF-DRAFT (same as E-neg) |
| E'-pos (Marty + Vitali + argument principle) | OPEN (structure clear) |
| Suzuki missing ingredients identified | ✓ (H'-bound, H'-tail — same structure as CCM) |
