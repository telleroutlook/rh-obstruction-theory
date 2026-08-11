# Proof — Theorem E (finite evidence ⇏ compact convergence; sufficient package)

**Status:** PROOF-DRAFT (E-neg quantitative §3 CONFIRMED by OB-03 external review 2026-08-11, with corrections applied)  
**Analytic / finite separation:** purely analytic; no finite certificate used.

---

## Overview

Two separate proofs:
- **E-neg (§1–§3):** for each fixed `N`, exhibit an entire function `F` satisfying `ℰ_N`
  that stays `≥ ε_N` away from `Ξ` on a disk `|z| ≤ R_N` (`R_N ≥ 2γ_{k_N+1}`) — the finite
  record does not identify `Ξ`. The key is a fixed-`N` Hadamard tail matched to the record
  by the implicit function theorem, then separated by the first unmatched coefficient. (This
  is **per-`N` non-identifiability**, not a claim that some sequence `(F_N)` fails to
  converge — see statement.md and §2.)
- **E-pos (§4):** given the extra package (H-norm, H-bound, H-uorder, H-div),
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

## §2. Why naive tail perturbations fail — motivation for the §3 IFT route

Before the correct construction (§3), it is worth recording why the obvious "hand-pick a
tail perturbation `δ_n` and read off non-convergence" approach does **not** work — this is
what motivates the implicit-function-theorem route.

**The naive attempts all self-defeat.** Take `μ_{n,N} := γ_n + δ_n` for `n > k_N` and
compare `F_N` with `Ξ` through the tail log-difference
`Δ_N(z) = Σ_{n>k_N} log[(1−z²/μ_{n,N}²)/(1−z²/γ_n²)]`, whose leading term is
`z² Σ_{n>k_N}(γ_n^{-2} − μ_{n,N}^{-2})`. For the perturbation to keep `F_N` entire of order 1
one needs `Σ (γ_n^{-2}−μ_{n,N}^{-2})` to converge — but then, being the tail of a convergent
series, it **tends to 0** as `k_N → ∞`. Concretely:

| perturbation `δ_n` | leading tail term | tail sum behavior |
|---|---|---|
| `c/n` | `≈ 2c/(nγ_n^3)` | converges → 0 |
| `c·γ_n/n` | `≈ 2c/(nγ_n^2)` | converges → 0 |
| `c·γ_n` (fixed ratio) | — | `N`-independent global rescaling; all `F_N` share it |

So any *summable* hand-picked perturbation makes the sequence converge (defeating the
witness), and a *non-summable* one either breaks order 1 or is an `N`-independent rescaling.
The naive approach cannot produce a record-respecting witness.

**The correct route (§3).** Do not hand-pick `δ_n`. For a **fixed** `N`, use the
implicit-function theorem to *match the finite record exactly* — the log-power-sum system
`Φ_r(u,c)=0` (`r=1,…,J`) with the exact Vandermonde Jacobian — leaving one tail parameter
`c` free, and then separate `F_c` from `Ξ` through the **first unmatched** log-power-sum via
a Cauchy coefficient estimate. This gives a per-`N` witness with no `N→∞` passage. The
resulting statement is **per-`N` non-identifiability** (statement.md Theorem E-neg), not
sequence non-convergence.

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
- **Order — REQUIRES A UNIFORM ORDER ENVELOPE (corrected twice; PROMPT_LINT L1+L14).**
  Local uniform boundedness (H-bound) alone does **NOT** bound the order of the limit `G`.
  Counterexample: `F_N ≡ Ξ·e^{z²−z₀²}` is a constant sequence, locally uniformly bounded
  on every disk, has the same zero divisor as Ξ, and `F_N(z₀)=Ξ(z₀)` — yet its limit has
  conventional order exactly 2 (`T(r, e^{z²−z₀²}) = r²/π + O(1)`, so `T(r,G) ≥ r²/π −
  o(r²)`) and is ≠ Ξ (OB-14 §3). The order of `G` therefore does not follow from (H-bound);
  it must be supplied by a **uniform order envelope**:
  ```
  (H-uorder):  ∀ε>0 ∃ C_ε, C_{0,ε}, r_ε (independent of N):
               T(r, F_N) ≤ C_ε · r^{1+ε} + C_{0,ε}   for all N, r ≥ r_ε.
  ```
  **WARNING (OB-14 §1.1, §4.3 — L1 error corrected).** The envelope must be
  `r^{1+ε}` (uniform conventional order ≤ 1), NOT the finite-type bound `T(r,F_N) ≤ Cr+C_0`.
  A uniform *linear* bound would transfer to `T(r,Ξ) ≤ Cr+C_0`, forcing Ξ to have finite
  exponential type — but the real Ξ has **infinite** exponential type (`log|Ξ(iy)| ∼
  (y/2)log(y/2)`). So a linear (H-order) is INCOMPATIBLE with the actual target and would
  make the theorem vacuous (no approximating family could exist). `(H-uorder)` with the
  `r^{1+ε}` exponent permits order-1 infinite-type functions, including Ξ.
  Under (H-uorder), `T(r,·)` is continuous under locally uniform convergence
  (`T(r,F_{N_j}) → T(r,G)`, OB-14 Lemma 2.2 — a direct `log⁺` uniform-continuity argument,
  no Ahlfors–Shimizu needed), so `T(r,G) ≤ C_ε r^{1+ε}+C_{0,ε}` and `ρ(G) ≤ 1`. A per-N
  bound `T(r,F_N)=O_N(r^{1+ε})` with N-dependent constant is **insufficient** (OB-14 §5:
  even Taylor polynomials of `G`, each order 0, converge to the order-2 `G`).
- **Zero divisor:** Ξ has a zero divisor `{±ω_n}_{n≥1}` ⊂ ℂ (its nontrivial zeros,
  unconditionally complex — their reality is the content of RH, not a hypothesis here).
  Write `Ξ(z) = Ξ(0) · ∏_{n≥1}(1 − z²/ω_n²)` (genus-1 paired product, no exponential
  factor: `E_1(z/ω)E_1(−z/ω) = 1−z²/ω²`), convergent since `Σ |ω_n|^{-2} < ∞`.
- **Divisor convergence (H-div), multiplicity-complete (OB-14 §1.2).** (H-tail) must be
  the two-sided disk condition: for every `R>0` with no zero of Ξ on `|z|=R`, the zeros of
  `F_N` in `|z|<R` (with multiplicity) can be listed `a_{N,1},…,a_{N,m(R)}` with
  `a_{N,k} → a_k` (the zeros of Ξ in the disk) and no others, for all large N. This is
  both no-intrusion AND full approximation with multiplicity (the literal one-sided
  no-intrusion clause is vacuous for zero-free approximants — OB-14 §4.1). By Rouché,
  the subsequential limit `G` then has exactly the complete zero divisor of Ξ.
- **Identity — needs the order envelope (H-uorder), not just the divisor.** The complete
  divisor + one-point normalization only give `G = Ξ·H` for a zero-free even entire `H`
  with `H(z₀)=1`; they do NOT force `H≡1` without (H-uorder) (else `H=e^{z²−z₀²}` is a
  counterexample). Given (H-uorder): `H=G/Ξ` is zero-free (First Main Theorem:
  `T(r,H) ≤ T(r,G)+T(r,Ξ)+O(1)`, order ≤ 1), so `H=e^{az+b}`; evenness forces `a=0`;
  `H(z₀)=1` forces `e^b=1`; hence `H≡1` and `G=Ξ`.
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
| E-neg (finite record does not identify Ξ — per-`N` non-identifiability, §3) | PROOF-DRAFT ✓ CONFIRMED (OB-03, 2026-08-11); restated per-`N` not sequence (OB-28) |
| Quantitative tail estimate §3: matching via log power sums | PROOF-DRAFT ✓ CONFIRMED (OB-03, 2026-08-11) — corrected IFT via Φ_r system |
| Quantitative tail estimate §3: exact Vandermonde Jacobian (no bounded factor) | PROOF-DRAFT ✓ CONFIRMED — ∂Φ_r/∂u_ℓ = r·a_ℓ^{r-1} exactly |
| Quantitative tail estimate §3: separation via Cauchy coefficient estimate | PROOF-DRAFT ✓ CONFIRMED — replaces invalid ratio argument at R=γ_{k+1} |
| Quantitative tail estimate §3: c_0 must be < δ(k,J,{γ_n}) | PROOF-DRAFT ✓ CONFIRMED — IFT gives explicit δ |
| Original Steps B and C of outsource OB-03 | REFUTED as written — must use corrected §3 above |
| Normalization convention (CCM frozen) | DONE |
| Suzuki meromorphic target | OUT OF SCOPE for this theorem (see limitations.md) |
