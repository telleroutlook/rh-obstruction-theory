# Problem OB-09 — E'-neg: IFT matching system for odd meromorphic target

**Type:** complex analysis (meromorphic functions of Nevanlinna order ≤ 1,
implicit function theorem, Vandermonde-type Jacobians)

**Non-circularity:** RH is not assumed and zero locations of ζ are not used
as inputs. The sequences {γ_n} below are abstract positive reals satisfying a
growth condition (analogous to Riemann zero ordinates, but treated axiomatically).
No Euler product, functional equation for ζ, or spectral property of ζ is assumed.

---

## All definitions (self-contained — everything is here)

### The target function W

Define
```
W(z) = z² · A(z) / B(z),
```
where A, B are entire functions with the following properties:

- **A is even:** A(−z) = A(z).
- **B is odd:** B(−z) = −B(z).  (Hence B has a simple zero at 0: B(z) = z·B̃(z)
  with B̃(0) ≠ 0, B̃ even.)
- **Nevanlinna order:** T(r, A) = O(r) and T(r, B) = O(r).
- **Zero divisor of A:** simple zeros at {±γ_n : n ≥ 1} where 0 < γ_1 < γ_2 < …,
  γ_n → ∞, Σ γ_n^{−2} < ∞.  No other zeros.  A(0) ≠ 0.
- **Zero divisor of B:** simple zeros at {z_k^B : k ≥ 1} (positions not assumed
  real), with Σ |z_k^B|^{−2} < ∞.  Also a simple zero at 0 (the z in B = z·B̃).

Under these conditions W = z²·A/B is **odd**: W(−z) = −z²·A(−z)/B(−z) = −z²·A/B = −W(z).
W has simple zeros at {±γ_n} (zeros of A become zeros of W because B(±γ_n) ≠ 0 by
assumption) and poles at zeros of B other than 0 (the z² in the numerator and the simple
zero of B at 0 cancel: near z=0, W(z) = z²·A(0)/(z·B̃(0)) + O(z²) so W has a simple zero
at 0, not a pole).

**Growth of W near the imaginary axis.**  For R > 0:
```
|W(iR)| ≥ C · |A(iR)|,    |A(iR)| ≥ |A(0)| · 2^{N(R)},
```
where N(R) := #{n : γ_n ≤ R} → ∞.  Hence |W(iR)| → ∞ as R → ∞.

**Numerical values (sanity only, not analytic inputs):**
γ_1 ≈ 14.134, γ_2 ≈ 21.022, γ_3 ≈ 25.010.

### The method class 𝔐_Suz

Fix k ≥ 1 (the first k zeros are "frozen") and J ≥ 1 (the number of Taylor
conditions to match).  A function F belongs to the admissible perturbation class if:

1. F is meromorphic with T(r, F) = O(r).
2. F is **odd**: F(−z) = −F(z).
3. The zeros of F at {±γ_1,…,±γ_k} are simple and match W exactly.
4. The poles of F are exactly the poles of W (same positions and multiplicities).
5. F(w₀) = W(w₀) at a fixed base point w₀ with w₀ ≠ 0 and W(w₀) ≠ 0,
   w₀ not a zero or pole of W.
6. The first J Taylor coefficients of F at w₀ match those of W:
   F^{(j)}(w₀) = W^{(j)}(w₀)  for j = 0, 1, …, J−1.

The "tail" zeros of F at positions {±μ_{k+1}, ±μ_{k+2}, …} (where μ_n are
free parameters, replacing γ_n for n > k) are not constrained by conditions 1–6
beyond Σ μ_n^{−2} < ∞ (needed for Nevanlinna order ≤ 1).

### The perturbation family

For a small parameter c ≠ 0, define the perturbed zero positions:
```
μ_n(c) = γ_n · (1 + c/(n−k))    for n > k.
```
(So μ_n(0) = γ_n and for n > k+J the positions are free; for k < n ≤ k+J
they will be adjusted by the IFT to enforce condition 6.)

Define the perturbed function:
```
F^{(c)}(z) = z² · A^{(c)}(z) / B(z),
```
where A^{(c)} is the even entire function with simple zeros at {±γ_1,…,±γ_k} ∪
{±μ_n(c) : n > k} and A^{(c)}(0) = A(0):
```
A^{(c)}(z) = A(0) · ∏_{n=1}^k (1 − z²/γ_n²) · ∏_{n>k} (1 − z²/μ_n(c)²).
```
This product converges locally uniformly since Σ μ_n(c)^{−2} < ∞ for |c| < 1
(using μ_n(c) ≥ γ_n/2 for large n).

F^{(c)} is odd (z² · even/odd with numerator even = odd), has the correct poles
(same as W), and has F^{(c)}(0) = 0 (simple zero at 0, same as W).

### The log-power-sum matching system

The Taylor coefficients of W at w₀ are determined by the logarithmic derivative:
```
(d/dz) log A^{(c)}(z) = −2z · Σ_{n≥1} 1/(z² − μ_n(c)²)
                        = −Σ_{r≥0} 2·P_{r+1}(c) · z^{2r+1},
```
where `P_r(c) = Σ_{n≥1} μ_n(c)^{−2r}` are the Newton power sums of the
reciprocal-square variables.

Define **reciprocal-square variables**:
```
u_ℓ(c) = μ_{k+ℓ}(c)^{−2}   for ℓ = 1,…,J    (the "free" variables near k+1,…,k+J),
b_m(c) = μ_{k+J+m}(c)^{−2} for m ≥ 1         (the "frozen tail"; no free parameter),
a_n    = γ_n^{−2}            for n ≥ 1         (the W reference values).
```
At c = 0: u_ℓ(0) = a_{k+ℓ}, b_m(0) = a_{k+J+m}.

The matching conditions F^{(j)}(w₀) = W^{(j)}(w₀) for j = 0,…,J−1 are
equivalent (after extracting the common pole contribution from B and the
z² factor) to the J scalar equations:
```
Φ_r(u, c) := Σ_{ℓ=1}^J u_ℓ^r  +  Σ_{m≥1} b_m(c)^r  −  Σ_{n≥1} a_n^r  =  0,
             for r = 1, 2, …, J.                                           (★)
```
(This is the same system as in OB-03 / E-neg §3; the odd/meromorphic structure of F
versus the entire structure of E-neg does not affect the matching equations because
the pole factor B and the z² factor are common to both F^{(c)} and W and cancel in
the Taylor matching.)

---

## The claims to be verified

### Claim A: IFT applies to the system (★)

**Claim A.** At `(u, c) = (u⁰, 0)` with `u_ℓ⁰ = a_{k+ℓ}`:

1. Φ_r(u⁰, 0) = 0 for all r = 1,…,J.  (Trivially true by definition.)

2. The Jacobian `∂Φ_r/∂u_ℓ (u⁰, 0) = r · a_{k+ℓ}^{r−1}`.

3. `det[∂Φ_r/∂u_ℓ]_{r,ℓ=1}^J = (∏_{r=1}^J r) · ∏_{1 ≤ p < q ≤ J} (a_{k+q} − a_{k+p}) ≠ 0`.
   (This is a scaled Vandermonde determinant; nonzero since a_{k+1} > a_{k+2} > … > 0
   are strictly decreasing.)

4. The map Φ: ℝ^J × ℝ → ℝ^J is C^1 near (u⁰, 0), with:
   - The series Σ_{m≥1} b_m(c)^r converging uniformly in c near 0 (since b_m(c) ≤
     2a_{k+J+m} for |c| < 1, and Σ a_n^r < ∞ for r ≥ 1).
   - The c-derivative ∂b_m/∂c(0) = −2a_{k+J+m}/(k+J+m−k) = −2a_{k+J+m}/m
     (computable explicitly; the series Σ_m |∂b_m/∂c| < ∞ converges).

Therefore the Implicit Function Theorem (Banach-space version or finite-dimensional
C^1 IFT) applies: there exist δ > 0 and a unique C^1 map c ↦ u(c) for |c| < δ with
u(0) = u⁰ and Φ(u(c), c) = 0.

**What to verify for Claim A:**
1. Confirm entry 2: `∂Φ_r/∂u_ℓ = r · u_ℓ^{r−1}` at u_ℓ = u_ℓ⁰.
2. Confirm entry 3: the resulting determinant is the stated scaled Vandermonde.
3. Confirm entry 4: the uniform convergence and C^1 regularity of Φ in c.
4. **Critical:** does the odd/meromorphic structure of F^{(c)} cause any modification
   to the system (★)?  Specifically: does the common factor z²/B(z) contribute terms
   to the Taylor matching that differ from the entire case?

   *The answer should be NO*: at a non-pole base point w₀, the contribution of
   z²/B(z) to the Taylor expansion at w₀ is a fixed function of w₀ (not depending on
   the tail zeros), and so it cancels from the matching equation F^{(j)}(w₀) = W^{(j)}(w₀).
   Confirm this explicitly.

### Claim B: F^{(c)} ≠ W for small c ≠ 0

**Claim B.** For 0 < |c| < δ (with δ from Claim A), `F^{(c)} ≠ W`.

*Proposed argument.* Define the (J+1)-th power sum discrepancy:
```
Δ_{J+1}(c) := Σ_{ℓ=1}^J u_ℓ(c)^{J+1}  +  Σ_{m≥1} b_m(c)^{J+1}  −  Σ_{n≥1} a_n^{J+1}.
```
At c = 0: Δ_{J+1}(0) = 0.  Differentiate using `v_ℓ = u_ℓ'(0)` (from IFT) and
`∂b_m/∂c(0) = −2a_{k+J+m}/m`:
```
Δ_{J+1}'(0) = (J+1)[ Σ_ℓ v_ℓ · a_{k+ℓ}^J  −  Σ_{m≥1} (2/m) a_{k+J+m}^{J+1} ].
```
Let q(x) = ∏_{ℓ=1}^J (x − a_{k+ℓ}).  From differentiating Φ_r(u(c),c) = 0:
```
Σ_ℓ v_ℓ · a_{k+ℓ}^J  −  Σ_{m≥1} (2/m) a_{k+J+m}^{J+1}  =  −Σ_{m≥1} (2/m) a_{k+J+m} · q(a_{k+J+m}).
```
For m ≥ 1: a_{k+J+m} < a_{k+J} < a_{k+J−1} < … < a_{k+1}, so each a_{k+J+m} is below
all J roots of q.  Since q has degree J with leading coefficient 1, q(x) has sign (−1)^J
for all x < a_{k+J}.  The series Σ (2/m) a_{k+J+m} |q(a_{k+J+m})| converges (terms
bounded by 2|q|_∞/m and q is bounded on {a_n : n ≥ k+J+1}).  The series is nonzero
(all terms have the same sign).  Hence Δ_{J+1}'(0) ≠ 0, so Δ_{J+1}(c) ≠ 0 for
0 < |c| < δ (shrinking δ if needed).

Non-zero Δ_{J+1}(c) means the (J+1)-th Taylor matching condition fails for F^{(c)}.
By the logarithmic series expansion:
```
F^{(c)}(z) − W(z)  =  −C · Δ_{J+1}(c)/(J+1) · z^{2J+2}  +  O(z^{2J+4})
```
near z = 0 (for z in a neighborhood not containing any pole).  By the Cauchy coefficient
estimate, for every R > 0:
```
sup_{|z| ≤ R} |F^{(c)}(z) − W(z)|  ≥  A_c · R^{2J+2},    A_c = C|Δ_{J+1}(c)|/(J+1) > 0.
```

**What to verify for Claim B:**
1. Confirm the formula for Δ_{J+1}'(0) via differentiation of the IFT solution.
2. Confirm the sign argument: q(a_{k+J+m}) has constant sign for all m ≥ 1.
3. Confirm the series Σ(2/m)a_{k+J+m}·q(a_{k+J+m}) is nonzero.
4. Confirm the Cauchy estimate step: the logarithmic series expansion holds for the
   odd meromorphic F^{(c)} at z near 0 (not at w₀).  Is z = 0 a valid base point for
   the expansion, or does the simple zero of F^{(c)} at 0 cause issues?  (The expansion
   should be of F^{(c)}(z)/z vs W(z)/z — both have removable singularities at 0.)

---

## Proof skeleton to be closed

### Step 1 — Jacobian computation (Claim A, items 1–3)

Compute `∂Φ_r/∂u_ℓ = r · u_ℓ^{r−1}` explicitly.  Show the resulting J×J matrix has
determinant equal to a scaled Vandermonde in {a_{k+1},…,a_{k+J}}, nonzero by
distinctness.

**Acceptance:** CONFIRMED with explicit determinant formula, or REFUTED with the
specific entry that is incorrect.

### Step 2 — C^1 regularity of Φ in c (Claim A, item 4)

Show that c ↦ Σ_{m≥1} b_m(c)^r is C^1 near c=0 for each r = 1,…,J, with
derivative given by Σ_m r · b_m(c)^{r−1} · ∂b_m/∂c.  Verify dominated convergence
applies.

**Acceptance:** CONFIRMED, or identify which r causes a convergence issue.

### Step 3 — No extra terms from z²/B(z) (Claim A, item 4 critical)

Show explicitly that the Taylor matching condition F^{(j)}(w₀) = W^{(j)}(w₀) reduces
to (★) without extra terms from the common factor z²/B(z).

**Acceptance:** CONFIRMED (with the explicit cancellation shown), or PARTIAL (identifying
which j values acquire extra terms that must be separately handled).

### Step 4 — Δ_{J+1}'(0) ≠ 0 (Claim B)

Using the IFT solution, compute Δ_{J+1}'(0) and show it is nonzero.

**Acceptance:** CONFIRMED (with the sign argument for q(a_{k+J+m}) spelled out), or
REFUTED (explicit value of Δ_{J+1}'(0) = 0 with explanation).

---

## Acceptance criteria

1. **CONFIRMED:** Steps 1–4 all verified; F^{(c)} satisfies conditions 1–6 of 𝔐_Suz
   and differs from W for 0 < |c| < δ; quantitative separation by Cauchy estimate holds.

2. **PARTIAL:** some steps confirmed; at least one gap identified with a precise fix.
   The minimum acceptable result: confirm Step 1 (Jacobian computation) and Step 3
   (no extra terms from z²/B).

3. **REFUTED:** one of the steps fails; an explicit counterexample or gap is given;
   the minimal additional hypothesis needed to repair it is stated.

4. **INCONCLUSIVE:** the argument cannot be decided without additional information
   (specify what is missing).

All outcomes must be decisive with precise arguments.  "The argument looks plausible"
is not CONFIRMED.

---

## Numerical anchor (sanity only — not an input)

For J = 1, k = 1, base point w₀ = 2i (far from real axis, not a zero or pole of W):

The Jacobian at Step 1 is a 1×1 matrix: ∂Φ_1/∂u_1 = 1 · a_{k+1}^0 = 1 ≠ 0. ✓

The power sum at c = 0: P_1(0) = Σ γ_n^{−2}.  For γ_n ∼ 2πn/log n this series
converges (compare with Σ (log n)²/n² < ∞).

The tail at Step 2: Σ_{m≥1} |∂b_m/∂c(0)| = Σ_{m≥1} 2a_{k+J+m}/m.  With a_n ∼ (log n)²/(4π²n²),
this is bounded by C·Σ (log n)²/n³ < ∞. ✓

The sign check at Step 4: for J=1, q(x) = x − a_{k+1}.  For m ≥ 1:
a_{k+1+m} < a_{k+1} (since a_n is strictly decreasing), so q(a_{k+1+m}) < 0 for all m.
Δ_2'(0) = 2[Σ_m (−2/m) a_{k+1+m} · (a_{k+1+m} − a_{k+1})] > 0 (all terms positive). ✓
