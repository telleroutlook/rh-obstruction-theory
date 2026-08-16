# Problem OB-43 — The p=2 arithmetic floor of q_min: an orbit-robust, hypothesis-free linear bound (OP1 direct route)

**Type:** arithmetic / 2-adic valuation theory / determinantal (lattice) geometry — a finite,
exact, RH-free question about rational vectors and 2-adic valuations.

**Non-circularity.** This problem does NOT assume the Riemann Hypothesis, does NOT use any
value, derivative, or zero location of ζ or any L-function, and does NOT read "analytic rank"
or any RH-equivalent input. The object is a finite integer/rational linear-algebra
configuration and its 2-adic valuations. The single "off-line" datum is one *hypothesized*
point `ρ = σ₀ + iτ₀` with `σ₀ ≠ 1/2` (the barrier asks whether a finite family of on-line
observations can cheaply register such a hypothesized point); nothing is assumed about the
truth or falsity of RH. All quantities below are exact rationals; all claims are checkable by
exact arithmetic. RH stays outside this problem.

This is the **p = 2 companion** to OB-42 (which proves the same barrier via the prime `p = 3`,
conditional on a *3-adic unimodularity* hypothesis on the orbit). The p = 2 route below is
**strictly stronger in two respects**: (a) its on-line valuation floor is *unconditional and
adversary-proof* — every pair of nodes contributes `≥ 3` to the 2-adic valuation, with no
clustering hypothesis; (b) the resulting `q_min` floor is *orbit-robust* — it survives even on
the orbits where the p = 3 floor collapses (§5). The referee is asked to **prove, propose a
feasible (sanity-checked) proof strategy for, refute, or precisely localize** the bound below. A
complete proof is NOT required for a successful deliverable: a concrete, plausible proof route
— with its key sub-steps identified and a lightweight check — is a first-class outcome (§4,
outcome **STRATEGY**).

---

## 1. All definitions (self-contained — every symbol and formula is here)

Fix the prime `p = 2` throughout. `v = v_2` is the 2-adic valuation on `ℚ`
(`v(0) = +∞`, `v(a/b) = v(a) − v(b)`). Fix an integer `m ≥ 2` (the observation dimension) and
rationals `σ, τ ∈ ℚ` describing a fixed off-line orbit (§1.3).

### 1.1 The node map and the on-line x-values
A **node** is a nonzero integer `t`. Its **x-value** is
```
    x(t) = (4 t² − 1) / (4 t² + 1)  ∈ ℚ.
```
`x(t)` depends only on `t²` (`x(t) = x(−t)`). A configuration is a tuple of `K ≥ m` integer
nodes `t_1, …, t_K` with pairwise-distinct x-values `x_k := x(t_k)`.

### 1.2 Chebyshev observation columns
For `j ≥ 0` let `T_j` be the Chebyshev polynomial of the first kind
(`T_0 = 1, T_1 = X, T_{j+1} = 2X·T_j − T_{j−1}`). The **observation column** of a node `t` is
```
    C(t) = ( C_1(t), …, C_m(t) ) ∈ ℚ^m,     C_j(t) = 4·( 1 − T_j(x(t)) ).
```
Since `T_j(1) = 1`, each `C_j` vanishes at `x = 1`, so `C_j(t) = (x(t) − 1)·(4 q_j(x(t)))` for
the polynomial `q_j` of §1.4.

### 1.3 The off-line target vector `d`
Given `ρ = σ₀ + i τ₀` off the critical line, its orbit is `{σ₀ ± iτ₀, 1−σ₀ ± iτ₀}` (4 atoms).
The **target vector** `d = (d_1, …, d_m) ∈ ℚ^m` is
```
    d_j = Σ_{atoms (r,ι)} Σ_{(r',ι') ∈ {(r,ι),(1−r,ι)}}  Re[ 1 − (1 − 1/(r'+iι'))^j ].
```
Each `Re[1 − (1 − 1/ρ')^j]` is an exact rational, so `d ∈ ℚ^m`. This is the finite Li-type
observation of the orbit — the vector a finite observer must "hit" to register a collision.

### 1.4 The graded basis and the matrix `B`
Define `q_i(x) = (1 − T_i(x))/(x − 1)` for `i = 1, …, m` (degree `i − 1`; division exact since
`T_i(1) = 1`). Write `4 q_i(x) = Σ_{l=0}^{i−1} B[i][l]·x^l`. Then `B` is `m × m`
**lower-triangular** with diagonal `B[i][i−1] = 4·(−2^{i−1})`, so
```
    v(det B) = Σ_{i=1}^m v( 4·2^{i−1} ) = Σ_{i=1}^m (i + 1) = m(m+3)/2.
```
(Unlike at `p = 3`, `det B` is deeply 2-adic — this is used below, not avoided.)

### 1.5 The collision constraint and the barrier quantity `q_min`
Let `A` be the `m × K` integer matrix whose columns are the cleared (common-denominator-
multiplied) integer forms of `C(t_1), …, C(t_K)`, and let `v_off` be the cleared integer form
of `d`. For an integer matrix `X` and integer `r`, let `D_r(X)` be the **r-th determinantal
divisor** = gcd of all `r × r` minors of `X` (`= 0` iff `rank X < r`). A **valid collision** is
a configuration with
```
    (C1)  v_off ∈ ℚ-span of the columns of A     (a finite integer relation exists), and
    (C2)  D_m(A) ≠ 0                              (⇔ rank A = m ⇔ K ≥ m on-line columns).
```
When valid, the minimal positive multiplier is the finite **collision size**
```
    q_min = D_m(A) / D_m([A | v_off])   (a positive integer).
```
The barrier **OP1** asks whether `inf_A q_min(m)` grows super-polynomially: OP1 holds iff
`log q_min = ω(log m)` uniformly over valid collisions. Since `q_min ≥ 2^{v(q_min)}`, a lower
bound `v(q_min) ≥ c·m − O(1)` gives `log q_min ≥ (c·m − O(1))·log 2 = Ω(m) ≫ ω(log m)` and
closes OP1. **This problem is the 2-adic floor `v(q_min) ≥ c·m − O(1)`.**

### 1.6 The determinantal divisor as a minor min
Take `K = m` (the general `K ≥ m` case reduces to the worst `m`-subset). The `m × (m+1)` matrix
`[A | v_off]` has exactly `m + 1` size-`m` minors: `det A` (delete the `d`-column) and, for each
online column `j`, the **`d`-replacement minor**
```
    minor_j := det( A with column j replaced by v_off ).
```
Hence `D_m([A|v_off]) = gcd( det A, minor_1, …, minor_m )` and
```
    v(q_min) = v(det A) − v( gcd(det A, minor_1, …, minor_m) )
             = v(det A) − min( v(det A), min_j v(minor_j) )
             = max( 0, v(det A) − min_j v(minor_j) ).
```
So the floor is `v(det A) − min_j v(minor_j)` whenever some minor is 2-adically shallower than
`det A` — the analog of the p=3 `max_j (N_j − C_j)`, here framed directly on the minors.

---

## 2. The theorem to be verified

> **Theorem (OP1 p=2 floor — orbit-robust linear valuation bound).**
> Let `p = 2`. There is an absolute constant `c > 0` such that for every `m ≥ 2`, **every**
> off-line orbit `(σ, τ)` (no unimodularity or other hypothesis), and every valid collision
> (§1.5) — equivalently every integer-node configuration with pairwise-distinct x-values —
> ```
>     v(q_min)  =  max_{1 ≤ j ≤ m} ( 1 + N_j − C_j )  ≥  c·m − O(1),
>     N_j = Σ_{k≠j} v(x_j − x_k),   C_j = v(⟨w, ε(X'_j)⟩),   w = B^{−1}d,
> ```
> uniformly in `m`, the (adversarially chosen) node set, and the orbit. Empirically `c ≈ 2`–`3`;
> any absolute `c > 0` closes OP1's 2-adic channel.

The **exact identity** `v(q_min) = max_j (1 + N_j − C_j)` is a **proved premise** (§3 Step 3,
verified orbit-free on 240 configs). Two facts make it powerful and orbit-free:
- **`N_j ≥ 3(m−1)` for every column, unconditional** (§3 Step 2: each `v(x_j − x_k) ≥ 3`, no
  clustering hypothesis) — so `v(q_min) ≥ 1 + 3(m−1) − min_j C_j`;
- `C_j = v(⟨w, ε(X'_j)⟩)` is the 2-adic valuation of the *fixed* off-line vector `w = B^{−1}d`
  paired against the leave-one-out symmetric vectors `ε(X'_j)` (§1.6, §3).

Hence the **entire open core** is the single bilinear bound **CORE-2** (§3 Step 4):
`min_j C_j ≤ (3 − c)·m + O(1)`. This is strictly weaker to demand than OB-42's joint p=3 bound
and requires **no orbit hypothesis**.

**Why the numerator alone is not enough.** By §3 Step 2, `v(det A) ≥ 2m² + m` — quadratic and
unconditional — but the gcd of the minors cancels the quadratic bulk. The residue is exactly
`max_j(1 + N_j − C_j)`, and the content is the *off-line* competition `min_j C_j`, not the (large,
easy) depth of `det A`.

---

## 3. Proof skeleton to be closed

Steps 1–3 are **proved** here (inlined as premises; the referee may use them freely). Step 4 is
the open core.

### Step 1 — The floor identity. **[proved, premise]**
Immediate from §1.6: `[A | v_off]` is `m × (m+1)`, its size-`m` minors are `det A` and the `m`
`d`-replacement minors, `D_m([A|v_off])` is their gcd, and `v` of a gcd is the min of the `v`'s.
Hence `v(q_min) = v(det A) − min_j v(minor_j)` (when positive). *(Verified exact, m = 3..7.)*

### Step 2 — The on-line side: an EXACT, UNCONDITIONAL formula for `v(det A)`. **[proved, premise]**
Two elementary 2-adic facts, for **all** integer nodes:
```
    (a)  x(t) − 1 = −2 / (4t² + 1)                        ⇒  v(x(t) − 1) = 1   (4t²+1 is odd).
    (b)  x(t_j) − x(t_k) = 8 (t_j² − t_k²) / ((4t_j²+1)(4t_k²+1))
                                                          ⇒  v(x_j − x_k) = 3 + v(t_j² − t_k²) ≥ 3.
```
From `C_j(t) = (x(t)−1)·4 q_j(x(t))` and the graded basis (§1.4), the matrix `A` factors as
`A = diag(x_k − 1) `-scaled `× B ×` (Vandermonde in the `x_k`), giving the **exact** identity
```
    v(det A) = Σ_{k} v(x_k − 1) + v(det B) + Σ_{k<l} v(x_k − x_l)
             = m + m(m+3)/2 + Σ_{k<l} v(x_k − x_l)
             ≥ m + m(m+3)/2 + 3·C(m,2) = 2m² + m.
```
*(Verified exact on all sampled configs, m = 3..6; e.g. `v(det B) = 27` at `m = 6`.)* **Key
contrast with p=3:** every pair contributes `≥ 3` *unconditionally* — no residue-clustering
pigeonhole, so the adversary cannot lower the per-pair floor. This is why the p=2 route needs no
orbit hypothesis.

### Step 3 — The EXACT floor identity (Step 3 upgraded from measured to proved). **[proved, premise]**
Factor `A = B · V · diag(x_k − 1)` where `V` is the Vandermonde `V_{lk} = x_k^l` (from
`C_i(t) = (x−1)·4q_i(x)` and `4q_i(x) = Σ_l B[i][l]x^l`), and write `d = B·w`, `w = B^{−1}d`
(node-independent). Then `minor_j = B · (V·diag(x−1) with column j replaced by w)`, and expanding
the replaced-Vandermonde determinant gives, **exactly**,
```
    v(det A) − v(minor_j) = v(x_j − 1) + Σ_{k≠j} v(x_j − x_k) − v(⟨w, ε(X'_j)⟩)
                          = 1 + N_j − C_j,
```
with `N_j := Σ_{k≠j} v(x_j − x_k)`, `C_j := v(⟨w, ε(X'_j)⟩)`, and `ε(X'_j)_i = (−1)^{m−1−i}
e_{m−1−i}(X'_j)` the signed elementary-symmetric vector of the other `m−1` x-values (`e` = elementary
symmetric). Combining with Step 1,
```
    v(q_min) = max_{1 ≤ j ≤ m} ( 1 + N_j − C_j ).
```
*(Verified EXACT on 240 valid configs across three orbits `σ = 3/4, 7/8, 4/5`, `m = 3..7` — the identity
is orbit-free.)* By Step 2, `N_j ≥ 3(m−1)` for **every** `j` (unconditional), so
```
    v(q_min) ≥ 1 + 3(m−1) − min_j C_j.        (★)
```

### Step 4 — The single leave-one-out bilinear bound (**the hard core, CORE-2**). **[open]**
By (★) the entire remaining problem is a **single** statement about the fixed off-line vector
`w = B^{−1}d` paired against the leave-one-out symmetric vectors:
> **Sub-claim (CORE-2).** There is an absolute `c > 0` such that for every `m`, every orbit, and
> every node configuration, `min_{1 ≤ j ≤ m} C_j = min_j v(⟨w, ε(X'_j)⟩) ≤ (3 − c)·m + O(1)`;
> i.e. at least one leave-one-out pairing is not too 2-adically deep. Then by (★),
> `v(q_min) ≥ c·m − O(1)`.

**Empirical calibration (honest — do not take as proved).** `min_j C_j` is **not** bounded — it grows
— but only with slope `≈ 1`, far below `N`'s slope `3`. Two independent adversaries converge on the
sharp value `min_j C_j ≈ m + 3`: (a) an adversary maximizing `min_j C_j` reaches `7,8,9,10`
(`m = 4..7`); (b) the floor-minimizing adversary drives **all** `C_j` equal to `7,8,9,10,11`
(`m = 4..8`), giving floor `6,11,14,18,21`. This suggests the sharp form `min_j C_j ≤ m + O(1)`,
whence `v(q_min) ≥ 2m − O(1)`; any `c > 0` suffices to close OP1.

**Structural handles available.**
- **(H-uniform-N) The uniform on-line base.** Unlike p=3, `N_j ≥ 3(m−1)` holds for *every* column,
  not just on average — so the reduction (★) needs no pigeonhole and no orbit hypothesis. The only
  task is to upper-bound the off-line `min_j C_j`.
- **(H-equalize) The extremal configuration equalizes `C_j`.** At the floor-minimizing optimum the
  `m` values `C_j` are all equal (observed). A bound on this common value — or on `avg_j C_j =
  (1/m)Σ_j C_j` (note `max_j(N_j − C_j) ≥ 3(m−1) − avg_j C_j` by averaging, an alternative to (★)) —
  suffices.
- **(H-bilinear) Newton-polygon / valuation of a fixed pairing.** `C_j = v(⟨w, ε(X'_j)⟩)` is the
  2-adic valuation of one bilinear form of the *fixed* `w` against the leave-one-out symmetric
  vectors of a single node set. The `m` vectors `ε(X'_1), …, ε(X'_m)` are not independent (they are
  the leave-one-out symmetric vectors of one degree-`m` node set, coupled by Newton's identities), so
  they cannot all be aligned to make `⟨w, ε(X'_j)⟩` deep simultaneously. Converting this coupling into
  `min_j C_j ≤ (3−c)m` is the crux.

**What to close for Step 4.** Prove CORE-2 (any absolute `c > 0`). By (★) this gives a linear 2-adic
floor for *every* orbit and closes OP1's 2-adic channel.

**Known dead-ends (inherited from the p=3 analysis — do not re-derive).** The column-wise
simplifications refuted for OB-42 (`max_j`-type bounds `= O(1)`, averaging `Σ = O(m)`, an
argmax column with bounded correction, a single shallow-correction high-depth column) and the
**adjugate no-cancellation reduction** (`min_j pred_j` with `pred_j = min_k[v(v_off_k) +
v(cofactor_{jk})]`; a loose upper bound with unbounded gap at `m = 8`) all fail there and are
expected to fail here for the same reason: the floor is a *joint* competition across columns, not
a single-column magnitude count.

---

## 4. Acceptance criteria

Report exactly one of the following, with the stated evidence. An honest partial/localized
outcome is a first-class result — do **not** force a prove/refute dichotomy.

1. **CONFIRMED.** A proof of the Theorem (§2) / Sub-claim (Step 4), for some absolute
   `m`-independent `c > 0`. State every hypothesis used; confirm none is RH, an L-value, a zero
   location, or an RH-equivalent (non-circularity). If the proof needs any orbit hypothesis,
   state it precisely — but note the empirical claim is that *none* is required (§5).

2. **STRATEGY (feasible proof route — a full proof is NOT required).** A concrete, plausible
   plan. To qualify it must: (a) name the main tool/theorem it would invoke (e.g. a
   Newton-polygon / Weierstrass-preparation bound on `⟨w, ε(X'_j)⟩` at `p = 2`, a
   resultant/discriminant valuation estimate, a Plücker-relation coupling of the `minor_j`, a
   2-adic rigidity result on the leave-one-out symmetric vectors, …) and why it applies; (b)
   break Step 4 into sub-lemmas and say which are standard vs genuinely new; (c) include a
   **lightweight check** that the route is not hopeless — e.g. verify the key sub-lemma on the §6
   anchor and one larger `m`. Identify the one step most likely to fail.

3. **PARTIAL.** A proof of a weaker-but-still-superpolynomial floor `v(q_min) ≥ f(m)` with the
   best `f` you can certify (e.g. `f(m) = c·√m`, `c·m/log m`, or a linear floor under an extra
   hypothesis), or a proof of one of the structural handles (H-minor)/(H-orbit-free) as a
   standalone lemma. Note: any `f(m) = ω(log m)` already closes OP1; a linear floor is the
   observed sharp form. Specify precisely what is proved and what remains.

4. **REFUTED.** An explicit family (fix an orbit `(σ,τ)`; give, for each `m` in an unbounded set,
   the `K ≥ m` integer nodes `t_k`, verified valid by exact arithmetic) with
   `v(det A) − min_j v(minor_j) = o(m)` — or bounded, or `O(log m)` — as `m → ∞`. This shows the
   2-adic floor is not linear (indeed sub-`ω(log m)` would threaten OP1's 2-adic channel) and the
   barrier needs a narrower profile — a legitimate, valuable outcome. (A single small-`m`
   configuration with a small floor is NOT a refutation; the claim is asymptotic with an `O(1)`
   slack.)

5. **INCONCLUSIVE + precise localization.** Identify the exact step that resists (e.g. "the
   `d`-column depth (H-minor) can be driven to within `o(m)` of `v(det A)` because …") and state
   the minimal additional input that would close it.

---

## 5. Provenance and the orbit-robustness evidence (for verification only)

The floor identity (Step 1), the exact `v(det A)` formula and per-pair bound (Step 2), and the
linear residual (Step 3) were verified by exact-arithmetic scripts in this repository's discovery
tier (untrusted, never imported into proofs): `probe_qmin_channel_split.py` and its inline
follow-ups. The per-pair identity `v(x_j − x_k) = 3 + v(t_j² − t_k²) ≥ 3` was checked on 500
random pairs; the `v(det A)` factorization on all sampled configs, `m = 3..6`.

**Orbit robustness is the key advantage over OB-42 and was isolated empirically.**
Adversarial-min floor (random-restart coordinate descent = a one-sided UPPER bound on the true
min), at `p = 2`, `m = 4,5,6,7`:

| orbit (σ, τ) | p=3 floor (OB-42) | **p=2 floor (this problem)** |
|---|---|---|
| σ=3/4, τ=1  (`D = 425`, 3-unimodular) | 2, 2, 4, 5 (holds) | **6, 11, 14, 18** |
| σ=7/8, τ=1  (NOT 3-unimodular) | 0, 0, 0, 1 (**collapses**) | **4, 9, 12, 16** |
| σ=4/5, τ=1  (NOT 3-unimodular) | 0, 0, 0, 1 (**collapses**) | **18, 26, 28, 38** |

So the p=2 floor stays linear (`≥ m`) precisely where the p=3 floor dies — it is a property of
*every* orbit, not a unimodular class. These scripts are reproducible; the referee need not
consult them (all premises are stated inline).

---

## 6. Numerical anchor (sanity only, not an input to the proof)

Exact, independently re-derivable by a few lines of rational arithmetic.

**Orbit** `ρ = 3/4 + i` (`σ₀ = 3/4, τ₀ = 1`; the split-prime orbit `D = 425 = 5²·17`).
**Configuration** `m = 4`, nodes `t = (9, 37, 5, 17)`, giving x-values
```
    x = ( 323/325,  5475/5477,  99/101,  1155/1157 ).
```
Per-pair 2-adic check (Step 2b), e.g. `v(x(9) − x(37)) = 3 + v(9² − 37²) = 3 + v(−1288)`,
`1288 = 2³·7·23` so `= 3 + 3 = 6 ≥ 3`. ✓ And `v(x(t) − 1) = 1` for each node. ✓ Then:
```
    v(det B) = m(m+3)/2 = 14.
    N_j = ( 19, 21, 21, 19 )   (each ≥ 3(m−1) = 9).
    C_j = ( 7, 7, 7, 7 )        (here all equal — the equalization of handle (H-equalize)).
    v(q_min) = max_j ( 1 + N_j − C_j ) = max(13, 15, 15, 13) = 15   (= direct v_2(q_min)).  ✓
    reduction (★):  v(q_min) ≥ 1 + 3(m−1) − min_j C_j = 1 + 9 − 7 = 3   (loose here; the bound is
                    asymptotic — the point is min_j C_j = 7 = m + 3 stays linear, not ~3m).
```
A referee should confirm (a) `v(x(t) − 1) = 1` for each node; (b) `v(x_j − x_k) = 3 + v(t_j² −
t_k²) ≥ 3` for the six pairs; (c) `v(det B) = 14`; (d) `N_j = (19,21,21,19)`, `C_j = (7,7,7,7)`;
(e) the identity `v(q_min) = max_j(1 + N_j − C_j) = 15`. **Sanity only — not an input.**

---

## Pre-send lint notes (PROMPT_LINT.md self-check)

| Item | Status |
|---|---|
| L1–L4 | N/A — no entire-function / order / canonical-product claims |
| L5 (RH via divisor / circular target) | PASS — no ζ/L zeros, no real-zero product; the only "off the critical line" mention is the *definition* of the single hypothesized off-line point (§1.3), not an RH assumption. Algebraic/analytic rank never appear; `d` is a finite rational Li-type observation, not an L-value |
| L6 (vacuous target / real atoms) | PASS — target is a finite rational determinantal floor; a non-vacuous REFUTED path (explicit orbit family with floor `= o(m)`) is available |
| L7–L17 | N/A — no counting-function factor, growth ray, Fredholm, meromorphic-type, or externally-cited black-box steps (all premises proved/measured in-repo, stated inline) |
| L18 (numerical anchor by script) | PASS — anchor re-derived by exact `Fraction` arithmetic: per-pair `v = 3 + v(t²−t'²)`, `v(x−1)=1`, `v(det B)=14`, `N_j=(19,21,21,19)`, `C_j=(7,7,7,7)`, identity `v(q_min)=max_j(1+N_j−C_j)=15` |
| L19 (honest inconclusive verdict) | PASS — outcomes STRATEGY / PARTIAL / INCONCLUSIVE+localization all first-class; no prove-or-refute dichotomy; a sub-`ω(log m)` refutation is explicitly welcomed. §3 Step 4 honestly labels the `min_j C_j = O(1)` hope as REFUTED (it grows, slope ≈ 1); CORE-2 is stated as the open target with adversary calibration marked not-a-proof |
| L20–L24 | N/A |
| Self-containment | PASS — every symbol/formula in-file (`x(t)`, Chebyshev `C_j`, target `d_j`, graded basis `q_i`/`B`, `v(det B)`, `D_r`, `q_min`, `minor_j`, per-pair `v_2` identities, `v(det A)` formula); `grep "see .*\.md"` → clean; §5 provenance is a reference only, not load-bearing |
| Deliverable breadth | PASS — a sanity-checked *proof strategy* (STRATEGY) is a successful deliverable; full proof not required |
| Privacy | PASS — no personal usernames, home paths, company/internal domains, or hardware model numbers; all quantities are abstract rationals/primes |
