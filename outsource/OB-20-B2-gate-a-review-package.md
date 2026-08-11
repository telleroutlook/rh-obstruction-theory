# Problem OB-20 — B2 Gate-A package: independent inspection of the full analytic assembly

**Type:** Gate-A independent mathematical review (whole-theorem inspection, not a fragment)

**What this is.** Unlike OB-01..19 (each verified one step or one finite computation), this
is a request to **independently inspect the entire B2 analytic chain as a coherent whole**
and issue a **Gate-A verdict**: is the theorem, as assembled from its stated lemmas,
correct, self-contained, and free of hidden gaps / circularity / RH-import? The finite
core is already independently certified (exact-rational reconstruction, prior review); the
open step is confirming the *assembly*.

**Non-circularity (mandatory).** RH is not assumed and must not appear in any hypothesis.
No zero ordinate of ζ, no Euler product, no functional equation of ζ is used. The multisets
below are **constructed** finite objects; `𝒵_+` is NOT ζ's zeros. A Gate-A pass must
confirm no step secretly imports RH or an RH-equivalent.

---

## All definitions (self-contained — everything is here)

### Ambient class

A **finite** multiset `𝒵 ⊂ ℂ \ {0,1}` (multiplicity `m_𝒵(z)`) is in `𝔛_sym` iff for
every `z`: `m_𝒵(z) = m_𝒵(z̄) = m_𝒵(1−z)` (symmetry under conjugation and `ρ↦1−ρ`,
with multiplicity). Predicate: `P(𝒵)=1` iff every atom has `Re ρ = 1/2`, else `P(𝒵)=0`.

### Test family and observation

Li-type tests `φ_j(ρ) = 1 − (1−1/ρ)^j`, `j = 1,…,m`. Global observation (Weil Σ'):
```
O_j(𝒵) = Σ_{ρ ∈ 𝒵} [φ_j(ρ) + φ_j(1−ρ)]   (with multiplicity; additive under ⊔).
```
`O_Φ(𝒵) = (O_1(𝒵),…,O_m(𝒵))`.

### On-line pairs and off-line quartet

`L(t) = {1/2+it, 1/2−it}` (`t>0`); `Q(σ_0,T) = {σ_0+iT, σ_0−iT, 1−σ_0+iT, 1−σ_0−iT}`
(`σ_0 = 3/4`, `T>0`). Both are in `𝔛_sym`. Orbit values (reflection-symmetric quartet):
```
O_j(L(t)) = 4 Re φ_j(1/2+it),   O_j(Q(3/4,T)) = 4 Re[φ_j(3/4+iT) + φ_j(1/4+iT)].
```

### The construction (the object under review)

Fix distinct rational heights `t_1<…<t_m>0`, rational `T>0`. Define:
```
C_{jk} = O_j(L(t_k)) = 4(1 − T_j(x_k)),   x_k = (4t_k²−1)/(4t_k²+1),  T_j = Chebyshev,
d_j(T) = O_j(Q(3/4,T)).
```
Solve `C β = −d(T)`, `β ∈ ℚᵐ` (needs `det C ≠ 0`). Let `R = lcm(denominators of β)`,
`n = Rβ ∈ ℤᵐ`, `M = max_k|n_k|`. Then:
```
𝒵_+ = ⊔_{k=1}^m M·L(t_k),
𝒵_− = (⊔_{k=1}^m (M+n_k)·L(t_k)) ⊔ R·Q(3/4,T).
```

### The claimed theorem (B2)

For a fixed finite Li family `Φ` (m tests), the above yields `𝒵_+, 𝒵_− ∈ 𝔛_sym` with
`P(𝒵_+)=1`, `P(𝒵_−)=0`, and **exact** collision `O_Φ(𝒵_−) = O_Φ(𝒵_+)` (i.e. `Cn+Rd=0`).

---

## The full analytic chain to inspect (the six links)

A Gate-A review must confirm **each link AND their coherent composition**:

**Link 1 (quartet decay / well-definedness).** `d_j(T) = 4Re[φ_j(3/4+iT)+φ_j(1/4+iT)]` is
well-defined and rational for rational `T` (φ_j rational, evaluated off `{0,1}`). [The
decay `d_j(T)→0` is not needed for the *exact* collision — B2 solves exactly at a fixed
`T` — but confirm `d_j(T)` is finite and the orbit formula's factor 4 is correct.]

**Link 2 (rank lemma).** `det C ≠ 0` for distinct positive rational `t_k`. Proof
(self-contained): `1−T_j(x) = (1−x)q_{j−1}(x)` with `deg q_{j−1}=j−1`, leading coeff
`2^{j−1}`; so `C = 4·diag(1−x_k)·[q_{j−1}(x_k)]`, and `[q_{j−1}(x_k)] = A·V` (A lower-
triangular with positive diagonal, V Vandermonde). Hence `det C = 4^m 2^{m(m−1)/2}
∏(1−x_k) ∏_{k<l}(x_l−x_k) ≠ 0` (since `x(t)=(4t²−1)/(4t²+1)` is strictly increasing, so
`x_k` distinct and `<1`). **Confirm this is a complete, citation-free proof.**

**Link 3 (rationality).** For rational `t_k, T`: `x_k ∈ ℚ`, `C ∈ ℚ^{m×m}`, `d(T) ∈ ℚ^m`,
hence `β = −C⁻¹d ∈ ℚ^m`. **Confirm.**

**Link 4 (integer scaling + nonneg multiplicity).** `R = lcm(denominators of β)` gives
`n = Rβ ∈ ℤ^m`; `M = max_k|n_k|` gives `M+n_k ≥ 0`. So `𝒵_+, 𝒵_−` have nonneg integer
multiplicities. **Confirm no signed/fractional multiplicity is forced.**

**Link 5 (membership + predicate).** `𝒵_± ∈ 𝔛_sym` (finite; L and Q closed under `ρ↦ρ̄`
and `ρ↦1−ρ`); `P(𝒵_+)=1` (all on `Re=1/2`); `P(𝒵_−)=0` (Q has `Re=3/4≠1/2`). **Confirm.**

**Link 6 (exact collision).** By additivity of `O_j` and the construction,
`O_j(𝒵_−) − O_j(𝒵_+) = Σ_k n_k C_{jk} + R d_j(T) = (Cn + Rd)_j = R(Cβ+d)_j = 0`.
**Confirm the identity holds exactly, and that Links 1–5 supply exactly what Link 6 needs.**

---

## The Gate-A questions (the actual deliverable)

Beyond confirming the six links, the review must answer these **whole-theorem** questions:

### Q1 — Hidden gap / circularity
Is there any step that silently assumes what it should prove? In particular: does any link
use RH, an RH-equivalent, or a property of ζ's actual zeros? (Expected: no — `𝒵_+` is a
buffer of `M` copies of arbitrary on-line pairs, not ζ's zeros.) Confirm or exhibit the
leak.

### Q2 — Non-vacuity
Is the class `𝔛_sym` genuinely populated by the construction for some concrete `(m, t_k,
T)`, with both `P=1` and `P=0` members genuinely differing on the predicate while sharing
`O_Φ`? Confirm the theorem is not vacuously true (e.g. via an empty or degenerate class).
[Note: a prior review flagged that WITHOUT a no-real-atom condition (NR) the obstruction
can be trivialized by adding invisible real atoms `{1/4,3/4}`. Confirm whether B2's
construction — which uses only on-line pairs + the off-line quartet, all non-real — avoids
this, and whether (NR) needs to be stated as an explicit class condition.]

### Q3 — Analytic/finite separation
Does the theorem cleanly separate its analytic content (there is essentially none — B2 is
finite algebra) from finite computation? Is every "black box" (Chebyshev identity,
Vandermonde nonsingularity, lcm scaling) elementary and citation-free as claimed?

### Q4 — Scope and escape honesty
Are the stated limitations correct and complete? Specifically: (a) fixed finite `Φ` only
(infinite hierarchy escapes); (b) `O(1)` counting-law perturbation (handled on the
augmented class by adjoining an inverse-counting background, else the bare class has no
counting law); (c) B2 is about zero *multisets* under finite observation, NOT about entire
functions (canonical-product realization is a separate task). Confirm these are the correct
and complete non-conclusions, or identify a missing one.

### Q5 — Gate-A verdict
Given Q1–Q4 and the six links: does B2, as assembled, constitute a correct, self-contained,
non-circular finite obstruction theorem — i.e. **should its status advance from PROOF-DRAFT
toward INDEPENDENTLY-CHECKED** on the mathematical axis? Or does a specific gap block it?

---

## Numerical anchor (sanity only — the exact assembly at m=2)

`m=2`, `t=(1,2)`, `T=1`, `σ_0=3/4`, Li tests `j=1,2` (independently recomputed, exact):
```
C = [[8/5, 8/17], [128/25, 512/289]],   det C = 3072/7225 ≠ 0,
d(1) = [1216/425, 1763072/180625],
β = −C⁻¹d(1) = [−1426/1275, −854/375],
R = 6375,  n = [−7130, −14518],  M = 14518,  M+n = [7388, 0] (both ≥ 0),
C n + R d(1) = [0, 0]  (exact collision).
```
This single instance exhibits all six links closing simultaneously. The Gate-A deliverable
is the whole-theorem judgment (Q1–Q5), not a re-run of this arithmetic (which prior review
already certified independently).

---

## Acceptance criteria

1. **GATE-A PASS:** all six links confirmed, Q1–Q4 answered with no blocking gap, and Q5
   returns "advance toward INDEPENDENTLY-CHECKED." State any conditions (e.g. "add (NR) as
   an explicit class condition") required for the pass.

2. **GATE-A CONDITIONAL:** the chain is correct but a specific textual fix is required
   before the status can advance (e.g. an explicit (NR) condition, or a limitation that
   must be stated). Give the exact required edit.

3. **GATE-A BLOCKED:** a genuine gap, circularity, or RH-import exists in the assembly.
   Identify the link/question, exhibit the problem, and state the minimal repair.

All outcomes decisive. A Gate-A verdict of "conditional, add (NR)" is a valuable and
acceptable result — the goal is an honest independent judgment of the whole theorem, not a
forced pass.
