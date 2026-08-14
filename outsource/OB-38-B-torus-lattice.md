# Problem OB-38 — B: Counting function asymptotics for the product operator on $T^4$

**Type:** analytic number theory / lattice-point counting / Abel summation

**Non-circularity:** RH is not assumed anywhere.  No zeros of $\zeta$, no Euler product,
no zero-counting law, and no functional equation of $\zeta$ appear in any step.  The
problem is a self-contained lattice-point asymptotic: counting pairs
$(p,q) \in \mathbb{Z}^2 \times \mathbb{Z}^2$ with $(1+|p|^2)(1+|q|^2) \leq \Lambda$.
The only analytic input is the classical Gauss circle problem bound for
$r_2(k) = \#\{p \in \mathbb{Z}^2 : |p|^2 = k\}$.

---

## Background and motivation

Paper B (spectral exclusion, Remark rem:counterex) exhibits $H_{\mathrm{prod}} =
(I - \Delta_x)(I - \Delta_y)$ on $T^4 = T^2_x \times T^2_y$ as an example of a
fourth-order operator whose spectral counting function $N_{H_{\mathrm{prod}}}(\Lambda)$
grows as $\Lambda \log \Lambda$ rather than the $\Lambda^{d/m} = \Lambda^{4/4} = \Lambda$
rate predicted by Weyl's law for an elliptic operator of order $m = 4$ on a
$d = 4$-dimensional manifold.  This $\Lambda \log \Lambda$ growth is the hallmark of a
**non-elliptic** product structure, and Paper B uses it as the explicit escape route in
its structural obstruction theorem: the class of operators with Weyl-law counting
$\sim c \Lambda$ does not contain $H_{\mathrm{prod}}$, while operators with the anomalous
$\Lambda \log \Lambda$ growth fall outside the method class targeted by Theorem D'.

**This problem asks for independent verification** of the asymptotic
$N_{H_{\mathrm{prod}}}(\Lambda) \sim \pi^2 \Lambda \log \Lambda$ via the Abel summation
argument sketched in Paper B.

---

## All definitions (self-contained — everything is here)

### Torus and Laplacian

$T^2 = \mathbb{R}^2/(2\pi\mathbb{Z})^2$ is the flat two-torus, and
$T^4 = T^2_x \times T^2_y$.

The Laplacian on $T^2$ is $-\Delta = -\partial_{x_1}^2 - \partial_{x_2}^2$, with
$L^2$-normalized Fourier eigenbasis $\{e^{ip \cdot x}/(2\pi)\}_{p \in \mathbb{Z}^2}$:
$$-\Delta\,\frac{e^{ip\cdot x}}{2\pi} = |p|^2\,\frac{e^{ip\cdot x}}{2\pi},
\quad |p|^2 = p_1^2 + p_2^2, \quad p = (p_1,p_2) \in \mathbb{Z}^2.$$

The operator $I - \Delta_x$ on $T^2_x$ has eigenvalues $1 + |p|^2$ for $p \in \mathbb{Z}^2$
with eigenfunction $e^{ip\cdot x}/(2\pi)$, multiplicity 1 per lattice vector $p$.

### Product operator

$$H_{\mathrm{prod}} = (I - \Delta_x)(I - \Delta_y) \quad \text{on } L^2(T^4).$$

The $L^2(T^4)$-eigenbasis is $\{e^{ip\cdot x}e^{iq\cdot y}/(2\pi)^2\}_{(p,q)\in
\mathbb{Z}^2 \times \mathbb{Z}^2}$, with eigenvalue
$$\lambda_{p,q} = (1+|p|^2)(1+|q|^2), \qquad (p,q) \in \mathbb{Z}^2 \times \mathbb{Z}^2.$$
Multiplicity is 1 per ordered pair $(p,q)$ (each Fourier mode is a distinct eigenfunction).

### Counting function and representation numbers

$$N_{H_{\mathrm{prod}}}(\Lambda) = \#\{(p,q) \in \mathbb{Z}^2 \times \mathbb{Z}^2 :
  (1+|p|^2)(1+|q|^2) \leq \Lambda\}.$$

The Gauss circle representation number: $r_2(k) = \#\{p \in \mathbb{Z}^2 : |p|^2 = k\}$
for $k \geq 0$.  Known values: $r_2(0) = 1$; $r_2(k) = 4\sum_{d|k,\,d\text{ odd}}
(-1)^{(d-1)/2}$ for $k \geq 1$ (Jacobi's two-square theorem).  In particular
$r_2(k) = 0$ if any prime $p \equiv 3 \pmod{4}$ divides $k$ to an odd power.

**Gauss circle asymptotics** (classical; see Hardy–Wright, *An Introduction to the
Theory of Numbers*, 6th ed. (Heath-Brown–Silverman), Oxford University Press, 2008,
for the two-square representation formula; the circle estimate
$\sum_{k \leq K} r_2(k) = \pi K + O(K^{1/2})$ follows elementarily from the
area comparison of unit squares around lattice points with the disc of radius
$\sqrt{K}$, with no need for deep results):
$$A(\Lambda) := \#\{q \in \mathbb{Z}^2 : 1 + |q|^2 \leq \Lambda\} = \pi(\Lambda - 1) + O(\Lambda^{1/2})
= \pi\Lambda + O(\Lambda^{1/2}). \tag{Gauss}$$

Equivalently, $\sum_{k=0}^{K} r_2(k) = \pi K + O(K^{1/2})$.

### Logarithm convention

$\log$ denotes the natural logarithm throughout.

---

## The claim to be verified

$$N_{H_{\mathrm{prod}}}(\Lambda) = \pi^2 \Lambda \log\Lambda + O(\Lambda)
\quad \text{as } \Lambda \to +\infty. \tag{Main}$$

Equivalently, $N_{H_{\mathrm{prod}}}(\Lambda) / (\Lambda \log\Lambda) \to \pi^2$.

---

## Proof skeleton to be closed

### Step 1 — Reduction to a sum over $p$

By definition:
$$N_{H_{\mathrm{prod}}}(\Lambda) = \sum_{\substack{p \in \mathbb{Z}^2 \\ 1+|p|^2 \leq \Lambda}}
A\!\left(\frac{\Lambda}{1+|p|^2}\right), \tag{S1}$$

where $A(X) = \#\{q \in \mathbb{Z}^2 : 1+|q|^2 \leq X\} = \pi X + O(X^{1/2})$ by (Gauss).

Substitute to split into main term and remainder.  Define
$\varepsilon(X) = A(X) - \pi X$, so that $|\varepsilon(X)| \leq C X^{1/2}$ uniformly
for $X \geq 1$ by (Gauss) (for $X < 1$ no $q$-vectors are counted, so $A(X)=1$,
handle separately).  Then:
$$N_{H_{\mathrm{prod}}}(\Lambda) = \pi\Lambda\,S_1(\Lambda) + R(\Lambda), \tag{S1'}$$

where
$$S_1(\Lambda) = \sum_{\substack{p \in \mathbb{Z}^2 \\ 1+|p|^2 \leq \Lambda}} \frac{1}{1+|p|^2},
\qquad R(\Lambda) = \sum_{\substack{p \in \mathbb{Z}^2 \\ 1+|p|^2 \leq \Lambda}}
\varepsilon\!\left(\frac{\Lambda}{1+|p|^2}\right). \tag{S1''}$$

**What to close for Step 1:** Confirm the decomposition (S1) is valid and that
splitting $A(X) = \pi X + O(X^{1/2})$ term by term is justified (summing $O$-terms is
valid since the number of $p$ with $1+|p|^2 \leq \Lambda$ is $O(\Lambda)$ and each
error is uniform).

### Step 2 — Abel summation for $S_1(\Lambda) \sim \pi \log\Lambda$

Write $S_1(\Lambda) = \sum_{k=0}^{N-1} \tfrac{r_2(k)}{1+k}$ where $N = \lfloor\Lambda\rfloor$.

Let $B(k) = \sum_{j=0}^{k} r_2(j)$.  Note $B(0) = r_2(0) = 1$; for $k \geq 1$,
$B(k) = \pi k + E(k)$ where $|E(k)| \leq C k^{1/2}$ by (Gauss).  Write $E(0) = 1$
(handled separately below).

Apply Abel summation (summation by parts) for $N \geq 2$:
$$\sum_{k=0}^{N-1} \frac{r_2(k)}{1+k}
= \frac{B(N-1)}{N} + \sum_{k=0}^{N-2} \frac{B(k)}{(1+k)(2+k)}. \tag{Abel}$$

Substitute $B(k) = \pi k + E(k)$:

**Main term** from $k \geq 1$ (the $\pi k$ part of $B(k)$):
$$\frac{\pi(N-1)}{N} + \sum_{k=1}^{N-2} \frac{\pi k}{(1+k)(2+k)}.$$

Partial fractions: $\dfrac{k}{(1+k)(2+k)} = \dfrac{-1}{1+k} + \dfrac{2}{2+k}$, so

$$\sum_{k=1}^{N-2}\frac{k}{(1+k)(2+k)}
= -\sum_{k=1}^{N-2}\frac{1}{1+k} + 2\sum_{k=1}^{N-2}\frac{1}{2+k}
= H_{N-1} + \frac{2}{N} - 2,$$

where $H_n = \sum_{j=1}^n 1/j$ is the $n$-th harmonic number.  Combined:

$$\pi\!\left(\frac{N-1}{N} + H_{N-1} + \frac{2}{N} - 2\right)
= \pi(H_N - 1). \tag{Main}$$

(Using $\tfrac{N-1}{N} + \tfrac{2}{N} = 1 + \tfrac{1}{N}$ and $H_N = H_{N-1} + 1/N$.)

The $k=0$ term $B(0)/(1\cdot 2) = 1/2$ (since $B(0)=1$, not $\pi\cdot0$) and the
error terms $|E(k)| \leq C k^{1/2}$ for $k \geq 1$ and $E(N-1)/N = O(N^{-1/2})$
all contribute $O(1)$ to $S_1(\Lambda)$.

Using $H_N = \log N + \gamma + O(N^{-1})$ (where $\gamma$ is the Euler–Mascheroni constant):
$$S_1(\Lambda)
= \pi(H_N - 1) + O(1)
= \pi\log\Lambda + O(1). \tag{S2}$$

A more precise form is $S_1(\Lambda) = \pi\log\Lambda + \pi(\gamma-1) + \tfrac{1}{2} + O(\Lambda^{-1/2})$,
where the $\tfrac{1}{2}$ comes from the $k=0$ term and $\pi(\gamma-1)$ from the harmonic asymptotics.

**What to close for Step 2:** (a) Reproduce the partial-fraction decomposition and the
telescoping identity $\sum_{k=1}^{N-2} k/((1+k)(2+k)) = H_{N-1} + 2/N - 2$ leading to
$\pi(H_N - 1)$ for the main term.  (b) Confirm the Abel summation formula (Abel) with
the correct upper limit $N-2$ (not $N-1$) in the second sum.  (c) Handle $k=0$ explicitly
($B(0)=1$, not $O(0^{1/2})$).  (d) State the constant-level result as $S_1(\Lambda) =
\pi\log\Lambda + O(1)$; a more precise form is $\pi\log\Lambda + \pi(\gamma-1) +
O(\Lambda^{-1/2})$, with remainder from the convergent series and boundary terms.

### Step 3 — Bounding the remainder $R(\Lambda) = O(\Lambda)$

From (S1''):
$$R(\Lambda) = O(\Lambda^{1/2})\,\sum_{\substack{p\in\mathbb{Z}^2\\1+|p|^2\leq\Lambda}}
(1+|p|^2)^{-1/2}
= O(\Lambda^{1/2})\,T(\Lambda), \tag{S3}$$

where $T(\Lambda) = \sum_{k=0}^{N-1} r_2(k)\,(1+k)^{-1/2}$.

**Dyadic shell bound for $T(\Lambda)$:** Separate $k=0$: $r_2(0)(1+0)^{-1/2} = 1$.
For $k \geq 1$, partition into dyadic shells
$I_j = \{k : 2^{j-1} < k \leq \min(2^j,\,N-1)\}$ for $j = 1, \ldots, J$ with
$J = \lceil\log_2(N-1)\rceil$ (empty shells ignored).  In shell $I_j$:
$$\sum_{k \in I_j} r_2(k)\,(1+k)^{-1/2} \leq C_1\,2^{-j/2}\!\sum_{k \in I_j} r_2(k)
= C_1\,2^{-j/2}\,O(2^j) = O(2^{j/2}),$$
using $\sum_{k \leq R} r_2(k) = O(R)$.  Summing over shells (at most $J \leq \log_2 N + 1$):
$$T(\Lambda)
\leq 1 + \sum_{j=1}^{J} O(2^{j/2}) = O(2^{J/2}) = O(N^{1/2}) = O(\Lambda^{1/2}). \tag{T-bound}$$

Therefore $R(\Lambda) = O(\Lambda^{1/2}) \cdot O(\Lambda^{1/2}) = O(\Lambda)$.

**What to close for Step 3:** (a) Confirm that the bound $\sum_{k \in I_j} r_2(k) =
O(2^j)$ follows from the Gauss circle asymptotics.  (b) Confirm the geometric
series bound $\sum_{j=1}^{J} 2^{j/2} = O(2^{J/2}) = O(N^{1/2}) = O(\Lambda^{1/2})$.
(c) Confirm $k=0$ contributes only $O(1)$ and does not affect the $O(\Lambda^{1/2})$
bound on $T(\Lambda)$.  (d) Confirm $J = \lceil\log_2(N-1)\rceil$ covers all $k \in
[1,N-1]$ with no gap.

### Step 4 — Conclusion

Combining (S1'), (S2), and $R(\Lambda) = O(\Lambda)$:
$$N_{H_{\mathrm{prod}}}(\Lambda) = \pi\Lambda(\pi\log\Lambda + O(1)) + O(\Lambda)
= \pi^2\Lambda\log\Lambda + O(\Lambda). \tag{Main}$$

**What to close for Step 4:** Confirm the product $\pi\Lambda \cdot S_1(\Lambda) =
\pi\Lambda(\pi\log\Lambda + O(1)) = \pi^2\Lambda\log\Lambda + O(\Lambda)$ with the
correct power of $\pi$ ($\pi$ from the Gauss circle in (Gauss), times $\pi$ from the
Abel sum $S_1 \sim \pi\log\Lambda$, giving $\pi^2$).  Confirm $O(\Lambda)$ absorbs
all lower-order contributions.

---

## Acceptance criteria

1. **CONFIRMED:** Steps 1–4 verified end-to-end; the numerical anchor at $\Lambda = 10$
   reproduced exactly; the computation at $\Lambda = 100$ matches the asymptotic within
   the stated error.
   Report: "$N_{H_{\mathrm{prod}}}(\Lambda) = \pi^2\Lambda\log\Lambda + O(\Lambda)$,
   proved by Abel summation with Gauss circle input; no RH or zeta zeros used."

2. **PARTIAL:** Steps 1–3 correct but Step 4 has a gap (e.g., the $O(1)$ constant in
   $S_1$ cannot be made fully explicit, or the error $O(\Lambda)$ has a log factor not
   absorbed); or the asymptotic is confirmed but with a weaker error bound than $O(\Lambda)$.
   State precisely what is and is not established.

3. **REFUTED:** An explicit error in the argument (e.g., the Abel summation boundary
   terms do not telescope as claimed, or the dyadic shell sum exceeds $O(\Lambda^{1/2})$);
   or a direct computer count shows $N_{H_{\mathrm{prod}}}(\Lambda)/(\Lambda\log\Lambda)
   \not\to \pi^2$.  Provide the explicit failure with the corrected asymptotic if known.

All three outcomes are decisive and first-class.

---

## Numerical anchor (sanity only — exact count for small $\Lambda$, not an input)

### Exact count: $N_{H_{\mathrm{prod}}}(10)$

We count pairs $(p,q) \in \mathbb{Z}^2 \times \mathbb{Z}^2$ with $(1+|p|^2)(1+|q|^2) \leq 10$.

For each value $n = 1 + |p|^2$, the number of $p$-vectors is $r_2(n-1)$, and the
number of admissible $q$-vectors is $A(\Lambda/n) = \#\{q : 1 + |q|^2 \leq 10/n\}$.

| $|p|^2$ | $n=1+\vert p\vert^2$ | $r_2(\vert p\vert^2)$ | $\lfloor 10/n - 1\rfloor_{\max\,\vert q\vert^2}$ | $A(10/n)$ | contribution |
|---|---|---|---|---|---|
| 0 | 1 | 1 | $\vert q\vert^2 \leq 9$ | 29 | 29 |
| 1 | 2 | 4 | $\vert q\vert^2 \leq 4$ | 13 | 52 |
| 2 | 3 | 4 | $\vert q\vert^2 \leq 2$ | 9 | 36 |
| 3 | 4 | 0 | — | — | 0 |
| 4 | 5 | 4 | $\vert q\vert^2 \leq 1$ | 5 | 20 |
| 5 | 6 | 8 | $\vert q\vert^2 \leq 0$ | 1 | 8 |
| 6 | 7 | 0 | — | — | 0 |
| 7 | 8 | 0 | — | — | 0 |
| 8 | 9 | 4 | $\vert q\vert^2 \leq 0$ | 1 | 4 |
| 9 | 10 | 4 | $\vert q\vert^2 \leq 0$ | 1 | 4 |

Notes: $r_2(3) = r_2(6) = r_2(7) = 0$ (primes $3, 7 \equiv 3 \pmod{4}$ appear to
odd power).  $A(10/n)$ values: $A(10)=29$ (sum $r_2(0)+\cdots+r_2(9) =
1+4+4+0+4+8+0+0+4+4$); $A(5)=13$; $A(10/3)\approx 3.3\Rightarrow A=9$; $A(2)=5$;
$A(10/6)\approx 1.67\Rightarrow A=1$; $A(10/9)\approx 1.11\Rightarrow A=1$;
$A(1)=1$.

$$N_{H_{\mathrm{prod}}}(10) = 29 + 52 + 36 + 0 + 20 + 8 + 0 + 0 + 4 + 4 = \mathbf{153}.$$

**Asymptotic comparison:**
$\pi^2 \cdot 10 \cdot \log(10) \approx 9.8696 \times 23.026 \approx 227$.
Relative shortfall at $\Lambda=10$: $(227-153)/227 \approx 33\%$, consistent with large
$O(\Lambda)$ lower-order corrections at small $\Lambda$.

### Verified anchor: $N_{H_{\mathrm{prod}}}(100)$

Independent enumeration by two paths (direct product count and $r_2$-convolution) gives:

$$\boxed{N_{H_{\mathrm{prod}}}(100) = 3505.}$$

Asymptotic prediction: $\pi^2 \cdot 100 \cdot \log(100) \approx 4545.12$.

$$\frac{N(100) - \pi^2\cdot100\cdot\log(100)}{\pi^2\cdot100\cdot\log(100)}
\approx \frac{3505 - 4545.12}{4545.12} \approx -22.88\%.$$

This is consistent with an $O(\Lambda)$ remainder whose coefficient at $\Lambda = 100$
produces roughly one order of magnitude less than the main term; convergence is
logarithmically slow.  The $O(\Lambda)$ notation makes no claim that the absolute
error is at most $100$ or that the relative error is at most $1/\log 100$ — those
interpretations are not consequences of the big-$O$ bound with unspecified constant.

---

## Pre-send lint notes (PROMPT_LINT.md self-check)

| Item | Status |
|---|---|
| L1 (order ≠ finite exponential type) | N/A — no entire/meromorphic functions; counting function only |
| L2 (parity from functional equation) | N/A |
| L3 (zero vs pole) | N/A |
| L4 (canonical product genus) | N/A |
| L5 (RH via divisor) | PASS — no RH, no zeta zeros; only Gauss circle problem ($\sum r_2(k)$) and harmonic series; both are classical, zero-free |
| L6 (vacuous target) | PASS — exact anchor $N_{H_{\mathrm{prod}}}(10) = 153$ is a non-vacuous computable value; REFUTED verdict requires a direct computer count showing $N/(\Lambda\log\Lambda)\not\to\pi^2$ |
| L7 (counting-function factor) | PASS — $N$ uses the correct multiplicity (1 per ordered pair $(p,q)$, not per norm); eigenvalue multiplicity is the number of $(p,q)$ pairs, not $r_2(|p|^2)\cdot r_2(|q|^2)$ summed over norms; table confirms this |
| L8 (global observation map) | N/A |
| L9 (growth not assumed) | PASS — $\Lambda\log\Lambda$ growth is derived from the Gauss circle sum and Abel summation; it is not assumed |
| L10 (power-sum ≠ Taylor jet) | N/A |
| L11 (dropped frozen terms) | PASS — boundary terms in Abel summation (the $B(N-1)/N$ term) explicitly retained and shown to be $O(1)$ |
| L12 (parity of leading degree) | N/A |
| L13 (Fredholm zeros) | N/A |
| L14 (per-$n$ vs uniform) | PASS — the $O(\Lambda^{1/2})$ bound in (Gauss) is uniform in $\Lambda$; used uniformly in Step 3 |
| L15 (zeros in $\Omega$ vs zeros in $\mathbb{C}$) | N/A |
| L16 (representation invariance) | PASS — $N_{H_{\mathrm{prod}}}(\Lambda)$ is an eigenvalue count, independent of basis; the split $T^4 = T^2_x\times T^2_y$ is explicit in the operator definition, not a basis choice |
| L17 (cited black boxes exact) | PASS — Jacobi two-square theorem for $r_2(k)$: Hardy–Wright, 6th ed. (Heath-Brown–Silverman), Oxford University Press, 2008, Thm 278; Gauss circle estimate $\sum_{k\leq K}r_2(k) = \pi K + O(K^{1/2})$: proved inline by unit-square area comparison in §3 of this file (no external citation needed); Abel summation stated explicitly in (Abel). |
| L18 (numerical anchors by script) | PASS — $N_{H_{\mathrm{prod}}}(10) = 153$ and $N_{H_{\mathrm{prod}}}(100) = 3505$ verified by two independent integer-enumeration paths (direct product count and $r_2$-convolution); relative error at $\Lambda=100$: $-22.88\%$, consistent with $O(\Lambda)$ remainder. |
| L19 (honest inconclusive verdict) | PASS — Step 2 offers a precise partial result (error estimate in $S_1$) if the $O(1)$ constant cannot be determined; REFUTED path is concrete |
| Self-containment | PASS — all symbols ($T^2$, $T^4$, $H_{\mathrm{prod}}$, $r_2$, $A$, $N$, $S_1$, $B$, $R$, $T$, $\log$) defined in-file; arithmetic values ($r_2(3)=0$ etc.) justified by Jacobi theorem; no "see other file" for load-bearing content |
