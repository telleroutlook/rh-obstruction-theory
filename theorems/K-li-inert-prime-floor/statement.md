# Statement — Theorem K (inert-prime Li-collision floor)

**Theorem ID:** K-li-inert-prime-floor  
**Mathematical status:** PROOF-DRAFT (prepared for Gate-A review)  
**Computational status:** NONE for the analytic theorem  
**Program ref:** Paper A Open Problem 1 / uniform on-line-node floor  
**Paper target:** eventual arithmetic-complexity companion; not yet promoted into Paper A

---

## §1. Chebyshev observation normalization

Let `T_j` be the Chebyshev polynomial of the first kind. For a primitive
rational on-line node `t=a/b` (`a∈Z`, `b≥1`, `gcd(a,b)=1`), put

```
x_t = (4a^2-b^2)/(4a^2+b^2),
C_j(t) = 1 - T_j(x_t).
```

Let `u_0 ∈ Q(i)` represent an off-line orbit and define

```
D_j(u_0) = 1 - (T_j(u_0) + overline{T_j(u_0)}) / 2.
```

The factors used in other Li conventions are irrelevant here: multiplying all
observations by a common nonzero rational constant does not change integer
relations.

## §2. Inert-prime hypothesis

Let `p ≡ 3 mod 4` be prime, so `p` is inert in `Z[i]`. Suppose

```
v_p(u_0) = -δ < 0
```

in the unique extension of `v_p` to `Q(i)`. Write

```
u_0 = ξ / p^δ,       ξ ∈ Z[i],   v_p(ξ)=0.
```

Let `N` be the multiplicative order of the reduction of `ξ` in
`F_{p^2}^*`. Define

```
B_m = max_{1≤j≤m} max(0, -v_p(D_j(u_0))).
```

## §3. Theorem

**Theorem K.** For every finite set of primitive rational on-line nodes
`t_1,...,t_K` and every integer relation

```
sum_{k=1}^K c_k C_j(t_k) + q D_j(u_0) = 0
      for j=1,...,m,
```
one has

```
v_p(q) ≥ B_m ≥ δ · max(0, m-N).
```

Consequently,

```
|q| ≥ p^{B_m} ≥ p^{δ max(0,m-N)}.
```

The bound is uniform in the number and choice of rational on-line nodes.

## §4. Non-claim

This proves an exponential floor only for off-line orbits whose `u_0` has an
inert prime in its denominator. It does not cover split-only denominators and
does not solve full Open Problem 1.
