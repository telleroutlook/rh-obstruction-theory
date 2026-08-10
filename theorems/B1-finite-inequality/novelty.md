# Novelty — Theorem B1

**Theorem ID:** B1-finite-inequality  
**Program ref:** §7.B, §9.D.5, §14.3

This file maps B1 against the closest prior theorems to identify the genuine delta.

---

## Closest prior results

### 1. Báez-Duarte / Burnol (NB approximation lower bounds)

**What they prove:** The Nyman–Beurling approximation error `inf_{f ∈ V_n} ‖1_{(0,1)} − f‖²`
has a lower bound of order `1/√log n`, with the tight asymptotics depending on
the distribution of zeta zeros (Burnol 2002, Báez-Duarte 2002/03).

**How it compares:** These results show that the NB approximation does not converge
to zero faster than `1/√log n` — equivalently, the RH-equivalent Li criterion
encodes difficulty at the asymptotic level.  They do NOT construct an off-line
zero multiset satisfying the first `K` Li inequalities.  They operate in a Hilbert
space norm, not via a combinatorial zero-set construction.

**Delta:** B1 is strictly weaker asymptotically (fixed `K`, not asymptotics) but
genuinely complementary: it constructs an explicit off-line `𝒵_−` in the
symmetric-zero ambient class that passes the first `K` strict positivity
conditions.  The question B1 answers — "can the first `K` Li tests fail to
discriminate?" — is not the same as "what is the rate of NB approximation?"

**Risk:** B1 at fixed `K` may be viewed as already known (implicit in Li/Voros
context), in which case B1 is published only as a lemma of Paper C, not a
standalone theorem.  This risk is acknowledged in PLAN.md (Paper A note).

### 2. Voros (Li coefficient asymptotics for off-line zeros)

**What they prove:** Off-line zeros produce a different asymptotic regime for
`λ_j` at large `j`; the sign pattern differs from the on-line case.

**How it compares:** Voros shows that a *full* off-line zero set is distinguishable
by the *infinite* Li sequence.  B1 shows a *single* off-line quartet is
indistinguishable from an on-line configuration by any *finite* initial segment.
These are consistent and complementary.

**Delta:** B1 provides the constructive finite-`K` side; Voros provides the
asymptotic infinite side.

### 3. Internal P21 (Hausdorff non-discrimination, LEGACY, PENDING Gate A)

**What it claims:** Fixed-order Hausdorff/Stieltjes moment differences cannot
distinguish on-line from off-line multisets.

**How it compares:** P21 is the closest analogue.  If P21 were Gate-A-cleared, B1
would largely overlap with it.

**Delta:** B1 is stated in the current `𝔛_sym` framework with explicit notation,
an analytic proof not relying on any private result, and the W2/W1 convention
distinction spelled out.  Until P21 passes Gate A, B1 is the primary analytic
record.  After Gate A review, if P21 is independent and compatible, B1 may be
merged with it or cited as a restatement.

### 4. Endres–Steiner (Weyl mismatch for Berry–Keating)

Not relevant to B1 (different theorem family: spectral/asymptotic, not
finite-observable).

---

## Verdict

| Prior result | Does it imply B1? | B1 delta |
|---|---|---|
| Báez-Duarte/Burnol | No (asymptotics ≠ finite K construction) | Constructive, fixed K |
| Voros | No (infinite Li ≠ finite K) | Finite K complementary side |
| P21 (LEGACY PENDING) | Possibly overlaps | Needs Gate A before judgment |
| None of the above | — | B1 is modestly new, conditional on P21 not clearing |

**Publication strategy:** B1 is not a standalone paper.  It is:
- a **lemma** supporting Paper A if B2 (exact collision) closes;
- a **checklist item** for Paper C (convergence obligations) regardless;
- publishable as a **reference note** if neither A nor C proceeds.

The LITERATURE_MATRIX.md correctly labels this as **THIN** at B1 level.
