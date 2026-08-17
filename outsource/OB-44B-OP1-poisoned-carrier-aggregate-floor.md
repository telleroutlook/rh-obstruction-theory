# Problem OB-44B — Poisoned odd carriers and the full relation-size floor

**Type:** p-adic valuation theory / determinantal lattice geometry

**Non-circularity.** All objects are finite rational matrices, Chebyshev values,
and p-adic valuations. This problem assumes no RH-equivalent condition, no
L-value, no zero of `ζ`, and no analytic zero-counting input. RH stays `[OUT]`.

This is the adversary half of OP1's odd-carrier route. OB-44A asks for a simple
prime factor of the orbit norm. This problem asks what happens when rational
node choices poison all such simple factors, with the output measured by the full
integer relation size rather than by `q_min` alone.

---

## 1. All definitions

For a rational prime `p` and nonzero rational `x`, let `v_p(x)` be the p-adic
valuation of `x`.

### 1.1 Rational nodes and Chebyshev columns

Let `m ≥ 2` be the observation dimension and let `K ≥ m` be the number of
on-line nodes. Let `T_j` be the Chebyshev polynomial of the first kind:

```
T_0=1,       T_1=x,       T_{j+1}=2xT_j−T_{j−1}.
```

A rational node is `t=u/v` with `u∈Z\{0\}`, `v≥1`, and `gcd(u,v)=1`. Define

```
D(t)=4u²+v²,
x(t)=(4u²−v²)/D(t),
C_j(t)=4(1−T_j(x(t))) ∈ Q.
```

A configuration is `T=(t_1,...,t_K)` with `x(t_1),...,x(t_K)` pairwise distinct.
Its height is `H(T)=max_k max(|u_k|,v_k)`.

### 1.2 Row-3 orbit and carrier primes

Fix integers `a,n` such that

```
n even, positive, 3∤n, a odd, 1≤a<n, gcd(a,n)=1.
```

Put

```
r=a²+n²−na,
N=r²+n⁴.
```

A prime `p` is a **simple carrier** if `v_p(N)=1`. It is **node-integral at
`t=u/v`** if `p∤D(t)`, and node-integral for `T` if this holds for every node.
If `p|D(t)`, then `t` **poisons** `p`.

### 1.3 Canonical observation matrix and `q_min`

Let

```
U(a,n)={a/n+i, a/n−i, 1−a/n+i, 1−a/n−i}.
```

Define the rational orbit vector `d(a,n)=(d_1,...,d_m)` by

```
d_j=2 Σ_{rho∈U(a,n)}
    Re(1−(1−1/rho)^j).
```

The factor `2` is part of the fixed reflection-doubled normalization. Do not
rescale `d` alone.

Form the rational `m×(K+1)` matrix

```
[C(t_1) ... C(t_K) | d(a,n)].
```

Let `L` be the least common multiple of the denominators of all entries of this
matrix, and define

```
A(T)=L[C(t_1) ... C(t_K)],
d_int(a,n)=L d(a,n).
```

Replacing `L` by a common positive multiple multiplies every column by the same
number and leaves the ratio below unchanged. Per-column or `d`-only rescaling is
not allowed.

For an integer matrix `X`, let `D_m(X)` be the gcd of its `m×m` minors. Define

```
q_min(T,a,n)=D_m(A(T))/D_m([A(T)|d_int(a,n)]).
```

The factorization in §1.4 implies `rank A(T)=m` whenever at least `m` of the
`x(t_k)` are pairwise distinct (as required). Thus `d` lies in the rational
column span and `q_min` is a positive integer.

Define the full integer relation lattice

```
Lambda(T,a,n)
 = {(c_1,...,c_K,q)∈Z^{K+1}:
    A(T)c+q d_int(a,n)=0, q≠0}.
```

Its sup-norm

```
size(T,a,n)=min_{(c,q)∈Lambda} max(|q|,|c_1|,...,|c_K|)
```

is the resource-bounded collision size. A `q_min` bound alone is weaker: it
controls only the off-line coefficient.

### 1.4 Graded basis and moment vector

For `i=1,...,m`, define

```
q_i(x)=(1−T_i(x))/(x−1).
```

Division is exact because `T_i(1)=1`. Write

```
4q_i(x)=Σ_{l=0}^{i−1}B[i][l]x^l,
```

and let `B=(B[i][l])`. Then `B` is lower triangular and

```
det B=±2^{m(m+3)/2}.
```

Let `V(x_1,...,x_m)=[x_k^{i-1}]_{i,k=1}^m`. Since
`C_i(x)=(x−1)4q_i(x)`,

```
[C(t_1) ... C(t_m)]
 = B V(x_1,...,x_m) diag(x_1−1,...,x_m−1).
```

The display uses a chosen `m`-tuple of nodes. When `K>m`, the determinantal
divisors take the gcd over all `m`-subsets; no rectangular extension of Lemma
BRIDGE is being assumed.

Define

```
w(a,n)=B^{-1}d(a,n),
M=(a²−n²−na)+n(2a−n)i,
β=n²/(2M).
```

Equivalently, with `w_+=a+ni` and `w_-=(a−n)+ni`,

```
M=w_+w_-,
N=|M|²=|w_+|²|w_-|².
```

The following lemma records the exact two-point reduction of the reflection sum.

### Lemma MOMENT

For `i=0,...,m−1`,

```
N=|M|²,
w_i=β(1+β)^i+conjugate(β)(1+conjugate(β))^i
```


**Proof.** Put `rho=a/n+i` and `W(rho)=1−1/rho`. The reflection
`rho↦1−rho` sends `W` to `W^{-1}`. Thus one reflection pair contributes

```
(1−W^i)+(1−W^{-i}) = 2(1−T_i((W+W^{-1})/2)).
```

Adding the conjugate reflection pair and then the fixed outer factor `2` gives

```
d_i=8(1−Re T_i(u)),       u=(W+W^{-1})/2.
```

A direct rational simplification gives

```
u=1+β,       β=u−1.
```

Therefore, using `(1−T_i(x))=(x−1)q_i(x)`,

```
4[βq_i(1+β)+conjugate(β)q_i(1+conjugate(β))]
 = 4[(1−T_i(u))+(1−conjugate(T_i(u)))]
 = d_i.
```

But `w_i=β(1+β)^i+conjugate(β)(1+conjugate(β))^i`, and the `i`-th row of
`B` evaluates `4q_i` on these moments. Hence `Bw=d`. The identity `N=|M|²`
is a polynomial expansion. ∎

---

## 2. Included clean-carrier theorem

This theorem is included so that the only open question is the poisoned case.

### Lemma POLE

If `p||N`, then

```
v_p(w_i)=−(i+1),       i=0,...,m−1.
```

**Proof.** Since `gcd(r,n)=1`, `N=r²+n⁴` is a sum of coprime squares. It is odd,
so every rational prime divisor is `1 mod 4`. Thus `p=ππbar` splits in `Z[i]`.
From `N=|M|²` and `v_p(N)=1`, exactly one of `π,πbar` divides `M`, with
exponent one. Also `p∤n`. Therefore

```
v_π(β)=v_π(n²)−v_π(2M)=−1,
```

and `1+β` has the same valuation because a valuation-`-1` pole dominates the
constant `1`. In the closed form for `w_i`, the conjugate summand is `π`-integral,
while

```
v_π(β(1+β)^i)=−(i+1).
```

Strict domination gives `v_π(w_i)=-(i+1)`. No negative valuation occurs at
`πbar`, so the rational valuation has the same value. ∎

### Lemma BRIDGE (square case `K=m`)

Suppose `K=m`. If `p||N` and `p` is node-integral for `T`, then

```
v_p(q_min(T,a,n))≥m.
```

**Proof.** Write `x_k=x(t_k)`. For each `j`, let

```
N_j=Σ_{k≠j}v_p(x_j−x_k),
```

and let `X'_j={x_k:k≠j}`. Define

```
S_j=
  Σ_{i=0}^{m−1}
    (-1)^{i+j}e_{m-1-i}(X'_j)w_i,
C_j^val=v_p(S_j),
```

where `e_s` is the elementary symmetric polynomial of degree `s`.

Let

```
V'_j=det[x_k^r]_{0≤r≤m−2, k≠j}
```

be the ordinary `(m−1)×(m−1)` Vandermonde determinant on `X'_j`.
Replacing column `j` of the factorized online matrix by `d=Bw` gives the minor

```
det A_j(d)
 = det B · ∏_{k≠j}(x_k−1) · V'_j · S_j.
```

This identity is linear in the arbitrary vector `w`; it does **not** require
`w_i` to be the value of a polynomial at a node. Expand the determinant on the
replaced column `w`. The cofactor of `w_i` is, up to the displayed sign, the
determinant of the Vandermonde matrix with row `i` and column `j` deleted. The
classical alternant identity gives

```
det[x_k^r]_{r∈{0,...,m−1}\setminus{i}, k≠j}
 = V'_j · e_{m-1-i}(X'_j).
```

Substituting this cofactor into the column expansion gives the displayed minor
identity.

Since

```
det A = det B · V(x_1,...,x_m) · ∏_k(x_k−1)
```

and the full Vandermonde differs from `V'_j` by a unit-sign product whose
p-adic valuation is `N_j`, dividing the minor valuation by that of `det A`,
using `v_p(det B)=0` and node-integrality (`v_p(x_k−1)=0`), gives

```
v_p(q_min)=max_j(N_j−C_j^val).
```

Node-integrality gives `p∤D(t_k)`, so every `x_k` and `x_k−1` is p-integral.
Hence every elementary symmetric coefficient in `C_j^val` is p-integral. By Lemma
POLE, the bottom term `w_{m-1}` has valuation `-m`, while every lower term has
valuation greater than `-m`. Thus `C_j^val=-m` for every `j`, and

```
v_p(q_min)=max_j(N_j+m)≥m.
```
∎

This theorem is conditional on an unpoisoned simple carrier and, as stated, on
the square case `K=m`. The remaining problem is whether simultaneous poisoning
and/or additional nodes can destroy the full relation-size floor.

### Scope of `K`

The actual Problem B below concerns `K≥m`, including `K=m+1` and unbounded
extra nodes. Lemma BRIDGE is only the square baseline; it is not being extended
by notation. A square-only result is not a CONFIRMED outcome. Moreover, the
numerical anchor below gives `K=m+1` configurations with `q_min=1`, so any
rectangular theorem must address the on-line coefficients as well.

---

## 3. Problem to be solved

> **Problem B.** Suppose `N(a,n)` has at least one simple carrier. Prove, for
> arbitrary rational node configurations, a bound on the full relation size
> ```
> log size(T,a,n)≥c(a,n)m−O_{a,n}(1),
> ```
> where `c(a,n)>0` may depend on the orbit but not on `m` or `T`. A uniform
> `c>0` over Row-3 orbits is stronger and welcome. A separate `q_min` lower
> bound is also interesting, but it does not by itself close the resource-bounded
> question.
>
> Alternatively, refute robustness by constructing infinitely many `m` and valid
> rational configurations poisoning every simple carrier for which
> `log size=o(m)` (or, for the weaker formulation, `log q_min=o(m)`).

A useful square-case intermediate target is

A useful intermediate target is

```
max_{p||N}v_p(q_min(T,a,n))≥c(a,n)m−O(1),
```

for `K=m`, together with a bound explaining how any lost p-adic floor reappears
in the on-line coefficients `c_k`. For `K>m`, the finite anchor below already
has `q_min=1`, so `q_min` is only a diagnostic. A height-refined full-size
target could take the form
`log size≥f(a,n,m,H(T))`.

### Why the adversary is nontrivial

Every simple carrier is `1 mod 4`, so `-1` is a quadratic residue modulo `p`.
Equivalently, `-4` is a square modulo the odd prime `p`. Hence there are residue
classes `u/v` modulo `p` satisfying

```
4u²+v²≡0 mod p.
```

By the Chinese remainder theorem, one rational node can poison a finite set of
simple carriers simultaneously. The naive argument “one node kills at most one
prime” is false. The question is whether CRT poisoning necessarily creates
enough p-adic or height complexity elsewhere to preserve an aggregate floor.

---

## 4. Acceptance criteria

Return exactly one of the following.

1. **CONFIRMED.** Prove a linear-log lower bound on the full relation size for
   arbitrary rational node configurations with `K≥m` — including `K=m+1` and
   unbounded extra nodes — for each fixed Row-3 orbit, or prove a uniform orbit
   version. State the dependence on `a,n,K,m,H`.

2. **PARTIAL.** Prove a nontrivial super-logarithmic bound, a linear bound for a
   named infinite family, or a height-refined theorem. A mere proof that
   `q_min>0` is not a PARTIAL success.

3. **REFUTED.** Construct infinitely many valid configurations poisoning every
   simple carrier and satisfying `log size=o(m)`; a `q_min`-only collapse is a
   weaker refutation and must be labeled as such.

4. **STRATEGY.** Give a concrete plan using simultaneous p-adic valuation
   estimates, aggregate Smith-invariant bounds, CRT covering arguments, or
   height-complexity tradeoffs. Identify which sublemmas are standard and which
   are new.

5. **INCONCLUSIVE.** Identify the exact missing lemma and explain why Lemma
   BRIDGE does not extend to poisoned carriers.

---

## 5. Numerical anchor (sanity only, not a proof input)

Take `a=1`, `n=10`. Then

```
N=18281=101·181.
```

For integer nodes `t=1,2,3,4`,

```
4t²+1=5,17,37,65,
```

so neither `101` nor `181` is poisoned. Lemma BRIDGE predicts

```
v_{101}(q_min)≥4,
v_{181}(q_min)≥4.
```

The residue classes

```
t≡5 mod 101,       t≡81 mod 181
```

satisfy `4t²+1≡0` modulo the respective prime. Their CRT combination is

```
t=17276,
```

and

```
4·17276²+1≡0 mod 101 and mod 181.
```

Thus one node can poison both simple carriers. The factorization,
non-divisibility, residue roots, and CRT witness were checked by exact integer
arithmetic; none is a proof input.

For the poisoned two-node configuration `(17276,1)` (`m=K=2`), the canonical
normalization above gives

```
q_min=218246018367,
v_101(q_min)=v_181(q_min)=1.
```

Thus poisoning both carriers reduces these two valuations from the clean `m=2`
floor to `1`; the open question is whether this is only an additive correction
or can become multiplicative collapse as `m→∞`.

A sharper poisoned pair with `m=K=2` is

```
t_1=19286,       t_2=26164.
```

Both poison `101` and `181`, but the canonical normalization gives

```
q_min=18,        v_101(q_min)=v_181(q_min)=0.
```

One exact relation is

```
q=18,
c_1=-1788723758742137225,
c_2= 3292056116081922725.
```

So the carrier p-adic floor has disappeared, while the full relation still has
sup-norm about `3.3×10^18`. This illustrates why the external target must include
the on-line coefficients, not only `q_min`.

With one extra node, even `q_min=1` can occur while all simple carriers remain
poisoned. For `m=2`, `K=3`, and

```
t_1=1005,       t_2=7883,       t_3=-10398,
```

each node poisons both `101` and `181`, and the canonical normalization gives

```
q_min=1,         v_101(q_min)=v_181(q_min)=0.
```

An exact full relation is

```
q=1,
c_1=-339609544170,
c_2=16156893919328,
c_3=8242578942472.
```

Thus a `q_min`-only formulation is already false for rectangular node sets. The
nontrivial remaining quantity is the full relation sup-norm, here
`16156893919328`.

---

## Pre-send lint record

| PROMPT_LINT item | Result |
|---|---|
| L1–L4 | N/A: no entire-function, canonical-product, or zero-location claim. |
| L5 | PASS: no RH input; the orbit is a finite arithmetic object, not a zero of `ζ`. |
| L6 | PASS: full, partial, refutation, strategy, and inconclusive paths are non-vacuous; `q_min>0` alone is excluded. |
| L7/L8 | PASS: the reflection-doubled `d` normalization and canonical common denominator `L` are fixed in §1.3. |
| L9–L16 | PASS/N/A: no analytic growth, Taylor-jet, Fredholm, or representation-invariant margin is assumed. |
| L17 | PASS: no external black box is assumed; POLE and BRIDGE are stated and proved in-file. |
| L18 | PASS: exact anchor is labeled sanity only. |
| L19 | PASS: PARTIAL and INCONCLUSIVE are first-class honest outcomes. |
| L20–L24 | N/A. |
| Self-containment | PASS: rational nodes, canonical clearing, `q_min`, full relation size, moment system, POLE, BRIDGE, adversary, outcomes, and anchor are defined in-file. |
| Privacy | PASS: no personal path, username, company, or internal host occurs. |
| Execution record (2026-08-17) | PASS: `checker/ob44b_prompt_anchor.py` verifies `Bw=d`, clean valuations, and the poisoned anchor in exact rational arithmetic; structural/focus/privacy checks and `git diff --check` pass at final rerun. |
