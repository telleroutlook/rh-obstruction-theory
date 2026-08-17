# Problem OE-03 — NT-A: Uniform Effective S-unit Theorem over ℤ[i] with Growing S

**Type:** Analytic / algebraic number theory (S-unit equations, Baker theory, effective heights)

**Non-circularity:** All hypotheses are elementary arithmetic over ℤ and ℤ[i]. No zeros of ζ, no RH, no Li coefficients, no ordinate values. RH stays `[OUT]`.

**Relation to Paper E.** This is blocking theorem NT-A (Paper E, thm:NTA). A proof of the claimed uniform effective bound would allow the S-unit approach to close the core conjecture (Conjecture 1 of Paper E: no Row-3 pair has both A⁺ and A⁻ powerful away from 5) unconditionally, subject to a finite-height search.

---

## All definitions (self-contained)

**Row-3 pair** (a, n): integers satisfying
- n even, n ≥ 4, 3∤n
- a odd, 1 ≤ a < n, gcd(a, n) = 1

Set:
- A⁺ = a² + n²,   A⁻ = (n−a)² + n²
- b := n−a,   so a+b = n
- w⁺ := a+ni ∈ ℤ[i],   w⁻ := b+ni = (n−a)+ni ∈ ℤ[i]
- N(w⁺) = A⁺,   N(w⁻) = A⁻

**Identity:** w⁺ − w⁻ = a−b = 2a−n.  [Note: also w⁺ + w⁻ = n(1+2i).]

**Powerful-away-from-5:** A positive integer N is powerful-away-from-5 if every prime
p ≠ 5 dividing N satisfies p² | N.

**Theorem C (proved):** gcd(A⁺, A⁻) ∈ {1, 5}.

**The Gaussian powerful parametrization.**
If A⁺ is powerful away from 5, then in ℤ[i]:
```
  w⁺ = a+ni = ε · (1+2i)^{f₁} · (1−2i)^{g₁} · ξ₊²
```
where:
- ε ∈ {1, i, −1, −i} is a unit in ℤ[i]
- f₁, g₁ ∈ {0, 1} encode the 5-adic type of A⁺   (since N(1+2i)=N(1−2i)=5)
- ξ₊ ∈ ℤ[i] is the "square root part"

(The Gaussian version of the standard powerful parametrization: if every rational prime
p≠5 divides A⁺ to even power, then the Gaussian factorization of w⁺ has each Gaussian
prime above p dividing w⁺ to even power, giving w⁺ = (5-part) · (perfect square in ℤ[i]).)

**The S-unit equation.**
With the parametrization of w⁺ and w⁻ above, the difference:
```
  w⁺ − w⁻ = n−2b = 2a−n   (a rational integer)
```
becomes:
```
  ε₁ · U₁ · ξ₊² − ε₂ · U₂ · ξ₋² = c,
```
where:
- U₁ = (1+2i)^{f₁}(1−2i)^{g₁}, U₂ = (1+2i)^{f₂}(1−2i)^{g₂}  (fixed from the 5-type)
- c = 2a−n  (satisfies |c| < n, c ≡ 0 mod 2 since a,n same parity iff both even — but
  a is odd and n is even, so c = 2a−n is odd)
- ξ₊, ξ₋ ∈ ℤ[i] are S-units for the set
```
  S = S₀ ∪ S(n),   S₀ = {primes of ℤ[i] above 5},
```
  where S(n) = {Gaussian primes 𝔭 : N(𝔭) | n} (primes of ℤ[i] dividing n).

**Key growth:** |S(n)| = Σ_{p|n, p≡1 mod 4} 2 + Σ_{p|n, p=2} 1 + Σ_{p|n, p≡3 mod 4} 0
= O(ω(n)), and for n ranging over Row-3 pairs with many prime factors, |S(n)| → ∞.

**The Evertse–Schmidt theorem (Gaussian analogue):** For FIXED S ⊂ ℤ[i], the S-unit
equation X − Y = 1 in S-units X, Y ∈ ℤ[i]* has at most C(|S|) solutions, where C
depends only on |S| (not on the specific primes in S). But C(|S|) provides NO explicit
height bound, and the bound degrades as |S| grows.

---

## The theorem / claim to be verified

**NT-A (what is needed).** An explicit function H: ℤ_{>0} × ℤ_{>0} → ℝ_{>0} such that:

For every Row-3 pair (a,n) and every 5-adic type (f₁,g₁,f₂,g₂) ∈ {0,1}⁴,
if ξ₊, ξ₋ ∈ ℤ[i] satisfy
```
  ε₁ U₁ ξ₊² − ε₂ U₂ ξ₋² = 2a − n,    |ξ₊|, |ξ₋| ≥ 1
```
with ξ₊, ξ₋ being S(n)-units (all their Gaussian prime divisors lie in S(n) ∪ S₀),
then:
```
  max(|ξ₊|, |ξ₋|) ≤ H(n, |S(n)|).
```

A useful form: H(n, s) = exp(C · n^α · s^β) for explicit constants C, α, β
(any β < ∞ would be a new result; polynomial in n · s would be optimal).

**Consequence.** If H(n, |S(n)|) = poly(n), then for n large, the only Row-3 S-unit
solutions have |ξ₊| ≪ poly(n), bounding A⁺ = N(w⁺) = N(U₁)·N(ξ₊)² ≤ 5·H(n,|S(n)|)².
Since A⁺ = a²+n² ≍ n², this gives n² ≪ poly(n)², holding for all large n only if
the polynomial degree ≥ 1 — compatible. So the bound must be COMBINED with the constraint
A⁺ = a²+n² exactly to give: A⁺ ≤ 5H² means a²+n² ≤ 5H², which for H = poly(n) gives
a bound on a, which can then be verified by finite search.

---

## Proof skeleton to be closed

### Step 1 — State the precise S-unit equation over ℤ[i]

Starting from the Gaussian powerful parametrization, derive all 2⁴ = 16 cases
(f₁, g₁, f₂, g₂) ∈ {0,1}⁴. Reduce by symmetry (complex conjugation and swapping
w⁺ ↔ w⁻) to the distinct cases. For each surviving case, write the S-unit equation
```
  X − Y = c,   X = ε₁ U₁ ξ₊²,   Y = ε₂ U₂ ξ₋²
```
in normal form, identifying the allowed set S.

**What to close:** Enumerate the distinct S-unit equations (up to symmetry). Confirm
that each has the same structure (a quadratic Thue–Mahler equation in the Gaussian
integer ξ₊ over the ring ℤ[i]).

### Step 2 — Review of effective S-unit bounds with growing S

Survey the state of the art for effective bounds on S-unit equations over number fields
when S is allowed to grow:

(a) **Baker–Wüstholz logarithmic forms:** For the equation X−Y=1 over ℚ, Baker gives
  |X| ≤ exp(C · p_1^{a_1} · ... · p_k^{a_k} · (log X)^ε) — but this involves log X
  on both sides, giving only an implicit bound unless |S| is fixed.

(b) **Evertse–Schlickewei–Schmidt (2002):** Gives at most C(s, d) solutions for
  equations over a number field of degree d with S of size s, but C(s,d) is explicit
  only as a function of s and d — not a height bound.

(c) **Bombieri–van der Poorten–Vaaler (1996):** Effective heights for unit equations
  in algebraic number fields, but requires S fixed.

(d) **Recent work (Győry–Yu, Murty–Samir, etc.):** Check literature post-2000 for
  uniform S-unit bounds where |S| grows. Identify the current gap.

**What to close:** Either cite an existing result that gives H(n, |S(n)|) as above,
or identify precisely why current technology does not provide such a bound.

### Step 3 — Conditional result under ABC over ℤ[i]

Assume: for any a, b, c ∈ ℤ[i] with a+b+c = 0 and gcd(a,b,c) = 1,
```
  max(|N(a)|, |N(b)|, |N(c)|) ≤ C(ε) · N(rad(abc))^{1+ε}
```
where rad(x) = product of distinct Gaussian prime divisors of x.

Apply to X − Y = c with X = ε₁ U₁ ξ₊², Y = ε₂ U₂ ξ₋²:
- N(X) = 5^{f₁+g₁} · N(ξ₊)² = 5^{e₁} · N(ξ₊)²
- N(Y) = 5^{f₂+g₂} · N(ξ₋)²
- rad(XY) = 5 · rad(N(ξ₊)) · rad(N(ξ₋)) ≤ 5 · N(ξ₊) · N(ξ₋)   (since ξ₊, ξ₋ are S-units)
- rad(c) = rad(2a−n) ≤ |2a−n| < n

ABC gives: N(X) ≤ C(ε) · (5 · N(ξ₊) · N(ξ₋) · n)^{1+ε}.
Since N(X) = 5^{e₁} N(ξ₊)², this gives N(ξ₊)² ≤ C(ε) · (5 N(ξ₊) N(ξ₋) n)^{1+ε},
hence N(ξ₊)^{1−ε} ≤ C(ε) · (N(ξ₋) · n)^{1+ε}.

**What to close for Step 3:** Use also the symmetric bound on N(ξ₋)^{1−ε} and
multiply or combine to get max(N(ξ₊), N(ξ₋)) ≤ H(n) for some explicit H(n) = poly(n)
(under ABC). Derive what this implies for the Row-3 powerful problem.

### Step 4 — From height bound to finite search

Assuming H(n, |S(n)|) is proved (unconditionally or conditionally):
- The constraint A⁺ = a²+n² = 5^{e₁} · N(ξ₊)² ≤ 5 · H² gives a ≤ √(5H² − n²).
- For H = poly(n), this bounds a polynomially in n.
- A finite-height search over all a ≤ √(5H²−n²) and all Row-3 conditions verifies
  that no simultaneous powerful pair exists above the bound.

---

## Acceptance criteria

1. **CONFIRMED — unconditional:** An explicit H(n, |S(n)|) such that the S-unit bound
   holds unconditionally for all Row-3 S-unit equations. With a derived finite-height
   consequence for the Row-3 powerful problem.

2. **CONFIRMED — conditional:** Same, under ABC over ℤ[i] (or over ℚ applied to
   the norms). The conditional hypothesis must be clearly stated with its standard
   reference.

3. **PARTIAL — reduction complete:** Step 1 completed with all S-unit equations in
   normal form; Step 2 identifies the precise current gap in the literature; Step 3
   derives the conditional bound even if Step 4 is incomplete.

4. **INCONCLUSIVE — gap identified:** A precise statement of the form "the S-unit
   bound H(n, |S(n)|) would follow from [Conjecture X], but [Conjecture X] is currently
   open because [reason]; the nearest available unconditional result gives only [weaker
   statement]." This is a valid and useful outcome.

---

## Key identities (verified algebraically)

- w⁺ − w⁻ = (a+ni) − (b+ni) = a−b = 2a−n. [Elementary.]
- N(1+2i) = 1+4 = 5. N(1−2i) = 5. (1+2i)(1−2i) = 5. [Standard Gaussian arithmetic.]
- If w⁺ = U·ξ₊² with U ∈ {1, 1+2i, 1−2i, 5} (5-adic types), then
  N(w⁺) = N(U)·N(ξ₊)² ∈ {N(ξ₊)², 5N(ξ₊)², 5N(ξ₊)², 25N(ξ₊)²}. [Multiplicativity of N.]
- gcd(A⁺, A⁻) | gcd(w⁺, w⁻) in ℤ[i], and the latter is in {1, 1+2i, 1−2i, 2+i, 2−i}
  (divisors of 5n in ℤ[i]). Theorem C pins gcd to {1,5} over ℤ.

---

## Numerical anchor (sanity only, not a proof input)

Row-3 S-unit equation instances for small n:
- n=6, (f₁,g₁,f₂,g₂)=(0,0,0,0): would require ξ₊²−ξ₋²=2a−6 with ξ₊,ξ₋∈{S(6)-units}.
  S(6) = {primes of ℤ[i] above 2, 3}. Since 2 = −i(1+i)², 3 is inert, S(6)∩{split} = ∅.
  So ξ₊,ξ₋ ∈ {units} = {1,i,−1,−i}, giving |ξ₊|=|ξ₋|=1, hence A⁺=N(U₁)·1 ∈ {1,5}.
  But A⁺=a²+36≥37. Contradiction — no S-unit solution for n=6 in this 5-type.
  (This confirms the numerical scan result for n=6.)

---

## Dead ends (do not re-attempt)

**DE-1 (Evertse–Schmidt for fixed S):** For each fixed n, applying Evertse–Schmidt
gives finitely many solutions to the S(n)-unit equation — but the bound C(|S(n)|, 2)
depends on n through |S(n)| and is not uniform. This approach does not close NT-A.

**DE-2 (ABC trivial bound):** As shown in Step 3, the naive ABC application gives
N(ξ₊)² ≤ C(ε)(N(ξ₊)N(ξ₋)n)^{1+ε}, which without a second inequality does not
close (both N(ξ₊) and N(ξ₋) are unknowns). See the calculation in Steps 3–4 for
the correct way to combine both bounds.

**DE-3 (Faltings on a higher genus curve):** The S-unit equation ε₁U₁ξ₊² − ε₂U₂ξ₋² = c
in (ξ₊, ξ₋) ∈ (ℤ[i])² defines a genus-1 curve (intersection of quadrics), not a
higher genus curve. Faltings does not apply (genus ≥ 2 required).
