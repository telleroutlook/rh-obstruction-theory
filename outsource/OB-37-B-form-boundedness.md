# Problem OB-37 — B: P-form boundedness of log-polyhomogeneous sub-principal perturbations

**Type:** pure functional analysis / pseudodifferential operators on compact manifolds

**Non-circularity:** RH is not assumed anywhere.  No zeta function, no zeros of $\zeta$,
no Euler product, no zero-counting law, and no zero-location hypothesis appear in any
step.  The result is entirely internal to elliptic operator theory on a closed smooth
manifold.  The operator $H = P + Q$ and its spectral properties are used in Paper B to
define a method class; the form-boundedness statement here is a pure functional-analytic
input to that definition, independent of number-theoretic content.

---

## Background and motivation

Paper B (spectral exclusion) studies operators of the form $H = P + Q$ on a closed
smooth manifold $M$, where $P$ is a positive classical elliptic pseudodifferential
operator of order $m > 0$ and $Q$ arises from log-polyhomogeneous sub-principal terms.
The structural obstruction theorem (Theorem D') requires that $H$ be semibounded and
that its quadratic form domain equal $H^{m/2}(M)$ — the same as that of $P$.

The sufficient condition for form-domain equality is **$P$-form boundedness of $Q$ with
relative bound less than $1$**: there exist $\delta \in (0,1)$ and $C_\delta < \infty$
such that $|q_Q[u]| \leq \delta\,q_P[u] + C_\delta\|u\|^2$ for all $u \in H^{m/2}(M)$.

The log-polyhomogeneous sub-principal condition forces $Q$ to have symbol in
$\Psi^{m-1+\varepsilon}_{1,0}(M)$ for every $\varepsilon \in (\max\{0,1-m\},1)$, which implies
order strictly less than $m$.  The standard tools (pseudodifferential Sobolev mapping,
Sobolev interpolation, sharp Gårding) then combine to give form boundedness with
arbitrarily small relative bound $\delta > 0$.

**This problem asks for independent verification of the four-step proof chain** that
establishes this form bound, with explicit constants, for all $m > 0$.

---

## All definitions (self-contained — everything is here)

### Manifold and function spaces

$M$ is a closed (compact, without boundary) smooth Riemannian manifold of dimension
$d \geq 1$.

$H^s(M)$ for $s \in \mathbb{R}$ denotes the $L^2$-based Sobolev space on $M$, with norm
$\|u\|_{H^s}^2 = \|(\mathrm{Id} - \Delta_g)^{s/2} u\|_{L^2}^2$,
where $\Delta_g$ is the (non-positive) Laplace–Beltrami operator.  In particular:
$H^0(M) = L^2(M)$, $\|u\|_{H^0} = \|u\|$.

### Classical elliptic pseudodifferential operator $P$

$P \in \Psi^m_{\mathrm{cl}}(M)$ is a classical pseudodifferential operator of order $m > 0$,
self-adjoint and positive: $\langle Pu, u\rangle \geq 0$ for all $u \in C^\infty(M)$.

**Principal symbol:** $h_m(x,\xi) \in C^\infty(T^*M \setminus 0)$, homogeneous of
degree $m$ in $\xi$, satisfying
$$h_m(x,\xi) \geq c|\xi|^m \quad \forall\,(x,\xi) \in T^*M \setminus 0,$$
for some constant $c > 0$ (using any smooth Riemannian norm $|\cdot|$ on $T^*_xM$).
This is the **ellipticity condition**.

**Domain and quadratic form:** $P$ has form domain $\mathrm{dom}(q_P) = H^{m/2}(M)$ and
quadratic form $q_P[u] = \langle Pu, u\rangle$ for $u \in H^{m/2}(M)$.

### Sub-principal perturbation $Q$

$Q \in \bigcap_{\varepsilon \in (0,1)} \Psi^{m-1+\varepsilon}_{1,0}(M)$
is a pseudodifferential operator satisfying: for every $\varepsilon \in (0,1)$,
the order of $Q$ is at most $m - 1 + \varepsilon$.

This assumption implies membership in some $\Psi^r_{1,0}$ with $r < m$; the proof only
uses that weaker consequence.  (The specific log-polyhomogeneous origin forces exactly
the intersection $\bigcap_{\varepsilon>0}\Psi^{m-1+\varepsilon}_{1,0}$; all that is used
below is membership in $\Psi^{m-1+\varepsilon}_{1,0}$ for a fixed $\varepsilon \in
(\max\{0,1-m\},1)$.)

$Q$ is assumed formally self-adjoint (so that $q_Q[u] = \langle Qu, u\rangle \in
\mathbb{R}$ for $u \in C^\infty(M)$), but the bound $|q_Q[u]|$ is stated in absolute
value to cover the general case.

**Quadratic form of $Q$:** For any chosen $\varepsilon \in (\max\{0,1-m\},1)$, put
$r = m-1+\varepsilon \in (0,m)$.  The mapping theorem gives
$Q : H^{r/2}(M) \to H^{-r/2}(M)$, so define
$$q_Q[u] := {}_{H^{-r/2}}\langle Qu, u \rangle_{H^{r/2}},
\qquad u \in H^{m/2}(M) \hookrightarrow H^{r/2}(M),$$
first on $C^\infty(M)$ where it agrees with the $L^2$ inner product, then extended by
density and continuity.  Formal self-adjointness ensures $q_Q[u] \in \mathbb{R}$.

### The claim

For every $\delta > 0$ there exists $C_\delta < \infty$ such that
$$|q_Q[u]| \leq \delta\,\langle Pu,u\rangle + C_\delta\,\|u\|^2
\quad \forall\,u \in H^{m/2}(M). \tag{FB}$$

---

## Proof skeleton to be closed

### Step 1 — Pseudodifferential Sobolev mapping

Choose $\varepsilon \in (\max\{0,1-m\},1)$, and put $r = m-1+\varepsilon \in (0,m)$ and
$\theta = r/m \in (0,1)$.  Since $Q \in \Psi^{m-1+\varepsilon}_{1,0}(M)$, the standard
pseudodifferential Sobolev mapping theorem (Taylor, *Short Course on Pseudodifferential
Operators*, I.(3.31), localized to closed manifolds via §I.8) gives:
$Q$ is a bounded operator
$$Q : H^{s + r/2}(M) \to H^{s - r/2}(M)
\quad \forall\,s \in \mathbb{R},$$
with operator norm $\|Q\|_{s+r/2 \to s-r/2} \leq C_1$
for a constant $C_1 = C_1(Q, r, s, M)$.

Setting $s = 0$: $Q : H^{r/2}(M) \to H^{-r/2}(M)$ with norm $C_Q := \|Q\|_{H^{r/2}\to H^{-r/2}}$.
By the $H^{-r/2}$-$H^{r/2}$ duality pairing:
$$|q_Q[u]| \leq C_Q\,\|u\|_{H^{r/2}}^2. \tag{1}$$

**What to close for Step 1:** Confirm the cited Sobolev mapping theorem applies with the
given regularity indices.  Confirm that the duality pairing
$H^{r/2} \times H^{-r/2} \to \mathbb{C}$ is the correct one to bound $|q_Q[u]|$.

### Step 2 — Sobolev interpolation

On a closed manifold with spectral Sobolev norms, the Laplace–Beltrami operator
$A = I - \Delta_g$ has a discrete spectral decomposition; Hölder's inequality on the
eigenvalue weights gives the interpolation inequality with constant 1: for
$0 \leq \theta \leq 1$ and $s_0 < s_1$, setting $s_\theta = (1-\theta)s_0 + \theta s_1$,
$$\|u\|_{H^{s_\theta}} \leq \|u\|_{H^{s_0}}^{1-\theta}\,\|u\|_{H^{s_1}}^\theta.$$

Apply with $s_0 = 0$, $s_1 = m/2$, $s_\theta = r/2$, so
$\theta = r/m \in (0,1)$ (valid since $r = m-1+\varepsilon \in (0,m)$ by the choice
of $\varepsilon$ in Step 1):
$$\|u\|_{H^{r/2}} \leq \|u\|^{1-\theta}\,\|u\|_{H^{m/2}}^\theta.$$

For any $\eta > 0$, the scaling Young inequality
$X^\theta Y^{1-\theta} \leq \eta X + C(\eta,\theta) Y$ gives:
$$\|u\|_{H^{r/2}}^2 \leq \eta\,\|u\|_{H^{m/2}}^2 + C(\eta,\theta)\,\|u\|^2,
\tag{2}$$
with explicit constant
$$C(\eta,\theta) = (1-\theta)\left(\frac{\theta}{\eta}\right)^{\theta/(1-\theta)}.$$

**What to close for Step 2:** Carry out the Young inequality explicitly to confirm the
formula for $C(\eta,\theta)$.  Note that $\theta \in (0,1)$ for the chosen
$\varepsilon \in (\max\{0,1-m\},1)$, so both exponents $1/\theta$ and $1/(1-\theta)$
are finite and $>1$.

### Step 3 — Sharp Gårding inequality for $P$

Since $P \in \Psi^m_{\mathrm{cl}}(M)$ is positive elliptic with principal symbol
$h_m(x,\xi) \geq c|\xi|^m$, the sharp Gårding inequality (Taylor, *Short Course on
Pseudodifferential Operators*, I.(4.18)–I.(4.19), localized to closed manifolds via
§I.8) gives:
$$\langle Pu, u\rangle \geq c_0\,\|u\|_{H^{m/2}}^2 - C_P\,\|u\|^2
\quad \forall\,u \in H^{m/2}(M), \tag{3}$$
where $c_0 > 0$ may be chosen proportional to $c$, and $C_P < \infty$ depends on
finitely many seminorms of the full symbol of $P$ (including derivatives of the
principal symbol), as well as the fixed metric, atlas, partition of unity, and
quantization.

Rearranging: $\|u\|_{H^{m/2}}^2 \leq c_0^{-1}(\langle Pu,u\rangle + C_P\|u\|^2)$. \tag{3'}$

**What to close for Step 3:** Confirm (3) holds for a positive classical elliptic $P$
with $h_m \geq c|\xi|^m$, and give the explicit dependence of $c_0$ and $C_P$ on the
data.  In particular, confirm that $c_0 > 0$ may be chosen proportional to $c$, and
that $C_P$ depends on finitely many seminorms of the full symbol of $P$ (not just
lower-order terms).

### Step 4 — Combining to give (FB)

If $C_Q = 0$, then $q_Q = 0$ and (FB) holds trivially with any $\delta > 0$ and
$C_\delta = 0$.  Assume henceforth $C_Q > 0$.

Substitute (3') into (2) and then (2) into (1):

$$|q_Q[u]| \leq C_Q\,\|u\|_{H^{r/2}}^2
\leq C_Q\Bigl(\eta\,\|u\|_{H^{m/2}}^2 + C(\eta,\theta)\|u\|^2\Bigr)$$

$$\leq C_Q\,\eta\,c_0^{-1}\Bigl(\langle Pu,u\rangle + C_P\|u\|^2\Bigr)
  + C_Q\,C(\eta,\theta)\,\|u\|^2$$

$$= \underbrace{C_Q\,\eta\,c_0^{-1}}_{=:\,\delta}\,\langle Pu,u\rangle
  + \underbrace{\bigl(C_Q\,\eta\,c_0^{-1}\,C_P + C_Q\,C(\eta,\theta)\bigr)}_{=:\,C_\delta}\,\|u\|^2.$$

Given any target $\delta > 0$, choose $\eta = \delta\,c_0 / C_Q$, which yields
(FB) with
$$C_\delta = C_Q\,(1-\theta)\left(\frac{\theta\,C_Q}{\delta\,c_0}\right)^{\theta/(1-\theta)}
  + \delta\,C_P. \tag{4}$$

**What to close for Step 4:** (a) Confirm the chain of inequalities above is correct
(no terms dropped or reversed).  (b) Confirm that the constant $C_\delta$ produced by
construction (4) satisfies $C_\delta \to +\infty$ as $\delta \to 0^+$ when $C_Q > 0$
and $0 < \theta < 1$ (since $C(\eta,\theta) \to \infty$ as $\eta \to 0^+$).  This is
the divergence of the proof-constructed constant; it does not preclude a finite $C_\delta$
if $Q$ has additional properties making $C_Q = 0$.
(c) State explicitly what $C_\delta$ depends on: the operator norm $C_Q$, the ellipticity
constant $c$ of $P$ (via $c_0$), the full symbol seminorms of $P$ (via $C_P$), and the
interpolation exponent $\theta = r/m$ (via $C(\eta,\theta)$).

---

## Acceptance criteria

1. **CONFIRMED:** Steps 1–4 are each verified to be correct; the chain of inequalities
   in Step 4 is reproduced end-to-end with explicit constants matching formula (4);
   the numerical anchor below is reproduced.
   Report the accepted statement: "For $P \in \Psi^m_{\mathrm{cl}}(M)$ positive
   elliptic with $h_m \geq c|\xi|^m$ and $Q \in \bigcap_{\varepsilon \in
   (\max\{0,1-m\},1)}\Psi^{m-1+\varepsilon}_{1,0}(M)$ formally self-adjoint,
   inequality (FB) holds for every $\delta > 0$ with $C_\delta$ given by (4), which
   depends on the chosen $r = m-1+\varepsilon$, the operator norm
   $C_Q = \|Q\|_{H^{r/2}\to H^{-r/2}}$, the Gårding constants $c_0$ and $C_P$, and
   the interpolation exponent $\theta = r/m$."

2. **PARTIAL:** Steps 1–3 correct but Step 4 has a gap (e.g., the explicit Young
   constant $C(\eta,\theta)$ cannot be confirmed, or the $C_Q=0$ case is not separated).
   Provide the precise obstruction and, if possible, a minimal fix or a precise
   sufficient condition that closes the gap.

3. **REFUTED:** An explicit counterexample: a closed manifold $M$, a positive elliptic
   $P$, a $Q \in \bigcap_{\varepsilon \in (\max\{0,1-m\},1)}\Psi^{m-1+\varepsilon}_{1,0}$, and a sequence
   $u_n \in H^{m/2}(M)$ with $|q_Q[u_n]|/(\langle Pu_n,u_n\rangle + \|u_n\|^2)
   \to \infty$.  Provide the exact construction.

4. **INCONCLUSIVE:** Steps 1–3 verified but Step 4 incomplete; reviewer states the
   precise partial result (e.g., confirmed for $m \geq 1$ only) and identifies the
   minimal remaining open point.

All four outcomes are decisive and first-class.

---

## Numerical anchor (sanity only — verified by Fourier mode computation, not an input)

**Setting:** $M = S^1 = \mathbb{R}/(2\pi\mathbb{Z})$, $d = 1$, $m = 2$.

$$P = -\tfrac{d^2}{dx^2} + 1 \in \Psi^2_{\mathrm{cl}}(S^1),
\quad h_2(\xi) = \xi^2 \geq 0, \quad \text{ellipticity: } h_2 + 1 \text{ gives }
\langle Pu,u\rangle = \|u'\|^2 + \|u\|^2 \geq \|u\|^2_{H^1}.$$

(Here $P$ acts as $P u = -u'' + u$ and $c = 1$, $c_0 = 1$, $C_P = 0$ in (3).)

$$Q = i\tfrac{d}{dx} \in \Psi^1_{\mathrm{cl}}(S^1), \quad \mathrm{ord}(Q) = 1 = m-1.$$

Since $\mathrm{ord}(Q) = 1 < 2 = m$, we have $Q \in \Psi^{m-1+\varepsilon}$ for every
$\varepsilon > 0$ (trivially, as $1 < 1 + \varepsilon$).  The operator $Q = i\,d/dx$
is formally self-adjoint on $L^2(S^1)$.

**Fourier modes:** For $n \in \mathbb{Z}$, let $u_n(x) = e^{inx}/\sqrt{2\pi}$,
so $\|u_n\| = 1$.  Then:
$$Pu_n = (n^2+1)u_n, \quad \langle Pu_n, u_n\rangle = n^2 + 1.$$
$$Qu_n = i(in)u_n = -n\,u_n, \quad q_Q[u_n] = \langle Qu_n,u_n\rangle = -n.$$

Therefore $|q_Q[u_n]| = |n|$.

**Form bound check (AM-GM):** By the arithmetic-geometric mean inequality
$n^2 + 1 \geq 2|n|$, we have:
$$|n| \leq \tfrac{1}{2}(n^2+1) = \tfrac{1}{2}\langle Pu_n,u_n\rangle.$$

So (FB) holds for Fourier modes with $\delta = 1/2$, $C_\delta = 0$.  For any $\delta > 0$, the explicit (generally non-optimal) proof constant $C_\delta = 1/(4\delta)$
satisfies $|n| \leq \delta(n^2+1) + 1/(4\delta)$ for all $n \in \mathbb{Z}$.

**Verification:** $\delta n^2 - |n| + \delta + 1/(4\delta) = \delta(|n| - 1/(2\delta))^2 + \delta \geq 0$. ✓

This matches (4): $C_\delta = C_Q\,C(\eta,\theta) + \delta\,C_P$ with $C_Q = 1$
(norm of $Q : H^{1/2} \to H^{-1/2}$), $C_P = 0$ (no lower-order part of $P$),
and $C(\eta,\theta) = 1/(4\eta)$ from the explicit Young formula with $\theta = 1/2$
(interpolation exponent for $H^{1/2}$ between $L^2$ and $H^1$) and $\eta = \delta c_0/C_Q = \delta$.
The value $1/(4\delta)$ is the bound produced by the proof construction; the minimum
non-negative constant over $n \in \mathbb{Z}$ is $\max\{0,\,1/(4\delta)-\delta\}$ and
generally differs from $1/(4\delta)$.

---

## Pre-send lint notes (PROMPT_LINT.md self-check)

| Item | Status |
|---|---|
| L1 (order ≠ finite exponential type) | N/A — no entire or meromorphic functions appear |
| L2 (parity from functional equation) | N/A |
| L3 (zero vs pole role) | N/A |
| L4 (canonical product genus) | N/A |
| L5 (RH via divisor) | PASS — no RH, no zeta, no zero locations; purely functional analytic |
| L6 (vacuous target) | PASS — $S^1$ example is a non-vacuous confirmed instance; REFUTED verdict requires explicit counterexample with construction |
| L7 (counting-function factors) | N/A |
| L8 (global observation map) | N/A |
| L9 (growth not assumed) | N/A |
| L10 (power-sum ≠ Taylor jet) | N/A |
| L11 (dropped frozen terms) | PASS — boundary terms absent ($M$ has no boundary); all terms in Steps 1–4 accounted for; $C(\eta,\theta)$ and $C_P$ both retained in (4) |
| L12 (parity of leading degree) | N/A |
| L13 (Fredholm zeros) | N/A |
| L14 (per-$n$ bound vs uniform) | PASS — (FB) is a uniform bound over all $u \in H^{m/2}(M)$; the Fourier-mode check is per-$n$ (sanity only) |
| L15 (zeros-in-$\Omega$ vs zeros-in-$\mathbb{C}$) | N/A |
| L16 (representation invariance) | PASS — (FB) is invariant under unitary conjugation: if $U$ is unitary on $L^2(M)$ and $P' = UPU^*$, $Q' = UQU^*$, then $\langle P'u',u'\rangle = \langle Pu,u\rangle$ and $|q_{Q'}[u']| = |q_Q[u]|$ with $u' = Uu$; the bound is representation-independent |
| L17 (cited black boxes exact) | PASS — cites: pseudodifferential Sobolev mapping theorem (Taylor, *Short Course*, I.(3.31), §I.8); Sobolev interpolation (spectral decomposition + Hölder, constant 1, self-contained); sharp Gårding inequality (Taylor, *Short Course*, I.(4.18)–I.(4.19), §I.8); each cited for the exact result used with precise reference |
| L18 (numerical anchors by script) | PASS — Fourier-mode anchor computed by explicit eigenvalue formula; AM-GM bound and optimal-$C_\delta$ formula derived algebraically; no floating-point arithmetic |
| L19 (honest inconclusive verdict) | PASS — four distinct outcome classes (CONFIRMED, PARTIAL, REFUTED, INCONCLUSIVE) each with precise triggering condition |
| Self-containment | PASS — all symbols ($M$, $d$, $H^s(M)$, $P$, $Q$, $h_m$, $c$, $q_P$, $q_Q$, $c_0$, $C_Q$, $C_P$, $C(\eta,\theta)$, $\theta$, $r$) defined in-file; proof references cite theorem numbers; no "see other file" for load-bearing content |
