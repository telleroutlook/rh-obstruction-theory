# Problem OB-26 — C Gate-A package: independent review of the finite-Euler-factor non-forcing theorem

**Type:** Gate-A independent mathematical review (whole-theorem inspection, scoped).

**What this is.** A request to **independently inspect Theorem C** — fixing finitely many
Euler factors of a Helson zeta function to the standard value `χ(p)=1` does not force its
zeros onto the critical line — as a coherent whole, and issue a **Gate-A verdict**: is it
correct, self-contained, non-circular, RH-free, does its one load-bearing citation
(Andersson 2024, Theorem 5) genuinely cover the object used, and — the crux for this
theorem — **is its own added content a materially new result or a one-paragraph corollary
of Andersson?** Unlike the sibling theorems (B1/B2/D/G), C is not self-contained analysis:
it imports one big external theorem and adds a short finite-factor argument. The review
must judge both the import and the increment.

**Non-circularity (mandatory, and unusually delicate here).** RH is not assumed and must
not be used. Two specific traps to confirm are avoided:
  - **(i)** Andersson's Theorem 5 is itself **unconditional** (the source explicitly
    contrasts with Seip / Bochkov–Romanov, whose `1/2<Re(s)<1` results are conditional on
    RH; Andersson's holds on the full `Re(s)<1` unconditionally). Confirm no conditional
    variant is invoked.
  - **(ii)** The `P=1` side of the target must **not** be instantiated by the Riemann `ζ`
    itself: "`ζ` has all zeros on the critical line" **is** RH. Confirm the theorem's
    obstruction does not secretly require a known-`P=1` companion whose `P=1` is RH-equivalent
    (see Q3 — this is the subtle target-structure question).

---

## All definitions (self-contained — everything is here)

### Helson zeta functions (the ambient class)
For a completely multiplicative function `χ : ℕ → ℂ` with `|χ(p)| = 1` for every prime `p`
(equivalently `χ(p) ∈ 𝕋`, the unit circle, extended completely multiplicatively), define
the formal Euler product
```
ζ_χ(s) = Π_p (1 − χ(p) p^{-s})^{-1},      convergent for Re(s) > 1,
```
with meromorphic continuation to a region (Helson class; Helson 1954, Bayart 2002,
Andersson 2024 §1). The single Euler factor is `L_p(s,χ) = (1 − χ(p)p^{-s})^{-1}`.

### `P₀`-standardness (the observation)
Fix a cutoff `P₀ > 0`. Call `χ` (and `ζ_χ`) **`P₀`-standard** if `χ(p) = 1` for all primes
`p ≤ P₀` — i.e. it agrees with the Riemann `ζ` on its first `π(P₀)` Euler factors. The
**observation map** of the method class is `O(ζ_χ) = (χ(p))_{p ≤ P₀}` (the first `π(P₀)`
Euler-factor data); a `P₀`-standard function has `O = (1,1,…,1)`.

### Target predicate
```
P(ζ_χ) = 1   ⟺   every nontrivial zero of ζ_χ in its continuation region
                  lies on the critical line Re(s) = 1/2.
```

### The finite-factor modifier
For a Helson `χ` and cutoff `P₀`, define
```
R(s) = R(s; P₀, χ) := Π_{p ≤ P₀}  L_p(s,1) / L_p(s,χ)
                    = Π_{p ≤ P₀}  (1 − χ(p) p^{-s}) / (1 − p^{-s}).
```
**Orientation (load-bearing — verify):** the numerator carries `χ(p)`, the denominator is
the standard factor. `R` is a **ratio of two finite Euler products**, meromorphic on `ℂ`;
it is *not* a Dirichlet polynomial (the `(1−p^{-s})` factors are inverted), so no
"degree `≤ P₀^{1/2}`" bound applies. Its role: `ζ_χ · R` replaces the `p ≤ P₀` Euler
factors of `ζ_χ` by the standard ones,
```
ζ_χ̃(s) := ζ_χ(s) · R(s)
        = [Π_{p>P₀} L_p(s,χ)] · [Π_{p≤P₀} L_p(s,χ)] · Π_{p≤P₀} L_p(s,1)/L_p(s,χ)
        = [Π_{p>P₀} L_p(s,χ)] · [Π_{p≤P₀} L_p(s,1)],
```
i.e. `ζ_χ̃ = ζ_χ̃` with `χ̃(p) = 1` for `p ≤ P₀` and `χ̃(p) = χ(p)` for `p > P₀`. Since `χ̃`
is completely multiplicative and unimodular, `ζ_χ̃` is itself a **Helson** zeta function.

### Allowed premise (source-verified / Gate-A CLEARED)
**Andersson 2024, Theorem 5** (arXiv:2408.15713, LaTeX label `thm5`; source-verified in
`baseline/andersson-2408.15713/`, see `PROVENANCE.md`), transcribed verbatim:

> Let `U ⊆ ℂ` be an open connected set containing the half plane `Re(s) > 1` and let
> `𝒵 ⊂ U ∩ {s : Re(s) < 1}` be any signed multiset without limit points on `U ∪ (1+iℝ)`.
> Then there exists a completely multiplicative unimodular function `χ` such that the Helson
> zeta-function `ζ_χ(s)` has meromorphic continuation from `Re(s) > 1` to `U` with
> prescribed poles and zeros with given multiplicities from `𝒵`. Furthermore we may choose
> `χ` such that the maximal domain of meromorphicity is `U`.

(Unconditional. Improves Seip / Bochkov–Romanov, whose `Re(s)>1/2` versions need RH.)

---

## The claimed theorem (C)

**Theorem C.** For every finite prime cutoff `P₀` and every point `z₁` with
`0 < Re(z₁) < 1`, `Re(z₁) ≠ 1/2`, there exists a `P₀`-standard Helson zeta function `ζ_χ̃`
with a zero at `z₁` (hence `P(ζ_χ̃) = 0`).

**Consequence (the obstruction).** No criterion depending only on the first `π(P₀)` Euler
factors — i.e. any predicate that is a function of `O(ζ_χ) = (χ(p))_{p≤P₀}` alone — can force
all zeros of a Helson zeta function onto the critical line: the `P₀`-standard fiber
`O⁻¹(1,…,1)` contains an object with `P = 0`.

**Method (three steps).**
- **Step 1 (import).** Apply Andersson Thm 5 with `U = ℂ`, `𝒵 = {z₁}` (a single simple
  zero, trivially no limit points): get a Helson `ζ_χ` with a prescribed zero at `z₁`.
- **Step 2 (modify).** Form `ζ_χ̃ = ζ_χ · R(s; P₀, χ)`, making it `P₀`-standard.
- **Step 3 (preserve).** `R` is holomorphic and nowhere zero on the open strip
  `0 < Re(s) < 1` (its zeros and poles all lie on `Re(s) = 0`), so `R(z₁) ≠ 0` and the zero
  at `z₁` survives in `ζ_χ̃`.

---

## Links to inspect

**Link A (citation covers the object).** Andersson Thm 5 with `U=ℂ`, `𝒵={z₁}`: confirm the
hypotheses are met (single-point signed multiset in `ℂ ∩ {Re(s)<1}`, no limit points on
`ℂ ∪ (1+iℝ)`) and the conclusion delivers a **completely multiplicative unimodular** `χ`
with a genuine **zero** (not pole) at `z₁`. Confirm the theorem number/label (**Theorem 5**,
`thm5`) and that Theorems 1–4 are not what is needed. **Confirm** the import is legitimate,
unconditional, and not a misread of an RH-conditional variant.

**Link B (multiplier orientation and telescoping).** Verify the algebraic identity
`ζ_χ · R = ζ_χ̃` with `χ̃(p)=1` for `p≤P₀`, and specifically the **orientation**
`R = Π(1−χ(p)p^{-s})/(1−p^{-s})` (numerator carries `χ`). A sign/inversion error here
(writing `(1−p^{-s})/(1−χ(p)p^{-s})`) would make `ζ_χ·R` replace factors in the wrong
direction. **Confirm** the orientation is correct by expanding `L_p(s,1)/L_p(s,χ)`.
(Sanity anchor, already script-checked: at `s=0.7+3i`, `P₀=3`, `χ(2)=i`, `χ(3)=e^{i}`, the
ratio `ζ_χ̃/ζ_χ` equals `Π(1−χ(p)p^{-s})/(1−p^{-s})` to machine precision and differs from
the inverted form.)

**Link C (zero-freeness of `R` on the open strip — no cancellation).** Each factor
`(1−χ(p)p^{-s})/(1−p^{-s})` has numerator zeros where `χ(p)p^{-s}=1` and denominator zeros
(poles of the factor) where `p^{-s}=1`; since `|χ(p)|=1`, both force `p^{-Re(s)}=1`, i.e.
`Re(s)=0`. So **all zeros and poles of `R` lie on `Re(s)=0`**, and `R` is holomorphic and
nowhere zero on the open strip `0<Re(s)<1`. **Confirm** this, and confirm the corollary:
the earlier "critical issue — `R` may vanish near `z_j`, so push `Im(z_j)` large" is a
**pseudo-problem** now removed; `R(z₁)≠0` holds automatically for every `z₁` in the open
strip.

**Link D (`ζ_χ̃` is Helson, so `P` is well-defined on it).** `χ̃` (=1 for `p≤P₀`, `=χ(p)`
for `p>P₀`) is completely multiplicative and unimodular, so `ζ_χ̃` is in the Helson class
and `P(ζ_χ̃)` is defined. Its zero at `z₁` (with `Re(z₁)≠1/2`) gives `P(ζ_χ̃)=0`. **Confirm**
the modification does not leave the class and does not (e.g. via `R`'s boundary poles at
`Re(s)=0`) disturb the zero set inside the open strip.

---

## Gate-A questions (the deliverable)

### Q1 — Hidden gap / circularity / RH-import
Does any step assume RH or a ζ-zero location? Confirm both non-circularity traps are
avoided: (i) Andersson Thm 5 is used unconditionally; (ii) the obstruction is **one-sided**
(exhibit a `P=0` object in the standard fiber) and does not smuggle in an RH-equivalent
"`P=1` companion". Confirm or exhibit the leak.

### Q2 — Non-vacuity (a serious construction is in the class)
The ambient class must contain a genuine, externally recognized object, not just the
synthetic `ζ_χ̃`. Confirm Andersson's Helson zeta functions are a serious published class
and that `ζ_χ̃` is a bona fide member (completely multiplicative unimodular coefficients,
Euler product, meromorphic continuation) — not an object rigged solely to defeat the
observation. Contrast with the L6 vacuity failure mode (atoms invisible to both observation
and predicate): here the off-line zero `z₁` is visible to `P` and the standard factors are
visible to `O`, so the two adversaries genuinely differ on `P` while sharing `O`.

### Q3 — Target structure: is one-sided enough? (the subtle one)
Theorem C exhibits a `P₀`-standard object with `P=0`. The acceptance test "the two
adversaries genuinely differ on the predicate while sharing the observation" would ideally
want **both** a `P=0` and a `P=1` object in the same fiber `O⁻¹(1,…,1)`. But a `P=1`
`P₀`-standard Helson function with **all** zeros on the line, produced **unconditionally**,
is not obviously available — and the tempting choice "`ζ` itself" has `P=1 ⟺ RH`, which is
**forbidden as a premise**. **Decide and state clearly:** is the one-sided statement ("no
function of `O` can *force* `P=1`, because the fiber contains a `P=0` object") logically
sufficient for the stated consequence, so that no `P=1` companion is needed? Or does the
information-obstruction framing require producing a `P=1` fiber-mate — in which case, can it
be done without RH (e.g. a Helson function whose zeros are *prescribed* all on the line by
Andersson Thm 5 with `𝒵 ⊂ {Re(s)=1/2}`), or is C honestly only a **one-sided**
non-forcing result? Either answer is acceptable; the deliverable is the correct framing and
the exact statement C is entitled to.

### Q4 — Citation scope and the "already in Andersson?" test
Andersson's remark (following Thm 5 in the source) notes his method can be modified so
`χ(p)` is "chosen from some finite set such that 0 is in the interior of the convex hull."
**Judge whether Andersson's construction already permits fixing finitely many `χ(p)=1`
directly** (which would make even Step 2's modification redundant), or whether the external
finite-factor ratio `R` is the genuine mechanism. Confirm the load-bearing citation is
Theorem 5 (not the fixed-finite-set remark) and that its scope (Helson class, `Re(s)<1`)
literally covers C's use.

### Q5 — Novelty honesty (the crux for C; Paper-A gate)
This is the decisive question. C = Andersson Thm 5 + a one-line zero-free finite-factor
ratio. **State honestly which holds:**
  - **(a) Corollary.** Andersson Thm 5 (possibly with his finite-set remark) directly
    yields the `P₀`-standard off-line zero; C's increment is a trivial observation. Then C
    is a **one-paragraph corollary**, to be published as a remark in Paper A, *not* marketed
    as a standalone barrier.
  - **(b) Modest but genuine increment.** The finite-factor modification is a real (if
    short) added step Andersson does not state, giving a cleanly quantified obstruction
    (observation = first `π(P₀)` factors; conclusion = no such-observation criterion forces
    `P=1`). Then C is a short standalone note or a §of Paper A.
  - **(c) Materially broader.** Only if a genuinely stronger claim is established (e.g. a
    zero at a height *bounded in terms of `P₀`*, or an extension beyond Helson) — which the
    current draft does **not** claim.
Give the verdict and the honest publication strategy. Per the repo's hard boundary, C is a
**barrier** only if method class / ambient class / observation / target / escape are all
explicit and non-vacuous; assess whether C clears that bar or is "only" a clean
non-forcing corollary.

### Q6 — Escape route and scope honesty
Confirm C's escape route is correctly stated and genuinely open: C applies to the **Helson
class** only and does **not** transfer to (i) the Selberg class (functional equation +
Ramanujan + degree axioms — EXT-4a: provably incompatible with free zero prescription),
(ii) `ζ` itself (Euler product + gamma factor + functional equation jointly), or (iii) any
combined-axiom class. Confirm the Davenport–Heilbronn comparison (functional equation
without Euler product ⇒ off-line zeros) is kept **logically separate** and not fused with C
into a single (unconstructed) object.

### Q7 — Gate-A verdict
Given Links A–D and Q1–Q6: is Theorem C a correct, self-contained (modulo its verified
citation), non-circular, RH-free result? Should its mathematical status advance from
PROOF-DRAFT toward INDEPENDENTLY-CHECKED — **and at what scope** (standalone note vs.
corollary-of-Andersson remark)? Or does a specific gap block it?

---

## Numerical anchor (sanity only — already script-checked, not an input)

Multiplier orientation, `P₀=3` (primes 2,3), `χ(2)=i`, `χ(3)=e^{i}`, `s = 0.7+3i` (inside
the strip):
- true multiplier `ζ_χ̃/ζ_χ = L_2(s,1)L_3(s,1)/(L_2(s,χ)L_3(s,χ)) ≈ 0.32009 + 0.17122 i`;
- candidate `Π(1−χ(p)p^{-s})/(1−p^{-s})` **matches** (numerator carries `χ`);
- inverted candidate `Π(1−p^{-s})/(1−χ(p)p^{-s}) ≈ 2.42908 − 1.29933 i` **does not** —
  confirming the orientation in Link B.
- zero-freeness: `min_{0.01≤Re≤0.99, |Im|≤20} |1−χ(p)p^{-s}| ≈ 0.0088 > 0` (sampled),
  consistent with all zeros/poles of `R` sitting on `Re(s)=0` (Link C).

The Gate-A deliverable is the whole-theorem judgment (Links A–D, Q1–Q7), especially the
**novelty verdict Q5**, not a re-run of these anchors.

---

## Acceptance criteria (all outcomes decisive)

1. **GATE-A PASS:** Links A–D confirmed, Q1–Q7 answered with no blocking gap; verdict
   "advance C toward INDEPENDENTLY-CHECKED", **with an explicit scope ruling** (Q5:
   standalone note vs. corollary-of-Andersson). State any required textual conditions.

2. **GATE-A CONDITIONAL:** the chain is correct but a specific textual fix is required
   (e.g. restate C as a one-sided non-forcing result per Q3; downgrade the novelty claim to
   "corollary" per Q5; fix the target framing). Give the exact edit.

3. **GATE-A BLOCKED:** a genuine gap, circularity, RH-import (e.g. a hidden `P=1`-via-RH
   companion), or citation-scope failure exists. Identify it, exhibit it, give the minimal
   repair.

An honest "the finite-factor step is correct and RH-free, but C is a one-paragraph corollary
of Andersson Theorem 5, not a standalone barrier — publish as a remark in Paper A" is a
**valid and useful result**. The goal is a truthful judgment of what C newly establishes,
not a PASS.
