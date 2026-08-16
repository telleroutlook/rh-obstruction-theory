# Problem OB-42 — The p=3 arithmetic floor of q_min: an irreducible joint valuation bound (OP1 direct route)

**Type:** arithmetic / p-adic valuation theory / determinantal (lattice) geometry — a finite,
exact, RH-free question about rational vectors and 3-adic valuations.

**Non-circularity.** This problem does NOT assume the Riemann Hypothesis, does NOT use any
value, derivative, or zero location of ζ or any L-function, and does NOT read "analytic rank"
or any RH-equivalent input. The object is a finite integer/rational linear-algebra
configuration and its 3-adic valuations. The single "off-line" datum is one *hypothesized*
point `ρ = σ₀ + iτ₀` with `σ₀ ≠ 1/2` (the barrier asks whether a finite family of on-line
observations can cheaply register such a hypothesized point); nothing is assumed about the
truth or falsity of RH. All quantities below are exact rationals; all claims are checkable by
exact arithmetic. RH stays outside this problem.

This is the direct route to the barrier program **OP1**, replacing the retired "incidence-lag"
leg (OB-41, REFUTED 2026-08-16 — the lag was a mis-formulated intermediate; the real target is
the size of `q_min` itself). The referee is asked to **prove, propose a feasible
(sanity-checked) proof strategy for, refute, or precisely localize** the bound below. A
complete proof is NOT required for a successful deliverable: a concrete, plausible proof route
— with its key sub-steps identified and a lightweight check — is a first-class outcome (§4,
outcome **STRATEGY**).

---

## 1. All definitions (self-contained — every symbol and formula is here)

Fix the prime `p = 3` throughout. `v = v_3` is the 3-adic valuation on `ℚ`
(`v(0) = +∞`, `v(a/b) = v(a) − v(b)`). Fix an integer `m ≥ 2` (the observation dimension) and
rationals `σ, τ ∈ ℚ` describing a fixed off-line orbit (§1.3–1.4).

### 1.1 The node map and the on-line x-values
A **node** is a nonzero rational `t`. Its **x-value** is
```
    x(t) = (4 t² − 1) / (4 t² + 1)  ∈ ℚ.
```
`x(t)` depends only on `t²` (`x(t) = x(−t)`). A configuration is a tuple of `K ≥ m` nodes
`t_1, …, t_K` with pairwise-distinct x-values `x_k := x(t_k)`.

### 1.2 Chebyshev observation columns
For `j ≥ 0` let `T_j` be the Chebyshev polynomial of the first kind
(`T_0 = 1, T_1 = X, T_{j+1} = 2X·T_j − T_{j−1}`). The **observation column** of a node `t` is
```
    C(t) = ( C_1(t), …, C_m(t) ) ∈ ℚ^m,     C_j(t) = 4·( 1 − T_j(x(t)) ).
```
Since `T_j(1) = 1`, each `C_j` vanishes at `x = 1`, so `C_j(t) = (x(t) − 1)·(4 q_j(x(t)))` for
the polynomial `q_j` of §1.5.

### 1.3 The off-line target vector `d`
Given `ρ = σ₀ + i τ₀` off the critical line, its orbit is `{σ₀ ± iτ₀, 1−σ₀ ± iτ₀}` (4 atoms).
The **target vector** `d = (d_1, …, d_m) ∈ ℚ^m` is
```
    d_j = Σ_{atoms (r,ι)} Σ_{(r',ι') ∈ {(r,ι),(1−r,ι)}}  Re[ 1 − (1 − 1/(r'+iι'))^j ].
```
Each `Re[1 − (1 − 1/ρ')^j]` is an exact rational, so `d ∈ ℚ^m`. This is the finite Li-type
observation of the orbit — the vector a finite observer must "hit" to register a collision.

### 1.4 The collision constraint and the barrier quantity `q_min`
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
`log q_min = ω(log m)` uniformly over valid collisions. Since `q_min ≥ 3^{v(q_min)}`, a lower
bound `v(q_min) ≥ m/2 − O(1)` gives `log q_min ≥ (m/2 − O(1))·log 3 = Ω(m) ≫ ω(log m)` and
closes OP1. **This problem is the 3-adic floor `v(q_min) ≥ m/2 − O(1)`.**

### 1.5 The graded basis, the matrix `B`, and the fixed off-line vector `w`
Define the polynomials `q_i(x) = (1 − T_i(x))/(x − 1)` for `i = 1, …, m` (a polynomial of
degree `i − 1`; the division is exact since `T_i(1) = 1`). Write
```
    4 q_i(x) = Σ_{l=0}^{i−1} B[i][l] · x^l.
```
Then `B = (B[i][l])_{1 ≤ i ≤ m, 0 ≤ l ≤ m−1}` is `m × m` **lower-triangular** with diagonal
`B[i][i−1] = 4·(−2^{i−1})`, all 3-adic units, so `v(det B) = 0`. Define the **fixed off-line
vector**
```
    w = B^{−1} d  ∈ ℚ^m
```
(node-INDEPENDENT; it depends only on the orbit through `d`). Index `w = (w_0, …, w_{m−1})`.

### 1.6 The two per-column valuations `N_j` and `C_j`
For a configuration with x-values `x_1, …, x_m` (take `K = m`; the general `K ≥ m` case reduces
to the worst `m`-subset — see §3) and each column index `j`, let `X'_j = {x_k : k ≠ j}` (the
`m − 1` other x-values) and define
```
    N_j = Σ_{k ≠ j} v(x_j − x_k)                                  (the ON-LINE valuation; orbit-free),
    C_j = v( S_j ),   S_j = Σ_{i=0}^{m−1} (−1)^{m−1−i} · e_{m−1−i}(X'_j) · w_i    (the OFF-LINE pairing),
```
where `e_l(X'_j)` is the `l`-th elementary symmetric polynomial of the `m − 1` values in `X'_j`
(`e_0 = 1`). So `C_j` is the 3-adic valuation of a **bilinear pairing** of the fixed off-line
vector `w` against the elementary symmetric functions of the on-line nodes.

### 1.7 3-adic unimodularity of the orbit
The orbit `(σ, τ)` is **3-adically unimodular** if every coordinate of `w = B^{−1} d` is a
3-adic unit: `v(w_i) = 0` for all `i = 0, …, m−1`. (Checkable in finitely many exact rational
operations for each `m`.) This is the hypothesis under which the floor below holds — see §2 and
the multi-orbit evidence in §5.

---

## 2. The theorem to be verified

> **Theorem (OP1 p=3 floor — irreducible joint valuation bound).**
> Let `p = 3`. There is an absolute constant `c` such that for every `m ≥ 2`, every
> **3-adically unimodular** off-line orbit `(σ, τ)` (§1.7), and every valid collision (§1.4)
> — equivalently, every node configuration with pairwise-distinct x-values —
> ```
>     v(q_min)  =  max_{1 ≤ j ≤ m} ( N_j − C_j )  ≥  m/2 − c,
> ```
> uniformly in `m` and in the (adversarially chosen) node set.

The equality `v(q_min) = max_j (N_j − C_j)` is a **proved premise** (§3, Step 1); the open core
is the lower bound `max_j (N_j − C_j) ≥ m/2 − c`. The constant need not be sharp — any
`m`-independent `c` with a linear-in-`m` floor closes OP1's 3-adic channel.

**Why this is genuinely hard (the bound is IRREDUCIBLE).** The bound is NOT equivalent to, and
does NOT follow from, any of the following simpler statements — each has been checked and
**refuted** by exact computation (§5):
- `max_j C_j = O(1)` — **FALSE**: the adversary can 3-adically align nodes so a single `C_j`
  grows without bound (`C_j ↑ 30+` for m as small as 4–6).
- `Σ_j C_j = O(m)` (an averaging bound) — **FALSE**: `Σ_j C_j` grows super-linearly.
- "the argmax-`N` column has `C_j = O(1)`" — **FALSE**: the adversary can inflate `C` exactly
  at the high-`N` column; the floor then *moves* to a different column.
- "∃ a column with `N_j ≥ m/2 − O(1)` AND `C_j ≤ 1`" — **FALSE**: no single low-`C` high-`N`
  column need survive.
The `O(1)` slack is essential: the floor is carried by a column that trades `N` against a
**bounded** (not zero) `C`, and which column carries it depends on the node set. The genuine
content is the *joint* competition between the pairwise-difference valuations `N_j` (forced
large by 3-adic pigeonhole, §3 Step 2) and the fixed-vector pairing valuations `C_j`, which no
single-column argument defeats.

---

## 3. Proof skeleton to be closed

Steps 1–3 are **proved** here (inlined as premises; the referee may use them freely). Step 4 is
the open core.

### Step 1 — The floor identity `v(q_min) = max_j (N_j − C_j)`. **[proved, premise]**
From the factorization `C_j(t) = (x(t) − 1)·4 q_j(x(t))` and the change of basis `[node-cols |
d] = B·[monomials | w]` (`w = B^{−1} d`), the `d`-residual `m`-minor factors, at `p = 3` (where
`v(x_k − 1) = 0` and `v(det B) = 0`), as
```
    v(minor_j) = Σ_{k<l, k,l ≠ j} v(x_k − x_l) + C_j,     v(det A_□) = Σ_{k<l} v(x_k − x_l),
```
so `v(q_min) = v(det A_□) − min_j v(minor_j) = max_j ( N_j − C_j )` with `N_j`, `C_j` as in
§1.6. *(Verified exact: the bilinear `C_j` of §1.6 equals the integer-minor `C_j` on every
sampled valid configuration, m = 3..7.)*

### Step 2 — The on-line side: `max_j N_j ≥ m/2 − O(1)`. **[proved, premise]**
At `p = 3` there is exactly one nonzero x-residue class mod 3 (plus the `x = 1` class), so `m`
distinct x-values are forced into `≤ 2` residue classes, and a pigeonhole/Newton-polygon count
gives
```
    v(det A_□) = Σ_{k<l} v(x_k − x_l)  ≥  PIG(m) := C(⌈m/2⌉, 2) + C(⌊m/2⌋, 2) = m²/4 − O(m).
```
Since `Σ_j N_j = 2·v(det A_□) ≥ 2·PIG(m)`, averaging gives `max_j N_j ≥ (2/m)·PIG(m) = m/2 −
O(1)`. *(Verified exact.)* **The difficulty is entirely the `− C_j` subtraction:** the column
achieving `max_j N_j` may have large `C_j` (Step 2 alone does NOT give the theorem).

### Step 3 — The bilinear reduction of `C_j`. **[proved, premise]**
`C_j = v( ⟨w, ε(X'_j)⟩ )` where `ε(X'_j) = ( (−1)^{m−1−i} e_{m−1−i}(X'_j) )_{i=0..m−1}` is the
signed elementary-symmetric vector of the `m − 1` other x-values, and `w = B^{−1} d` is fixed.
Under 3-adic unimodularity every `w_i` is a unit, so `C_j = 0` unless the node set is specially
3-adically aligned. *(Verified exact; and the alignment CAN force `C_j` large — this is exactly
why the theorem is not trivial.)*

### Step 4 — The joint lower bound (**the hard core**). **[open]**
> **Sub-claim (Step 4 core).** For `p = 3` and a 3-adically unimodular orbit, no node
> configuration can drive `N_j − C_j < m/2 − c` for *every* column `j` simultaneously; i.e.
> `max_j (N_j − C_j) ≥ m/2 − c`, uniformly in `m` and the node set.

**Structural handles available.**
- **(H-anchor) The unit anchor (why unimodularity matters).** The `e_0 = 1` term of `S_j` is
  `(−1)^{m−1} w_{m−1}`, a 3-adic **unit** under §1.7. So `C_j > 0` requires the *higher*
  symmetric terms `e_{m−1−i}(X'_j) w_i` (`i < m−1`) to 3-adically cancel the unit anchor — a
  codimension condition on the node set that a single column can meet but (empirically) not all
  columns at once. When the anchor coordinate `w_{m−1}` is NOT a unit the floor collapses to ~0
  (see §5: orbits `σ = 7/8, 4/5`), which is why unimodularity is the correct hypothesis.
- **(H-count) The mod-3 pigeonhole (Step 2).** The same clustering that forces `N_j` large
  (few residue classes) constrains the `e_l(X'_j)` mod 3, coupling the `C_j` across columns:
  the vectors `ε(X'_j)`, `j = 1..m`, are the `m` "leave-one-out" symmetric vectors of one node
  set and cannot be independently aligned to `w`. The open task is to convert this coupling
  into "not all `N_j − C_j` can be small at once."
- **(H-det) Shared-determinant coupling.** The `minor_j` are the `d`-residual `m`-minors of one
  rank-`m` matrix; they satisfy Plücker/Sylvester relations, so the `C_j` are not free
  parameters. A resultant/Newton-polygon bound on how deeply `⟨w, ε(X'_j)⟩` can vanish for
  `w` fixed and `X'_j` ranging over leave-one-out subsets of a single 3-adically-clustered node
  set would suffice.

**What to close for Step 4.** Prove the Sub-claim (any absolute `c`, linear floor). A proof
closes OP1's 3-adic channel and hence (with the p=3 construction) the barrier.

---

## 4. Acceptance criteria

Report exactly one of the following, with the stated evidence. An honest partial/localized
outcome is a first-class result — do **not** force a prove/refute dichotomy.

1. **CONFIRMED.** A proof of the Theorem (§2) / Sub-claim (Step 4), for some absolute
   `m`-independent `c`. State every hypothesis used; confirm none is RH, an L-value, a zero
   location, or an RH-equivalent (non-circularity). If the proof needs a hypothesis strictly
   stronger than 3-adic unimodularity (§1.7), state it precisely — that still closes OP1 for the
   orbit class satisfying it.

2. **STRATEGY (feasible proof route — a full proof is NOT required).** A concrete, plausible
   plan. To qualify it must: (a) name the main tool/theorem it would invoke (e.g. a
   Newton-polygon bound on `⟨w, ε(X'_j)⟩`, a resultant/discriminant valuation estimate, a
   Plücker-relation coupling of the `minor_j`, a p-adic equidistribution/rigidity result on the
   leave-one-out symmetric vectors, …) and why it applies; (b) break Step 4 into sub-lemmas and
   say which are standard vs genuinely new; (c) include a **lightweight check** that the route is
   not hopeless — e.g. verify the key sub-lemma on the §6 anchor and one larger `m`. Identify the
   one step most likely to fail.

3. **PARTIAL.** A proof of a weaker-but-still-superpolynomial floor `v(q_min) ≥ f(m)` with the
   best `f` you can certify (e.g. `f(m) = c·√m`, `c·m/log m`, or a linear floor under an extra
   residue-pattern hypothesis), or a proof of one of the structural handles (H-count)/(H-det)/
   (H-anchor) as a standalone lemma. Note: any `f(m) = ω(log m)` already closes OP1; a linear
   floor is the observed sharp form. Specify precisely what is proved and what remains.

4. **REFUTED.** An explicit family (fix a 3-adically unimodular orbit `(σ,τ)`; give, for each
   `m` in an unbounded set, the `K ≥ m` nodes `t_k`, verified valid by exact arithmetic) with
   `max_j (N_j − C_j) = o(m)` — or bounded, or `O(log m)` — as `m → ∞`. This shows the 3-adic
   floor is not linear (indeed sub-`ω(log m)` would threaten OP1's 3-adic channel) and the
   barrier needs a narrower profile — a legitimate, valuable outcome. (A single small-`m`
   configuration with a small floor is NOT a refutation; the claim is asymptotic with an `O(1)`
   slack. Non-unimodular orbits are excluded by hypothesis and are not refutations — see §5.)

5. **INCONCLUSIVE + precise localization.** Identify the exact step that resists (e.g. "the
   leave-one-out coupling (H-count) does not by itself bound the joint min because …") and state
   the minimal additional input that would close it.

---

## 5. Provenance and the unimodularity hypothesis (for verification only)

The floor identity (Step 1), the pigeonhole bound (Step 2), and the bilinear reduction (Step 3)
were verified by exact-arithmetic scripts in this repository's discovery tier (untrusted, never
imported into proofs): `probe_qmin_p3_floor_fast.py`, `probe_qmin_Cj_bilinear.py`,
`probe_qmin_floor_survival.py`. The irreducibility (the four refuted simpler forms in §2) is
from `probe_qmin_Cj_lift_attack.py`, `probe_qmin_floor_mechanism.py`,
`probe_qmin_floor_carrier.py`, `probe_qmin_floor_pigeonhole.py`.

**The unimodularity hypothesis is load-bearing and was isolated empirically**
(`probe_qmin_multiorbit.py`). Adversarial-min floor (random-restart coordinate descent = a
one-sided UPPER bound on the true min), at `p = 3`, `m = 4,5,6,7`:

| orbit (σ, τ) | `w = B⁻¹d` all 3-units? | min-floor (m=4,5,6,7) | vs `m/2 − 2` |
|---|---|---|---|
| σ=3/4, τ=1  (`D = 425`) | **yes** | 2, 2, 4, 5 | holds |
| σ=3/4, τ=2 | **yes** | 2, 2, 4, 5 | holds |
| σ=5/8, τ=1 | **yes** | 2, 2, 4, 5 | holds (2nd independent orbit) |
| σ=7/8, τ=1 | no | 0, 0, 0, 1 | **fails** |
| σ=4/5, τ=1 | no | 0, 0, 0, 1 | **fails** |

So the floor is a property of the **unimodular orbit class** (≥ 2 independent confirming
orbits), not of every orbit. Because the barrier's construction is free to *choose* its orbit,
a unimodular orbit (D=425 or σ=5/8) is a valid witness with the floor intact. These scripts are
reproducible; the referee need not consult them (all premises are stated inline).

---

## 6. Numerical anchor (sanity only, not an input to the proof)

Exact, independently re-derivable by a few lines of rational arithmetic.

**Orbit** `ρ = 3/4 + i` (`σ₀ = 3/4, τ₀ = 1`; the split-prime orbit `D = 425 = 5²·17`). For
`m = 4` the fixed off-line vector is
```
    w = B^{−1} d = ( −304/425,  −91184/180625,  −25884464/76765625,  −6963575344/32625390625 ),
    v_3(w_i) = (0, 0, 0, 0)   ⇒  the orbit is 3-adically unimodular (§1.7).  ✓
```
**Configuration** `m = 4`, nodes `t = (9, 37, 5, 17)`, giving x-values
```
    x = ( 323/325,  5475/5477,  99/101,  1155/1157 ),   x-residues mod 3 = (2, 0, 0, 0).
```
Then, by §1.6,
```
    N_j = (0, 4, 2, 4),   C_j = (0, 0, 0, 0),   v(q_min) = max_j (N_j − C_j) = 4  ≥  m/2 = 2.   ✓
```
Here three x-values share residue 0 mod 3, forcing the pairwise valuations that make `N_2, N_4
= 4`; `w` unimodular keeps all `C_j = 0` on this (unaligned) node set. Under adversarial 3-adic
alignment a single `C_j` can be driven large (§2, §5), yet the maximum `N_j − C_j` stays
`≥ m/2 − O(1)` — the content of the Theorem. A referee should confirm (a) `v_3(w_i) = 0`;
(b) the x-residues `(2,0,0,0)`; (c) `N_j = (0,4,2,4)`, `C_j = (0,0,0,0)`; (d) floor `= 4`.
**Sanity only — not an input.**

---

## Pre-send lint notes (PROMPT_LINT.md self-check)

| Item | Status |
|---|---|
| L1–L4 | N/A — no entire-function / order / canonical-product claims |
| L5 (RH via divisor / circular target) | PASS — no ζ/L zeros, no real-zero product; the only "off the critical line" mention is the *definition* of the single hypothesized off-line point (§1.3), not an RH assumption. The algebraic rank / analytic rank never appear; `d` is a finite rational Li-type observation, not an L-value |
| L6 (vacuous target / real atoms) | PASS — target is a finite rational determinantal floor; a non-vacuous REFUTED path (explicit unimodular-orbit family with floor `= o(m)`) is available |
| L7–L17 | N/A — no counting-function factor, growth ray, Fredholm, meromorphic-type, or externally-cited black-box steps (all premises proved in-repo, stated inline) |
| L18 (numerical anchor by script) | PASS — anchor re-derived by exact `Fraction` arithmetic: `w`, `v_3(w_i)=0`, x-residues `(2,0,0,0)`, `N=(0,4,2,4)`, `C=(0,0,0,0)`, floor `=4` |
| L19 (honest inconclusive verdict) | PASS — outcomes STRATEGY / PARTIAL / INCONCLUSIVE+localization all first-class; no prove-or-refute dichotomy; a sub-`ω(log m)` refutation is explicitly welcomed |
| L20–L24 | N/A |
| Self-containment | PASS — every symbol/formula in-file (`x(t)`, Chebyshev `C_j`, target `d_j`, graded basis `q_i`/`B`, `w = B⁻¹d`, `N_j`, `C_j`, `e_l`, `D_r`, `q_min`, unimodularity, `PIG(m)`); `grep "see .*\.md"` → clean; §5 provenance is a reference only, not load-bearing |
| Deliverable breadth | PASS — a sanity-checked *proof strategy* (STRATEGY) is a successful deliverable; full proof not required |
| Privacy | PASS — no personal usernames, home paths, company/internal domains, or hardware model numbers; all quantities are abstract rationals/primes |
