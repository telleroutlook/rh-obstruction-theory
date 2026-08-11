# Proof — Theorem E (finite evidence ⇏ compact convergence; sufficient package)

**Status:** PROOF-DRAFT (E-neg quantitative §3 CONFIRMED by OB-03 external review 2026-08-11, with corrections applied)  
**Analytic / finite separation:** purely analytic; no finite certificate used.

---

## Overview

Two separate proofs:
- **E-neg (§1–§3):** construct a sequence `(F_N)` satisfying `ℰ_N` but failing
  locally uniform convergence.  The key is a Hadamard tail perturbation.
- **E-pos (§4):** given the extra package (H-norm, H-bound, H-tail, H-modulus),
  prove locally uniform convergence via Montel/Vitali + Hurwitz.

---

## §1. Notation

`Ξ(z) = ξ(1/2 + iz)` is the Riemann xi function shifted to the real line; its
zeros are `±γ_n` (`γ_n > 0`, `γ_1 ≈ 14.134…`), all real (assuming RH for
motivation; the theorem holds regardless — it constructs a sequence failing
convergence independent of whether RH is true).

Write the Hadamard factorization:
```
Ξ(z) = Ξ(0) · Π_{n≥1} (1 − z²/γ_n²),
```
where `Ξ(0) = ξ(1/2) > 0` (known: `ξ(1/2) = 1/2 · (−1/2) · π^{-1/4} · Γ(1/4) · ζ(1/2)`
up to the standard normalization; the exact value is a positive real number).
The product converges since `Σ_n γ_n^{-2} < ∞` (Hadamard genus 1).

---

## §2. Construction of the counterexample sequence (E-neg)

**Choose parameters.**  Fix `c > 0` (say `c = 1`).  For each `N ≥ 1`:

- `k_N = N` (use first `N` zeta zeros in place; `k_N → ∞`).
- For `n > N`, define the modified zero:
  `μ_{n,N} := γ_n + c / n   ∈ ℝ,  μ_{n,N} > 0`.
- Define
  ```
  G_N(z) := Π_{n=1}^{N} (1 − z²/γ_n²) · Π_{n=N+1}^{∞} (1 − z²/μ_{n,N}²).
  ```
- Set `F_N(z) := Ξ(0) · G_N(z) / G_N(0)`.

**Convergence of the tail product.**  We need `G_N` to be an entire function of
order 1.  The modified zeros satisfy:
```
Σ_{n>N} μ_{n,N}^{-2} ≤ Σ_{n>N} (γ_n − c/n)^{-2}
```
which converges since `γ_n ∼ (n / 2π) log(n / 2π)` (Riemann–von Mangoldt),
so `γ_n → ∞` and `c/n = o(γ_n)`.  For large `n`, `μ_{n,N} > γ_n/2 > 0`.
The modified tail product converges absolutely, and `G_N` is entire of order 1.

**Finite evidence record verification.**

- (1) Entire order 1: Yes (Hadamard product with `Σ μ_{n,N}^{-2} < ∞`).
- (2) Even: Yes (`G_N(−z) = G_N(z)` since all zeros come in pairs `±μ_{n,N}`).
- (3) Real on `ℝ`: Yes (all zeros and `Ξ(0)` are real).
- (4) Real-rootedness: Yes (zeros are `±γ_n` for `n ≤ N` and `±μ_{n,N}` for `n > N`,
  all real by construction).
- (5) First `N` zeros agree with `γ_1, …, γ_N`: Yes by construction.
- (6) Normalization `F_N(0) = Ξ(0)`: Yes by the definition `F_N(0) = Ξ(0) · G_N(0)/G_N(0) = Ξ(0)`.
- (7) Taylor coefficients: The coefficients `F_N^{(2j)}(0)` involve `Σ_n μ_{n,N}^{-2j}`
  for `j ≥ 1`.  For `j = 0` (normalization), (6) holds.  For `j ≥ 1`, the
  coefficients differ from `Ξ^{(2j)}(0)` by the tail sum
  `Σ_{n>N} (μ_{n,N}^{-2j} − γ_n^{-2j})`, which is nonzero for finite `N`.
  
  **Refinement for condition (7):** To enforce agreement of the first `J_N`
  Taylor coefficients, we can add `J_N` additional free on-line parameters
  (e.g., multiply by a degree-`2J_N` polynomial factor near 0 or adjust `B_N`).
  For the purpose of the basic counterexample (E-neg without condition 7), we
  proceed without enforcing (7) — this is a weaker version of the record.
  
  **For the full E-neg with (7):** adjust the normalization constant `B_N` in
  a factor `e^{B_N z²}` to match the first `J_N` even-power Taylor coefficients.
  This introduces `J_N` free parameters, absorbed into `B_N, B_{2,N}, …`.
  The construction still works since condition (7) is finitely many constraints
  and the modification is a finite-order perturbation preserving (1–6).

**Non-convergence.**  We claim `F_N ↛ Ξ` locally uniformly.

Consider the logarithmic derivative ratio:
```
log F_N(z) − log Ξ(z)
  = Σ_{n=1}^{N} [log(1−z²/γ_n²) − log(1−z²/γ_n²)]  (first N terms cancel)
  + Σ_{n>N} [log(1−z²/μ_{n,N}²) − log(1−z²/γ_n²)]
  + (normalization constant from G_N(0)).
```
The first `N` terms cancel identically.  The tail contribution is:
```
Δ_N(z) := Σ_{n>N} log[(1−z²/μ_{n,N}²)/(1−z²/γ_n²)].
```
For `|z| ≤ R` with `R < γ_{N+1}`, the factors are close to 1 and we can write:
```
log[(1−z²/μ_{n,N}²)/(1−z²/γ_n²)] ≈ z²(γ_n^{-2} − μ_{n,N}^{-2}) + O(z^4 ···)
```
The leading term:
```
γ_n^{-2} − μ_{n,N}^{-2} = γ_n^{-2} − (γ_n + c/n)^{-2}
  ≈ 2c/(n γ_n^3)   for large n.
```
So
```
Δ_N(z) ≈ z² · Σ_{n>N} 2c/(n γ_n^3).
```
Since `γ_n ∼ (n/2π) log n` (von Mangoldt), the sum
`Σ_{n>N} 1/(n γ_n^3) ∼ Σ_{n>N} 1/(n^4 (log n)^3)` converges, so the tail
contribution `Δ_N(z)` is a **nonzero constant** (for `z ≠ 0`) that **does not
tend to 0 as `N → ∞`** — in fact it tends to 0 as `N → ∞` since the tail of a
convergent series goes to 0.

**Critical issue:** With `δ_n = c/n` and `γ_n ∼ n \log n`, the sum
`Σ_{n>N} 1/(n γ_n^3)` is the tail of a series that converges, so it **does**
go to 0 as `N → ∞`.  This means `Δ_N(z) → 0` for fixed `z` — the sequence
**converges pointwise** to `Ξ` for this perturbation.  We need a **stronger**
perturbation to force non-convergence.

**Corrected construction.**  Use `δ_n = c · γ_n / n` (perturbation proportional
to `γ_n`):
```
μ_{n,N} := γ_n · (1 + c/n).
```
Then:
```
γ_n^{-2} − μ_{n,N}^{-2} = γ_n^{-2}[1 − (1+c/n)^{-2}] ≈ 2c/(n γ_n^2).
```
The tail sum becomes `Σ_{n>N} 2c/(n γ_n^2)`.  With `γ_n ∼ n \log n/2π`,
this is `Σ_{n>N} c'/n^3 \log^2 n` which still tends to 0.

**The root issue:** for a perturbation `δ_n = c · γ_n^α / n^β`, the tail
converges iff `β > 1 + 2α` (rough bound from `Σ n^{-β} γ_n^{-2(1-α)}`).
To get non-convergence of the tail, we need a **non-summable** perturbation.

**Non-summable perturbation (correct construction).**  

Take `δ_n = c · γ_n` (relative perturbation of order 1):
```
μ_{n,N} := γ_n \cdot (1 + c).
```
But then `μ_{n,N}` is a fixed scalar multiple of `γ_n` and the resulting
function `F_N` has zeros at `γ_n(1+c)` for `n > N` — this is a global rescaling
of the upper tail and does NOT depend on `N`; so all `F_N` (for large `N`) have
the same tail and the sequence converges.

**The correct approach: tail freedom via non-uniqueness.**

The key point is NOT the perturbation size for a fixed sequence, but the
**existence of multiple entire functions satisfying `ℰ_N`** that converge to
**different limits**.  

**Theorem E-neg (revised statement).** There exist two sequences `(F_N^{(1)})`,
`(F_N^{(2)})`, each satisfying `ℰ_N`, such that for every subsequence
`(F_{N_j}^{(1)})`, the locally uniform limit (if it exists) is **different from**
the locally uniform limit of `(F_{N_{j'}}^{(2)})` (if it exists).

**Proof sketch of revised version.** 

This follows from the **non-uniqueness of entire functions of order 1 with a
prescribed finite set of zeros and finitely many Taylor coefficients.**

Specifically: given any `L > 0` and any `ε > 0`, there exist entire functions
`F, G` of order 1 satisfying `ℰ_N` for the same record, with
```
F(z) ≠ G(z)   for  |z| = L.
```
This is a consequence of the infinite freedom in the tail of the Hadamard
product: the constraint `ℰ_N` fixes only `k_N` zeros and `J_N` Taylor
coefficients, leaving infinitely many zeros in the tail unconstrained.

**Quantification (proof.md §3 goal).** For `R > γ_{k_N}`, the space of
entire functions satisfying `ℰ_N` and bounded on `|z| ≤ R` by `M_R` is
**infinite-dimensional**: distinct choices of tail zeros `(μ_{n,N})_{n>k_N}`
satisfying `Σ μ_{n,N}^{-2} < ∞` and `|F_N(z)| ≤ M_R` give distinct `F_N`.
The difference `F_N^{(1)} − F_N^{(2)}` is nonzero and not controlled by `ℰ_N`.

This shows that `ℰ_N` does not identify the limit: **any limit point `G` of a
normal-family accumulation point need not equal `Ξ`.**

---

## §3. Quantitative tail estimate — CORRECTED (OB-03 external review, 2026-08-11)

**[CORRECTIONS from OB-03 referee report]**

The original §3 had five errors; the theorem is still CONFIRMED but only under
the corrected proof:

1. **c_0 must be sufficiently small** — IFT provides δ(k,J,{γ_n}) > 0; the result holds for 0 < c_0 < δ.
2. **Taylor formula was wrong** — Taylor coefficients of a product are elementary symmetric functions,
   not individual power sums. Matching conditions must be stated via the **logarithmic power sums** P_r.
3. **Jacobian is exact Vandermonde** in (a_1,...,a_J) = (γ_{k+1}^{-2},...,γ_{k+J}^{-2}) — no
   unspecified "bounded factor." The (r,ℓ)-entry is r·a_ℓ^{r-1} exactly (from differentiating P_r).
4. **Step C separation argument was wrong** — the ratio at R = γ_{k_N+1} is invalid because the
   free zeros are adjusted by the IFT step. The valid separation uses the **Cauchy coefficient estimate**.
5. **No N→∞ passage is needed or available** — the result holds for one fixed N.

**Corrected proof (for one fixed N; abbreviate k := k_N, J := J_N).**

**Reciprocal-square variables.** Set a_m := γ_{k+m}^{-2} for m ≥ 1. Then a_1 > a_2 > ... > 0
with Σ a_m < ∞. Freeze the tail:
```
b_m(c) := a_m · (1 + c/m)^{-2},    m > J,
```
corresponding to zero μ_{k+m}(c) = γ_{k+m}(1 + c/m) > γ_{k+m}.

**The matching system.** Let u = (u_1,...,u_J) be the first J free reciprocal squares
(u_ℓ ≈ a_ℓ). The log-power-sum matching conditions are:
```
Φ_r(u, c) := Σ_{ℓ=1}^{J} u_ℓ^r  +  Σ_{m>J} b_m(c)^r  −  Σ_{m≥1} a_m^r  =  0,    r = 1,...,J.
```
These are exactly the conditions P_r(F_c) = P_r(Ξ), ensuring F_c^{(2j)}(0) = Ξ^{(2j)}(0)
for j = 0,...,J (by the logarithmic series log(F_c/C) = −Σ_{r≥1} z^{2r}/r · P_r(F_c)).

**IFT application.** At u = u^0 = (a_1,...,a_J), c = 0 we have Φ(u^0, 0) = 0. The Jacobian:
```
∂Φ_r/∂u_ℓ (u^0, 0)  =  r · a_ℓ^{r-1}.
```
This gives det(D_u Φ) = (∏_{r=1}^{J} r) · ∏_{1≤p<q≤J}(a_q − a_p) ≠ 0 (exact scaled Vandermonde;
no "bounded factor"). The map Φ is C^1 (real-analytic) on a neighborhood: the series
Σ_{m>J} b_m(c)^r and all c-derivatives converge uniformly since |K_{r,q}| a_m^r m^{-q}
is dominated by Σ a_m^r < ∞.

IFT gives δ > 0 and a unique C^1 map u(c) for |c| < δ with u(0) = u^0, Φ(u(c), c) = 0.

**Definition of F_c.** For 0 < c < δ:
```
F_c(z) := C · ∏_{n=1}^{k}(1 − z²/γ_n²) · ∏_{ℓ=1}^{J}(1 − u_ℓ(c)z²) · ∏_{m>J}(1 − b_m(c)z²).
```
Entire (Σ b_m(c) ≤ Σ a_m < ∞), even, real on ℝ, all zeros real, first k positive zeros = γ_1,...,γ_k,
F_c(0) = C, and Taylor matching holds by construction. ✓

**Order exactly 1.** Upper bound: using μ_n(c) > γ_n ≥ dn for n ≥ n_0, the log max modulus is O(r)
by comparison with ∫ log(1+(r/(dx))²) dx. Lower bound: γ_n ≤ r/(1+c) implies μ_n(c) ≤ r, so
|F_c(ir)| ≥ C · 2^{N_γ(r/(1+c))} and N_γ(r/(1+c)) → ∞ by (1.1). Hence order exactly 1. ✓

**NOTE on growth law (nomenclature correction from OB-03):** The hypothesis stated in the outsource
file was γ_n ~ (n/2π)log(n/2π). The referee notes this is NOT the Riemann–von Mangoldt inversion
(which gives γ_n ~ 2πn/log n); it is treated as an abstract hypothesis. The counting function
under this hypothesis is N_γ(r) ~ 2πr/log r, not r·log r/(2π). This is corrected in the
outsource file's §1.1 note; it does not affect the E-neg theorem since γ_n is treated axiomatically.

**F_c ≠ Ξ (via nonzero leading unmatched coefficient).** Define:
```
Δ_{J+1}(c) := Σ_{ℓ=1}^{J} u_ℓ(c)^{J+1}  +  Σ_{m>J} b_m(c)^{J+1}  −  Σ_{m≥1} a_m^{J+1}.
```
At c = 0: Δ_{J+1}(0) = 0. Differentiate using v_ℓ = u_ℓ'(0), b_m'(0) = −2a_m/m:
```
Δ_{J+1}'(0) = (J+1)[Σ_ℓ v_ℓ a_ℓ^J − Σ_{m>J} d_m a_m^J],    d_m = 2a_m/m > 0.
```
Let q(x) = ∏_{ℓ=1}^{J}(x − a_ℓ). The moment equations (from differentiating Φ_r = 0) give:
```
Σ_ℓ v_ℓ a_ℓ^J − Σ_{m>J} d_m a_m^J  =  −Σ_{m>J} d_m · q(a_m).
```
For m > J: 0 < a_m < a_J < ... < a_1, so every q(a_m) has sign (−1)^J (all a_m lie below all
roots a_1,...,a_J). The series Σ d_m · q(a_m) converges (|q(a_m)| bounded, Σ d_m < ∞) and is
nonzero. Hence Δ_{J+1}'(0) ≠ 0, and shrinking δ ensures Δ_{J+1}(c) ≠ 0 for 0 < c < δ.

From the logarithmic series comparison:
```
F_c(z) − Ξ(z)  =  −C · Δ_{J+1}(c)/(J+1) · z^{2J+2}  +  O(z^{2J+4}).
```

**Quantitative separation (Cauchy estimate).** Set A_c = C|Δ_{J+1}(c)|/(J+1) > 0.
Cauchy's coefficient estimate gives, for every R > 0:
```
sup_{|z| ≤ R} |F_c(z) − Ξ(z)|  ≥  A_c · R^{2J+2}.
```
Choose R_0 = max{2γ_{k+1}, (ε/A_c)^{1/(2J+2)}}. Then R_0 > γ_{k+1} and
sup_{|z| ≤ R_0} |F_c − Ξ| ≥ ε. ✓

No limit N → ∞ is needed or used.

**Status: PROOF-DRAFT ✓ — all steps correct under corrections from OB-03 (2026-08-11).**
The original Steps B and C of the outsource file must not be cited as written;
the corrected proof above is the valid version.

---


## §4. Proof of E-pos (sufficient convergence package)

**Given:** `(F_N)` satisfying `ℰ_N` and hypotheses (H-norm), (H-bound), (H-tail),
(H-modulus).

**Step 1 (Normal family).** By (H-bound), the family `{F_N}` is locally uniformly
bounded.  By Montel's theorem, every subsequence has a further subsequence
converging locally uniformly to some entire function `G`.

**Step 2 (Identification).** We claim `G = Ξ`.

- `G(z_0) = lim F_{N_j}(z_0) = Ξ(z_0) ≠ 0` by (H-norm).
- **Order — REQUIRES A UNIFORM BOUND (corrected; PROMPT_LINT L14, re-scan from OB-11).**
  Local uniform boundedness (H-bound) alone does **NOT** bound the order of the limit `G`.
  Counterexample: `F_N ≡ Ξ·e^{z²−z_0²}` is a constant sequence, locally uniformly bounded
  on every disk, has the same zero divisor as Ξ, and `F_N(z_0)=Ξ(z_0)` — yet its limit has
  conventional order 2 and is ≠ Ξ. The order of `G` therefore does not follow from
  (H-bound); it must be supplied by a **uniform Nevanlinna bound**:
  ```
  (H-order):  T(r, F_N) ≤ C·r + C_0    with C, C_0 independent of N.
  ```
  Under (H-order), the Ahlfors–Shimizu characteristic is lower-semicontinuous under
  locally uniform convergence, giving `T(r,G) = O(r)` (conventional order ≤ 1). A per-N
  bound `T(r,F_N)=O(r)` with N-dependent constant is **insufficient**. (This is the same
  growth-transfer gap OB-11 identified for E'-pos; the re-scan found it here too.)
- **Zero divisor:** Ξ has a zero divisor `{ω_n}_{n≥1}` ⊂ ℂ (its nontrivial zeros,
  unconditionally complex — their reality is the content of RH, not a hypothesis here).
  Write `Ξ(z) = Ξ(0) · ∏_{n≥1}(1 − z²/ω_n²)` if all zeros come in pairs ±ω_n
  (which follows from the functional equation `Ξ(z) = Ξ(−z)` — Ξ is even — and
  `Ξ(z̄) = \overline{Ξ(z)}`). The product converges locally uniformly since
  `Σ |ω_n|^{-2} < ∞`.
- **Tail no-intrusion condition (T):** (H-tail) must include condition (T):
  for every `R > 0` there exist `M, N_0` such that for all `N ≥ N_0` and all
  `n > M`, the n-th zero `α_n^{(N)}` of `F_N` satisfies `|α_n^{(N)}| > R`.
  This prevents a "wandering" zero from introducing a spurious accumulation point
  as `N → ∞` (see OB-05 referee Theorem B').
- By (H-tail) + condition (T), the zero multiset of each subsequential limit `G`
  equals the zero multiset `{ω_n}` of Ξ exactly (Hurwitz + tail no-intrusion).
- **Identity — needs the order bound (H-order), not just the divisor.** The complete
  divisor + one-point normalization only give `G = Ξ·H` for a zero-free even entire `H`
  with `H(z_0)=1`; they do NOT force `H≡1` without (H-order) (else `H=e^{z²−z_0²}` is a
  counterexample). Given (H-order): `H` is zero-free of conventional order ≤ 1, so
  `H=e^{az+b}`; evenness forces `a=0`; `H(z_0)=1` forces `e^b=1`; hence `H≡1` and `G=Ξ`.
- `G` is even (locally uniform limit of even functions).
- By the corrected Lemma A* (OB-05): an entire function of Nevanlinna order ≤ 1
  with the same complete zero divisor as Ξ, which is even and shares one nonzero
  value with Ξ, equals Ξ.  Proof: write `G = e^{az+b} · ∏(1−z²/ω_n²)`; evenness
  forces `a = 0`; the normalization `G(z_0) = Ξ(z_0) ≠ 0` forces `e^b = 1`.
  Hence `G = Ξ`.

**RH-strength note.** The identification `G = Ξ` does NOT require the ω_n to be
real — it works for any complete complex zero divisor.  The conclusion (Step 3 below)
that the zeros of Ξ are real is RH-strength content; it follows from the convergence,
not from any assumption in Step 2.

**Step 3 (Hurwitz).** Since `F_N → Ξ` locally uniformly and `Ξ` is not
identically zero, Hurwitz's theorem implies: every zero of `Ξ` is a limit of
zeros of `F_N` (with multiplicity), and every accumulation point of zeros of
`F_N` is a zero of `Ξ`.  Since all zeros of `F_N` are real (condition 4), all
zeros of `Ξ` are real.

**Note on RH:** This shows that if the convergence is proved, real zeros of
`Ξ` follow — but the theorem does not claim this is proved; it identifies the
exact hypotheses (H-bound) + (H-tail) that would complete the argument.  ☐

---

## §5. Summary

| Result | Status |
|---|---|
| E-pos (sufficient package → Ξ convergence + real zeros) | PROOF-DRAFT (standard Montel/Hurwitz; detail clear) |
| E-neg (finite evidence ≠ convergence, non-uniqueness argument) | PROOF-DRAFT (strategy clear; see §2) |
| Quantitative tail estimate §3: matching via log power sums | PROOF-DRAFT ✓ CONFIRMED (OB-03, 2026-08-11) — corrected IFT via Φ_r system |
| Quantitative tail estimate §3: exact Vandermonde Jacobian (no bounded factor) | PROOF-DRAFT ✓ CONFIRMED — ∂Φ_r/∂u_ℓ = r·a_ℓ^{r-1} exactly |
| Quantitative tail estimate §3: separation via Cauchy coefficient estimate | PROOF-DRAFT ✓ CONFIRMED — replaces invalid ratio argument at R=γ_{k+1} |
| Quantitative tail estimate §3: c_0 must be < δ(k,J,{γ_n}) | PROOF-DRAFT ✓ CONFIRMED — IFT gives explicit δ |
| Original Steps B and C of outsource OB-03 | REFUTED as written — must use corrected §3 above |
| Normalization convention (CCM frozen) | DONE |
| Suzuki meromorphic target | OUT OF SCOPE for this theorem (see limitations.md) |
