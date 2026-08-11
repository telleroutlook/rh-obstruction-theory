# Problem OB-01-D — Heat-trace logarithms for elliptic operators

## Referee-ready audit, counterexample, and corrected theorem

**Verdict.** The three claims in the supplied draft cannot all be accepted.

| Item | Verdict | Precise outcome |
|---|---|---|
| Claim A | **REFUTED** | A positive classical elliptic pseudodifferential operator on a closed manifold can have heat-trace terms \(t^k\log t\), \(k\ge 1\). Moreover, the regular coefficients at nonnegative integral powers need not be local. An explicit operator on \(S^1\) is proved below. |
| Claim B | **PARTLY CONFIRMED AFTER RESTRICTION** | Smooth elliptic **differential** operators with smooth local strongly elliptic boundary conditions have the usual power expansion without logarithms. Pseudodifferential/nonlocal boundary conditions can introduce logarithms. Absence of boundary alone does not exclude all logarithms for general classical pseudodifferential generators. |
| Claim C | **REFUTED AS STATED** | The cited log-polyhomogeneous theorem concerns a weighted trace \(\operatorname{Tr}(Ae^{-tP})\), with \(A\) log-polyhomogeneous and the heat generator \(P\) classical. It does not give the asserted formula for \(\operatorname{Tr}(e^{-tH})\) when \(H\) itself is log-polyhomogeneous. The stated \(d=m=1\) symbol and cosphere calculation are also inconsistent. |

There is, however, a useful corrected obstruction:

> **Correct leading-singularity obstruction.** If \(H\) is a positive self-adjoint classical elliptic pseudodifferential operator of order \(m>0\) on a closed \(d\)-manifold, then its leading heat-trace term is a nonzero pure power \(a_0t^{-d/m}\), with no factor \(\log(1/t)\). Logarithms may occur only at nonnegative integral powers of \(t\) (and the \(t^0\log t\) coefficient is zero). Consequently such an \(H\) cannot satisfy
>
> \[
> \operatorname{Tr}(e^{-tH})\sim C\,t^{-d/m}\log(1/t),
> \qquad C\ne0.
> \]

Thus an obstruction to the *leading* singularity \(t^{-1}\log(1/t)\) survives, but the stronger assertion “no logarithmic term at any order” does not.

---

## 1. Exact setting and notation

Let \(M\) be a compact smooth manifold without boundary, \(\dim M=d\ge1\), and let \(E\to M\) be a finite-rank Hermitian vector bundle. A **classical** pseudodifferential operator \(H\in\mathrm{CL}^m(M;E)\) has a full symbol

\[
h(x,\xi)\sim\sum_{j=0}^{\infty}h_{m-j}(x,\xi),
\qquad
h_{m-j}(x,r\xi)=r^{m-j}h_{m-j}(x,\xi)
\quad(r\ge1,\ |\xi|\ge1).
\]

Assume that \(H\) is elliptic, self-adjoint, and strictly positive. Then \(e^{-tH}\) is trace class for every \(t>0\), and

\[
Z_H(t):=\operatorname{Tr}(e^{-tH})
=\sum_n e^{-t\lambda_n}.
\]

For a classical operator \(Q\), write

\[
\operatorname{Wres}(Q)
:=(2\pi)^{-d}\int_{S^*M}
\operatorname{tr}_E q_{-d}(x,\xi)\,dS,
\]

where \(q_{-d}\) is the homogeneous symbol component of degree \(-d\). This is the Wodzicki residue in the standard normalization.

The only external analytic inputs used below are the classical complex-power/trace-expansion theorem of Seeley–Grubb–Seeley, in the explicit form recorded by Lesch, and the standard Mellin inversion formula. The counterexample itself is also verified directly, without relying on those inputs.

---

## 2. Citation and scope audit

### 2.1 Berline–Getzler–Vergne

The number **Theorem 2.30** is a valid heat-kernel reference in:

> N. Berline, E. Getzler, M. Vergne, *Heat Kernels and Dirac Operators*, Grundlehren der mathematischen Wissenschaften 298, Springer, 1992; corrected reprint, 2004, Theorem 2.30.

Its relevant scope is the heat kernel of a **generalized Laplacian**, hence a second-order differential operator of Laplace type. It does not assert the claimed no-log expansion for every classical pseudodifferential operator of arbitrary positive order.

### 2.2 Gilkey

The citation “Gilkey, Theorem 1.8.1” is incorrect for the desired heat expansion. The relevant result is:

> P. B. Gilkey, *Invariance Theory, the Heat Equation, and the Atiyah–Singer Index Theorem*, 2nd ed., CRC Press, 1995 (some front matter bears the 1994 copyright date), **Lemma 1.8.2**.

That lemma concerns a self-adjoint elliptic **partial differential operator** with positive-definite leading symbol. Lemma 1.8.1 is not the general heat-kernel expansion invoked in the draft. Consequently Gilkey's result also does not support Claim A at the stated pseudodifferential level of generality.

### 2.3 The correct closed-manifold pseudodifferential reference

For a classical elliptic pseudodifferential heat generator, the appropriate structure theorem is:

> M. Lesch, “On the noncommutative residue for pseudodifferential operators with log-polyhomogeneous symbols,” *Annals of Global Analysis and Geometry* **17** (1999), 151–187, **Theorem 3.7 and equations (3.18)–(3.19)**; the classical case \(k=0\) is summarized already in equations (1.3)–(1.4). Lesch explicitly traces the underlying result to G. Grubb and R. Seeley, “Weakly parametric pseudodifferential operators and Atiyah–Patodi–Singer boundary problems,” *Inventiones Mathematicae* **121** (1995), 481–529, **Theorem 2.7**.

For a classical insertion \(A\in\mathrm{CL}^a\) and a classical positive elliptic generator \(P\in\mathrm{CL}^m\), this gives the unambiguously indexed form

\[
\operatorname{Tr}(Ae^{-tP})
\sim
\sum_{\substack{j\ge0\\j-a-d\notin m\mathbb Z_{\ge0}}}
c_jt^{(j-a-d)/m}
+\sum_{k\ge0}(c'_k\log t+d_k)t^k.
\]

In particular, even when \(A=I\), logarithmic terms are allowed at nonnegative integral powers of \(t\). The coefficients of the nonintegral powers and of the logarithmic terms are local symbol invariants; the regular coefficients \(d_k\) can contain global information. Thus the locality assertion in Claim A also requires correction.

### 2.4 An independent published warning against Claim A

C. Bär and S. Moroianu, “Heat kernel asymptotics for roots of generalized Laplacians,” *International Journal of Mathematics* **14** (2003), 397–412, **Theorems 7 and 8**, exhibit logarithmic terms for roots of Laplace-type operators on closed manifolds in the relevant parity cases. Such roots are classical elliptic pseudodifferential operators. This independently rules out the proposed blanket no-log theorem.

---

## 3. Correct theorem for a classical generator on a closed manifold

### Theorem 3.1 — General heat-trace structure and residue criterion

Let \(H\in\mathrm{CL}^m(M;E)\), \(m>0\), be positive, self-adjoint, and elliptic on a closed \(d\)-dimensional manifold. Then

\[
Z_H(t)
\sim
\sum_{\substack{j\ge0\\j-d\notin m\mathbb Z_{\ge0}}}
c_jt^{(j-d)/m}
+\sum_{k=0}^{\infty}(b_k\log t+d_k)t^k,
\qquad t\downarrow0.
\tag{3.1}
\]

The restriction in the first sum prevents double-counting when an exponent is a nonnegative integer. The logarithmic coefficient at \(t^k\) is governed by

\[
\boxed{
[t^k\log(1/t)]\,Z_H(t)
=\frac{(-1)^k}{m\,k!}\operatorname{Wres}(H^k)
}
\qquad(k\in\mathbb Z_{\ge0}).
\tag{3.2}
\]

In particular:

1. \(\operatorname{Wres}(I)=0\), so there is no \(t^0\log t\) term.
2. Logarithms can occur at \(t^k\), \(k\ge1\), for a general classical pseudodifferential \(H\).
3. All logarithmic coefficients vanish if and only if
   \(\operatorname{Wres}(H^k)=0\) for every \(k\ge1\).
4. If \(H\) is a differential operator, then every \(H^k\) is differential and has zero Wodzicki residue, so no logarithmic terms occur.
5. The leading term is a pure power

   \[
   Z_H(t)=c_0t^{-d/m}+o(t^{-d/m}),
   \qquad c_0>0,
   \tag{3.3}
   \]

   and hence never \(Ct^{-d/m}\log(1/t)\).

#### Proof

For \(\Re s>d/m\), define the spectral zeta function

\[
\zeta_H(s)=\operatorname{Tr}(H^{-s}).
\]

Seeley's complex-power theorem and the Grubb–Seeley trace expansion give a meromorphic continuation of \(\zeta_H\) with at most simple poles at

\[
s=\frac{d-j}{m},
\qquad j\in\mathbb Z_{\ge0}.
\]

For \(\gamma>d/m\), Mellin inversion gives

\[
Z_H(t)=\frac{1}{2\pi i}\int_{\Re s=\gamma}
\Gamma(s)\zeta_H(s)t^{-s}\,ds.
\tag{3.4}
\]

Shifting the contour across the poles yields (3.1). At a point \(s=-k\), \(k\in\mathbb Z_{\ge0}\), the gamma function has residue

\[
\operatorname*{Res}_{s=-k}\Gamma(s)=\frac{(-1)^k}{k!}.
\]

Moreover, by the defining relation between the zeta residue and the Wodzicki residue,

\[
\operatorname*{Res}_{s=-k}\zeta_H(s)
=\frac1m\operatorname{Wres}(H^k).
\tag{3.5}
\]

If the quantity in (3.5) is nonzero, \(\Gamma(s)\zeta_H(s)\) has a double pole at \(-k\). Writing \(s=-k+u\), the double-pole contribution contains

\[
\frac{(-1)^k}{m\,k!}\operatorname{Wres}(H^k)
\frac{t^k e^{-u\log t}}{u^2}.
\]

The residue in \(u\) is therefore

\[
\frac{(-1)^k}{m\,k!}\operatorname{Wres}(H^k)\,
t^k\log(1/t),
\]

which proves (3.2). Since the symbol of \(I\) has no component of degree \(-d\), \(\operatorname{Wres}(I)=0\). If \(H\) is differential, so is \(H^k\), and again there is no negative-degree homogeneous symbol component; hence every residue vanishes.

Finally, the leading pole \(s=d/m>0\) does not coincide with a pole of \(\Gamma\), so it produces only the pure power \(t^{-d/m}\). Equivalently, its coefficient is the positive phase-space integral

\[
c_0=(2\pi)^{-d}\int_{T^*M}
\operatorname{tr}_E(e^{-h_m(x,\xi)})\,d\xi\,dx>0
\]

in the scalar-positive principal-symbol case, with the usual invariant interpretation in general. This proves (3.3). ∎

### Corollary 3.2 — The usable replacement for Claim A

No positive classical elliptic pseudodifferential operator on a closed \(d\)-manifold can have \(Ct^{-d/m}\log(1/t)\), \(C\ne0\), as its leading heat-trace singularity. This is strictly weaker than the false statement that its heat trace contains no logarithms anywhere.

---

## 4. Explicit closed-manifold counterexample to Claim A

### Proposition 4.1

There exists a positive self-adjoint classical elliptic pseudodifferential operator \(H\) of order one on the closed manifold \(S^1\) whose heat trace has a nonzero \(t\log(1/t)\) term.

#### Construction

Write \(S^1=\mathbb R/(2\pi\mathbb Z)\) and let

\[
e_n(x)=(2\pi)^{-1/2}e^{inx},
\qquad n\in\mathbb Z.
\]

Choose a smooth positive even function \(r(\xi)\) with \(r(\xi)=|\xi|\) for \(|\xi|\ge1\), and fix \(a>0\). Define the Fourier multiplier

\[
h(\xi)=r(\xi)+\frac{a}{r(\xi)},
\qquad He_n=h(n)e_n.
\]

For \(|\xi|\ge1\),

\[
h(\xi)=|\xi|+a|\xi|^{-1}.
\]

Thus \(h\) is a classical symbol of order one, with no logarithm in its symbol expansion. It is elliptic and positive, and \(H\) is self-adjoint. Put \(h_0=h(0)>0\). Its heat trace is

\[
Z_H(t)=e^{-th_0}+2\sum_{n=1}^{\infty}e^{-t(n+a/n)}.
\tag{4.1}
\]

#### Direct asymptotic calculation

For \(u\ge0\), \(0\le e^{-u}-1+u\le u^2/2\). Consequently,

\[
\sum_{n\ge1}e^{-tn}
\left(e^{-at/n}-1+\frac{at}{n}\right)=O(t^2),
\tag{4.2}
\]

because \(\sum n^{-2}<\infty\). Hence

\[
\sum_{n\ge1}e^{-t(n+a/n)}
=\sum_{n\ge1}e^{-tn}
-at\sum_{n\ge1}\frac{e^{-tn}}n+O(t^2).
\tag{4.3}
\]

The two sums are exact elementary functions:

\[
\sum_{n\ge1}e^{-tn}=\frac1{e^t-1}
=t^{-1}-\frac12+\frac{t}{12}+O(t^3),
\]

\[
\sum_{n\ge1}\frac{e^{-tn}}n
=-\log(1-e^{-t})
=\log(1/t)+\frac t2+O(t^2).
\]

Substituting into (4.1)–(4.3) gives

\[
\boxed{
Z_H(t)=\frac2t-2a\,t\log(1/t)
+\left(\frac16-h_0\right)t+O(t^2)
}
\qquad(t\downarrow0).
\tag{4.4}
\]

The logarithmic coefficient is nonzero. In residue language, the degree \(-1\) symbol of \(H\) is \(a|\xi|^{-1}\), so

\[
\operatorname{Wres}(H)
=(2\pi)^{-1}\int_0^{2\pi}
\bigl(a+a\bigr)\,dx=2a,
\]

and (3.2) gives \([t\log(1/t)]Z_H=-2a\), agreeing with (4.4).

For \(d=m=1\), Claim A's asserted remainder after retaining the \(t^{-1}\) and \(t^0\) terms would be \(O(t)\). Formula (4.4) contains \(t\log(1/t)\), which is not \(O(t)\). Thus both the no-log assertion and the stated remainder estimate fail. ∎

---

## 5. Claim B: boundary conditions

### 5.1 Correct no-log statement

Let \(P\) be a smooth elliptic **differential** operator on a compact smooth manifold with smooth boundary, and let \(B\) be a smooth local differential boundary system satisfying the usual strong/parameter ellipticity hypotheses. Then the realized operator \(P_B\) has a heat-trace expansion in pure powers,

\[
\operatorname{Tr}(e^{-tP_B})
\sim\sum_{j\ge0}C_j t^{(j-d)/m},
\qquad t\downarrow0,
\tag{5.1}
\]

with no logarithmic terms. The coefficients are sums of local interior and boundary integrals.

For a Laplace-type operator (\(m=2\)) with Dirichlet or Robin boundary conditions, the standard canonical form is

\[
\operatorname{Tr}(e^{-tP_B})
\sim\sum_{n=0}^{\infty}a_n(P,B)t^{(n-d)/2},
\qquad
a_n=a_n^M+a_n^{\partial M},
\tag{5.2}
\]

where \(a_n^M\) is the interior contribution, \(a_n^{\partial M}\) is the boundary contribution, and \(a_n^M=0\) for odd \(n\). This is the clean way to encode the familiar integer/half-integer pattern.

The draft's displayed “two-series” formula is at best bookkeeping: its two exponent sets overlap after reindexing, and for a general order-\(m\) boundary problem the structure depends on the boundary operators. It should be replaced by (5.1), or by (5.2) in the Laplace-type case.

An explicit accessible statement for Dirichlet/Robin Laplace-type problems is equation (1) in P. Gilkey, K. Kirsten, J. H. Park, and D. Vassilevich, “Asymptotics of the heat equation with ‘exotic’ boundary conditions or with time dependent coefficients” (2001). For the general comparison with pseudodifferential boundary conditions, see G. Grubb, “Trace expansions for pseudodifferential boundary problems for Dirac-type operators and more general systems,” *Arkiv för Matematik* **37** (1999), 45–86, **Theorem 9.1 and Corollary 9.2**. Grubb explicitly notes that differential boundary operators yield no logarithmic terms, whereas the general pseudodifferential case has log terms.

### 5.2 When boundary logarithms can appear

Logarithmic terms can occur when the boundary problem contains genuinely pseudodifferential or nonlocal data, such as general spectral/Atiyah–Patodi–Singer-type boundary projections. Under Grubb's hypotheses the expansion has terms of the form

\[
(\beta_k\log t+\gamma_k)t^{k/m}.
\]

Additional logarithms can also arise from singular geometries or nonsmooth boundary decompositions; those are outside the smooth local problem considered here.

### 5.3 Consequence for the proposed class \(\mathcal C_{\mathrm{ell}}\)

The restriction “compact manifold without boundary” removes boundary-generated logarithms, but it is **not sufficient to remove all logarithms** if \(\mathcal C_{\mathrm{ell}}\) still contains arbitrary classical elliptic pseudodifferential operators. Proposition 4.1 is a counterexample inside that boundaryless class.

There are two sound replacements:

1. restrict \(\mathcal C_{\mathrm{ell}}\) to positive elliptic **differential** operators; or
2. retain pseudodifferential operators but impose the exact residue condition

   \[
   \operatorname{Wres}(H^k)=0
   \quad\text{for every }k\ge1.
   \]

If the program needs only to exclude a *leading* \(t^{-d/m}\log(1/t)\) term, no extra residue assumption is needed: Corollary 3.2 already supplies that weaker obstruction for every classical elliptic pseudodifferential generator on a closed manifold.

---

## 6. Claim C: log-polyhomogeneous symbols

### 6.1 Internal symbol-order inconsistency

In the draft's definition,

\[
\tau_{m-j}(x,r\xi)=r^{m-j}\tau_{m-j}(x,\xi).
\]

Therefore, when \(m=1\), a constant coefficient \(c\) is homogeneous of degree \(0\), not degree \(1\). The expression

\[
\tau_1(x,\xi)=c|\xi|^0=c
\]

contradicts the definition. It would be a \(\tau_0\) term. A degree-one \(\tau_1\) would instead have the form \(c|\xi|\) in the scalar isotropic model.

### 6.2 The cited theorem has a different heat generator

Lesch's Theorem 3.7 assumes

\[
A\in\mathrm{CL}^{a,k}(M;E)
\quad\text{is log-polyhomogeneous},
\qquad
P\in\mathrm{CL}^{m,0}(M;E)
\quad\text{is a classical elliptic generator},
\]

and proves an expansion for the **weighted heat trace**

\[
\operatorname{Tr}(Ae^{-tP}).
\]

Lesch explicitly restricts the heat generator \(P\) to the classical class in that theorem. One cannot set \(A=I\), rename \(P\) as a log-polyhomogeneous \(H\), and infer the draft's formula for \(\operatorname{Tr}(e^{-tH})\). This is the central category error in Claim C.

### 6.3 Correct leading coefficient for the weighted-trace interpretation

For completeness, suppose \(P\) has positive scalar principal symbol \(p_m\), and the leading logarithmic symbol of \(A\) is

\[
a_{a,1}(x,\xi)\log|\xi|
=\tau_a(x,\xi)\log|\xi|,
\qquad
\tau_a(x,r\xi)=r^a\tau_a(x,\xi).
\]

Put \(q=(d+a)/m>0\). The leading symbol integral is

\[
(2\pi)^{-d}\int_{T^*M}
\operatorname{tr}\!\left(
\tau_a(x,\xi)\log|\xi|\,e^{-tp_m(x,\xi)}
\right)\,d\xi\,dx.
\]

Scaling \(\xi=t^{-1/m}\eta\) and then integrating radially gives the coefficient

\[
\boxed{
[t^{-q}\log(1/t)]\operatorname{Tr}(Ae^{-tP})
=\frac{\Gamma(q)}{m^2(2\pi)^d}
\int_{S^*M}
\operatorname{tr}\!\left(\tau_a p_m^{-q}\right)\,dS
}.
\tag{6.1}
\]

Formula (6.1) uses the convention \(\log|\xi|\). If the symbol is instead written using \(\log p_m\), the leading logarithm is multiplied by \(m\), changing \(m^2\) to \(m\). This convention dependence is another reason the coefficient cannot be quoted without specifying the precise symbol normalization.

Equation (6.1) is a statement about \(\operatorname{Tr}(Ae^{-tP})\), not about \(\operatorname{Tr}(e^{-tH})\) for a log-polyhomogeneous generator \(H\).

### 6.4 The circle computation in the draft is wrong

Take the standard circle of length \(2\pi\), \(P=|D|\), and the weight \(A=c\log|D|\) on the nonzero Fourier modes. Here \(d=m=1\), \(a=0\), \(q=1\), and \(p_1=1\) on \(S^*S^1\). The cosphere has two sheets, \(\xi=+1\) and \(\xi=-1\), so

\[
\int_{S^*S^1}c\,dS
=\int_0^{2\pi}(c+c)\,dx=4\pi c.
\]

Thus (6.1) yields

\[
[t^{-1}\log(1/t)]
\operatorname{Tr}(c\log|D|\,e^{-t|D|})=2c,
\]

in agreement with

\[
2c\sum_{n\ge1}(\log n)e^{-tn}
\sim\frac{2c}{t}\log(1/t).
\]

It is not \(c/(2\pi)\). More generally, for a circle of length \(L\), the same coefficient is \(cL/\pi\). The draft omitted both the base integral and the two cotangent directions.

### 6.5 A log term in the generator does not give the asserted leading heat term

Correct the draft's constant coefficient to degree zero, fix \(c>0\), and consider the positive Fourier multiplier

\[
H_c e_n=(|n|+c\log|n|)e_n
\]

for sufficiently large \(|n|\), with the finitely many low modes defined positively. This is a log-polyhomogeneous order-one symbol with a lower-order \(c\log|\xi|\) term. Its heat trace has

\[
Z_{H_c}(t)
=2\sum_{n\ge1}e^{-tn}n^{-ct}+O(1)
=\frac2t-2c\log(1/t)+O(1).
\tag{6.2}
\]

Indeed, on the range relevant to the Laplace sum,
\(n^{-ct}=1-ct\log n+O(t^2\log^2n)\), while

\[
\sum_{n\ge1}(\log n)e^{-tn}
=t^{-1}\log(1/t)+O(t^{-1}).
\]

After splitting off the exponentially small range \(n>t^{-2}\), the summed Taylor remainder is \(O(t\log^2(1/t))\), which proves (6.2). The logarithm occurs at order \(t^0\), not as \(t^{-1}\log(1/t)\).

If a positive degree-one term \(c|\xi|\log|\xi|\) is placed in the leading symbol instead, the eigenvalues grow like \(n\log n\), faster than linearly; the leading heat trace is correspondingly smaller, of order \(1/(t\log(1/t))\), not \(t^{-1}\log(1/t)\).

### 6.6 What growth actually produces \(t^{-1}\log(1/t)\)

A counting law

\[
N_H(\Lambda)\sim C\Lambda\log\Lambda
\]

does yield

\[
\operatorname{Tr}(e^{-tH})
\sim C\,t^{-1}\log(1/t)
\]

by the standard Laplace–Stieltjes/Karamata argument. On the standard full circle, where the modes \(\pm n\) have multiplicity two, one can model the coefficient \(C=(2\pi)^{-1}\) by eigenvalues

\[
\lambda_{\pm n}\sim\frac{4\pi n}{\log n}.
\]

This corresponds to symbol growth \(|\xi|/\log|\xi|\), up to the displayed constant. It is not a classical elliptic order-one symbol, and it is not in Lesch's finite nonnegative-log-degree class \(\mathrm{CL}^{1,k}\). Hence it is a genuinely different escape route from the classical obstruction.

---

## 7. Final corrected statement suitable for use as “Theorem D”

### Theorem D (corrected)

Let \(M\) be a compact smooth manifold without boundary, \(\dim M=d\ge1\), and let \(H\) be a positive self-adjoint classical elliptic pseudodifferential operator of order \(m>0\). Then

\[
\operatorname{Tr}(e^{-tH})
=a_0t^{-d/m}+o(t^{-d/m}),
\qquad a_0>0,
\]

and no term \(Ct^{-d/m}\log(1/t)\), \(C\ne0\), can occur. The complete expansion may nevertheless contain terms \(t^k\log t\), \(k\ge1\), whose coefficients are given by (3.2).

In particular, if a target spectrum has

\[
\operatorname{Tr}(e^{-tH_{\rm target}})
\sim \frac{1}{2\pi}\frac{\log(1/t)}{t},
\]

then it cannot be the spectrum, with multiplicity, of a positive classical elliptic order-one pseudodifferential operator on a closed one-dimensional manifold.

#### Proof

The first assertion is Theorem 3.1(5). Dividing by \(t^{-d/m}\log(1/t)\) gives

\[
\frac{\operatorname{Tr}(e^{-tH})}
{t^{-d/m}\log(1/t)}
=\frac{a_0+o(1)}{\log(1/t)}
\longrightarrow0,
\]

whereas the proposed target ratio tends to a nonzero constant. The two asymptotics are incompatible. ∎

---

## 8. Acceptance-criteria checklist

1. **Claim A:** refuted. BGV Theorem 2.30 is correctly numbered but applies to generalized Laplacians, not arbitrary classical pseudodifferential operators. Gilkey's relevant result is Lemma 1.8.2, not Theorem 1.8.1, and also concerns differential operators. Proposition 4.1 is an explicit counterexample.
2. **Claim B:** no-log is confirmed for smooth differential generators with smooth local strongly elliptic boundary conditions. Pseudodifferential/nonlocal boundary conditions can create logarithms. Boundarylessness alone does not exclude all logarithms in the general pseudodifferential class.
3. **Claim C:** refuted as a statement about the ordinary heat trace of a log-polyhomogeneous generator. The verifiable exact source is Lesch 1999, Theorem 3.7 and equations (3.18)–(3.19), but its object is \(\operatorname{Tr}(Ae^{-tP})\) with classical \(P\). Formula (6.1) gives the corrected leading weighted-trace coefficient under explicit conventions.
4. **Explicit classical counterexample:** \(He_n=(|n|+a/|n|)e_n\) for \(n\ne0\), smoothly completed at low frequency, is positive classical elliptic on \(S^1\) and has the term \(-2a\,t\log(1/t)\).
5. **Programmatic conclusion:** the all-orders no-log theorem fails, but the leading-log obstruction needed to rule out \(t^{-1}\log(1/t)\) remains valid in the classical closed-manifold class.

---

## References

1. N. Berline, E. Getzler, M. Vergne, *Heat Kernels and Dirac Operators*, Grundlehren der mathematischen Wissenschaften 298, Springer, 1992; corrected reprint 2004, Theorem 2.30.
2. P. B. Gilkey, *Invariance Theory, the Heat Equation, and the Atiyah–Singer Index Theorem*, 2nd ed., CRC Press, 1995, Lemma 1.8.2.
3. R. T. Seeley, “Complex powers of an elliptic operator,” *Proceedings of Symposia in Pure Mathematics* **10** (1967), 288–307.
4. G. Grubb and R. T. Seeley, “Weakly parametric pseudodifferential operators and Atiyah–Patodi–Singer boundary problems,” *Inventiones Mathematicae* **121** (1995), 481–529, Theorem 2.7.
5. M. Lesch, “On the noncommutative residue for pseudodifferential operators with log-polyhomogeneous symbols,” *Annals of Global Analysis and Geometry* **17** (1999), 151–187, Theorem 3.7, equations (3.18)–(3.19), Definition 4.1, and Corollary 4.8. DOI: 10.1023/A:1006504318696.
6. G. Grubb, “Trace expansions for pseudodifferential boundary problems for Dirac-type operators and more general systems,” *Arkiv för Matematik* **37** (1999), 45–86, Theorem 9.1 and Corollary 9.2. DOI: 10.1007/BF02384828.
7. C. Bär and S. Moroianu, “Heat kernel asymptotics for roots of generalized Laplacians,” *International Journal of Mathematics* **14** (2003), 397–412, Theorems 7–8. DOI: 10.1142/S0129167X03001788.
8. P. B. Gilkey, K. Kirsten, J. H. Park, D. Vassilevich, “Asymptotics of the heat equation with ‘exotic’ boundary conditions or with time dependent coefficients,” arXiv:math-ph/0105009, equation (1).
