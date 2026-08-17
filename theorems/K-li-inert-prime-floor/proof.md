# Proof — Theorem K

**Status:** PROOF-DRAFT.

## §1. On-line observations are p-integral

Fix a primitive rational node `t=a/b` and write

```
x_t = (4a^2-b^2)/(4a^2+b^2).
```

Suppose `p | 4a^2+b^2`. If `p|b`, then `p|a`, contradicting primitiveness. Hence
`b` is invertible modulo `p` and

```
(2ab^{-1})^2 ≡ -1 mod p.
```

This is impossible when `p ≡ 3 mod 4`. Therefore `p ∤ 4a^2+b^2`, so `x_t` is
p-integral. Chebyshev polynomials have integer coefficients, so
`T_j(x_t)` and `C_j(t)=1-T_j(x_t)` are p-integral for every `j`.

## §2. A useful off-line pole

Write `u_0=ξ/p^δ` with `v_p(ξ)=0`. For `j≥1`,

```
T_j(z) = 2^{j-1}z^j + (terms of degree < j).
```

Thus

```
v_p(T_j(u_0)) = -jδ
```

unless cancellation occurs between the leading term and lower-degree terms.
When the trace of `ξ^j` from `F_{p^2}` to `F_p` is nonzero, no such cancellation
occurs in the real part: the leading pole of

```
(T_j(u_0)+overline{T_j(u_0)})/2
```

has coefficient `Tr(ξ^j)/2`, which is a p-adic unit because `p` is odd. Hence

```
v_p(D_j(u_0)) = -jδ
```

for every such `j`.

The reduction of `ξ` has finite order `N` in `F_{p^2}^*`. For every positive
multiple `j` of `N`, `ξ^j` reduces to `1`, whose trace is `2≠0`. Choose the
largest positive multiple of `N` not exceeding `m`. It is at least `m-N+1`
when `m≥N`. Therefore

```
B_m ≥ δ(m-N+1)
```

for `m≥N`. The weaker displayed bound `δ max(0,m-N)` is conservative and also
covers `m<N` by making the right-hand side zero.

## §3. Conclude from any relation

Assume

```
Σ_k c_kC_j(t_k)+qD_j(u_0)=0
```

for every `j`. By §1 the on-line sum is p-integral. Therefore `qD_j(u_0)` is
p-integral for every `j`. Choosing `j` that realizes `B_m` gives

```
v_p(q) ≥ B_m.
```

Combining with §2 yields

```
v_p(q) ≥ δ max(0,m-N),
```

and hence `|q|≥p^{B_m}≥p^{δ max(0,m-N)}`.

