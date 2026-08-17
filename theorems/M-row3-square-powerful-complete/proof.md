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

## Proof of (ii): Sub-family 4∤n

Write n ≡ 2 (mod 4). Here A⁺ ≡ **5** (mod 8).

**Even-e case: individual mod-8 obstruction.**
If e is even: 5^e · M² = (5^{e/2} M)² = □.
Squares mod 8 ∈ {0, 1, 4}. But A⁺ ≡ 5 (mod 8). Contradiction.
Therefore A⁺ ≠ 5^e · M² for any even e ≥ 0. This rules out A⁺ = □ individually.

**Mixed case: (e₁ even, e₂ odd) or (e₁ odd, e₂ even).**
If A⁺ = □ (e₁ even): impossible individually as above. Same for A⁻ = □.

**Simultaneous odd-e case: (5□,5□), direct reduction.**
Suppose `A⁺=5S²` and `A⁻=5T²`. Put `b=n-a`, `x=b/n`, `r=T/n`, and `s=S/n`.
Dividing by `n²` gives the two rational 5-conics

```
x²+1 = 5r²,          x²-2x+2 = 5s².
```

The first conic has the rational point `(x,r)=(2,1)`. Parametrizing the line of
slope `t` through it gives

```
x = 2(5t²-5t+1)/(5t²-1),
r = -(5t²-4t+1)/(5t²-1).
```

Substituting this in the second conic and writing `Y=(5t²-1)s` yields

```
Y² = 10t⁴-20t³+24t²-12t+2.       (C)
```

Now put `u=t-1` and `v=Y`. The shifted quartic is

```
v² = 10u⁴+20u³+24u²+16u+4.
```

For `u≠0`, define

```
A = v+2+4u+2u²,
B = v(1+u)+2+6u+6u²,
X = 4A/u²,
Y_E = 16B/u³+40.
```

Then

```
Y_E²-(X³-32X+64)
  = 64A(10u⁴+20u³+24u²+16u+4-v²)/u⁶,
```

so `(X,Y_E)` lies on `E: Y_E²=X³-32X+64`. Away from the exceptional torsion
points, the inverse is

```
u = -4X/(4X-Y_E+8),
v = 2(2X³-Y_E²+16Y_E-64)/(4X-Y_E+8)²,
t = 1+u.
```

After clearing denominators, the quartic error is
`16X³(Y_E²-X³+32X-64)/(4X-Y_E+8)^4`, hence vanishes on `E`. Thus the map is
birational.

The independent PARI/GP replay gives `rank E(Q)=0`; its torsion subgroup is
`Z/4Z={O,(4,0),(0,8),(0,-8)}`. Their pullbacks are respectively

```
(t,Y) = (1,2), (1/3,2/9), (1,-2), (1/3,-2/9).
```

Each gives `x=1/2`, hence `a=n-b=n/2`. Since `gcd(a,n)=1`, this forces `n=2`,
contradicting `n≥4`. Therefore no Row-3 solution survives.

This completes the odd-e case. The rank-zero and torsion computations on
`E`, its translated 2-torsion model, and its 2-isogenous model are independently
replayed by PARI/GP (`checker/verify_OE02_pari_replay.py`). The theorem remains
mathematically `PROOF-DRAFT`: the corrected 5-conic reduction and explicit
birational map still require independent human review.

---

## Case summary

| Case | Sub-family | Obstruction | Status |
|---|---|---|---|
| A⁺=□, A⁻=□ (e₁,e₂ even) | 4|n | Theorem L (elliptic, rank 0) | PROOF-DRAFT |
| A⁺=5^odd·□, A⁻=anything | 4|n | 5T²≡{0,4,5}≠1 mod 8 | PROOF-DRAFT |
| anything, A⁻=5^odd·□ | 4|n | symmetric | PROOF-DRAFT |
| A⁺=□ (e even) individually | 4∤n | □≡{0,1,4}≠5 mod 8 | PROOF-DRAFT |
| A⁻=□ (e even) individually | 4∤n | symmetric | PROOF-DRAFT |
| A⁺=5□, A⁻=5□ | 4∤n | direct 5-conic reduction + rank-zero quartic | PROOF-DRAFT (CAS rank replay closed; human map audit open) |

---

## Dependencies

- Theorem B (Paper E, thm:mod4, proved): 4∤n→ mod 8 ≡5; 4|n→ mod 8 ≡1.
- Theorem L (this repo, thm:square): no simultaneous perfect squares.
- Elementary number theory: squares mod 8 and mod 16.
- Direct OE-02 5-conic reduction; exact map checker
  `checker/verify_OE02_quartic_map.py`; the independent PARI/GP replay is
  `checker/verify_OE02_pari_replay.py`.
