# Problem OB-39 — B: Karamata Tauberian theorem for log-varying counting functions

**Type:** real analysis / Tauberian theory / citation verification

**Non-circularity:** RH is not assumed.  The zeros $\gamma_n$ appear only as a
positive sequence with a known unconditional counting law; no zero-location
hypothesis (RH or otherwise) is used.  The task is to verify a Tauberian theorem
citation and check that its hypotheses hold.

---

## Background and motivation

Paper B (spectral exclusion results) uses the following implication at a critical
point in the proof of Theorem D (and Theorem D$'$):

> If $N(\Lambda) \sim \frac{1}{2\pi}\Lambda\log\Lambda$ as $\Lambda\to+\infty$,
> then $Z(t) := \sum_{n=1}^\infty e^{-\gamma_n t} \sim \frac{1}{2\pi}\,t^{-1}\log(1/t)$
> as $t\to 0^+$.

The paper applies this to $N_\zeta(\Lambda) := \#\{n : \gamma_n \le \Lambda\}$
with the Riemann–von Mangoldt asymptotic $N_\zeta(\Lambda)\sim\frac{\Lambda\log\Lambda}{2\pi}$
(Titchmarsh–Heath-Brown, unconditional), obtaining
$Z_\zeta(t)\sim\frac{1}{2\pi}\,t^{-1}\log(1/t)$.

Here the sequence $\{\gamma_n\}$ enumerates all $\gamma>0$ such that $\beta+i\gamma$
is a non-trivial zero of $\zeta$ ($0<\beta<1$), each zero counted with analytic
multiplicity; if two distinct zeros share the same imaginary part, that ordinate is
repeated.  This matches the counting convention of
$N_\zeta(T)=\#\{\rho:\,0<\Re\rho<1,\,0<\Im\rho\le T\}$ (counted with multiplicity),
ensuring the Riemann–von Mangoldt formula applies without adjustment.

The paper cites this direction as **BGT [1987] §1.7**; the precise reference is
**BGT §1.7.2, Theorem 1.7.1, p.~37**.

**BGT** is: N.H. Bingham, C.M. Goldie, J.L. Teugels,
*Regular Variation*, Cambridge University Press, 1987.

**BGT already handles the log-varying case.** BGT §1.7.2, Theorem 1.7.1, p.~37
states the Karamata Tauberian theorem for **arbitrary slowly varying factors**:
for non-decreasing right-continuous $U$, $\rho\ge 0$, $c>0$, and $\ell$ slowly
varying at $+\infty$,
$$U(x)\sim \frac{c}{\Gamma(1+\rho)}\,x^\rho\ell(x)
\;\iff\;
\widehat U(s)\sim c\,s^{-\rho}\,\ell(1/s)\quad(s\to 0^+).$$
Setting $\rho=1$, $c=C$, $\ell(x)=\log x$ and using $\Gamma(2)=1$ gives the needed
implication directly.  There is no gap; the paper need only cite BGT §1.7.2, Theorem 1.7.1.

---

## All definitions (self-contained — everything is here)

### The sequence and its counting function

Fix a positive sequence $0<\gamma_1\le\gamma_2\le\cdots$ (with multiplicity).
Define:
$$N(\Lambda) := \#\{n : \gamma_n \le \Lambda\}, \qquad
Z(t) := \sum_{n=1}^\infty e^{-\gamma_n t} \quad(t>0).$$

$Z(t)$ is the **Laplace–Stieltjes transform** of the counting measure
$\mu = \sum_{n=1}^\infty \delta_{\gamma_n}$: more precisely,
$Z(t) = \int_0^\infty e^{-tx}\,d N(x)$.

### Regular variation and slowly varying functions

A measurable function $L:(0,\infty)\to\RR$ is **slowly varying**
(at $+\infty$) if it is eventually positive (i.e.\ positive for all sufficiently
large $x$) and $L(\lambda x)/L(x)\to 1$ as $x\to+\infty$ for every $\lambda>0$.

A function $f$ is **regularly varying of index $\rho\in\RR$** if
$f(x) = x^\rho L(x)$ for some slowly varying $L$.

Examples: $L(x)=\log x$ is slowly varying (eventually positive for $x>1$; for
BGT Theorem 1.7.1, one may take $L(x)=\log x$ for $x\ge e$ with any positive
extension to $(0,e)$).

### The BGT Karamata Tauberian theorem (general slowly varying form)

**BGT §1.7.2, Theorem 1.7.1, p.~37** (Bingham–Goldie–Teugels, *Regular Variation*,
Cambridge University Press, 1987): Let $U$ be non-decreasing and right-continuous
with $U(x)=0$ for $x<0$.  Suppose $\rho\ge 0$, $c>0$, and $\ell$ is slowly varying
at $+\infty$.  Then:
$$U(x)\sim \frac{c}{\Gamma(1+\rho)}\,x^\rho\ell(x)
\;\iff\;
\widehat U(s):=\int_{[0,\infty)}e^{-sx}\,dU(x)\sim c\,s^{-\rho}\,\ell(1/s)
\quad(s\to 0^+).$$

**Application to Paper B:** Take $U=N$, $\rho=1$, $c=C=1/(2\pi)$, $\ell(x)=\log x$,
and use $\Gamma(2)=1$:
$$N(\Lambda)\sim \frac{1}{2\pi}\Lambda\log\Lambda
\;\iff\;
Z(t)\sim \frac{1}{2\pi}\,t^{-1}\log(1/t)\quad(t\to 0^+).$$

Both directions are covered by a single theorem.  Paper B uses only the Abelian
direction ($N\to Z$), which also follows directly from the Step 1 argument below.

### Log-varying case (summary)

The case needed for Paper B is $N(\Lambda)\sim\frac{1}{2\pi}\Lambda\log\Lambda$.
By BGT §1.7.2, Theorem 1.7.1 (see above), this implies
$Z(t)\sim\frac{1}{2\pi}\,t^{-1}\log(1/t)$ as $t\to 0^+$, and the converse holds too.

Only the forward direction ($N\to Z$) is needed by Paper B.

---

## The claim to be verified

**Claim 1 (Citation).** State the exact theorem number and hypothesis in
BGT [1987] that gives the implication
$N(\Lambda)\sim C\Lambda\log\Lambda \Rightarrow Z(t)\sim C\,t^{-1}\log(1/t)$.
If BGT does not contain this statement, identify the correct reference.

**Claim 2 (Hypotheses).** For the specific sequence $\{\gamma_n\}$ (nontrivial
zero ordinates of $\zeta$), verify that the hypotheses of the identified theorem hold:
- monotonicity of $N$: trivially satisfied (counting function).
- growth condition: $N(\Lambda) \sim \frac{1}{2\pi}\Lambda\log\Lambda$ is
  unconditional (Riemann–von Mangoldt, Titchmarsh [1986] Theorem 9.4).
- convergence of $Z(t)$ for $t>0$: by block estimate,
  $$Z(t)\le\sum_{k=0}^\infty e^{-tk}\,N(k+1)
  \ll \sum_{k=0}^\infty e^{-tk}(k+1)\log(k+2)<\infty$$
  for each fixed $t>0$ (group the sum $\sum_n e^{-\gamma_n t}$ by $k\le\gamma_n<k+1$;
  each block contributes at most $e^{-tk}\cdot N(k+1)$ to $Z(t)$).

**Claim 3 (Direction).** Confirm that the Tauberian theorem gives the implication
in the direction $N\to Z$ (not merely $Z\to N$).  The Abelian direction ($N\to Z$)
is usually the easier one (no Tauberian condition needed); the harder converse
requires a Tauberian condition on $N$.  Identify which direction the cited result covers.

---

## Proof skeleton to be closed

### Step 1 — Abelian direction: $N(\Lambda)\sim C\Lambda\log\Lambda \Rightarrow Z(t)\sim Ct^{-1}\log(1/t)$

The forward (Abelian) direction follows by integration by parts and dominated
convergence; no Tauberian condition is needed.

Write
$$Z(t) = \int_0^\infty e^{-tx}\,dN(x) = t\int_0^\infty e^{-tx}N(x)\,dx$$
(integration by parts; the boundary term $e^{-tx}N(x)\to 0$ as $x\to\infty$ for
each $t>0$ since $N(x)=O(x\log x)$).

Substitute $x = u/t$:
$$Z(t) = \int_0^\infty e^{-u}N(u/t)\,du.$$

**Dominating function for DCT:** Fix $A\ge e$ and $K>0$ such that $N(x)\le Kx\log x$
for all $x\ge A$, and set $M=N(A)$.  For $0<t\le e^{-1}$ and all $u>0$:
$$0\le e^{-u}\frac{N(u/t)}{t^{-1}\log(1/t)} \le e^{-u}\bigl[M + Ku(1+\log_+u)\bigr],$$
where $\log_+u=\max(\log u,0)$; the right side is integrable on $(0,\infty)$.

For each fixed $u>0$, $N(u/t)/(t^{-1}\log(1/t))\to Cu$ as $t\to 0^+$.  By DCT:
$$\frac{Z(t)}{t^{-1}\log(1/t)}\to C\int_0^\infty e^{-u}u\,du = C\cdot\Gamma(2) = C.$$

Therefore:
$$Z(t) = C\,t^{-1}\log(1/t) + o\!\bigl(t^{-1}\log(1/t)\bigr)\quad(t\to 0^+).$$

The integral $\int_0^\infty e^{-u}u\log u\,du = \Gamma'(2)=1-\gamma_{\rm EM}$ is
finite, so the $\log u$ part of $N(u/t)\sim C(u/t)(\log(1/t)+\log u)$ contributes
an $O(t^{-1})$ term, which is $o(t^{-1}\log(1/t))$.  However, the only control on
the remainder $N(x)-Cx\log x$ is $o(x\log x)$, so the $\Gamma'(2)$ computation does
not yield a genuine second asymptotic: it is not established that
$Z(t)=Ct^{-1}\log(1/t)+C(1-\gamma_{\rm EM})t^{-1}+o(t^{-1})$.

**What to close for Step 1:**
(a) Verify that $e^{-u}[M+Ku(1+\log_+u)]$ is integrable on $(0,\infty)$.
(b) Confirm $\Gamma(2)=1$ (the $\Gamma(\alpha+1)$ factor in BGT Theorem 1.7.1
    evaluates to 1 at $\rho=1$, producing no extra constant).
(c) Confirm that only the Abelian direction ($N\to Z$) is needed for Paper B;
    the Tauberian direction ($Z\to N$) is not required.

### Step 2 — BGT reference

The exact BGT reference is **§1.7.2, Theorem 1.7.1, p.~37** (full statement in
the Definitions section above).  Taking $U=N$, $\rho=1$, $c=C$, $\ell(x)=\log x$,
and $\Gamma(2)=1$ gives the needed equivalence directly.  The log-varying case is
not a gap in BGT; it is covered by the same theorem applied with a non-constant
slowly varying factor.

The Abelian direction ($N\to Z$) does not require a Tauberian condition; Paper B
uses only this direction.  Step 1 above provides an independent direct proof.

**What to close for Step 2:** Confirm that $\ell(x)=\log x$ satisfies the slowly
varying hypothesis of BGT Theorem 1.7.1 (see definition above), and that $N_\zeta$
satisfies all remaining hypotheses: non-decreasing, right-continuous, locally finite,
positive measure.

---

## Acceptance criteria

1. **CONFIRMED:** Exact BGT theorem number identified; hypotheses verified for
   $\{\gamma_n\}$; the forward direction $N\to Z$ confirmed (either as an Abelian
   theorem in BGT, or via the Step 1 argument above).  Paper B's citation is
   either exactly right or requires only the minor qualification that the Abelian
   direction does not need a Tauberian condition.

2. **PARTIAL:** The Abelian direction ($N\to Z$) is confirmed (Step 1 verified)
   but the BGT citation is imprecise (no exact theorem number found, or the §1.7
   reference does not cover exactly this case).  Report what the correct attribution
   should be (e.g.\ "standard Abelian theorem, no BGT theorem number needed").

3. **REFUTED:** The Step 1 argument has a gap (e.g.\ dominated convergence fails),
   or the counting function $N_\zeta$ does not satisfy a needed hypothesis.
   Provide the explicit obstruction.

4. **INCONCLUSIVE:** Step 1 argument unverified but no counterexample found;
   BGT reference undetermined.  State what minimal additional input would close
   the question.

---

## Numerical anchor (sanity only — not an input)

Independent computation using Odlyzko's first 50 zeros (table available at
\texttt{odlyzko/zeta\_tables/zeros1}, stated accuracy $\le3\times10^{-9}$):

$$R(t) := \frac{t\,Z_{50}(t)}{\log(1/t)},
\qquad Z_{50}(t) := \sum_{n=1}^{50}e^{-\gamma_n t}.$$

| $t$ | $Z_{50}(t)$ | $t\,Z_{50}(t)$ | $R(t)$ |
|---:|---:|---:|---:|
| 0.010 | 22.236179 | 0.222362 | 0.048285 |
| 0.005 | 32.794833 | 0.163974 | 0.030948 |
| 0.001 | 45.834795 | 0.045835 | 0.006635 |

Reference value: $1/(2\pi)=0.159155$.

**Note on fixed-$K$ limits:** For any fixed $K$,
$Z_K(t)\to K$ and $t\,Z_K(t)/\log(1/t)\to 0$ as $t\downarrow 0$.
Hence this finite-$K$ table verifies the zero-data and code only; it cannot
demonstrate the target limit $1/(2\pi)$.  To observe the asymptotic numerically,
the truncation height $T=T(t)$ must grow as $t\downarrow 0$ (requiring e.g.\
$t\,T(t)\to\infty$), and the tail $\sum_{\gamma_n>T(t)}e^{-\gamma_n t}$ must be
controlled separately.

---

## Pre-send lint notes (PROMPT_LINT.md self-check)

| Item | Status |
|---|---|
| L1 (order ≠ finite exp type) | N/A — no entire functions |
| L2 (parity) | N/A |
| L3 (zero vs pole) | N/A |
| L4 (canonical product genus) | N/A |
| L5 (RH via divisor) | PASS — $\gamma_n$ only via unconditional von Mangoldt; RH not assumed |
| L6 (vacuous target) | PASS — explicit REFUTED path (DCT fails or hypothesis fails) |
| L7 (counting-law factor) | PASS — $N_\zeta\sim\frac{1}{2\pi}\Lambda\log\Lambda$ stated explicitly; $2\pi$ factor tracked |
| L8 (global observation map) | N/A |
| L9 (growth not assumed) | PASS — $N_\zeta$ growth from Titchmarsh Thm 9.4, stated as unconditional |
| L10–L15 | N/A |
| L16 (representation invariance) | N/A |
| L17 (cited black boxes) | PASS — BGT §1.7.2, Theorem 1.7.1, p.~37 cited with exact section, theorem number, and page; Titchmarsh (2nd ed., revised by D. R. Heath-Brown, 1986) Theorem 9.4 cited by number |
| L18 (numerical anchor by script) | PASS — $Z_{50}(t)$ values independently computed from Odlyzko's first 50 zeros; fixed-$K$ limitation stated explicitly; no misinterpretation of finite truncation as the infinite-sum limit |
| L19 (honest inconclusive verdict) | PASS — INCONCLUSIVE outcome listed |
| L20–L24 | N/A |
| Self-containment | PASS — all symbols defined; BGT full citation given |
