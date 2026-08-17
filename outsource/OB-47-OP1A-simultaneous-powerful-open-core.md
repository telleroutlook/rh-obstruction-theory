# Problem OB-47 — Simultaneous powerful-away-from-5 Gaussian norms: the open core

**Type:** arithmetic / Diophantine (powerful integers, Gaussian UFD, quadratic
norms, S-unit equations)

**Non-circularity.** Purely finite arithmetic. No RH, no zero of `ζ`, no
L-value, no analytic zero-counting, no fitted ordinate. RH is `[OUT]`.

**Relation to OB-46.** This problem is the residual open core after the OB-46
review established three unconditional invariants (§2 below) and identified the
dead ends (§4). The proved lemmas are free to use without re-proof.

---

## 1. All definitions

An integer `X ≥ 1` is **powerful** if every prime `p | X` satisfies `p² | X`.

An integer `X ≥ 1` is **powerful away from 5** if every rational prime `p ≠ 5`
dividing `X` satisfies `p² | X`. No condition is imposed on `v₅(X)`.

Fix integers `a, n` satisfying the **off-line Row-3 conditions**:
```
n even,  n ≥ 4,  3 ∤ n;
a odd,   1 ≤ a < n;
gcd(a, n) = 1.
```
Define primitive Gaussian integers and their rational norms:
```
w₊ = a + ni,        A₊ = |w₊|² = a² + n²,
w₋ = (a−n) + ni,    A₋ = |w₋|² = (a−n)² + n².
```
Write `N = A₊ A₋`. Both `w₊` and `w₋` are primitive (gcd of real and imaginary
parts is 1) because `gcd(a, n) = gcd(a−n, n) = 1`.

For a rational prime `p ≡ 1 (mod 4)` splitting as `p = πₚ π̄ₚ` in `ℤ[i]`,
primitivity forces at most one of `πₚ, π̄ₚ` to divide `w₊`, so
`vₚ(A₊) = v_{πₚ}(w₊)`.  Consequently:
```
A₊ powerful away from 5
  ⟺  w₊ is powerful away from the Gaussian primes (1±2i) over 5
      (every Gaussian prime 𝔭 ∤ 5 dividing w₊ divides it to multiplicity ≥ 2).
```
Same equivalence holds for `A₋` and `w₋`.

---

## 2. Free lemmas (proved unconditionally — use without re-proof)

**Lemma 1 (gcd).** `gcd(A₊, A₋) ∈ {1, 5}`.  
*Proof sketch.* Any common prime `p` must divide `A₊ − A₋ = n(2a−n)` and
satisfy `p ∤ n` (else `p | gcd(a,n) = 1`). Then `p | 5a²`, forcing `p = 5`.
The common 5-adic valuation is at most 1.

**Lemma 2 (3 ∤ N).** `3 ∤ A₊` and `3 ∤ A₋` for every Row-3 pair.  
*Proof sketch.* `3 ∤ n` (Row-3 condition), so `n² ≡ 1 (mod 3)`. If `3 | a`:
`A₊ ≡ 1, A₋ ≡ 2 (mod 3)`. If `3 ∤ a`:
`A₊ ≡ 2 (mod 3)`; `A₋ ≡ 1` or `2 (mod 3)` depending on `a mod n mod 3`.
Neither factor is 0 mod 3.

**Lemma 3 (prime residues).** Every rational prime `p | N` satisfies
`p ≡ 1 (mod 4)`. In particular `2 ∤ N` and `3 ∤ N`.  
*Proof sketch.* Since `a` is odd and `n` is even, `A₊ ≡ 1 (mod 2)`. For an
odd prime `p | a² + n²` with `p ∤ n` (forced by `gcd(a,n) = 1`): the
congruence `(a/n)² ≡ −1 (mod p)` requires `−1` to be a quadratic residue mod
`p`, hence `p ≡ 1 (mod 4)`.

**Lemma 4 (8-adic).** `A₊ ≡ A₋ (mod 8)`, both congruent to `1` or `5 (mod 8)`.  
*Proof sketch.* `a²≡1 (mod 8)` (a odd); `n²≡0` or `4 (mod 8)` (n even);
`(a−n)²≡1 (mod 8)` (a−n odd). Adding gives `A₊ ≡ A₋ (mod 8)`.

**Lemma 5 (5-adic automatic in ℱ₅).** If `5 | A₊` and `5 | A₋` (which happens
exactly when `a ≡ n−a (mod 5)`, i.e., `2a ≡ n (mod 5)`), then
`v₅(N) = v₅(A₊) + v₅(A₋) ≥ 2`, so the 5-adic powerfulness condition for `N`
is automatic. The remaining requirement is that `A₊` and `A₋` are both
powerful away from 5.

**Lemma 6 (shift identity).** `A₊ − A₋ = n(2a−n)`.

---

## 3. The exact open question

> **Core question.** Does there exist an off-line Row-3 pair `(a, n)` for which
> `A₊` and `A₋` are **simultaneously** powerful away from 5?

By Lemmas 1 and 5, this is equivalent to asking whether `N = A₊ A₋` is ever
powerful on the Row-3 family.

Equivalently (via the Gaussian formulation): are there two primitive Gaussian
integers `w₊ = a + ni` and `w₋ = (a−n) + ni` on the same horizontal line,
differing by the real shift `w₊ − w₋ = n`, both powerful away from the
Gaussian primes `(1±2i)`?

---

## 4. Known dead ends — do not resubmit

**D1 (Faltings / Darmon–Granville inapplicable).** Substituting the powerful
factorization `A₊ = 5^{e₁} u₁² v₁³` and `A₋ = 5^{e₂} u₂² v₂³` into
`A₊ − A₋ = n(2a−n)` yields a system of 2 equations in 5 unknowns
`(a, u₁, v₁, u₂, v₂)`. For fixed `n` this defines a **3-dimensional algebraic
variety** (a 3-fold), not a curve. Faltings' theorem and Chabauty apply to
curves (`dim = 1`) only. Bombieri–Lang would be needed for the 3-fold, and that
conjecture is unproved.

**D2 (abc over ℚ or ℚ(i) is trivial).** For the Row-3 abc triple
`(A₋, n(2a−n), A₊)`, the powerful hypothesis gives
`rad(A₊ A₋) ≤ 25√N ≍ n²`, so the abc bound reads `n² ≪ (n³)^{1+ε}`, which is
trivially satisfied for all `n ≥ 1`. No upper bound on `n` is obtained.

**D3 (Local congruences alone are insufficient).** For every prime-power
modulus `p^k` checked so far (including `p = 3, 7, 11, 13, 17, 19, 23, 29,
31, 37, 41, 43, 47` and `k ≤ 3`), there exist residue classes in which Row-3
conditions are satisfied and both `A₊` and `A₋` avoid having any specific small
prime as a first-power divisor. A purely local argument cannot close the
problem.

---

## 5. Proof targets (decreasing strength)

**T1 (Full).** Prove that no Row-3 pair has both `A₊` and `A₋` powerful away
from 5.

**T2 (All-but-finite).** Prove that at most finitely many Row-3 pairs have both
`A₊` and `A₋` powerful away from 5. Specify an effective height bound.

**T3 (Positive-density infinite subfamily).** Prove the simultaneous condition
fails for a positive-density subfamily of Row-3 pairs (with the density
convention stated explicitly).

**T4 (Primitive divisor in ℤ[i]).** Prove that for all but finitely many Row-3
pairs, `w₊ = a + ni` has a Gaussian prime `𝔭 ∤ 5` with `v_𝔭(w₊) = 1`. This
implies `A₊` is not powerful away from 5 for those pairs and closes the problem
one-sided.

**T5 (Conditional strategy).** Give a proof route that closes under a named
unproven conjecture (e.g., abc over ℚ(i) with an explicit exponent below 3,
Szpiro for elliptic curves over ℚ(i), Bombieri–Lang for the 3-fold), stating
the precise conjecture, the implied constant, and how the 5-adic exceptional
branches are handled.

---

## 6. Suggested proof approaches (not yet tried)

### Approach A — S-unit equations over ℤ[i]

Write `w₊ = (1+2i)^{f₁}(1−2i)^{g₁} ξ₊²` and `w₋ = (1+2i)^{f₂}(1−2i)^{g₂} ξ₋²`
in ℤ[i] (ignoring cube factors for the sketch; the full case includes a "`v³`"
component). The shift identity `w₊ − w₋ = n` becomes
```
(1+2i)^{f₁}(1−2i)^{g₁} ξ₊² − (1+2i)^{f₂}(1−2i)^{g₂} ξ₋² = n.
```
For each fixed tuple `(f₁, g₁, f₂, g₂) ∈ {0,1}⁴` (only finitely many 5-adic
types), this is an **S-unit equation over ℤ[i]** with `S = {(1+2i),(1−2i)}`.
By Evertse–Schlickewei–Schmidt (or the Gaussian analogue of Thue–Mahler for
norm forms), the number of solutions in `(ξ₊, ξ₋)` is finite for each fixed
`n`. The task is to turn this into a uniform bound over all `n`.

*What is needed:* a version of Evertse's S-unit theorem over ℤ[i] that gives
a bound on the height of `ξ₊, ξ₋` in terms of `n`, rather than just
finiteness for each fixed `n`.

### Approach B — Thue–Mahler / norm-form equations for fixed n

For fixed `n` and `eᵢ ∈ {0, 1}`, the equation `a² + n² = 5^{eᵢ} s²`
(simplest case: powerful = perfect square times 5-power) is a **norm equation**
in ℤ[i]:
```
N(a + ni) = 5^{eᵢ} s²  ⟹  a + ni = (1±2i)^{eᵢ} · α²
```
for some `α ∈ ℤ[i]` with `N(α) = s` and `gcd(α, 5) = 1`. Taking real parts
gives `a = Re[(1±2i)^{eᵢ} α²]`, a degree-2 polynomial equation in
`Re(α), Im(α)`. **For fixed `n`**, the constraint that both `a² + n²` and
`(a−n)² + n²` have this form simultaneously defines an intersection of two
genus-1 curves (for each fixed `n` and `eᵢ` tuple), which by Faltings has
finitely many rational points. The task is to carry this out for the general
"powerful" case (not just "square times 5-power"), where the parametrization is
`w₊ = (1±2i)^{f} u₊² v₊³`.

*What is needed:* handle the `v³` cube factor, which elevates degree from 2 to
5 in the unknowns and changes the curve genus calculation.

### Approach C — Primitive divisors via Gaussian Zsygmondy

For fixed `n`, the Gaussian integers `w₊(a) = a + ni` for varying odd `a` with
`gcd(a, n) = 1` form a set of primitive Gaussian integers. A **primitive
divisor theorem** for this family would assert: for all but finitely many `a`,
`w₊(a)` has a Gaussian prime factor `𝔭` (over a prime `p ≡ 1 (mod 4)`,
`p ≠ 5`) that does not divide `w₊(a′)` for any previously encountered `a′`.
Such a primitive prime appears to exactly first power and immediately prevents
`A₊(a)` from being powerful away from 5. Bilu–Hanrot–Voutier proved primitive
divisor theorems for Lucas and Lehmer sequences; an analogous statement for
shifted-norm families `{|a + ni|² : a ∈ ℤ}` is not in the literature but is
plausible.

*What is needed:* a primitive divisor theorem for the family
`{a + ni : a odd, gcd(a,n) = 1}` in ℤ[i], uniform in `n`.

### Approach D — Powerful-gap lower bound

If `A₊` and `A₋` are both powerful away from 5 with `A₊ > A₋`, the gap is
```
A₊ − A₋ = n(2a−n),  with  |A₊ − A₋| < n² ≈ A₋.
```
Classical powerful-gap theorems (Molsen 1939, Golomb 1970; conditional on abc:
Granville 1998) give lower bounds for the gap between consecutive powerful
integers. For the unconditional bound: any two consecutive powerful integers
`m, m+k` satisfy `k ≥ m^{1/2}/2` approximately (Størmer / Pillai), though this
applies to `m+1`-type gaps. Under abc, for any `k ≥ 1` there are only finitely
many powerful pairs `(A, A+k)`. Here `k = n(2a−n)` is variable, so a direct
application requires bounding both `A₋` and `k` together.

*What is needed:* a powerful-gap bound that applies when the gap itself scales
as `k ≍ A₋` (rather than `k` being fixed), possibly via a more careful abc
application over ℤ[i] with explicit exponents.

---

## 7. Acceptance criteria

Return exactly one of the following.

**CONFIRMED.** A full unconditional proof that no Row-3 pair has both `A₊` and
`A₋` powerful away from 5.

**PARTIAL.** A proved all-but-finite (T2), positive-density (T3), or primitive-
divisor (T4) result. State the exact family, the effective height bound, and
how the 5-adic branches are handled.

**REFUTED.** An explicit off-line Row-3 pair `(a, n)` with both `A₊` and `A₋`
powerful away from 5. Provide the complete prime factorizations of `A₊`, `A₋`,
and `N`.

**STRATEGY.** A concrete proof route for one of T1–T4. It must identify:
- the main tool and its precise statement;
- which sublemmas are standard and which are new;
- how the cube-factor ("`v³`") component in the powerful parametrization is
  handled;
- how the 5-adic branches `(e₁, e₂) ∈ {(0,0),(0,2),(2,0),(1,1),(1,k≥2)}` are
  covered.

**INCONCLUSIVE.** A precise localization: which step in which approach (A, B,
C, or D) fails, and what new theorem would be required to complete it.

---

## 8. Numerical evidence (sanity only — not a proof input)

Exact scan of `4 ≤ n < 5000`, `n` even, `3 ∤ n`, `1 ≤ a < n`, `a` odd,
`gcd(a, n) = 1`:

```
Total Row-3 pairs:                    1,898,236
A₊ powerful away from 5:               633
A₋ powerful away from 5:               633
Both simultaneously:                      0
```

The 633 single-factor cases are all isolated; no pair achieves both. Reproduced
by `checker/ob44a_factorization_scan.py` (exact arithmetic).

**Numerical anchor** (sanity check, not a premise):
```
a = 19,  n = 22:
  A₊ = 845 = 5 · 13²   (powerful away from 5: yes)
  A₋ = 493 = 17 · 29   (powerful away from 5: no)
```
A₊ is a single-factor witness; A₋ has two simple primes, so the simultaneous
condition fails here.

---

## Pre-send lint record

| PROMPT_LINT item | Result |
|---|---|
| L1–L4 | N/A: no entire-function, canonical-product, or analytic zero-location claim. |
| L5 | PASS: no RH, no zero of ζ, no γ_n. Domain defined by explicit arithmetic conditions. |
| L6 | PASS: REFUTED and INCONCLUSIVE are first-class outcomes. |
| L7–L16 | PASS/N/A: no counting factor, no growth-ray, no Fourier multiplier, no Fredholm, no representation-invariant claim. |
| L17 | PASS: free lemmas are proved in-file (§2). Dead ends D1–D3 each cite a specific reason. Approaches A–D state exactly what is needed without asserting it is proved. |
| L18 | PASS: numerical anchor in §8 is labeled sanity only and not a proof input. |
| L19 | PASS: PARTIAL, STRATEGY, and INCONCLUSIVE are all accepted outcomes. |
| L20–L24 | N/A. |
| Self-containment | PASS: powerful / powerful-away-from-5, Row-3 conditions, A₊/A₋/N, Gaussian equivalence, all lemmas with proofs, dead ends, approaches, criteria, and anchor are defined in-file. |
| Privacy | PASS: no personal path, username, company, or internal host. |
