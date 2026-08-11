# OB-03 — Referee audit and complete proof

## Verdict

**Main non-uniqueness conclusion: CONFIRMED after precise quantifier repairs.**

The theorem's mathematical core is correct under all three hypotheses imposed on
\(\{\gamma_n\}\).  The proposed proof is not correct as written:

1. the parameter \(c_0\) must be quantified and restricted to be sufficiently
   small;
2. the Taylor-coefficient formula in Step B is false for orders \(j\ge 2\);
3. the Jacobian becomes a Vandermonde matrix only after passing to logarithmic
   coefficients (equivalently, reciprocal-zero power sums);
4. the asserted Step C estimate at \(R=\gamma_{k_N+1}\) does not follow, because
   the first free zero is changed by the implicit-function step and the other
   factors can compensate it;
5. the passage \(N\to\infty\) is unavailable: no hypothesis says that
   \(k_N\to\infty\) (or that \(J_N\) has any prescribed behavior).

The proof below repairs these points.  It also gives an explicit disk-separation
bound from the first Taylor coefficient that is *not* constrained by the finite
evidence.

---

## 1. Exact audit of the data and permitted prerequisites

Fix one value of \(N\), and abbreviate
\[
  k:=k_N\ge 1,\qquad J:=J_N\ge 1.
\]
The sequence is assumed to satisfy, literally,
\[
  0<\gamma_1<\gamma_2<\cdots\to\infty,
  \qquad \sum_{n\ge1}\gamma_n^{-2}<\infty,
\]
and
\[
  \gamma_n\sim \frac{n}{2\pi}\log\frac{n}{2\pi}
  \sim \frac{1}{2\pi}n\log n.
  \tag{1.1}
\]

Only the following standard results from classical complex analysis and finite-
dimensional real analysis are used:

- the locally uniform convergence criterion for infinite products;
- the power series for \(\log(1-w)\), with locally uniform termwise summation;
- the real implicit function theorem in \(\mathbb R^J\);
- the definition of the order of an entire function and elementary estimates of
  its maximum modulus;
- Cauchy's coefficient estimate.

No assertion about the Riemann hypothesis, and no analytic-number-theory theorem,
is used in the proof.

### 1.1 A nomenclature error in the source

The growth law (1.1) is **not** the asymptotic law for the ordinates of the
nontrivial zeros of the Riemann zeta function.  The Riemann--von Mangoldt formula
\[
  N(T)=\frac{T}{2\pi}\log\frac{T}{2\pi}-\frac{T}{2\pi}+O(\log T)
\]
instead gives, after inversion,
\(\gamma_n\sim 2\pi n/\log n\).  This editorial error is irrelevant to the
abstract theorem proved below, because (1.1) is treated as the actual hypothesis.

Likewise, (1.1) implies the counting asymptotic
\[
  N_\gamma(r):=\#\{n:\gamma_n\le r\}
  \sim \frac{2\pi r}{\log r},
  \tag{1.2}
\]
not \(r\log r/(2\pi)\) as stated in the draft.  Indeed, if
\(m=N_\gamma(r)\), then
\(\gamma_m\le r<\gamma_{m+1}\); both endpoints are asymptotic to
\((m/(2\pi))\log m\), and inversion gives (1.2).

### 1.2 What the square-summability assumption does and does not prove

The condition \(\sum\gamma_n^{-2}<\infty\) proves locally uniform convergence of
\(\prod_n(1-z^2/\gamma_n^2)\).  By itself it does **not** prove order at most one.
For example, \(\gamma_n=2^n\) satisfies the square-summability condition, whereas
the resulting product has order zero (its logarithmic maximum modulus is
\(O((\log r)^2)\)).  In the present problem, exact order one follows from the
additional growth assumption (1.1).

---

## 2. Corrected theorem

### Theorem

Assume (1.1) and the other hypotheses above, and set
\[
  \Xi(z)=C\prod_{n\ge1}\left(1-\frac{z^2}{\gamma_n^2}\right),
  \qquad C>0.
\]
For the fixed integers \(k,J\), there is a number
\(\delta=\delta(k,J,\{\gamma_n\})>0\) with the following property.

For every \(c\in(0,\delta)\), there is an even, real entire function \(F_c\) of
order exactly one such that

1. every zero of \(F_c\) is real;
2. its first \(k\) positive zeros are exactly
   \(\gamma_1,\ldots,\gamma_k\);
3. \(F_c(0)=C\);
4. \(F_c^{(2j)}(0)=\Xi^{(2j)}(0)\) for \(0\le j\le J\);
5. \(F_c\ne\Xi\).

More precisely, a nonzero number \(\Delta_{J+1}(c)\), defined in (6.1) below,
satisfies
\[
  [z^{2J+2}](F_c-\Xi)
  =-\frac{C}{J+1}\Delta_{J+1}(c)\ne0.
  \tag{2.1}
\]
Consequently, for every \(\varepsilon>0\), the choice
\[
  R_0=\max\left\{
       2\gamma_{k+1},
       \left(\frac{(J+1)\varepsilon}
       {C|\Delta_{J+1}(c)|}\right)^{1/(2J+2)}
       \right\}
  \tag{2.2}
\]
has \(R_0>\gamma_{k+1}\) and obeys
\[
  \sup_{|z|\le R_0}|F_c(z)-\Xi(z)|\ge\varepsilon.
\]

Thus the intended non-uniqueness theorem holds.  Formula (2.2) also makes the
dependence on the chosen perturbation parameter precise.

---

## 3. Reciprocal-square variables and the correct matching equations

For \(m\ge1\), put
\[
  a_m:=\gamma_{k+m}^{-2}.
\]
Then
\[
  a_1>a_2>\cdots>0,
  \qquad \sum_{m\ge1}a_m<\infty.
  \tag{3.1}
\]

The first \(J\) reciprocal squares will be free variables
\(u=(u_1,\ldots,u_J)\).  For \(m>J\), freeze the remaining tail at
\[
  b_m(c):=a_m\left(1+\frac{c}{m}\right)^{-2}.
  \tag{3.2}
\]
This corresponds to the real zero
\[
  \mu_{k+m}(c)=\gamma_{k+m}\left(1+\frac{c}{m}\right).
\]

For \(r=1,\ldots,J\), define
\[
  \Phi_r(u,c)
  :=\sum_{\ell=1}^J u_\ell^r
    +\sum_{m>J}b_m(c)^r
    -\sum_{m\ge1}a_m^r.
  \tag{3.3}
\]

These are the correct equations.  They ask the perturbed reciprocal-zero power
sums to agree with the reference power sums through degree \(J\).

### Smoothness of \(\Phi\)

Choose \(c_*<(J+1)/2\).  For \(|c|\le c_*\) and \(m>J\), the factor
\(1+c/m\) is bounded below by \(1/2\).  Every \(q\)-th \(c\)-derivative of
\(b_m(c)^r\) is bounded in absolute value by
\[
  K_{r,q}\,a_m^r m^{-q}
\]
for a constant independent of \(m\).  The dominating series converges, since
\(\sum_m a_m^r<\infty\).  Therefore the infinite sums in (3.3), together with
all their \(c\)-derivatives, converge uniformly on compact subintervals of
\((-c_*,c_*)\).  In particular,
\[
  \Phi:\mathbb R^J\times(-c_*,c_*)\longrightarrow\mathbb R^J
\]
is \(C^1\) (indeed real analytic).

At
\[
  u^0=(a_1,\ldots,a_J),\qquad c=0,
\]
we have \(\Phi(u^0,0)=0\), and
\[
  \frac{\partial\Phi_r}{\partial u_\ell}(u^0,0)
  =r a_\ell^{r-1}.
  \tag{3.4}
\]
Hence
\[
  \det D_u\Phi(u^0,0)
  =\left(\prod_{r=1}^Jr\right)
    \prod_{1\le p<q\le J}(a_q-a_p)\ne0.
  \tag{3.5}
\]
This is the exact scaled Vandermonde determinant; there is no unspecified
"bounded factor."

The implicit function theorem now supplies \(\delta_0>0\) and a unique \(C^1\)
map
\[
  u(c)=(u_1(c),\ldots,u_J(c)),\qquad |c|<\delta_0,
  \tag{3.6}
\]
such that
\[
  u(0)=u^0,qquad \Phi(u(c),c)=0.
  \tag{3.7}
\]

By shrinking \(\delta_0\), all \(u_\ell(c)\) remain positive and distinct, and
the corresponding numbers
\[
  \nu_{k+\ell}(c):=u_\ell(c)^{-1/2},\qquad 1\le\ell\le J,
  \tag{3.8}
\]
remain in pairwise disjoint neighborhoods of
\(\gamma_{k+1},\ldots,\gamma_{k+J}\), all lying strictly above \(\gamma_k\).

---

## 4. Definition of the perturbed function and Taylor matching

For \(0<c<\delta_0\), define
\[
\begin{split}
  F_c(z):={}&C
  \prod_{n=1}^k\left(1-\frac{z^2}{\gamma_n^2}\right)
  \prod_{\ell=1}^J(1-u_\ell(c)z^2)\\
  &\times
  \prod_{m>J}(1-b_m(c)z^2).
\end{split}
  \tag{4.1}
\]

Because \(\sum_{m>J}b_m(c)\le\sum_{m>J}a_m<\infty\), the last product
converges absolutely and locally uniformly.  Thus \(F_c\) is entire.  It is even,
real on the real axis, and has precisely the real zeros furnished by its factors.
The choice made after (3.8) ensures that no new positive zero lies at or below
\(\gamma_k\), so the first \(k\) positive zeros are exactly the pinned ones.
Also \(F_c(0)=C\).

It remains to justify that (3.7) is exactly the required Taylor matching.  On a
small disk around zero, local uniform convergence and the series for
\(\log(1-w)\) give
\[
  \log\frac{F_c(z)}{C}
  =-\sum_{r\ge1}\frac{z^{2r}}{r}P_r(F_c),
  \tag{4.2}
\]
where
\[
  P_r(F_c)=
  \sum_{n=1}^k\gamma_n^{-2r}
  +\sum_{\ell=1}^J u_\ell(c)^r
  +\sum_{m>J}b_m(c)^r.
\]
Similarly,
\[
  \log\frac{\Xi(z)}{C}
  =-\sum_{r\ge1}\frac{z^{2r}}{r}P_r(\Xi),
  \qquad
  P_r(\Xi)=\sum_{n\ge1}\gamma_n^{-2r}.
  \tag{4.3}
\]
Equations (3.3) and (3.7) say precisely that
\[
  P_r(F_c)=P_r(\Xi),\qquad 1\le r\le J.
\]
It follows from (4.2)--(4.3) that
\[
  \log\frac{F_c(z)}{\Xi(z)}=O(z^{2J+2}),
  \qquad z\to0,
\]
and hence
\[
  F_c(z)-\Xi(z)=O(z^{2J+2}).
  \tag{4.4}
\]
Therefore
\[
  F_c^{(2j)}(0)=\Xi^{(2j)}(0),
  \qquad 0\le j\le J.
\]

This also identifies the defect in the draft formula: a Taylor coefficient of a
product is an elementary symmetric function of all reciprocal squares, not one
power sum times a common nonzero factor.  Passing to the logarithm creates the
power sums and the exact Vandermonde matrix (3.5).

---

## 5. Exact order one

Finite changes of zeros do not affect the estimates below, but we give a direct
proof.

### Upper bound

From (1.1), there are constants \(d>0\) and \(n_0\) such that
\(\gamma_n\ge dn\) for \(n\ge n_0\).  For \(|z|\le r\), the frozen zeros satisfy
\(\mu_n(c)>\gamma_n\), and therefore
\[
  \log M_{F_c}(r)
  \le O(\log(2+r))
     +\sum_{n\ge n_0}\log\left(1+\frac{r^2}{d^2n^2}\right).
  \tag{5.1}
\]
By comparison with the integral of the decreasing function
\(x\mapsto\log(1+(r/(dx))^2)\), the series on the right is \(O(r)\).
Thus
\[
  \log M_{F_c}(r)=O(r),
\]
and the order of \(F_c\) is at most one.

### Lower bound

For every frozen index \(n>k+J\),
\[
  \mu_n(c)=\gamma_n\left(1+\frac{c}{n-k}\right)
  \le(1+c)\gamma_n.
\]
Consequently, if \(\gamma_n\le r/(1+c)\), then \(\mu_n(c)\le r\), and the
corresponding factor of \(|F_c(ir)|\) is at least \(2\).  Hence
\[
  \log M_{F_c}(r)
  \ge \log|F_c(ir)|
  \ge \log C+
      \bigl(N_\gamma(r/(1+c))-k-J\bigr)\log2.
  \tag{5.2}
\]
Using (1.2), the right side is bounded below by a positive constant times
\(r/\log r\) for all sufficiently large \(r\).  Therefore
\[
  \limsup_{r\to\infty}
  \frac{\log\log M_{F_c}(r)}{\log r}\ge1.
\]
Together with the upper bound, this proves that \(F_c\) has order exactly one.

This argument also repairs Step A: the factors counted in the lower bound must
be those with \(\mu_n(c)\le r\) (or, as above, with
\(\gamma_n\le r/(1+c)\)); the implication
\(\gamma_n\le r\Rightarrow\mu_n(c)\le r\) used in the draft is false.

---

## 6. The first unmatched coefficient is nonzero

Define
\[
  \Delta_{J+1}(c):=
  \sum_{\ell=1}^J u_\ell(c)^{J+1}
  +\sum_{m>J}b_m(c)^{J+1}
  -\sum_{m\ge1}a_m^{J+1}.
  \tag{6.1}
\]
At \(c=0\), this is zero.  We prove that its derivative at zero is nonzero.

Let \(v_\ell:=u_\ell'(0)\).  Since
\[
  b_m'(0)=-\frac{2a_m}{m},
\]
differentiating \(\Phi_r(u(c),c)=0\) at \(c=0\) and dividing by \(r\) gives
\[
  \sum_{\ell=1}^J v_\ell a_\ell^{r-1}
  =\sum_{m>J}d_m a_m^{r-1},
  \qquad 1\le r\le J,
  \tag{6.2}
\]
where
\[
  d_m:=\frac{2a_m}{m}>0.
\]

Let
\[
  q(x):=\prod_{\ell=1}^J(x-a_\ell).
\]
The equalities (6.2) match all moments of degrees \(0,\ldots,J-1\).  Since
\(q(a_\ell)=0\), they imply
\[
\begin{split}
  \sum_{\ell=1}^Jv_\ell a_\ell^J
  -\sum_{m>J}d_m a_m^J
  &=-\sum_{m>J}d_m q(a_m).
\end{split}
  \tag{6.3}
\]
The series converges absolutely because \(q(a_m)\) is bounded and
\(\sum d_m<\infty\).  Moreover,
\[
  0<a_m<a_J<\cdots<a_1\qquad(m>J),
\]
so every \(q(a_m)\) has the same strict sign \((-1)^J\).  The right side of
(6.3) is therefore nonzero.  Differentiating (6.1) now yields
\[
\begin{split}
  \Delta_{J+1}'(0)
  &=(J+1)\left(
     \sum_{\ell=1}^Jv_\ell a_\ell^J
     -\sum_{m>J}d_m a_m^J
     \right)\\
  &=-(J+1)\sum_{m>J}d_mq(a_m)\ne0.
\end{split}
  \tag{6.4}
\]
In fact its sign is \((-1)^{J+1}\).

After shrinking \(\delta_0\) to some \(\delta>0\), equation (6.4) guarantees
\[
  \Delta_{J+1}(c)\ne0,
  \qquad 0<c<\delta.
  \tag{6.5}
\]

Equations (4.2)--(4.3), together with equality of the first \(J\) power sums,
then give
\[
  \log\frac{F_c(z)}{\Xi(z)}
  =-\frac{\Delta_{J+1}(c)}{J+1}z^{2J+2}
   +O(z^{2J+4}).
\]
Because \(F_c(0)=\Xi(0)=C\), it follows that
\[
  F_c(z)-\Xi(z)
  =-\frac{C\Delta_{J+1}(c)}{J+1}z^{2J+2}
   +O(z^{2J+4}),
  \tag{6.6}
\]
which proves both (2.1) and \(F_c\ne\Xi\).

---

## 7. Quantitative separation on a disk

Set \(G_c:=F_c-\Xi\) and
\[
  A_c:=\left|[z^{2J+2}]G_c\right|
  =\frac{C|\Delta_{J+1}(c)|}{J+1}>0.
\]
Cauchy's coefficient estimate gives, for every \(R>0\),
\[
  A_c\le \frac{\sup_{|z|\le R}|G_c(z)|}{R^{2J+2}}.
\]
Thus
\[
  \sup_{|z|\le R}|F_c(z)-\Xi(z)|
  \ge A_cR^{2J+2}.
  \tag{7.1}
\]
Taking \(R=R_0\) from (2.2) proves the required inequality for every
\(\varepsilon>0\), for the fixed evidence record \(\mathcal E_N\).  No limit in
\(N\) is needed.

---

## 8. What remains true about the proposed tail ratio

For a fixed \(R>0\), the frozen infinite product in the draft does converge to a
strictly positive finite number.  Indeed,
\[
  Q_R(c):=\prod_{m>J}
  \frac{1+R^2b_m(c)}{1+R^2a_m}
\]
has factors in \((0,1]\), and
\[
  0\le
  1-\frac{1+R^2b_m(c)}{1+R^2a_m}
  =\frac{R^2(a_m-b_m(c))}{1+R^2a_m}
  \le R^2a_m.
\]
Since \(\sum a_m<\infty\), the standard positive-product criterion gives
\[
  0<Q_R(c)\le1.
\]

This positivity is only a bound for fixed \(R,k,J,c\); it supplies no uniform
lower bound depending on \(c\) alone.  More importantly, the adjusted free
factors can be greater than one and can partially compensate the frozen tail.
Thus it does not justify
\[
  |F(i\gamma_{k+1})-\Xi(i\gamma_{k+1})|
  \ge (1-\eta(c))|\Xi(i\gamma_{k+1})|.
\]
The coefficient argument in Sections 6--7 is the valid replacement.

---

## 9. Referee checklist

| Item | Verdict | Precise conclusion |
|---|---|---|
| Product convergence | Confirmed | Follows from summability of reciprocal squares. |
| Order \(1\) from square summability alone | Rejected | The growth hypothesis is essential; \(\gamma_n=2^n\) is a counterexample. |
| Step A under all stated hypotheses | Confirmed after repair | Use (5.1)--(5.2); the draft counted the wrong factors and inverted \(N_\gamma\) incorrectly. |
| Direct Taylor formula in Step B | Rejected | Taylor coefficients are elementary symmetric functions, not individual power sums times a common factor. |
| IFT/Vandermonde mechanism | Confirmed after reformulation | The power-sum map (3.3) has the exact Jacobian (3.4)--(3.5). |
| Size of \(c_0\) | Corrected | IFT proves the result only for \(0<c_0<\delta(k,J,\gamma)\). |
| Frozen tail product for fixed \(R\) | Confirmed | It converges to a positive number, but the bound is not uniform in the omitted parameters. |
| Original Step C argument | Rejected | It ignores the free-zero adjustment and uses an unjustified \(N\to\infty\) limit. |
| Main non-uniqueness theorem | Confirmed | Equations (6.6) and (7.1) give a nonzero coefficient and the required quantitative separation. |

**Final status: the intended theorem is proved, but only by the corrected statement
and proof above; the original Steps B and C must not be cited as written.**
