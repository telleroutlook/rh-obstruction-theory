# Problem OB-01 — Heat-trace log singularity vs. Seeley-DeWitt no-log theorem

**Type:** Spectral theory / PDE. This is a citation-verification + exception-confirmation
task. The theorems are classical; the deliverable is precise theorem numbers and
confirmation of the log-polyhomogeneous exception.

**Non-circularity:** No step in this problem involves the Riemann zeta function,
zero locations, or RH. Everything is pure operator theory on compact manifolds.

---

## What you need to verify (three independent claims)

### Claim A — Seeley-DeWitt: no logarithmic terms for classical elliptic operators

**Setting (fully self-contained).**
Let $M$ be a compact smooth Riemannian manifold without boundary, $\dim M = d \ge 1$.
Let $H$ be a positive-definite classical pseudodifferential operator on $M$ of order
$m > 0$, with positive spectrum $\{\lambda_n\}_{n \ge 1}$, $\lambda_n \to +\infty$.

A **classical** pseudodifferential operator of order $m$ has principal symbol
$\sigma_m(x,\xi)$ that is smooth, homogeneous of degree $m$ in $\xi$ for $|\xi| \ge 1$,
and admits a full symbol expansion
$$
\sigma(x,\xi) \sim \sigma_m(x,\xi) + \sigma_{m-1}(x,\xi) + \sigma_{m-2}(x,\xi) + \cdots
$$
with $\sigma_{m-j}$ homogeneous of degree $m-j$ in $\xi$. **No $\log|\xi|$ terms appear.**

Define the operator heat trace:
$$
Z_H(t) := \operatorname{Tr}(e^{-tH}) = \sum_{n \ge 1} e^{-t\lambda_n}, \quad t > 0.
$$

**Claim A.** As $t \to 0^+$:
$$
Z_H(t) \sim \sum_{k=0}^\infty a_k\, t^{(k-d)/m},
$$
where each $a_k$ is a local geometric invariant (integral over $M$ of a density built
from the symbol of $H$ and the metric) and **no term of the form $t^\alpha \log(1/t)$
appears for any $\alpha \in \mathbb{R}$**.

More precisely: for every $K \ge 0$,
$$
\left| Z_H(t) - \sum_{k=0}^{K} a_k\, t^{(k-d)/m} \right| = O\!\left(t^{(K+1-d)/m}\right)
\text{ as } t \to 0^+,
$$
with no logarithmic correction.

**Task for Claim A.** Confirm this statement is correct, and supply the precise theorem
reference (author, book/journal, edition, theorem number) from one or more of:

- Berline–Getzler–Vergne, *Heat Kernels and Dirac Operators* (Springer, 2004 corrected
  printing of 1992 edition). Our proof draft cites "Thm 2.30" — please confirm whether
  this is the correct theorem number for the full polyhomogeneous expansion with no-log,
  or give the correct number.
- Gilkey, *Invariance Theory, the Heat Equation, and the Atiyah-Singer Index Theorem*
  (2nd ed., CRC Press, 1995). Our proof draft cites "Thm 1.8.1" — please confirm or
  correct.
- Seeley, "Complex powers of an elliptic operator," *Proc. Symp. Pure Math.* **10** (1967).

Any one confirmed reference suffices. If all three have a different theorem number than
cited, supply the correct one.

---

### Claim B — Manifolds with boundary

**Claim B.** For compact manifolds **with** boundary (standard local elliptic boundary
conditions), the heat-trace expansion is:
$$
Z_H(t) \sim \sum_{k=0}^\infty b_k\, t^{(k-d)/m} + \sum_{k=0}^\infty b'_k\, t^{(k-d+1)/m}
$$
(two series, one from interior terms, one from boundary terms — possibly with half-integer
exponents), still with **no logarithmic terms**.

**Task for Claim B.** Confirm whether this is correct, or state the exact condition under
which logarithmic terms can appear for manifolds with boundary. Cite the relevant theorem
(Grubb–Seeley, or Gilkey, or equivalent). For Theorem D in our program, the operator
class $\mathcal{C}_\text{ell}$ is defined to include only compact manifolds **without
boundary** — confirm that this restriction is sufficient to exclude all logarithmic terms.

---

### Claim C — Log-polyhomogeneous operators: logarithmic terms DO appear

**Setting.** A **log-polyhomogeneous** operator of order $m$ on a $d$-dimensional compact
manifold has symbol expansion
$$
\sigma(x,\xi) \sim \sum_{j \ge 0} \bigl[\sigma_{m-j}(x,\xi) + \tau_{m-j}(x,\xi)\,\log|\xi|\bigr]
$$
for $|\xi| \ge 1$, where $\sigma_{m-j}$ and $\tau_{m-j}$ are homogeneous of degree $m-j$
in $\xi$. (This class was introduced in Schrohe 1992 and studied in Lesch 1995,
Grubb–Seeley 1995.)

**Claim C.** For $H$ a log-polyhomogeneous operator of order $m$ on a compact $d$-manifold,
the heat-trace expansion acquires additional terms of the form:
$$
Z_H(t) \sim \cdots + c_0\, t^{-d/m} \log(1/t) + \cdots \quad \text{as } t \to 0^+.
$$
The coefficient $c_0$ is determined by the leading log-symbol coefficient $\tau_m(x,\xi)$
via:
$$
c_0 = \frac{1}{m\,(2\pi)^d} \int_{S^*M} \operatorname{tr}(\tau_m)\, dS,
$$
where $S^*M$ is the cosphere bundle and $dS$ is the canonical measure.

**Specific sub-case of interest.** For $d = 1$, $m = 1$ (operator on a compact
1-manifold, i.e., a circle), with $\tau_1(x,\xi) = c \cdot |\xi|^0$ (i.e., $\tau_1 = c$,
a constant):
$$
c_0 = \frac{c}{1 \cdot 2\pi} = \frac{c}{2\pi}.
$$
By choosing $c = 1$ (i.e., $\tau_1 \equiv 1$), we can arrange $c_0 = (2\pi)^{-1}$.

**The Riemann context (for orientation only — not an input to your proof).**
The Riemann zeta zero-counting function satisfies $N_\zeta(T) \sim T\log T / (2\pi)$,
and the associated heat trace satisfies $Z_\zeta(t) \sim (2\pi)^{-1} \log(1/t)/t$
as $t \to 0^+$. Claim C says a log-polyhomogeneous operator with $c_0 = (2\pi)^{-1}$
(achievable by choosing $\tau_1 \equiv 1$ on the circle) can match this singularity type.
This is why the log-polyhomogeneous class is an escape route from Theorem D.

**Task for Claim C.** Confirm the coefficient formula $c_0 = (m(2\pi)^d)^{-1} \int_{S^*M}\operatorname{tr}(\tau_m)\,dS$, citing the source (Schrohe 1992, Lesch 1995, or Grubb–Seeley 1995 with theorem number). Confirm the $d=1, m=1$ computation $c_0 = c/(2\pi)$.

---

## Acceptance criteria

1. **Claim A:** CONFIRMED or REFUTED, with exact theorem number and edition for the
   no-log expansion. If our cited "BGV Thm 2.30" or "Gilkey Thm 1.8.1" is wrong,
   supply the correct reference.
2. **Claim B:** Confirm no-log holds without boundary, state the condition with boundary.
3. **Claim C:** CONFIRMED or REFUTED, with exact source for the $c_0$ formula.
   If the formula is wrong, supply the correct one.
4. If any claim is false as stated: explicit counterexample (a classical elliptic
   operator on a compact manifold that has a $\log(1/t)$ term in its heat trace).
5. An "inconclusive + partial" response is acceptable if you can confirm some claims
   but not others — state precisely which are confirmed and which remain open.

---

## Numerical anchor (sanity only — not an input)

For the Laplacian on the flat torus $\mathbb{T}^d$ (order $m=2$, dimension $d$):
$Z_\Delta(t) = \sum_{n \in \mathbb{Z}^d} e^{-t|n|^2} \sim (4\pi t)^{-d/2}$ as $t \to 0^+$,
with no $\log$ terms. This is a classical fact consistent with Claim A.
