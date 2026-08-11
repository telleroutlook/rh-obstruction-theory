# Proof — Theorem E' (E-prime-meromorphic)

**Status:** PROOF-DRAFT (E'-neg redesigned after OB-06 2026-08-11); OPEN (E'-pos)  
**Analytic / finite separation:** purely analytic.  
**Key corrections (OB-06 2026-08-11):** W is ODD (not even); γ_n are ZEROS of W
(not poles); poles of W come from zeros of ξ'(1/2−iz); old E'-neg construction
(perturbing "poles at γ_n") was entirely wrong and is replaced below.

---

## §1. Meromorphic Hadamard uniqueness — CONFIRMED AFTER CORRECTION

**Lemma E'.1.** Let `F`, `G` be meromorphic functions of **conventional order ≤ 1**
(for every `ε>0`, `T(r,·) ≤ C_ε r^{1+ε}+C_{0,ε}`; this includes the maximal-type case
`T ≍ r log r`, i.e. `W` itself — NOT the linear `O(r)` bound), with identical complete zero
divisors (`ord_a F = ord_a G` for all a), with `F/G` even (both F,G odd suffices), and
`F(w₀) = G(w₀) ≠ 0` at some non-pole `w₀`. Then `F = G`.

*Proof (OB-06 referee §3).* H := F/G is entire, zero-free, of conventional order ≤ 1
(`T(r,H) ≤ T(r,F)+T(r,1/G)+O(1)`, First Main Theorem), even. A zero-free entire function of
order ≤ 1 is `H = e^{az+b}` (Hadamard, Conway XI.3.4). Evenness forces `a = 0`. Normalization
forces `e^b = 1`. Hence `H ≡ 1`. ☐

*Correct canonical product.* For paired zeros `±z_j` with `Σ|z_j|^{-2} < ∞`:
```
Z(z) = ∏_j (1 − z²/z_j²)
```
converges locally uniformly (Weierstrass pairing identity: `E_1(z/a)E_1(z/−a) = 1 − z²/a²`).
The alternative `∏(1−z²/z_j²)e^{z²/z_j²}` introduces a spurious `exp(z²·Σz_j^{-2})` factor
of order 2 and is WRONG for this setting.

---

## §2. Analytic structure of W — CORRECTED (OB-06)

`W(z) = z² A(z) / B(z)` in the abstract form, where A is even (zeros ±γ_n),
B is odd with a simple zero at 0 (B(z) = z·B̃(z), B̃ even), both of Nevanlinna
order ≤ 1.  Concretely `A(z) = ξ(1/2−iz)`, `B(z) = ξ'(1/2−iz)` (up to normalization).

**Parity.** W is ODD: `W(−z) = −W(z)`.
(Proof: X(z) := ξ(1/2−iz) is even; ξ'(s)=−ξ'(1−s) → ξ'(1/2−iz) is odd;
ratio X/X' is odd; times z² still odd.)

**Zeros.** γ (a zero of ξ of multiplicity m) → simple zero of W at z = γ:
```
W(z) = −iγ²/m · (z − γ) + O((z−γ)²).
```
γ is NOT a pole of W. There is no residue at γ.

**Poles.** Zeros of ξ'(1/2−iz) not cancelled by zeros of ξ(1/2−iz).
At z=0: ξ'(1/2)=0; the z² numerator and simple zero of B at 0 give W a simple
zero at 0 (W odd, so vanishing order at 0 is odd).

**Non-collision assumption (OB-09 referee §2.2, mandatory).** For "γ_n is a zero of
W" one needs `Z(A) ∩ (Z(B)\{0}) = ∅` — the zeros of A (at ±γ_n) must not coincide
with nonzero zeros of B, else pole/zero cancellation occurs. This is an explicit
assumption of the method class, added below.

**No |W(iR)| → ∞ claim (OB-09 referee §2.2).** The earlier assertion
`|W(iR)| ≥ C|A(iR)| → ∞` is FALSE in general — counterexample `A(z)=sin(πz)/(πz)`,
`B(z)=z cos(2πz)` gives `|W(iR)| → 0`. The separation argument must NOT rely on
`|W(iR)| → ∞`; use the Cauchy-estimate route below instead.

---

## §3. E'-neg: non-uniqueness construction — CONFIRMED AFTER CORRECTION (OB-09 §7)

**[OB-09 referee 2026-08-11: the power-sum matching system Φ_r was REFUTED — it
matches the expansion at z=0, NOT the Taylor jet at a nonzero base point w₀. The
correct construction uses the direct w₀-jet system below (referee §7), which closes
with an explicit rational Wronskian–Vandermonde Jacobian.]**

**Method-class assumptions (corrected).** Fix k ≥ 1, J ≥ 1. Assume:
- (A1) A even, Nevanlinna order ≤ 1, simple zeros exactly at {±γ_n}, A(0) ≠ 0:
  `A(z) = A(0) ∏_{n≥1}(1 − a_n z²)`, `a_n = γ_n^{-2}`, `a_1 > a_2 > … > 0`, Σ a_n < ∞.
- (A2) B odd, Nevanlinna order ≤ 1, all zeros simple, `Z(B) ∩ ℝ = {0}` (so no
  real zero of B collides with the real ±γ_n).
- (A3) base point `w₀ = iτ`, `τ ∈ ℝ\{0}`, `B(iτ) ≠ 0`.

**Perturbation family.** Freeze γ_1,…,γ_k. For the tail `n = k+J+m` (m ≥ 1) set
```
μ_{k+J+m}(c) = γ_{k+J+m}(1 + c/(J+m)),   so  b_m(c) = γ_{k+J+m}^{-2}(1+c/(J+m))^{-2},
```
(note the denominator is **J+m**, not m — OB-09 §2.3 correction). The J positions
`μ_{k+1},…,μ_{k+J}` are free variables `u_ℓ = μ_{k+ℓ}^{-2}`, adjusted by IFT.
Define:
```
A_{u,c}(z) = A(0) ∏_{n=1}^k(1−a_n z²) ∏_{ℓ=1}^J(1−u_ℓ z²) ∏_{m≥1}(1−b_m(c) z²),
F^{(c)}(z) = z² A_{u(c),c}(z) / B(z).
```

**The correct jet system (OB-09 §7).** Let `t = z²`, `t₀ = w₀² = −τ² < 0`, and
```
L(t; u, c) = log[A_{u,c}(z)/A(z)] = Σ_ℓ log((1−u_ℓ t)/(1−x_ℓ t)) + Σ_m log((1−b_m(c)t)/(1−y_m t)),
```
with `x_ℓ = a_{k+ℓ}`, `y_m = a_{k+J+m}`. Define the matching functionals:
```
Ψ_j(u, c) := ∂_t^j L(t₀; u, c),   j = 0, 1, …, J−1.
```
Then `Ψ(u⁰, 0) = 0` where `u_ℓ⁰ = x_ℓ`. Since `∂_{u_ℓ} L = −t/(1−u_ℓ t)`, the
Jacobian `D_u Ψ(u⁰,0)` is the Wronskian of `g_ℓ(t) = −t/(1−x_ℓ t)` at `t₀`:
```
det D_u Ψ(u⁰,0) = (−t₀)^J (∏_{j=0}^{J-1} j!) · ∏_{p<q}(x_q − x_p) / ∏_ℓ(1−x_ℓ t₀)^J ≠ 0.
```
This is an explicit rational Wronskian–Vandermonde determinant, nonzero since the
x_ℓ are distinct and `w₀ = iτ` is not a zero of A. The C¹ regularity in c follows
from Σ y_m < ∞ and the dominated-derivative bound `|d/dc·b_m(c)^r| ≤ C·y_m^r/(J+m)`.

**IFT conclusion.** For `−ε < c ≤ 0` there is a unique C¹ branch `u(c)` with
`Ψ(u(c),c) = 0`, i.e. `L(t; u(c),c) = O((t−t₀)^J)`, hence
`A_{u(c),c}(z) − A(z) = O((z−w₀)^J)`. Multiplying by `z²/B(z)` (holomorphic, nonzero
at w₀) gives the J-jet matching `(F^{(c)})^{(j)}(w₀) = W^{(j)}(w₀)`, j = 0,…,J−1. ✓

**Membership + distinctness.** For small `c < 0`: `F^{(c)}` is odd, meromorphic of
conventional order ≤ 1 (`T(r,F^{(c)}) ≍ r log r`, matching `W`: the poles of `B` give
`N(r,∞) ≍ (1/2π)r log r`; the perturbed zeros `μ_n ≍ γ_n` add the same order — NOT `O(r)`),
keeps the frozen simple zeros ±γ_1,…,±γ_k, has exactly the poles of W (assumption (A2)
prevents collisions), and satisfies the J-jet condition. And `F^{(c)} ≠ W`: equality would
force `A_{u(c),c} ≡ A`, but `μ_n(c) = γ_n(1+c/(n−k)) < γ_n` for `c < 0`, n > k+J.
Hence `F^{(c)} ∈ 𝔐_Suz` and `F^{(c)} ≠ W`. ✓ (OB-09 referee §7.2)

**Separation (corrected degree, OB-09 §5.1).** The leading discrepancy is ODD:
```
F^{(c)}(z) − W(z) = −(A(0)/B̃(0)) · Δ_{J+1}(c)/(J+1) · z^{2J+3} + O(z^{2J+5}),
```
degree **2J+3** (odd), not 2J+2 (the old even degree contradicted F−W being odd).
For `0 < R < R_B := dist(0, Z(B)\{0})`, Cauchy's estimate gives
`sup_{|z|=R} |F^{(c)}−W| ≥ |A(0)/B̃(0)·Δ_{J+1}(c)/(J+1)| R^{2J+3}`, with
`Δ_{J+1}(c) ≠ 0` for small `c ≠ 0` (nondegeneracy via `q(y_m)` constant sign,
OB-09 §5).

**Status: PROOF-DRAFT ✓ CONFIRMED AFTER CORRECTION (OB-09 2026-08-11).** The
construction closes via the direct w₀-jet system (§7 of the referee report), not
the power-sum system. The power-sum system Φ_r is REFUTED for this purpose.

---

## §4. E'-pos strategy — CORRECTED (OB-11 2026-08-11)

**[OB-11 referee: the E'-pos claim under (LB*)+(H'-pole-sep)+(H'-tail)+(H'-norm) is
REFUTED. Two independent counterexamples; corrected hypotheses below.]**

**Counterexamples to the original hypotheses:**
- *Growth gap.* `F_n ≡ W·exp(z²−w₀²)` (constant sequence) satisfies parity, local
  boundedness on Ω, zero-divisor convergence, pole matching, and normalization, but
  converges to `W·e^{z²−w₀²} ≠ W`. The divisor + one-point normalization only give
  `G = W·H` with `H` zero-free even, `H(w₀)=1`; they do NOT force `H ≡ 1`. Here
  `T(r,H) ≍ r²`: order must be controlled by an independent hypothesis.
- *Pole-cancellation gap.* A rational-multiplier family `F_n = W·H·Q_n` can place a
  double zero at `±p ∈ 𝒫` (cancelling W's simple pole there) while relocating the pole
  to `±p_n`; it meets every original hypothesis (with `T(r,F_n)=O(r)` uniform), yet its
  limit drops `p` from the polar divisor. Independent of the growth gap.

**Corrected hypotheses (statement.md §5).** (P), (LB), (ZT.1), plus:
- **(ZT_ℂ)** full-plane tail no-intrusion (every zero of `F_n` in `{|z|≤R}`, incl. at
  `𝒫`, is a matched zero) — closes pole cancellation;
- **(PL⁺)** each `p ∈ 𝒫` has a disk with exactly one simple pole `p_n → p` and no zeros;
- **(N)** normalization;
- **(UG)** uniform conventional-order bound: `∀ε>0`, `T(r,F_n) ≤ C_ε r^{1+ε}+C_{0,ε}`,
  constants independent of n — closes the growth gap. (Exponent `r^{1+ε}`, NOT linear
  `Cr+C₀`: `T(r,W) ≍ r log r`, so a linear bound would exclude `W` — L1/L14, OB-30 re-scan.)

**Corrected proof (OB-11 §6, PROOF-DRAFT):**
1. **Montel + diagonal (Ω).** (LB) ⟹ subsequence `F_{n_j} → G` locally uniformly on Ω,
   `G` holomorphic, odd, `G(w₀) = W(w₀) ≠ 0`. Montel suffices (Conway VII.2.9); no Marty.
2. **Zeros in Ω.** Hurwitz + (ZT.1)+(ZT_ℂ): `Z(G;Ω) = {0, ±γ_k}`, all simple.
3. **Genuine simple pole at each `p ∈ 𝒫`.** Contour/residue argument on a circle around
   `p`: locally uniform convergence transfers Laurent coefficients, forcing `G` to have
   a simple pole at `p` (not removable — the log-derivative contour integral equals −1,
   impossible for a removable point). (PL⁺) supplies the needed no-zero-in-disk. Also
   gives spherical local uniform convergence across `p`.
4. **Order transfer.** Ahlfors–Shimizu characteristic + (UG) ⟹ `T(r,G) ≤ C_ε r^{1+ε}+C_{0,ε}`
   (conventional order ≤ 1) for the meromorphic extension. (This is the step that fails
   without a *uniform* bound; and the envelope must be `r^{1+ε}`, not linear, else it
   excludes `W`.)
5. **Identify.** `G, W` share the complete divisor, `G/W` even, `G(w₀)=W(w₀)≠0` ⟹
   by Lemma E'.1, `G ≡ W`. Subsequence principle upgrades to full-sequence convergence.

**Status:** PROOF-DRAFT ✓ (OB-11 §6 is a complete line-by-line proof of the corrected
theorem). Suzuki application: (LB), (ZT_ℂ), (PL⁺), (UG) must be verified for W(a,θ;z).

---

## §5. Status

| Step | Status |
|---|---|
| Lemma E'.1 (meromorphic Hadamard uniqueness) | CONFIRMED AFTER CORRECTION (OB-06; Conway XI.3.4; F/G route) |
| W parity (ODD) | CONFIRMED: W(−z) = −W(z) (OB-06) |
| W zero structure (γ_n are ZEROS) | CONFIRMED: simple zeros; W = −iγ²/m·(z−γ)+O(…) (OB-06) |
| Non-collision Z(A)∩(Z(B)\{0})=∅ | Required assumption (OB-09 §2.2); added to method class (A2) |
| \|W(iR)\|→∞ claim | REFUTED (OB-09 §2.2): false in general; separation uses Cauchy estimate instead |
| Old E'-neg (perturbing "poles at γ_n") | REFUTED (γ_n are zeros not poles; residue argument entirely wrong) |
| E'-neg power-sum system Φ_r | REFUTED (OB-09): matches expansion at z=0, not jet at nonzero w₀ |
| E'-neg via direct w₀-jet system (§3, OB-09 §7) | CONFIRMED AFTER CORRECTION — Wronskian–Vandermonde Jacobian, closed IFT |
| E'-neg separation degree | CORRECTED: leading term is z^{2J+3} (odd), not z^{2J+2} (OB-09 §5.1) |
| Old E'-pos ("even F_N → even W") | REFUTED (W is odd) |
| E'-pos as first stated (LB*/H'-pole-sep/H'-tail/H'-norm ⟹ G=W) | REFUTED (OB-11): growth gap + pole-cancellation gap, each with counterexample |
| E'-pos CORRECTED (adds ZT_ℂ, PL⁺, UG) | PROOF-DRAFT ✓ (OB-11 §6 line-by-line; Montel not Marty) |
| Suzuki missing ingredients | OPEN: (LB), (ZT_ℂ), (PL⁺), (UG), odd parity for W(a,θ;z) |
