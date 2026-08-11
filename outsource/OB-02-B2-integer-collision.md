# Problem OB-02 — Exact finite-observation collision with integer multiplicities (Theorem B2)

**Type:** Algebraic / combinatorial. No number theory or Riemann zeta function knowledge
required. The construction is purely algebraic once the test functionals are defined.

**Non-circularity:** No step assumes RH, reads Riemann zero locations, or uses any
zeta-function numerics. The objects are defined combinatorially.

---

## All definitions (self-contained — everything is here)

### Admissible symmetric zero multisets

An **admissible symmetric zero multiset** is a locally finite multiset
$\mathcal{Z} \subset \{s \in \mathbb{C} : 0 < \operatorname{Re}(s) < 1\}$ satisfying:
- Conjugate symmetry: $\rho \in \mathcal{Z} \Rightarrow \bar\rho \in \mathcal{Z}$ (same multiplicity).
- Functional symmetry: $\rho \in \mathcal{Z} \Rightarrow 1-\rho \in \mathcal{Z}$ (same multiplicity).
- Admissibility: $\sum_{\rho \in \mathcal{Z}} |\rho|^{-2} < \infty$.

The **critical-line predicate** is $P(\mathcal{Z}) = 1$ iff every element of $\mathcal{Z}$
has $\operatorname{Re}(\rho) = 1/2$; otherwise $P(\mathcal{Z}) = 0$.

The **off-line quartet** at $(\sigma_0, T)$ with $\sigma_0 \in (1/2, 1)$, $T > 0$:
$$
Q(\sigma_0, T) := \{\sigma_0 + iT,\; \sigma_0 - iT,\; (1-\sigma_0) + iT,\; (1-\sigma_0) - iT\}.
$$
This is admissible, symmetric, with $P(Q) = 0$.

### Li-type test functionals

For $j = 1, \ldots, m$, the **Li-type test functional** is:
$$
\varphi_j(\rho) := 1 - \Bigl(1 - \frac{1}{\rho}\Bigr)^j.
$$
The **observation functional** on a finite multiset $\mathcal{Z}$:
$$
O_j(\mathcal{Z}) := \sum_{\rho \in \mathcal{Z}} \bigl[\varphi_j(\rho) + \varphi_j(\bar\rho)\bigr]
                  = \sum_{\rho \in \mathcal{Z}} 2\,\operatorname{Re}[\varphi_j(\rho)].
$$
The **observation map** $O_\Phi = (O_1, \ldots, O_m) : \mathfrak{X}_\text{sym} \to \mathbb{R}^m$.

### The Jacobian matrix

Fix $m$ distinct rational heights $0 < t_1 < \cdots < t_m$. Define the $m \times m$ matrix:
$$
J_{jk} := 2\operatorname{Re}\bigl[\varphi_j(1/2 + it_k) + \varphi_j(1/2 - it_k)\bigr]
         = 2\bigl(1 - \cos(j\theta_k)\bigr),
$$
where $\theta_k = 2\arctan(2t_k) - \pi \in (-\pi, 0)$ for $t_k > 0$.

### The quartet contribution

For the off-line quartet $Q(3/4, T)$:
$$
\delta_j^{\text{off}}(T) := O_j(Q(3/4, T))
= 2\operatorname{Re}[\varphi_j(3/4 + iT) + \varphi_j(3/4 - iT)].
$$
This is a rational number for rational $T$.

---

## The theorem to be verified

**Theorem B2.** For any $m \ge 1$ and any $m$ distinct rational heights $0 < t_1 < \cdots < t_m$,
there exist finite admissible symmetric multisets $\mathcal{Z}_+$, $\mathcal{Z}_-$ with:
1. $P(\mathcal{Z}_+) = 1$ (all zeros on the critical line).
2. $P(\mathcal{Z}_-) = 0$ (some zeros off the critical line).
3. $O_j(\mathcal{Z}_+) = O_j(\mathcal{Z}_-)$ **exactly** for $j = 1, \ldots, m$.

---

## Proof sketch to be closed

### Step 1 — Li Jacobian is nonsingular over $\mathbb{Q}$

**Claim.** $\det J \ne 0$, with $J \in \mathbb{Q}^{m \times m}$ for rational $t_k$.

**Draft skeleton.**

Let $x_k = \cos\theta_k \in (-1, 0)$ for $t_k > 0$. Since $\theta_k \in (-\pi, 0)$ and
$t_k \mapsto \theta_k = 2\arctan(2t_k) - \pi$ is strictly decreasing, the values
$\theta_1 > \theta_2 > \cdots > \theta_m$ are distinct, so $x_1 > x_2 > \cdots > x_m$
are distinct.

Chebyshev identity: $\cos(j\theta) = T_j(\cos\theta)$, where $T_j$ is the Chebyshev
polynomial of degree $j$ with leading coefficient $2^{j-1}$.

Since $T_j(1) = 1$: factorization $1 - T_j(x) = (1-x) Q_j(x)$ where $Q_j$ has degree
$j-1$ and leading coefficient $2^{j-1} > 0$.

So $J_{jk} = 2(1-x_k) Q_j(x_k)$. Factor out positive diagonal $\operatorname{diag}(2(1-x_k))$:
$$
\det J = \prod_k 2(1-x_k) \cdot \det[Q_j(x_k)].
$$
Since $x_k \in (-1,1)$, each $1-x_k > 0$, so we need $\det[Q_j(x_k)] \ne 0$.

The polynomials $\{Q_j\}_{j=1}^m$ have degrees $0, 1, \ldots, m-1$ (strictly increasing).
Write $Q_j(x) = \sum_{i=1}^j U_{ji} x^{i-1}$ with upper-triangular $U$, diagonal entries
$U_{jj} = 2^{j-1}$. Then:
$$
[Q_j(x_k)]_{j,k} = U \cdot V(x_1, \ldots, x_m),
$$
where $V$ is the Vandermonde matrix with $(i,k)$-entry $x_k^{i-1}$.
$$
\det[Q_j(x_k)] = \underbrace{\det U}_{= \prod_j 2^{j-1} = 2^{m(m-1)/2} > 0}
\cdot \underbrace{\det V}_{= \prod_{k < l}(x_l - x_k) \ne 0 \text{ (distinct } x_k)}.
$$

**Rationality:** For rational $t_k$, $x_k = \cos\theta_k = \operatorname{Re}(w_k)$ where
$w_k = (2it_k-1)/(2it_k+1) \in \mathbb{Q}(i)$. Thus $J_{jk} = 2(1 - \operatorname{Re}(w_k^j)) \in \mathbb{Q}$.
Similarly $\delta_j^{\text{off}}(T) \in \mathbb{Q}$ for rational $T$.

**What to close for Step 1:** Verify the Chebyshev factorization $(1-T_j(x))/(1-x) = Q_j(x)$
with $\deg Q_j = j-1$ and leading coefficient $2^{j-1}$. The recurrence is
$T_{j+1}(x) = 2x T_j(x) - T_{j-1}(x)$ with $T_0 = 1$, $T_1 = x$. Derive the formula
for $\deg Q_j$ and its leading coefficient from this recurrence.

### Step 2 — Rational solution and integer scaling

**Given:** $\det J \ne 0$ over $\mathbb{Q}$. Set $\alpha^\mathbb{Q} = -J^{-1} \delta^{\text{off}}(T) \in \mathbb{Q}^m$.

Let $R = \operatorname{lcm}(\text{denominators of } \alpha^\mathbb{Q}_k)$ and
$\alpha = R \cdot \alpha^\mathbb{Q} \in \mathbb{Z}^m$. Replace $Q(3/4, T)$ by $R$ copies.

Then $J \alpha = R \cdot J \alpha^\mathbb{Q} = R \cdot (-\delta^{\text{off}}(T)) = -\delta^{\text{off,scaled}}(T)$
exactly over $\mathbb{Z}$.

**What to close for Step 2:** Confirm the lcm-scaling gives $J\alpha + R\,\delta^{\text{off}} = 0$
exactly (not approximately). State the observation equality:
$$
O_j(\mathcal{Z}_-) - O_j(\mathcal{Z}_+)
= \sum_k \alpha_k J_{jk} + R\,\delta_j^{\text{off}}(T) = 0.
$$

### Step 3 — Multiplicity buffer and valid removal

**Construction.**
$$
M := R \cdot \max_k |\alpha^\mathbb{Q}_k|, \quad
\mathcal{Z}_+ := \{1/2 \pm it_k : k=1,\ldots,m, \text{ each with multiplicity } M\}.
$$
Note $P(\mathcal{Z}_+) = 1$.

For $k$ with $\alpha_k > 0$: add $\alpha_k$ copies of $\{1/2 \pm it_k\}$ to $\mathcal{Z}_+$.
For $k$ with $\alpha_k < 0$: remove $|\alpha_k|$ copies. Since $|\alpha_k| \le M$,
removal is valid ($\mathcal{Z}_+$ has multiplicity $M$ at each height).
Add $R$ copies of $Q(3/4, T)$. Call the result $\mathcal{Z}_-$.

$P(\mathcal{Z}_-) = 0$ because $Q(3/4, T)$ contributes elements at $\operatorname{Re} = 3/4 \ne 1/2$.

**What to close for Step 3:** Confirm that $\mathcal{Z}_-$ is admissible and symmetric
(finitely many changes to a finite multiset preserve both).

---

## Acceptance criteria

1. **Step 1:** CONFIRMED or REFUTED. If confirmed, verify the Chebyshev leading-coefficient
   computation explicitly. If refuted, give a counterexample (specific $m, t_1, \ldots, t_m$
   with $\det J = 0$).
2. **Step 2:** CONFIRMED that the observation equality holds exactly (over $\mathbb{Z}$, not approximately).
3. **Step 3:** CONFIRMED that $\mathcal{Z}_-$ is admissible and symmetric, and that all
   removals are valid.
4. Overall: CONFIRMED (Theorem B2 holds as stated) or PARTIAL (specify which steps hold)
   or REFUTED (explicit counterexample to the existence claim).
5. An "inconclusive + partial" response is acceptable.

---

## What this does and does not prove

This theorem says: there exist two finite admissible symmetric zero multisets in the
critical strip with the same Li-type observation vector but different critical-line
predicates. It does **not** involve the Riemann zeta function or RH in any way.
The construction works for any $m$ and any rational heights.

---

## Numerical anchor (sanity only — run if helpful, not required)

For $m = 2$, $t_1 = 1$, $t_2 = 2$, $T = 10$, $\sigma_0 = 3/4$:
- $\theta_1 = 2\arctan(2) - \pi \approx -0.6435$, $x_1 = \cos\theta_1 \approx 0.7809$.
- $\theta_2 = 2\arctan(4) - \pi \approx -0.9273$, $x_2 = \cos\theta_2 \approx 0.6$, $x_2 \approx 0.6$.

Wait — let me recompute for sanity: $\arctan(4) \approx 1.3258$, $2 \times 1.3258 - \pi \approx -0.4900$,
$\cos(-0.4900) \approx 0.8824$. And $\arctan(2) \approx 1.1071$, $2 \times 1.1071 - \pi \approx -0.5274$,
$\cos(-0.5274) \approx 0.8660$. Both in $(-1,1)$, distinct. $\det J$ is a specific nonzero rational.
The reviewer is welcome to compute $\det J$ for these values and verify it is nonzero.
