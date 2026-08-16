# Problem OB-41 — Uniform p-adic rigidity of the argument-ratio: the O(1) incidence-lag bound (OP1 LEG3)

**Type:** arithmetic / p-adic analysis / determinantal (lattice) geometry — a finite,
exact, RH-free question about rational vectors and p-adic valuations.

**Non-circularity.** This problem does NOT assume the Riemann Hypothesis, does NOT use any
value, derivative, or zero location of ζ or any L-function, and does NOT read "analytic
rank" or any RH-equivalent input. The object is a finite integer/rational linear-algebra
configuration and its p-adic valuations. The single "off-line" datum is one *hypothesized*
point `ρ = σ₀ + iτ₀` with `σ₀ ≠ 1/2` (the barrier asks: can a finite family of on-line
observations detect such a hypothesized point?); nothing is assumed about the truth or
falsity of RH. All quantities below are exact rationals; all claims are checkable by exact
arithmetic. RH stays outside this problem.

This is the sole remaining open leg (LEG3) of a barrier program (OP1) whose other two legs
are proved. The referee is asked to **prove, propose a feasible (sanity-checked) proof
strategy for, refute, or precisely localize** the bound below. A complete proof is NOT
required for a successful deliverable: a concrete, plausible proof route — with its key
sub-steps identified and at least a lightweight check (small-case computation, a reduction
to a known theorem, or a heuristic that the mechanism is real) — is a first-class outcome
(see §4, outcome **STRATEGY**).

---

## 1. All definitions (self-contained — every symbol and formula is here)

Fix an odd prime `p`, an integer `m ≥ 2` (the observation dimension), and rationals
`σ, τ ∈ ℚ` describing a fixed off-line orbit (see §1.4). All arithmetic is over `ℚ`; `v_p`
is the p-adic valuation on `ℚ` (`v_p(0) = +∞`, `v_p(a/b) = v_p(a) − v_p(b)`).

### 1.1 The node map and x-classes
A **node** is a nonzero rational `t`. Its **x-value** is
```
    x(t) = (4 t² − 1) / (4 t² + 1)  ∈ ℚ.
```
Note `x(t)` depends only on `t²`, so `x(t) = x(−t)`: the map `t ↦ x(t) mod p` is
**2-to-1** on nonzero residues. Hence there are exactly `(p−1)/2` distinct nonzero-`t`
x-classes mod `p` (plus the class of `x = 1`, which is `x(t) → 1` as `t → ∞`, i.e. the
image of `t ≡ 0`). For a rational `x = a/b` in lowest terms, its **x-residue** mod `p` is
`xres(x) = a·b⁻¹ mod p` if `p ∤ b`, and `∞` (undefined) if `p | b`.

### 1.2 Chebyshev observation columns (context; not load-bearing for the core bound)
For `j ≥ 0` let `T_j` be the Chebyshev polynomial of the first kind
(`T_0 = 1, T_1 = X, T_{j+1} = 2X·T_j − T_{j−1}`). The **observation column** of a node `t`
is the integer-clearable rational vector in `ℚ^m`
```
    C(t) = ( C_1(t), …, C_m(t) ),   C_j(t) = 4·( 1 − T_j(x(t)) ),   x = x(t).
```

### 1.3 The off-line target vector (context)
Given `ρ = σ₀ + i τ₀` off the critical line, its orbit is
`{σ₀ ± iτ₀, 1−σ₀ ± iτ₀}` (4 atoms). The **target vector** `d = (d_1, …, d_m) ∈ ℚ^m` is
```
    d_j = Σ_{atoms (r,ι)} Σ_{(r',ι') ∈ {(r,ι),(1−r,ι)}}  Re[ 1 − (1 − 1/(r'+iι'))^j ].
```
(This is the finite Li-type observation of the orbit; `Re[1 − (1 − 1/ρ')^j]` is an exact
rational.) `d` is the vector a finite observer would need to "hit" to register a collision.

### 1.4 The off-line atom `u` (Joukowski image) — carries `σ, τ`
From `ρ = σ₀ + iτ₀` form
```
    w = 1 − 1/ρ,      u = (w + 1/w) / 2  =: σ + i τ ∈ ℚ(i).
```
`σ := Re(u)` and `τ := Im(u)` are **the atom's own real and imaginary parts** — NOT `σ₀,
τ₀`. (Worked value in §6.) The four orbit atoms give up to 4 such `u`; fix any one.

### 1.5 The affine functional Ψ and the on-line weight Φ
For a finite set `S = {t_{k_1}, …, t_{k_r}}` of nodes, write `x_k = x(t_k)` and define the
**orbit-sum functional** (an exact rational; `Re` = real part in `ℚ(i)`)
```
    Ψ(S) = 2·Re[ (u − 1) · ∏_{k ∈ S} (u − x_k) ]
```
and the **on-line p-adic weight**
```
    Φ(S) = Σ_{k ∈ S} v_p(x_k − 1)  +  Σ_{k < l, k,l ∈ S} v_p(x_l − x_k).
```

### 1.6 The collision constraint (what makes a configuration "valid")
Let `A` be the `m × K` integer matrix whose columns are the cleared (common-denominator-
multiplied) integer forms of `C(t_1), …, C(t_K)`, and let `v_off` be the cleared integer
form of `d`. For an integer matrix `X` and integer `r`, let `D_r(X)` be the **r-th
determinantal divisor** = gcd of all `r × r` minors of `X` (equivalently, the product of
the first `r` Smith-normal-form invariant factors; `D_r(X) = 0` iff `rank X < r`). A
**valid collision** is a configuration with
```
    (C1)  v_off ∈ ℚ-span of the columns of A     (a finite integer relation exists), and
    (C2)  D_m(A) ≠ 0                              (⇔ rank A = m ⇔ K ≥ m on-line columns).
```
When valid, the minimal positive multiplier is the finite index
```
    q_min = D_m(A) / D_m([A | v_off])   (a positive integer; the barrier's collision size).
```
(C2) forces `K ≥ m`: an `m × K` matrix of rank `m` needs at least `m` columns. This
`K ≥ m` fact is what supplies the competition in §2.

### 1.7 The incidence lag
A subset `S` of size `m−1` is a **Φ-minimizer** if `Φ(S) = min_{|S'|=m−1} Φ(S')`. The
**incidence lag** of a valid collision is
```
    lag = min_{ S ∈ argmin Φ }  v_p( Ψ(S) ).
```
(`|S| = m−1`; the min is over the on-line node set of the collision.) Below, `ψ(S) :=
v_p(Ψ(S))`, so `lag = min over Φ-minimizers of ψ(S)`.

### 1.8 x-class slack
`navail` = number of distinct finite x-residues `xres(x(t_k)) mod p` among the nodes,
excluding the class of `x = 1`. The **x-class slack** is
```
    slack_x = (p − 1)/2 − (m − 1).
```
The relevant regime (matching the barrier's other legs) is `p ≥ 2m − 1`, i.e.
`slack_x ≥ 0`. (For `p < 2m−1` a configuration cannot even fill `m−1` distinct x-classes;
those are forced-degenerate artifacts, excluded — see §4.)

---

## 2. The theorem to be verified

> **Theorem (OP1 LEG3 — uniform O(1) incidence-lag bound).**
> There is an absolute constant (namely 3) such that for every odd prime `p`, every
> `m ≥ 2` with `p ≥ 2m − 1`, every off-line split-prime orbit atom `u` (§1.4), and every
> **valid collision** (§1.6) on `K ≥ m` on-line nodes,
> ```
>     lag  ≤  2      if slack_x ≥ 1,
>     lag  ≤  3      if slack_x = 0,
> ```
> uniformly in `m` and `p`, and independently of the orbit `u`.

Equivalently (via the reduction of §3): at a lag-achieving Φ-minimizer with swing node `x`,
```
    v_p(x − α)  ≤  2   (slack_x ≥ 1),   ≤ 3  (slack_x = 0),   α = σ − τ·Im(H)/Re(H),
```
where `H = (u − 1)·∏_{j ∈ C}(u − x_j)` over the complement `C = S ∖ {swing}`. In words: the
**argument-ratio** `Im(H)/Re(H)` of the on-line complement product cannot p-adically
approach the fixed target `(σ − x)/τ` beyond depth 2 (resp. 3) **under the collision
constraint** (C1)–(C2).

The bound may be replaced by any absolute constant `≤ C₀` uniform in `m, p, u` — the value 3
(and the slack split 2 / 3) is the observed sharp form, but the essential deliverable is
**m-independence** (an O(1) bound), which is what closes the leg.

---

## 3. Proof skeleton to be closed

The following two steps are already **proved** here (inlined as premises); the referee may
use them freely. Steps 3 and 4 are the open core.

### Step 1 — Reduction: `lag ≤ min over Φ-minimizers of ψ(S)`. **[proved, premise]**
The `d`-augmented `m`-minor of `[A | v_off]` factors (column-linearity in the `d`-column,
plus the `C_j = (x−1)g_j` factorization) as
`det[A_S | d] = (p-unit)·∏_{k∈S}(x_k−1)·Vand(S)·Ψ(S)`, and `v_p(D_{m−1}(A)) = min_{S'}Φ(S')`
(the top-rows minor realizes `D_{m−1}`). Hence `lag = min_{S'}[Φ(S')+ψ(S')] − min_{S'}Φ(S')
≤ ψ(S_0)` for any `S_0 ∈ argmin Φ`. So `lag ≤ min over Φ-minimizers of ψ`.
*Verified exact across 3 orbits, `p ∈ {3,7,11}`, `m = 2..7`, all node families.*

### Step 2 — Two-source valuation identity. **[proved, premise]**
With `H = (u−1)∏_{j∈C}(u−x_j) = P + Qi` (`P = Re H`, `Q = Im H`), `σ = Re(u)`, `τ = Im(u)`,
and any swing node `x`:
```
    Ψ({x} ∪ C) = 2·Re[(u − x)·H] = 2·Re(H)·(α − x),   α = σ − τ·Q/P = σ − τ·Im(H)/Re(H),
```
so, taking valuations (odd `p`),
```
    ψ = v_p(Ψ) = v_p(Re H) + v_p(x − α).                              (§6s-main)
```
*Verified exact 0/6000 (both the algebraic identity and the valuation identity) across all
3 orbits.* Consequence: the lag has two independent p-adic sources, (i) `v_p(Re H)` and
(ii) `v_p(x − α)`.

### Step 3 — Bound the real-part source `v_p(Re H)`. **[open — likely the easier half]**
*Empirically* `v_p(Re H) ≤ 1` at lag-achieving Φ-minimizers, and it contributes 0 at the
`slack_x = 0` extreme (the whole lag lives in term (ii); see §6 anchor). **What to close for
Step 3:** prove a uniform bound `v_p(Re H) ≤ c₁` (constant, `m`-independent) at a
lag-achieving Φ-minimizer of a valid collision — or show it is dominated by / foldable into
Step 4. A clean statement of "how p-divisible can `Re[(u−1)∏(u−x_j)]` be for on-line
`x_j` in distinct x-classes" would suffice.

### Step 4 — Bound the argument-ratio source `v_p(x − α)` (**the hard core**). **[open]**
This is the essential difficulty. The pairwise-swap observation (below) gives only
`min over Φ-minimizers of ψ ≤ v_p(x_a − x_b)` for a swappable same-class pair `{a,b}` — but
`v_p(x_a − x_b)` is adversary-controlled (nodes `t_a, t_b` can be chosen with `x(t_a) ≡
x(t_b)` to arbitrarily high p-adic order), so pairwise-swap **alone does not** bound the
lag. The genuine mechanism must be a **rigidity** of `α = σ − τ·Im(H)/Re(H)` as the
complement `C` ranges over the choices compatible with a valid collision:

> **Sub-claim (Step 4 core).** For a valid collision (C1)–(C2) with `K ≥ m` and `slack_x ≥
> 1`, no choice of complement `C` (equivalently, no lag-achieving Φ-minimizer) can satisfy
> `α ≡ x (mod p³)` for the doubled-class swing node `x`; i.e. `v_p(x − α) ≤ 2`. At `slack_x
> = 0` the bound relaxes by exactly one unit (`≤ 3`), the extra unit coming from the
> `x(t) = x(−t)` class-doubling forced when only `(p−1)/2 = m−1` x-classes are available.

**What to close for Step 4.** Prove the Sub-claim. Two structural facts are available as
starting handles:
- **(H-swap) Pairwise-swap identity (proved).** If `a, b` share an x-class and there are
  Φ-minimizers `S ∋ a`, `S' ∋ b` with identical complement `C = S∖{a} = S'∖{b}`, then `α =
  α(C)` is the *same* for both, so `ψ(S) = v_p(x_a − α)`, `ψ(S') = v_p(x_b − α)`; both `≥
  d+1` would force `x_a ≡ x_b ≡ α (mod p^{d+1})`, contradicting `v_p(x_a − x_b) = d`. Hence
  `min(ψ(S), ψ(S')) ≤ v_p(x_a − x_b)`. *(Verified on 1144/1144 swappable pairs.)*
- **(H-comp) The K ≥ m competition (proved boundary).** A valid collision needs `D_m(A) ≠
  0`, so `K ≥ m` and there are `C(K, m−1) ≥ m` competing Φ-minimizers; the lag is the
  **min** over all of them. The determinantal constraint `D_m(A) ≠ 0` ties the `Ψ(S)`
  across subsets `S` (they are the `d`-residual minors of one rank-`m` matrix), so they
  cannot *all* be simultaneously deep. The open task is to convert this shared-determinant
  coupling into the uniform depth bound of the Sub-claim.

A proof of Step 4 (with or without Step 3 folded in) closes LEG3 and hence the split-prime
case of OP1.

---

## 4. Acceptance criteria

Report exactly one of the following, with the stated evidence. An honest partial/localized
outcome is a first-class result — do **not** force a prove/refute dichotomy.

1. **CONFIRMED.** A proof of the Theorem (§2), or of Step 4 (the Sub-claim) plus a proof or
   citation closing Step 3. State every hypothesis used; confirm none of them is RH, an
   L-value, a zero location, or an RH-equivalent (non-circularity). The uniform constant
   need not be exactly 3 — any absolute `m`-independent `C₀` closes the leg; state your `C₀`.

2. **STRATEGY (feasible proof route — a full proof is NOT required).** A concrete,
   plausible plan to prove the Theorem, even if not carried to completion. To qualify it
   must: (a) name the main tool/theorem it would invoke (e.g. a p-adic
   equidistribution/rigidity result, a resultant/discriminant valuation bound, a
   Newton-polygon argument on `∏(u−x_j)`, a Smith-normal-form coupling of the competing
   `Ψ(S)`, …) and why it applies here; (b) break Step 4 into sub-lemmas and say which are
   standard vs genuinely new; (c) include at least a **lightweight check** that the route is
   not hopeless — e.g. verify the key sub-lemma on the §6 anchor and one `slack_x ≥ 1` case,
   or reduce the Sub-claim to a clean statement whose small-case truth you confirm. Identify
   the one step most likely to fail. A well-argued route with a passing sanity check is a
   successful, deliverable outcome.

3. **PARTIAL.** A proof of one regime (e.g. `slack_x ≥ 1` only, or the two-term bound with
   Step 3 done but Step 4 open), or a proof of an `m`-*dependent* bound `lag ≤ f(m)` with
   the best `f` you can certify (e.g. `O(log m)`, `O(1)` only for fixed residue patterns).
   Specify precisely what is proved and what remains.

4. **REFUTED.** An explicit **valid collision** (exhibit `p, m, u`, the `K ≥ m` nodes
   `t_k`, and verify (C1)–(C2) and `D_m(A) ≠ 0` by exact arithmetic) with `lag ≥ 3` at
   `slack_x ≥ 1`, or a family with `lag → ∞` as `m → ∞` in the regime `p ≥ 2m−1`. This
   would show the incidence lag is not O(1) and the leg needs a narrower profile — a
   legitimate and valuable outcome. (Note: `slack_x = 0` configs reaching `lag = 3` are
   NOT refutations; the claim allows 3 there. `p < 2m−1` forced-degenerate configs are
   excluded by hypothesis and are not refutations.)

5. **INCONCLUSIVE + precise localization.** If neither a proof nor a counterexample is
   reached, identify the exact step that resists (e.g. "the shared-determinant coupling
   (H-comp) does not by itself bound the depth because …"), and state the minimal additional
   input that would close it.

---

## 5. Provenance of the premises (for verification only, not part of the problem)

The two premise steps and the empirical bounds were verified by exact-arithmetic scripts in
this repository's discovery tier (untrusted, never imported into proofs): the affine
identity and Φ/Ψ factorization (`probe_leg3_affine.py`, `probe_leg3_psi_bound.py`), the
two-source identity `ψ = v_p(Re H) + v_p(x−α)` (0/6000 exact, 3 orbits), the pairwise-swap
identity (1144/1144), the collision boundary `K ≥ m` (`qmin_fast`/determinantal-divisor),
and the orbit-independent regime split (`slack_x ≥ 1 → ≤2`, `slack_x = 0 → ≤3`; `p ≤ 13`,
`m ≤ 6`, orbits `D = 425, 4, 26`). These are stated inline above as premises; the referee
need not consult the scripts, but they exist and are reproducible.

---

## 6. Numerical anchor (sanity only, not an input to the proof)

Exact, independently re-derivable by hand or a few lines of rational arithmetic.

**Orbit** `ρ = 3/4 + i` (so `σ₀ = 3/4, τ₀ = 1`; this is the split-prime orbit `D = 425 =
5²·17`). Its atom (§1.4):
```
    w = 1 − 1/(3/4 + i) = 1 − (3/4 − i)/((3/4)² + 1) = 13/25 + (16/25) i,
    u = (w + 1/w)/2 = 273/425 − (64/425) i,    so  σ = 273/425,  τ = −64/425.
```
**Configuration** `p = 7`, `m = 4`, nodes `t = (688, 426, 596, 1374)`. Then
`x(t_k) = (4t_k² − 1)/(4t_k² + 1)` has x-residues `(5, 2, 2, 5) mod 7`, giving two doubled
x-classes → `navail = 2 = m − 2`, `slack_x = (7−1)/2 − 3 = 0`.

The two Φ-minimizers `S = {0,1,2}` and `S = {1,2,3}` (0-indexed) both give
`ψ(S) = v_p(Ψ(S)) = 3`, so `lag = 3`. Two-source split at `S = {0,1,2}`, swing node `k=0`
(`H = (u−1)(u−x_1)(u−x_2)`):
```
    v_p(Re H) = 0,   v_p(x_0 − α) = 3,   α = σ − τ·Im(H)/Re(H),
    ⇒  ψ = 0 + 3 = 3 = v_p(Ψ).                         ✓ (matches §6s-main)
```
This is a `slack_x = 0` witness at the sharp value 3 (allowed by the Theorem). A referee
should confirm (a) the atom `u = 273/425 − 64i/425`; (b) the x-residues `(5,2,2,5)`; (c)
`lag = 3`; (d) the two-source split `0 + 3`. Under `slack_x ≥ 1` the same search caps `lag`
at 2 (verified across `p ≤ 13`, `m ≤ 6`, all three orbits). **Sanity only — not an input.**

---

## Pre-send lint notes (PROMPT_LINT.md self-check)

| Item | Status |
|---|---|
| L1–L4 | N/A — no entire functions / order / canonical-product claims |
| L5 (RH via divisor) | PASS — no zeta/L zeros, no real-zero product; the only "off the critical line" mention is the *definition* of the single hypothesized off-line point, not an RH assumption. `grep -ni "critical line\|real zeros"` → one definitional hit (§1.3), no divisor-over-real-zeros |
| L6 (vacuous target / real atoms) | PASS — the target is a finite rational determinantal configuration; REFUTED path (explicit valid collision with `lag ≥ 3` at `slack_x ≥ 1`, or `lag → ∞`) is available and non-vacuous |
| L7–L17 | N/A — no counting-function factor, growth ray, Fredholm, meromorphic-type, or cited-black-box steps (premises proved in-repo, stated inline) |
| L18 (numerical anchor by script) | PASS — anchor independently re-derived by exact `Fraction` arithmetic: atom `u = 273/425 − 64i/425`, x-residues `(5,2,2,5)`, `lag = 3`, two-source split `0 + 3`; hand-derivation of `u` in §6 checks (`w = 13/25 + 16i/25`, `u = (w+1/w)/2 = (273 − 64i)/425`) |
| L19 (honest inconclusive verdict) | PASS — outcomes STRATEGY / PARTIAL / INCONCLUSIVE+localization all first-class; no prove-or-refute dichotomy |
| L20–L24 | N/A |
| Self-containment | PASS — every symbol/formula in-file (`x(t)`, Chebyshev `C_j`, target `d_j`, atom `u`, `Ψ`, `Φ`, determinantal divisor `D_r`, `q_min`, `slack_x`, `α`, two-source identity); `grep "see .*\.md"` → clean; §5 provenance is a reference only, not load-bearing |
| Deliverable breadth (user directive) | PASS — a sanity-checked *proof strategy* (outcome STRATEGY) is explicitly a successful deliverable; full proof not required |
| Privacy | PASS — scanned for personal usernames, absolute home paths, company/internal domains, and hardware model numbers → none present (all quantities are abstract rationals/primes) |
