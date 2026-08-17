# Problem OE-02 — NT-C t=1 open case: simultaneous (5S², 5T²) for 4∤n

**Type:** Pure arithmetic / Diophantine (elliptic curves, Gaussian integers, quadratic norms)

**Non-circularity:** All hypotheses are elementary arithmetic over ℤ and ℤ[i]. No zeros of ζ, no RH, no Li coefficients, no ordinate values. RH stays `[OUT]`.

**Relation to OE-01.** OE-01 covers the cube-factor case (t≥2 in the Erdős–Szekeres
decomposition A± = s²t³). This problem handles the remaining t=1 sub-case not yet closed
by Paper E Theorem E: both A⁺ and A⁻ of the form 5S² simultaneously, when 4∤n.

---

## All definitions (self-contained)

**Row-3 pair** (a, n): integers satisfying
- n even, n ≥ 4, 3∤n
- a odd, 1 ≤ a < n, gcd(a, n) = 1

Set:
- A⁺ = a² + n²
- A⁻ = (n − a)² + n²
- b := n − a   (so b odd, 1 ≤ b < n, gcd(b, n) = 1, a + b = n)

**Identity (proved):** A⁺ − A⁻ = n(2a − n) = n(a − b).

**Theorem B (proved, Paper E thm:mod4):**
- 4|n → A⁺ ≡ A⁻ ≡ 1 (mod 8)
- 4∤n → A⁺ ≡ A⁻ ≡ 5 (mod 8)

**Theorem C (proved, Paper E thm:gcd):** gcd(A⁺, A⁻) ∈ {1, 5}.

**Theorem D (proved, Paper E thm:square):** No Row-3 pair has A⁺ = □ and A⁻ = □
simultaneously (2-isogeny descent; rank 0 on E: Y²=X(X+4)(X-1)).

**Theorem E (proved for 4|n, Paper E thm:squarepow):** For 4|n, the t=1 obstruction
is complete: no A⁺ = 5^e · m² is possible for odd e (individual mod-16 obstruction),
and simultaneous squares (e=0) are excluded by Theorem D.

**The remaining open case (this problem):** 4∤n (i.e., n ≡ 2 mod 4) and both
A⁺ = 5S², A⁻ = 5T² for positive integers S, T.

---

## What is already known (do not re-derive)

**1. Mod-8 compatibility (not an obstruction).**
For 4∤n: A⁺ ≡ 5 (mod 8) by Theorem B. And 5S² ≡ 5 (mod 8) iff S is odd.
So the representation A⁺ = 5S² requires S odd — compatible, not a contradiction.

**2. Mod-16 compatibility (not an obstruction).**
n = 4k+2, so n² ≡ 4 (mod 16). A⁺ = a²+n² ≡ a²+4 (mod 16).
Since a is odd, a² ≡ 1 or 9 (mod 16), giving A⁺ ≡ 5 or 13 (mod 16).
For S odd: 5S² ≡ 5 or 13 (mod 16). The sets match — no mod-16 obstruction.

**3. Gaussian integer necessary condition (to verify in Step 1).**
In ℤ[i]: A⁺ = N(a+ni) = 5S² means N(a+ni) = N(2+i) · S².
Since 2+i and 2−i are the two Gaussian primes above 5, exactly one divides a+ni.
Write a+ni = (2+i)·α² or a+ni = (2−i)·α² for some α ∈ ℤ[i].
Similarly a+ni = a+ni and b+ni = (n−a)+ni, with a+b = n.

In case a+ni = (2+i)α² and b+ni = (2+i)β²:
  (a+ni) + (b+ni) = n + 2ni = n(1+2i).
  So (2+i)(α²+β²) = n(1+2i).
  N: 5(N(α)²+N(β)²+...) — this constrains n.
  
In case a+ni = (2+i)α² and b+ni = (2−i)β²:
  Sum: (2+i)α² + (2−i)β² = n(1+2i).
  Let α = p+qi, β = r+si. Then:
    Real: 2(p²−q²) + 2(r²−s²) − (−2pq) − (2rs) ... [expand fully in Step 1].

The key claim (to verify): both cases force 10 | n, i.e., n ≡ 10 (mod 20)
(since n ≡ 2 mod 4 and 5 | n follows from one of the two cases).

**4. Numerical evidence.** Zero simultaneous (5S², 5T²) instances for all Row-3 pairs
with n ≤ 3000 (exact scan: `theorems/M-row3-square-powerful-complete/checker/verify_M.py`).

---

## The theorem / claim to be verified

**Claim:** There is no Row-3 pair (a, n) with 4∤n such that A⁺ = 5S² and A⁻ = 5T²
simultaneously for positive integers S, T.

Equivalently: the system
```
  a² + n² = 5S²
  (n−a)² + n² = 5T²
  n ≡ 2 (mod 4),  3∤n,  a odd,  1 ≤ a < n,  gcd(a,n) = 1
```
has no integer solutions.

---

## Proof skeleton to be closed

### Step 1 — Gaussian factorization and divisibility constraint

Work in ℤ[i] with its unique factorization. Since A⁺ = N(a+ni) = 5S², and
N(2+i) = N(2−i) = 5, exactly one of (2+i), (2−i) divides a+ni in ℤ[i].

**(Case I)** a+ni = (2+i)·(p+qi)² for some p,q ∈ ℤ. Expand:
  a+ni = (2+i)(p²−q²+2pqi) = 2(p²−q²)−2pq·i + i(p²−q²) + 2pq·(−1)...
  = (2p²−2q²−2pq) + (p²−q²+2pq)·i... [compute explicitly].
  
  Similarly (n−a)+ni = (2±i)(r+si)² for the same or conjugate prime.

**(Step 1 goal):** For each of the four cases (Case I/II for A⁺) × (Case I/II for A⁻),
derive the constraint on (a, n) and show that in each case either:
  (a) 5|n is forced (so n ≡ 10 mod 20), or
  (b) a direct contradiction arises (e.g., parity or gcd failure).

**What to close:** Verify the claim "10|n is a necessary condition" from the
Gaussian integer parametrization. If a sub-case yields 5∤n, derive the contradiction.

### Step 2 — Reduction to an elliptic curve

Restricting to n ≡ 10 (mod 20) (the surviving sub-family from Step 1), substitute
A⁺ = 5S², A⁻ = 5T², a + b = n (with b = n−a) into the identity:
  A⁺ + A⁻ = a² + b² + 2n² = 5(S² + T²).

And:
  A⁺ − A⁻ = a² − b² = (a−b)(a+b) = (a−b)n.

Set u = (a−b)/2 (integer, since a−b = 2a−n is even when n is even), so a = n/2+u,
b = n/2−u, and:
  A⁺ = (n/2+u)² + n² = n²/4 + nu + u² + n²,
  A⁻ = (n/2−u)² + n² = n²/4 − nu + u² + n².

So A⁺ + A⁻ = 5n²/2 + 2u² and A⁺ − A⁻ = 2nu. These must equal 5(S²+T²) and 5(S²−T²):
  S²+T² = (5n²/2 + 2u²)/5 = n²/2 + 2u²/5   [requires 5|u² or specific form],
  S²−T² = 2nu/5                              [requires 5|nu].

From 5|nu and gcd(n,5)=1 (if 5∤n) or 5|n: work case by case.

**Substitution goal:** Eliminate one variable to obtain a Weierstrass-form elliptic
curve C(n) in (S, T, u) or a derived pair. For fixed n, determine the Mordell–Weil
group rank of C(n).

### Step 3 — Rank determination

For the elliptic curve(s) C(n) from Step 2:
- Compute the rank over ℚ (2-descent or LMFDB lookup for small n).
- If rank 0 for all n ≡ 10 mod 20: the rational points are torsion. Enumerate all
  torsion points and check whether any give valid Row-3 solutions (a odd, gcd(a,n)=1,
  1 ≤ a < n).
- If rank = 1 for some n: Chabauty–Coleman may apply after supplying the explicit
  Mordell-Weil setup and a suitable prime. Rank >1 is not covered without a separate
  effective height bound.

### Step 4 — Row-3 compatibility check

For any rational point (S, T, u) on C(n) (from torsion or bounded height):
- Check a = n/2 + u is odd and 1 ≤ a < n.
- Check gcd(a, n) = 1.
- Check n ≡ 2 (mod 4), 3∤n.

A point passing all checks would be a counterexample to the claim. If none pass,
this confirms the claim for the family covered by the elliptic argument.

---

## Acceptance criteria

1. **CONFIRMED:** Proof that for all Row-3 pairs with 4∤n, the system A⁺=5S², A⁻=5T²
   has no solution. Must cover the 10∤n and the 10|n sub-cases.

2. **PARTIAL — 10∤n closed:** Proof that 10∤n sub-family is impossible (Gaussian
   factorization forces 5|n), plus INCONCLUSIVE for 10|n sub-family.

3. **PARTIAL — elliptic rank 0 for n ≡ 10 mod 20:** Rank-0 proof plus torsion
   enumeration showing no valid Row-3 point. Does not cover the n ≡ 2 mod 20 sub-case
   if it was not fully disposed of in Step 1.

4. **REFUTED:** An explicit Row-3 pair (a,n) with n > 3000 (numerical lower bound)
   where A⁺=5S², A⁻=5T² with exact arithmetic verification.

5. **INCONCLUSIVE:** Precise statement of what is proved and what remains, identifying
   the residual obstruction (e.g., "the curve has rank 1 for n=X; height bound gives
   no Row-3 solutions up to B, but uniform bound over all n ≡ 10 mod 20 is open").

---

## Key identities (verified algebraically)

- A⁺ + A⁻ = a² + (n−a)² + 2n² = 2a² − 2an + n² + 2n² = 2a²−2an+3n².
  Alternatively: = (a²+n²) + ((n−a)²+n²).
- A⁺ − A⁻ = n(2a−n). [Elementary algebra.]
- gcd(A⁺, A⁻) | gcd(A⁺−A⁻, A⁻) = gcd(n(2a−n), A⁻). Since gcd(n,a)=1 and a is odd,
  gcd(n(2a−n), A⁻) ∈ {1,5} — proved in Theorem C.

---

## Numerical anchor (sanity only, not a proof input)

Row-3 pairs with 4∤n and n ≤ 50, checking if A⁺ or A⁻ is 5×□:
- n=6, a=1: A⁺=37 (prime), A⁻=61 (prime). Neither 5×□.
- n=6, a=5: A⁺=61, A⁻=37. Same.
- n=10, a=1: A⁺=101 (prime), A⁻=181 (prime). Neither 5×□.
- n=10, a=3: A⁺=109 (prime), A⁻=149 (prime). Neither.
- n=10, a=7: A⁺=149, A⁻=109. Same.
- n=10, a=9: A⁺=181, A⁻=101. Same.
- n=14, a=1: A⁺=197 (prime). Not 5×□.
- n=50, a=9: A⁺=2581 (prime). Not 5×□.

Zero instances of simultaneous A⁺=5S², A⁻=5T² in the full scan n≤3000.

---

## Dead ends (do not re-attempt)

**DE-1 (mod-8/16 local obstruction):** As shown above, 5S²≡5 (mod 8) is consistent
with A⁺≡5 (mod 8) when S is odd. The mod-16 values also match. No local obstruction
at 2 exists for this case.

**DE-2 (mod-5 local obstruction):** If 5∤n, then gcd(A⁺,5)=1 so A⁺=5S² requires
5|A⁺=a²+n², i.e., a²≡−n² (mod 5), i.e., (a/n)²≡−1 (mod 5). But −1 is not a QR
mod 5 (since 5≡1 mod 4... wait: −1 is a QR mod p iff p≡1 mod 4; 5≡1 mod 4 so −1≡4
is a QR mod 5 since 2²=4). So (a/n)≡±2 (mod 5) is possible. Not a contradiction.

**DE-3 (ABC trivial bound):** See OE-01 Dead End DE-1 for the calculation showing the
ABC approach gives a trivially satisfied bound n²≪n^{3+ε}.
