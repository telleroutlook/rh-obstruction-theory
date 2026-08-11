# Problem OB-32 — H Gate-A package: independent review of the information-obstruction partial order

**Type:** Gate-A independent mathematical review (whole-theorem inspection, scoped).

**What this is.** A request to **independently inspect Theorem H (H-information-hierarchy)**
and issue a **Gate-A verdict** on **H's own increment**. H is a *unification framework*: it
places the repo's information obstructions into a structured order of observation maps. Its
two instantiations are **already Gate-A established and inherited unchanged** — the
`O_finite` obstruction is Theorem B2 (Gate-A PASS OB-20 + independent checker OB-21), and the
`O_theta` obstruction is Theorem G-info (Gate-A PASS OB-22 + independent checker OB-17). So
this review does **not** re-audit B2 or G; it targets **only what H adds**:
1. the claim that the four observation maps form a **PARTIAL order** (a lattice under
   refinement), **NOT** a strict total chain (a self-audit, OB-27, corrected an earlier false
   "`O_finite ⊂ O_theta ⊂ O_vM ⊂ O_oracle`" claim);
2. the **incomparability theorem H'(i)**: `O_finite` and `O_theta` are incomparable
   (neither refines the other), with two explicit script-verified witnesses;
3. the **coarsening H'(ii)**: `O_finite ≺ O_oracle` and `O_theta ≺ O_oracle`, each inheriting
   the exact (Gate-A-established) B2 / G collisions.

**Non-circularity (mandatory).** RH is not assumed and not used. H concerns *which
coordinates of a zero-multiset each observation map can see*; no zero location or reality
enters. Confirm no RH-import (the inherited B2/G obstructions are themselves RH-free, already
verified).

---

## All definitions (self-contained)

### Observation maps on admissible multisets
Let `𝔛_sym` be the admissible zero-multisets (symmetric under conjugation and `ρ↦1−ρ`, with
an admissibility exponent). An **observation map** is `O : 𝔛_sym → S`. A method "operates via
`O`" if its input is only `O(𝒵)`. An **information obstruction** for `(P,O)` is a pair
`(𝒵₊,𝒵₋)` with `O(𝒵₊)=O(𝒵₋)` (exact collision) but `T(𝒵₊)≠T(𝒵₋)` (target predicate
distinguishes them), neither using an RH-equivalent.

### The four maps
- `O_finite(𝒵)` = the finite vector `(Li_k(𝒵))_{k≤K}` (or `(W(φ_j))_{j≤K}`) — Li/Weil
  moments, e.g. `Li_1(𝒵)=Σ_ρ 1/ρ`. **Sees real parts** (via `1/ρ`). Used in B1, B2.
- `O_theta(𝒵)` = the archimedean/theta-level data. **Crucial subtlety (verify):** in Theorem
  G this is `d_n = θ_level(n)`, the Riemann–Siegel `θ`-unfolding levels, a **fixed,
  zero-free sequence independent of `𝒵`** (determined by the `Γ`-function, not by the
  multiset). Read literally it is *constant* as a functional of `𝒵`. Read charitably as an
  Im-part/unfolded-count functional of `𝒵`, it **sees only imaginary parts**, blind to real
  parts. Used in G.
- `O_vM(𝒵)` = full von Mangoldt explicit-formula data (`Λ(n)` for all `n`).
- `O_oracle(𝒵)` = all zero ordinates `{γ_n}` (finest).

### The target predicate
`T(𝒵)` distinguishes on-line from off-line multisets (the shared predicate of B1/B2/G).

---

## The claims to inspect (H's own increment)

**Claim 1 (partial order, NOT total chain — OB-27 correction).** The four maps form a
**partial order** under refinement (`O_a ≼ O_b` iff `O_b(𝒵)=O_b(𝒵') ⇒ O_a(𝒵)=O_a(𝒵')`):
`O_finite ≼ O_oracle`, `O_theta ≼ O_oracle`, `O_theta ≼ O_vM`, but **`O_finite` and
`O_theta` are incomparable**. An earlier draft asserted the strict total chain
`O_finite ⊂ O_theta ⊂ O_vM ⊂ O_oracle`; that is **false** and was withdrawn (OB-27).
**Confirm** the corrected structure is a partial order and the withdrawn chain is gone.

**Claim 2 (incomparability H'(i)).** Two explicit witnesses (both script-verified):
- **`O_theta` does not refine `O_finite`.** Two symmetric quartets at the same height `T`
  but different real offset — `𝒵_a` at `σ=3/4` (atoms `{3/4±iT, 1/4±iT}`) and `𝒵_b` at
  `σ=9/10` (`{9/10±iT, 1/10±iT}`) — have the **same imaginary-part multiset** `{±T,±T}`,
  hence identical `O_theta`, but **different** `O_finite`: `Li_1 = Σ_ρ 1/ρ` gives
  `0.0199129…` vs `0.0198551…` (`T=10`). So `O_theta(𝒵_a)=O_theta(𝒵_b)` while
  `O_finite(𝒵_a)≠O_finite(𝒵_b)`.
- **`O_finite` does not refine `O_theta`.** An `S(T)`-type ordinate move `γ_n→γ_n+ε_n`
  chosen in the kernel of the first `K` Li functionals (finite matching, the B1 IFT) changes
  the unfolded count, so `O_finite` collides while `O_theta` separates.
**Confirm** both witnesses, and the sharper point that if `O_theta` is read as G's fixed
zero-free sequence `d_n=θ_level(n)`, it is *constant* on multisets — it separates **nothing**
and cannot dominate `O_finite` (PROMPT_LINT L23). Either reading gives incomparability.

**Claim 3 (coarsening H'(ii)).** Both maps are strict coarsenings of `O_oracle`:
- `O_finite ≺ O_oracle`: the B2 quartet pair has `O_finite(𝒵₊)=O_finite(𝒵₋)` (exact Li
  collision, B2 §4.3 — Gate-A PASS OB-20) but distinct ordinates.
- `O_theta ≺ O_oracle`: by the S(T) gap identity (G Lemma G.2), an S(T) perturbation with
  `ε_n` bounded by `S(γ_n)/A'(γ_n)` (`A'(t)=θ'(t)/π`) preserves `O_theta` but changes the
  ordinates (Gate-A PASS OB-22).
**Confirm** part (ii) correctly inherits the exact B2/G collisions (this half rests on
established results; only part (i)'s witnesses are H's new PROOF-DRAFT content).

**Claim 4 (`O_vM` sub-cases, G-hard).** Whether `O_vM = O_oracle` or `O_vM ≺ O_oracle`
depends on the G-hard conjecture (whether von Mangoldt data recovers `S(T)`); either way the
`O_finite`/`O_theta` incomparability (Claim 2) is unaffected. **Confirm** this is stated as
conditional on G-hard (a CONJECTURE), not resolved.

---

## Gate-A questions (the deliverable)

### Q1 — Non-circularity
Confirm no step uses RH or ζ-zero location; H is about which coordinates each map sees. The
inherited B2/G obstructions are RH-free (already established).

### Q2 — Partial order, not chain (Claim 1)
Confirm the corrected structure is a partial order with `O_finite ⋈ O_theta` incomparable,
and that the withdrawn strict total chain does not reappear anywhere in the statement/proof.

### Q3 — Incomparability witnesses (Claim 2, L23)
Confirm both witnesses (same-Im pair separated by `Li_1` not `θ`; S(T) move separated by `θ`
not `Li`), and the L23 subtlety: a fixed argument-independent sequence (`d_n=θ_level(n)`) is
constant on multisets and cannot be an information layer that dominates `O_finite`. Confirm
the two maps read *different coordinates* (real parts vs imaginary-part count), hence
incomparable — not nested.

### Q4 — Coarsening inherits established results (Claim 3)
Confirm part (ii) (`O_finite`, `O_theta` ≺ `O_oracle`) correctly rests on the Gate-A-
established B2 (OB-20) and G-info (OB-22) collisions, and that H does not re-derive or weaken
them.

### Q5 — No new analytic content / no overclaim
Confirm H introduces **no new analytic content** beyond B2/G — its increment is purely the
partial-order framing + the incomparability witnesses — and that it does not overclaim (it is
a unification framework, not a new barrier; the only new mathematical assertion is
incomparability, which is elementary given the witnesses).

### Q6 — Gate-A verdict + status
Given Claims 1–4 and Q1–Q5: is H's increment correct, non-circular, and honestly scoped?
Its natural status: the inherited instantiations are INDEPENDENTLY-CHECKED (via B2/G); H's
own **incomparability theorem H'(i)** is elementary and script-witnessed — can it advance to
INDEPENDENTLY-CHECKED, with H positioned as a **unification framework / organizing section**
(e.g. in Paper A or E), not a standalone barrier? Or identify a specific gap.

---

## Numerical anchor (sanity only — not an input)

- Incomparability witness (script-checked, `T=10`): quartets at `σ=3/4` vs `σ=9/10` share
  the imaginary-part multiset `{±10,±10}` (so identical `O_theta`), but
  `Li_1 = Σ_ρ 1/ρ = 0.0199129…` vs `0.0198551…` (distinct `O_finite`). Reverse direction: an
  S(T) ordinate move in the kernel of the first `K` Li functionals keeps `O_finite` fixed
  while changing the unfolded count (`O_theta`).
The Gate-A deliverable is the whole-increment judgment (Claims 1–4, Q1–Q6), not a re-audit of
B2/G (already Gate-A PASS).

---

## Acceptance criteria (all outcomes decisive)

1. **GATE-A PASS:** Claims 1–4 confirmed, Q1–Q6 answered with no blocking gap; verdict
   "H's incomparability increment H'(i) may advance to INDEPENDENTLY-CHECKED; H is a correct
   unification framework (partial order), positioned as an organizing section not a standalone
   barrier". State any required textual conditions.
2. **GATE-A CONDITIONAL:** correct but a specific textual fix is required (e.g. sharpen the
   `O_theta` definition to fix the read, restate a coarsening). Give the exact edit.
3. **GATE-A BLOCKED:** a genuine gap, circularity, or a residue of the withdrawn total-chain
   claim exists. Identify it, exhibit it, give the minimal repair.

An honest "the incomparability increment is correct and elementary; H is a useful unification
framework but adds no new analytic content beyond B2/G; publish as an organizing
section/appendix, not a standalone result" is a valid, first-class outcome.
