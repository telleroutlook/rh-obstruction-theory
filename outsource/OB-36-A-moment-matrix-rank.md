# Problem OB-36 — A: Non-singularity of the real-part moment matrix for consecutive-power Li tests

**Type:** pure algebra / polynomial identity verification

**Non-circularity:** RH is not assumed anywhere. The points $\rho_k = 1/2 + it_k$ are
formal complex numbers with specified positive rational imaginary parts $t_k$; they are
**not** assumed to be zeros of $\zeta$, and no zero-location hypothesis enters any step.
No Euler product, functional equation of $\zeta$, or zero-counting law is used.

---

## Background and motivation

Paper A's Theorem A (Li collision, B2 framework) uses a matrix

$$C_{jk} = 4\,\mathrm{Re}\,\varphi_j(\tfrac{1}{2}+it_k), \qquad
  \varphi_j(\rho) = 1-(1-\rho^{-1})^j,$$

whose non-singularity is proved in Lemma 2.4 via a Chebyshev–Vandermonde reduction
(the substitution $w_k = 1-\rho_k^{-1}$, for which $|w_k|=1$ exactly, converts
$C_{jk}$ into $4(1-T_j(x_k))$ with $x_k = \mathrm{Re}(w_k)$, and a Vandermonde
argument closes the proof).

Remark 2.7 of Paper A discusses whether an analogous argument applies to the
**moment-type** test $\varphi_j(\rho) = \rho^{-j}$, for which the collision matrix
is $M_{jk} = \mathrm{Re}(z_k^j)$ where $z_k = \rho_k^{-1}$.  The current remark
(after revision) states that the Lemma 2.4 argument does not apply directly because
$z_k = \rho_k^{-1}$ does not lie on the unit circle, and that non-singularity
"requires a separate argument."

**This problem asks for independent verification of a proof sketch** that closes that
gap and establishes non-singularity for all $m$ and all distinct positive rational
$t_k$, using the identity $z_k = 1 - w_k$ and $|w_k|=1$ to redirect to the same
Vandermonde structure.

---

## All definitions (self-contained — everything is here)

### Nodes and matrices

Fix $m \geq 1$ and distinct positive rationals $t_1 < t_2 < \cdots < t_m$.  Define:

$$\rho_k = \tfrac{1}{2} + it_k \in \mathbb{C}, \qquad k = 1, \ldots, m.$$

$$z_k = \rho_k^{-1} = \frac{1/2 - it_k}{1/4 + t_k^2}
      = \underbrace{\frac{2}{1+4t_k^2}}_{a_k} - i\underbrace{\frac{4t_k}{1+4t_k^2}}_{b_k},
\qquad a_k,b_k > 0.$$

$$w_k = 1 - z_k = 1 - \rho_k^{-1}
      = \frac{4t_k^2-1}{4t_k^2+1} + i\frac{4t_k}{4t_k^2+1}.$$

$$x_k = \mathrm{Re}(w_k) = \frac{4t_k^2-1}{4t_k^2+1} \in (-1,1)
  \quad\text{(strictly increasing in }t_k).$$

The **moment collision matrix** (unnormalized) is the $m\times m$ real matrix:

$$M_{jk} = \mathrm{Re}(z_k^j), \qquad j,k = 1,\ldots,m.$$

(The paper uses $C_{jk} = 4M_{jk}$; $\det C = 4^m \det M$, so non-singularity is equivalent.)

### Chebyshev polynomials

$T_j$ denotes the degree-$j$ Chebyshev polynomial of the first kind, defined by
$T_j(\cos\theta) = \cos(j\theta)$ for $\theta \in \mathbb{R}$.  First few:
$T_0=1$, $T_1(x)=x$, $T_2(x)=2x^2-1$, $T_3(x)=4x^3-3x$.
Leading coefficient of $T_j$ (for $j\geq 1$) is $2^{j-1}$.

**Key identity** (used in Lemma 2.4): for any $z$ with $|z|=1$,
$$\mathrm{Re}(z^j) = T_j(\mathrm{Re}(z)).$$

### The polynomials $f_j$

Define, for $j \geq 1$:

$$f_j(x) = \sum_{l=0}^{j} \binom{j}{l}(-1)^l\,T_l(x).$$

Explicitly: $f_1(x)=1-x$; $f_2(x)=2x^2-2x$; $f_3(x)=-4x^3+6x^2-2$;
$f_4(x)=8x^4-16x^3+4x^2+8x-4$.
In general, $f_j$ has degree $j$ and leading coefficient $(-1)^j 2^{j-1} \neq 0$.

---

## The claim to be verified

**Claim (moment matrix non-singularity).** For all $m \geq 1$ and all distinct positive
rationals $t_1,\ldots,t_m$, the matrix $M = (M_{jk}) = (\mathrm{Re}(z_k^j))$ satisfies
$\det M \neq 0$.

---

## Proof skeleton to be closed

### Step 1 — Unit-circle identity: $|w_k|=1$

Verify that $|w_k|^2 = 1$ for every $k$.

Computation:
$$|w_k|^2 = \Bigl(\frac{4t_k^2-1}{4t_k^2+1}\Bigr)^2 + \Bigl(\frac{4t_k}{4t_k^2+1}\Bigr)^2
= \frac{(4t_k^2-1)^2+16t_k^2}{(4t_k^2+1)^2} = \frac{(4t_k^2+1)^2}{(4t_k^2+1)^2} = 1.$$

**What to close for Step 1:** confirm the displayed algebra is correct.

### Step 2 — Reduction: $M_{jk} = f_j(x_k)$

Use $z_k = 1 - w_k$ and the binomial theorem:

$$z_k^j = (1-w_k)^j = \sum_{l=0}^j \binom{j}{l}(-1)^l w_k^l.$$

Take real parts. Since $|w_k|=1$ (Step 1), the Chebyshev identity gives
$\mathrm{Re}(w_k^l) = T_l(\mathrm{Re}(w_k)) = T_l(x_k)$.  Therefore:

$$M_{jk} = \mathrm{Re}(z_k^j) = \sum_{l=0}^j \binom{j}{l}(-1)^l T_l(x_k) = f_j(x_k).$$

**What to close for Step 2:** check the Chebyshev identity is applicable (only needs
$|w_k|=1$, established in Step 1), and confirm term-by-term that the expansion of
$\mathrm{Re}(z_k^j)$ equals $f_j(x_k)$ for at least two values of $(j,k)$.

### Step 3 — Non-singularity via Vandermonde

The polynomials $f_1, f_2, \ldots, f_m$ have degrees $1, 2, \ldots, m$ and nonzero leading
coefficients $(-1)^j 2^{j-1}$.  They form a basis for the space of polynomials of degree
at most $m$ vanishing at $x=0$ (note $f_j(1)=0$ for all $j$ since $T_j(1)=1$, but that
is irrelevant here — what matters is that they have distinct degrees).

Standard linear algebra: $[f_j(x_k)]_{j,k=1}^m = A \cdot V(x_1,\ldots,x_m)$, where
$V$ is the $m\times m$ Vandermonde matrix with $V_{jk} = x_k^{j-1}$ and $A$ is a lower-
triangular matrix with diagonal entries equal to the leading coefficients of $f_j$
(up to a Vandermonde index shift — see below).

More precisely: since $f_j$ has degree $j$ and leading coefficient $c_j = (-1)^j 2^{j-1}$,

$$f_j(x) = c_j x^j + \text{lower}, \quad c_j \neq 0.$$

The evaluation matrix $[f_j(x_k)]$ can be factored as
$[f_j(x_k)] = [c_j x_k^j + \cdots] = \operatorname{diag}(c_1,\ldots,c_m)\cdot V'(x_1,\ldots,x_m)$
modulo a lower-triangular correction, where $V'_{jk} = x_k^j$.  The matrix $V'$ is a
Vandermonde with first-power rows, $\det V' = \prod_{j>k}(x_j-x_k)\cdot \prod_k x_k$... 

*Cleaner statement of the step:* The polynomials $\{f_1,\ldots,f_m\}$ span the space
$P_m = \{p \in \mathbb{R}[x] : \deg p \leq m\}$ (they have degrees $1,\ldots,m$,
hence are linearly independent).  Therefore the evaluation matrix $[f_j(x_k)]$ equals
a lower-triangular-times-Vandermonde product with nonzero diagonal.  Since the $x_k$
are distinct ($x(t)$ strictly increasing on $(0,\infty)$), $\det V \neq 0$, hence
$\det M = \det[f_j(x_k)] \neq 0$.

**What to close for Step 3:** (a) confirm that the factorization
$[f_j(x_k)] = A \cdot V(x_1,\ldots,x_m)$ holds with $A$ lower-triangular and
$\det A = \prod_j c_j \neq 0$; (b) confirm $x(t)=(4t^2-1)/(4t^2+1)$ is strictly
increasing so that distinct $t_k$ give distinct $x_k$.

### Consistency check: $m=2$ closed form

For $m=2$, substituting $b_k^2 = a_k(2-a_k)$ (which follows from $|z_k|^2 = 2a_k$,
a consequence of $|\rho_k^{-1}|^2 = 4/(1+4t_k^2) = 2\cdot 2/(1+4t_k^2) = 2a_k$):

$$\det M = a_1(a_2^2-b_2^2) - a_2(a_1^2-b_1^2)
         = a_1 a_2(a_2-a_1) + a_2 b_1^2 - a_1 b_2^2
         = 2a_1 a_2(a_2-a_1).$$

Since $a_k = 2/(1+4t_k^2) > 0$ is strictly decreasing and $t_1 < t_2$, we have
$a_1 > a_2 > 0$ and $\det M = 2a_1 a_2(a_2-a_1) < 0$.  In particular $\det M \neq 0$.

**What to close for the consistency check:** reproduce the identity
$\det M = 2a_1 a_2(a_2-a_1)$ algebraically, and verify it is nonzero for any
$0 < t_1 < t_2$.

---

## Acceptance criteria

1. **CONFIRMED:** Steps 1–3 are each verified to be correct (gaps in the sketch filled
   where noted); the $m=2$ closed form matches; the two numerical anchors below match.
   Report the accepted statement: "For all $m\geq 1$ and distinct positive rationals
   $t_k$, the moment matrix $M_{jk}=\mathrm{Re}(\rho_k^{-j})$ is non-singular over
   $\mathbb{Q}$."

2. **PARTIAL:** Steps 1–2 correct but Step 3's factorization argument has a gap; or
   confirmed for all $m \leq 3$ but with a gap for general $m$.  Provide the
   precise obstruction and, if possible, a minimal fix.

3. **REFUTED:** An explicit counterexample: distinct positive rational $t_1,\ldots,t_m$
   with $\det M = 0$.  Provide the exact rational matrix and its exact zero determinant.

4. **INCONCLUSIVE:** Steps 1–2 verified, Step 3 incomplete; reviewer can state a precise
   partial result and identify the minimal remaining open point.

All four outcomes are decisive and first-class.  The CONFIRMED verdict would
allow Remark 2.7 of Paper A to be strengthened from "requires a separate argument" to
a stated consequence of Lemma 2.4's $|w_k|=1$ identity.

---

## Numerical anchor (sanity only — verified by independent script, not an input)

**Anchor 1 ($m=2$, $t=(1,2)$):**

$$z_1 = \tfrac{2}{5}-\tfrac{4}{5}i, \quad z_2 = \tfrac{2}{17}-\tfrac{8}{17}i,
\quad x_1 = \tfrac{3}{5}, \quad x_2 = \tfrac{15}{17}.$$

$$M = \begin{pmatrix} 2/5 & 2/17 \\ -12/25 & -60/289 \end{pmatrix},
\qquad \det M = -\frac{192}{7225}.$$

Closed-form check: $2a_1 a_2(a_2-a_1) = 2\cdot\tfrac{2}{5}\cdot\tfrac{2}{17}
\cdot(\tfrac{2}{17}-\tfrac{2}{5}) = 2\cdot\tfrac{4}{85}\cdot(-\tfrac{24}{85})
= -\tfrac{192}{7225}$.  ✓

**Anchor 2 ($m=3$, $t=(1,2,3)$):**

$$M = \begin{pmatrix}
  2/5 & 2/17 & 2/37 \\
  -12/25 & -60/289 & -140/1369 \\
  -88/125 & -376/4913 & -856/50653
\end{pmatrix},
\qquad \det M = -\frac{786432}{6221454725}.$$

(Script-verified by exact rational arithmetic in SymPy; the raw numerator
$786432 = 3 \cdot 2^{18}$ and denominator $6221454725 = 5^2\cdot 17^3\cdot 37^3$
can be checked independently.)

Quick single-entry sanity: $M_{11} = \mathrm{Re}((1/2+i)^{-1}) = \mathrm{Re}(2/5-4i/5) = 2/5$.

---

## Pre-send lint notes (PROMPT_LINT.md self-check)

| Item | Status |
|---|---|
| L1 (order ≠ finite exp type) | N/A — no entire/meromorphic functions |
| L2 (parity from functional eq) | N/A |
| L3 (zero vs pole) | N/A |
| L4 (canonical product genus) | N/A |
| L5 (RH via divisor) | PASS — $\rho_k$ are free formal complex numbers; no RH hypothesis, no divisor |
| L6 (vacuous target) | PASS — $m=1$ gives $M=[a_1]>0$ non-singular trivially; $m=2$ closed form $2a_1a_2(a_2-a_1)\neq 0$ is non-vacuous; explicit refutation path exists (REFUTED verdict) |
| L7 (counting-function factor) | N/A |
| L8 (global observation map) | N/A |
| L9 (growth not assumed) | N/A |
| L10 (power-sum ≠ Taylor jet) | N/A |
| L11 (frozen terms) | N/A |
| L12 (parity of leading degree) | N/A |
| L13 (Fredholm zeros) | N/A |
| L14 (per-n bound) | N/A |
| L15 (zeros-in-Ω) | N/A |
| L16 (representation invariance) | PASS — $\det M$ is a representation-invariant scalar; $C=4M$ so $\det C = 4^m \det M$, non-singularity equivalent; noted explicitly |
| L17 (cited black boxes) | PASS — cite Chebyshev identity $\mathrm{Re}(z^j)=T_j(\mathrm{Re}(z))$ for $\vert z\vert=1$ (elementary), Vandermonde non-singularity for distinct nodes (elementary); Lemma 2.4 cited only for $\vert w_k\vert=1$ which is reproved in Step 1 |
| L18 (numerical anchor by script) | PASS — Anchors 1 and 2 independently computed by SymPy exact rational arithmetic; closed form for $m=2$ algebraically derived and checked |
| L19 (honest inconclusive verdict) | PASS — four distinct outcome classes including PARTIAL and INCONCLUSIVE |
| L20–L24 | N/A |
| Self-containment | PASS — all symbols ($\rho_k$, $z_k$, $w_k$, $x_k$, $T_j$, $f_j$, $M$) defined in-file; no "see other file" for load-bearing content |
