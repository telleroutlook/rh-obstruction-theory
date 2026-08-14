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
11. Remark formula audit (P11)
12. Barrier criterion grep (P12–P13)
13. Abstract/intro scope read (P14)
14. Complexity analogy grep (P15)
15. Evidence-level audit of proof citations (P16–P17)
