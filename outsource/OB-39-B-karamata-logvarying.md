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

The paper cites this direction as **BGT [1987] §1.7** without a theorem number.

**BGT** is: N.H. Bingham, C.M. Goldie, J.L. Teugels,
*Regular Variation*, Cambridge University Press, 1987.

**The gap:** The standard Karamata Tauberian theorem (BGT Theorem 1.7.1) states:
$$N(\Lambda)\sim C\Lambda^\alpha \;\iff\; Z(t)\sim C\,\Gamma(\alpha+1)\,t^{-\alpha}
\quad(t\to 0^+),$$
which covers only the **pure-power** case $\alpha>0$.
The **log-varying** case $N(\Lambda)\sim C\Lambda\log\Lambda$ is a slowly varying
departure from pure power, and it is not immediately obvious from Theorem 1.7.1
whether the same equivalence holds, or whether only one direction is valid.

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

A positive measurable function $L:(0,\infty)\to(0,\infty)$ is **slowly varying**
(at $+\infty$) if $L(\lambda x)/L(x)\to 1$ as $x\to+\infty$ for every $\lambda>0$.

A function $f$ is **regularly varying of index $\rho\in\RR$** if
$f(x) = x^\rho L(x)$ for some slowly varying $L$.

Examples: $L(x)=\log x$ is slowly varying.
$f(x) = x\log x$ is regularly varying of index $1$ with $L(x)=\log x$.

### The BGT Karamata Tauberian theorem (pure-power form)

**BGT Theorem 1.7.1** (as used in the paper): For $\alpha>0$ and $C>0$,
$$N(\Lambda)\sim C\Lambda^\alpha
\;\iff\;
Z(t)\sim \frac{C\,\Gamma(\alpha+1)}{t^\alpha}\quad(t\to 0^+).$$

### Log-varying Karamata (the needed direction)

The case needed for Paper B is $N(\Lambda)\sim\frac{1}{2\pi}\Lambda\log\Lambda$.
This is **not** covered directly by BGT Theorem 1.7.1 since $\alpha=1$ but with a
$\log\Lambda$ factor.  The relevant extension should be in BGT §1.7 as a corollary
or exercise, or in a companion theorem.

**Candidate statement** (to be confirmed or corrected):
For $C>0$,
$$N(\Lambda)\sim C\,\Lambda\log\Lambda
\;\Longrightarrow\;
Z(t)\sim C\,t^{-1}\log(1/t)\quad(t\to 0^+).$$

Note: only the forward direction ($N\to Z$) is needed by Paper B.

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
- convergence of $Z(t)$ for $t>0$: follows from $\gamma_n \ge 14$ (all ordinates
  above 14), so $Z(t) \le e^{-14t}/(1-e^{-t}) < \infty$.

**Claim 3 (Direction).** Confirm that the Tauberian theorem gives the implication
in the direction $N\to Z$ (not merely $Z\to N$).  The Abelian direction ($N\to Z$)
is usually the easier one (no Tauberian condition needed); the harder converse
requires a Tauberian condition on $N$.  Identify which direction the cited result covers.

---

## Proof skeleton to be closed

### Step 1 — Abelian direction: $N(\Lambda)\sim C\Lambda\log\Lambda \Rightarrow Z(t)\sim Ct^{-1}\log(1/t)$

The forward (Abelian) direction should follow by integration by parts or a direct
comparison, since it does not require a Tauberian condition.

Write
$$Z(t) = \int_0^\infty e^{-tx}\,dN(x) = t\int_0^\infty e^{-tx}N(x)\,dx$$
(integration by parts, assuming $e^{-tx}N(x)\to 0$ as $x\to\infty$, which holds
for $t>0$ since $N(x) = O(x\log x)$ and $e^{-tx}x\log x\to 0$).

Substitute $x = u/t$:
$$Z(t) = \int_0^\infty e^{-u}N(u/t)\,du.$$

Now $N(u/t)\sim C(u/t)\log(u/t) = C(u/t)(\log u - \log t)$ as $t\to 0^+$ for
each fixed $u>0$.  Dominated convergence (to be verified: the DCT exchange is
justified by showing $N(u/t)/(t^{-1}\log(1/t))$ is uniformly bounded by an
integrable function of $u$) then gives:
$$Z(t)\sim t^{-1}\log(1/t)\cdot C\int_0^\infty e^{-u}u\,du
+ t^{-1}\cdot C\int_0^\infty e^{-u}u\log u\,du.$$

Since $\int_0^\infty e^{-u}u\,du = 1$ and
$\int_0^\infty e^{-u}u\log u\,du = \Gamma'(2) = 1 - \gamma_{\rm EM}$ (finite),
the second term is $o(t^{-1}\log(1/t))$, giving:
$$Z(t)\sim C\,t^{-1}\log(1/t).$$

**What to close for Step 1:**
(a) Justify the dominated convergence exchange (find the dominating function of $u$).
(b) Confirm $\int_0^\infty e^{-u}u\log u\,du$ is $o(\log(1/t))$ relative to the
first term.
(c) State whether this argument is standard (e.g.\ as an Abelian theorem in BGT) or
requires additional input.

### Step 2 — Locate the BGT result

Identify the exact location in BGT [1987] where the log-varying case is treated.
Candidates:
- BGT §1.7 (slowly varying functions and Tauberian theory)
- BGT Theorem 1.7.4 (Tauberian for regularly varying $N$)
- BGT Corollary 1.7.3 or adjacent results

**What to close for Step 2:**
Provide the theorem number, page number, and exact statement from BGT [1987].
If the log-varying case is only the Abelian direction (no Tauberian condition),
confirm that the Abelian argument above (Step 1) suffices for Paper B's use.

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

Use the first $K=50$ ordinates of $\zeta$ (available in standard tables;
$\gamma_1\approx 14.135$, $\gamma_2\approx 21.022$, etc.) to compute:
$$R(t) := Z_{50}(t)\cdot\frac{t}{\log(1/t)},
\quad Z_{50}(t) := \sum_{n=1}^{50}e^{-\gamma_n t},$$
at $t\in\{0.01, 0.005, 0.001\}$.  The predicted limit is $\frac{1}{2\pi}\approx 0.1592$.

Quick sanity at $t=0.01$: the dominant terms are $e^{-0.01\cdot 14.135}\approx 0.869$,
$e^{-0.01\cdot 21.022}\approx 0.810$, ... so $Z_{50}(0.01)\approx 30{-}35$,
giving $R(0.01)\approx 30/\log(100) = 30/4.605\approx 6.5$.
The convergence to $1/(2\pi)\approx 0.159$ is slow (logarithmic); $K=50$ is
insufficient to observe the limit numerically.
The anchor here is therefore qualitative: confirm $Z_{50}(t)$ is computable and
verify that $Z_{50}(t)\cdot t^1$ grows like $\log(1/t)$ (not like a power of $t$).

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
| L17 (cited black boxes) | PASS — BGT exact theorem number is the deliverable; Titchmarsh Thm 9.4 cited by number |
| L18 (numerical anchor by script) | PASS — $Z_{50}(t)$ computable from standard zero tables |
| L19 (honest inconclusive verdict) | PASS — INCONCLUSIVE outcome listed |
| L20–L24 | N/A |
| Self-containment | PASS — all symbols defined; BGT full citation given |
