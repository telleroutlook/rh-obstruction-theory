# Proof — Theorem E' (E-prime-meromorphic)

**Status:** PROOF-DRAFT (E'-neg redesigned after OB-06 2026-08-11); OPEN (E'-pos)  
**Analytic / finite separation:** purely analytic.  
**Key corrections (OB-06 2026-08-11):** W is ODD (not even); γ_n are ZEROS of W
(not poles); poles of W come from zeros of ξ'(1/2−iz); old E'-neg construction
(perturbing "poles at γ_n") was entirely wrong and is replaced below.

---

## §1. Meromorphic Hadamard uniqueness — CONFIRMED AFTER CORRECTION

**Lemma E'.1.** Let `F`, `G` be meromorphic functions with `T(r,F) = O(r)`,
`T(r,G) = O(r)`, with identical complete zero divisors (`ord_a F = ord_a G` for
all a), with `F/G` even (both F,G odd suffices), and `F(w₀) = G(w₀) ≠ 0` at some
non-pole `w₀`. Then `F = G`.

*Proof (OB-06 referee §3).* H := F/G is entire, zero-free, `T(r,H) = O(r)`, even.
By Hadamard: `H = e^{az+b}`. Evenness forces `a = 0`. Normalization forces `e^b = 1`.
Hence `H ≡ 1`. ☐ (Conway, *Functions of One Complex Variable I*, 2nd ed., Thm XI.3.4.)

*Correct canonical product.* For paired zeros `±z_j` with `Σ|z_j|^{-2} < ∞`:
```
Z(z) = ∏_j (1 − z²/z_j²)
```
converges locally uniformly (Weierstrass pairing identity: `E_1(z/a)E_1(z/−a) = 1 − z²/a²`).
The alternative `∏(1−z²/z_j²)e^{z²/z_j²}` introduces a spurious `exp(z²·Σz_j^{-2})` factor
of order 2 and is WRONG for this setting.

---

## §2. Analytic structure of W — CORRECTED (OB-06)

`W(z) = z² ξ(1/2−iz) / ξ'(1/2−iz)`.

**Parity.** W is ODD: `W(−z) = −W(z)`.
(Proof: X(z) := ξ(1/2−iz) is even; ξ'(s)=−ξ'(1−s) → ξ'(1/2−iz) is odd;
ratio X/X' is odd; times z² still odd.)

**Zeros.** γ (a zero of ξ of multiplicity m) → simple zero of W at z = γ:
```
W(z) = −iγ²/m · (z − γ) + O((z−γ)²).
```
γ is NOT a pole of W. There is no residue at γ.

**Poles.** Zeros of ξ'(1/2−iz) not cancelled by zeros of ξ(1/2−iz).
At z=0: ξ'(1/2)=0; local behavior determined by vanishing order of ξ' at 1/2.

---

## §3. E'-neg: non-uniqueness construction — REDESIGNED

**Strategy (corrected — PROOF-DRAFT).**

The old construction perturbed "poles at γ_n"; this was wrong since γ_n are zeros
of W, not poles. The corrected construction perturbs the **zeros** of W.

**Step 1.** Fix `k = k_N` (first k zeros γ_1,…,γ_k of W are held fixed).
For `n > k`, set `μ_n^{(c₀)} = γ_n(1 + c₀/(n−k))`. Define the perturbed odd
meromorphic function:
```
F^{(c₀)}(z) = z² · ξ^{(c₀)}(1/2−iz) / ξ'(1/2−iz)
```
where `ξ^{(c₀)}` is the Hadamard product for ξ with zeros γ_n replaced by μ_n^{(c₀)}
for `n > k`.  The poles of `F^{(c₀)}` are the same as those of W (zeros of ξ').
`F^{(c₀)}` is odd (same parity argument as W).

**Step 2 (IFT for Taylor matching).** Adjust J_N of the free tail zeros
`μ_{k+1},…,μ_{k+J_N}` to enforce:
```
(1/j!) F^{(c₀)(j)}(w₀) = (1/j!) W^{(j)}(w₀),   j = 0,…,J_N−1.
```
The Jacobian matrix of the matching system at `c₀ = 0` with respect to
`(μ_{k+1},…,μ_{k+J_N})` has the structure of a Vandermonde matrix in
`{1/(w₀ − γ_n)}_{n=k+1}^{k+J_N}`, nonsingular since the γ_n are distinct and
`w₀ ∉ {γ_n}`. IFT gives `δ > 0` and a unique `C^1` branch `μ_n(c₀)` for `|c₀| < δ`.

**Step 3 (separation).** For `c₀ ≠ 0`, the (J_N+1)-th Taylor coefficient of
`F^{(c₀)}` differs from W's. Cauchy's estimate gives:
```
sup_{|z| ≤ R₀} |F^{(c₀)}(z) − W(z)| ≥ A_{c₀} · R₀^{2J_N+2}
```
for an explicit `A_{c₀} > 0` depending on the coefficient discrepancy (same argument
as E-neg §3; see E-compactness/proof.md §3).

**What remains to write out.** The full meromorphic IFT argument in Step 2
(analogous to E-neg §3's log-power-sum system Φ_r) needs to be made explicit
for the odd meromorphic case. The Vandermonde structure is clear; execution is
PROOF-DRAFT.

---

## §4. E'-pos strategy — OPEN

Under hypotheses (LB*) + (H'-pole-sep) + (H'-tail) + (H'-norm):

1. **(LB*) → Montel on Ω.** For each compact L ⊂ Ω = ℂ\{poles of W}, (LB*) gives
   an open neighborhood U_L on which F_n are holomorphic and uniformly bounded.
   Montel (Conway, VII.2.9) → a subsequence converging uniformly on U_L, hence on L.
   Diagonal construction over exhaustion L_j ↗ Ω gives a single subsequence converging
   on all of Ω. (Marty not needed — Montel for analytic functions suffices on Ω.)

2. **Identification G = W.** Limit G is odd, has the same complete zero divisor
   as W (via H'-tail + tail no-intrusion condition T), same poles (via H'-pole-sep
   + argument principle), `G(w₀) = W(w₀)` (H'-norm). By Lemma E'.1, `G = W`.

**Status:** OPEN. Structure clear; execution deferred.

---

## §5. Status

| Step | Status |
|---|---|
| Lemma E'.1 (meromorphic Hadamard uniqueness) | CONFIRMED AFTER CORRECTION (OB-06; Conway XI.3.4; F/G route) |
| W parity (ODD) | CONFIRMED: W(−z) = −W(z) (OB-06) |
| W zero structure (γ_n are ZEROS) | CONFIRMED: simple zeros; W = −iγ²/m·(z−γ)+O(…) (OB-06) |
| Old E'-neg (perturbing "poles at γ_n") | REFUTED (γ_n are zeros not poles; residue argument entirely wrong) |
| E'-neg redesigned (perturbing zeros of W) | PROOF-DRAFT (Vandermonde IFT; write-out open) |
| Old E'-pos ("even F_N → even W") | REFUTED (W is odd) |
| E'-pos redesigned (odd F_N → W via Montel on Ω) | OPEN (structure complete; Montel suffices) |
| Suzuki missing ingredients | ✓ identified (odd parity; H'-bound/(LB*); H'-tail) |
