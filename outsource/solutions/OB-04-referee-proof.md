# Problem OB-04 — Referee-ready audit and corrected proof of Proposition G.3

**Subject:** smooth Gram-level adversary and $O_\theta$-indistinguishability  
**Final status:** **REFUTED AS WRITTEN; CORRECTED PROPOSITION PROVED.**  
**RH status:** every analytic input used below is unconditional.

---

## 1. Referee verdict

The four intended conclusions have a valid mathematical core, but the submitted proof
cannot be accepted as written. The exact status is as follows.

| Item | Verdict | Reason |
|---|---|---|
| 1. $O_\theta(\mathcal Z_{\rm RH})=O_\theta(\mathcal Z_{\rm smooth})$ | **Conditional/formal** | It is immediate if $O_\theta$ is, by definition, the constant map $\mathcal Z\mapsto(d_n)$. The attachment does not supply the external definition of $\mathfrak M_{\rm FC}$, so the claimed program-level factorization cannot be independently checked here. |
| 2. $\mathcal Z_{\rm RH}\ne\mathcal Z_{\rm smooth}$ | **True, draft proof invalid** | The displayed discrepancy formula has the wrong convention/sign and omits the endpoint half-jump. Nonvanishing of $S(t)$ at arbitrary $t$ does not imply a mismatch at a zero ordinate. A correct unconditional proof is given below. |
| 3. Distinct entire functions | **True for the two explicitly defined canonical products** | Equality of the products would force equality of their zero multisets. The Hadamard uniqueness theorem quoted in the submission is false without an exponential-factor condition. Also, the ordinate product is not Riemann's actual $\Xi$-function unless RH holds. |
| 4. Quantitative separation on $i\mathbb R_+$ | **True after adding one classical input; draft proof invalid** | A single factor different from $1$ does not prevent all remaining factors from compensating it. Using Littlewood's unconditional bound $S_1(T)=O(\log T)$, one obtains the stronger result $F_d(iR)/F_\gamma(iR)=e^{O(1)}/R\to0$. |

Thus the original proposition is not referee-ready. Sections 2–7 state and prove the
corrected result.

---

## 2. Exact conventions and admissible inputs

### 2.1 The Riemann–Siegel phase

Let

\[
\theta(t)=\Im\log\Gamma\!\left(\frac14+\frac{it}{2}\right)
             -\frac t2\log\pi ,
\]

where the branch of $\log\Gamma$ is continued from $t=0$ and is normalized by
$\theta(0)=0$. Put

\[
A(t):=\frac{\theta(t)}{\pi}+1.
\]

Stirling's expansion and its differentiated forms give

\[
\begin{aligned}
A(t)
 &=\frac{t}{2\pi}\log\frac{t}{2\pi e}+\frac78+O(t^{-1}),\\
A'(t)
 &=\frac{1}{2\pi}\log\frac{t}{2\pi}+O(t^{-2}),\\
A''(t)
 &=\frac{1}{2\pi t}+O(t^{-3}).
\end{aligned}
\tag{2.1}
\]

### 2.2 Zero counting and $S(t)$

Let $\gamma_1\le\gamma_2\le\cdots$ be the positive imaginary parts of all
nontrivial zeros of $\zeta(s)$, repeated with their full multiplicities. For $t$ that
is not a zero ordinate, let

\[
N(t)=\#\{n:\gamma_n\le t\}.
\]

With the standard continuously varied argument,

\[
S(t)=\frac1\pi\arg\zeta\!\left(\frac12+it\right),
\]

the exact Riemann–von Mangoldt identity is

\[
N(t)=A(t)+S(t)
\tag{2.2}
\]

away from zero ordinates. Values assigned at the jump points do not affect any integral
below. We use the following classical unconditional estimates:

\[
S(t)=O(\log t),
\qquad
S_1(T):=\int_0^T S(t)\,dt=O(\log T).
\tag{2.3}
\]

The second estimate is Littlewood's bound. It was not listed among the explicit inputs in
the submitted draft, but it is the extra classical fact used below to prove Item 2 without
numerical zero tables and to close the large-$R$ separation in Item 4. Bondarenko–Seip
explicitly recall both unconditional bounds and the standard midpoint convention for
$S$ at a zero; see the references in §9.

### 2.3 Smooth levels

For $n\ge1$, define $d_n$ to be the unique positive solution of

\[
A(d_n)=n,
\qquad\text{equivalently}\qquad
\theta(d_n)=(n-1)\pi.
\tag{2.4}
\]

Thus $d_n=g_{n-1}$ in the standard nonnegative indexing of Gram points. Let

\[
D(t):=\#\{n:d_n\le t\}.
\]

For all sufficiently large $t$ away from the $d_n$, monotonicity gives

\[
D(t)=\lfloor A(t)\rfloor.
\tag{2.5}
\]

### 2.4 The observation map

The only definition that makes Item 1 immediate is

\[
O_\theta:\mathcal X\longrightarrow\mathbb R^{\mathbb N},
\qquad
O_\theta(\mathcal Z)=(d_n)_{n\ge1}
\quad(\mathcal Z\in\mathcal X).
\tag{2.6}
\]

This is a constant map. To infer an obstruction for a method class
$\mathfrak M_{\rm FC}$, one must separately assume or prove the factorization condition

\[
\text{every admissible output of every }P\in\mathfrak M_{\rm FC}
\text{ factors through }O_\theta.
\tag{2.7}
\]

Merely saying that a method reads prime powers or gamma factors does **not** imply (2.7):
prime-power data can encode the zeta function and hence its zeros. The external program
definition needed to verify (2.7) was not included in this attachment.

### 2.5 The two canonical products

To avoid an RH-dependent misuse of notation, define

\[
F_\gamma(z):=C\prod_{n\ge1}\left(1-\frac{z^2}{\gamma_n^2}\right),
\qquad
F_d(z):=C\prod_{n\ge1}\left(1-\frac{z^2}{d_n^2}\right),
\tag{2.8}
\]

where $C=\xi(1/2)>0$. These are the functions denoted by $\Xi$ and
$\Xi_{\rm smooth}$, respectively, in the submitted draft. The notation $F_\gamma$
is essential: unconditionally,

\[
\Xi_{\rm R}(z):=\xi\!\left(\frac12+iz\right)
\]

has a zero at

\[
z=\gamma+i\left(\frac12-\beta\right)
\]

for every zero $\rho=\beta+i\gamma$ of $\zeta$. Hence (2.8) represents the actual
Riemann $\Xi$-function if and only if all nontrivial zeros lie on the critical line.

---

## 3. Preliminary checks

### Lemma 3.1 — Existence and uniqueness of every $d_n$

For each $n\ge1$, equation (2.4) has exactly one positive solution.

#### Proof

Let $\psi=\Gamma'/\Gamma$. Differentiation gives

\[
\theta'(t)=\frac12\Re\psi\!\left(\frac14+\frac{it}{2}\right)
              -\frac12\log\pi
\]

and

\[
\theta''(t)=-\frac14\Im\psi'\!\left(\frac14+\frac{it}{2}\right).
\]

For $\Re z>0$,

\[
\psi'(z)=\sum_{k=0}^{\infty}\frac1{(k+z)^2}.
\]

If $t>0$, every summand on the right has negative imaginary part, so
$\theta''(t)>0$. Thus $\theta'$ is strictly increasing on $t>0$. Moreover,

\[
\theta'(0)=\frac12\bigl(\psi(1/4)-\log\pi\bigr)<0,
\]

whereas (2.1) gives $\theta'(t)\to+\infty$. Hence $\theta$ first strictly decreases
from $\theta(0)=0$, has one minimum, and then strictly increases to $+\infty$.
Consequently it crosses every level $(n-1)\pi\ge0$ exactly once at a positive
argument. $\square$

### Lemma 3.2 — Counting asymptotics and product convergence

As $t\to\infty$,

\[
D(t)=\frac{t}{2\pi}\log\frac{t}{2\pi e}+O(1),
\qquad
N(t)=\frac{t}{2\pi}\log\frac{t}{2\pi e}+O(\log t).
\tag{3.1}
\]

In particular,

\[
d_n\sim\gamma_n\sim\frac{2\pi n}{\log n}.
\tag{3.2}
\]

Both products in (2.8) converge locally uniformly and define even entire functions of
order exactly $1$.

#### Proof

Equations (2.1), (2.2), (2.3), and (2.5) give (3.1); monotone inversion gives (3.2).
Notice that (3.2), not
$\gamma_n\sim \frac{n}{2\pi}\log\frac{n}{2\pi}$, is the correct inversion of the
zero-counting asymptotic.

Equation (3.2) implies

\[
\sum_n\gamma_n^{-2}<\infty,
\qquad
\sum_n d_n^{-2}<\infty,
\]

so the paired products converge locally uniformly.

For either sequence $a_n\in\{\gamma_n,d_n\}$, let
$A_a(t)=\#\{n:a_n\le t\}=O(t\log t)$. For $r\ge2$, Stieltjes integration gives

\[
\sum_n\log\left(1+\frac{r^2}{a_n^2}\right)
=\int_0^\infty \frac{2r^2A_a(t)}{t(t^2+r^2)}\,dt
=O(r\log r).
\tag{3.3}
\]

This yields order at most $1$. On the other hand,

\[
\log|F_a(ir)/C|
\ge A_a(r)\log2\gg r\log r,
\]

which yields order at least $1$. Thus the order is exactly $1$. $\square$

### Lemma 3.3 — Fractional-part averaging

There is $T_0>0$ such that $A$ is strictly increasing on $[T_0,\infty)$, and

\[
\int_{T_0}^{T}\left(\{A(t)\}-\frac12\right)dt=O(1)
\qquad(T\ge T_0).
\tag{3.4}
\]

Here $\{x\}=x-\lfloor x\rfloor$.

#### Proof

Choose $T_0$ so that (2.1) gives $A'(t)>0$ for $t\ge T_0$. On a complete
level interval $A(t)\in[n,n+1]$, make the change of variable $u=A(t)$, and write

\[
q(u):=\frac1{A'(A^{-1}(u))}.
\]

Then

\[
\int_{A^{-1}(n)}^{A^{-1}(n+1)}
\left(\{A(t)\}-\frac12\right)dt
=\int_n^{n+1}\left(u-n-\frac12\right)q(u)\,du.
\tag{3.5}
\]

The factor $u-n-1/2$ has mean zero, while

\[
q'(u)=-\frac{A''(t)}{A'(t)^3},
\qquad t=A^{-1}(u).
\]

By (2.1), the absolute value of the $n$-th complete-interval contribution in
(3.5) is

\[
O\!\left(\frac1{t_n(\log t_n)^3}\right)
=O\!\left(\frac1{n(\log n)^2}\right),
\qquad t_n=A^{-1}(n).
\]

These bounds are summable. An incomplete terminal interval contributes
$O(1/A'(T))=O(1/\log T)$. Hence the primitive in (3.4) is bounded. $\square$

### Lemma 3.4 — Counting-function representation of the product ratio

For $R>0$, set

\[
K_R(t):=\frac{2R^2}{t(t^2+R^2)}.
\tag{3.6}
\]

Then

\[
\log\frac{F_d(iR)}{F_\gamma(iR)}
=\int_0^\infty K_R(t)\bigl(D(t)-N(t)\bigr)\,dt.
\tag{3.7}
\]

#### Proof

For $f_R(t)=\log(1+R^2/t^2)$, one has $-f_R'(t)=K_R(t)$. Stieltjes
integration by parts gives

\[
\sum_n f_R(d_n)=\int_0^\infty K_R(t)D(t)\,dt
\]

and the analogous identity for $\gamma_n$. The boundary terms vanish by (3.1), and
the difference integral converges because $D(t)-N(t)=O(\log t)$. Subtraction gives
(3.7). $\square$

---

## 4. Corrected Proposition G.3

### Proposition G.3* (precise form)

Assume that $O_\theta$ is the constant observation map (2.6). Let

\[
\mathcal Z_\gamma=\{\gamma_n:n\ge1\},
\qquad
\mathcal Z_d=\{d_n:n\ge1\},
\]

with multiplicities, and let $F_\gamma,F_d$ be the canonical products (2.8). Then:

1. $O_\theta(\mathcal Z_\gamma)=O_\theta(\mathcal Z_d)=(d_n)_{n\ge1}$.
2. The multisets $\mathcal Z_\gamma$ and $\mathcal Z_d$ differ in infinitely many
   entries.
3. $F_\gamma\ne F_d$ as entire functions; both are even entire functions of order
   exactly $1$ and take the value $C$ at $0$.
4. As $R\to\infty$,

   \[
   \log\frac{F_d(iR)}{F_\gamma(iR)}=-\log R+O(1).
   \tag{4.1}
   \]

   Equivalently, there are constants $c,C_1,R_0>0$ such that

   \[
   \frac{c}{R}\le
   \frac{F_d(iR)}{F_\gamma(iR)}
   \le\frac{C_1}{R}
   \qquad(R\ge R_0).
   \tag{4.2}
   \]

   In particular,

   \[
   \left|\frac{F_d(iR)}{F_\gamma(iR)}-1\right|\longrightarrow1,
   \tag{4.3}
   \]

   so the separation required in the original Item 4 holds for every sufficiently large
   $R$, not merely along a subsequence.

### Proof

#### Item 1

This is exactly the definition (2.6). It is a formal statement about a constant map; no
property of zeta zeros is involved.

#### Item 2

We prove the stronger assertion that the symmetric difference of the two multisets is
infinite. Suppose instead that the symmetric difference were finite. Then their counting
functions would satisfy

\[
D(t)-N(t)=m
\tag{4.4}
\]

for all sufficiently large $t$ outside the two discrete sets of jump points, where
$m\in\mathbb Z$ is constant. By (2.2) and (2.5),

\[
m=\lfloor A(t)\rfloor-A(t)-S(t)=-\{A(t)\}-S(t),
\]

so

\[
S(t)=-\{A(t)\}-m.
\tag{4.5}
\]

Integrating (4.5) and applying Lemma 3.3 gives

\[
S_1(T)=-\left(m+\frac12\right)T+O(1).
\tag{4.6}
\]

Because $m$ is an integer, $m+1/2\ne0$. Equation (4.6) contradicts the
unconditional estimate $S_1(T)=O(\log T)$. Therefore the symmetric difference is
infinite, proving Item 2.

#### Item 3

Lemma 3.2 proves convergence, evenness, normalization, and exact order $1$. A locally
uniformly convergent canonical product has precisely the zeros contributed by its factors,
with their multiplicities. If $F_d=F_\gamma$, the two functions would have the same zero
multiset, contradicting Item 2. Hence $F_d\ne F_\gamma$.

No Hadamard uniqueness theorem is needed. For comparison, the general assertion quoted
in the submitted draft is false: $1$ and $e^z$ have order at most $1$, have the same
empty zero multiset, and agree at $z=0$, but are not equal. The correct general conclusion
is that two order-$\le1$ functions with the same zeros can differ by $e^{az+b}$; evenness
and normalization would then remove that freedom in the present setting.

#### Item 4

For all sufficiently large $t$, equations (2.2) and (2.5) give, away from jump points,

\[
D(t)-N(t)=-\{A(t)\}-S(t).
\tag{4.7}
\]

The fixed initial interval contributes $O(1)$, uniformly in $R\ge1$, to (3.7).
Consequently

\[
\log\frac{F_d(iR)}{F_\gamma(iR)}
=-\int_{T_0}^{\infty}K_R(t)\{A(t)\}\,dt
 -\int_{T_0}^{\infty}K_R(t)S(t)\,dt+O(1).
\tag{4.8}
\]

For the fractional-part term, Lemma 3.3 and an integration by parts against the bounded
primitive of $\{A(t)\}-1/2$ give

\[
\int_{T_0}^{\infty}K_R(t)
\left(\{A(t)\}-\frac12\right)dt=O(1)
\tag{4.9}
\]

uniformly in $R$. Indeed, $K_R(t)$ is positive and decreasing, and its total variation
on $[T_0,\infty)$ is at most $2/T_0$. Also,

\[
\int_{T_0}^{\infty}K_R(t)\,dt
=\log\left(1+\frac{R^2}{T_0^2}\right).
\]

Therefore

\[
\int_{T_0}^{\infty}K_R(t)\{A(t)\}\,dt
=\frac12\log\left(1+\frac{R^2}{T_0^2}\right)+O(1)
=\log R+O(1).
\tag{4.10}
\]

For the $S$-term, define $G(t)=\int_{T_0}^tS(u)\,du$. By (2.3),
$G(t)=O(\log t)$. Integration by parts yields

\[
\int_{T_0}^{\infty}K_R(t)S(t)\,dt
=-\int_{T_0}^{\infty}K_R'(t)G(t)\,dt.
\tag{4.11}
\]

The boundary terms vanish. Uniformly for $R\ge T_0$,

\[
-K_R'(t)\ll
\begin{cases}
t^{-2},&T_0\le t\le R,\\
R^2t^{-4},&t\ge R.
\end{cases}
\]

Hence

\[
\int_{T_0}^{\infty}|K_R'(t)G(t)|\,dt
\ll\int_{T_0}^{R}\frac{\log t}{t^2}\,dt
 +R^2\int_R^\infty\frac{\log t}{t^4}\,dt
=O(1).
\tag{4.12}
\]

Substituting (4.10) and (4.12) into (4.8) proves (4.1). Since every factor in
$F_d(iR)/F_\gamma(iR)$ is positive, exponentiation gives (4.2), and (4.3) follows.
This proves Item 4 and the proposition. $\square$

### Corollary 4.1 — Absolute difference

The corrected proof also gives

\[
|F_d(iR)-F_\gamma(iR)|\longrightarrow\infty.
\]

Indeed, Lemma 3.2 gives $F_\gamma(iR)\to\infty$, while (4.3) shows that

\[
|F_d(iR)-F_\gamma(iR)|
=F_\gamma(iR)
\left|\frac{F_d(iR)}{F_\gamma(iR)}-1\right|
\sim F_\gamma(iR).
\]

This conclusion is valid, but it did not follow from the submitted argument merely from
"the ratio is not equal to $1$" at isolated points.

---

## 5. The submitted discrepancy formula is not correct

Let $\gamma_n$ be a **simple** zero ordinate, and assign $S(\gamma_n)$ its midpoint
value. The half-weighted zero count at $\gamma_n$ is $n-1/2$, so the exact formula is

\[
A(\gamma_n)+S(\gamma_n)=n-\frac12.
\]

Because $A(d_n)=n$,

\[
A(d_n)-A(\gamma_n)=S(\gamma_n)+\frac12.
\tag{5.1}
\]

The mean-value theorem therefore gives

\[
d_n-\gamma_n
=\frac{S(\gamma_n)+1/2}{A'(\xi_n)}
\tag{5.2}
\]

for some $\xi_n$ between $d_n$ and $\gamma_n$. Using (2.1) and
$S(\gamma_n)=O(\log\gamma_n)$, one may sharpen this to

\[
d_n-\gamma_n
=\frac{S(\gamma_n)+1/2}{A'(\gamma_n)}
 +O\!\left(\frac1{\gamma_n\log\gamma_n}\right).
\tag{5.3}
\]

Thus the submitted expression

\[
\gamma_n-d_n=\frac{S(\gamma_n)}{N'(\gamma_n)}+O(1/\gamma_n)
\]

has three defects:

1. $N$ is a step function and has no ordinary derivative at a zero; the intended
   derivative must be $A'(t)=\theta'(t)/\pi$.
2. With the midpoint convention, the sign is reversed and the term $1/2$ is mandatory.
3. At a multiple zero, the relation depends on the position inside the multiplicity block,
   so no single formula indexed as above is valid without further notation.

In particular, the fact that $S(t)\ne0$ for infinitely many arbitrary $t$ does not prove
$d_n\ne\gamma_n$ for any $n$. In fact, nonvanishing at infinitely many $t$ is already
elementary from (2.2): between consecutive zero ordinates $N(t)$ is constant while
$A(t)$ is nonconstant. The cited oscillation theorems are much stronger than what that
claim requires, but they do not repair the index/convention gap.

If a printed citation for arbitrarily large nonzero values is nevertheless desired,
K.-M. Tsang, *Acta Arith.* **46** (1986), Theorem 1, proves an unconditional
$\Omega$-theorem for $S(t)$ and therefore implies that $S(t)\ne0$ for arbitrarily large
$t$. That result is not used in Proposition G.3*.

---

## 6. Why the submitted Step 4 does not work

At $R=\gamma_n$, the $n$-th factor

\[
\frac{1+R^2/d_n^2}{1+R^2/\gamma_n^2}
\]

may differ from $1$, but the remaining infinitely many positive factors can compensate
it exactly. Therefore

\[
\text{one factor}\ne1
\quad\not\Longrightarrow\quad
\prod_k\frac{1+R^2/d_k^2}{1+R^2/\gamma_k^2}\ne1.
\]

Even the nonidentity $F_d\ne F_\gamma$ would not by itself imply that their ratio stays
away from $1$ along an unbounded sequence on the imaginary axis. The global counting
argument in Lemma 3.4 and Item 4 is what excludes compensation and proves the stronger
asymptotic (4.1).

No calculation at $R=\gamma_1$ is needed.

---

## 7. Correct low-height numerical sanity check

The numerical anchor in the submitted draft is incorrect. With the normalization in §2,
ordinary high-precision evaluation gives

\[
\begin{aligned}
\theta(14)&\approx-1.78294870041615,\\
\gamma_1&\approx14.13472514173469,\\
\theta(\gamma_1)&\approx-1.72867024667584,\\
d_1=g_0&\approx17.84559954041086.
\end{aligned}
\]

Thus $\theta(\gamma_1)$ is not close to $0$, and $d_1$ is not approximately
$\gamma_1$. These numbers are only a sanity check; none is used in the proof.

---

## 8. Logical scope of the obstruction

The corrected proposition proves a genuine noninjectivity statement for the constant map
$O_\theta$: two different multisets are sent to the same output. It yields an obstruction
for a method class only after the factorization hypothesis (2.7) has been verified from that
class's formal definition.

Accordingly, the justified conclusion is:

> Any procedure whose entire relevant observation factors through the constant map
> $O_\theta$ cannot distinguish $\mathcal Z_\gamma$ from $\mathcal Z_d$.

The stronger sentence "any procedure reading only zero-free arithmetic data cannot
distinguish them" is not established and should not appear without an independent
information/factorization theorem.

Finally, if $F_\gamma$ in the proposition is replaced by the actual Riemann function
$\Xi_{\rm R}(z)=\xi(1/2+iz)$, then Item 3 remains unconditionally true by a dichotomy:
if RH is false, $\Xi_{\rm R}$ has a nonreal zero while $F_d$ has only real zeros; if RH
is true, $\Xi_{\rm R}=F_\gamma$ and Proposition G.3* applies. However, the proof of the
imaginary-axis ratio asymptotic in Item 4 concerns the ordinate product $F_\gamma$; it
must not be advertised as an unconditional asymptotic for the actual $\Xi_{\rm R}$.

---

## 9. References

1. NIST Digital Library of Mathematical Functions, §25.10(i), especially equations
   25.10.1–25.10.2 (Hardy's $Z$-function and the Riemann–Siegel phase),
   <https://dlmf.nist.gov/25.10>.
2. E. C. Titchmarsh, revised by D. R. Heath-Brown, *The Theory of the Riemann
   Zeta-Function*, 2nd ed., Clarendon Press, Oxford, 1986, §§9.3 and 9.9.
3. A. Bondarenko and K. Seip, “Extreme values of the Riemann zeta function and its
   argument,” *Mathematische Annalen* **372** (2018), 999–1015,
   <https://doi.org/10.1007/s00208-018-1663-2>. The introduction records the standard
   convention for $S(t)$ and the unconditional bounds $S(t)=O(\log t)$ and
   $S_1(t)=O(\log t)$.
4. K.-M. Tsang, “Some $\Omega$-theorems for the Riemann zeta-function,”
   *Acta Arithmetica* **46** (1986), no. 4, 369–395. This is the correct bibliographic
   location; the submitted “J. Number Theory 23 (1986)” citation is not correct for this
   paper. Stable scan: <https://eudml.org/doc/206012>.
5. B. Ya. Levin, *Distribution of Zeros of Entire Functions*, revised ed., Translations
   of Mathematical Monographs 5, American Mathematical Society, 1980, Chapter I.
6. D. J. Platt and T. S. Trudgian, “The Riemann hypothesis is true up to
   $3\cdot10^{12}$,” *Bulletin of the London Mathematical Society* **53** (2021),
   792–797, <https://doi.org/10.1112/blms.12460>.
7. A. M. Odlyzko, “Tables of zeros of the Riemann zeta function,”
   <https://www-users.cse.umn.edu/~odlyzko/zeta_tables/>.

---

## 10. Final disposition

**Original Proposition G.3:** not confirmed as written.  
**Corrected Proposition G.3*:** proved unconditionally, subject only to the explicit
definition of $O_\theta$ in (2.6).  
**Program-level Fredholm obstruction:** conditional on separately verifying the
factorization requirement (2.7) from the missing definition of $\mathfrak M_{\rm FC}$.
