# papers/PAPER_LINT.md — pre-submission self-audit checklist

Every check must be **actually run** (grep command, script, compilation) before
submission.  "Looks fine by eye" is not a pass.  Record the run output as a one-line
note next to each item.

This file lives at `papers/PAPER_LINT.md`.  Run it against a specific paper by
substituting `TEX=papers/<id>/<file>.tex` in the commands below.

---

## Part I — TeX / structural (automatable)

### P1 — No hardcoded cross-references

Every `Theorem A`, `Lemma 2.4`, `Corollary D`, etc. in the body must be a
`\ref{...}`, not a hand-typed letter or number.  Hard-coded refs become stale when
theorem order changes.

```bash
TEX=papers/paper-A/arithmetic-information-barriers-rh.tex
# Detect hardcoded main-result refs (Theorem~X, Corollary~X, Lemma~N.N)
grep -n 'Theorem~[A-Z]\|Corollary~[A-Z]\|Lemma~[0-9]' "$TEX" \
  | grep -v '\\ref{'
```

**Pass:** zero lines output.
**Current status (paper-A):** 38 hardcoded occurrences found — fix before external review.

---

### P2 — Every `\label` is referenced at least once

An unreferenced label wastes the reader's lookup effort and signals dead structure.

```bash
# Extract all label names; skip lines marked % xref-only; check each appears in a \ref or \eqref
grep -P '\\label\{[^}]+\}' "$TEX" | while IFS= read -r LINE; do
  echo "$LINE" | grep -q 'xref-only' && continue
  L=$(echo "$LINE" | grep -oP '(?<=\\label\{)[^}]+')
  n=$(grep -cE "\\\\(eqref|ref)\{$L\}" "$TEX" 2>/dev/null || true)
  [ "$n" -eq 0 ] && echo "UNUSED: $L"
done
```

**Pass:** zero `UNUSED` lines.  Exception: section labels referenced only from a
table-of-contents or external hyperlink are acceptable — mark with a comment
`% xref-only`.
**Current status (paper-A):** 21 unused labels — either add `\ref` usages or remove.

---

### P3 — Every bibliography entry is cited

```bash
# Extract all \bibitem keys; check each appears in a \cite
grep -oP '\\bibitem\{[^}]+\}' "$TEX" | sed 's/\\bibitem{//;s/}//' | while read K; do
  n=$(grep -c "\\\\cite[^{]*{[^}]*\\b$K\\b" "$TEX" 2>/dev/null)
  [ "$n" -eq 0 ] && echo "UNCITED: $K"
done
```

**Pass:** zero `UNCITED` lines.

---

### P4 — Clean LaTeX compilation

```bash
cd "$(dirname "$TEX")"
pdflatex -interaction=nonstopmode "$(basename "$TEX")" 2>&1 \
  | grep -E "undefined|Warning.*ref|Warning.*cite|Error" | grep -v Overfull | grep -v Underfull
```

**Pass:** zero lines (only Overfull/Underfull hbox warnings are acceptable at draft
stage — fix before final submission).

---

### P5 — Short title semantically matches full title

```bash
grep -n '\\title\[' "$TEX"
```

Manually verify that the bracketed short title preserves all load-bearing
qualifiers (e.g. "Formal", "Finite", "Exact") that distinguish the paper's actual
scope from a broader claim.

**Current status (paper-A):** short title drops "Formal" — fix before submission.

---

## Part II — Mathematical content

### P6 — Every lemma / proposition / theorem is used in a later proof

```bash
# List all \label{lem:*}, \label{thm:*}, \label{prop:*}, \label{cor:*}
# Then check each is \ref'd in the proof text
grep -oP '\\label\{(lem|thm|prop|cor):[^}]+\}' "$TEX" \
  | sed 's/\\label{//;s/}//' | while read L; do
  n=$(grep -c "\\\\ref{$L}" "$TEX")
  [ "$n" -eq 0 ] && echo "UNUSED RESULT: $L"
done
```

For each `UNUSED RESULT`: either (a) use it in a proof, (b) remove it, or
(c) add a comment explaining it is background context only.  A result proved but never
used is misleading about the logical dependencies.

---

### P7 — Definition consistency: same predicate, same wording throughout

For each formally defined object (predicate, class, map), grep for its name and
verify every occurrence uses identical quantifiers and modifiers.

```bash
# Example: predicate P — check "every atom" vs "every nontrivial atom" vs other variants
grep -n "every.*atom\|nontrivial atom\|P(\\\\mathcal" "$TEX"
```

Repeat for every defined term.  **Pass:** all occurrences use identical wording,
or differences are explicitly flagged as "informal paraphrase."

**What to check in paper-A:** predicate $P$, ambient class $\mathfrak{H}_\text{sym}$,
collision condition $(\star)$, observation map $O_j$.

---

### P8 — Every borrowed result is attributed at first use

If a lemma restates or builds on a known result, the citation must appear **at that
lemma** (not only in the bibliography or in a later remark).

```bash
grep -n '\\begin{lemma}\|\\begin{proposition}\|\\begin{corollary}' "$TEX" \
  | while IFS=: read lineno rest; do
  # Check the 5 lines following for a \cite
  window=$(sed -n "$((lineno)),$((lineno+5))p" "$TEX")
  echo "$window" | grep -q '\\cite' || echo "Line $lineno: no \\cite near $(echo $rest | head -c 60)"
done
```

**Manual follow-up:** for any lemma without a nearby `\cite`, confirm the result is
original or add the attribution.

**Current status (paper-A):** Lemma 2.8 (sum-product identity) restates
Bombieri–Lagarias (1999) without a citation at the lemma — add `\cite{BombieriLagarias1999}`.

---

### P9 — Asymptotic error orders verified by script

For every displayed asymptotic of the form $f(T) = g(T) + O(T^{-k})$:

1. Write or point to a script in `checker/` or `discovery/` that independently
   expands $f$ to the stated order.
2. Confirm the remainder really is $O(T^{-k})$, not $O(T^{-(k-1)})$.
3. If the order improvement relies on a parity/symmetry argument
   (e.g. a real/imaginary splitting), state the symmetry explicitly in the proof.

```bash
grep -n 'O(T\^{-\|O(T^{-' "$TEX"
```

For each hit: is the claimed order independently verified?  Record the script path.

**Current status (paper-A):** Lemma 2.9 ($q_j(T) = 4j^2/T^2 + O(T^{-4})$) — the
$O(T^{-3}) \to O(T^{-4})$ step was unargued; parity argument now added (this session).

---

### P10 — No informal qualifiers in formal definitions or theorem statements

```bash
grep -n 'nontrivial\|clearly\|obvious\|trivially\|it is easy to see\|well-known' "$TEX"
```

In **formal definitions and theorem statements**: remove or replace with a precise
condition.  In proof text or remarks: acceptable if genuinely self-evident to the
target audience, but flag for review.

---

### P11 — All formulas in remarks / footnotes verified

For every `\begin{remark}` containing a formula:

1. Is the formula consistent with the surrounding definitions?
2. If it claims a structural property (e.g. "Vandermonde relation", "Chebyshev
   identity applies"), is the prerequisite (e.g. $|z|=1$) actually satisfied?

```bash
# Extract remark blocks for manual reading
awk '/\\begin{remark}/,/\\end{remark}/' "$TEX"
```

For each formula in a remark: check the preconditions hold for the objects being
discussed, not merely for superficially similar objects.

**Current status (paper-A):** Remark 2.7 — cosine-Vandermonde claim had wrong angle
factor ×2 and missing $r_k^j$ precondition; fixed this session.

---

## Part III — Methodology and scope (per CLAUDE.md)

### P12 — Barrier criteria: all five components explicit

A result may be labeled a *barrier* only when the paper explicitly states:
1. **Method class** (membership checkable)
2. **Ambient object class**
3. **Observation map**
4. **Target predicate**
5. **Escape route** (explicit construction outside the class)

```bash
grep -n 'barrier\|obstruction\|no-go' "$TEX" | grep -iv '%'
```

For each hit: verify all five components are named in the theorem statement or
immediately adjacent text.

---

### P13 — No RH-equivalent claimed as a barrier

An RH-equivalent criterion (`C ⟺ RH`) locates difficulty; it does not prove
impossibility.

```bash
grep -n 'equivalent.*RH\|iff.*RH\|RH.*iff\|if and only if.*Riemann' "$TEX"
```

For each hit: confirm the result is labeled "RH-equivalent reformulation" or
"locates difficulty," **not** "barrier" or "obstruction."

---

### P14 — Abstract and introduction scope claims

```bash
sed -n '/\\begin{abstract}/,/\\end{abstract}/p' "$TEX"
sed -n '/\\section{Introduction}/,/\\section{/p' "$TEX" | head -80
```

Manually verify: no sentence implies progress toward, or evidence for/against, RH.
Permitted: "this shows a class of strategies cannot succeed" with explicit class.
Forbidden: "this suggests RH is…", "this is consistent with RH", "this supports RH."

---

### P15 — Complexity-theory analogies labeled as motivational only

```bash
grep -n 'natural proof\|Razborov\|Baker.*Gill\|relativiz\|barrier.*complex' "$TEX"
```

For each hit: confirm the text contains a qualifier such as "structural and
motivational, not a formal reduction."  A bare analogy without this disclaimer
overstates the result.

---

### P16 — Two-axis evidence status for every imported claim

Every claim imported from the literature that is used as a **premise** in a proof
must have:
- Mathematical status: `REFEREED` or `INDEPENDENTLY-CHECKED`
- Computational status (if a computational claim): `REPRODUCIBLE` or higher

```bash
grep -n '\\cite{' "$TEX" | while IFS=: read lineno rest; do
  # Flag citations in proof environments
  context=$(sed -n "$((lineno-3)),$((lineno+3))p" "$TEX")
  echo "$context" | grep -q '\\begin{proof}\|therefore\|hence\|it follows\|by.*,' \
    && echo "Line $lineno: cite in proof context — check evidence level: $rest"
done | head -30
```

**Manual follow-up:** for each citation inside a proof, check the cited result is
verified in `baseline/` or labeled as an assumption.

---

### P17 — Representation-invariant margins only

```bash
grep -n 'margin\|eigenvalue\|Schur\|pivot\|shift.*I\|c_a\|c_L\|lambda.*shift' "$TEX"
```

For each margin-like quantity: confirm it is the generalized Rayleigh quotient
$\lambda(a)$ or another proved invariant under the method class's allowed
transformations.  A scalar shift $-c I$ or an unnormalized Schur residual is a
diagnostic, not a universal lower bound.

---

### P18 — Constructive/existential qualifier: definition honors downstream corollaries

When a formal definition contains a qualifier such as "explicit", "constructive",
"computable", or "effective", every theorem or corollary that claims to produce an
instance of the class must satisfy the qualifier.  Where a corollary is non-constructive
(e.g. proved via a pure-existence argument), the definition must explicitly allow
existential instances, or the qualifier must be removed.

```bash
# Step 1: find all occurrences of qualifier words
grep -n 'explicit\|constructive\|computable\|effective' "$TEX" | grep -v '%'
# Step 2: find all \begin{definition} blocks
awk '/\\begin\{definition\}/,/\\end\{definition\}/' "$TEX"
```

**Manual check:** for each definition block containing a qualifier, list every
downstream theorem/corollary that claims an instance.  Verify each either (a) provides
an explicit construction, or (b) is labeled "existential" and the definition permits it.

---

### P19 — Parity/symmetry arguments proven to sufficient order

When a proof invokes a parity or symmetry argument to cancel an error term
(e.g. "the $T^{-k}$ coefficient is purely imaginary, so $\operatorname{Re}[\cdot]$
has no $T^{-k}$ term"), the expansion must be displayed to **one order beyond** the
claimed cancellation.  The proof must show explicitly that the next real part is
non-zero (or state its sign), not leave it implicit.

```bash
grep -n 'purely imaginary\|purely real\|odd.*order\|even.*order\|imaginary part\|real part.*vanish' "$TEX"
```

For each hit inside a proof block: check that the asymptotic expansion is carried to
sufficient order that the cancellation is self-contained.

---

### P20 — No unsupported strong number-theoretic assertions

Assertions such as "is transcendental", "is irrational", "cannot be rational",
"must be algebraic", "is provably" outside a formal proof require an explicit
citation or must be weakened to "is not currently known to be rational" (or
analogous hedge).

```bash
grep -n 'transcendental\|irrational\|cannot be rational\|must be algebraic\|provably\b' "$TEX" \
  | grep -iv '%'
```

**Pass:** every hit either falls inside a `\begin{proof}...\end{proof}` block and the
claim is derived there, or is immediately followed by a `\cite{...}`, or is replaced
with a hedged phrasing.

---

### P21 — "Analogous argument" claims have no in-paper refutation

When a passage says "an analogous argument applies to [Y]", grep the rest of the
paper for any remark, footnote, or parenthetical that restricts or explicitly refuses
the analogy for [Y].

```bash
grep -n 'analogous\|same argument\|by the same reasoning\|an analogous\|same proof' "$TEX"
```

For each hit: search for the specific object [Y] named in the analogy claim and
verify no other passage contradicts it.  If a later section adds a restriction
(e.g. "for moment-type tests, distinct heights do not imply Vandermonde
invertibility"), then the earlier "analogous argument" claim must be qualified or
removed.

---

### P22 — External theorem invocations name all substituted parameters

When a proof invokes an external theorem by author and number
(e.g. "By Andersson \cite{...}, Theorem 5"), the proof text must state what
specific objects, sets, and parameter values are being substituted into the
cited theorem's hypotheses.  A bare citation without a parameter-mapping is
insufficient.

```bash
grep -n 'By.*\\\\cite\|by.*\\\\cite\|Apply.*\\\\cite\|Applying.*\\\\cite\|invoking.*\\\\cite' "$TEX"
```

For each hit: verify the sentence or the immediately following one names the specific
inputs (e.g. "applied with $U = \{\operatorname{Re} s > 0\}$ and divisor
$D = [z_1]$").

---

### P23 — Operator class definition: formal symmetry precedes self-adjoint extension

When an operator class definition depends on an extension theorem (KLMN /
Friedrichs / Lax–Milgram), the definition must first establish formal symmetry
and semi-boundedness on a dense domain **before** invoking the extension.
Self-adjointness may not be assumed as a hypothesis and then derived by KLMN:
that is circular.

```bash
grep -n 'KLMN\|Friedrichs\|self-adjoint.*extension\|quadratic form\|form domain' "$TEX"
```

For each hit: verify the surrounding definition/proof lists (i)~formally symmetric
on $C^\infty(M)$ and (ii)~semi-bounded on $C^\infty(M)$ as explicit hypotheses
**prior** to the statement "the Friedrichs extension is the unique self-adjoint
operator associated with the shifted form."

---

### P25 — Literature formula descriptions match the cited source

When the text (introduction, background, or body) describes a formula from a cited
external result — e.g. writes an explicit equation and attributes it to a specific
author/paper — the formula must be checked against the source in `baseline/` or the
arXiv tarball, not relied on from memory.  Common failure modes:

- Confusing two normalizations in the same paper (e.g. CCM's $\hat{\xi}_\lambda$ vs
  the separate $k_\lambda \to \Xi$ result, Lemma 7.3).
- Omitting an open step that the cited paper names explicitly.
- Describing the cited theorem's conclusion as if the open step were already closed.

```bash
# Find every sentence that contains both a formula and a \cite, outside proof blocks
grep -n '\\cite{' "$TEX" | grep -v '\\begin{proof}\|\\end{proof}' | head -30
```

**Manual check:** for each hit, open the corresponding `baseline/` source (or arXiv
tarball) and verify: (a) the displayed formula matches the cited paper's exact
statement, (b) any open step named in the cited paper is also flagged as open in
this paper's description.

---

### P24 — Optional theorem-environment titles do not repeat the automatic label

`\begin{theorem}[D]` renders as "Theorem 1 (D)" when the theorem is automatically
numbered 1 — and as "Theorem D (D)" if the environment is already titled `D` by a
custom counter.  Grep for optional arguments to theorem-like environments and
manually verify the rendered output does not duplicate the label.

```bash
grep -n '\\begin{.*}\[' "$TEX"
```

For each hit: check the rendered PDF (or mentally evaluate the counter) to confirm
the optional argument is a descriptive subtitle, not a repetition of the
auto-generated theorem identifier.

---

### P26 — Reference operator construction does not introduce spurious symbol-class terms

When a proof constructs a reference operator $P$ (to compare with $H$) by
quantization, symmetrization, and addition of a positive constant $b$, the
difference $Q = H - P$ contains a $-bI$ term of order~$0$.
For $m < 1$ and $\varepsilon < 1-m$, the order $m-1+\varepsilon < 0$ is
strictly below~$0$, so $-bI \notin \Psi^{m-1+\varepsilon}_{1,0}$.
The claim ``$Q \in \Psi^{m-1+\varepsilon}_{1,0}$ for every $\varepsilon\in(0,1)$''
is therefore wrong when $m < 1$.

```bash
# Find all operator constructions that add a constant to ensure positivity
grep -n 'positive constant\|P\\\s*:=\|P\s*=.*bI\|ensure.*P.*ge\|P\\\ge.*c.*>' "$TEX"
```

**For each hit:** verify one of the following:
(a) The construction uses $P = A^*A + \Pi_{\ker A}$ (no additive constant, so $Q = H-P \in \Psi^{m-1+\varepsilon}$ for all $\varepsilon$); or
(b) the constant is explicitly split: write $Q = Q_0 - bI$ where $Q_0 = H - P_0 \in \Psi^{m-1+\varepsilon}$ and the $-bI$ term is handled as a direct $b\|u\|^2$ form contribution; or
(c) the symbol-class claim is restricted to $\varepsilon > \max(0, 1-m)$.

---

### P27 — Tauberian theorems used in both directions are stated as biconditionals

When a Tauberian theorem (Karamata, Ikehara, Wiener–Ikehara, etc.) is invoked
in the paper in **both** the forward direction ($N \Rightarrow Z$) and the
inverse direction ($Z \Rightarrow N$), verify the cited theorem is actually a
biconditional ($\iff$), not only a one-way implication.

```bash
# Find Karamata / Tauberian invocations
grep -n 'Karamata\|Tauberian\|Ikehara\|Wiener.*Ikehara\|one needs\|suffices to have' "$TEX"
```

For each hit involving ``one needs $N_H(T) \sim \ldots$ to match $Z_H(t) \sim \ldots$'':
trace the cited theorem to confirm the $\Leftarrow$ direction is stated.  If only
the $\Rightarrow$ direction appears in the theorem statement, either add the
reverse direction or replace ``one needs'' with ``one sufficient condition is.''

---

### P28 — Single-letter symbol conflicts resolved

When a paper uses the same single letter for two distinct mathematical objects
(e.g.\ $S$ for both the set of observable records and the critical strip
$\{0 < \operatorname{Re} s < 1\}$), one occurrence must be renamed.

```bash
# Check for overloaded single-letter symbols in definitions and theorem statements
# Look for the same capital letter used in two different \begin{definition} blocks
grep -n '\\begin{definition}' "$TEX" | while IFS=: read lineno rest; do
  window=$(sed -n "${lineno},$((lineno+15))p" "$TEX")
  echo "Line $lineno: $(echo "$window" | grep -o '\$[A-Z]\$' | sort -u | tr '\n' ' ')"
done
```

**Manual check:** for each definition block, list the single-letter capitals it
introduces; verify none conflicts with a same-letter symbol introduced in another
definition or used as standard notation (strip, domain, set, space) elsewhere in
the paper.

---

### P29 — `\texorpdfstring` bookmark text matches formula's logical meaning

When a section/subsection uses `\texorpdfstring{$formula$}{bookmark-text}`, the
bookmark text must accurately express the *logical content* of the formula under
the definitions in force, not just a superficial reading of its symbols.

Common failure mode: a binary relation $R(A,B)$ reads as "$A$ does not $R$ $B$"
in the symbol string, but the *defined* meaning of $R$ makes $B$ the active
agent, so the correct reading is "$B$ does not [inverse of $R$] $A$".

```bash
grep -n '\\texorpdfstring' "$TEX"
```

For each hit: identify the definition of every relation/operator used in the
formula; re-derive what the formula asserts in plain English; compare with the
bookmark text.  **Pass:** bookmark text and logical meaning agree.

**Precedent (paper-A):** $\Ofinite\npreceq\Otheta$ with definition
$O_a\preceq O_b\iff O_a=f\circ O_b$ (i.e.\ "$O_b$ refines $O_a$") was given
bookmark "O-fin does not refine O-theta" — wrong direction; correct bookmark
is "O-theta does not refine O-fin".

---

### P30 — Every free variable in a theorem/corollary statement is explicitly bound

In every `\begin{theorem}`, `\begin{corollary}`, `\begin{proposition}` block,
each variable that is not a universally quantified dummy must be bound by an
explicit prefix ("Fix $K\ge 1$", "Let $K\ge 1$ be given", "for all $K\ge 1$",
or as a conclusion variable in the "there exists" clause).

```bash
# Extract all theorem-like environment openers and the 15 lines following
grep -n '\\begin{\(theorem\|corollary\|proposition\|maincor\|mainthm\|mainthmprime\)}' "$TEX" \
  | while IFS=: read lineno rest; do
    window=$(sed -n "${lineno},$((lineno+15))p" "$TEX")
    echo "--- Line $lineno ---"
    echo "$window"
    echo
  done
```

**Manual check:** for each block, list every capital letter and named parameter
that appears; verify each is bound.

**Precedent (paper-A):** Corollary "Positivity threshold" used $K$ in
"$\Li_j(\mathcal{Z}_+)>0$ for $j=1,\ldots,K$" without first writing "Fix $K\ge 1$".

---

### P31 — "Same argument as part (X)" spells out the conclusion for part (Y)

When a multi-part proof abbreviates a sub-proof with "by the same argument as
part~(X)" or "an analogous argument gives", the *conclusion* of that sub-proof
must be stated explicitly for part~(Y), not left implicit.

In particular: if part~(X) proves "$\zeta \in \mathcal{H}_S$" via a chain
$A \Rightarrow B \Rightarrow \zeta\in\mathcal{H}_S$, then part~(Y) must
exhibit the corresponding chain ending with "$\zeta'\in\mathcal{H}_S$",
even if step~$A$ is abbreviated.

```bash
grep -n 'same argument\|analogous argument\|same reasoning\|as part~\|as in part' "$TEX"
```

For each hit: verify the conclusion of the current part is spelled out
explicitly (not just "hence [condition X]" while omitting the class-membership
conclusion that requires the full chain).

**Precedent (paper-A):** Part~(b) of Corollary~D said $R_0$ "holomorphic on $S$
(same argument as part~(a))" but omitted "$\zeta_{\chi^+}$ extends
holomorphically to $U_0$, so $\zeta_{\chi^+}\in\mathcal{H}_S$" — a required
intermediate conclusion suppressed by the abbreviation.

---

### P32 — Operator class definition: Friedrichs realization identified by name after construction

When a definition block constructs a Friedrichs (or other canonical)
realization $H_F$ of a formal operator $H$, the text immediately following
the `\end{definition}` must state explicitly that $H$ is henceforth identified
with $H_F$ and that all spectral objects (counting function, heat trace,
spectrum) refer to $H_F$.

Without this declaration, theorems using $N_H$ or $\operatorname{spec}_\times(H)$
are technically undefined for the original formal operator.

```bash
# Find definitions that introduce a Friedrichs extension
grep -n 'Friedrichs\|H_F\|self-adjoint.*extension' "$TEX"
```

For each hit inside a `\begin{definition}...\end{definition}` block:
verify the line immediately after `\end{definition}` contains an explicit
identification sentence.

**Precedent (paper-B):** Definition of $\Csub$ constructed $H_F$ inside the
block, but Theorem~D$'$ then used $N_H$ and $\operatorname{spec}_\times(H)$
without the identification having been declared.

---

### P33 — Statement-proof domain mismatch: lemma statement must cover the full domain used by proof and downstream

When a proof establishes a result for a **broader domain** than the lemma statement claims
(e.g., proof uses only the fact that entries are distinct positive reals, but statement
restricts to positive rationals), and downstream theorems use the result over the broader
domain, the statement must be upgraded to match.

Additionally: if downstream usage relies on **connectivity** of the domain (e.g., for
analytic continuation, an implicit function theorem application, or "$\Omega$ is connected"
to conclude that a zero-set is isolated), that connectivity must be stated as an explicit
hypothesis or conclusion in the lemma, not left implicit.

```bash
# Step 1: Find every lemma whose proof contains a domain-relevant word
grep -n '\\begin{lemma}\|\\begin{proposition}' "$TEX" | while IFS=: read lineno rest; do
  # Look in the 40 lines of proof following this lemma
  proof=$(sed -n "${lineno},$((lineno+40))p" "$TEX")
  echo "$proof" | grep -qi 'real\|positive real\|\\mathbb{R}\|distinct.*real' && \
    echo "Line $lineno: proof mentions real — check statement domain"
done
# Step 2: Find downstream uses outside the lemma that reference its name
grep -n 'Lemma.*[0-9]\.' "$TEX" | grep -v '\\begin{lemma}\|\\begin{proof}' | head -20
```

**Manual check:** for each flagged lemma, (a) read the proof and record the actual domain
used; (b) read the statement and record the claimed domain; (c) find every downstream
`\ref` site; (d) check the downstream site requires the actual (broader) domain;
(e) if yes, upgrade the statement.  Also verify the domain is explicitly stated as
connected wherever a connectivity argument is used.

**Precedent (paper-A):** Lemma 3.1 stated for positive rationals; proof only needed distinct
positive reals; lines 895–908 used it over the open real set $\Omega$.  The "Vandermonde is
real" argument was complete — only the statement was too narrow.

---

### P34 — Spectral/counting definition domain covers every operator sub-class that uses it

When formal spectral invariants $(N_H, Z_H, \operatorname{spec}_\times(H),$ heat trace, etc.)
are defined for a **restricted operator class** (e.g.\ non-negative, or positive-definite),
verify that **every** operator appearing in a theorem that invokes those invariants provably
belongs to that restricted class — or extend the definition to a broader class (e.g.\
lower-semibounded with finitely many negative eigenvalues) and state the extension explicitly.

```bash
# Find all definitions of spectral invariants
grep -n 'N_H\|Z_H\|\\operatorname{spec}_\\times\|\\operatorname{spec}' "$TEX" \
  | grep '\\begin{definition}\|:=\|\\coloneqq' | head -20
# Find all operator classes in definitions / theorem statements
grep -n '\\mathcal{C}\|\\mathcal{H}\|H_F\|\\Csub\|lower.semibounded\|semi.*bound' "$TEX" | head -20
```

**Manual check:** (a) read the definition block that introduces each spectral invariant and
record the stated domain of $H$; (b) for each theorem using that invariant, identify the
operator class $\mathcal{C}$; (c) verify $\mathcal{C}$ satisfies the domain restriction.
If $\mathcal{C}$ admits finitely many negative eigenvalues but the definition requires
non-negativity, add a sentence:

> For any lower-semibounded self-adjoint operator with compact resolvent, list its
> eigenvalues $\lambda_1 \le \lambda_2 \le \cdots$ with multiplicity and apply the
> same definitions of $N_H$ and $Z_H$.

**Precedent (paper-B):** $N_H$, $Z_H$, $\operatorname{spec}_\times(H)$ defined for
non-negative $H$; but $H_F\in\mathcal{C}_\mathrm{sub}$ can have finitely many negative
eigenvalues.  Finite negative spectrum does not affect the asymptotic conclusion, but the
definition must explicitly permit it.

---

### P35 — Parameterized class superscripts re-quantified in dependent theorems; local symbol constants localized

**Part A — parameter re-quantification.**
When a definition introduces a class with superscript/subscript parameters
(e.g.\ $\mathcal{C}_\mathrm{sub}^{m,K}(M)$), every theorem or corollary that produces or
asserts membership in the class must either (a) universally quantify all parameters
("for all $m\ge 1$, $K\ge 1$, $M$ compact without boundary…") or (b) reference a fixed
previously-named instance.  A theorem header that drops the superscripts leaves the
parameters ambiguous.

```bash
# Find class names with potential superscripts used in theorem/corollary blocks
grep -n '\\begin{\(theorem\|corollary\|proposition\)}' "$TEX" | while IFS=: read L _; do
  window=$(sed -n "${L},$((L+10))p" "$TEX")
  echo "$window" | grep -qE '\\mathcal\{C\}|\\mathcal\{H\}|\\Csub' && \
    echo "Line $L: check class parameters are re-quantified"
done
```

**Part B — local vs global symbol constants.**
Symbol/PDE estimates of the form $|(\partial^\alpha_x\partial^\beta_\xi a)(x,\xi)| \le C_{\alpha\beta}$
are valid only locally when the symbol $a$ is defined on a coordinate patch $U$.  The
constant must be written $C_{\alpha\beta,U_0}$ for every $U_0 \Subset U$, not a single
global constant, unless the manifold is compact and the operator is globally defined.

```bash
grep -n 'C_{\\\\\alpha\|C_\\alpha\|symbol.*estimate\|uniform.*bound.*symbol' "$TEX"
```

**Manual check (Part B):** for each symbol estimate, verify whether $a(x,\xi)$ is defined
on a coordinate patch or globally; if on a patch, confirm the bound writes $C_{\alpha\beta,U_0}$
and states "$U_0\Subset U$."

**Precedent (paper-B):** $\mathcal{C}_\mathrm{sub}$ used in Theorem D$'$ without
re-quantifying $m,K,M$; local symbol estimate wrote $C_{\alpha\beta}$ for a
coordinate-patch symbol.

---

### P36 — Existence vs construction: citation qualifier when a specific object is needed

When a theorem has an **existence conclusion** (proved by compactness, contradiction, or a
non-constructive fixed-point argument) but a downstream proof uses a **specific object**
produced by that theorem (e.g.\ a particular sequence of parameters, a specific certificate,
or an explicit formula from the construction), the citation must be qualified:

> By **the construction in the proof of** Theorem~X (equivalently, equation~$(\star)$), …

A bare "By Theorem~X" in that context implies only that some object with the stated
properties exists, not that the downstream argument has access to a particular one.

```bash
# Find all bare "By Theorem" / "by Theorem" citations not followed by "proof" or "construction"
grep -n 'By Theorem\|by Theorem\|By Corollary\|by Corollary' "$TEX" \
  | grep -v 'proof\|construction\|equation\|formula' | head -30
```

**Manual check:** for each hit, determine whether the downstream argument uses only the
*existence* of an object or whether it relies on a *specific* object produced by the proof.
If the latter, add "the construction in the proof of" or cite the specific equation.

**Precedent (paper-A):** line 922 cited "By Theorem~A" but needed the specific parameters
from the Theorem~A construction (equation $(\star)$); the existence statement alone did not
supply those parameters.

---

### P37 — Degenerate-parameter case convention explicit in counting/combinatorial formulas

When a counting lemma, quartet asymptotic, or combinatorial observation formula admits a
**degenerate parameter value** where the geometric object collapses or a multiplicity changes
(e.g.\ $\sigma_0=1/2$ makes a four-point orbit collapse to two on-line points each appearing
with multiplicity~2; $h=0$ makes a test trivial), the multiset interpretation and the
resulting formula for that special case must be stated **explicitly** — either in the theorem
as an additional case, or in an immediately adjacent remark.

```bash
# Find "quartet" / "Q(" / "L(T)" and orbit formulas
grep -n 'quartet\|Q(1/2\|\\sigma_0=1/2\|degenerate\|\\sigma_0\\ne 1/2' "$TEX" | head -20
# Find formulas that use a parameter that could be zero or a boundary value
grep -n 'multiset\|orbit.*multiplicity\|with multiplicity\|counted with' "$TEX" | head -20
```

**Manual check:** for each counting formula, list all parameter boundary values allowed by
the stated domain; for each boundary value, work out what the formula gives and whether
that agrees with the geometric meaning.  If a special case needs a separate sub-formula or
a "multisets" qualifier, add it.

**Precedent (paper-A):** $Q(\sigma_0,T)$ for $\sigma_0=1/2$ collapses to two on-line points
with multiplicity~2 each, giving $Q(1/2,T)=2L(T)$; this was not stated, leaving the
multiplicity convention ambiguous.

---

### P38 — Self-adjointness inner product named at every invocation

When a theorem asserts, or cites a result asserting, that an operator is **self-adjoint**,
the **inner product** on which self-adjointness holds must be named — especially when a
non-standard inner product (e.g.\ Weil quadratic form, Sobolev form, graph inner product)
is in use.  A bare "is self-adjoint on $\mathcal{H}$" is incomplete if $\mathcal{H}$ can
be equipped with more than one natural inner product.

```bash
grep -n 'self-adjoint\|self.adjoint\|hermitian\|symmetric.*operator' "$TEX" | head -30
```

**Manual check:** for each hit, identify the inner product in force.  If the inner product
is not the standard $L^2$ inner product, verify the text names it.  For cited results
(e.g.\ CCM Theorem 5.10), open the source and confirm the inner product used in the
citation matches the inner product used in the paper.

**Precedent (paper-B):** CCM Theorem 5.10 asserts self-adjointness on $E_N'\oplus E_N^\perp$
equipped with the **Weil quadratic form-induced inner product**, not the standard $L^2$
inner product; the description omitted this, making "self-adjoint" ambiguous.

---

## Running order for pre-submission

1. `pdflatex` — fix all errors and undefined-ref warnings (P4)
2. Hardcoded refs grep → convert to `\ref` (P1)
3. Unused labels grep → add `\ref` or remove (P2)
4. Unused bibliography grep (P3)
5. Short title check (P5)
6. Unused results grep (P6)
7. Definition consistency grep for each key term (P7)
8. Attribution grep for each lemma block (P8)
9. Asymptotics grep → point to or run verifying scripts (P9)
10. Informal qualifiers grep (P10)
11. Remark formula audit (P11) — verify every inequality/identity claimed, not just display
12. Barrier criterion grep (P12–P13)
13. Abstract/intro scope read (P14)
14. Complexity analogy grep (P15)
15. Evidence-level audit of proof citations (P16–P17)
16. Constructive/existential qualifier consistency (P18)
17. Parity arguments to sufficient order (P19)
18. Strong number-theoretic assertions (P20)
19. Analogy claim refutation check (P21)
20. External theorem parameter instantiation (P22)
21. **Statement-proof domain mismatch — statement ≥ proof domain (P33)**
22. Operator definition prerequisite ordering (P23)
23. **Spectral definition domain covers all operator sub-classes (P34)**
24. Literature formula descriptions vs source (P25)
25. Optional theorem title duplication (P24)
26. Reference operator symbol class (P26)
27. **Parameterized class superscripts re-quantified; local symbol constants (P35)**
28. **Existence vs construction citation qualifier (P36)**
29. Tauberian theorems used bidirectionally (P27)
30. Single-letter symbol conflicts (P28)
31. `\texorpdfstring` bookmark semantic correctness (P29)
32. Free variable binding in theorem statements (P30)
33. "Same argument" conclusion completeness (P31)
34. Friedrichs realization identification after definition (P32)
35. **Degenerate-parameter case convention in counting formulas (P37)**
36. **Self-adjointness inner product named at invocation (P38)**
