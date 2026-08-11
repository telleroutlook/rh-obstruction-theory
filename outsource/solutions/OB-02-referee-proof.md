# Problem OB-02 — Exact finite-observation collision with integer multiplicities (Theorem B2)

**Referee-ready verdict:** **CONFIRMED**, after correcting two auxiliary contribution
formulas in the draft. The theorem itself is true under the stated definitions.
The original proof sketch is not valid verbatim because its displayed matrix and
quartet vector do not equal the contributions prescribed by the stated observation
functional. A corrected, self-contained proof is given below.

---

## 1. Exact statement and permitted inputs

Fix an integer \(m\geq 1\) and distinct rational numbers
\[
0<t_1<\cdots<t_m.
\]
An **admissible symmetric zero multiset** is a locally finite multiset
\(\mathcal Z\subset\{s\in\mathbb C:0<\operatorname{Re}s<1\}\) such that:

1. \(\rho\in\mathcal Z\) implies \(\bar\rho\in\mathcal Z\) with the same
   multiplicity;
2. \(\rho\in\mathcal Z\) implies \(1-\rho\in\mathcal Z\) with the same
   multiplicity; and
3. \(\sum_{\rho\in\mathcal Z}|\rho|^{-2}<\infty\), with multiplicities counted.

Define \(P(\mathcal Z)=1\) precisely when every element of \(\mathcal Z\) has
real part \(1/2\), and define \(P(\mathcal Z)=0\) otherwise.

For \(j=1,\ldots,m\), put
\[
\varphi_j(\rho)=1-\left(1-\frac1\rho\right)^j
\]
and, for a finite multiset \(\mathcal Z\) in the open critical strip, define
\[
O_j(\mathcal Z)
=\sum_{\rho\in\mathcal Z}
  \bigl(\varphi_j(\rho)+\varphi_j(\bar\rho)\bigr)
=\sum_{\rho\in\mathcal Z}2\operatorname{Re}\varphi_j(\rho),
\]
with multiplicities included in the sum.

The theorem to prove is the following.

> **Theorem B2.** There are finite admissible symmetric multisets
> \(\mathcal Z_+\) and \(\mathcal Z_-\) such that
> \[
> P(\mathcal Z_+)=1,\qquad P(\mathcal Z_-)=0,
> \]
> and
> \[
> O_j(\mathcal Z_+)=O_j(\mathcal Z_-)
> \quad (j=1,\ldots,m).
> \]

The supplied problem is self-contained. The proof below uses only:

1. the definitions above and additivity of finite multiset sums;
2. the Chebyshev identity \(T_j(\cos\theta)=\cos(j\theta)\) and the supplied
   recurrence
   \[
   T_{j+1}(x)=2xT_j(x)-T_{j-1}(x),\qquad T_0=1,\quad T_1=x;
   \]
3. elementary rational linear algebra and the Vandermonde determinant formula.

No assertion about the Riemann zeta function, its zeros, or RH is used.

---

## 2. Audit of the draft notation

Let
\[
L(t):=\{\tfrac12+it,\tfrac12-it\}
\]
denote one critical-line pair, with multiplicity one at each point. Let
\[
Q_T:=Q(\tfrac34,T)
=\{\tfrac34+iT,\tfrac34-iT,\tfrac14+iT,\tfrac14-iT\}.
\]

The following corrections are forced by the stated definition of \(O_j\).

### 2.1 Critical-line pair contribution

Write \(\rho_t=\tfrac12+it\). Because \(L(t)\) contains both \(\rho_t\) and
\(\bar\rho_t\),
\[
\begin{aligned}
O_j(L(t))
&=\bigl(\varphi_j(\rho_t)+\varphi_j(\bar\rho_t)\bigr)
  +\bigl(\varphi_j(\bar\rho_t)+\varphi_j(\rho_t)\bigr)\\
&=4\operatorname{Re}\varphi_j(\rho_t).
\end{aligned}
\]
Now
\[
w_t:=1-\frac1{\rho_t}=\frac{2it-1}{2it+1}
\]
has modulus one. For
\[
\theta(t)=2\arctan(2t)-\pi\in(-\pi,0)
\]
one has \(w_t=e^{-i\theta(t)}\), hence
\[
O_j(L(t))=4\bigl(1-\cos(j\theta(t))\bigr).
\]
Consequently the actual pair-contribution matrix is
\[
C_{jk}:=O_j(L(t_k))
=4\bigl(1-\cos(j\theta_k)\bigr),
\qquad \theta_k=\theta(t_k).
\tag{2.1}
\]

In the draft,
\[
2\operatorname{Re}
 \bigl(\varphi_j(\rho_t)+\varphi_j(\bar\rho_t)\bigr)
\]
was equated with \(2(1-\cos(j\theta))\). Its correct value is
\(4(1-\cos(j\theta))\). Thus the first displayed expression for the draft
matrix is the actual contribution \(C_{jk}\), whereas its last displayed
expression is smaller by a factor of two.

### 2.2 Off-line quartet contribution

The actual quartet vector is
\[
\begin{aligned}
d_j(T):=O_j(Q_T)
&=2\bigl[
  \varphi_j(\tfrac34+iT)+\varphi_j(\tfrac34-iT)
  +\varphi_j(\tfrac14+iT)+\varphi_j(\tfrac14-iT)
  \bigr]\\
&=4\operatorname{Re}\bigl[
  \varphi_j(\tfrac34+iT)+\varphi_j(\tfrac14+iT)
  \bigr].
\end{aligned}
\tag{2.2}
\]
The vector called \(\delta^{\mathrm{off}}\) in the draft includes only the
\(\operatorname{Re}\rho=3/4\) conjugate pair and omits the
\(\operatorname{Re}\rho=1/4\) pair. It therefore is not \(O_j(Q_T)\).

### 2.3 Monotonicity and range

If \(x(t)=\cos\theta(t)\), elementary trigonometry gives the rational formula
\[
x(t)=\frac{4t^2-1}{4t^2+1}.
\tag{2.3}
\]
Thus \(x(t)\in(-1,1)\), not necessarily \((-1,0)\), and
\[
x'(t)=\frac{16t}{(4t^2+1)^2}>0.
\]
Also \(\theta'(t)=4/(1+4t^2)>0\). Hence
\[
t_1<\cdots<t_m
\quad\Longrightarrow\quad
\theta_1<\cdots<\theta_m,
\quad x_1<\cdots<x_m.
\tag{2.4}
\]
The monotonic directions stated in the draft were reversed, but distinctness—the
property needed in the determinant argument—remains true.

These corrections change neither the theorem nor the core interpolation idea.
They only ensure that the linear system uses the contributions actually defined
by \(O_j\).

---

## 3. Invertibility of the corrected contribution matrix

> **Lemma 3.1.** The matrix \(C=(C_{jk})_{1\leq j,k\leq m}\) from (2.1) belongs
> to \(M_m(\mathbb Q)\) and is nonsingular.

**Proof.** Put \(x_k=\cos\theta_k\). By (2.3), every \(x_k\) is rational, and
by (2.4) the \(x_k\) are pairwise distinct. The Chebyshev identity gives
\[
C_{jk}=4\bigl(1-T_j(x_k)\bigr).
\tag{3.1}
\]
This already proves \(C_{jk}\in\mathbb Q\).

We next verify the degree and leading coefficient needed in the determinant
argument. The recurrence gives
\[
T_1(x)=x,\qquad T_2(x)=2x^2-1.
\]
Inductively, if \(j\geq2\), \(T_j\) has degree \(j\) and leading coefficient
\(2^{j-1}\): in
\[
T_{j+1}=2xT_j-T_{j-1},
\]
the first term has degree \(j+1\) and leading coefficient \(2^j\), whereas the
second has degree \(j-1\), so no cancellation of the leading term is possible.

The same recurrence evaluated at \(x=1\), with \(T_0(1)=T_1(1)=1\), proves
\(T_j(1)=1\) for every \(j\). Therefore \(1-x\) divides \(1-T_j(x)\). Define
\[
q_j(x):=\frac{1-T_j(x)}{1-x}.
\tag{3.2}
\]
For \(j=1\), \(q_1=1\). For \(j\geq2\), the numerator in (3.2) has degree
\(j\) and leading term \(-2^{j-1}x^j\), while the divisor has leading term
\(-x\). Hence
\[
\deg q_j=j-1,
\qquad \operatorname{lc}(q_j)=2^{j-1}.
\tag{3.3}
\]

Using (3.2), factor (3.1) as
\[
C_{jk}=4(1-x_k)q_j(x_k).
\]
Let \(B=(q_j(x_k))_{j,k}\). If
\[
q_j(x)=\sum_{i=1}^{j}a_{ji}x^{i-1},
\]
then the coefficient matrix \(A=(a_{ji})_{1\leq j,i\leq m}\) is **lower**
triangular, with diagonal entries \(a_{jj}=2^{j-1}\). (The draft called it
upper triangular; the determinant conclusion is unaffected.) Let
\(V_{ik}=x_k^{i-1}\). Then \(B=AV\), so
\[
\begin{aligned}
\det C
&=4^m\left(\prod_{k=1}^m(1-x_k)\right)\det A\det V\\
&=4^m\left(\prod_{k=1}^m(1-x_k)\right)
  2^{m(m-1)/2}
  \prod_{1\leq k<\ell\leq m}(x_\ell-x_k).
\end{aligned}
\tag{3.4}
\]
Here \(1-x_k>0\) and \(x_\ell-x_k>0\) for \(k<\ell\). Thus (3.4) is nonzero.
\(\square\)

---

## 4. Rationality of the quartet vector

> **Lemma 4.1.** If \(T>0\) is rational, then
> \(d(T)=(d_1(T),\ldots,d_m(T))\in\mathbb Q^m\), and \(d(T)\neq0\).

**Proof.** For rational \(T\), both
\(\tfrac34+iT\) and \(\tfrac14+iT\) belong to \(\mathbb Q(i)\). The map
\[
z\longmapsto 1-\left(1-\frac1z\right)^j
\]
uses only rational operations and integer powers, so its values at those points
belong to \(\mathbb Q(i)\). Their real parts are rational, and (2.2) gives
\(d_j(T)\in\mathbb Q\).

Moreover \(\varphi_1(\rho)=1/\rho\). Hence
\[
d_1(T)=4\left(
\frac{\tfrac34}{(\tfrac34)^2+T^2}
+\frac{\tfrac14}{(\tfrac14)^2+T^2}
\right)>0.
\tag{4.1}
\]
Thus \(d(T)\neq0\). \(\square\)

---

## 5. Exact rational solution and integer multiplicities

Fix any positive rational \(T\); for definiteness one may take \(T=1\). By
Lemmas 3.1 and 4.1, the vector
\[
\beta:=-C^{-1}d(T)
\tag{5.1}
\]
belongs to \(\mathbb Q^m\). Choose a positive integer \(R\) divisible by the
denominator of every component of \(\beta\), written in lowest terms, and put
\[
n:=R\beta\in\mathbb Z^m.
\tag{5.2}
\]
Multiplying (5.1) by \(R\) gives the exact identity
\[
Cn+R\,d(T)=0
\qquad\text{in }\mathbb Q^m.
\tag{5.3}
\]
There is no approximation in (5.3). The multiplicity data \(n_1,\ldots,n_m,R\)
are integers.

Strictly speaking, because \(C\) and \(d(T)\) are generally rational rather
than integral, (5.3) is an equality in \(\mathbb Q^m\), not literally an
equality whose displayed entries all lie in \(\mathbb Z\). If a literal integer
matrix equation is desired, take a common denominator \(D\) of all entries of
\(C\) and \(d(T)\); then
\[
(DC)n+R(Dd(T))=0
\qquad\text{in }\mathbb Z^m.
\tag{5.4}
\]
Thus the intended assertion—exact equality obtained using integer
multiplicities—is fully valid.

Since \(d(T)\neq0\) and \(C\) is invertible, \(n\neq0\). Set
\[
M:=\max_{1\leq k\leq m}|n_k|\in\mathbb Z_{\geq1}.
\tag{5.5}
\]
Define the finite multisets
\[
\mathcal Z_+
:=\bigsqcup_{k=1}^m M\,L(t_k)
\tag{5.6}
\]
and
\[
\mathcal Z_-
:=\left(\bigsqcup_{k=1}^m (M+n_k)\,L(t_k)\right)
  \sqcup R\,Q_T.
\tag{5.7}
\]
Here \(r\,S\) means \(r\) multiset copies of \(S\). Formula (5.5) ensures
\[
M+n_k\geq M-|n_k|\geq0,
\]
so every multiplicity in (5.7) is a nonnegative integer. Equivalently, if one
starts from \(\mathcal Z_+\), all requested removals are valid.

By additivity of \(O_j\), (2.1), (2.2), and (5.3),
\[
\begin{aligned}
O_j(\mathcal Z_-)-O_j(\mathcal Z_+)
&=\sum_{k=1}^m n_k O_j(L(t_k))+R O_j(Q_T)\\
&=\sum_{k=1}^m C_{jk}n_k+R d_j(T)\\
&=0
\end{aligned}
\tag{5.8}
\]
for every \(j=1,\ldots,m\). This proves the required exact observation
collision.

---

## 6. Symmetry, admissibility, and the predicates

Each pair \(L(t_k)\) lies in the open critical strip and is invariant, with
equal multiplicities, under both
\[
\rho\longmapsto\bar\rho
\quad\text{and}\quad
\rho\longmapsto1-\rho.
\]
The quartet \(Q_T\) also lies in the strip and is invariant under both maps.
The construction changes multiplicities only by whole pairs and whole quartets;
therefore the required symmetries and their multiplicities are preserved.

Both \(\mathcal Z_+\) and \(\mathcal Z_-\) are finite. They are consequently
locally finite, and
\[
\sum_{\rho\in\mathcal Z_\pm}|\rho|^{-2}<\infty.
\]
Thus both are admissible symmetric zero multisets.

Every point of \(\mathcal Z_+\) has real part \(1/2\), so
\(P(\mathcal Z_+)=1\). The multiset \(\mathcal Z_-\) contains \(R\geq1\)
copies of every point of \(Q_T\), including points with real parts \(1/4\) and
\(3/4\). Hence \(P(\mathcal Z_-)=0\).

Together with (5.8), this completes the proof of Theorem B2. \(\square\)

---

## 7. Exact sanity check for \(m=2\)

Take \(t_1=1\), \(t_2=2\), and \(T=1\). Then
\[
x_1=\frac35,
\qquad
x_2=\frac{15}{17},
\]
and the corrected contribution matrix is
\[
C=
\begin{pmatrix}
\frac85 & \frac8{17}\\[2mm]
\frac{128}{25} & \frac{512}{289}
\end{pmatrix},
\qquad
\det C=\frac{3072}{7225}\neq0.
\]
The actual quartet vector is
\[
d(1)=
\begin{pmatrix}
\frac{1216}{425}\\[2mm]
\frac{1763072}{180625}
\end{pmatrix}.
\]
Solving (5.1) gives
\[
\beta=
\begin{pmatrix}
-\frac{1426}{1275}\\[2mm]
-\frac{854}{375}
\end{pmatrix}.
\]
One may take
\[
R=6375,
\qquad
n=(-7130,-14518),
\qquad
M=14518.
\]
Then
\[
Cn+R\,d(1)=0
\]
exactly. Thus \(\mathcal Z_+\) has multiplicity \(14518\) at each of the two
critical-line pairs, while \(\mathcal Z_-\) has multiplicities \(7388\) and
\(0\) at those pairs and also contains \(6375\) copies of \(Q_1\). This is an
exact example, not a floating-point check.

For reference, the correct angle data are
\[
\theta(1)=2\arctan 2-\pi\approx-0.927295,
\qquad
\theta(2)=2\arctan 4-\pi\approx-0.489957.
\]

---

## 8. Acceptance-criteria disposition

| Item | Disposition |
|---|---|
| Step 1 | **CONFIRMED after correction.** The relevant matrix is rational and nonsingular. The draft has a factor-of-two error, reverses two monotonicity statements, gives the wrong range \((-1,0)\), and mislabels a lower-triangular coefficient matrix as upper triangular. None of these defeats the corrected determinant proof. |
| Step 2 | **CONFIRMED after correction.** The draft's quartet vector is not the observation of the stated quartet. With the actual vector \(d(T)\), clearing denominators yields integer multiplicities and the exact rational identity (5.3); (5.4) is a literal integer equation if desired. |
| Step 3 | **CONFIRMED.** The buffer \(M=\max_k|n_k|\) makes every removal valid. Symmetry is preserved because changes are made by complete symmetric pairs and quartets—not merely because the number of changes is finite. Finiteness gives admissibility. |
| Overall | **CONFIRMED. Theorem B2 holds as stated.** The original sketch must not be accepted verbatim, but the corrected proof above establishes the theorem without strengthening its hypotheses. |

---

## 9. Scope of the result

The argument constructs two artificial finite symmetric multisets with identical
first \(m\) Li-type observations and different critical-line predicates. It does
not assert that either multiset is the zero multiset of a zeta or \(L\)-function,
and it uses no information about Riemann zeros or RH.
