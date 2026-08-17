# Problem OB-46 — Simultaneous shifted Gaussian-powerful values in OP1-A

**Status (2026-08-17): PARTIALLY RESOLVED → see OB-47 for the open core.**

Three unconditional invariants are now proved (see §3 below and the OB-46
review record):
- **Thm 1:** $3 \nmid N$ for every Row-3 pair.
- **Thm 2:** All prime factors of $N$ satisfy $p \equiv 1 \pmod 4$;
  $A_+ \equiv A_- \pmod 8$.
- **Thm 3:** $\gcd(A_+, A_-) \in \{1, 5\}$; when $5 \mid A_+$ and $5 \mid A_-$
  the 5-adic powerfulness condition $v_5(N) \geq 2$ is automatic.

The remaining open question — can $A_+$ and $A_-$ be **simultaneously**
powerful away from 5? — is forwarded to **OB-47**, which states only that core
and avoids the dead ends (Faltings on a 3-fold, trivial abc bound) identified
during the OB-46 review.

**Type:** arithmetic / algebraic number theory (Gaussian UFD, powerful values,
quadratic norms)

**Non-circularity.** This is a purely finite arithmetic problem. It assumes no
RH-equivalent condition, no zero of `ζ`, no L-value, no analytic zero-counting
input, and no fitted zero ordinate. RH stays `[OUT]`.

This problem supersedes the broader OB-44A formulation. It isolates the only
remaining OB-44A core: two horizontally shifted primitive Gaussian integers
cannot simultaneously be powerful away from the primes over `5`. A full proof,
an explicit counterexample, a genuine infinite-family theorem, or a precise
proof strategy is desired. A finite scan is not a solution.

---

## 1. All definitions

An integer `X≥1` is **powerful away from `5`** if every rational prime
`p≠5` dividing `X` satisfies `p² | X`. No condition is imposed on the exponent
of `5`.

An integer `X≥1` is **powerful** if every prime `p | X` satisfies `p² | X`.

Let `Z[i]` be the Gaussian integers. A Gaussian integer `η` is **powerful away
from the primes over `5`** if every Gaussian prime `𝔭∤5` dividing `η` divides it
with multiplicity at least two. Again no condition is imposed on the two primes
over `5`.

Fix integers `a,n` satisfying the following **off-line Row-3 conditions**:

```
n even, n≥4, 3∤n;
a odd, 1≤a<n;
gcd(a,n)=1.
```

Define two primitive Gaussian integers and their norms:

```
w_+ = a+ni,
w_- = (a−n)+ni,

A_+ = |w_+|² = a²+n²,
A_- = |w_-|² = (a−n)²+n².
```

Also define

```
N=A_+A_-.
```

The off-line normalization `n≥4` excludes the boundary point `(a,n)=(1,2)`,
for which `a/n=1/2` and `N=25`; that point is on the critical line and is not
an off-line counterexample.

---

## 2. Exact reductions already proved

The following identities and implications are elementary and may be used freely.

### 2.1 Norm factorization

Expanding the two quadratics gives

```
N = (a²+n²)((a−n)²+n²).
```

Equivalently, with

```
w_+ = a+ni,       w_- = (a−n)+ni,
```

one has

```
N=|w_+|²|w_-|².
```

### 2.2 The two rational factors are almost coprime

The gcd satisfies

```
gcd(A_+,A_-) ∈ {1,5}.
```

Indeed, if a prime `p` divides both, then `p∤n`, since `p|n` would give
`A_+≡a² mod p`, contradicting `gcd(a,n)=1`. Hence `p` divides

```
A_+−A_- = n(2a−n),
```

so `p|2a−n`. Thus `n≡2a mod p`, and

```
A_+≡a²+(2a)²=5a² mod p.
```

Since `p∤a`, this forces `p=5`. The same congruence modulo `25` shows that the
common `5`-adic valuation is at most one.

### 2.3 Exact powerful criterion

Because the two factors have no common prime divisor except possibly one copy
of `5`,

```
N is powerful
⟺ A_+ and A_- are both powerful away from 5
    and v_5(A_+)+v_5(A_-)≠1.
```

Thus the problem is not merely to show that one quadratic factor is not
powerful away from `5`; the `5`-adic exceptional branch must also be handled.

### 2.4 Gaussian formulation

Since `gcd(a,n)=gcd(a−n,n)=1`, both Gaussian integers are primitive. For a
rational prime `p≠5`, a common divisor of the two coordinates would force
`p` to divide both coordinates, so no such rational prime occurs. Therefore the
rational norm condition is equivalent to the Gaussian-powerful condition away
from the primes over `5`:

```
A_+ powerful away from 5
⟺ w_+ powerful away from the Gaussian primes over 5,

A_- powerful away from 5
⟺ w_- powerful away from the Gaussian primes over 5.
```

The two Gaussian integers also differ horizontally by the real integer `n`:

```
w_+ − w_- = n.
```

So the core question is whether two primitive Gaussian integers on the same
horizontal line, with this explicit shift relation, can both be powerful away
from the primes over `5`.

---

## 3. Problem to be solved

> **Problem OP1-A′.** Prove that there is no off-line Row-3 pair `(a,n)` for
> which both `w_+=a+ni` and `w_-=(a−n)+ni` are powerful away from the Gaussian
> primes over `5`, except possibly when
> ```
> v_5(A_+)+v_5(A_-)=1.
> ```
>
> Equivalently, prove that `N=A_+A_-` is never powerful on the off-line Row-3
> family.
>
> Alternatively, give an explicit off-line Row-3 pair for which `N` is powerful.

The desired result has the following exact form:

```
For every a,n satisfying §1,
there exists a rational prime p such that v_p(N)=1.
```

### Preferred proof targets, in decreasing strength

1. Prove the full off-line Row-3 impossibility.
2. Prove it for all but finitely many pairs `(a,n)`.
3. Prove it for a natural positive-density infinite subfamily.
4. Give a primitive-divisor theorem for at least one of `w_+` or `w_-` outside
   the finite set of Gaussian primes over `5`.
5. Give a sharp conditional route (for example, an abc-type consequence),
   explicitly stating the hypothesis and the implied constant/exponent.

---

## 4. Known obstacles and dead ends

1. **A generic squarefree-values theorem for binary quartics does not apply
   verbatim.** The quartic has norm-type structure over `Q(i)`, and the relevant
   root field is quadratic.

2. **A small finite modulus alone is unlikely to prove the obstruction.** For
   several small prime-square moduli there remain local residue classes in which
   both quadratic factors avoid a first-power divisibility relation. Do not
   submit a finite residue table as a proof.

3. **One factor can be powerful away from `5`.** This is not impossible by
   itself. For example,
   ```
   a=19, n=22:
       A_+=19²+22²=845=5·13²,
       A_-=(19−22)²+22²=493=17·29.
   ```
   Thus only the simultaneous condition is the target.

4. **Do not forget the `5`-adic branch.** Even if both factors are powerful
   away from `5`, `N` is still non-powerful when
   `v_5(A_+)+v_5(A_-)=1`.

5. **The exceptional critical-line point is excluded.** `(a,n)=(1,2)` gives
   `A_+=A_-=5` and `N=25`, but `a/n=1/2`. It is not an off-line Row-3 point.

---

## 5. Numerical evidence (sanity only, not a proof input)

An exact deposited scan of the finite box

```
4≤n<5000, n even, 3∤n, 1≤a<n, a odd, gcd(a,n)=1
```

contains

```
1,898,236
```
Row-3 pairs. Exact factorization gives:

```
powerful N:                         0
N with no simple prime factor:      0
A_+ powerful away from 5:           633
A_- powerful away from 5:           633
both factors powerful away from 5:  0
```

The scan is reproduced by `checker/ob44a_factorization_scan.py`; a reviewer need
not consult it because all definitions and the claimed finite counts are stated
here. These counts are evidence only, not premises.

---

## 6. Acceptance criteria

Return exactly one of the following.

1. **CONFIRMED.** A full proof that `N` is never powerful on the off-line
   Row-3 family.

2. **PARTIAL.** A proved all-but-finite, positive-density, or named infinite
   subfamily result. State the exact family and density convention.

3. **REFUTED.** An explicit off-line Row-3 pair `(a,n)` with `N` powerful.
   Provide the factorizations of `A_+`, `A_-`, and `N`.

4. **STRATEGY.** A concrete proof route. It must identify:
   - the main tool;
   - which sublemmas are standard;
   - which are new;
   - how the norm-type/Galois obstruction is bypassed;
   - how the `5`-adic exceptional branch is handled.

5. **INCONCLUSIVE.** A precise localization of the missing theorem, including
   why existing primitive-divisor, squarefree-values, or Gaussian-factorization
   tools do not apply.

---

## 7. Numerical anchor (sanity only)

Take

```
a=19, n=22.
```

Then:

```
A_+=19²+22²=845=5·13²,
A_-=(19−22)²+22²=493=17·29,
N=845·493=416585
  =5·13²·17·29.
```

The first factor is powerful away from `5`, but the second has two simple
prime factors, so this is not a simultaneous counterexample.

---

## Pre-send lint record

| PROMPT_LINT item | Result |
|---|---|
| L1–L4 | N/A: no entire-function, canonical-product, or analytic zero-location claim. |
| L5 | PASS: `grep “on the critical line”` hits §1 line 56 — boundary-point exclusion label only, not a hypothesis; no real-zero divisor, no zero of `ζ`, no γ_n. Domain defined by explicit arithmetic conditions. |
| L6 | PASS: full proof, partial theorem, explicit counterexample, strategy, and inconclusive paths are non-vacuous. |
| L7–L16 | PASS/N/A: no counting-factor, growth-ray, Taylor-jet, Fredholm, or representation-invariant claim is used. |
| L17 | PASS: no external theorem is assumed; any proposed tool must state exact scope. |
| L18 | PASS: numerical scan and anchor are labeled sanity only and are not proof inputs. |
| L19 | PASS: PARTIAL and INCONCLUSIVE are first-class outcomes. |
| L20–L24 | N/A. |
| Self-containment | PASS: powerful-away-from-5, Gaussian-powerful, Row-3 domain, shifted Gaussian factors, exact criterion, dead ends, evidence, outcomes, and anchor are defined in-file. |
| Privacy | PASS: no personal path, username, company, or internal host occurs. |
