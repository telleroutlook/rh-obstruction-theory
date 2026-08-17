# OE-03 Review Record — NT-A Attempts

## Attempt 1 (2026-08-17): REFUTED

**Claimed:** H(n, |S(n)|) = O(1) unconditionally because gcd(a,n)=1 collapses
S(n)-unit support to S₀.

**Refuted:** ξ₊ is supported on prime factors of A⁺ = a²+n², not on factors of n.
gcd(a²+n², n) = 1 (by gcd(a,n)=1), so A⁺'s prime factors NEVER divide n.
The support of ξ₊ is entirely outside S(n) = {primes of n}, making the proposed
"collapse" vacuous — ξ₊ is NOT an S₀∪S(n)-unit at all.

Concrete counterexamples (verified computationally):
- n=4, a=1: A⁺=17 prime, 17∉S₀∪S(4)
- n=10, a=1: A⁺=101 prime, 101∉S₀∪S(10)
- n=32, a=1: A⁺=5²·41, prime 41∉S₀∪S(32)

The actual support of ξ₊ consists of all prime factors of A⁺=a²+n² (excluding
the 5-adic part), and this set grows with (a,n) in an uncontrolled way.

---

## Re-evaluation: Why all three pivots face the same barrier

**Pivot 1 (abc on higher-degree identity):** Dead end (proved in Paper E §Dead ends).
Any identity involving A⁺, A⁻, n(2a-n) has rad ≤ C·n⁴ while A⁺ ≍ n²,
giving n² ≪ n^{4+ε} — trivially satisfied, no contradiction.

**Pivot 2 (Baker linear forms directly):** Fails because |X/Y - 1| ≍ 1/n is
POLYNOMIALLY small, not exponentially small. Baker's theorem requires the linear
form to be exponentially small in the height to derive a contradiction; 1/n does
not meet that threshold. The lower bound exp(-C·log n·log log n) is not less than 1/n.

**Pivot 3 (Pell/Thue-Mahler):** The factorization (ξ₊-ξ₋)(ξ₊+ξ₋) = 2a-n is a
Thue-Mahler equation for FIXED c = 2a-n, giving effective bounds by Evertse-Schlickewei.
But c varies with (a,n), and a uniform bound over all c requires |S| control —
returning to the original obstruction.

---

## Current status: OPEN

The core NT-A obstruction stands: effective S-unit bounds for X-Y=c over ℤ[i] require
|S| fixed, but the support of ξ₊ and ξ₋ depends on A⁺ and A⁻ and grows arbitrarily.

A genuine breakthrough would need one of:
- A uniform Thue-Mahler bound for families of equations (unknown)
- An ABC-type result over ℤ[i] with exponent < 3 (unknown, stronger than abc)
- An approach that avoids S-unit equations entirely (e.g., geometry-of-numbers
  for Gaussian integers, or an arithmetic geometry argument)
