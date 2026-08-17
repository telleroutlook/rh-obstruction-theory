# OB-47 Referee Verdict: Simultaneous powerful-away-from-5 Gaussian norms

**Problem file:** `outsource/OB-47-OP1A-simultaneous-powerful-open-core.md`
**Outcome:** **INCONCLUSIVE**
**Status recommendation:** Record failure localizations as precise blocking theorems;
do not promote OP1-A to INDEPENDENTLY-CHECKED; retain OB-47 open pending any of the
four new theorems listed below.

---

## 1. Verdict summary

All four proposed approaches (A–D) are blocked by genuine, distinct obstructions
in modern Diophantine geometry. The failure localizations are accepted as correct
(with one precision note on Approach B). No approach was incorrectly dismissed;
no approach contains a hidden shortcut that the referee missed. The problem is
genuinely hard and the localization is the most useful deliverable at this stage.

---

## 2. Approach-by-approach assessment

### Approach A — S-unit equations over ℤ[i]

**Failure localization accepted.**

The core issue is correct: normalizing $w_+ - w_- = n$ to an equation of the
form $X' - Y' = 1$ forces the prime factors of $n$ into the allowed set $S$.
Because $n$ varies over the Row-3 family, $S$ grows with $n$. Evertse–Schlickewei–
Schmidt and its Gaussian analogues give finiteness for a **fixed** finite $S$;
they do not give height bounds that are uniform as $|S| \to \infty$. This
correctly rules out Approach A as stated.

**Required new theorem (A):** A uniform, effective S-unit theorem over $\mathbb{Z}[i]$
for equations $X - Y = n$ in which the allowed prime set $S = S_0 \cup S(n)$
(with $|S(n)| = O(\omega(n))$) grows with the right-hand side, yielding an explicit
height bound in terms of $n$ and $|S(n)|$.

### Approach B — Thue–Mahler / norm-form equations for fixed $n$

**Failure localization accepted with a precision note.**

*What is correct:* For the simplest sub-case — powerful = perfect square times a
power of 5, ignoring the cube factor — fixing $n$ and the 5-adic type $(e_1, e_2)$
reduces the system to a **1-dimensional algebraic curve** (4 real unknowns from
$\alpha, \beta \in \mathbb{Z}[i]$, minus 3 real constraints from
$\operatorname{Im}(w_+) = n$, $\operatorname{Im}(w_-) = n$, and
$\operatorname{Re}(w_+) - \operatorname{Re}(w_-) = n$). For this curve, Faltings
guarantees finitely many rational points for each fixed $n$, but is ineffective
and gives no uniform bound as $n \to \infty$.

*Precision note:* The response describes the cube factor as causing the variety to
be "each individual curve... of genus well above 1." The more accurate description
is that with the full powerful parametrization
$w_+ = (1+2i)^{f_1}(1-2i)^{g_1} u_1^2 v_1^3$ (8 real unknowns for the pair
$(u_1, v_1, u_2, v_2) \in \mathbb{Z}[i]^4$, minus 3 constraints), the variety is
**5-dimensional**, not a curve at all. Faltings is inapplicable not because the
genus is too low but because the dimension is too high. The square-only sub-case
does give a curve, but even there Faltings is ineffective. These two obstructions
are distinct; the failure localization is correct in spirit but merges them.

**Required new theorem (B):** An effective proof (or conditional-on-Bombieri–Lang
effective bound) for rational points on the specific 5-fold
$\{(a, u_1, v_1, u_2, v_2) : a^2+n^2 = 5^{e_1} u_1^2 v_1^3,\;
(a-n)^2+n^2 = 5^{e_2} u_2^2 v_2^3\}$, uniform in $n$. For the square-only
sub-case, an effective version of Faltings for the associated genus-$g$ curve
(with $g$ determined by the degree of the norm-form equation) suffices.

### Approach C — Primitive divisors via Gaussian Zsygmondy

**Failure localization accepted.**

Bilu–Hanrot–Voutier's primitive divisor theorem for Lucas and Lehmer sequences
depends critically on the linear recurrence structure (fixed characteristic roots
and a multiplication-by-$\alpha$ action). The family
$\{a + ni : a \text{ odd}, \gcd(a,n) = 1\}$ is a polynomial family in $a$ with
no such recurrence, and no analogue of the Bilu–Hanrot–Voutier theorem exists
in the literature for this type of family.

**Required new theorem (C):** A Zsygmondy-type primitive divisor theorem for the
family $\{a + ni\}$ in $\mathbb{Z}[i]$: an absolute constant $C$ such that for
all Row-3 pairs with $n > C$, at least one of $w_+ = a + ni$ or $w_- = (a-n)+ni$
has a Gaussian prime $\mathfrak{p} \nmid 5n$ appearing to exactly first power.
(A one-sided version sufficing for T4 would also close the problem.)

### Approach D — Powerful-gap lower bound

**Failure localization accepted.**

The gap $A_+ - A_- = n(2a-n)$ scales as $O(n^2) \asymp A_-$, not $o(A_-)$. Classical
powerful-gap theorems (Størmer, Molsen, unconditional Pillai) apply to gaps of size
$o(A^{1/2})$ in the regime $k \ll A$; they give nothing when $k \asymp A$. Applying
abc over $\mathbb{Q}(i)$ with the powerful hypothesis yields
$n^2 \ll n^{3+\varepsilon}$, which is trivial (Dead End D2 of OB-47, reproduced here
correctly).

**Required new theorem (D):** A conditional or unconditional powerful-gap theorem
that applies when the gap $k \asymp A$. Concretely: if $A_+ - A_- = k$ with
$A_\pm$ powerful away from 5, and $k \asymp A_-$, prove that $A_- \ll k^{C}$ for
some explicit $C < \infty$. This would require abc over $\mathbb{Z}[i]$ with an
exponent strictly less than 3 in $\mathrm{rad}(A_+ A_- k)$, or an independent
Diophantine argument.

---

## 3. Summary of required new theorems

| ID | Theorem needed | Approach unlocked |
|---|---|---|
| NT-A | Uniform effective S-unit theorem over ℤ[i] with growing S | A |
| NT-B | Effective Bombieri–Lang / Faltings for the norm-form 5-fold (or square-only curve) | B |
| NT-C | Zsygmondy primitive divisor theorem for shifted Gaussian norm family | C |
| NT-D | Powerful-gap bound for $k \asymp A$ (abc over ℤ[i] with exponent < 3) | D |

Any single one of NT-A, NT-C, or NT-D proved unconditionally would likely resolve
OB-47 directly. NT-B requires an effective version of a deep conjecture.

---

## 6. Addendum: refined geometric localization (2026-08-17, third submission)

A third submission correctly resolved all prior errors and provided refined geometric
localization for Approach B (NT-B):

**Square-only sub-case (β=δ=1):** The simultaneous system
$a^2+n^2 = 5^{e_1}u^2$ and $(a-n)^2+n^2 = 5^{e_2}v^2$ (for fixed $n$) defines the
**intersection of two quadrics in $\mathbb{P}^3$**: a smooth spatial curve of degree 4
and genus $g = 1$ (an elliptic curve, by the adjunction formula
$g = 1 + d_1 d_2(d_1+d_2-4)/2 = 1$). Faltings does not apply (requires $g \geq 2$).
The rational points are governed by Mordell-Weil; the rank may be positive, allowing
infinitely many rational points for a given $n$. Bounding solutions uniformly over $n$
requires: (a) rank control for each fixed $n$ (2-descent or Chabauty), and (b) a
uniform height bound as $n \to \infty$.

**Full powerful case (β,δ non-trivial):** The system is a 3-fold (5 unknowns, 2
equations); Bombieri–Lang required.

**Refinement of NT-B:** An effective version of Faltings / rank-zero proof for the
intersection-of-two-quadrics elliptic curve family, uniform in $n$, would close the
square-only sub-case. The general case still needs effective Bombieri–Lang.

**Minor imprecision noted:** B2 table entry lists "$v_5(2a-n)=1$" but the correct
condition is "$v_5(2a-n) \geq 1$" (verified: $a=1, n=52$ has $v_5(2a-n)=2$ with
$v_5(A_\pm)=1$). Does not affect the branch analysis.

No approach uses RH, a zero of $\zeta$, a zero ordinate, or any equivalent
reformulation. The problem and all four approaches are purely arithmetic.
RH stays `[OUT]`.

---

## 5. Status recommendation for PLAN.md

- OP1-A: remains **OPEN**; the three unconditional invariants (OB-46 Thm 1–3)
  stand, but the simultaneous powerful-away-from-5 question is unresolved.
- OB-47: **INCONCLUSIVE — failure precisely localized (NT-A/B/C/D)**.
- Next action: if any of NT-A/C/D enters the literature or can be proved internally,
  re-open OB-47 with that theorem as a free lemma.
