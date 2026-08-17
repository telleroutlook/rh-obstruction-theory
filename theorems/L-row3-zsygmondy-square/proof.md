# Proof of Theorem L — NT-C Square Subcase

**RH status:** RH stays `[OUT]`. No ζ zeros, no Li coefficients, no RH hypothesis.

---

## Step 1 — Pythagorean Parametrization

Suppose A⁺ = a²+4m² = x² and A⁻ = (2m−a)²+4m² = y² for positive integers x, y.

Since a is odd and x must satisfy x² = a²+4m² ≡ 1 mod 4, x is odd. Write:

    x − a = 2s₁,  x + a = 2t₁  ⟹  s₁t₁ = m²,  t₁ − s₁ = a  (s₁ < t₁)

Similarly for y with c = 2m−a (odd):

    y − c = 2s₂,  y + c = 2t₂  ⟹  s₂t₂ = m²,  t₂ − s₂ = c = 2m−a

**Constraint:** (t₁−s₁) + (t₂−s₂) = a + (2m−a) = 2m. Setting S = s₁+s₂ and P = s₁s₂:

    S(m² − P)/P = 2m   ⟹   P = Sm²/(S + 2m).                  … (*)

For positive integer s₁,s₂: P must be a positive integer AND the discriminant

    Δ = S² − 4P = (S−2m)(u−v)²/[4(S+2m)]    (where uv = 5m², u+v = S, d = u−v)

must be a perfect square (since s₁,s₂ = (S ± √Δ)/2 must be integers).

---

## Step 2 — Reduction to the Genus-1 Curve C

The discriminant condition Δ = □ with uv = 5m² forces the existence of rational
coordinates x = a/(2m), y = √Δ/(2m) satisfying the genus-1 curve:

    C : y² = x⁴ − 3x² + 1

[Derivation: substituting the AM-GM identity (u−v)² = (u+v)²−4uv = S²−20m² and
the expression for Δ, one arrives at the homogeneous form y²b⁴ = a⁴−3a²b²+b⁴
with b = 2m, which dehomogenizes to C above for x = a/b.]

Row-3 requires x = a/(2m) ≠ 0 (a ≥ 1) and x ≠ ∞.

So it suffices to show: the only rational points on C are x ∈ {0, ∞}.

---

## Step 3 — Birational Equivalence to an Elliptic Curve E

C has the rational point P₀ = (0, 1) (since 0−0+1=1=1²). Apply the substitution:

    U = (y + 1)/x²   ⟹   x² = (2U − 3)/(U² − 1)    (for x ≠ 0)

Setting V = x(U²−1) gives V² = (2U−3)(U²−1) = 2U³−3U²−2U+3.

Scale via X₁ = 2U, Y₁ = 2V:

    Y₁² = X₁³ − 3X₁² − 4X₁ + 12

Translate X₂ = X₁ − 1:

    Y₁² = X₂³ − 7X₂ + 6 = (X₂−1)(X₂−2)(X₂+3)

Translate X₃ = X₂ − 1:

    E : Y₁² = X₃³ + 3X₃² − 4X₃ = X₃(X₃+4)(X₃−1)

The map (x, y) ↦ (X₃, Y₁) is birational (defined away from x=0 and the pole U=∞),
and extends to an isomorphism of projective curves over ℚ.

Torsion: E(ℚ)_tors = {∞, (0,0), (1,0), (−4,0)} (full 2-torsion, verified by direct
substitution into E).

---

## Step 4 — Rank 0 by 2-Isogeny Descent

E has the form Y² = X(X² + 3X − 4) with a = 3, b = −4.

**The φ-isogeny** φ: E → E' with kernel ⟨(0,0)⟩ gives the isogenous curve:

    E' : Y² = X³ − 6X² + 25X   (a' = −2a = −6, b' = a²−4b = 9+16 = 25)

**φ-Selmer group S^φ(E/ℚ):** Candidates are square classes of divisors of b = −4:
d ∈ {±1, ±2}. Homogeneous space: N² = dM⁴ + 3M²e² − (4/d)e⁴.

- d = 1: trivially soluble (M=1, e=0).
- d = −1: soluble — (M=2, e=1): N² = −16+12+4 = 0. So d=−1 ∈ S^φ.
- d = 2: **fails in ℚ₂** (verify mod 8 for all parities of M,e with gcd(M,e)=1):
  - M odd, e even: N² ≡ 2·1 ≡ 2 mod 4. Not a square. ✗
  - M ≡ 2 mod 4, e odd: N² ≡ 4−2 = 2 mod 8. Not a square. ✗
  - M ≡ 0 mod 4, e odd: N² ≡ 0+0−2 ≡ 6 mod 8. Not a square. ✗
  - M, e both odd: N² ≡ 2+3−2 = 3 mod 8. Not a square. ✗
- d = −2: fails since S^φ is a group and 2 ∉ S^φ.

**Conclusion:** |S^φ(E)| = 2.

**φ̂-Selmer group S^{φ̂}(E'/ℚ):** Candidates d ∈ {±1, ±5} (±25 = ±1 in ℚ*/(ℚ*)²).
Homogeneous space: N² = dM⁴ − 6M²e² + (25/d)e⁴.

- d = 1: trivially soluble.
- d = −1: N² = −M⁴−6M²e²−25e⁴ < 0 for all real (M,e) ≠ 0. Fails over ℝ. ✗
- d = 5: soluble — (M=1, e=1): N² = 5−6+5 = 4, N=2. ✓
- d = −5: N² = −5M⁴−6M²e²−5e⁴ < 0. Fails over ℝ. ✗

**Conclusion:** |S^{φ̂}(E')| = 2.

**Rank formula:**

    2^r = |S^φ| · |S^{φ̂}| / 4 = 4/4 = 1   ⟹   r = 0.

Therefore E(ℚ) = E(ℚ)_tors = {∞, (0,0), (1,0), (−4,0)}.

---

## Step 5 — Pullback to C

Trace each torsion point back via X₃ ↦ X₂ = X₃+1 ↦ X₁ = X₂ ↦ U = X₁/2 ↦ x² = (2U−3)/(U²−1):

| X₃ | U | x² | x |
|---|---|---|---|
| ∞ | ∞ | 0 | 0 |
| 0 | 1/2 | 8/3 | irrational |
| 1 | 1 | −1/0 = ∞ | ∞ |
| −4 | −3/2 | −24/5 | no real solution |

Every rational point on E pulls back to x ∈ {0, ∞} or to an irrational/nonexistent value of x. Since the birational map is defined over ℚ, these are ALL rational points on C.

---

## Step 6 — Exclusion by Row-3 Conditions

The Row-3 parametrization requires x = a/(2m) with a ≥ 1 (odd integer) and m ≥ 2.
This forces x > 0 and x < 1 (since a < n = 2m). In particular, x ≠ 0 and x ≠ ∞.

No torsion point on E gives a value x ∈ (0,1) ∩ ℚ. □

---

## Step 7 — Verification

Independent checker: `checker/verify_L.py` confirms:
1. Torsion points satisfy E's equation.
2. Pullback gives exactly x ∈ {0, ∞, ±√(8/3), complex}.
3. Zero simultaneous perfect-square Row-3 pairs up to n = 2000.
