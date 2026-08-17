# Problem OE-05 — NT-C: Cube-Factor Powerful Obstruction for Row-3

**Type:** Pure arithmetic / Diophantine geometry
**Non-circularity:** All hypotheses are elementary: even integers, odd integers, gcd,
norms in ℤ[i]. No zeros of ζ, no RH, no Li coefficients, no ordinates are assumed.
RH stays `[OUT]`.

**What is already established at the repository evidence level (do not re-prove):**
- **Theorem L** (this repo): no Row-3 pair has both A⁺ and A⁻ perfect squares.
- **Theorem M** (this repo): no Row-3 pair has both A⁺ and A⁻ of the form 5^e · m²
  (the t=1 square-based powerful case). Status `PROOF-DRAFT`: elementary congruences
  plus 2-isogeny descent on E: Y²=X³−32X+64; an independent CAS descent check remains
  a Gate-A gap.

**Returned-feedback status (2026-08-17):** the bounded-support/Baker reply is
**NOT ESTABLISHED / INCONCLUSIVE**. It conflates a fixed actual support set with
`|S|<=M` and does not control the heights entering Matveev's theorem. The audit is
recorded in `outsource/solutions/OE-05-cubefactor-feedback-review.md`; exact scope
checks are in `checker/audit_OE03_OE05_feedback.py`.

**Second returned-feedback status (2026-08-17):** the biquadratic/fixed-j/twist reply
is **REJECTED**. Exact checks refute both claimed pencil determinants; the supplied
Weierstrass model has `j=98784/53`, not `148176/25`; and it has no rational 2-torsion,
so the proposed `x mod squares` descent is invalid. See
`outsource/solutions/OE-05-biquadratic-feedback-review.md`.

**This problem:** the t≥2 cube-factor case that Theorems L and M do not cover.

---

## All definitions (self-contained)

**Row-3 pair** (a, n): integers satisfying
- n even, n ≥ 4, 3 ∤ n
- a odd, 1 ≤ a < n, gcd(a, n) = 1

Write n = 2m. Set:
- A⁺ = a² + n²
- A⁻ = (n − a)² + n²

**Identity (proved):** A⁺ − A⁻ = n(2a − n).

**Theorem C of Paper E (proved):** gcd(A⁺, A⁻) ∈ {1, 5}.

**Theorem B of Paper E (proved):**
- 4 ∤ n ⟹ A⁺ ≡ A⁻ ≡ 5 (mod 8)
- 4 | n ⟹ A⁺ ≡ A⁻ ≡ 1 (mod 8)

**Powerful-away-from-5:** N is powerful-away-from-5 if every prime p ≠ 5 with p | N
satisfies p² | N.

**Erdős–Szekeres decomposition:** Every powerful-away-from-5 integer N writes uniquely
(up to units) as N = 5^e · s² · t³ with t squarefree and 5 ∤ st. Call t the
cube factor of N.

**t=1 case (PROOF-DRAFT):** N = 5^e · s² (t=1) is the square-based powerful case.
Theorem M claims no Row-3 pair has both A⁺ and A⁻ in this form. This is NOT the subject
of OE-05.

**t≥2 case (OPEN — subject of OE-05):** There exists at least one prime p | t (p ≠ 5,
p squarefree factor of the cube part) with p‖A⁺ (exactly first power in s² · t³ sense?
No — powerful says v_p(A⁺) ≥ 2 for all p ≠ 5; in the Erdős–Szekeres decomposition
with t > 1, t is squarefree and v_p(N) = 2v_p(s)+3v_p(t) where v_p(t) ∈ {0,1}. For
p | t: v_p(N) = 2v_p(s)+3, so v_p(N) ≡ 1 (mod 2); v_p(N) ∈ {3,5,7,...}.) The
condition t > 1 in the cube-factor decomposition means at least one split prime
p ≡ 1 (mod 4), p ≠ 5, divides N to an odd exponent ≥ 3.

**NT-C (OE-05 target):** For every Row-3 pair (a, n), at least one of A⁺, A⁻ is NOT
powerful-away-from-5.

The t=1 case is proved. It remains to show no Row-3 pair has BOTH A⁺ and A⁻
powerful-away-from-5 when at least one has cube factor t ≥ 2.

**Gaussian formulation:** In ℤ[i], write w⁺ = a + ni and w⁻ = (n−a) + ni. If A⁺ is
powerful-away-from-5 with cube factor t₊ > 1, then in the ℤ[i] factorization
w⁺ = (unit)·(2+i)^{f} · ∏ πⱼ^{eⱼ} · ∏ π̄ₖ^{fₖ}, at least one Gaussian prime
πⱼ above a split prime pⱼ | t₊ appears to exponent eⱼ ≥ 3 (odd ≥ 3), since
gcd(a,n)=1 forces exactly one of {πⱼ, π̄ⱼ} to divide w⁺ (the other does not), and
v_{πⱼ}(w⁺) = v_{pⱼ}(A⁺) ≥ 3.

---

## The theorem / claim to be verified

**NT-C Cube-Factor Case.** There is no Row-3 pair (a, n) such that both A⁺ and A⁻
are powerful-away-from-5 with cube factor t > 1 (i.e., t ≥ 2, meaning at least one
prime p ≠ 5 divides A⁺ to an odd exponent ≥ 3, and similarly for A⁻).

An equivalent formulation: there is no Row-3 pair where both A⁺ and A⁻ are
powerful-away-from-5 AND neither is in the form 5^e · m² (the t=1 case).

---

## Proof skeleton to be closed

### Step 0 — What t=1 proof uses and why it fails for t≥2

Theorem M's proof for the 4∤n case reduces to: if A⁺ = 5^e·s² (t=1), the Gaussian
factorization forces w⁺ = (unit)·(2+i)^e·α² with α ∈ ℤ[i]. The sum identity
w⁺ + w⁻ = n(1+2i) then places α²+β² = n/(unit)·(2+i)^{1−e}, reducing to a fixed
elliptic curve (rank 0, no Row-3 rational points).

For t≥2: w⁺ = (unit)·(2+i)^e·U·α² where U = ∏ πⱼ with pⱼ | t₊ is a Gaussian
integer supported on primes OUTSIDE 5n. The sum identity becomes:

    U₁·α² + U₂·β² = n·(2+i)     (up to units, adjusting for 5-factors)

where U₁, U₂ are Gaussian integers whose prime support is not a priori bounded. This
is a Thue–Mahler equation with variable support — the growing-S barrier (see §Dead ends).

**What to close for Step 0:** Identify whether additional constraints from Theorem B
(the mod-8/mod-16 congruences) restrict the possible cube factors t₊, t₋ enough to
close the problem without uniform S-unit bounds.

---

### Step 1 — Local obstructions from mod-8 conditions

By Theorem B:
- 4 ∤ n ⟹ A⁺ ≡ 5 (mod 8). A powerful number ≡ 5 (mod 8) requires the 2-adic
  structure v₂(A⁺) = 0 and A⁺/5 ≡ 1 (mod 8). For A⁺ = 5·s²·t³: s odd, t odd,
  5·s²·t³ ≡ 5 (mod 8) iff s²·t³ ≡ 1 (mod 8) iff s·t ≡ ±1 (mod 8) (since s,t odd).
- 4 | n ⟹ A⁺ ≡ 1 (mod 8). For A⁺ = 5^e·s²·t³: if e=0, s²·t³ ≡ 1 (mod 8);
  if e≥1, 5^e ≡ 5 or 1 (mod 8) depending on parity of e; requires careful case split.

**What to close for Step 1:** Derive from Theorem B congruence conditions on s, t for
each sub-family (4∤n, 4|n). Determine whether mod-8 or mod-16 forces t to be a perfect
square (which would collapse t≥2 to a further constrained case) or rules out t≥2 entirely.

---

### Step 2 — Gaussian prime structure of cube-factor terms

Suppose p | t₊ (p ≡ 1 mod 4, p ≠ 5, p prime). Then v_p(A⁺) ≥ 3 (odd). Let π above
p be the unique Gaussian prime with π|w⁺ (unique by gcd(a,n)=1). Then v_π(w⁺) ≥ 3.

Similarly if p | t₋, v_π'(w⁻) ≥ 3 for the appropriate Gaussian prime π' above p.

From Theorem C: gcd(w⁺, w⁻) has norm in {1, 5}. Therefore no Gaussian prime above
p ≠ 5 divides BOTH w⁺ and w⁻. So the cube-factor primes of A⁺ and A⁻ are disjoint
(outside the 5-part).

Gap identity: A⁺ − A⁻ = n(2a−n). With v_π(w⁺) ≥ 3 and π ∤ w⁻:

    π³ | w⁺ − w⁻ = w⁺ − w⁻ = (A⁺ − A⁻)/(w⁺ + w̄⁻)  [Gaussian norm identity]

This requires p³ | n(2a−n)·(something). Since p ∤ n (because p | A⁺ and gcd(A⁺,n)=1),
p | (2a−n)·(something). Derive a congruence constraint on a mod p³.

**What to close for Step 2:** Show that the constraint p³ | something derived from the
gap identity, combined with the Row-3 conditions on (a, n), forces either p | n
(contradicting gcd(A⁺,n)=1) or a contradiction in another way. If this closes the case,
NT-C cube-factor follows without S-unit equations.

---

### Step 3 — Thue–Mahler / descent approach (expected barrier)

The Gaussian equation U₁α² − U₂β² = n (from Step 0) is a Thue-Mahler equation over
ℤ[i] with S = {Gaussian primes above 5, primes above n} ∪ {primes of U₁, U₂}.

The primes of U₁ (cube-factor primes of A⁺) lie outside S₀ ∪ S(n) (see OE-03/04
review records for the proof: gcd(A⁺,n)=1 implies cube-factor primes ∉ S(n)). So
the effective support S is not a priori bounded, and known Evertse–Schmidt bounds
require |S| fixed.

**What to close for Step 3:** Either (a) show that the cube-factor condition forces
|cube-factor primes of A⁺| ≤ K for some absolute K (making S bounded), or (b)
identify an approach that bypasses S-unit equations entirely.

Remark: (b) is likely needed. The Steps 1–2 (local/structural) approach above may
close the problem without reaching Step 3.

---

## Acceptance criteria

1. **CONFIRMED:** Proof that no Row-3 pair has both A⁺ and A⁻ powerful-away-from-5
   with cube factor t≥2. Combined with Theorem M (t=1 case), this gives full NT-C.
   Proof must not use RH, zero locations, or any unverified conjecture.

2. **PARTIAL — mod constraints close a sub-family:** Proof that for 4|n (or 4∤n)
   the cube-factor condition is impossible. A genuine case split with the complementary
   case remaining open is acceptable; label clearly.

3. **PARTIAL — Step 2 structural obstruction:** A complete derivation of the p³-gap
   identity constraint, even if it only excludes cube-factor primes p above a threshold.

4. **INCONCLUSIVE:** Precise statement of what is proved, what barrier is hit, and
   the strongest partial localization reachable (e.g., "cube factors t satisfy t | f(n)
   for explicit f" as a necessary condition).

5. **REFUTED:** An explicit Row-3 pair (a, n) with n > 2000 where both A⁺ and A⁻
   are powerful-away-from-5 with cube factor t≥2. Must be verified by the independent
   checker `checker/verify_M.py` (which already excludes n≤3000 for the t=1 case;
   a separate check is needed for t≥2 with n≤3000 as additional sanity).

---

## Key identities and facts (all verified, not from memory)

**I1:** A⁺ − A⁻ = n(2a − n).  [Algebraic identity.]

**I2 (Theorem C):** gcd(A⁺, A⁻) ∈ {1, 5}.  [Proved in Paper E.]

**I3 (Theorem B):** 4∤n ⟹ A⁺ ≡ A⁻ ≡ 5 (mod 8); 4|n ⟹ A⁺ ≡ A⁻ ≡ 1 (mod 8).
[Proved in Paper E.]

**I4 (gcd-norm separation):** For p ≠ 5 prime, p | A⁺ ⟹ p ∤ n.
[Proof: A⁺ = a²+n²; if p|A⁺ and p|n then p|a, contradicting gcd(a,n)=1.]

**I5 (Gaussian prime uniqueness):** For p ≡ 1 (mod 4) prime, p ≠ 5, p | A⁺:
exactly one of the two Gaussian primes above p divides w⁺ = a+ni.
[Proof: if both π and π̄ divide w⁺, then p | w⁺ in ℤ[i], forcing p|a and p|n,
contradicting gcd(a,n)=1.]

**I6 (cube-factor exponent):** In the Erdős–Szekeres decomposition A⁺ = 5^e·s²·t³
with t squarefree, 5∤st: a prime p|t satisfies v_p(A⁺) ≡ 1 (mod 2) and v_p(A⁺) ≥ 3.

---

## Numerical anchor (sanity only, not a proof input)

Script `checker/OE01_anchor.py` verifies (output: 0 instances in both cases):

```
for all Row-3 pairs (a,n) with 4 ≤ n ≤ 2000, n even, 3∤n, a odd, gcd(a,n)=1:
  zero pairs have both A+ and A- powerful-away-from-5.
  (Covers t=1 and t>=2 simultaneously.)
```

This is a computational sanity check only. The analytic proof must cover all n.

---

## Dead ends (do not re-attempt)

**DE-1 (ABC over ℚ):** A⁺ + (−A⁻) = n(2a−n). rad(A±) ≤ 5·(A±)^{1/3}·n^{ω(n)} for
the powerful case; the abc inequality gives max(A±) ≪ n^{3+ε}, trivially satisfied.

**DE-2 (Evertse S-units with fixed S):** For fixed n, Evertse gives finitely many
Thue–Mahler solutions (Evertse, *On equations in S-units and the Thue-Mahler equation*,
Invent. Math. 75 (1984), Theorem 1 — scope: S fixed). But S grows with n (cube-factor
primes of A⁺ are new primes outside S(n)), so no uniform bound is available.
See OE-03/04 review records.

**DE-3 (Baker linear forms on |A⁺/A⁻ − 1|):** |A⁺/A⁻ − 1| ≍ (2a−n)/n is
polynomially small in n, not exponentially small. Baker's lower bound on linear forms
in logarithms gives |Λ| > exp(−C·log H·log log H) for height H ≍ A⁺ (Baker, *A
sharpening of the bounds for linear forms in logarithms I*, Acta Arith. 21 (1972),
Theorem 1 — scope: fixed number of logarithms). Since 1/n is polynomially small, the
Baker lower bound is not less than 1/n for large n. No contradiction.

**DE-4 (density/sieve):** Powerful numbers in [n², 2n²] are O(√(2n²)) = O(n) in count.
Row-3 pairs number φ(n)/4 ≈ n/(4 log log n). A density argument gives no bound of 0.
