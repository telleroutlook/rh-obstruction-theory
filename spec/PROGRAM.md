# Research Program v2.0 — Structural and Finite-Information Obstructions for RH-Equivalent Frameworks

**Working title:** *What Finite RH Certificates Cannot See: Indistinguishability, Spectral Invariants, and Convergence Obligations*  
**Document type:** final research plan  
**Author:** Lin Tao  
**Version:** 2.0  
**Date:** 2026-08-10  
**Status:** research program, not a proof or disproof of the Riemann Hypothesis

## Honesty banner

This program does **not** claim that the Riemann Hypothesis (RH) is inherently difficult, independent of a formal theory, or unreachable by broad families of mathematics. It seeks narrower and genuinely provable results of two kinds:

1. **information obstructions:** a precisely defined method sees only an observation map \(O\), while two admissible objects with different zero-location behavior have the same observation;
2. **structural obstructions:** every candidate in a precisely defined operator or certificate class has an invariant incompatible with the invariant required by an exact RH realization.

A theorem is called a barrier only when the method class, ambient object class, observation map, target predicate, and escape route are all explicit. An RH-equivalent criterion is **not** by itself a barrier: an unconditional proof of that criterion would simply prove RH.

The minimum success criterion is one non-vacuous no-go theorem for one natural, externally recognizable class. A collection of failed computations, a representation-dependent margin collapse, or a reformulation equivalent to RH does not meet that criterion.

---

## 1. Executive decision

The program will concentrate on three theorem families, in this order:

1. **finite-observable indistinguishability:** finite moment, finite Li-type, finite Weil-test, or finite Euler-factor information cannot determine global zero support in a stated ambient class;
2. **compact-convergence obligations for spectral approximants:** finite-stage self-adjointness, real-rootedness, or agreement with finitely many zeta zeros does not imply convergence to Ξ; identify the additional normal-family and tail estimates that would make the limit valid;
3. **spectral-asymptotic exclusions:** classical compact elliptic or other explicitly delimited operator classes cannot realize the zeta spectrum because their Weyl/heat-trace invariants are incompatible with the Riemann–von Mangoldt law.

The proposed universal **\(c_a\)- or \(c_L\)-margin barrier is not a primary theorem target**. A scalar shift appearing in one basis or Schur decomposition is not a method-class invariant. It remains useful as a diagnostic inside one frozen certificate architecture, but it can support a barrier only after the norm, congruence class, admissible preconditioners, and certificate proof system are fixed.

The recent operator-theoretic literature also changes the natural point of attack. The localized Weil form now has a clean representation-invariant quantity—its lowest Rayleigh quotient—and recent work constructs finite or local real-zero objects. The decisive unclosed bridge is global convergence with controlled tails. The program therefore treats **finite evidence versus certified compact convergence** as a central boundary.

---

## 2. Mathematical baseline

### 2.1 Completed zeta and the real-zero formulation

Set

\[
\xi(s)=\frac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
\qquad
\Xi(z)=\xi\!\left(\frac12+iz\right).
\]

Then Ξ is an even real entire function of order one. RH is equivalent to all zeros of Ξ being real.

The positive ordinates of the nontrivial zeros have counting function

\[
N_\zeta(T)
=\frac{T}{2\pi}\log\frac{T}{2\pi}
-\frac{T}{2\pi}+O(\log T).
\]

Any exact spectral realization must reproduce this \(T\log T\) leading law, not merely a finite prefix of ordinates.

### 2.2 Weil positivity and localization

For \(v\in C_c^\infty(\mathbb R)\), let

\[
Q_W(v_1,v_2)=W(v_1*\widetilde v_2),
\qquad
Q_W(v)=Q_W(v,v),
\]

where \(W\) is the Weil functional and \(\widetilde v(x)=\overline{v(-x)}\). Weil's criterion states

\[
\mathrm{RH}
\quad\Longleftrightarrow\quad
Q_W(v)\ge 0\quad\text{for every }v\in C_c^\infty(\mathbb R).
\]

For a support radius \(a>0\), let \(Q_W^a\) be the restriction to functions supported in \((-a,a)\). Because \(v*\widetilde v\) is supported in \((-2a,2a)\), its prime-power term involves only \(n\le e^{2a}\). Thus each localized form uses finite prime data, while the assertion for all \(a\) remains global.

The correct representation-invariant lower margin is

\[
\lambda(a)=
\inf_{0\ne v\in D(Q_W^a)}
\frac{Q_W^a(v)}{\lVert v\rVert_{L^2(-a,a)}^2}.
\]

Recent work of Suzuki constructs the associated lower-bounded self-adjoint operator \(A_a\), proves that its spectrum is discrete with \(+\infty\) as its only accumulation point (so the largest lower bound \(\lambda(a)\) is an eigenvalue), proves that \(\lambda(a)\) is **continuous in \(a\)** (Theorem 1.3), and proves that for sufficiently small \(a>0\) the lowest eigenvalue is **positive and simple** with an even eigenfunction, satisfying the asymptotic \(\lambda(a)=\log\frac1a+\mu_1-\log(2\pi)+\psi(2)-1+O(a)\), \(\mu_1>0\), as \(a\to0^+\) (Theorem 1.4). This is now the baseline for any local-Weil argument; a basis-dependent pivot or Schur complement is secondary evidence, not the invariant itself. Note that the same \(\log(1/a)\) scale that appeared as an apparent negative shift \(-c_L\) in an unnormalized Schur decomposition here enters the representation-invariant quantity with the **opposite role** — it is the leading positive term making \(\lambda(a)>0\) for small \(a\). This is direct evidence that the \(c_L\)-dominance was a representation artifact (see §11.3). See [Suzuki, *Weil's quadratic form via the screw function*](https://arxiv.org/abs/2606.09096) (Theorems 1.3–1.4).

### 2.3 The modern finite/local spectral picture

Three recent developments must be built into the program:

- Connes and van Suijlekom prove real-zero results for Fourier transforms of extremal eigenfunctions associated with lower-bounded convolution-type quadratic forms, including finite truncations; see [Communications in Mathematical Physics 406 (2025), 312](https://doi.org/10.1007/s00220-025-05493-1).
- Connes, Consani, and Moscovici construct self-adjoint finite-parameter operators \(\dln\) from truncated Weil data, with \(\det_{\mathrm{reg}}(\dln-z)=-i\,\lambda^{-iz}\widehat\xi(z)\) (an **entire** target, \(\widehat\xi\) = Fourier transform of \(\xi\), all zeros real and equal to the operator spectrum), and identify convergence of the **suitably normalized** determinants toward the Riemann \(\Xi\) function as the decisive open step; see [*Zeta Spectral Triples*](https://arxiv.org/abs/2511.22755). Caution for Paper C: the phase factor \(\lambda^{-iz}\) preserves zeros but does **not** preserve a locally uniform limit, so "suitably normalized" is load-bearing — this is the CCM-side normalization trap, distinct from the meromorphic \(\xi/\xi'\) target of the Suzuki route.
- Suzuki constructs unconditional finite-interval characteristic functions \(W(a,\theta;z)\) that are entire with **all zeros real** (Theorem 1.5), and proves (Corollary 6) that RH follows **if** one can choose \(\theta=\theta(a)\) and a compensating factor \(\phi(a,z)\) so that \(e^{\phi(a,z)}W(a,\theta;z)\to z^2\,\xi(1/2-iz)/\xi'(1/2-iz)\) uniformly on every compact subset of \(\mathbb C\); see [arXiv:2606.09096](https://arxiv.org/abs/2606.09096). Note the target limit is a **meromorphic** logarithmic-derivative expression whose poles sit at the zeros — not \(\Xi\) itself.

These results show exactly why finite real-rootedness is not enough. If nonzero entire functions with only real zeros converge locally uniformly, Hurwitz-type arguments preserve real zero location in the limit — **but this transfer is not automatic for the Suzuki normalization**, whose target \(z^2\xi/\xi'\) is meromorphic (poles at the zeros), so a pole/residue version of the limiting argument is required rather than the entire-function Hurwitz theorem (see §10.E.3). The missing content is therefore a **certified convergence modulus, normal-family bound, normalization, and tail control** identifying the limit with the specified object — \(z^2\xi(1/2-iz)/\xi'(1/2-iz)\) in Suzuki's Corollary 6, or the normalized regularized determinant in the Connes–Consani–Moscovici construction (a distinct normalization; the two must not be conflated).

### 2.4 Quantitative equivalents as precedent, not barriers

The Nyman–Beurling/Báez-Duarte program and Li's criterion are useful precedents because they separate a true equivalence from quantitative approximation difficulty:

- finite-dimensional Nyman–Beurling approximation has known lower bounds of order \(1/\sqrt{\log n}\), sharpened using zeta zeros; see [Burnol](https://arxiv.org/abs/math/0103058) and [Báez-Duarte](https://arxiv.org/abs/math/0205003);
- Li positivity is equivalent to RH only when required for **all** indices, and off-line zeros cause a different large-index asymptotic regime; see [Voros](https://arxiv.org/abs/math/0506326).

These works do not show that the criteria cannot prove RH. They show how global zero information reappears as an infinite-order or asymptotic obligation. This is the model for the present program.

---

## 3. What counts as a barrier theorem

### 3.1 Observation-factorization barrier

Let:

- \(\mathfrak X\) be an explicitly defined class of admissible zero data, entire functions, generalized zeta functions, or operators;
- \(P:\mathfrak X\to\{0,1\}\) be the target property, such as critical-line support;
- \(O_r:\mathfrak X\to\mathfrak Y_r\) be the information visible at resource level \(r\);
- a method \(M\) be **\(O_r\)-local** if \(M=\phi\circ O_r\) for some decision or certificate rule \(\phi\).

An exact pair \(x_+,x_-\in\mathfrak X\) satisfying

\[
O_r(x_+)=O_r(x_-),
\qquad
P(x_+)\ne P(x_-)
\]

proves that no \(O_r\)-local rule decides \(P\) correctly on all of \(\mathfrak X\).

For one-sided certificate methods, the analogous theorem requires that both objects satisfy every acceptance condition available to the method while only one has \(P=1\).

This schema is representation-independent once \(O_r\) is fixed. It also makes the theorem's scope visible: the conclusion applies to the ambient class \(\mathfrak X\), not automatically to ζ.

### 3.2 Structural-invariant barrier

Let \(\mathcal C\) be a candidate class and let \(J\) be an invariant preserved by the allowed equivalences and perturbations. If every \(C\in\mathcal C\) satisfies \(J(C)\in S\), while an exact RH realization must satisfy \(J_\zeta\notin S\), then no \(C\in\mathcal C\) is an exact realization.

Examples of acceptable invariants include:

- eigenvalue counting asymptotics;
- heat-trace singularity class;
- order and type of a spectral determinant;
- deficiency indices;
- rank growth or proof complexity inside a frozen certificate system.

### 3.3 Statements that are not barriers

The following will not be labeled barriers:

1. **RH-equivalence:** \(C\Longleftrightarrow\mathrm{RH}\) locates the remaining difficulty but does not prove impossibility.
2. **Finite failure of one sufficient inequality:** this excludes that inequality at those parameters, not all methods using the same mathematical object.
3. **A margin tending to zero:** strictly positive quantities can tend to zero and remain provable at every finite stage.
4. **A synthetic off-line zero configuration outside the declared ambient class:** it says nothing about methods that use the missing axioms.
5. **No result found in a literature search:** negative search is a novelty signal, not a theorem.
6. **Machine-verified finite arithmetic without a proved analytic bridge:** the computation certifies only the finite statement replayed by the checker.

---

## 4. Foundational design rules

### Rule 1 — Separate criteria from proof methods

Every proposed theorem must state whether it concerns:

- a mathematical criterion equivalent to RH;
- an algorithm for checking finite instances;
- a formal certificate system;
- or an entire family of analytic proofs.

Only the last three can be limited by a method barrier, and only after the method is formally specified.

### Rule 2 — Use invariant margins

Raw pivots, matrix eigenvalues in an unnormalized basis, Schur residuals, and a displayed scalar shift are not invariant under rescaling or congruence. The default margin is a generalized Rayleigh quotient relative to a fixed Hilbert norm or Gram matrix. Any alternative must prove its invariance under every transformation allowed in the method class.

### Rule 3 — State the adversarial universe

An off-line quartet preserving conjugation and \(s\mapsto1-s\) symmetry does not automatically define an \(L\)-function. Ambient classes will be graded:

- symmetric locally finite zero multisets;
- order-one entire functions with Ξ-like symmetries and counting law;
- generalized Dirichlet/Euler products;
- extended Selberg-class or automorphic \(L\)-functions;
- the single function ζ.

A theorem at one level may not be advertised at a stronger level.

### Rule 4 — Distinguish fixed finite order from an unbounded hierarchy

Showing that no fixed \(K\) works does not exclude a method with \(K\to\infty\), an adaptive stopping rule, or a theorem supplying a uniform tail bound. Every result must specify whether the resource is fixed, bounded by a function, or unbounded.

### Rule 5 — Require an escape route

A useful barrier identifies what a successful approach must add. Examples include flatness in a moment problem, a global Euler/functional-equation coupling, a nonclassical logarithmic symbol, or a certified normal-family bound.

### Rule 6 — Keep logical independence out of scope

The arithmetical form of RH neither supplies a method barrier nor rules out formal independence. No claim about ZFC, Peano arithmetic, or an undefined notion of intrinsic difficulty will be made without a separate formal-logic project.

---

## 5. Research questions

**RQ1. Finite observables.** For which natural finite-dimensional spaces of test functions can critical-line support and off-line support produce identical observations?

**RQ2. Exact versus approximate indistinguishability.** Can strict finite positivity be upgraded to exact equality of finite moments or Weil observables while retaining Ξ-like symmetry, order, and counting law?

**RQ3. Euler tails.** How much zero-location freedom remains after finitely many Euler factors are frozen in a generalized Euler-product class?

**RQ4. Spectral invariants.** Which natural operator classes are excluded by \(T\log T\) counting or the corresponding \(t^{-1}\log(1/t)\) heat-trace behavior?

**RQ5. Convergence evidence.** Which finite spectral or determinant checks fail to imply locally uniform convergence, and what minimal checkable envelope would make convergence rigorous?

**RQ6. Restricted Weil certificates.** After freezing a norm and proof system, can one prove a rank, degree, or condition-number lower bound for split-residual/Schur certificates as \(a\to\infty\)?

---

## 6. Work package A — Evidence stabilization and literature closure

### A.1 Purpose

No private or machine-verified result will enter a published theorem as an established premise until its statement, analytic proof, normalization, and computational witness are independently inspectable.

### A.2 Two-axis evidence ledger

Each claim receives both a mathematical and a computational status.

| Axis | Status |
|---|---|
| Mathematical | `DEFINITION`, `CONJECTURE`, `PROOF-DRAFT`, `INDEPENDENTLY-CHECKED`, `REFEREED` |
| Computational | `NONE`, `EXPLORATORY`, `REPRODUCIBLE`, `INDEPENDENT-CHECKER`, `FORMALIZED` |

A repository deposit or DOI is archival publication, not peer review. “Lean-ready” is not “Lean-formalized.” A finite Arb certificate does not independently validate the analytic theorem that produced the finite matrix.

### A.3 Mandatory audit of existing inputs

For FP-0.35, the claimed second-window termination theorem, and P19–P22:

1. freeze the exact theorem statement, test space, norm, parameter convention, and quantifiers;
2. translate all local-Weil notation to the \(a\), \(Q_W^a\), and \(\lambda(a)\) baseline used in the current literature;
3. separate analytic reductions from finite interval computations;
4. replay every finite certificate from raw prime-power data with an independent checker;
5. verify public record metadata and citation status directly;
6. obtain an external mathematical review before using any result as a premise.

Until this gate closes, these results are **conditional case studies**. They may motivate a conjecture but not support a universal theorem.

### A.4 Deliverables and gate

- `REFERENCE_BASELINE.md`: exact definitions and conventions;
- `CLAIM_LEDGER.yaml`: two-axis status for every imported claim;
- `LITERATURE_MATRIX.md`: theorem, scope, prior art, and unresolved delta;
- independent replay reports for finite certificates.

**Gate A:** every premise used in Work Packages B–E is either refereed/publicly checkable or restated as an explicit assumption.

---

## 7. Work package B — Finite-observable indistinguishability

This is the primary theorem program.

### B.1 Ambient zero-data class

Begin with a class \(\mathfrak X_{\mathrm{sym}}\) of locally finite multisets \(\mathcal Z\) in the critical strip satisfying:

1. invariance under conjugation and \(\rho\mapsto1-\rho\);
2. a stated convergence-exponent bound sufficient for all observables;
3. a Riemann–von Mangoldt-type counting law, if needed;
4. optional agreement with a prescribed finite prefix of on-line zeros.

Define

\[
P(\mathcal Z)=1
\quad\Longleftrightarrow\quad
\Re\rho=\frac12\text{ for every }\rho\in\mathcal Z.
\]

For a finite test family \(\Phi=(\phi_1,\dots,\phi_m)\), define a regularized observation map

\[
O_\Phi(\mathcal Z)
=\left(\sum_{\rho\in\mathcal Z}^{*}\phi_j(\rho)\right)_{j=1}^{m}.
\]

The summation convention and admissible test decay must be part of the theorem.

### B.2 The theorem ladder

#### B1 — Strict finite-inequality non-discrimination

For every fixed finite family of strict continuous positivity tests, construct a sufficiently high symmetric off-line quartet whose contribution is small enough that all tests retain their sign.

Applications:

- the first \(K\) Li inequalities;
- a fixed finite family of Weil test functions;
- fixed-order Hausdorff or Stieltjes differences.

This theorem is intentionally modest: it excludes only fixed finite evidence.

#### B2 — Exact finite-observation collision

Construct \(\mathcal Z_+,\mathcal Z_-\in\mathfrak X_{\mathrm{sym}}\) such that

\[
O_\Phi(\mathcal Z_+)=O_\Phi(\mathcal Z_-),
\qquad
P(\mathcal Z_+)=1,
\qquad
P(\mathcal Z_-)=0.
\]

The proposed proof architecture is:

1. insert one high off-line symmetric quartet;
2. use finitely many high on-line atoms as compensating degrees of freedom;
3. solve the finite nonlinear moment equations by a full-rank Jacobian/implicit-function argument;
4. preserve local finiteness and the counting law because only finitely many high atoms move;
5. convert the multiset to a canonical product and verify order and symmetry.

The full-rank condition is a theorem hypothesis, not an informal genericity claim.

#### B3 — Truncated moment support theorem

Translate B2 into the language of truncated moment cones. The expected statement is that an interior truncated moment vector generally has multiple representing measures with different supports; support recovery becomes finite only after an escape condition such as flat extension, finite atomicity with a rank certificate, or an a priori separation hypothesis.

The proof should build on standard truncated-moment theory rather than reprove it. Relevant anchors are [Curto–Fialkow's flat-extension theory](https://doi.org/10.1090/memo/0648) and [Bayer–Teichmann's proof of Tchakaloff's theorem](https://arxiv.org/abs/math/0502473).

#### B4 — Ξ-like entire-function realization

Realize the two data sets as order-one entire functions \(F_+,F_-\) satisfying

\[
F(s)=F(1-s),
\qquad
F(\overline s)=\overline{F(s)},
\]

with identical declared finite observations and different zero support. Fix the Hadamard factors and normalization explicitly; otherwise an arbitrary exponential factor can trivialize the collision.

### B.3 RH-specific application boundary

The conclusions at B1–B4 apply to the declared symmetric-entire ambient class. They do **not** show that finite observations are useless when combined with the exact Euler product, exact gamma factor, analytic continuation, and coefficient arithmetic of ζ. The publishable conclusion must say precisely which additional structure escapes the theorem.

### B.4 Fail-fast tests

- If the off-line construction cannot satisfy the stated convergence or counting law, narrow the theorem before computation.
- If exact collision requires signed or nonintegral zero multiplicities, retain only the inequality theorem and do not market exact indistinguishability.
- If the result is an immediate corollary of a standard moment theorem with no RH-specific translation, publish it only as a lemma supporting a stronger application.
- If an application uses a fixed \(K\), the title and abstract must not imply failure of the \(K\to\infty\) hierarchy.

### B.5 Deliverable

**Paper A:** *Finite Observables Do Not Determine Critical-Line Support* — an abstract collision theorem, canonical-product realization, and carefully scoped applications to Li/Weil/moment certificates.

---

## 8. Work package C — Prime-tail freedom and external comparison objects

### C.1 Finite Euler-factor barrier

Let \(P_0\) be a prime cutoff. Consider Helson zeta functions

\[
\zeta_\chi(s)=\prod_p(1-\chi(p)p^{-s})^{-1},
\qquad |\chi(p)|=1.
\]

Andersson proves strong prescribed-zero and prescribed-pole results for meromorphically continued Helson zeta functions; see [*Mittag-Leffler type theorems for Helson zeta-functions*](https://arxiv.org/abs/2408.15713).

The target proposition is:

> For every finite prime cutoff \(P_0\) and suitable prescribed off-line zero set in the continuation region, there is a Helson zeta function with \(\chi(p)=1\) for all \(p\le P_0\) and with the prescribed zero set.

The intended reduction is to apply the prescribed-zero theorem and then modify finitely many Euler factors. Because a finite change contributes an explicitly controlled meromorphic factor whose zeros and poles lie on a known boundary, it should not disturb the prescribed interior zero set. Every domain and boundary exception must be checked in the proof.

If established, this gives a clean statement: **no rule depending only on finitely many Euler factors can force RH-like zero location across the Helson class.** It does not apply to the Selberg class or to ζ without an additional transfer theorem.

### C.2 Functional equation alone

Davenport–Heilbronn-type functions demonstrate that a Riemann-type functional equation without an Euler product does not force critical-line zeros. This is a comparison example, not half of a combined countermodel.

The finite-Euler and functional-equation examples must remain logically separate. One object lacking a functional equation and another lacking an Euler product do not prove that the union of both axiom sets permits off-line zeros.

### C.3 Aspirational strengthening

Investigate whether a natural generalized-prime or extended \(L\)-function class admits both:

1. a zeta-like functional equation and growth law;
2. arbitrary agreement with a finite initial segment of Euler data;
3. rigorously established off-line zeros.

This is a genuine research problem. Failure to construct such an object is not evidence that none exists.

### C.4 Deliverable and novelty gate

The finite-Euler proposition is standalone only if it adds a nontrivial fixed-local-factor refinement to existing prescribed-zero theorems. Otherwise it becomes a supporting section of Paper A.

---

## 9. Work package D — Spectral-asymptotic no-go theorems

### D.1 Spectral realization contract

A Hilbert–Pólya candidate is non-circular only if it supplies all of the following:

1. a Hilbert space and densely defined operator constructed without importing zeta zeros;
2. self-adjointness proved from the construction;
3. compact resolvent or a precisely defined regularized spectral object;
4. an exact trace, determinant, or characteristic identity linking the spectrum to ξ;
5. the required multiplicities and normalization.

Defining a diagonal self-adjoint operator from the known ordinates is excluded by item 1 and provides no RH content.

### D.2 Classical compact elliptic class

Let \(\mathcal C_{\mathrm{ell}}\) consist of classical positive elliptic differential or pseudodifferential operators of order \(m>0\) on compact \(d\)-dimensional smooth manifolds, with standard elliptic boundary conditions where applicable, together with a declared class of perturbations preserving the leading Weyl law.

For \(H\in\mathcal C_{\mathrm{ell}}\),

\[
N_H(T)\sim C_H T^{d/m}.
\]

No power law equals

\[
\frac{T}{2\pi}\log\frac{T}{2\pi}-\frac{T}{2\pi}+O(\log T).
\]

Equivalently, the zeta-ordinate heat trace has a \(t^{-1}\log(1/t)\)-type leading singularity, whereas the classical compact elliptic Seeley–DeWitt class has a pure polyhomogeneous power expansion. This yields a structural exclusion once the exact eigenvalue map and perturbation class are fixed.

Endres and Steiner already prove a specific no-go theorem for Berry–Keating realizations on compact quantum graphs by comparing spectral type and Weyl asymptotics; see [J. Phys. A 43 (2010), 095204](https://doi.org/10.1088/1751-8113/43/9/095204). This is the closest established model for the intended style of theorem.

### D.3 Extensions worth testing

- finite direct sums of compact elliptic systems;
- bounded or relatively compact perturbations preserving the leading counting law;
- compact quantum graphs with local energy-independent vertex conditions;
- fixed polynomial transforms of classical elliptic spectra;
- spectral determinants whose order/type is forced by a classical heat expansion.

Each extension needs its own preservation lemma. “Compact perturbation” must not be used without the hypotheses under which the counting asymptotic is stable.

### D.4 Explicit escape class

The theorem must state that it does not exclude:

- noncompact or infinite-volume systems with renormalized traces;
- infinite quantum graphs;
- nonlocal or log-polyhomogeneous symbols;
- energy-dependent boundary conditions;
- Krein/Pontryagin-space or absorption-spectrum realizations;
- arithmetic/noncommutative geometries outside the classical elliptic calculus.

An escape example with the correct \(T\log T\) leading order should be included to show the barrier is not a restatement of the target.

### D.5 Novelty gate and deliverable

The raw Weyl mismatch is close to a standard corollary. Before claiming a new paper, complete a theorem-by-theorem prior-art audit. A paper is justified only if it supplies a materially broader, sharply defined invariant class or an exact determinant obstruction not already in the literature.

**Paper B, conditional on novelty:** *Spectral-Asymptotic Exclusions for Classical Hilbert–Pólya Candidates*.

---

## 10. Work package E — Finite spectral matching versus compact convergence

This is the second primary theorem program and the most direct response to current Weil-form spectral research.

### E.1 Finite evidence record

For an approximating entire function \(F_N\) or self-adjoint operator \(H_N\), define a finite evidence record containing some combination of:

- self-adjointness of \(H_N\);
- real-rootedness of \(F_N\);
- agreement of the first \(k_N\) zeros with verified zeta ordinates;
- agreement of finitely many Taylor coefficients, traces, or moments;
- a finite-dimensional determinant identity;
- interval-certified residuals at finitely many sample points.

The record contains no conclusion about an infinite limit unless it includes a proved tail envelope.

### E.2 Negative theorem target

Prove that the selected finite evidence record does not imply locally uniform convergence to the declared limit object (Ξ, the CCM normalized determinant \(\to\Xi\), or the Suzuki meromorphic target \(z^2\xi/\xi'\) — fix one normalization per instance; see §2.3). The counterexample sequence should:

1. satisfy every finite-stage real-zero and matching condition in the class;
2. retain the declared normalization at a base point;
3. fail to converge locally uniformly, or converge to a different allowed limit;
4. expose exactly which uncontrolled tail or growth parameter causes failure.

The theorem must be stronger than the slogan “finite numerics do not prove an infinite theorem.” It should quantify the invisible degrees of freedom in the canonical product or spectral tail.

### E.3 Positive escape theorem

Pair the obstruction with a sufficient convergence package. A candidate package is:

1. **normalization:** \(F_N(z_0)\) and any exponential Hadamard factor are fixed;
2. **local boundedness:** for every \(R\), an explicit \(M_R\) satisfies \(\sup_N\sup_{|z|\le R}|F_N(z)|\le M_R\);
3. **identification data:** convergence on a set with a finite accumulation point, or convergence of a full Taylor jet with a summable uniform tail bound;
4. **nonzero limit:** a certified lower bound at one point;
5. **effective modulus:** computable \(N(R,\varepsilon)\) for uniform error on \(|z|\le R\).

Montel/Vitali-type compactness identifies the limit. For an **entire** target, Hurwitz transfers real-zero location; for the **meromorphic** Suzuki target \(z^2\xi/\xi'\) (poles at the zeros), the transfer must be recast — e.g. as convergence of the reciprocal \(1/W\) toward \(\xi'/(z^2\xi)\), or as a Rouché/argument-principle count on contours avoiding the poles, so that real poles of the limit correspond to real zeros of \(\xi\). This pole/residue step is a genuine technical obligation of the Suzuki route, not a formality. The theorem should be stated in the exact normalization used by the Connes–Consani–Moscovici determinant or the Suzuki characteristic function, keeping the two normalizations separate.

### E.4 Application targets

1. **CCM/CvS truncations:** list the precise determinant normalization and the missing uniform tail bound.
2. **Suzuki \(W(a,\theta;z)\):** the precise target is Corollary 6 — the uniform-on-compacts limit \(e^{\phi(a,z)}W(a,\theta;z)\to z^2\xi(1/2-iz)/\xi'(1/2-iz)\), together with the admissible choice of \(\theta=\theta(a)\) and the compensating factor \(\phi(a,z)\). Translate this into explicit estimates on the deficiency vectors \(v_\pm(a,\cdot)\) of \(\mathscr D_a^\ast\) and the Fredholm/self-adjoint-extension data, and specify the pole/residue transfer of §E.3.
3. **Any internal real-zero approximants:** determine whether their evidence controls a normal family or only a finite spectral window.

The output is useful even if no negative theorem is new: it becomes a referee-grade checklist specifying the exact analytic obligation that converts impressive finite agreement into RH.

### E.5 Deliverable

**Paper C:** *Real-Rooted Approximants and the Missing Compactness Theorem in Spectral Approaches to RH* — one finite-evidence counterexample theorem and one explicit sufficient convergence criterion.

---

## 11. Work package F — Restricted local-Weil certificate complexity

This package retains the useful part of the finite-window Schur work without promoting a coordinate artifact to a universal barrier.

### F.1 Freeze a certificate proof system

For each \((a,N)\), specify:

- the Galerkin subspace and Gram matrix \(G_{a,N}\);
- the exact matrix \(M_{a,N}\) representing \(Q_W^a\);
- the allowed basis changes and preconditioners;
- the block split and permitted residual bounds;
- the maximum residual rank/order \(r\);
- the accepted proof objects and checker semantics.

Define a certificate system \(\mathsf P_{r,N}\) and an invariant target

\[
M_{a,N}\succeq \delta G_{a,N}.
\]

Define certificate complexity κ as the minimum rank, degree, block depth, or bit complexity required by this frozen system.

### F.2 Admissible theorem targets

- a lower bound \(\kappa(a,\delta)\ge g(a,\delta)\);
- an explicit family of test vectors defeating every certificate of rank \(r\le r_0(a)\);
- a proof that one cone of sufficient decompositions is strictly smaller than the PSD cone by a quantitative separation;
- a conditioning lower bound showing why a specified interval scheme requires growing precision.

These are proof-system or numerical-analysis theorems. They do not say that \(Q_W^a\) is nonpositive or that other proof methods fail.

### F.3 Conditions for using the scalar-shift mechanism

A decomposition containing a term \(-c_a I\) may be used only after proving:

1. the exact identity in the standard \(Q_W^a\) normalization;
2. invariance of the claimed obstruction under every allowed congruence and preconditioner;
3. an upper bound on the compensating positive operator in the same norm;
4. a conclusion stronger than “the positive margin tends to zero”;
5. consistency with the representation-invariant lowest eigenvalue \(\lambda(a)\).

If a change of representation reallocates or removes the apparent \(c_a\) dominance, the universal conjecture is abandoned and the observation remains a case-study diagnosis.

**Documented precedent that this reallocation actually occurs.** Suzuki's Theorem 1.4 gives \(\lambda(a)=\log\frac1a+\text{const}+O(a)\) as \(a\to0^+\): in the representation-invariant lowest eigenvalue, the \(\log(1/a)\) scale is the leading term making \(\lambda(a)>0\), i.e. it *carries* small-\(a\) positivity. The same \(\log\) scale, appearing as \(-c_a I\) in an unnormalized Schur decomposition, was read as *eroding* the margin. Same scale, opposite sign of effect under a change of representation — a concrete instance of exactly the artifact condition 5 guards against. Any \(-c_a I\) argument must therefore reconcile with this \(\lambda(a)\) asymptotic before it can be promoted beyond a frozen-system diagnosis.

### F.4 Deliverable

**Paper D, only after the invariance gate:** *Lower Bounds for a Restricted Schur-Certificate System for Local Weil Positivity*.

---

## 12. Verification architecture

### 12.1 Trusted and untrusted layers

1. **Discovery layer:** may use floating point, zero tables, heuristic fitting, and symbolic experimentation. It produces conjectures only.
2. **Analytic layer:** contains human-readable theorem statements and proofs. Every infinite-to-finite reduction lives here.
3. **Certificate generator:** may be untrusted and may fail.
4. **Independent checker:** reconstructs finite claims from raw data using exact or outward-rounded arithmetic.
5. **Governance layer:** derives status from dependencies and checker output; it cannot elevate a computational certificate above the analytic theorem on which its interpretation depends.

### 12.2 Required proof artifacts

Every theorem directory contains:

- `statement.md` with all quantifiers and definitions;
- `dependencies.yaml` with evidence levels;
- `proof.md` separating analytic and finite steps;
- `witness/` with raw data, not producer summaries;
- `checker/` with an independent replay path;
- `limitations.md` stating the exact non-conclusions;
- `novelty.md` mapping the theorem against prior art.

### 12.3 Proofctl gates

- no self-reported `PASS`;
- no zero tables in construction or proof layers unless the theorem explicitly concerns verified finite zeros;
- no theorem status from a numerical fit;
- certificate schema version pinned to checker version;
- source and witness hashes included;
- mutation tests for every rejection condition;
- a failed or missing analytic dependency forces downstream status to `BLOCKED`.

---

## 13. Milestones and decision gates

| Phase | Months | Deliverable | Hard gate |
|---|---:|---|---|
| M0 — Baseline | 0–2 | Work Package A; source dossier; normalized Weil definitions; evidence ledger | no private result used as established without inspection |
| M1 — Abstract collision | 2–4 | B1 strict-inequality theorem and prototype B2 exact collision | explicit admissible on/off-line pair; no RH assumption |
| M2 — Entire/moment application | 4–6 | B3–B4 and Paper A draft | canonical product, symmetry, convergence, and scope all checked |
| M3 — Convergence boundary | 5–8 | finite-evidence counterexample plus positive compactness criterion | exact match to one modern spectral normalization |
| M4 — External models | 7–9 | finite-Euler-factor proposition or supporting section | fixed local factors proved, not asserted |
| M5 — Spectral invariants | 8–10 | prior-art-complete elliptic/graph no-go theorem or survey note | material novelty beyond known Weyl mismatch |
| M6 — Restricted certificates | 9–12 | frozen proof system and go/no-go result for Paper D | representation-invariance and non-vacuity gates pass |
| M7 — Synthesis | after two theorem papers | limited unifying principle | no universal “all RH methods” language |

The work is stopped or narrowed at each hard gate. A clean negative novelty result, a failed exact-collision construction, or proof that a proposed class is vacuous is recorded but not relabeled as success.

---

## 14. Acceptance tests for every claimed barrier

### 14.1 Formal tests

- **Class test:** membership in the method/candidate class is mathematically checkable.
- **Non-vacuity test:** at least one serious published construction lies in the class.
- **Target test:** the two adversarial objects genuinely have different target truth values.
- **Observation test:** equality of observations is exact, not numerical coincidence.
- **Invariant test:** the obstruction survives all equivalences allowed by the class.
- **No-RH test:** neither RH nor a known RH-equivalent statement appears among the hypotheses.
- **Escape test:** at least one explicit route outside the class is identified.
- **Scope test:** the conclusion names the ambient class and resource bound.

### 14.2 Computational tests

- exact rational or interval replay where applicable;
- independent reconstruction from raw prime-power or moment data;
- precision escalation and conditioning report;
- adversarial mutation of every witness field;
- deterministic offline checker;
- cross-implementation agreement for at least one nontrivial instance.

### 14.3 Publication tests

- theorem statement readable without repository access;
- all private results either reproduced or assumptions;
- closest prior theorem stated explicitly;
- counterexamples and escape conditions included;
- title and abstract do not imply progress toward proving RH;
- archive deposit, code verification, independent review, and peer review are labeled separately.

---

## 15. Risk register

| Risk | Failure mode | Response |
|---|---|---|
| Definitional artificiality | class is tailored to one failed script | require multiple natural members or downgrade to a case study |
| Adversary too weak | off-line object lacks structure used by serious RH methods | grade the ambient class and state the missing axiom as the escape route |
| Fixed-order overclaim | theorem excludes only one \(K\) but is presented as global | quantify resources in theorem title and abstract |
| Representation dependence | margin collapse disappears after preconditioning | use generalized Rayleigh/invariant complexity or abandon claim |
| Bottoming out | proof requires controlling all zeta zeros | narrow to constructive collision/invariant mismatch; mark wider claim open |
| Prior art saturation | theorem is standard moment or Weyl theory | require a new RH-specific realization or publish only a reference note |
| Verification category error | finite checker is treated as analytic proof | dependency gate prevents promotion |
| Modern literature bypass | project attacks a gap already closed in 2025–2026 | baseline review updated before each paper freeze |
| No effective escape | barrier is true but uninformative | pair every negative theorem with a sufficient condition outside the class |
| Meromorphic-target transfer (Paper C) | the Suzuki limit target \(z^2\xi/\xi'\) has poles at the zeros, so entire-function Hurwitz does not transfer real-zero location | recast as reciprocal/argument-principle count on pole-avoiding contours (§10.E.3); if the pole/residue step cannot be closed, restrict Paper C's escape theorem to the CCM entire-determinant normalization only |

---

## 16. Expected paper portfolio

### Paper A — primary, highest probability

**Finite Observables Do Not Determine Critical-Line Support**

- abstract finite-observation collision theorem;
- strict finite Li/Weil/moment non-discrimination;
- canonical-product realization;
- flatness/global-structure escape conditions;
- exact statement of why the result does not apply directly to ζ.

### Paper C — primary, highest strategic value

**Real-Rooted Approximants and the Missing Compactness Theorem in Spectral Approaches to RH**

- finite spectral matching counterexample theorem;
- normal-family/tail-control sufficiency theorem;
- application checklist for CCM/CvS and Suzuki limits.

### Paper B — conditional on novelty

**Spectral-Asymptotic Exclusions for Classical Hilbert–Pólya Candidates**

- compact elliptic/graph invariant class;
- exact \(T\log T\) and heat-trace mismatch;
- stability under declared perturbations;
- explicit nonlocal/noncompact escape class.

### Paper D — exploratory

**Lower Bounds for a Restricted Schur-Certificate System for Local Weil Positivity**

- formal certificate proof system;
- invariant complexity measure;
- quantitative lower bound or explicit separating vector;
- no universal \(c_a\) claim.

### Synthesis paper — only after at least two theorem papers

A unifying statement may be attempted only after the observation and convergence barriers are proved. The likely principle is limited:

> A proof architecture whose accepted evidence factors through a bounded-dimensional observation map, and which supplies neither a uniqueness prior nor an effective tail modulus, cannot determine a global support property on an ambient class containing an exact observation collision.

This is a theorem schema, not a claim that all RH strategies have this form.

---

## 17. Success criteria

### Minimum viable success

One exact, non-vacuous theorem of the observation-factorization or structural-invariant form, with a natural class, explicit adversaries or invariant mismatch, and a stated escape route.

### Strong success

Paper A and Paper C both close, giving:

1. a rigorous finite-information obstruction;
2. a rigorous convergence boundary tailored to current Weil-form spectral constructions;
3. a concrete checklist for what a successful global limit proof must add.

### Aspirational success

A common information/compactness theorem covers finite moments, finite Euler data, and finite spectral windows without becoming vacuous, circular, or falsely universal.

### Explicit non-successes

The following do not count as completion:

- another RH-equivalent reformulation;
- a finite matrix with positive pivots;
- a method that fails at one prime window;
- a numerical sequence of real zeros matching zeta zeros;
- a private checker reporting `PASS`;
- a broad philosophical claim that RH conserves difficulty.

---

## 18. Immediate 30-day execution plan

### Days 1–7 — Freeze the baseline

1. Write the exact Weil-form convention from Suzuki 2026.
2. Map every internal \(L\), \(c_L\), matrix block, and support threshold to \(a\), \(Q_W^a\), and \(\lambda(a)\).
3. Build the two-axis evidence ledger.
4. Verify every claimed public citation and separate repository deposit from refereed publication.

### Days 8–14 — Prototype the first unconditional theorem

1. Define \(\mathfrak X_{\mathrm{sym}}\) and the allowed test family.
2. Prove the high-quartet small-contribution lemma.
3. Apply it to the first \(K\) Li coefficients and one finite Weil-test family.
4. State the exact fixed-\(K\) limitation.

### Days 15–21 — Test exact collision

1. Choose high on-line compensating atoms.
2. compute the observation Jacobian symbolically;
3. prove or refute the rank condition;
4. construct a rational/interval-certified example;
5. attempt the canonical-product realization.

### Days 22–30 — Open the convergence track

1. Freeze one CCM/CvS or Suzuki normalization.
2. list every currently proved finite/local property;
3. state the missing locally uniform convergence estimate;
4. construct a finite-evidence counterexample sequence;
5. formulate a normal-family plus identification theorem with an effective tail obligation.

**Day-30 decision:** continue to Paper A if exact collision or a strong strict-inequality theorem survives; continue to Paper C if the convergence counterexample is materially sharper than a generic textbook observation. Otherwise narrow the claims before building a repository around them.

---

## 19. Core reference map

### Weil form and current spectral constructions

1. M. Suzuki, [*Weil's quadratic form via the screw function*](https://arxiv.org/abs/2606.09096), 2026 preprint.
2. A. Connes and C. Consani, [*Weil positivity and Trace formula, the archimedean place*](https://arxiv.org/abs/2006.13771), Selecta Math. 27 (2021).
3. A. Connes and W. D. van Suijlekom, [*Quadratic Forms, Real Zeros and Echoes of the Spectral Action*](https://doi.org/10.1007/s00220-025-05493-1), Commun. Math. Phys. 406 (2025), 312.
4. A. Connes, C. Consani, and H. Moscovici, [*Zeta Spectral Triples*](https://arxiv.org/abs/2511.22755), 2025 preprint.

### Quantitative RH equivalents

5. J.-F. Burnol, [*A lower bound in an approximation problem involving the zeros of the Riemann zeta function*](https://arxiv.org/abs/math/0103058), Adv. Math. 170 (2002), 56–70.
6. L. Báez-Duarte, [*A strengthening of the Nyman–Beurling criterion for the Riemann hypothesis*](https://arxiv.org/abs/math/0205003), 2002/2003.
7. A. Voros, [*Sharpenings of Li's criterion for the Riemann Hypothesis*](https://arxiv.org/abs/math/0506326), 2005/2006.

### Moment and finite-information tools

8. R. Curto and L. Fialkow, [*Flat Extensions of Positive Moment Matrices: Recursively Generated Relations*](https://doi.org/10.1090/memo/0648), Memoirs AMS 136 (1998).
9. C. Bayer and J. Teichmann, [*The proof of Tchakaloff's theorem*](https://arxiv.org/abs/math/0502473), Proc. AMS 134 (2006).

### Generalized Euler products and spectral no-go precedents

10. J. Andersson, [*Mittag-Leffler type theorems for Helson zeta-functions*](https://arxiv.org/abs/2408.15713), 2024 preprint.
11. S. Endres and F. Steiner, [*The Berry–Keating operator on \(L^2(\mathbb R_+,dx)\) and on compact quantum graphs*](https://doi.org/10.1088/1751-8113/43/9/095204), J. Phys. A 43 (2010).

### Complexity barriers as a methodological analogy only

12. T. Baker, J. Gill, and R. Solovay, [*Relativizations of the P =? NP Question*](https://doi.org/10.1137/0204037), SIAM J. Comput. 4 (1975).
13. A. Razborov and S. Rudich, [*Natural Proofs*](https://www.sciencedirect.com/science/article/pii/S002200009791494X), J. Comput. Syst. Sci. 55 (1997).
14. S. Aaronson and A. Wigderson, [*Algebrization: A New Barrier in Complexity Theory*](https://doi.org/10.1145/1490270.1490272), ACM Trans. Comput. Theory 1 (2009).

The complexity papers provide a standard of formal precision: a barrier requires a defined proof behavior and a separating construction. They do not imply that an analogous universal RH barrier exists.

---

## 20. Final research posture

The most credible project is not to prove that RH “conserves difficulty.” It is to prove several exact boundary theorems:

- finite observations do not locate an infinite zero set without a uniqueness prior;
- finite self-adjoint approximants do not identify a global entire-function limit without compactness and tail control;
- classical spectral classes with the wrong Weyl law cannot be exact realizations;
- one restricted certificate calculus may require growing complexity even when other methods remain available.

These conclusions are narrower than the original philosophical ambition, but they are logically closed, testable, compatible with current literature, and capable of producing publishable mathematics without solving RH.
