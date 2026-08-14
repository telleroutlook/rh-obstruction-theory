# Problem OB-40 — B: Seeley complex powers and the classical symbol of $H^{1/m}$

**Type:** microlocal analysis / pseudodifferential operator theory / citation verification

**Non-circularity:** RH is not assumed.  No zeros of $\zeta$, no Euler product,
no zero-counting law.  This is a question about the symbol calculus of
pseudodifferential operators on compact manifolds.

---

## Background and motivation

Paper B's proof of Theorem D (classical elliptic operators excluded) reduces the
general order-$m$ case to order 1 as follows (paper, proof of Theorem D):

> "By the pseudodifferential Weyl law (Hörmander [1968], Theorem 4.4; for general
> order $m>0$ reduce to order 1 via $H^{1/m}$, which is a classical elliptic
> $\Psi$DO of order 1 by Seeley's complex-powers theory [Seeley 1967], with
> $N_H(\Lambda)=N_{H^{1/m}}(\Lambda^{1/m})$)"

Two claims are bundled in this parenthetical:

**(A) Existence:** $H^{1/m}$ is well-defined as a pseudodifferential operator on $M$.

**(B) Classicality:** $H^{1/m}$ is a *classical* (polyhomogeneous) $\Psi$DO of
order 1, with principal symbol $h_m(x,\xi)^{1/m}$.

The **Seeley 1967** paper is:
R.T. Seeley, "Complex powers of an elliptic operator," in *Singular Integrals
(Proc. Sympos. Pure Math., Chicago, 1966)*, AMS, Providence, RI, 1967, pp. 288–307.

**No gap: Seeley's construction is in the classical calculus.** The contour-integral
construction in Seeley [1967] uses a parametric resolvent whose symbol has a full
asymptotic expansion in terms homogeneous of degrees $-m-j$ (in $(\xi,\lambda^{1/m})$);
integrating term by term against $\lambda^z\,d\lambda$ yields a symbol with a complete
polyhomogeneous expansion of degrees $mz, mz-1, mz-2, \ldots$.  Hence
$H^z\in\Psi^{mz}_{\rm cl}(M)$.  The $S^{mz}_{1,0}$ membership is only the weaker
outer envelope that classical symbols automatically satisfy; it is not the final
precision of the construction.  The precise reference is Shubin (2001), §11,
Theorem 11.2; §9 covers only the parametric resolvent.

---

## All definitions (self-contained — everything is here)

### Setting

$M$ is a closed smooth manifold of dimension $d\ge 1$.
$H$ is a positive self-adjoint pseudodifferential operator of order $m>0$ on $M$,
with compact resolvent and **classical** principal symbol:
$$\sigma(H)(x,\xi) \sim h_m(x,\xi) + h_{m-1}(x,\xi) + \cdots,$$
where each $h_{m-j}$ is smooth and positively homogeneous of degree $m-j$ in $\xi$
for $|\xi|\ge 1$, and $h_m(x,\xi)\ge c|\xi|^m>0$ for $|\xi|\ge 1$
(**positive classical elliptic of order $m$**).

### Classical $\Psi$DO calculus $\Psi^r_{\rm cl}(M)$

A pseudodifferential operator $A\in\Psi^r_{\rm cl}(M)$ is **classical** if its
complete symbol in every local chart has an asymptotic expansion
$$\sigma(A)(x,\xi)\sim a_r(x,\xi)+a_{r-1}(x,\xi)+\cdots,$$
where each $a_{r-j}$ is smooth and **positively homogeneous of degree $r-j$** in
$\xi$ for $|\xi|\ge 1$.

The **principal symbol** of $A\in\Psi^r_{\rm cl}$ is $a_r$, which transforms as a
function on $T^*M\setminus 0$.

### Seeley's complex powers

For a positive classical elliptic $H\in\Psi^m_{\rm cl}(M)$ with $H>0$, Seeley
[1967] defines $H^z$ for $z\in\CC$ as an operator whose symbol is constructed via
a contour integral:
$$H^z = \frac{i}{2\pi}\int_\Gamma \lambda^z (H-\lambda)^{-1}\,d\lambda,$$
where $\Gamma$ is a ray (or keyhole contour) in the resolvent set of $H$, oriented
from $\infty e^{-i\varphi}$ to $\infty e^{i\varphi}$ around the spectral cut along
the negative real axis (Seeley's convention); equivalently in standard orientation,
$$H^z = \frac{1}{2\pi i}\int_\Gamma \lambda^z (\lambda-H)^{-1}\,d\lambda$$
with $\Gamma$ encircling the spectrum counterclockwise.  Seeley proves
$H^z\in\Psi^{mz}_{\rm cl}(M)$ (see Shubin §11, Theorem 11.2 for the explicit
classical-symbol statement).

**The key question:** Is the output $H^z$ in the *classical* calculus
$\Psi^{mz}_{\rm cl}(M)$ (polyhomogeneous symbol), or only in $\Psi^{mz}(M)$
(general $S^{mz}_{1,0}$ symbol)?

### The counting-function reduction

For any positive operator $H$ with eigenvalues $0<e_1\le e_2\le\cdots$:
$$N_H(\Lambda) = \#\{k : e_k\le\Lambda\},\quad
N_{H^{1/m}}(\Lambda) = \#\{k : e_k^{1/m}\le\Lambda\}
= \#\{k : e_k\le\Lambda^m\} = N_H(\Lambda^m).$$
Hence $N_H(\Lambda) = N_{H^{1/m}}(\Lambda^{1/m})$ by substitution $\Lambda\to\Lambda^{1/m}$.
This part is **elementary** (verified above).

---

## The claims to be verified

**Claim A (Existence).** For a positive classical elliptic $H\in\Psi^m_{\rm cl}(M)$
with $H>0$, $H^{1/m}$ is well-defined as a pseudodifferential operator on $M$.
This should follow from Seeley [1967]; state the exact theorem.

**Claim B (Classicality).** $H^{1/m}\in\Psi^1_{\rm cl}(M)$, i.e.\ $H^{1/m}$ has
a polyhomogeneous symbol of order 1 with principal symbol $h_m(x,\xi)^{1/m}$.
This requires either:
- A result in Seeley [1967] showing the output is classical when the input is, OR
- A separate reference establishing classicality (e.g.\ Shubin, Taylor, or Hörmander).

**Claim C (Sufficiency for Paper B).** The proof of Theorem D only needs the Weyl
law $N_{H^{1/m}}(\Lambda)\sim C_H\Lambda^d$ for some $C_H>0$.
Does Claim B (full classicality) follow from the weaker statement that $H^{1/m}$
is *any* order-1 elliptic $\Psi$DO on $M$ (not necessarily classical)?

**Claim D (Reduction correctness).** Confirm $N_H(\Lambda)=N_{H^{1/m}}(\Lambda^{1/m})$
is valid, and that the Weyl law for $H^{1/m}$ gives Weyl constant
$C_H = (2\pi)^{-d}\!\int_{T^*M}\!\mathbf{1}_{h_m(x,\xi)^{1/m}\le 1}\,d\xi\,dx
= (2\pi)^{-d}\!\int_{T^*M}\!\mathbf{1}_{h_m(x,\xi)\le 1}\,d\xi\,dx$.

This formula is for $H$ acting on scalar functions (or sections of a rank-1 bundle).
If Paper B allows $H$ acting on sections of a vector bundle $E$ of fiber rank $r$,
the Weyl constant becomes
$C_H = (2\pi)^{-d}\!\int_{T^*M}\!\operatorname{tr}_E\!\bigl(\mathbf{1}_{h_m(x,\xi)\le 1}\bigr)\,d\xi\,dx$,
where $h_m(x,\xi)$ is a positive self-adjoint endomorphism of $E_x$ and the indicator
is applied in the spectral sense.  The reduction $N_H(\Lambda)=N_{H^{1/m}}(\Lambda^{1/m})$
is unaffected: it is a pointwise eigenvalue identity holding at every multiplicity.

---

## Proof skeleton to be closed

### Step 1 — Seeley's result for $H^z$

Locate the theorem in Seeley [1967] that defines $H^z$ and states its symbol class.
Identify whether the output is in $\Psi^{mz}_{1,0}$ or $\Psi^{mz}_{\rm cl}$.

**Candidate statement** (to confirm): If $H\in\Psi^m_{\rm cl}(M)$ is positive
elliptic with $H>0$, then $H^z\in\Psi^{mz}_{1,0}(M)$ for all $z\in\CC$,
and for $z=s\in\RR$, $H^s$ has principal symbol $h_m(x,\xi)^s$ in the
$S^{ms}_{1,0}$ sense.

**What to close for Step 1:** Does Seeley's construction yield a classical symbol,
or only $S^{ms}_{1,0}$?  Cite the specific pages/theorem of Seeley [1967].

### Step 2 — Classicality of $H^{1/m}$

If Seeley does not directly give classicality, identify the correct reference.

**Candidate references:**
- M.A. Shubin, *Pseudodifferential Operators and Spectral Theory*, Springer, 2001,
  **§11, Theorem 11.2** (complex powers; §9 covers only the parametric resolvent).
- M. Taylor, *Partial Differential Equations II*, Springer, 1996, §7.
- L. Hörmander, *The Analysis of Linear Partial Differential Operators III*,
  Springer, 1985, §18.1.

**Hint:** For $H$ *classical* positive elliptic of order $m$, the contour-integral
construction of $H^s$ produces an operator whose symbol has an asymptotic expansion
$\sigma(H^s)\sim h_m^s + (\text{lower order classical terms})$, so $H^s$ IS
classical of order $ms$.  This is expected to follow from the standard calculus,
but requires a reference that explicitly handles the polyhomogeneous expansion of
$H^s$ (not just its $S^{ms}_{1,0}$ membership).

**What to close for Step 2:** Provide a precise reference (with theorem number)
for $H^s\in\Psi^{ms}_{\rm cl}(M)$ when $H\in\Psi^m_{\rm cl}(M)$ is positive
elliptic with $H>0$.

### Step 3 — Sufficiency check

Assuming only $H^{1/m}\in\Psi^1(M)$ (order 1, not necessarily classical), does
the pseudodifferential Weyl law for order-1 operators still give
$N_{H^{1/m}}(\Lambda)\sim C_H\Lambda^d$?

The standard Weyl law requires an operator of order $r>0$ in the classical calculus
(to apply Hörmander [1968] Theorem 4.4).  If $H^{1/m}$ is only in $S^1_{1,0}$
(not classical), the standard Weyl law may not apply.

**What to close for Step 3:** Determine whether classicality of $H^{1/m}$ is
truly needed for the Weyl law in Paper B's proof, or whether a weaker symbol
condition suffices.

---

## Acceptance criteria

1. **CONFIRMED:** Seeley [1967] (or an identified companion reference) establishes
   $H^{1/m}\in\Psi^1_{\rm cl}(M)$ with principal symbol $h_m(x,\xi)^{1/m}$, with
   explicit theorem number; Weyl law applies directly; reduction $N_H(\Lambda)=
   N_{H^{1/m}}(\Lambda^{1/m})$ correct; Weyl constants agree.

2. **PARTIAL-A:** $H^{1/m}\in\Psi^1_{1,0}(M)$ confirmed (not classical), but
   Weyl law for $S^1_{1,0}$ operators also established (via a separate reference),
   so Paper B's proof still works with a different/additional citation.

3. **PARTIAL-B:** Classicality confirmed but reduction $N_H(\Lambda)=
   N_{H^{1/m}}(\Lambda^{1/m})$ needs adjustment (e.g.\ $H>0$ required for
   eigenvalue bijection).

4. **REFUTED:** $H^{1/m}$ is not a $\Psi$DO of any standard class for some
   positive elliptic $H$ (explicit example); or Weyl law fails for the
   resulting operator class.

5. **INCONCLUSIVE:** References located but classicality question unresolved;
   state what additional source would close it.

---

## Numerical anchor (sanity only — not an input)

For $H = -d^2/dx^2 + 1$ on $S^1 = \RR/(2\pi\ZZ)$ (order $m=2$, dimension $d=1$):

- Eigenvalues of $H$: $e_n = n^2+1$ for $n\in\ZZ$ (each with multiplicity 1 per Fourier mode).
- $H^{1/2}$ should have eigenvalues $e_n^{1/2} = (n^2+1)^{1/2}$.
- Reduction check: $N_H(\Lambda) = \#\{n\in\ZZ : n^2+1\le\Lambda\}$
  $= N_{H^{1/2}}(\Lambda^{1/2})$, since
  $\#\{n : (n^2+1)^{1/2}\le\Lambda^{1/2}\} = \#\{n : n^2+1\le\Lambda\}$. ✓

Weyl constant: the principal symbol is $h_2(x,\xi)=\xi^2$ (not $\xi^2+1$; the $+1$
is lower order and does not contribute to the Weyl constant).
$$C_H = (2\pi)^{-1}\int_{T^*S^1}\mathbf{1}_{h_2(x,\xi)\le 1}\,d\xi\,dx
= (2\pi)^{-1}\cdot\underbrace{\int_0^{2\pi}dx}_{2\pi}\cdot
  \underbrace{\int_{-1}^1 d\xi}_{2} = 2.$$
Weyl law predicts $N_H(\Lambda)\sim 2\Lambda^{1/2}$, matching
$N_H(\Lambda)=2\lfloor\sqrt{\Lambda-1}\rfloor+1\sim 2\sqrt\Lambda$. ✓

Reviewer should verify: $N_H(100) = 2\cdot 9+1=19$ (since $\sqrt{99}\approx 9.95$,
so $n^2+1\le 100$ iff $|n|\le 9$: gives $n=-9,...,9$, total 19 modes).
And $N_{H^{1/2}}(10) = \#\{n : (n^2+1)^{1/2}\le 10\} = \#\{n: n^2+1\le 100\} = 19$. ✓

---

## Pre-send lint notes (PROMPT_LINT.md self-check)

| Item | Status |
|---|---|
| L1 (order ≠ finite exp type) | N/A — no entire functions |
| L2–L4 | N/A |
| L5 (RH via divisor) | PASS — no RH, no zeta zeros |
| L6 (vacuous target) | PASS — REFUTED path exists (explicit non-$\Psi$DO example) |
| L7–L15 | N/A |
| L16 (representation invariance) | PASS — principal symbol $h_m^{1/m}$ is coordinate-invariant on $T^*M\setminus 0$ |
| L17 (cited black boxes) | PASS — Seeley [1967] cited with problem asking for exact theorem; Hörmander [1968] cited with theorem number (4.4); Shubin/Taylor listed as candidate references |
| L18 (numerical anchor by script) | PASS — $N_H(100)=19$ and $N_{H^{1/2}}(10)=19$ independently checkable |
| L19 (honest inconclusive verdict) | PASS — INCONCLUSIVE outcome listed |
| L20–L24 | N/A |
| Self-containment | PASS — all operators, symbol classes, manifold conditions defined in-file; Seeley/Hörmander/Shubin fully cited |
