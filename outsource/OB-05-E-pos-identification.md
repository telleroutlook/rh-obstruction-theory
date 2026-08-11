# Problem OB-05 — E-pos: Evenness Argument Pins G = Ξ

**Type:** complex analysis (entire functions, Hadamard factorization, normal families)  
**Non-circularity:** RH is not assumed anywhere. The γ_n are the positive imaginary parts
of the nontrivial zeros of ζ (treated as given positive real numbers satisfying the
convergence condition Σ γ_n^{-2} < ∞); their location on the critical line is NOT
assumed. The theorem is about identifying a limit function G using analytic properties
alone — it is not about proving G = Ξ implies RH.

---

## All definitions (self-contained — everything is here)

**ξ and Ξ.** Define
```
ξ(s) = (1/2) s(s-1) π^{-s/2} Γ(s/2) ζ(s),
Ξ(z) = ξ(1/2 + iz).
```
Then Ξ is an even real entire function of order 1. Its positive zeros are
{γ_n : n ≥ 1}, γ_1 ≈ 14.134, γ_n → ∞. Because Ξ is even, its full zero
multiset is {±γ_n : n ≥ 1}. The normalization Ξ(0) = ξ(1/2) > 0 is a fixed
positive real number (approximately 0.4971). The Hadamard product is:
```
Ξ(z) = Ξ(0) · ∏_{n≥1} (1 − z²/γ_n²),
```
which converges locally uniformly on ℂ since Σ γ_n^{-2} < ∞.

**Order of an entire function.** An entire function f has order ρ ≤ 1 if
|f(z)| = O(e^{C|z|}) for some C > 0.

**Hadamard factorization theorem.** (Levin, *Distribution of Zeros of Entire
Functions*, Chapter 1, Theorem 3; or Titchmarsh, *Theory of Functions*, §8.24.)
If f is an entire function of order ≤ 1 with zeros {z_n} (Σ |z_n|^{-2} < ∞,
each z_n ≠ 0), and f(0) ≠ 0, then:
```
f(z) = f(0) · e^{az+b} · ∏_n (1 − z/z_n) e^{z/z_n}
```
for unique constants a, b ∈ ℂ. If all zeros are symmetric ±α_n (with
Σ α_n^{-2} < ∞ and f(0) ≠ 0), then:
```
f(z) = f(0) · e^{az+b} · ∏_{n≥1} (1 − z²/α_n²).
```

**Even entire function.** f is even if f(z) = f(−z) for all z ∈ ℂ.

**Hurwitz's theorem.** (Standard; Titchmarsh §3.45.) If (F_N) are analytic on a
domain D and F_N → G locally uniformly, and G is not identically zero, then:
every zero of G in D is a limit of zeros of F_N (with multiplicity); and if
z_* ∈ D is not a zero of G, then for large N, F_N has no zeros in a small
disk around z_*.

**γ_n as given data.** Throughout, {γ_n : n ≥ 1} is the fixed sequence of
positive zeros of Ξ, satisfying γ_n ∼ 2πn/log n (von Mangoldt law). No
assumption on γ_n being on the critical line of ζ is made — they are simply
the given zeros of Ξ.

---

## The claims to be verified

### Claim A (Hadamard evenness pin)

**Claim A.** Let G be an entire function satisfying:
- (i) G has order ≤ 1;
- (ii) G is even: G(z) = G(−z);
- (iii) G has zero multiset exactly {±γ_n : n ≥ 1} (same as Ξ, with the same
  multiplicities), and G(0) ≠ 0;
- (iv) G(z_0) = Ξ(z_0) at some fixed point z_0 ∈ ℂ with Ξ(z_0) ≠ 0.

Then G = Ξ.

*Proposed proof.* By Hadamard (applied to G with zeros {±γ_n}, G(0) ≠ 0, order ≤ 1):
```
G(z) = G(0) · e^{az+b} · ∏_{n≥1} (1 − z²/γ_n²)
```
for some a, b ∈ ℂ. Condition (ii): G(z) = G(−z) gives
```
G(0) · e^{az+b} · P(z) = G(0) · e^{−az+b} · P(z),
```
where P(z) = ∏(1 − z²/γ_n²) is even. Hence e^{az} = e^{−az} for all z, forcing a = 0.
Then G(z) = G(0) e^b · ∏(1 − z²/γ_n²). Condition (iv):
```
G(0) e^b · ∏(1 − z_0²/γ_n²) = Ξ(z_0) = Ξ(0) · ∏(1 − z_0²/γ_n²).
```
Since Ξ(z_0) ≠ 0, the product ∏(1 − z_0²/γ_n²) ≠ 0. Therefore G(0) e^b = Ξ(0),
giving G(z) = Ξ(0) · ∏(1 − z²/γ_n²) = Ξ(z). ☐

**What to close for Claim A:** Verify each step is airtight:
1. The Hadamard factorization applies (confirm order ≤ 1 and G(0) ≠ 0 are used correctly).
2. The evenness step: is e^{az+b} = e^{−az+b} → a = 0 correct, even if a ∈ ℂ?
3. The normalization step: confirm ∏(1 − z_0²/γ_n²) ≠ 0 follows from Ξ(z_0) ≠ 0.
4. Any gap: can the proof fail if the zeros {±γ_n} are not "simple" (some γ_n equal)?
   (For the Riemann zeros, simplicity is expected but not proved; the argument
   requires at minimum that the multisets agree with multiplicities.)

### Claim B (Hurwitz zero-set convergence)

The E-pos proof uses a limiting sequence F_N → G and claims G has exactly the
zero multiset {±γ_n}. This requires a careful Hurwitz argument.

**Setup.** Let (F_N)_{N≥1} be a sequence of entire functions converging locally
uniformly on ℂ to G. Assume:
- (H-zero) For each N, the zero multiset of F_N is {±α_n^{(N)} : n ≥ 1}, where
  α_n^{(N)} ∈ ℝ, α_n^{(N)} > 0 for all n, and for every fixed n:
  α_n^{(N)} → γ_n as N → ∞.
- (H-uniform) The convergence F_N → G is locally uniform (uniform on every
  compact subset of ℂ).
- (H-nonzero) G is not identically zero.

**Claim B.** Under (H-zero), (H-uniform), (H-nonzero), the zero multiset of G
is exactly {±γ_n : n ≥ 1}.

*Proposed proof.*

**G has zero at each ±γ_n:** Fix n. Since α_n^{(N)} → γ_n and F_N(α_n^{(N)}) = 0,
and F_N → G locally uniformly, applying Hurwitz's theorem to the closed disk
B(γ_n, ε) for small ε: since zeros α_n^{(N)} ∈ B(γ_n, ε) for large N, by Hurwitz,
G has a zero in B(γ_n, ε). Since ε was arbitrary, G(γ_n) = 0 (taking ε → 0 and
using that zeros of G are isolated since G ≢ 0). By symmetry G(−γ_n) = 0.

**G has no other zeros:** Let z_* ∉ {±γ_n}. There exists δ > 0 such that
|z_* − (±γ_n)| ≥ δ for all n. By (H-zero), for large N, all zeros α_n^{(N)} of
F_N satisfy |z_* − (±α_n^{(N)})| ≥ δ/2 for all n (since α_n^{(N)} → γ_n and
the γ_n are separated from z_*). Hence F_N has no zeros in B(z_*, δ/2) for large N.
By Hurwitz, G has no zeros in B(z_*, δ/2), so in particular G(z_*) ≠ 0.

**What to close for Claim B:**
1. Is the Hurwitz argument for "G has zero at γ_n" rigorous? (The subtlety: we need
   F_N to have zeros CONVERGING to γ_n in a fixed disk, not just the n-th zero converging.)
2. For "G has no other zeros": does the separation argument work uniformly? Specifically:
   for z_* fixed and NOT equal to any γ_n, can we always find δ > 0 and N_0 such that
   for N ≥ N_0, all zeros of F_N stay δ/2-away from z_*? The issue: γ_n → ∞, so
   for large n, z_* may be close to γ_n. Is the separation argument valid?

**Gap to fill:** The argument "for large N, F_N has no zeros in B(z_*, δ/2)" requires
knowing that F_N has ONLY the zeros {±α_n^{(N)}}, i.e., no "extra" zeros outside
this listed set. Is this guaranteed by the structure of the construction, or does it
need to be an explicit part of hypothesis (H-zero)?

### Claim C (combined: G = Ξ from the hypotheses of E-pos)

Combining Claims A and B: under (H-zero), (H-uniform), (H-nonzero), plus G is even
of order 1 and G(z_0) = Ξ(z_0) ≠ 0, conclude G = Ξ.

---

## Proof skeleton to be closed

### Step 1 — Verify Claim A (Hadamard pin by evenness)

The algebraic argument above appears to be complete. Verify:
- The step e^{az} = e^{−az} for all z ∈ ℂ implies a = 0: CONFIRM (differentiate at z=0).
- No issue with a ∈ ℂ (complex a): CONFIRM (same argument, a = 0 over ℂ).
- Cite the precise theorem from Titchmarsh or Levin for the Hadamard factorization
  for even entire functions.

**What to close for Step 1:** Produce a clean, citable proof of Claim A, confirming
or refuting each sub-step.

### Step 2 — Verify Claim B (Hurwitz zero convergence)

The gap: the argument "G has no other zeros" requires F_N to have exactly the listed
zeros. Specify the precise form of hypothesis (H-zero) that makes Claim B rigorous.

**What to close for Step 2:** Determine whether Claim B holds under the stated (H-zero),
or whether an additional hypothesis is needed (e.g., "F_N has exactly the zero multiset
{±α_n^{(N)}} and no others"). If additional hypotheses are needed, state them precisely.

### Step 3 — Assemble Claim C

Given Steps 1 and 2: write out the complete proof of G = Ξ from the E-pos hypotheses.
Identify any remaining gap.

---

## Acceptance criteria

1. **CONFIRMED** for Claim A: the evenness + Hadamard + normalization argument is
   verified to be rigorous with precise citations; no gap remains.

2. **CONFIRMED** for Claim B: the Hurwitz argument gives G has exactly the zero multiset
   {±γ_n}, and the precise form of (H-zero) needed is stated; OR a gap is identified and
   an explicit additional hypothesis is stated to close it.

3. **PARTIAL**: one of Claims A or B is confirmed, the other has an identified gap
   with a precise fix (additional hypothesis or corrected argument).

4. **REFUTED**: one of Claims A or B fails as stated; a counterexample or gap is given.
   The reviewer should state which alternative identification step (if any) replaces it.

5. **INCONCLUSIVE**: the argument is plausible but cannot be decided without further
   information about (H-zero) or the order of G.

All outcomes must be decisive: "it seems right" is not CONFIRMED. A CONFIRMED verdict
requires a proof; a REFUTED verdict requires a counterexample or identified logical gap.

---

## Numerical anchor (sanity only — not an input to the proof)

The simplest check: take the single-zero function
```
G_1(z) = Ξ(0)(1 − z²/γ_1²),   γ_1 ≈ 14.134.
```
This is a degree-2 polynomial, even, with G_1(0) = Ξ(0) > 0.
A sequence F_N = Ξ(0) ∏_{n=1}^{N}(1 − z²/γ_n²) converges locally uniformly
to Ξ (by standard product convergence since Σ γ_n^{-2} < ∞).
Check: the claim G = Ξ applies to the limit with z_0 = 0, G(0) = Ξ(0).
This is trivially confirmed for this sequence. The non-trivial content is
for sequences where α_n^{(N)} ≠ γ_n for n > some threshold.
