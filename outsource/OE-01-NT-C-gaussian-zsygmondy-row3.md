# Problem OE-01 — NT-C: Gaussian Zsygmondy for the Row-3 Family

**Status update (2026-08-17):** the square/t=1 subcase is now covered by Theorems L
and M (repository status `PROOF-DRAFT`). The remaining active target is the cube-factor
case, reformulated more precisely as OE-05. The support correction below is part of the
post-review audit.

**Type:** Pure arithmetic / Diophantine geometry  
**Non-circularity:** All hypotheses are elementary: even integers, odd integers, gcd,
norms in ℤ[i]. No zeros of ζ, no RH, no Li coefficients, no ordinate values.
RH stays `[OUT]`.

---

## All definitions (self-contained)

**Row-3 pair** (a, n): integers satisfying
- n even, n ≥ 4, 3 ∤ n
- a odd, 1 ≤ a < n, gcd(a, n) = 1

Write n = 2m. Set:
- A⁺ = a² + n²
- A⁻ = (a − n)² + n²   [equivalently (n − a)² + n²]

**Identity (proved):** A⁺ − A⁻ = n(2a − n).

**Theorem C of Paper E (proved):** gcd(A⁺, A⁻) ∈ {1, 5}.

**Powerful-away-from-5:** A positive integer N is _powerful-away-from-5_ if every
prime p ≠ 5 dividing N satisfies p² | N. (Equivalently, every p ≠ 5 with v_p(N) = 1
is absent; primes p ≡ 3 mod 4 always satisfy this automatically since they appear to
even power in any Gaussian norm N(α).)

**NT-C (the claim):** There exists an absolute constant C such that for every
Row-3 pair (a, n) with n > C, at least one of A⁺, A⁻ is NOT powerful-away-from-5.

**Equivalent Gaussian formulation:** In ℤ[i], at least one of w⁺ = a + ni or
w⁻ = (a − n) + ni has a Gaussian prime 𝔭 with N(𝔭) coprime to 5n appearing to
exactly first power.

---

## The theorem / claim to be verified

**NT-C (stated above).** A proof of any of the following suffices:

(i) **(Square subcase)** There are only finitely many Row-3 pairs (a, n) such that
both A⁺ and A⁻ are perfect squares (equivalently, perfect squares times powers of 5).

(ii) **(Powerful subcase)** There are only finitely many Row-3 pairs (a, n) such that
both A⁺ and A⁻ are powerful-away-from-5.

The square subcase (i) implies NT-C only for pairs where the cube factor in the
Erdős–Szekeres representation A± = s²t³ is trivial (t=1). The full claim (ii) is NT-C.

---

## Proof skeleton to be closed

### Step 0 — Preliminary reductions

**0a.** Primes p ≡ 3 mod 4, p ∤ n: these are inert in ℤ[i], and v_p(N(a+ni)) is
always even (= 2·v_p(a+ni)), so they never contribute a first-power divisor. Only
split primes p ≡ 1 mod 4 with p ∤ 5n are relevant.

**0b.** p = 2: A⁺ = a²+n² ≡ 1 mod 4 (a odd, n even), so 2 ∤ A⁺. Same for A⁻.

**Conclusion of Step 0:** "Both A⁺ and A⁻ powerful-away-from-5" is the same as:
for every split prime p ≡ 1 mod 4, p ∤ 5n, dividing A⁺ (or A⁻), v_p(A⁺) ≥ 2.

---

### Step 1 — Pythagorean parametrization (square subcase)

Suppose A⁺ = a²+4m² = x² and A⁻ = (2m−a)²+4m² = y² for some positive integers
x, y (the square subcase with 5-factor absorbed for simplicity).

From x² − a² = 4m²: since a is odd and x is odd, write x − a = 2s₁, x + a = 2t₁,
so s₁t₁ = m² and t₁ > s₁ > 0, t₁ − s₁ = a.

From y² − (2m−a)² = 4m²: similarly write y − (2m−a) = 2s₂, y + (2m−a) = 2t₂,
so s₂t₂ = m² and t₂ > s₂ > 0, t₂ − s₂ = 2m − a.

**Constraint:** (t₁ − s₁) + (t₂ − s₂) = a + (2m−a) = 2m. ✓ (Automatic.)

The nontrivial constraint: s₁, s₂ are divisors of m² (since s₁t₁ = s₂t₂ = m²), and:

```
Let S = s₁ + s₂,  P = s₁s₂.
Then: S(m² − P)/P = 2m  ⟹  P = Sm²/(S + 2m).
```

For s₁, s₂ to be positive integers: P = Sm²/(S+2m) must be a positive integer AND
the discriminant S² − 4P = S(S² + 2mS − 4m²)/(S+2m) must be a perfect square.

**What to close for Step 1:** Show that for all Row-3 pairs (m with 3 ∤ m) and all
S = s₁+s₂ with s₁,s₂ | m² and s₁,s₂ < m, either P = Sm²/(S+2m) is not a
positive integer, OR S²−4P is not a perfect square.

Partial result (see Step 2): the discriminant condition reduces to an elliptic curve.

---

### Step 2 — Elliptic curve obstruction (square subcase)

Suppose Step 1 has a solution: P integer and Δ = S²−4P = □. Substituting P:

```
Δ = S²−4P = (S−2m)(u−v)² / (4(S+2m))
```

where (u, v) with u+v = S and uv = 5m² are the factorization of 5m² giving
S = u+v. (For the 5∤m case this is a factorization of 5m² from the constraint
that u+v+2m | 4m³ — see derivation below.)

Equivalently, Δ = □ iff (S−2m)/(S+2m) = (r/t)² for some rational r/t, which
gives S = 2m(4r²+t²)/(t²−4r²) and requires t² > 4r² (t > 2r).

Substituting into uv = 5m² and u+v = S yields the quartic:

```
(u−v)² = S² − 4·5m² = S² − 20m².
```

Setting u = (S+d)/2, v = (S−d)/2 (d = u−v), d² = S²−20m², and with S as
above, this leads to the genus-1 curve:

```
C : y² = x⁴ − 3x²b² + b⁴    (in affine coordinates x = a/b, y = d/(2m))
```

which factors as y² = (x²−xb−b²)(x²+xb−b²) over ℤ.

**What to close for Step 2:** Determine all integer points on C with the Row-3
constraints (3 ∤ m, a odd, gcd(a, 2m) = 1). Specifically:

- Compute the rank of C over ℚ. Rank 0 permits direct torsion enumeration; rank 1
  requires a fully set-up Chabauty argument; rank >1 is not closed by this protocol.
- Identify all rational points and check that none satisfy the Row-3 constraints for
  n > C.

*Difficulty class:* Descent on an elliptic curve. Standard tools (2-descent, LMFDB,
Magma/SageMath) apply.

---

### Step 3 — Extension to the general powerful case

When A⁺ = 5^{e₁}·s₁²·t₁³ (Erdős–Szekeres, with cube factor t₁ ≥ 2), the Gaussian
factorization gives w⁺ = unit · (5-part) · U·α², where U is a Gaussian integer supported
on Gaussian primes above the split primes in t₁ (together with the odd 5-part, if any).
Because gcd(a,n)=1 implies gcd(A⁺,n)=1, those non-5 primes are **outside** the prime
divisors of n. Thus the support of U is not bounded by S(n).

The difference w⁺ − w⁻ = 2a−n remains. With both w⁺ and w⁻ powerful away from 5,
this yields a varying Gaussian S-unit equation:

```
U₁α² − U₂β² = n,
```

where U₁, U₂ (and also the square parts α, β) contribute prime support outside 5n.
The allowed prime set S is not determined by the factor set of n; in particular it is
not correct to write |S|=O(ω(n)). The actual support grows through the cube-factor
primes of A⁺ and A⁻, blocking direct Evertse–Schmidt.

**Obstacle (cube factor / growing S):** No current theorem gives effective uniform
bounds on the S-unit equation X − Y = n when |S| → ∞ with n. The cube-factor case
remains open beyond the elliptic-curve approach.

**Partial result sufficing for Paper E:** Proving the square subcase (i) would already
be a new Zsygmondy-type result; even the rank-0 proof for C suffices to establish
NT-C for the square subcase and motivate NT-C as a theorem.

---

## Acceptance criteria

1. **CONFIRMED — full NT-C:** Proof that for n > C (explicit C), no Row-3 pair has
   both A⁺ and A⁻ powerful-away-from-5. Covers cube factors.

2. **CONFIRMED — square subcase:** Proof that the elliptic curve C has rank 0 over ℚ
   (or finitely many integer points), plus verification that no Row-3 point on C
   gives a simultaneous solution for n > C. Does not cover cube factors but is
   a genuine Zsygmondy-type result.

3. **PARTIAL — descent setup:** A complete 2-descent on C determining the rank,
   even if the infinite-descent argument to exclude integer points is incomplete.
   Partial evidence accepted if it identifies the Mordell–Weil group and leaves only
   finite descent to close.

4. **REFUTED:** An explicit Row-3 pair (a, n) with n > C₀ = 1000 (numerical lower
   bound) where both A⁺ and A⁻ are powerful-away-from-5. Must survive the checker:
   independently verified with exact arithmetic.

5. **INCONCLUSIVE:** A precise statement of what is and is not proved, together with
   the strongest partial localization reachable (e.g., upper bound on the rank, or
   a proof that the cube factor cannot arise when a²+n² < B for explicit B).

---

## Key identities (all verified by script, not from memory)

**Identity 1:** A⁺ − A⁻ = n(2a − n). [Algebraic identity, no condition on a, n.]

**Identity 2 (Pythagorean):** For s₁t₁ = m² (positive integers), (t₁−s₁)²+4m² = (t₁+s₁)².
Proof: expand (t₁+s₁)² = t₁²+2t₁s₁+s₁² = (t₁−s₁)²+4t₁s₁ = (t₁−s₁)²+4m².

**Identity 3 (discriminant):** With S = s₁+s₂, P = Sm²/(S+2m), and d = |s₁−s₂|:
S² − 4P = d²·(S−2m)/(S+2m). [Verified: substitute P and simplify.]

---

## Numerical anchor (sanity only, not a proof input)

Script `checker/OE01_anchor.py` (to be created) verifies:

- For all Row-3 pairs (a, n) with 4 ≤ n ≤ 2000, n even, 3 ∤ n, a odd, gcd(a,n)=1:
  zero pairs have both A⁺ and A⁻ powerful-away-from-5.
- For perfect-square subcase: zero simultaneous solutions up to n=1000.
- For the elliptic curve C: values b=1, a=2,...,100: (a⁴−3a²+1) is a perfect square
  only for a=1 (giving 1⁴−3+1=−1 < 0, excluded) and a=0 (trivial). No solutions.

---

## Dead ends (do not re-attempt)

**DE-1 (ABC over ℚ):** Writing A⁺ + (−A⁻) = n(2a−n) and applying ABC gives
max(A±) ≪ rad(A⁺·A⁻·n(2a−n))^{1+ε}. Since rad(A±) ≤ 5·√A± (powerful), this yields
max(A±) ≪ n^{3+ε}, trivially satisfied. No contradiction. (Same as Dead End D2 in OB-47.)

**DE-2 (Evertse S-units with fixed S):** For fixed n, Evertse gives finitely many
solutions to U₁α²−U₂β²=n. But S = {primes above 5n} grows with n, so no uniform
bound is available from this direction.

**DE-3 (density/sieve):** Powerful numbers in [n², 2n²] number ~Cn. Row-3 pairs
number ~φ(n)/4. Since φ(n) can be as large as n−1, density alone does not give 0.
