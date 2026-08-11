# Problem OB-34 — H resend: incomparability of O_finite and O_theta^{samp} (all K), via the B2 pair

**Type:** Gate-A independent mathematical review (single incomparability claim, scoped).

**What this is.** A **resend** after OB-32 BLOCKED the H incomparability theorem H'(i). OB-32's
two defects are fixed and the claim is re-scoped: (a) `O_oracle` is now the full multiset `𝒵`
(not ordinates-only); (b) the observation `O_theta` is now the explicitly **nonconstant**
sampled-count map `O_theta^{samp}` (the literal `d_n=θ_level(n)` is constant and is not used
for incomparability). With these fixes the incomparability `O_finite ⋈ O_theta^{samp}` holds
**for every K**, and — the key point — the harder (reverse) direction **inherits the
Gate-A-established B2 exact-collision pair (OB-20)**, so no new unaudited construction is
introduced. The review is asked to confirm the two witnesses and the map definitions.

**Non-circularity (mandatory).** RH is not used. Everything is finite-multiset combinatorics
(`Li_1 = Σ1/ρ`, atom counts) plus the already-established B2 collision. `{γ_n}` never enters;
the multisets are constructed finite objects. Confirm no RH-import.

---

## All definitions (self-contained)

`𝔛_sym` = finite zero-multisets symmetric under conjugation and `ρ↦1−ρ`.

- **`O_finite^{(K)}(𝒵) = (Li_1(𝒵),…,Li_K(𝒵))`**, `Li_j(𝒵)=Σ_{ρ∈𝒵}[φ_j(ρ)+φ_j(1−ρ)]`,
  `φ_j(ρ)=1−(1−1/ρ)^j` (the B2 R-symm convention; for `j=1`, `Li_1(𝒵)=Σ_ρ 1/ρ` up to the
  reflection). Sees real parts.
- **`O_theta^{samp}(𝒵) = (N_𝒵(d_1),…,N_𝒵(d_M))`**, a **fixed** level set `d_1<…<d_M`,
  `N_𝒵(u)=#{ρ∈𝒵 : |Im ρ| ≤ u}` counted **with multiplicity**. This is a genuine, **nonconstant**
  functional of `𝒵` (unlike Theorem G's literal `d_n=θ_level(n)`, which is a fixed
  `𝒵`-independent sequence, hence constant — see the caveat).
- **`O_oracle(𝒵) = 𝒵`** (the full multiset; finest).
- **Refinement preorder:** `O_a ≼ O_b` iff `O_b(𝒵)=O_b(𝒵') ⇒ O_a(𝒵)=O_a(𝒵')`. `O_a ⋈ O_b`
  ("incomparable") iff neither `O_a ≼ O_b` nor `O_b ≼ O_a`. (A preorder — antisymmetry only on
  info-equivalence classes; **no lattice** is claimed.)

**Established premise (inherited).** Theorem B2 (Gate-A PASS OB-20 + checker OB-21): for any
finite test family there is a pair `𝒵₊, 𝒵₋ ∈ 𝔛_sym` with
```
𝒵₊ = ⋃_k {1/2±it_k}^{(M_0)}   (on-line, multiplicity M_0),
𝒵₋ = ⋃_k {1/2±it_k}^{(M_0+n_k)} ∪ Q(σ₀,T)^{(R)}   (σ₀∈(1/2,1), T>t_n, R≥1),
```
such that `O_finite^{(m)}(𝒵₊)=O_finite^{(m)}(𝒵₋)` **exactly** (the collision `Cn+Rd=0`),
`P(𝒵₊)=1`, `P(𝒵₋)=0`. Here `Q(σ₀,T)={σ₀±iT, 1−σ₀±iT}` is the off-line quartet.

---

## The claim to inspect

**Theorem H'(i) (incomparability, all K).** For the maps above, `O_finite^{(K)} ⋈
O_theta^{samp}` for every `K≥1`. Two **exact** witnesses, one per direction.

**Witness 1 — `O_finite ⋠ O_theta^{samp}`** (a pair with `O_theta^{samp}` **equal** but
`O_finite` **different**). Take two symmetric quartets at the **same height** `T` but different
real offset: `𝒵_a=Q(3/4,T)={3/4±iT,1/4±iT}` and `𝒵_b=Q(9/10,T)={9/10±iT,1/10±iT}`. Both have
the **identical imaginary-part multiset** `{±T,±T}`, so `N_{𝒵_a}(u)=N_{𝒵_b}(u)` at **every**
level `u` ⇒ `O_theta^{samp}(𝒵_a)=O_theta^{samp}(𝒵_b)` (equal). But `Li₁` differs:
`Li₁(𝒵_a)=0.0199129…` vs `Li₁(𝒵_b)=0.0198551…` (at `T=10`; exact rationals below). So an
`O_theta^{samp}`-collision is **not** an `O_finite`-collision ⇒ **`O_finite ⋠ O_theta^{samp}`**.

**Witness 2 — `O_theta^{samp} ⋠ O_finite`** (a pair with `O_finite` **equal for all `j`** but
`O_theta^{samp}` **different**), **via the Gate-A-established B2 pair (OB-20).** Take the B2
`(𝒵₊,𝒵₋)`: `O_finite^{(m)}(𝒵₊)=O_finite^{(m)}(𝒵₋)` **exactly** (the B2 collision). But `𝒵₋`
carries the off-line quartet `Q(σ₀,T)^{(R)}` at height `T` that `𝒵₊` lacks. For the **fixed**
level set, choose the B2 instance's free parameters so some `d_m∈(t_n,T]` (the heights `t_k`
and `T>t_n` are free): a level in `(t_n,T)` gives `N_{𝒵₋}(d_m)−N_{𝒵₊}(d_m)=2Σ_k n_k`; a level
just above `T` gives `2Σ_k n_k+4R≥4` (the quartet's 4 atoms, all `|Im|=T`, multiplicity `R≥1`,
are now counted). Either way `O_theta^{samp}(𝒵₊)≠O_theta^{samp}(𝒵₋)`. So an `O_finite`-collision
(exact, all `j`) is **not** an `O_theta^{samp}`-collision ⇒ **`O_theta^{samp} ⋠ O_finite`**.

**Together:** neither refines the other ⇒ `O_finite^{(K)} ⋈ O_theta^{samp}`, all `K`. Witness 1
is elementary; Witness 2 inherits B2's established exact collision — no new unaudited construction.

---

## Gate-A questions

### Q1 — Non-circularity
Confirm no RH / zero-location input: Witness 1 is elementary finite arithmetic; Witness 2
inherits the B2 collision (itself RH-free, Gate-A PASS OB-20). Confirm.

### Q2 — Map definitions well-posed
Confirm `O_theta^{samp}` is a genuine nonconstant functional of `𝒵` on a fixed level set, and
that it is correctly distinguished from Theorem G's literal constant `d_n=θ_level(n)` (which
would give `O_theta ≺ O_finite`, comparable — not the object here). Confirm `O_oracle=𝒵`.

### Q3 — Witness 1 (same-Im quartets, different `Li₁`) exact
Confirm `𝒵_a=Q(3/4,T)`, `𝒵_b=Q(9/10,T)` share the imaginary-part multiset `{±T,±T}` (equal
`O_theta^{samp}` at every level), and `Li₁(𝒵_a)≠Li₁(𝒵_b)` (at `T=10`,
`51296/2576009 ≠ 2001800/100820081`, exact). ⇒ `O_finite ⋠ O_theta^{samp}`.

### Q4 — Witness 2 (the B2 pair separates under `O_theta^{samp}`) — the load-bearing one
Confirm: the B2 pair has an exact `O_finite^{(m)}` collision (OB-20, inherited), and `𝒵₋`'s
off-line quartet at height `T` (mult `R≥1`) forces `N_{𝒵₋} − N_{𝒵₊} = 2Σn_k` (level in
`(t_n,T)`) or `2Σn_k+4R≥4` (level just above `T`), so the sampled counts differ. Confirm `R≥1`
always (B2 K3 integer scaling) and that `t_k, T` are free enough to place a fixed `d_m` in the
window. Confirm the two direction-labels are assigned correctly (one witness per direction).

### Q5 — Scope / honesty
Confirm the claim is scoped to `O_theta^{samp}` (nonconstant), that the literal-`O_theta`
comparability caveat is retained, that "lattice" is not claimed (only a preorder), and that H
adds no new analytic content beyond the elementary witnesses + the inherited B2 collision.

### Q6 — Gate-A verdict
Given Witnesses 1–2 and Q1–Q5: is `O_finite^{(K)} ⋈ O_theta^{samp}` (all K) correctly
established, non-circular, honestly scoped? May H'(i) advance PROOF-DRAFT → INDEPENDENTLY-
CHECKED for the `O_theta^{samp}` reading (with H a refinement-preorder organizing framework,
not a standalone barrier)? Or identify a specific gap (e.g. a level-placement or direction-label
error).

---

## Numerical anchor (sanity only — not an input)

- Witness 1 (exact, script-verified): same-Im quartets `Q(3/4,10)` and `Q(9/10,10)` have
  equal `O_theta^{samp}` (imaginary parts `{±10,±10}` for both) but
  `Li₁ = 51296/2576009 (=0.0199129…) ≠ 2001800/100820081 (=0.0198551…)`.
- Witness 2 (structural): `R≥1` (B2 integer scaling), quartet at height `T`; a level just
  above `T` gives a count difference `≥4R≥4`. The B2 collision itself is OB-20-established +
  OB-21-checker-replayed.
The deliverable is the Q1–Q6 judgment, not a re-run of the B2 checker.

---

## Acceptance criteria (all outcomes decisive)

1. **GATE-A PASS:** Witnesses 1–2 confirmed (direction labels fixed), Q1–Q6 answered; verdict
   "advance H'(i) for `O_theta^{samp}` to INDEPENDENTLY-CHECKED; H is a correct refinement-
   preorder framework". State any textual conditions (e.g. the direction-label cleanup).
2. **GATE-A CONDITIONAL:** correct modulo a specific fix (level-placement quantifier, a
   direction label, or the `O_theta^{samp}` definition). Give the edit.
3. **GATE-A BLOCKED:** a genuine gap (e.g. the B2 free parameters cannot place a fixed `d_m` in
   the window, or `Σn_k` and `4R` can conspire to cancel at every sampled level). Identify and
   exhibit it.

An honest "the incomparability holds for `O_theta^{samp}` via the B2 pair; H is an organizing
framework, not a standalone barrier" is a valid, first-class outcome.
