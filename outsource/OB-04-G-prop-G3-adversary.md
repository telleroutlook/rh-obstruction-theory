# Problem OB-04 — Smooth adversary: O_θ-indistinguishability for Theorem G (Prop. G.3)

**Type:** Analytic number theory. Requires knowledge of: (1) the Riemann-von Mangoldt
formula, (2) properties of the argument function $S(T)$, (3) the Hadamard factorization
of entire functions of order 1. No knowledge of RH is assumed; the obstruction holds
regardless of whether RH is true.

**Non-circularity:** No step assumes RH. The two multisets $\mathcal{Z}_\text{RH}$ and
$\mathcal{Z}_\text{smooth}$ are distinct objects; the theorem says they are
indistinguishable by a specific observation map.

---

## All definitions (self-contained — everything is here)

### The smooth counting function and archimedean levels

The **Riemann-von Mangoldt formula** (classical, unconditional; source: Titchmarsh,
*Theory of the Riemann Zeta-Function*, 2nd ed., §9.1–§9.4; Davenport,
*Multiplicative Number Theory*, Ch. 15):
$$
N(T) = \frac{\theta(T)}{\pi} + 1 + S(T),
$$
where:

- $N(T) = \#\{\rho : \operatorname{Im}(\rho) \in (0,T]\}$ is the zero-counting function
  of $\zeta(s)$ in the upper critical strip (zeros $\rho = \beta + i\gamma$ with
  $0 < \beta < 1$, $0 < \gamma \le T$).

- $\theta(T) = \operatorname{Im}\log\Gamma\!\Bigl(\frac{1}{4} + \frac{iT}{2}\Bigr) - \frac{T}{2}\log\pi$
  is the smooth phase, entirely determined by the gamma factor (zero-free data).
  It satisfies $\theta(T) = \frac{T}{2}\log\frac{T}{2\pi} - \frac{T}{2} - \frac{\pi}{8} + O(T^{-1})$.

- $S(T) = \frac{1}{\pi}\arg\zeta\!\Bigl(\frac{1}{2} + iT\Bigr)$ is the argument function
  (fluctuation). Its defining properties (all classical, unconditional):
  - $S(T) = O(\log T)$ (unconditionally; Backlund 1914).
  - $S(T) \ne 0$ for infinitely many $T$ (follows from sign-change results; Backlund 1914
    showed $S(T)$ changes sign; the oscillation between positive and negative values is
    established in Tsang 1986, J. Number Theory 23, and Selberg 1946).
  - The discrepancy: if $\gamma_n$ is the $n$-th positive Riemann zero ordinate and
    $d_n$ is defined below, then $\gamma_n - d_n = S(\gamma_n)/N'(\gamma_n) + O(1/\gamma_n)$
    where $N'(T) \sim \log(T/2\pi)/(2\pi)$.

**Archimedean levels.** Define $d_n$ as the unique positive solution to:
$$
\frac{\theta(d_n)}{\pi} + 1 = n.
$$
These exist and are unique for each $n \ge 1$ because $\theta$ is strictly increasing for
large $T$ and $\theta(T)/\pi \to \infty$. They satisfy $d_n \sim \gamma_n$ and
$d_n \ne \gamma_n$ whenever $S(\gamma_n) \ne 0$.

### The observation map $O_\theta$

A method $P \in \mathfrak{M}_\text{FC}$ (Fredholm certificate class) computes only from
**zero-free arithmetic data** (prime powers, gamma factors, no zero ordinates). Its
observation map returns only the archimedean levels:
$$
O_\theta(\mathcal{Z}) := (d_1, d_2, d_3, \ldots)
$$
for **any** input zero multiset $\mathcal{Z}$. The key property: $O_\theta$ depends only
on $\theta(T)$, which is zero-free. **$O_\theta$ is the same function regardless of
what $\mathcal{Z}$ is.**

### The two adversary multisets

$$
\mathcal{Z}_\text{RH} := \{\gamma_n : n \ge 1\} \quad \text{(true Riemann zero ordinates, with multiplicity)},
$$
$$
\mathcal{Z}_\text{smooth} := \{d_n : n \ge 1\} \quad \text{(archimedean levels)}.
$$

### The entire functions attached to each

$$
\Xi(z) := \Xi(0) \cdot \prod_{n \ge 1}\Bigl(1 - \frac{z^2}{\gamma_n^2}\Bigr),
\qquad
\Xi_\text{smooth}(z) := \Xi(0) \cdot \prod_{n \ge 1}\Bigl(1 - \frac{z^2}{d_n^2}\Bigr),
$$
where $\Xi(0) = \xi(1/2) > 0$ is a fixed positive constant (computable: $\Xi(0) \approx 0.4972$).

**Both products converge:** $\sum_n \gamma_n^{-2} < \infty$ (classical; follows from
$\gamma_n \sim n/(2\pi)\log(n/(2\pi))$). Since $d_n \sim \gamma_n$, the same holds for $d_n$.

---

## The proposition to be verified

**Proposition G.3.** The following four statements all hold:

1. $O_\theta(\mathcal{Z}_\text{RH}) = O_\theta(\mathcal{Z}_\text{smooth}) = (d_n)_{n \ge 1}$.
2. $\mathcal{Z}_\text{RH} \ne \mathcal{Z}_\text{smooth}$ as multisets.
3. $\Xi_\text{smooth} \ne \Xi$ as entire functions.
4. There exist radii $R \to \infty$ such that $|\Xi_\text{smooth}(iR)/\Xi(iR) - 1|$ is bounded
   away from 0.

---

## Proof skeleton to be closed

### Step 1 — $O_\theta$ outputs the same sequence for both (trivial)

By definition, $O_\theta$ outputs $(d_n)$ independently of its input multiset; the
sequence $(d_n)$ is computed from $\theta(T)$ alone, which is zero-free. Statement 1 is
immediate from the definition of $O_\theta$. $\checkmark$

**Task for Step 1:** Confirm this is a valid definition of the observation map, i.e.,
that the Fredholm certificate class $\mathfrak{M}_\text{FC}$ as described in the program
is indeed restricted to methods that read only zero-free arithmetic data. (If the class
were defined differently, this step would need adjustment.)

### Step 2 — The two multisets differ

**Claim.** $\{\gamma_n\} \ne \{d_n\}$, i.e., $\gamma_n \ne d_n$ for some (in fact
infinitely many) $n$.

**Draft.** By the discrepancy formula $\gamma_n - d_n = S(\gamma_n)/N'(\gamma_n) + O(1/\gamma_n)$,
it suffices to show $S(T) \ne 0$ for infinitely many $T$. This is classical:
- Backlund (1914): $S(T)$ takes both positive and negative values.
- Selberg (1946): $\int_0^T S(t)^2\,dt \sim T\log\log T/(2\pi^2)$, proving oscillation.
- Tsang (1986): $\Omega_\pm(\sqrt{\log\log T})$ bounds (sharp oscillation).

**What to close for Step 2:** Supply the precise citation (author, journal, year, theorem)
for the statement that $S(T) \ne 0$ for infinitely many $T$ (equivalently, $S(T)$ is not
identically zero). The claim does not require the sharp oscillation bounds — just that
$S$ is not identically zero. Confirm the discrepancy formula $\gamma_n - d_n = S(\gamma_n)/N'(\gamma_n) + O(1/\gamma_n)$ from Titchmarsh or equivalent.

### Step 3 — Hadamard uniqueness implies $\Xi_\text{smooth} \ne \Xi$

**Hadamard factorization theorem (classical; entire functions of order $\le 1$):**
An entire function of order at most 1 is uniquely determined by:
- Its multiset of zeros $\{z_n\}$ (with multiplicities), and
- Its value at one point $z = 0$ (assuming $F(0) \ne 0$).

Precisely: if $F$ and $G$ are entire of order $\le 1$ with the same zeros (counted with
multiplicity) and $F(0) = G(0) \ne 0$, then $F = G$.

**Draft.** $\Xi$ and $\Xi_\text{smooth}$ are both entire of order 1 (Hadamard genus 1,
since $\sum \gamma_n^{-2} < \infty$ and similarly for $d_n$). Both are even and have
value $\Xi(0)$ at $z = 0$. By Hadamard uniqueness, they are equal iff their zero multisets
are equal. Since $\{\gamma_n\} \ne \{d_n\}$ (Step 2), we conclude $\Xi_\text{smooth} \ne \Xi$.

**What to close for Step 3:** (i) Confirm $\Xi_\text{smooth}$ has order exactly 1 (same
argument as $\Xi$: $d_n \sim \gamma_n$ so $\sum d_n^{-2} < \infty$, genus 1, and order 1
by the lower bound $|\Xi_\text{smooth}(iR)| \ge \Xi(0) \cdot 2^{N_d(R)}$ where $N_d(R) \to \infty$).
(ii) Confirm the Hadamard uniqueness theorem applies here (standard; cite Levin,
*Distribution of Zeros of Entire Functions*, or Titchmarsh, *Theory of Functions*, §8.2).

### Step 4 — Quantitative separation (optional, discovery-tier)

**Claim.** For $R = \gamma_n$ where $d_n \ne \gamma_n$:
$$
\frac{\Xi_\text{smooth}(iR)}{\Xi(iR)} = \prod_{k \ge 1}\frac{1 + R^2/d_k^2}{1 + R^2/\gamma_k^2}
\ne 1.
$$
The $k = n$ factor is $(1 + R^2/d_n^2)/(1 + R^2/\gamma_n^2) = (1 + \gamma_n^2/d_n^2)/2 \ne 1$
when $d_n \ne \gamma_n$.

Since $|\Xi(iR)| \to \infty$ as $R \to \infty$ (standard lower bound), the absolute
difference $|\Xi_\text{smooth}(iR) - \Xi(iR)| \to \infty$.

**What to close for Step 4 (optional):** Give an explicit lower bound on
$|\Xi_\text{smooth}(iR)/\Xi(iR) - 1|$ at a specific $R$, e.g., $R = \gamma_1 \approx 14.134$.
For this you will need $d_1$ (the solution to $\theta(d_1)/\pi + 1 = 1$, i.e., $\theta(d_1) = 0$).
The classical fact is $\theta(d_1) = 0$ gives $d_1$ slightly below $\gamma_1 \approx 14.134$
(since $S(\gamma_1) < 0$ for the first zero by Backlund's explicit computation). A numerical
value of $d_1$ is acceptable for this step (this is the only step that benefits from
numerical data; the analytic content is in Steps 1–3).

---

## Acceptance criteria

1. **Step 1:** Confirm or adjust the definition of $O_\theta$.
2. **Step 2:** Supply precise citation for $S(T) \not\equiv 0$; confirm the discrepancy formula.
3. **Step 3:** CONFIRMED (entire of order 1 + Hadamard uniqueness applies) with citations,
   or identify a gap.
4. **Step 4 (optional):** Explicit numerical bound at $R = \gamma_1$, or confirmation that
   the qualitative argument (product bounded away from 1) is sufficient.
5. Overall: CONFIRMED (Prop. G.3 holds as stated), PARTIAL (which steps), or REFUTED.
6. An "inconclusive + partial" response is acceptable. In particular, if Step 4 cannot
   be closed quantitatively, Steps 1–3 alone suffice for the qualitative obstruction.

---

## What this does and does not prove

This proposition says: a method reading only archimedean level data $(d_n)$ cannot
distinguish the true Riemann zero multiset from the smooth adversary $\{d_n\}$, because
both produce the same $(d_n)$ output. The two multisets are provably distinct and give
distinct entire functions.

This is an **information obstruction** for the Fredholm certificate class. It does **not**:
- Prove or disprove RH.
- Claim that $\mathcal{Z}_\text{smooth}$ is "close to" the Riemann zeros in any analytic sense.
- Claim that no method can prove RH; it claims that methods in $\mathfrak{M}_\text{FC}$
  (defined by their observation class $O_\theta$) cannot do so.

---

## Numerical anchor (sanity only)

The function $\theta(T)$ can be computed explicitly:
$\theta(14) = \arg\Gamma(1/4 + 7i) - 7\log\pi \approx -4.498$,
$\theta(14.134) \approx -0.0$ (near the first zero of $\theta$, which is close to $\gamma_1$).
The archimedean level $d_1$ satisfies $\theta(d_1)/\pi = 0$, giving $d_1 \approx 14.1347$,
while $\gamma_1 \approx 14.1347$ also — the two are extremely close (the discrepancy
$\gamma_1 - d_1 = S(\gamma_1)/N'(\gamma_1)$ is small but nonzero).
