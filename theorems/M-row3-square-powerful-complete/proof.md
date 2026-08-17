# Proof of Theorem M

## Setup and notation

Row-3 pair (a, n): n = 2m, a odd, gcd(a,n) = 1, n ≥ 4, 3∤n.
A⁺ = a² + n², A⁻ = (n−a)² + n².

By Theorem B (Paper E, label thm:mod4):
- 4∤n → A⁺ ≡ A⁻ ≡ **5** (mod 8)
- 4|n → A⁺ ≡ A⁻ ≡ **1** (mod 8)

Squares mod 8: {0, 1, 4}.
5m² mod 8: m odd → 5; m ≡ 2 mod 4 → 4; m ≡ 0 mod 4 → 0. So {0, 4, 5}.

---

## Proof of (i): Sub-family 4|n

Write n = 4k. Claim: A⁺ ≠ 5^e · M² for any e ≥ 1 (odd e), and the simultaneous
e=0 (perfect square) case is excluded by Theorem L.

**Step 1 (mod 8, odd e).**
If e is odd: 5^e · M² = 5 · (5^{(e−1)/2} M)² = 5T².
5T² mod 8: T odd → 5·1 = 5; T even → 0 or 4. So 5T² ∈ {0, 4, 5} mod 8.
But A⁺ ≡ 1 (mod 8) when 4|n. Since 1 ∉ {0, 4, 5}, this is a contradiction.
Therefore A⁺ ≠ 5^e · M² for any odd e ≥ 1. □ (individual impossibility for odd e)

Remark: The mod-16 argument refines this — for n = 4k: A⁺ = a² + 16k² ≡ a² (mod 16),
and a odd gives a² ≡ 1 or 9 (mod 16); while 5T² ≡ 5 or 13 (mod 16) for T odd,
and 5T² ≡ 0 or 4 (mod 16) for T even. Neither {5,13} nor {0,4} meets {1,9},
confirming the obstruction at a finer scale.

**Step 2 (even e = perfect square).**
If e is even: 5^e · M² = (5^{e/2} M)² = □. For the SIMULTANEOUS case (both A⁺ = □
and A⁻ = □), Theorem L (Paper E, label thm:square) provides a rank-0 elliptic
obstruction. The case of A⁺ = □ while A⁻ ≠ □ is not further constrained by this
theorem (it is not a claim).

Combining Steps 1–2: for 4|n, no simultaneous (5^{e₁}·M², 5^{e₂}·M'²) pair survives
where (e₁,e₂) has at least one odd entry (individual mod-8 kills it), or where both
are even (Theorem L kills it). This proves the 4|n case completely. □

---

## Proof of (ii): Sub-family 4∤n (partial)

Write n ≡ 2 (mod 4). Here A⁺ ≡ **5** (mod 8).

**Even-e case: individual mod-8 obstruction.**
If e is even: 5^e · M² = (5^{e/2} M)² = □.
Squares mod 8 ∈ {0, 1, 4}. But A⁺ ≡ 5 (mod 8). Contradiction.
Therefore A⁺ ≠ 5^e · M² for any even e ≥ 0. This rules out A⁺ = □ individually.

**Mixed case: (e₁ even, e₂ odd) or (e₁ odd, e₂ even).**
If A⁺ = □ (e₁ even): impossible individually as above. Same for A⁻ = □.

**Simultaneous odd-e case: (5□, 5□) — OPEN.**
If A⁺ = 5S² and A⁻ = 5T² (both e₁, e₂ odd): both are ≡ 5 (mod 8) (for S, T odd),
which is consistent with A⁺ ≡ A⁻ ≡ 5 (mod 8). The mod-8/16 obstructions do NOT
exclude this case.

Numerical evidence: no Row-3 pair with n ≤ 3000 satisfies this (sweep in checker).
A proof is currently outstanding; see OE-01 for the outsource formulation.

---

## Case summary

| Case | Sub-family | Obstruction | Status |
|---|---|---|---|
| A⁺=□, A⁻=□ (e₁=e₂=0) | 4|n | Theorem L (elliptic, rank 0) | PROVED |
| A⁺=5^odd·□, A⁻=anything | 4|n | 5T²≡{0,4,5}≠1 mod 8 | PROVED (individual) |
| anything, A⁻=5^odd·□ | 4|n | symmetric | PROVED (individual) |
| A⁺=□ (e even) individually | 4∤n | □≡{0,1,4}≠5 mod 8 | PROVED |
| A⁻=□ (e even) individually | 4∤n | symmetric | PROVED |
| A⁺=5□, A⁻=5□ | 4∤n | compatible with mod 8/16 | **OPEN** |

---

## Dependencies

- Theorem B (Paper E, thm:mod4, proved): 4∤n→ mod 8 ≡5; 4|n→ mod 8 ≡1.
- Theorem L (this repo, thm:square): no simultaneous perfect squares (4|n case only).
- Elementary number theory: squares mod 8 and mod 16.
