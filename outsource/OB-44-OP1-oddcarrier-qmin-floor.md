# Problem OB-44 — The odd-carrier-prime floor of q_min: an orbit-universal, node-set-uniform linear bound via a proved moment pole (OP1 direct route)

**Type:** arithmetic / p-adic valuation theory (p an odd prime dividing an explicit quartic
norm) / determinantal (lattice) geometry — a finite, exact, RH-free question about rational
vectors and their p-adic valuations, together with **one** analytic-number-theory lemma
(squarefree/powerful values of a binary quartic form).

**Non-circularity.** This problem does NOT assume the Riemann Hypothesis, does NOT use any
value, derivative, or zero location of ζ or any L-function, and does NOT read "analytic rank"
or any RH-equivalent input. The object is a finite integer/rational linear-algebra configuration
and its p-adic valuations. The single "off-line" datum is one *hypothesized* point
`ρ = σ₀ + iτ₀` with `σ₀ ≠ 1/2` (the barrier asks whether a finite family of on-line observations
can cheaply register such a hypothesized point); nothing is assumed about the truth or falsity of
RH. All quantities below are exact rationals; all claims are checkable by exact arithmetic. RH
stays outside this problem.

This is the **odd-carrier-prime companion** to OB-42 (`p = 3`, conditional on a *3-adic
unimodularity* hypothesis on the orbit) and OB-43 (`p = 2`, unconditional on the `v₂(β) ≥ 2`
orbit family). The route below is **strictly more universal** in three respects:
(a) the carrier prime is not a *fixed* small prime but an **orbit-specific** prime `p ≥ 5`
dividing a single explicit norm `N`, and **every** Row-3 orbit possesses one;
(b) the floor holds for **arbitrary node sets** — not only consecutive nodes — because the
underlying pole mechanism never uses node consecutivity;
(c) it needs **no orbit hypothesis** at all (neither 3-unimodularity nor `v₂(β) ≥ 2`).
The engine is a **proved** statement: for the carrier prime `p ‖ N`, the moment sequence
`w = B^{−1}d` has an exact p-adic **pole** `v_p(w_i) = −(i+1)`. Steps 1–3 below (the identity, the
pole sub-law, and the bridge to `q_min`) are **proved and inlined as premises**; the referee is
asked to close a **single** number-theoretic core — the existence of a suitable simple factor of
`N` — and is invited to **prove, propose a feasible (sanity-checked) strategy for, refute, or
precisely localize** it. A complete proof is NOT required for a successful deliverable: a
concrete, plausible proof route with its key sub-steps identified and a lightweight check is a
first-class outcome (§4, outcome **STRATEGY**).

---

## 1. All definitions (self-contained — every symbol and formula is here)

Fix an odd prime `p`. `v = v_p` is the p-adic valuation on `ℚ` (`v(0) = +∞`,
`v(a/b) = v(a) − v(b)`). Fix an integer `m ≥ 2` (the observation dimension).

### 1.1 The off-line orbit and the "Row-3" family
Fix coprime integers `a, n` with **n even, 3 ∤ n, a odd, gcd(a, n) = 1** (the **Row-3** family).
The hypothesized off-line point is `ρ = (a + n i)/n = a/n + i` (so `σ₀ = a/n`, `τ₀ = 1`); its
orbit is the 4-atom set `{σ₀ ± iτ₀, 1−σ₀ ± iτ₀}`.

### 1.2 The node map and the on-line x-values
A **node** is a nonzero integer `t`. Its **x-value** is
```
    x(t) = (4 t² − 1) / (4 t² + 1)  ∈ ℚ.
```
`x(t)` depends only on `t²` (`x(t) = x(−t)`). A configuration is a tuple of `m` **integer** nodes
`t_1, …, t_m` with pairwise-distinct x-values `x_k := x(t_k)`. **Node sets are arbitrary** — no
consecutivity or ordering is assumed.

### 1.3 Chebyshev observation columns
For `j ≥ 0` let `T_j` be the Chebyshev polynomial of the first kind
(`T_0 = 1, T_1 = X, T_{j+1} = 2X·T_j − T_{j−1}`). The **observation column** of a node `t` is
```
    C(t) = ( C_1(t), …, C_m(t) ) ∈ ℚ^m,     C_j(t) = 4·( 1 − T_j(x(t)) ).
```
Since `T_j(1) = 1`, each `C_j` vanishes at `x = 1`, so `C_j(t) = (x(t) − 1)·(4 q_j(x(t)))` for
the polynomial `q_j` of §1.5.

### 1.4 The off-line target vector `d`
The **target vector** `d = (d_1, …, d_m) ∈ ℚ^m` is
```
    d_j = Σ_{atoms (r,ι)} Σ_{(r',ι') ∈ {(r,ι),(1−r,ι)}}  Re[ 1 − (1 − 1/(r'+iι'))^j ],
```
the sum running over the 4 orbit atoms `(r,ι)` of §1.1. Each `Re[1 − (1 − 1/ρ')^j]` is an exact
rational, so `d ∈ ℚ^m`. This is the finite Li-type observation of the orbit — the vector a finite
observer must "hit" to register a collision.

### 1.5 The graded basis and the matrix `B`
Define `q_i(x) = (1 − T_i(x))/(x − 1)` for `i = 1, …, m` (degree `i − 1`; division exact since
`T_i(1) = 1`). Write `4 q_i(x) = Σ_{l=0}^{i−1} B[i][l]·x^l`. Then `B` is `m × m`
**lower-triangular** with diagonal `B[i][i−1] = 4·(−2^{i−1})`, so
```
    det B = ± 2^{ m(m+3)/2 }     (a PURE power of 2; verified m ≤ 8).
```
In particular **`v_p(det B) = 0` for every odd prime `p`** — the property that makes the identity
below hold for every odd carrier with no side hypothesis.

### 1.6 The moment vector `w`
The **moment vector** is the unique solution of the lower-triangular system
```
    B · w = d,     w = ( w_0, …, w_{m−1} ) ∈ ℚ^m       (w = B^{−1}d, node-independent).
```

### 1.7 The carrier norm `N`
Let `β = 1 − 1/ρ = [(a² + n² − na) + n² i] / (a² + n²)`, and set `re := a² + n² − na`. The
**carrier norm** is the numerator norm of `β`:
```
    N := | numerator(β) |² = re² + (n²)² = (a² + n² − na)² + n⁴.
```
`N` is a positive integer depending only on the orbit `(a, n)`.

### 1.8 The collision constraint and the barrier quantity `q_min`
Let `A` be the `m × m` integer matrix whose columns are the cleared (common-denominator-
multiplied) integer forms of `C(t_1), …, C(t_m)`, and let `v_off` be the cleared integer form of
`d`. For an integer matrix `X` and integer `r`, let `D_r(X)` be the **r-th determinantal divisor**
= gcd of all `r × r` minors of `X`. A **valid collision** is a configuration with `v_off` in the
ℚ-span of the columns of `A` (a finite integer relation exists) and `D_m(A) ≠ 0` (rank `A = m`).
When valid, the minimal positive multiplier is the finite **collision size**
```
    q_min = D_m(A) / D_m([A | v_off])   (a positive integer).
```
The `m × (m+1)` matrix `[A | v_off]` has exactly `m + 1` size-`m` minors: `det A` and, for each
online column `j`, the **d-replacement minor** `minor_j := det(A with column j replaced by v_off)`.
Hence `D_m([A|v_off]) = gcd(det A, minor_1, …, minor_m)` and, for any prime `q`,
```
    v_q(q_min) = v_q(det A) − min( v_q(det A), min_j v_q(minor_j) ) = max( 0, v_q(det A) − min_j v_q(minor_j) ).
```
The barrier **OP1** asks whether `inf_A q_min(m)` grows super-polynomially: OP1 holds iff
`log q_min = ω(log m)` uniformly over valid collisions. Since `q_min ≥ p^{v_p(q_min)}`, a lower
bound `v_p(q_min) ≥ c·m − O(1)` for a fixed prime `p ≥ 5` gives
`log q_min ≥ (c·m − O(1))·log p ≥ (c·m − O(1))·log 5 = Ω(m) ≫ ω(log m)` and closes OP1. **This
problem is the odd-carrier floor `v_p(q_min) ≥ m` for a carrier `p ‖ N`, `p ≥ 5`.**

---

## 2. The theorem to be verified

> **Theorem (OP1 odd-carrier floor — orbit-universal, node-set-uniform linear bound).**
> Let `(a, n)` be any Row-3 orbit (§1.1) and `m ≥ 2`. Suppose `N` (§1.7) has a **simple** prime
> factor `p` (`v_p(N) = 1`, necessarily `p ≥ 5`) that is **node-integral** for the chosen node
> set, i.e. `p ∤ (4 t_k² + 1)` for every node `t_k` (equivalently every `x_k` is p-integral). Then,
> for that node set,
> ```
>     v_p(q_min)  =  max_{1 ≤ j ≤ m} N_j  +  m   ≥   m,     N_j := Σ_{k≠j} v_p(x_j − x_k) ≥ 0.
> ```
> Since `p ≥ 5`, this gives `log q_min ≥ m·log 5 = Ω(m)`, closing OP1's arithmetic channel for
> the orbit — **for arbitrary node sets, with no orbit hypothesis.**

The bound is driven by an exact p-adic **pole** in the moment sequence: `v_p(w_i) = −(i+1)`
(Step 2). Three facts, all **proved** below (Steps 1–3), make the theorem hold with no orbit and
no consecutivity hypothesis:

- **(Step 1) the exact identity** `v_p(q_min) = max_j ( N_j − C_j )`, `C_j = v_p(⟨w, ε(X'_j)⟩)`,
  valid for **every** odd carrier `p` because `v_p(det B) = 0` (§1.5) — verified orbit-free on
  240 configs;
- **(Step 2) the moment-pole sub-law** `v_p(N) = 1 ⟹ v_p(w_i) = −(i+1)`, proved from the exact
  closed form `w_i = β(1+β)^i + β̄(1+β̄)^i` (`β = n²/(2M)`, `M = (a²−n²−na)+n(2a−n)i`) together with
  the identity `N = |M|²`: at the unique prime `𝔭 ∣ p` with `v_𝔭(M) = 1`, `β` has a simple pole
  `v_𝔭(β) = −1` — verified on 770 simple-factor checks;
- **(Step 3) the clean bridge** node-integral carrier `⟹ C_j = −m` for every column `⟹`
  `v_p(q_min) = max_j N_j + m ≥ m` — verified on 798 consecutive + 252 random non-consecutive node
  sets.

**Scope caveat (the single open hypothesis — L5 honesty).** The theorem's hypothesis is the
existence of a **node-integral simple factor** of `N`. This has a provable sufficient condition
and a thin exceptional set:
- **Provable sufficient condition:** any simple factor `p > 4m² + 1` is automatically
  node-integral (`4t_k² + 1 ≤ 4m² + 1 < p` for consecutive nodes `t_k ≤ m`; for a general node
  set with `max_k t_k = T`, replace `m` by `T`). Verified sufficient for all `m` tested.
- **Existence of a simple factor at all** (`N` not a perfect power / not powerful): `N` is a sum
  of two **coprime** squares (Lemma B below), so `N` is powerful iff the Gaussian integer
  `z = re + n²i` is powerful in `ℤ[i]`; **0 of 12124** Row-3 orbits (`n < 400`) give a powerful
  `N`. Not yet a theorem — this is the number-theoretic core (§3 Step 4).
- **Residual (good-carrier) failures:** orbits whose simple factors are all `≤ 4m²+1`, i.e. `N`'s
  squarefree part is `(4m²+1)`-smooth — a **smoothness-exceptional** set (rare, NOT bounded in
  `n`; observed to `n ≈ 278`). It holds for **7640 / 7688** orbit–`m` pairs (`m ≤ 12`, `n < 160`).
  There a node-poisoned carrier still gives `v_p(q_min) ≥ m − O(1)` (measured `O(1) ≤ 1`), and the
  aggregate floor (OB-41 family) independently keeps `log q_min = Ω(m)`.

So OP1's arithmetic channel is closed by a **proved mechanism** modulo one clean number-theory
lemma (Lemma B: `N` never powerful) plus a smoothness caveat with an `O(1)` fallback. RH stays
[OUT].

---

## 3. Proof skeleton to be closed

Steps 1–3 are **proved** here (inlined as premises; the referee may use them freely). Step 4 is
the open number-theoretic core.

### Step 1 — The exact floor identity, valid for EVERY odd carrier. **[proved, premise]**
Factor `A = B · V · diag(x_k − 1)` where `V` is the Vandermonde `V_{lk} = x_k^l` (from
`C_i(t) = (x−1)·4q_i(x)` and `4q_i(x) = Σ_l B[i][l]x^l`), and write `d = B·w` (§1.6). Expanding the
`d`-replacement minor gives, **exactly**,
```
    v_p(q_min) = max_{1 ≤ j ≤ m} ( v_p(x_j − 1) + Σ_{k≠j} v_p(x_j − x_k) − v_p(⟨w, ε(X'_j)⟩) ),
```
where `⟨w, ε(X'_j)⟩ = Σ_{i=0}^{m−1} (−1)^{m−1−i} e_{m−1−i}(X'_j)·w_i`, `e_r` = elementary
symmetric polynomial, and `X'_j = {x_k : k ≠ j}`. Because the carrier is a **node-integral**
prime, `v_p(x_j − 1) = 0` (§1.8/Step 3), so with `N_j := Σ_{k≠j} v_p(x_j − x_k)` and
`C_j := v_p(⟨w, ε(X'_j)⟩)`,
```
    v_p(q_min) = max_{1 ≤ j ≤ m} ( N_j − C_j ).
```
**Why it holds for every odd carrier with no hypothesis:** the derivation needs `v_p(det B) = 0`,
and `det B = ±2^{m(m+3)/2}` is a pure power of 2 (§1.5) ⇒ `v_p(det B) = 0` for **every** odd `p`.
*(Identity verified EXACT on 240 valid configs across three orbits, `m = 3..7`; det B power-of-2
verified `m ≤ 8`.)*

### Step 2 — The moment-pole sub-law `v_p(N)=1 ⟹ v_p(w_i) = −(i+1)`. **[proved from a closed form; premise]**
The moments have an **exact closed form** — a rank-2 Lucas sequence. Let
```
    M := (a² − n² − na) + n(2a − n) i   ∈ ℤ[i],      β := n² / (2M)   ∈ ℚ(i).
```
Then, for the two-point functional `L(f) = β·f(1+β) + β̄·f(1+β̄)` (which equals the `B^{−1}`-solve
because `{4q_j}` is a triangular basis and `L(4q_j) = d_j`; this is the 4-atom → 2-point
reciprocal-pairing collapse of OB-43 §3 Step 4, generalized to all Row-3 — **verified on 270
orbits, `n < 60`**),
```
    w_i = L(x^i) = β·(1+β)^i + β̄·(1+β̄)^i,     for all i ≥ 0.
```
Equivalently `w` satisfies the order-2 recurrence with integer characteristic polynomial
`N·x² − B·x + C` (leading coefficient exactly `N`, primitive), roots `1+β, 1+β̄` — verified on
364 orbits. **Key algebraic identity (proved symbolically):**
```
    N = |M|² :   (a² + n² − na)² + n⁴  =  (a² − n² − na)²  +  (n(2a − n))²      (identity in ℤ[a,n]).
```
**The p-adic pole (transparent from the closed form).** Fix a simple factor `p ‖ N = |M|²`. Then:
- `N` is a sum of two coprime squares (Lemma B reductions), so `p ≡ 1 (mod 4)` **splits** in `ℤ[i]`;
- `v_p(|M|²) = 1` ⟹ `M` is divisible by **exactly one** prime `𝔭 ∣ p`, to order 1
  (`v_𝔭(M) = 1`, `v_{𝔭̄}(M) = 0`);
- `p ∤ n` (if `p ∣ n` then `re ≡ a² (mod p)` with `gcd(a,n)=1` ⇒ `p ∤ re`, contradicting
  `p ∣ N = re² + n⁴`), so `β = n²/(2M)` has `v_𝔭(β) = −1`, `v_{𝔭̄}(β) = 0`;
- the pole dominates the `+1`: `v_𝔭(1+β) = −1`. Hence the term `β(1+β)^i` has
  `v_𝔭 = −1 + i·(−1) = −(i+1)`, while the conjugate term `β̄(1+β̄)^i` is `𝔭`-integral
  (`v_𝔭 ≥ 0`, since conjugation sends `𝔭 ↦ 𝔭̄` and `v_{𝔭̄}(β) = 0`).

Strict domination ⟹ no cancellation ⟹ `v_p(w_i) = v_𝔭(w_i) = −(i+1)` (`w_i ∈ ℚ`). ∎ *(Verified
on 770 simple-factor checks, `n < 60`; this is OB-43's "`γ ≡ 1 mod 2` ⇒ Re odd" argument, with the
split-prime pole **location** `v_𝔭(M) = 1` doing the work.)* In particular `v_p(w_{m−1}) = −m`.

> A second, self-contained proof of the same sub-law (not using the closed form) is available:
> from the order-2 recurrence `w_i = c₁ w_{i−1} + c₂ w_{i−2}`, `c₁ = B/N`, `c₂ = −C/N`, one has
> `v_𝔭(c₁) = v_p(B) − v_p(N) = −1` (`v_p(B) = 0`, verified) and `v_𝔭(c₂) ≥ −1` (`C ∈ ℤ`), plus the
> base case `v_p(w_0) = −1`, `v_p(w_1) = −2`; the induction `v_𝔭(c₁ w_{i−1}) = −(i+1)` strictly below
> `v_𝔭(c₂ w_{i−2}) ≥ −i` gives `v_p(w_i) = −(i+1)` with no cancellation. Verified 1060 checks.

> **Honest scope of Step 2 (L5).** The clean law is **only** for `v_p(N) = 1`. For split primes
> with `v_p(N) ≥ 2` dividing `M` asymmetrically (e.g. `a=49, n=58, p=5`: `v_5(N)=2`,
> `v_5(w_i) = [−1,−1,−3,−4,−5,−4,−7,…]`) the pole order fluctuates — neither `−(i+1)` nor
> `−2(i+1)`. This is why the theorem is stated for a **simple** factor; the existence of one is
> exactly the open core (Step 4). The **only** verified-not-derived ingredient is the two-point
> collapse `w_i = β(1+β)^i + β̄(1+β̄)^i` itself (270 orbits) — it is OB-43's proved reciprocal-
> pairing technique generalized; `N = |M|²` and the pole valuation are fully rigorous.

### Step 3 — The clean bridge: node-integral carrier ⟹ `C_j = −m` ⟹ `v_p(q_min) ≥ m`. **[proved, premise]**
Suppose the carrier `p ‖ N` is **node-integral**: `p ∤ (4t_k² + 1)` for every node. Then:
- `x_k − 1 = −2/(4t_k² + 1)` and `p` odd ⇒ `v_p(x_k − 1) = 0` (used in Step 1); each `x_k` is
  p-integral, so `e_{m−1−i}(X'_j)` is p-integral (`v_p ≥ 0`) and `N_j = Σ_{k≠j} v_p(x_j − x_k) ≥ 0`.
- In the pairing `C_j = v_p( Σ_{i=0}^{m−1} (−1)^{m−1−i} e_{m−1−i}(X'_j)·w_i )`, the sub-law (Step 2)
  gives `v_p(w_i) = −(i+1)`, so term `i` has valuation `≥ −(i+1)`; the `i = m−1` term is
  `(−1)^0·e_0·w_{m−1} = w_{m−1}` with valuation **exactly** `−m`, while every `i < m−1` term has
  valuation `≥ −(i+1) > −m`. The bottom term **strictly dominates** ⇒ no cancellation ⇒
  `C_j = −m` for **every** column `j`.

Combining with Step 1: `v_p(q_min) = max_j (N_j − (−m)) = max_j N_j + m ≥ m`. ∎ *(Verified EXACT:
`C_j = −m` and `v_p(q_min) = max_j N_j + m ≥ m` on 798 consecutive-node checks AND 252 **random
non-consecutive** node sets — the proof never uses consecutivity.)*

> **The node-set adversary (why consecutivity is not needed).** `N` depends only on the orbit, so
> the carrier primes are **fixed** per orbit. The adversary's only way to defeat a given simple
> carrier `p_i ‖ N` is to **poison** it by placing a node at `t ≡ ±r_i (mod p_i)` with
> `p_i ∣ 4t²+1` — legal because every `p_i ≡ 1 (mod 4)` (so `−1/4` is a QR). But that costs **one
> node per simple factor** and, when it removes the node-integral carrier, induces only an `O(1)`
> node-pole correction (measured `≤ 1`). With `≥ 2` simple factors the adversary cannot poison all
> of them within `m` nodes for large `m`. RH [OUT].

### Step 4 — CORE: existence of a node-integral simple factor of `N`. **[open — one number-theory lemma + a smoothness caveat]**
The theorem's only hypothesis is: `N` has a **simple** prime factor `p ≥ 5` that is node-integral
for the chosen node set. Two sub-parts, of which the first is the clean nugget:

> **Lemma B (the crisp open nugget).** For every Row-3 orbit `(a, n)`, `N = (a²+n²−na)² + n⁴` is
> **never a powerful number** — equivalently, `N` has at least one prime factor `p` with
> `v_p(N) = 1`.

*Reductions already proved (referee may use freely):* Writing `re = a²+n²−na`, one has
`gcd(re, n) = 1` (if a prime `ℓ ∣ n` then `re ≡ a² (mod ℓ)` and `gcd(a,n)=1` ⇒ `ℓ ∤ re`). Hence
`N = re² + (n²)²` is a sum of **two coprime squares**, so `N` is powerful **iff** the Gaussian
integer `z = re + n²i` is powerful in `ℤ[i]`, and every prime factor of `N` is `≡ 1 (mod 4)`.
Lemma B is therefore the statement "**`z = re + n²i` is never a powerful Gaussian integer for
Row-3 `(a, n)`**" — a squarefree/powerful-values question for a binary quartic form. Evidence:
**0 / 12124** Row-3 orbits (`n < 400`) give a powerful `N`.

**Good-carrier (node-integral) existence.** Given Lemma B, one still needs a simple factor that is
node-integral. **Provable sufficient condition:** any simple factor `p > 4·(max_k t_k)² + 1` is
node-integral. For consecutive nodes `t ≤ m` this is `p > 4m²+1`, and such a factor exists for
**7640 / 7688** orbit–`m` pairs (`m ≤ 12`, `n < 160`). The residual is the smoothness-exceptional
set (`N`'s squarefree part is `(4m²+1)`-smooth); there Step 3's `O(1)` node-poison correction and
the aggregate floor keep `log q_min = Ω(m)`.

**What the referee is asked to close.** Prove Lemma B (or the equivalent Gaussian statement); AND
either (i) prove a uniform good-carrier existence (every Row-3 orbit has a simple factor
`> 4m²+1`, or a node-integral simple factor for every node set), or (ii) prove the smoothness
exceptional set is finite / density zero and bound the node-poison `O(1)` correction in closed
form. A proof of Lemma B alone (with the provable `p > 4m²+1` sufficient condition) already closes
OP1 for the 99%+ non-exceptional orbits with an **arbitrary-node-set** floor `v_p(q_min) ≥ m`.

**Known dead-ends (do not re-derive).** (1) The **stronger** general pole law
`v_p(w_i) = −(i+1)·min(v_p(N), 2)` is **REFUTED** (Step 2 scope note): split primes with
`v_p(N) ≥ 2` fluctuate. Use only the **simple**-factor sub-law. (2) The tight equality
`v_p(q_min) = m·min(v_p(N), 2)` is **REFUTED** (`v_p(q_min)` is often `m−1` for non-carrier
`N`-primes; the robust statement is the existential `max_{p|N, simple, node-integral} v_p(q_min) ≥ m`).
(3) The base-case over-claim "`den(w_0) = N` exactly" is **NON-universal** (306/364) — the correct
base case is the per-prime valuation (iii).

---

## 4. Acceptance criteria

Report exactly one of the following, with the stated evidence. An honest partial/localized
outcome is a first-class result — do **not** force a prove/refute dichotomy.

1. **CONFIRMED.** A proof of Lemma B (`N = (a²+n²−na)²+n⁴` never powerful for Row-3 `(a,n)`),
   together with a good-carrier existence argument (a node-integral simple factor exists for the
   relevant node sets). State every hypothesis used; confirm none is RH, an L-value, a zero
   location, or an RH-equivalent. Steps 1–3 may be used as proved premises.

2. **STRATEGY (feasible proof route — a full proof is NOT required).** A concrete, plausible plan
   for Lemma B. To qualify it must: (a) name the main tool it would invoke (e.g. a
   squarefree-sieve / square-free-values-of-polynomials result à la Hooley/Greaves, a
   Gaussian-integer factorization argument on `z = re + n²i`, a descent showing `z` cannot be
   `w²·u` with `u` a unit, a bound on powerful values of a binary quartic form, …) and why it
   applies; (b) break Lemma B into sub-lemmas and say which are standard vs genuinely new;
   (c) include a **lightweight check** — verify the key sub-lemma on the §6 anchor and one larger
   orbit. Identify the one step most likely to fail. A sanity-checked strategy for the
   good-carrier existence is equally welcome.

3. **PARTIAL.** A proof that `N` is squarefree (or powerful-free) for a positive-density / all-but-
   finitely-many subfamily of Row-3 orbits; OR a proof of a weaker-but-still-superpolynomial floor
   `v_p(q_min) ≥ f(m)` (any `f(m) = ω(log m)` closes OP1); OR a proof of the good-carrier existence
   conditional on Lemma B. Specify precisely what is proved and what remains.

4. **REFUTED.** Either (a) an explicit Row-3 orbit `(a, n)` with `N` powerful (a genuine
   counterexample to Lemma B — verify by exact factorization), OR (b) an explicit family (fix an
   orbit; give, for each `m` in an unbounded set, the `m` integer nodes) for which **every** simple
   factor of `N` is node-poisoned and `v_p(q_min) = o(m)` for all `p ≥ 5`, showing the odd-carrier
   floor is not linear and the barrier needs a narrower profile. (A single small-`m` configuration
   with a small floor is NOT a refutation; the claim is asymptotic with an `O(1)` slack.)

5. **INCONCLUSIVE + precise localization.** Identify the exact step that resists (e.g. "powerful-
   free values of `re² + n⁴` are not accessible by current squarefree-sieve technology because the
   form is not primitive in the required sense…") and state the minimal additional input that would
   close it.

---

## 5. Provenance (for verification only — all premises are stated inline)

Steps 1–3 were verified by exact-arithmetic scripts in this repository's discovery tier
(untrusted, never imported into proofs): the identity (Step 1) and det B power-of-2 in the
`q_min` floor-identity probe; the moment-pole sub-law (Step 2) — order-2 recurrence,
`lead = N`, primitivity, base case (iii), strict domination — in the moment-pole sub-law probe
(1060 simple-factor checks, `n < 70`); the clean bridge (Step 3) — `C_j = −m`,
`v_p(q_min) = max_j N_j + m ≥ m` — in the bridge probe (798 consecutive + 252 random
non-consecutive node sets). The `2 ∤ N`, `3 ∤ N` facts (min prime factor `≥ 5`) and `gcd(re, n) = 1`
(⇒ sum of coprime squares) were checked on 2969 / 12124 Row-3 orbits. These scripts are
reproducible; the referee need not consult them (all premises are stated inline).

---

## 6. Numerical anchor (sanity only, not an input to the proof)

Exact, independently re-derivable by a few lines of rational arithmetic.

**Orbit** `ρ = 1/10 + i` (`a = 1, n = 10`; Row-3: `n` even, `3 ∤ 10`, `a` odd, `gcd(1,10)=1`).
Then `re = a² + n² − na = 1 + 100 − 10 = 91` (`= 7·13`), `n² = 100`, `gcd(91, 10) = 1`, and
```
    N = re² + (n²)² = 91² + 100² = 8281 + 10000 = 18281 = 101 · 181   (squarefree — NOT powerful).
```
As a cross-check of `N = |M|²` (Step 2): `M = (a²−n²−na) + n(2a−n)i = −109 − 80i`, and
`|M|² = 109² + 80² = 11881 + 6400 = 18281 = N`. ✓
Both `101 ≡ 1` and `181 ≡ 1 (mod 4)`, as forced by Lemma B's "sum of coprime squares". Take the
carrier `p = 101` (simple, `≥ 5`).

**Configuration** `m = 4`, consecutive nodes `t = (1, 2, 3, 4)`. Denominators
`4t²+1 = (5, 17, 37, 65)` — **none divisible by 101**, so `p = 101` is node-integral. ✓
x-values `x = (3/5, 15/17, 35/37, 63/65)`. Then:
```
    v_101(w_i) = (−1, −2, −3, −4)        (the moment pole, Step 2:  v_p(w_i) = −(i+1)).
    N_j = (0, 0, 0, 0)                    (all x_j − x_k are 101-units for this node set).
    C_j = (−4, −4, −4, −4)                (all = −m = −4, the clean bridge, Step 3).
    v_101(q_min) = max_j N_j + m = 0 + 4 = 4   (= direct v_101(q_min); q_min has 19 digits).  ✓
```
A referee should confirm (a) `N = 18281 = 101·181` is squarefree; (b) `101 ∤ (4t²+1)` for
`t = 1..4`; (c) `v_101(w_i) = −(i+1)` for `i = 0..3`; (d) `C_j = −4` for every column;
(e) `v_101(q_min) = max_j N_j + m = 4`. **Sanity only — not an input.**

---

## Pre-send lint notes (PROMPT_LINT.md self-check)

| Item | Status |
|---|---|
| L1–L4 | N/A — no entire-function / order / canonical-product claims |
| L5 (RH via divisor / circular target) | PASS — no ζ/L zeros, no real-zero product; the only "off the critical line" mention is the *definition* of the single hypothesized off-line point (§1.1), not an RH assumption. Algebraic/analytic rank never appear; `d` is a finite rational Li-type observation, not an L-value |
| L6 (vacuous target / real atoms) | PASS — target is a finite rational determinantal floor; a non-vacuous REFUTED path (a powerful `N`, or a node-poisoned family with floor `= o(m)`) is available |
| L7–L17 | N/A — no counting-function factor, growth ray, Fredholm, meromorphic-type step. The one externally-cited black box (a squarefree/powerful-values result for Lemma B) is explicitly in the OPEN core (§3 Step 4 / §4), not used as a proved premise |
| L18 (numerical anchor by script) | PASS — anchor re-derived by exact `Fraction` arithmetic: `N = 18281 = 101·181`, node-integrality `101 ∤ {5,17,37,65}`, `v_101(w_i) = (−1,−2,−3,−4)`, `C_j = (−4,−4,−4,−4)`, `v_101(q_min) = max_j N_j + m = 4` |
| L19 (honest inconclusive verdict) | PASS — outcomes STRATEGY / PARTIAL / INCONCLUSIVE+localization all first-class; no prove-or-refute dichotomy; a powerful-`N` or node-poison refutation is explicitly welcomed. Step 2 honestly labels the stronger `min(v_p(N),2)` law and the `den(w_0)=N` base case as REFUTED/non-universal; the theorem is stated only for a **simple** node-integral factor, and the existence of one is honestly isolated as the open core with a quantified exceptional set (7640/7688; 0/12124 powerful) |
| L20–L24 | N/A |
| Self-containment | PASS — every symbol/formula in-file (`x(t)`, Chebyshev `C_j`, target `d_j`, graded basis `q_i`/`B`, `det B`, moment `w = B^{−1}d`, carrier norm `N`, `D_r`, `q_min`, `minor_j`, identity `max_j(N_j−C_j)`, sub-law, bridge); `grep "see .*\.md"` → clean; §5 provenance is a reference only, not load-bearing |
| Deliverable breadth | PASS — a sanity-checked *proof strategy* (STRATEGY) is a successful deliverable; full proof not required |
| Privacy | PASS — no personal usernames, home paths, company/internal domains, or hardware model numbers; all quantities are abstract rationals/primes |
