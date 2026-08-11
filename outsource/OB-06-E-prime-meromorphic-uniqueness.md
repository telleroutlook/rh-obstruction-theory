# Problem OB-06 — Meromorphic Hadamard Uniqueness and Marty's Theorem Application

**Type:** complex analysis (meromorphic functions of order 1, normal families,
Mittag-Leffler products)  
**Non-circularity:** RH is not assumed. The sequences {γ_n} and {d_n} are treated
as given sequences of positive real numbers satisfying growth conditions. Nothing
about the location of ζ zeros is assumed. The theorem concerns whether finitely many
data points determine a meromorphic function — a pure complex-analysis question.

---

## All definitions (self-contained — everything is here)

**Meromorphic function of order 1.** A meromorphic function f is of order ≤ 1 if
its Nevanlinna characteristic T(r, f) = O(r), equivalently, if |f(z)| = O(e^{C|z|})
away from neighborhoods of the poles.

**Mittag-Leffler/Weierstrass factorization for meromorphic functions of order 1.**
(Titchmarsh, *Theory of Functions* §8.7; Levin, *Distribution of Zeros of Entire
Functions*, Chapter 5.) Let f be meromorphic of order ≤ 1 with:
- zeros {z_k} (Σ |z_k|^{-2} < ∞, each z_k ≠ 0);
- poles {p_k} (Σ |p_k|^{-2} < ∞, each p_k ≠ 0);
- f(0) defined (0 is neither a zero nor pole).

Then:
```
f(z) = f(0) e^{az+b} · [∏_k (1 − z/z_k) e^{z/z_k}] / [∏_k (1 − z/p_k) e^{z/p_k}]
```
for unique a, b ∈ ℂ. If zeros and poles are all purely imaginary ±iα_k, ±iβ_k, the
product simplifies (even structure pins a = 0 by the same argument as in OB-05).

**The target meromorphic function W.** Define
```
W(z) = z² ξ(1/2 − iz) / ξ'(1/2 − iz),
```
where ξ(s) = (1/2) s(s-1) π^{-s/2} Γ(s/2) ζ(s). Under RH (assumed for motivation
only — the structure of W is defined unconditionally):
- W is meromorphic of order 1;
- poles of W are at z = γ_n (positive Riemann zero ordinates) and z = −γ_n;
- zeros of W: at z = 0 (double) plus the zeros of ξ(1/2 − iz) not coming from
  poles of ξ'/ξ — i.e., at z where ξ'(1/2 − iz) = 0 (zeros of the derivative);
- W(w_0) is defined and nonzero for generic w_0.
- W(z) = W(−z) (W is even — from the functional equation ξ(s) = ξ(1−s)).

**Residue of W at γ_n.** Assuming γ_n is a simple zero of ξ, let p = 1/2 − iγ_n.
Then ξ(p) = 0 and ξ'(p) ≠ 0. Near z = γ_n:
```
ξ(1/2 − iz) = ξ(p + (−i)(z − γ_n)) = (−i)(z − γ_n) ξ'(p) + O((z−γ_n)²).
```
Therefore:
```
Res_{z=γ_n} W(z) = lim_{z→γ_n} (z − γ_n) · z² · ξ(1/2−iz) / ξ'(1/2−iz)
                  = γ_n² · lim_{z→γ_n} (z − γ_n) · (−i)(z−γ_n)ξ'(p) / [(−i)ξ'(p)]
                  [numerator grows as (z−γ_n)², denominator as (z−γ_n)]
```
More carefully: ξ'(1/2 − iz) at z → γ_n is ξ'(p) · (−i) ≠ 0 (to leading order), so
the pole is simple and:
```
Res_{z=γ_n} W(z) = γ_n² · [(−i) ξ'(p)] / [(−i) ξ'(p)] = −i γ_n².
```
So the residue is **R_n = −i γ_n²**. This is purely imaginary and nonzero for γ_n > 0.

*Verification (sanity):* For γ_1 ≈ 14.134, R_1 = −i · 14.134² ≈ −199.77 i. The
residue is independent of ξ'(p) (it cancels), confirming robustness under rescaling.

*Note:* The simplicity of zeros of ξ is an open problem (known to hold for the
first ~10^{13} zeros numerically). The Theorem E' proof assumes this as an explicit
hypothesis of the method class 𝔐_Suz.

**Method class 𝔐_Suz (finite evidence).** A sequence (F_N)_{N≥1} is in 𝔐_Suz if each
F_N is meromorphic of order 1 satisfying:
- poles of F_N are {±p_k^{(N)} : k = 1, …, K_N}, K_N → ∞;
- F_N(w_0) = W(w_0) at a fixed base point w_0 (not a pole or zero of W);
- the first J_N Taylor coefficients of F_N at w_0 match those of W;
- F_N is even: F_N(z) = F_N(−z).

**Even meromorphic function.** F is even if F(z) = F(−z). An even meromorphic
function of order 1 with poles at ±p_k has the Weierstrass–Mittag-Leffler
factorization with a = 0 (same parity argument as for entire functions).

**Marty's theorem / normal families of meromorphic functions.** (Marty 1931;
see Schiff, *Normal Families*, Theorem 1.10; or Beardon–Minda, *Spherical
Geometry and Normal Families*.) A family ℱ of meromorphic functions on a domain
D is a normal family (every sequence has a subsequence converging locally uniformly
in the spherical metric) if and only if
```
sup_{f ∈ ℱ} f^#(z) < ∞   locally uniformly in z,
```
where f^#(z) = |f'(z)| / (1 + |f(z)|²) is the spherical derivative.

A sufficient condition: if (F_N) are meromorphic on D, the poles of F_N are
separated from the domain of interest, and |F_N| is locally uniformly bounded
away from the poles, then {F_N} is normal (apply Montel's theorem for analytic
functions in the pole-free region).

---

## The claims to be verified

### Claim A: Meromorphic Hadamard uniqueness — exact statement and proof

**Lemma E'.1 (proposed).** Let F, G be meromorphic functions of order ≤ 1, both even,
with:
- the same multiset of poles {±p_k : k ≥ 1} with Σ |p_k|^{-2} < ∞;
- the same multiset of zeros {±z_j : j ≥ 1} with Σ |z_j|^{-2} < ∞;
- F(w_0) = G(w_0) ≠ 0 at some non-pole point w_0.

Then F = G.

*Proposed proof.* Write F = P/Q and G = P'/Q' where P = ∏(1 − z²/z_j²) e^{z²/z_j²}
(or the appropriate Weierstrass product for the zeros) and Q = ∏(1 − z²/p_k²) e^{z²/p_k²}
(for the poles), and similarly for P', Q'. Since poles are the same: Q and Q' differ by
a nonzero constant C_Q. Since zeros are the same: P and P' differ by e^{az+b} · C_P for
some a, b ∈ ℂ. By evenness, a = 0. The normalization F(w_0) = G(w_0) ≠ 0 forces
C_Q/C_P = 1. Hence F = G.

**What to verify for Claim A:**
1. The Weierstrass–Mittag-Leffler representation for even meromorphic functions of order
   ≤ 1: write out the precise form (which theorem in Titchmarsh §8.7 or Levin?). The
   products P and Q as written above — do they converge for Σ |z_j|^{-2} < ∞?
   (For genus-1 products: e^{z²/z_j²} is the convergence factor, but for order ≤ 1
   with Σ |z_j|^{-2} < ∞ the Weierstrass genus-1 product converges. Confirm.)
2. The step "F = e^{az+b} · C · (P/Q)": is this the correct form, and is the
   exponential factor really e^{az+b} (order ≤ 1 forces at most a linear exponent)?
3. The parity argument a = 0: same as OB-05 Claim A. Confirm it works for meromorphic
   functions (G(z) = G(−z) forces a = 0 in the exponential factor).
4. The normalization step: F(w_0) = G(w_0) with F(w_0) ≠ 0 forces C = 1.
   Confirm C_Q/C_P = 1.
5. **Critical check:** Is the proposed form (P/Q for zeros and poles separately)
   the right Weierstrass–Mittag-Leffler form for meromorphic functions? The standard
   form is more subtle — write out the exact factorization theorem being invoked, by
   theorem number in a standard reference.

### Claim B: Marty's theorem application to (F_N)

**Setup.** Let (F_N) be a sequence in 𝔐_Suz, with poles {±p_k^{(N)}} converging
to {±γ_k} as N → ∞ (for each fixed k). Assume:
- (H'-bound): |F_N(z)| ≤ M_K for |z| ≤ K, z outside all disks B(p_k^{(N)}, δ_K)
  of radius δ_K > 0 around each pole; M_K and δ_K depend only on K (not on N).
- (H'-pole-sep): The poles p_k^{(N)} are separated from any compact set disjoint from
  {γ_k}: for z in a fixed compact K_0 with dist(z, {±γ_k}) > δ > 0, all poles
  p_k^{(N)} stay at distance > δ/2 from K_0 for large N.

**Claim B.** Under (H'-bound) and (H'-pole-sep), the sequence (F_N) restricted to
any compact K_0 with dist(K_0, {±γ_k}) > 0 has a subsequence converging locally
uniformly on K_0.

*Proposed argument.* On K_0, (F_N) is analytic (poles are away from K_0 by
(H'-pole-sep)) and uniformly bounded (by (H'-bound)). By Montel's theorem for
analytic functions, (F_N|_{K_0}) is a normal family, hence has a uniformly convergent
subsequence on K_0.

**What to verify for Claim B:**
1. Does this argument correctly apply Montel's theorem (for analytic functions,
   not Marty's theorem for meromorphic)? Montel's theorem: locally uniformly bounded
   analytic functions → normal family. This is more elementary than Marty's theorem.
   When is Marty's theorem (spherical derivative bound) actually needed in this context,
   vs. when is Montel sufficient?
2. Is there a step in the E'-pos proof where the poles cannot be "pushed away" from
   the compact of interest (because {γ_k} accumulate in the domain of convergence)?
   If K_0 is required to contain neighborhoods of finitely many poles, Montel does
   not directly apply. State precisely when the pole-separation hypothesis (H'-pole-sep)
   is needed vs. when an augmented Marty argument is necessary.
3. The sequence of compacts: to get locally uniform convergence on all of ℂ (minus
   the poles), one needs a diagonal argument over compacts. Does this work given that
   each limit on K_j might be a different subsequence? Specify whether a single
   subsequence works or a diagonal construction is needed.

### Claim C: Simplicity-of-zeros assumption — scope

The residue formula R_n = −i γ_n² (derived above) requires γ_n to be a SIMPLE
zero of ξ. The E'-neg construction and E'-pos limit identification both use this.

**Claim C.** State precisely: which parts of the E' theorems (statement.md §3–§5)
require the simplicity of zeros of ξ? What happens if some γ_n is a multiple zero?

**What to verify for Claim C:**
1. The Vandermonde IFT argument in E'-neg (§4): does it require simple poles of W
   (i.e., simple zeros of ξ), or does it work with higher-order poles?
2. The limit identification in E'-pos: does G = W require that the poles of G are
   simple (so that the pole data pins the function exactly)?
3. If simplicity fails: is the E' theorem vacuous (no example in 𝔐_Suz), or does
   it apply with multiplicities explicitly stated?

---

## Proof skeleton to be closed

### Step 1 — Meromorphic factorization theorem (Claim A)

Find and state the precise version of the Weierstrass–Mittag-Leffler factorization
for even meromorphic functions of order ≤ 1 used in Claim A. Cite by theorem number.
Confirm the proof of Lemma E'.1 is rigorous under this factorization.

**Acceptance:** either the proof is CONFIRMED with a precise citation by theorem
number (e.g. "Titchmarsh §8.7, Theorem X"), or a gap is identified and a precise
fix is given.

### Step 2 — Marty vs Montel (Claim B)

Determine whether the E'-pos argument requires Marty's theorem or whether Montel's
theorem for analytic functions suffices on any pole-free compact.

**Acceptance:** a clear decision: MONTEL SUFFICES or MARTY NEEDED, with the
argument for which case applies and what (H'-bound)/(H'-pole-sep) must be assumed.

### Step 3 — Simplicity scope (Claim C)

Determine the exact role of the simplicity-of-zeros assumption in E'-neg and E'-pos.

**Acceptance:** a precise statement of which results require simple zeros and which
do not; and whether the method class 𝔐_Suz should explicitly include or exclude
the case of multiple zeros.

---

## Acceptance criteria

1. **CONFIRMED** for each of Claims A, B, C: rigorous with precise citations.
2. **PARTIAL**: some claims confirmed, others have identified gaps with precise fixes.
3. **REFUTED**: a specific claim fails as stated; a counterexample or gap is given;
   the minimal additional hypothesis needed to repair it is stated.
4. **INCONCLUSIVE**: the argument cannot be decided without additional information
   (specify what is missing).

For Claims A–C all outcomes are acceptable; no false-dichotomy between "proved" and
"disproved." A PARTIAL or INCONCLUSIVE with a precise gap description is a valid result.

---

## Numerical anchor (sanity only — not an input)

For Lemma E'.1: take the explicit example
```
F(z) = (1 − z²/4) / (1 − z²/9),   G(z) = 2 · (1 − z²/4) / (2 − 2z²/9).
```
Both have poles at ±3 and zeros at ±2, and are even. F(0) = G(0) = 1 ≠ 0.
Check F = G: F(z) = (1 − z²/4)/(1 − z²/9), G(z) = (1 − z²/4)/(1 − z²/9). Yes, equal.

For a case where uniqueness FAILS: by OB-04 (Hadamard uniqueness for entire functions
is false without parity constraint), check that the MEROMORPHIC case also fails without
parity: e.g., F(z) = 1/(1 − z/3) and G(z) = e^z/(1 − z/3) — same pole at z=3,
no zeros, but F(0) = G(0) = 1. These are NOT even. The parity constraint is essential.
