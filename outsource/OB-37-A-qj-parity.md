# Problem OB-37 — A: Parity argument for O(T^{-3}) vanishing in q_j(T) asymptotics

**Type:** pure analysis / asymptotic expansion / complex algebra

**Non-circularity:** RH is not assumed anywhere.  The points $\sigma_0 + iT$ and
$1-\sigma_0 + iT$ are explicit complex numbers with $\sigma_0 \in (0,1)$ a fixed real
parameter and $T \in \mathbb{R}$ a real variable.  No zeros of $\zeta$, no Euler
product, no functional equation of $\zeta$, and no zero-counting law enters any step.
The function $\varphi_j$ is a polynomial-type transform of $\rho^{-1}$ with integer
binomial coefficients; all claims are elementary complex algebra and the binomial
theorem.

---

## Background and motivation

Paper A (B2 framework), Lemma 2.9 (label `lem:qasympt`) asserts:

$$q_j(T) = \frac{4j^2}{T^2} + O(T^{-4}) \quad \text{as } T \to +\infty,$$

where $q_j(T)$ is the Li evaluation of the four-point multiset $Q(\sigma_0, T)$ for
fixed $\sigma_0 \in (0,1)$, $\sigma_0 \neq 1/2$ (full definitions below).  The
expansion exhibits a conspicuous gap: the leading $T^{-2}$ term is followed directly
by $O(T^{-4})$, with no $T^{-3}$ term.  A direct Laurent expansion produces an
$O(T^{-3})$ remainder in $\operatorname{Re} g(T)$; Paper A's proof sketch invoked a
parity argument to promote that remainder to $O(T^{-4})$.

**This problem asks for independent verification** of all three components:

1. The parity identity $g(-T) = \overline{g(T)}$ holds algebraically for all
   $T \in \mathbb{R}$.
2. That parity forces the $T^{-3}$ coefficient of $\operatorname{Re} g(T)$ to vanish.
3. That the $T^{-2}$ coefficient of $\operatorname{Re} g(T)$ is exactly $j^2$
   (independent of $\sigma_0$), so $q_j(T) = 4j^2/T^2 + O(T^{-4})$.
4. That the two numerical anchors below are reproduced by exact rational arithmetic.

---

## All definitions (self-contained — everything is here)

### Li test function

Fix an integer $j \geq 1$.  Define:

$$\varphi_j(\rho) = 1 - (1 - \rho^{-1})^j, \qquad \rho \in \mathbb{C} \setminus \{0\}.$$

This is a degree-$j$ polynomial in $\rho^{-1}$ with integer binomial coefficients:
$\varphi_j(\rho) = \sum_{k=1}^{j} \binom{j}{k}(-1)^{k+1} \rho^{-k}$.  In particular,
all coefficients are real, so:

$$\varphi_j(\bar\rho) = \overline{\varphi_j(\rho)} \quad \text{for all } \rho \neq 0.$$

First values: $\varphi_1(\rho) = \rho^{-1}$;
$\varphi_2(\rho) = 2\rho^{-1} - \rho^{-2}$;
$\varphi_3(\rho) = 3\rho^{-1} - 3\rho^{-2} + \rho^{-3}$.

### The four-point multiset

Fix $\sigma_0 \in (0,1)$, $\sigma_0 \neq 1/2$.  For $T \in \mathbb{R} \setminus \{0\}$
define the multiset:

$$Q(\sigma_0, T) = \{\sigma_0 + iT,\; \sigma_0 - iT,\; 1-\sigma_0 + iT,\; 1-\sigma_0 - iT\}.$$

This is a four-element multiset closed under complex conjugation ($\rho \mapsto \bar\rho$)
and under the symmetry $\rho \mapsto 1 - \rho$.

### Li evaluation and $q_j(T)$

For a finite multiset $Z$ of nonzero complex numbers define (B2 R-symm convention,
Paper A §2):

$$\mathrm{Li}_j(Z) = 2 \sum_{\rho \in Z} \varphi_j(\rho),$$

where the sum counts multiplicity.  Set:

$$q_j(T) := \mathrm{Li}_j(Q(\sigma_0, T)).$$

### Reduction to $g(T)$

Define:

$$g(T) = \varphi_j(\sigma_0 + iT) + \varphi_j(1-\sigma_0 + iT).$$

Expanding $\mathrm{Li}_j(Q)$ over all four points and using
$\varphi_j(\bar\rho) = \overline{\varphi_j(\rho)}$ to pair conjugates:

$$q_j(T)
= 2\bigl[\varphi_j(\sigma_0{+}iT) + \varphi_j(\sigma_0{-}iT)
      + \varphi_j(1{-}\sigma_0{+}iT) + \varphi_j(1{-}\sigma_0{-}iT)\bigr]
= 4\,\operatorname{Re} g(T).$$

The factor 4 arises because each conjugate pair contributes $2\operatorname{Re}$ of the
upper-half element, and there are two pairs.

### Expansion objective

The claim is that, as $T \to +\infty$:

$$\operatorname{Re} g(T) = \frac{j^2}{T^2} + O(T^{-4}),
\qquad q_j(T) = \frac{4j^2}{T^2} + O(T^{-4}).$$

---

## The claim to be verified

**Claim (Lemma 2.9 coefficient).** For all integers $j \geq 1$, all
$\sigma_0 \in (0,1)$ with $\sigma_0 \neq 1/2$, and $T \to +\infty$:

$$q_j(T) = \frac{4j^2}{T^2} + O(T^{-4}).$$

Equivalently, with $g(T) = \varphi_j(\sigma_0+iT) + \varphi_j(1-\sigma_0+iT)$:

(a) **Parity:** $g(-T) = \overline{g(T)}$ for all $T \in \mathbb{R}$.

(b) **Vanishing $T^{-3}$:** The real-part Laurent expansion
    $\operatorname{Re} g(T) = \sum_{k \geq 2} a_k T^{-k}$ satisfies $a_3 = 0$.

(c) **Leading coefficient:** $a_2 = j^2$, independent of $\sigma_0$.

---

## Proof skeleton to be closed

### Step 1 — Parity identity: $g(-T) = \overline{g(T)}$

Apply $\varphi_j(\bar\rho) = \overline{\varphi_j(\rho)}$ to each summand:

$$\varphi_j(\sigma_0 - iT)
= \varphi_j\!\bigl(\overline{\sigma_0+iT}\bigr)
= \overline{\varphi_j(\sigma_0+iT)},$$

$$\varphi_j(1-\sigma_0 - iT)
= \varphi_j\!\bigl(\overline{1-\sigma_0+iT}\bigr)
= \overline{\varphi_j(1-\sigma_0+iT)}.$$

Therefore:

$$g(-T)
= \varphi_j(\sigma_0-iT) + \varphi_j(1-\sigma_0-iT)
= \overline{\varphi_j(\sigma_0+iT)} + \overline{\varphi_j(1-\sigma_0+iT)}
= \overline{g(T)}.$$

**What to close for Step 1:** confirm the identity $\varphi_j(\bar\rho)
= \overline{\varphi_j(\rho)}$ for general $\rho \neq 0$ and $j \geq 1$ (it follows from
the binomial expansion: every coefficient $\binom{j}{k}(-1)^{k+1}$ is a real integer,
and complex conjugation commutes with real-coefficient polynomial evaluation).  Verify
explicitly for $j = 1$, $\rho = 3/4 + 3i$: $\varphi_1(3/4+3i) = 4/51 - 16i/51$ and
$\varphi_1(3/4-3i) = 4/51 + 16i/51 = \overline{\varphi_1(3/4+3i)}$.

### Step 2 — Parity forces $a_3 = 0$ in $\operatorname{Re}\,g(T)$

From Step 1, $\operatorname{Re} g(-T) = \operatorname{Re}\,\overline{g(T)} = \operatorname{Re}\,g(T)$.
So $h(T) := \operatorname{Re}\,g(T)$ is an **even** function of $T$.

For large $|T|$, $h(T)$ admits a Laurent expansion in $1/T$ (the denominator of each
$\varphi_j(\sigma+iT)$ is $(\sigma^2+T^2)^j$, which is an even polynomial in $T$; so
$h(T)$ extends as a rational function in $T$ near $1/T=0$).  Since $h(-T) = h(T)$,
every odd-power coefficient must vanish: $a_k = 0$ for all odd $k \geq 1$.  In
particular $\mathbf{a_1 = 0}$ and $\mathbf{a_3 = 0}$.

**What to close for Step 2:** confirm that the denominator
$(\sigma^2+T^2)^j$ is indeed even in $T$ (it is, since $T$ appears only as $T^2$), so
$\varphi_j(\sigma+iT)$ is a rational function of $T$ admitting a Laurent expansion in
$1/T$, and then the parity argument is sufficient to kill all odd-power coefficients.

### Step 3 — Leading coefficient: $a_2 = j^2$

For large $T$ expand $(\sigma + iT)^{-1}$:

$$(\sigma + iT)^{-1}
= \frac{\sigma - iT}{\sigma^2 + T^2}
= \frac{-i}{T} + \frac{\sigma}{T^2} + \frac{i\sigma^2}{T^3}
  - \frac{\sigma^3}{T^4} + O(T^{-5}).$$

So $1 - (\sigma+iT)^{-1} = 1 + u$ with
$u = i/T - \sigma/T^2 + O(T^{-3})$.  The binomial theorem through order $T^{-2}$:

$$ju = \frac{ij}{T} - \frac{j\sigma}{T^2} + O(T^{-3}),$$

$$\tfrac{j(j-1)}{2}\,u^2
= \tfrac{j(j-1)}{2} \cdot \frac{-1}{T^2} + O(T^{-3}).$$

Summing:

$$(1-(\sigma+iT)^{-1})^j
= 1 + \frac{ij}{T} - \frac{j\sigma + j(j-1)/2}{T^2} + O(T^{-3}),$$

$$\varphi_j(\sigma+iT)
= -\frac{ij}{T} + \frac{j\sigma + j(j-1)/2}{T^2} + O(T^{-3}).$$

Adding the two summands of $g(T)$ with $\sigma = \sigma_0$ and $\sigma = 1-\sigma_0$:

$$g(T)
= -\frac{2ij}{T}
  + \frac{\bigl[j\sigma_0 + j(j-1)/2\bigr] + \bigl[j(1-\sigma_0) + j(j-1)/2\bigr]}{T^2}
  + O(T^{-3}).$$

The $T^{-2}$ numerator collapses:

$$j\sigma_0 + j(1-\sigma_0) + j(j-1)
= j \cdot 1 + j(j-1)
= j + j^2 - j
= j^2.$$

Therefore $g(T) = -2ij/T + j^2/T^2 + O(T^{-3})$, and:

$$\operatorname{Re}\,g(T) = \frac{j^2}{T^2} + O(T^{-3}).$$

Step 2 shows $a_3 = 0$, promoting this to:

$$\operatorname{Re}\,g(T) = \frac{j^2}{T^2} + O(T^{-4}),
\qquad q_j(T) = \frac{4j^2}{T^2} + O(T^{-4}).$$

**Key observation:** the $\sigma_0$-independence follows from $\sigma_0 + (1-\sigma_0) = 1$,
which holds for any $\sigma_0 \in (0,1)$.

**What to close for Step 3:** verify the displayed algebra (in particular, that
$j\sigma_0 + j(1-\sigma_0) + j(j-1) = j^2$ for all $j$ and all $\sigma_0$), and
confirm that "the $O(T^{-3})$ improves to $O(T^{-4})$" is justified by Step 2 (it
is: Step 3's direct expansion produces an $O(T^{-3})$ term in $\operatorname{Re} g$;
Step 2's parity argument shows its coefficient is zero).

### Consistency check: direct T^{-3} coefficient is purely imaginary

Carry the binomial expansion one order further.  Setting
$u = i/T - \sigma/T^2 - i\sigma^2/T^3 + O(T^{-4})$:

$$u^2 = -T^{-2} - 2i\sigma T^{-3} + O(T^{-4}), \qquad
u^3 = -iT^{-3} + O(T^{-4}).$$

Then:

$$\varphi_j(\sigma+iT)
= -\frac{ij}{T}
  + \frac{j\sigma + j(j-1)/2}{T^2}
  + \frac{i\,c_3(\sigma,j)}{T^3}
  + O(T^{-4}),$$

where $c_3(\sigma,j) = j\sigma^2 + j(j-1)\sigma + j(j-1)(j-2)/6 \in \mathbb{R}$.

The $T^{-3}$ coefficient in $g(T)$ is $i[c_3(\sigma_0,j) + c_3(1-\sigma_0,j)]/T^3$,
which is **purely imaginary**.  Therefore $\operatorname{Re}\,g(T)$ receives no
contribution at order $T^{-3}$, confirming $a_3 = 0$ directly.

**What to close for the consistency check:** derive $u^2$ and $u^3$ from
$u = i/T - \sigma/T^2 + O(T^{-3})$ (one step of complex squaring and cubing), confirm
$c_3(\sigma,j)$ is the displayed real expression, and note that its imaginary coefficient
$i c_3/T^3$ contributes 0 to $\operatorname{Re}\,g$.

---

## Acceptance criteria

1. **CONFIRMED:** Steps 1–3 are each verified to be correct; the consistency check
   confirms the $T^{-3}$ coefficient in $\operatorname{Re}\,g$ is purely imaginary; both
   numerical anchors match the exact values below.  Report the accepted statement:
   "For all $j \geq 1$, $\sigma_0 \in (0,1)$, and $T \to +\infty$, the expansion
   $q_j(T) = 4j^2/T^2 + O(T^{-4})$ holds, with the $T^{-3}$ coefficient identically
   zero by the parity of $\operatorname{Re}\,g(T)$ as an even function of $T$, and
   leading coefficient $j^2$ from $\sigma_0 + (1-\sigma_0) = 1$."

2. **PARTIAL:** The parity identity (Step 1) and $T^{-3}$ vanishing (Step 2) are
   confirmed, but the leading coefficient in Step 3 has an error.  Provide the
   corrected coefficient and identify which step in the algebra is wrong.

3. **REFUTED:** An explicit triple $(j, \sigma_0, T)$ where the $T^{-3}$ term in
   $q_j(T)$ is demonstrably nonzero by exact arithmetic, or where $T^2 q_j(T)
   \not\to 4j^2$.  Provide the exact rational matrix and identify the step in the
   skeleton that fails.

4. **INCONCLUSIVE:** Parity (Step 1) confirmed and $T^{-3}$ vanishing (Step 2)
   accepted, but the Step 3 computation is incomplete; reviewer states a precise
   partial result (e.g.\ "coefficient is $j^2$ for $j = 1, 2$ by direct computation
   but the general $j$ cancellation $\sigma_0 + (1-\sigma_0) = 1$ is not checked")
   and names the remaining open point.

All four outcomes are decisive and first-class.

---

## Numerical anchor (sanity only — verified by exact rational arithmetic, not an input)

### Anchor 1 ($j=1$, $T=3$, $\sigma_0 = 3/4$)

The four multiset points are $3/4 \pm 3i$ and $1/4 \pm 3i$.

**Computing $\varphi_1(3/4+3i)$:**

$$\rho^{-1}
= \frac{3/4 - 3i}{(3/4)^2 + 9}
= \frac{3/4 - 3i}{153/16}
= \frac{4}{51} - \frac{16}{51}i.$$

$$\varphi_1(3/4+3i) = 1 - \Bigl(1 - \tfrac{4}{51} + \tfrac{16}{51}i\Bigr)
= \frac{4}{51} - \frac{16}{51}i.$$

**Computing $\varphi_1(1/4+3i)$:**

$$\rho'^{-1}
= \frac{1/4 - 3i}{(1/4)^2 + 9}
= \frac{1/4 - 3i}{145/16}
= \frac{4}{145} - \frac{48}{145}i.$$

$$\varphi_1(1/4+3i) = \frac{4}{145} - \frac{48}{145}i.$$

**$q_1(3)$:**

$$q_1(3) = 4\,\operatorname{Re}\bigl[\varphi_1(3/4+3i) + \varphi_1(1/4+3i)\bigr]
= 4\Bigl[\frac{4}{51} + \frac{4}{145}\Bigr]
= 4 \cdot \frac{4 \cdot 145 + 4 \cdot 51}{51 \cdot 145}
= 4 \cdot \frac{784}{7395}
= \frac{3136}{7395}.$$

$$T^2 \cdot q_1(3) = 9 \cdot \frac{3136}{7395} = \frac{9408}{2465} \approx 3.817.$$

Expected limit: $4 \cdot 1^2 = 4$.
Finite-$T$ error: $4 - 9408/2465 = 452/2465 \approx 0.183$.

**Parity check:**

$$g(-3)
= \varphi_1(3/4-3i) + \varphi_1(1/4-3i)
= \bigl(\tfrac{4}{51}+\tfrac{16}{51}i\bigr)
  + \bigl(\tfrac{4}{145}+\tfrac{48}{145}i\bigr).$$

$\operatorname{Re}\,g(-3) = 4/51 + 4/145 = 784/7395 = \operatorname{Re}\,g(3)$.  ✓

### Anchor 2 ($j=2$, $T=3$, $\sigma_0 = 3/4$)

**Computing $\varphi_2(3/4+3i)$:**

$1 - \rho^{-1} = 47/51 + 16i/51$ (from Anchor 1).

$$(47 + 16i)^2 = 47^2 - 16^2 + 2 \cdot 47 \cdot 16\,i = 2209 - 256 + 1504i = 1953 + 1504i.$$

$$\varphi_2(3/4+3i)
= 1 - \frac{1953 + 1504i}{51^2}
= \frac{648}{2601} - \frac{1504}{2601}i
= \frac{72}{289} - \frac{1504}{2601}i.$$

**Computing $\varphi_2(1/4+3i)$:**

$1 - \rho'^{-1} = 141/145 + 48i/145$ (from Anchor 1).

$$(141 + 48i)^2 = 141^2 - 48^2 + 2 \cdot 141 \cdot 48\,i
= 19881 - 2304 + 13536i = 17577 + 13536i.$$

$$\varphi_2(1/4+3i)
= 1 - \frac{17577 + 13536i}{145^2}
= \frac{3448}{21025} - \frac{13536}{21025}i.$$

**$q_2(3)$:**

$$\frac{648}{2601} + \frac{3448}{21025}
= \frac{648 \times 21025 + 3448 \times 2601}{2601 \times 21025}
= \frac{13\,624\,200 + 8\,968\,248}{54\,686\,025}
= \frac{22\,592\,448}{54\,686\,025}.$$

$$q_2(3) = \frac{4 \times 22\,592\,448}{54\,686\,025}
= \frac{90\,369\,792}{54\,686\,025}
= \frac{10\,041\,088}{6\,076\,225}.$$

$$T^2 \cdot q_2(3) = 9 \cdot \frac{10\,041\,088}{6\,076\,225}
= \frac{90\,369\,792}{6\,076\,225} \approx 14.876.$$

Expected limit: $4 \cdot 2^2 = 16$.
Finite-$T$ error: $16 - 90\,369\,792/6\,076\,225 = 6\,849\,808/6\,076\,225 \approx 1.127$.

Quick single-entry sanity: $\operatorname{Re}\,\varphi_2(3/4+3i) = 648/2601 = 72/289$,
verified as $2601 - 1953 = 648$ and $(47+16i)^2 = 1953+1504i$.

---

## Pre-send lint notes (PROMPT_LINT.md self-check)

| Item | Status |
|---|---|
| L1 (order ≠ finite exp type) | N/A — no entire or meromorphic functions; all claims are elementary rational function asymptotics in $T$ |
| L2 (parity from functional equation) | N/A — parity here is of $g(T)$ as a function of the real variable $T$, derived from $\varphi_j(\bar\rho)=\overline{\varphi_j(\rho)}$; no $\xi$ parity used |
| L3 (zero vs pole role) | N/A — no poles or zeros of $\zeta$ appear |
| L4 (canonical product genus) | N/A — no canonical products |
| L5 (RH via divisor) | PASS — $\sigma_0$, $T$ are free real parameters; no $\zeta$-zero location assumed; no divisor over real zeros |
| L6 (vacuous target) | PASS — explicit REFUTED path provided; numerical anchors at $(j=1,T=3)$ and $(j=2,T=3)$ are non-vacuous; the $O(T^{-4})$ remainder is genuine (not 0) at finite $T$ |
| L7 (counting-function factor) | N/A — no zero-counting functions |
| L8 (global observation map + $\Sigma'$ convention) | PASS — $\mathrm{Li}_j(Z) = 2\sum_{\rho\in Z}\varphi_j(\rho)$ defined explicitly; $q_j = \mathrm{Li}_j(Q) = 4\operatorname{Re}\,g(T)$ derived with the factor tracked step by step |
| L9 (growth not assumed) | N/A — no growth claim; the expansion is a convergent Laurent series for large $|T|$ |
| L10 (power-sum ≠ Taylor jet) | N/A — no IFT or power-sum matching |
| L11 (frozen terms) | N/A |
| L12 (parity of leading discrepancy degree) | N/A — no discrepancy sequence |
| L13 (Fredholm determinant zeros) | N/A |
| L14 (per-$n$ bound) | N/A |
| L15 (zeros-in-$\Omega$) | N/A |
| L16 (representation invariance) | PASS — $q_j(T)$ is a scalar function of $T$; no matrix or basis dependence |
| L17 (cited black boxes: exact theorem number and scope) | PASS — no external citations; only the binomial theorem and elementary Laurent expansion of $(\sigma+iT)^{-1}$ are used, both self-contained and proved inline |
| L18 (numerical anchor verified by script, labeled sanity only) | PASS — Anchors 1 and 2 computed by exact rational arithmetic (SymPy/Fractions, independently verifiable); full working recorded; parity check at $T = -3$ included; labeled "sanity only, not an input" |
| L19 (honest inconclusive verdict) | PASS — four distinct outcome classes: CONFIRMED, PARTIAL, REFUTED, INCONCLUSIVE + precise localization |
| L20 (Fourier multiplier / continuous spectrum) | N/A |
| L21 (cross-theorem convention; factor $\times 2$ vs $\times 4$) | PASS — convention $\mathrm{Li}_j(Z) = 2\sum_\rho \varphi_j(\rho)$ (B2 R-symm, Paper A §2) defined explicitly in "All definitions"; the factor of 4 in $q_j = 4\operatorname{Re}\,g$ derived from first principles using conjugate-pairing, not borrowed from another theorem file |
| L22 (preprint vs published equation numbers) | N/A — no external citations |
| L23 (ordering of observation maps) | N/A |
| L24 (per-$N$ ≠ sequence non-convergence) | N/A |
| Self-containment | PASS — all symbols ($\varphi_j$, $Q$, $\mathrm{Li}_j$, $q_j$, $g$, $\sigma_0$, $T$, $j$, $c_3$) defined in-file; no "see other file" for any load-bearing formula |
