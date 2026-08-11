# Problem OB-07 — B2: Counting-Law Constraint for the Ambient Class 𝔛_sym

**Type:** analytic number theory / combinatorics (counting functions, zero distributions)  
**Non-circularity:** RH is not assumed. The sequences {γ_n} appearing below are
hypothetical zero ordinates of a multiset 𝒵 ∈ 𝔛_sym — they are NOT assumed to be
Riemann zeros. The ambient class 𝔛_sym is defined purely combinatorially (§2 below).
No Euler product, no functional equation, no ζ-related property is assumed.

---

## All definitions (self-contained — everything is here)

**Ambient class 𝔛_sym.** A locally finite multiset 𝒵 in the critical strip
{0 < Re(ρ) < 1} belongs to 𝔛_sym if:
1. Conjugation symmetry: ρ ∈ 𝒵 ⟹ ρ̄ ∈ 𝒵 (with equal multiplicity).
2. Functional-equation symmetry: ρ ∈ 𝒵 ⟹ 1−ρ ∈ 𝒵 (with equal multiplicity).
3. Admissibility: Σ_{ρ ∈ 𝒵} |ρ|^{−(1+ε)} < ∞ for some ε ∈ (0,1).

Conditions 1–3 are the ONLY conditions on 𝔛_sym. There is NO counting-law requirement
in the definition as stated in `theorems/B2-exact-collision/statement.md`.

**Counting function.** For 𝒵 ∈ 𝔛_sym, define
```
N_𝒵(T) := #{ρ ∈ 𝒵 : 0 < Im(ρ) ≤ T}    (counted with multiplicity).
```

**The Riemann–von Mangoldt counting law.** The Riemann zeta function's zero multiset
𝒵_ζ satisfies
```
N_{𝒵_ζ}(T) = (T/2π) log(T/2π) − T/2π + O(log T).
```
This is NOT assumed for general 𝒵 ∈ 𝔛_sym.

**The B2 construction.** Theorem B2 builds two multisets:
```
𝒵_+ = (M · L(t_1)) ⊔ … ⊔ (M · L(t_m)),
𝒵_- = ((M+n_1) · L(t_1)) ⊔ … ⊔ ((M+n_m) · L(t_m)) ⊔ (R · Q(3/4, T)),
```
where:
- L(t_k) = {1/2+it_k, 1/2−it_k} is an on-line conjugate pair at height t_k;
- Q(3/4, T) = {3/4+iT, 3/4−iT, 1/4+iT, 1/4−iT} is the symmetric quartet;
- M, n_k ∈ ℤ, M ≥ max_k |n_k| (buffer to keep all multiplicities ≥ 0);
- R ∈ ℤ_{>0} (a positive integer scaling factor, see §4.5 of proof.md).

The counting functions are:
```
N_{𝒵_+}(T_*) = 2mM    (exactly 2mM zeros in the upper half-strip up to height T_*).
N_{𝒵_-}(T_*) = 2Σ_k(M+n_k) + R · [# of Q-elements in upper half]
              = 2mM + 2Σ_k n_k + R,   since Q contributes 2 elements
                with Im(ρ) = T to the upper-half count.
```
So:
```
N_{𝒵_-}(T_*) − N_{𝒵_+}(T_*) = 2Σ_k n_k + R.
```

This is typically a large positive integer, so:
```
N_{𝒵_-}(T) ≠ N_{𝒵_+}(T)   for T near T_*.
```

**Observation map and Σ' convention.** For a test function φ_j and 𝒵 ∈ 𝔛_sym, define
the Weil symmetric summation over each orbit {ρ, ρ̄, 1−ρ, 1−ρ̄}:
```
O_j(𝒵) := Σ_{ρ ∈ 𝒵, Im(ρ)>0} [φ_j(ρ) + φ_j(ρ̄) + φ_j(1−ρ) + φ_j(1−ρ̄)].
```
For an on-line pair L(t) = {1/2+it, 1/2−it} with t > 0: since 1−ρ = 1/2−it = ρ̄, the
four terms reduce to 4 Re φ_j(1/2+it). For the off-line quartet Q = {3/4+iT, 3/4−iT,
1/4+iT, 1/4−iT}, the four orbit elements are all already in Q, so O_j(Q) = sum of φ_j
over all four elements = 4 Re[φ_j(3/4+iT) + φ_j(1/4+iT)].

**The observation map:**
```
O_Φ : 𝔛_sym → ℝ^m,   O_Φ(𝒵) = (O_j(𝒵))_{j=1}^{m}.
```

**The paper-A theorem statement.** Paper A claims: for any FIXED finite test family Φ
(m tests), there exist 𝒵_+ ∈ 𝔛_sym (P = 1) and 𝒵_- ∈ 𝔛_sym (P = 0) with
O_Φ(𝒵_-) = O_Φ(𝒵_+) exactly.

**Question about 𝔛_sym definition.** The definition of 𝔛_sym above has NO counting-law
requirement. However, the program §7.B.3 and related discussions mention:
> "the ambient class requires exact O(log T) counting"
as a potential additional constraint. If 𝔛_sym were to require
```
N_𝒵(T) = (T/2π) log(T/2π) − T/2π + O(log T)   (*)
```
then the B2 construction would fail: 𝒵_- adds O(1) zeros vs 𝒵_+, giving
N_{𝒵_-}(T) = N_{𝒵_+}(T) + O(1), but the difference in SHAPE between 𝒵_+ (finitely
many zeros at bounded heights) and the required T log T growth would be violated.

---

## The claims to be verified

### Claim A: Does the stated 𝔛_sym include or exclude (*)?

The current definition of 𝔛_sym (conditions 1–3 above) does NOT include the counting
law (*). Therefore:
- 𝒵_+ as constructed (finite multiset, M copies of each on-line pair) is in 𝔛_sym as
  defined (conditions 1–3 are trivially satisfied for a finite multiset).
- 𝒵_- as constructed is also in 𝔛_sym (finite modification of 𝒵_+).
- The B2 theorem holds within 𝔛_sym as defined.

**Claim A.** Under the stated definition of 𝔛_sym (conditions 1–3 only), the B2
construction gives valid members 𝒵_+, 𝒵_- ∈ 𝔛_sym. The counting-law (*) is NOT
required for membership in 𝔛_sym, and the absence of (*) is not a gap in the proof.

**What to verify for Claim A:**
1. Confirm that conditions 1–3 as stated are sufficient for 𝒵_+, 𝒵_- to be in 𝔛_sym.
   (Both are finite multisets, so conditions 1–3 are trivially satisfied.)
2. Is there any mathematical reason why the ambient class for the obstruction theorem
   should additionally require (*)? Specifically: does the information obstruction
   claim (that O_Φ does not determine P) become trivial or vacuous if 𝔛_sym is
   too large (e.g., contains degenerate finite multisets)?

### Claim B: Counting-law balancing step

If a future version of Paper A requires 𝔛_sym to satisfy (*), the B2 construction
would need modification. The proof.md §7 says:
> "If the ambient class requires exact O(log T) counting, an additional balancing
> step is needed (moving more on-line atoms to compensate). This is left for refinement."

**Claim B.** Assume 𝔛_sym is augmented to require (*). Determine whether the B2
construction can be modified to give 𝒵_+, 𝒵_- ∈ 𝔛_sym^{(*)} (the augmented class)
while maintaining the exact observation collision O_Φ(𝒵_-) = O_Φ(𝒵_+).

*Sketch of a potential fix.* Instead of a finite multiset, take
```
𝒵_+' := the Riemann zero multiset 𝒵_ζ  (assuming RH for construction only, or use
          a "dummy" multiset with the right counting law).
```
Then modify tail zeros as in E-neg (perturbing high zeros). The collision would use
the same Vandermonde argument as E-neg §3 plus the B2 quartet-cancellation argument.

*Problem:* the "dummy" multiset approach requires knowing a specific multiset with
the right counting law AND satisfying conditions 1–3. The simplest example would be
a uniformly spaced approximation: 𝒵_+ = {±i·(2πn/log n) : n ≥ 1} (Gram approximation
to zero ordinates). Does this satisfy admissibility (condition 3)? Verify Σ |ρ|^{-(1+ε)} < ∞
for ρ ~ i·(2πn/log n).

**What to verify for Claim B:**
1. Confirm that 𝒵_ζ (the Riemann zero multiset, assuming RH) satisfies conditions 1–3.
   (This is standard: the Riemann zeros are in the critical strip, Σ |γ_n|^{-2} < ∞.)
2. Determine whether the B2 quartet-plus-compensating-pairs construction can be applied
   to an infinite base multiset (like 𝒵_ζ) rather than the finite 𝒵_+.
3. If the base is infinite: does the IFT argument of proof.md §4 still give a finite
   number of on-line adjustments? (The Vandermonde rank argument of §4.3 uses exactly
   m free parameters; with an infinite base, adjusting m of them should still work.)
4. Is the counting-law condition necessary at all for the obstruction? The key claim
   (O_Φ does not determine P) needs only the collision to exist; the counting law is
   a naturality/non-degeneracy condition, not a mathematical necessity.

### Claim C: Scope of Paper A under the two possible definitions

**Claim C.** Determine which of the following two formulations of the ambient class
gives the strongest and most publishable result:

(I) 𝔛_sym without (*): the theorem holds, but critics may object that the class is
    too large (finite multisets are degenerate).

(II) 𝔛_sym with (*): the theorem would be stronger and more natural, but the B2
     construction needs modification.

Determine whether (II) is achievable with a modification that does not require
assuming RH (the modification cannot use 𝒵_ζ as the base, since that would
make the construction conditional on RH).

---

## Proof skeleton to be closed

### Step 1 — Verify Claim A (current construction is valid in 𝔛_sym as defined)

Straightforward: finite multisets satisfy conditions 1–3 trivially. State this as a
clean lemma and confirm it.

### Step 2 — Assess whether (*) should be in 𝔛_sym (Claim C)

This is the key design question. Two considerations:
(a) If 𝔛_sym without (*) is used, is there a "trivial" counterexample that makes the
    theorem vacuous? (E.g., can one always collide two finite multisets trivially,
    without using the test family at all?)
(b) If so, a counting-law requirement makes the theorem more substantive.

**Concrete test:** can one find 𝒵_- (P=0) and 𝒵_+ (P=1), BOTH FINITE, with
O_Φ(𝒵_-) = O_Φ(𝒵_+), WITHOUT any reference to the Li coefficients or the
Vandermonde argument? For instance, 𝒵_+ = {3/4 + i, 3/4 − i, 1/4 + i, 1/4 − i}
(which has P=0 since Re=3/4≠1/2). Take 𝒵_- = {1/2+i√2, 1/2−i√2, 1/4+iT, ...}.
The question is whether a trivial collision is possible for ARBITRARY Φ.

### Step 3 — Counting-law balancing (Claim B, if needed)

If the reviewer determines (*) is necessary, sketch the minimal modification to the
B2 construction that achieves 𝒵_+ ∈ 𝔛_sym^{(*)} without assuming RH.

---

## Acceptance criteria

1. **CONFIRMED-NO-CHANGE**: the current definition of 𝔛_sym (without counting law)
   is adequate for a non-trivial obstruction theorem; Claim A holds; no modification needed.

2. **CONFIRMED-AUGMENT**: the counting law (*) should be added to 𝔛_sym; Claim B
   gives a modification of the B2 construction that works; the theorem statement is
   strengthened.

3. **PARTIAL**: Claim A is confirmed (current construction valid), but the reviewer
   identifies a naturality concern with the finite-multiset ambient class, with a
   suggested strengthening.

4. **BLOCKING-GAP**: without (*), the theorem is vacuous or trivially achievable
   (non-vacuity fails); the B2 construction requires modification; no clean fix is
   available without additional tools.

All outcomes are decisive. "The current definition might be ok" is not CONFIRMED.

---

## Numerical anchor (sanity only — not an input)

For m = 1, φ_1(ρ) = 1/ρ (Li coefficient λ_1). Using the Σ' convention defined above:

For 𝒵_+ = {1/2+i, 1/2−i, 1/2+2i, 1/2−2i} (two on-line pairs at t=1, t=2):
```
O_1(𝒵_+) = 4 Re(1/(1/2+i)) + 4 Re(1/(1/2+2i))
           = 4 · [1/2/(1/4+1)] + 4 · [1/2/(1/4+4)]
           = 4 · [2/5] + 4 · [2/17]
           = 8/5 + 8/17 = (136 + 40)/85 = 176/85.
```

For a quartet Q(3/4, T=1) = {3/4+i, 3/4−i, 1/4+i, 1/4−i}:
```
O_1(Q) = 4 · [Re(1/(3/4+i)) + Re(1/(1/4+i))]
        = 4 · [3/4/(9/16+1) + 1/4/(1/16+1)]
        = 4 · [3/4 · 16/25 + 1/4 · 16/17]
        = 4 · [12/25 + 4/17] = 4 · (204+100)/425 = 1216/425.
```

Both values match the sanity check in the B2 proof (proof.md §4.5): d_1(T=1) = 1216/425.
For m=1 with C_{11} = 4(1−T_1(x_1)) and one on-line pair, the counting-law check is:
N_{𝒵_-}(1+ε) = 2(M+n_1) + 2 (the two Q-elements with Im > 0), a finite integer.
If (*) requires growth T log T, these finite multisets do not satisfy it.
