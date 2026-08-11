# Problem OB-03 — Non-uniqueness of order-1 entire functions matching finite evidence

**Type:** Classical complex analysis. Hadamard factorization + implicit function theorem.
No analytic number theory required. The sequence $\{\gamma_n\}$ below is any sequence
satisfying the stated conditions — the Riemann zero ordinates are one instance but the
result is purely about complex analysis.

**Non-circularity:** No step assumes RH. The sequence $\{\gamma_n\}$ is treated
axiomatically; the result holds for any sequence satisfying the given growth condition.

---

## All definitions (self-contained — everything is here)

### The reference entire function

Let $\{\gamma_n\}_{n \ge 1}$ be a sequence of positive reals satisfying:
- $0 < \gamma_1 < \gamma_2 < \cdots \to +\infty$.
- **Hadamard condition:** $\sum_{n \ge 1} \gamma_n^{-2} < \infty$.
- **von Mangoldt growth:** $\gamma_n \sim \frac{n}{2\pi}\log\frac{n}{2\pi}$ as $n \to \infty$.
  (Used only for the quantitative bound in Step C; Steps A–B hold with just the first two conditions.)

The **reference entire function:**
$$
\Xi(z) := C \cdot \prod_{n \ge 1} \Bigl(1 - \frac{z^2}{\gamma_n^2}\Bigr), \quad C > 0.
$$

**Properties of $\Xi$:**
- Entire of order 1 (Hadamard genus 1, since $\sum \gamma_n^{-2} < \infty$).
- Even: $\Xi(-z) = \Xi(z)$.
- Real on $\mathbb{R}$.
- All zeros real: $\pm\gamma_1, \pm\gamma_2, \ldots$
- $\Xi(0) = C$.

### The finite evidence record $\mathcal{E}_N$

Fix integers $k_N \ge 1$ (number of pinned zeros) and $J_N \ge 1$ (number of pinned Taylor
coefficients). A function $F$ **satisfies $\mathcal{E}_N$** if:
1. $F$ is entire of order 1.
2. $F(-z) = F(z)$ (even).
3. $F$ is real on $\mathbb{R}$.
4. All zeros of $F$ are real.
5. The first $k_N$ zeros of $F$ (positive real) are exactly $\gamma_1, \ldots, \gamma_{k_N}$.
6. $F(0) = C$.
7. $F^{(2j)}(0) = \Xi^{(2j)}(0)$ for $j = 0, 1, \ldots, J_N$.

---

## The theorem to be verified

**Theorem (Non-uniqueness).** For any $\varepsilon > 0$, there exists an entire function
$F \ne \Xi$ satisfying all conditions (1)–(7) of $\mathcal{E}_N$ such that:
$$
\sup_{|z| \le R_0} |F(z) - \Xi(z)| \ge \varepsilon
$$
for some $R_0 = R_0(N, \varepsilon, c_0) > \gamma_{k_N+1}$.

---

## Proof skeleton to be closed

### Step A — Perturbed tail product is entire of order 1

Fix $c_0 > 0$. For $n > k_N$ define:
$$
\mu_n := \gamma_n \Bigl(1 + \frac{c_0}{n - k_N}\Bigr) > \gamma_n > 0.
$$

Define the preliminary perturbed function:
$$
F_0(z) := C \cdot \prod_{n=1}^{k_N} \Bigl(1 - \frac{z^2}{\gamma_n^2}\Bigr) \cdot \prod_{n > k_N} \Bigl(1 - \frac{z^2}{\mu_n^2}\Bigr).
$$

**Claim A.** $F_0$ is entire of order exactly 1 (not just $\le 1$).

**Draft.** The Hadamard condition for the tail: $\mu_n > \gamma_n$, so
$\sum_{n > k_N} \mu_n^{-2} \le \sum_{n > k_N} \gamma_n^{-2} < \infty$ (by assumption).
The product converges absolutely and locally uniformly; $F_0$ is entire. Order $\le 1$
follows from $\sum \mu_n^{-2} < \infty$. Order exactly 1 (lower bound): use the
von Mangoldt growth $\gamma_n \sim n/(2\pi)\log(n/(2\pi))$ to show
$|F_0(iR)| \ge C \cdot \prod_{n: \gamma_n \le R} (1 + R^2/\mu_n^2) \ge C \cdot 2^{N(R)}$
where $N(R) \sim R\log R/(2\pi) \to \infty$, giving $\log M(r) \ge c r$ for large $r$.

**What to close for Step A:** Fill in the order-exactly-1 lower bound rigorously. Confirm
the Hadamard tail-product convergence argument is complete.

---

### Step B — Taylor coefficient matching via implicit function theorem

$F_0$ satisfies conditions (1)–(6) but generally fails condition (7). To fix this, we
use $J_N$ of the tail zero positions as free parameters.

**The Taylor coefficient system.** For the even entire function:
$$
F(z) = C \cdot \prod_{n=1}^{k_N} (1-z^2/\gamma_n^2) \cdot \prod_{n > k_N}(1-z^2/\nu_n^2),
\quad \text{with free } \nu_{k_N+1}, \ldots, \nu_{k_N+J_N} \approx \gamma_{k_N+1}, \ldots, \gamma_{k_N+J_N},
$$
and $\nu_n = \mu_n$ for $n > k_N + J_N$ (frozen). Define the target mismatch:
$$
e_j(\nu) := F^{(2j)}(0)/(2j)! - \Xi^{(2j)}(0)/(2j)!
           = - C \Bigl[\sum_{n>k_N} \nu_n^{-2j} - \gamma_n^{-2j}\Bigr] \cdot (\text{product factor}),
\quad j = 1, \ldots, J_N.
$$

**The Jacobian matrix.** Differentiating $e_j$ with respect to the free zeros
$\nu_{k_N+1}^{-2}, \ldots, \nu_{k_N+J_N}^{-2}$ (regarded as independent variables $u_l = \nu_{k_N+l}^{-2}$):
$$
\frac{\partial e_j}{\partial u_l} = - C \cdot (j)\, u_l^{j-1} \cdot (\text{bounded factor}).
$$
The leading factor gives an $J_N \times J_N$ matrix with $(j,l)$-entry proportional to
$u_l^{j-1}$. This is a **Vandermonde matrix** in $(u_1, \ldots, u_{J_N}) = (\gamma_{k_N+1}^{-2}, \ldots, \gamma_{k_N+J_N}^{-2})$.

Since $\gamma_{k_N+1} < \gamma_{k_N+2} < \cdots < \gamma_{k_N+J_N}$, the values
$u_l = \gamma_{k_N+l}^{-2}$ are distinct, and the Vandermonde determinant:
$$
\det[u_l^{j-1}]_{j,l=1}^{J_N} = \prod_{k < l}(u_l - u_k) \ne 0.
$$

By the implicit function theorem, for small $c_0$ there exist adjusted
$\nu_{k_N+1}^{(c_0)}, \ldots, \nu_{k_N+J_N}^{(c_0)}$ satisfying $e_j = 0$ for $j = 1, \ldots, J_N$.
The resulting $F$ has order 1 (the adjustment is small for small $c_0$) and satisfies all of $\mathcal{E}_N$.

**What to close for Step B:** Write out the IFT application precisely: state the implicit
function space (a neighborhood of $u_l = \gamma_{k_N+l}^{-2}$ in $\mathbb{R}^{J_N}$), verify
the target map is smooth in the free parameters, confirm the Jacobian is exactly the
Vandermonde above (up to the "bounded factor" which must be verified to be nonzero at the
base point). The key claim is: the "bounded factor" does not vanish at the unperturbed values.

---

### Step C — Quantitative separation: $F \ne \Xi$ with explicit bound

**Claim C.** For $R = \gamma_{k_N+1}$ (the first modified zero):
$$
|F(iR) - \Xi(iR)| \ge c(c_0) \cdot |\Xi(iR)| \to \infty \text{ as } N \to \infty
$$
for some $c(c_0) > 0$ depending only on $c_0$.

**Draft.** At $z = iR$, $R = \gamma_{k_N+1}$:
$$
\frac{F(iR)}{\Xi(iR)} = \prod_{n > k_N} \frac{1 + R^2/\nu_n^2}{1 + R^2/\gamma_n^2}.
$$
The $n = k_N+1$ factor (at $R = \gamma_{k_N+1}$, $\nu_{k_N+1} = \mu_{k_N+1} = \gamma_{k_N+1}(1+c_0)$):
$$
\frac{1 + \gamma_{k_N+1}^2 / \mu_{k_N+1}^2}{1 + 1} = \frac{1 + (1+c_0)^{-2}}{2} =: \eta(c_0).
$$
Note $\eta(c_0) < 1$ for $c_0 > 0$. The remaining factors (all $> 0$) contribute a product
that may differ from 1 but is bounded away from 0.

**Lower bound for $|\Xi(iR)|$:**
$$
|\Xi(iR)| = C \prod_{n \ge 1}(1 + R^2/\gamma_n^2) \ge C \prod_{n: \gamma_n \le R} 2 = C \cdot 2^{N(R)},
$$
where $N(R) = \#\{n: \gamma_n \le R\}$. By von Mangoldt, $N(R) \sim R\log R/(2\pi) \to \infty$.

Therefore $|F(iR) - \Xi(iR)| \ge (1-\eta(c_0)) \cdot |\Xi(iR)| \to \infty$, so for any
$\varepsilon > 0$ we can choose large $R$ (large $N$).

**What to close for Step C:** (i) Account for the perturbation to $\nu_{k_N+1}^{(c_0)}$ from the
Taylor-matching step — does it change $\eta(c_0)$ by a bounded or unbounded amount?
(ii) Confirm the product of remaining factors is bounded away from 0. This requires showing
the infinite tail product $\prod_{n > k_N+J_N} (1 + R^2/\mu_n^2)/(1 + R^2/\gamma_n^2)$
converges to a positive finite limit.

---

## Acceptance criteria

1. **Step A:** CONFIRMED (entire of order exactly 1) with the lower bound filled in.
2. **Step B:** CONFIRMED (IFT applies, Jacobian nonsingular) with the "bounded factor"
   verified nonzero. OR: identify any gap in the Vandermonde structure.
3. **Step C:** CONFIRMED (quantitative separation explicit) with the tail product issue
   resolved. OR: state conditions under which the tail product bound holds.
4. Overall verdict: CONFIRMED (theorem holds), PARTIAL (which steps hold), or REFUTED
   (explicit counterexample to the non-uniqueness claim).
5. An "inconclusive + partial" response is acceptable.

---

## Numerical anchor (sanity only)

Take $\{\gamma_n\} = \{n : n \ge 1\}$ (the integers — satisfies $\sum n^{-2} < \infty$,
does not satisfy von Mangoldt growth, but suffices for Steps A–B). With $k_N = 2$,
$J_N = 1$, $c_0 = 0.1$:
- $\mu_3 = 3(1 + 0.1/1) = 3.3$, $\mu_4 = 4(1 + 0.1/2) = 4.2$, etc.
- The Taylor coefficient $e_1$ (mismatch of $F''(0)$ from $\Xi''(0)$) is a concrete
  rational function of the free parameter $\nu_3^{-2}$; the IFT gives a nearby value.
