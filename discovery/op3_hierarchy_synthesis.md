# OP3 synthesis — the observation-hierarchy separation level is governed by the ARITHMETIC of the encoding

**Tier:** DISCOVERY / SYNTHESIS. This is a *conceptual synthesis of already-proved results*
(Theorem A, Theorem B, and the OP2 Lindemann–Weierstrass note), **not** a new standalone theorem.
Proved vs. open is marked explicitly below. RH stays `[OUT]`.

Paper A, Open Problem 3: is there a natural sequence of observations `O_1 ⪯ O_2 ⪯ … → O_oracle`
(the identity `O_oracle(Z)=Z`), and **at what level does the chain separate `P=1` from `P=0`?**
The OP1 and OP2 results together answer this along two orthogonal axes.

## Axis 1 — refine WITHIN the rational Li encoding (quantitative)

- **Unbounded (proved).** For every finite `m`, `O_fin^{(m)}` (first `m` Li tests) admits an exact
  collision `Z_+ ≠ Z_-` with `P(Z_+)=1, P(Z_-)=0` (Theorem A: `Cn + Rq(T)=0`, `C ∈ Q^{m×m}`
  nonsingular ⟹ integer witness with denominator `R`). Theorem B: no fixed finite prefix separates.
  So the *unbounded* Li chain **never separates at finite `m`** — only the oracle limit does.
- **Resource-bounded (OP1, partial).** The collision witness has a minimal complexity
  `q_min(m)` (the least admissible denominator/`R`, equivalently the lattice index of §6ao/§6cs).
  For an observer/configuration constrained to denominator or atom-height budget `≤ H`, the collision
  **no longer fits** once `q_min(m) > H`. Hence the *bounded* Li chain **separates at level `m*`
  where `q_min(m*) > H`.** The odd-carrier result (OB-44) gives `q_min ≥ p^{…}` growing with the
  carrier (log `q_min = Ω(m)` on that family), so under a polynomial budget `H = T^A` the bounded
  chain separates at a finite, computable level. Whether `q_min` grows *uniformly* (all admissible
  parameter families) is the open core of OP1 — reduces to the purely rational lemma
  "`N=(a²+n²−na)²+n⁴` is never a powerful integer" (see [[op1_arithmetic_floor_findings]], OB-44).

## Axis 2 — switch the ENCODING to Weil observations (arithmetic)

- **Analytic / Schwartz-dense family (OP2, proved).** For `ĥ = P·e^{−a z²}` (algebraic data), the
  observation values are `(algebraic)·exp(distinct algebraic exponent)`, so Lindemann–Weierstrass
  forbids **any** nontrivial integer collision. The chain therefore **separates immediately (level 1):
  no collision exists at all.** (Only genuine `C_c^∞` / Paley–Wiener periods stay open.) See
  `op2_weil_rationality_findings.md`.

## The unifying picture

The barrier's robustness is controlled by the **arithmetic of the observation encoding**, not by the
sheer amount of data:

| encoding | collision exists? | hierarchy separates `P` at… |
|---|---|---|
| rational Li, unbounded | **yes, every `m`** (Thm A) | only the oracle limit (Thm B) |
| rational Li, budget `H` | yes iff `q_min(m) ≤ H` | level `m*`: `q_min(m*) > H` (OP1) |
| Weil `P·Gaussian`, alg. data | **no** (Lindemann–Weierstrass) | level 1 — immediately (OP2) |

So OP3's "separation level" is **`min(m* , 1_{encoding is arithmetically independent})`**: either the
resource first exceeds the collision complexity `q_min` (OP1 axis), or the encoding is switched to one
whose values are algebraically independent, killing collisions outright (OP2 axis). More Li data never
separates (unbounded); a tighter budget or a richer encoding does. **The exact information barrier is
a rationality phenomenon of the Li encoding.**

**Honesty markers.** Proved: Thm A, Thm B (paper); OP2 no-collision for the Schwartz-dense class
(L–W, referee-verified). Open: uniform `q_min` growth (OP1 core = binary-quartic powerful-number
lemma, outsourced as OB-44); the `C_c^∞` Weil case (period arithmetic). This table is a *map of what
is and isn't established*, not a claim that OP3 is resolved. RH stays `[OUT]`.
