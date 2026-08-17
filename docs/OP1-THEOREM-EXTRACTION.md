# OP1 theorem extraction plan

**Purpose.** Separate the genuinely theorem-level OP1 fragments from the discovery
attack log, without treating a promising reduction or a finite search as a proof.
All full-OP1 claims remain open until their packages pass Gate-A.

## Extracted proof-draft packages

| Package | Content | Why it is safe to package | Non-claim |
|---|---|---|---|
| `theorems/J-li-collision-lattice-floor` | Exact off-line coefficient divisor `q_min` as a lattice index / determinantal-divisor ratio | Self-contained integer linear algebra; no unproved arithmetic-growth assumption | Does not bound the infimum over all constructions |
| `theorems/K-li-inert-prime-floor` | Exponential floor for off-line data with an inert prime `p=3 mod 4` in a Chebyshev denominator | Uniform p-integrality of rational on-line conductors plus a Chebyshev p-adic pole | Does not cover split-only denominators |

Both packages are `PROOF-DRAFT / EXPLORATORY` and Gate-A OPEN. Their exact finite
checkers are sanity replays, not theorem certificates.

## Candidate fragments requiring consolidation before theorem packages

1. **p=3 consecutive-node floor.** Discovery §6co states a single-prime
   `v_3(q_min) ≥ m/2-O(1)` for an explicit orbit family. A theorem package must
   first consolidate the moment-residue formula, cluster bound, and coupling lemma
   into one self-contained proof. Do not import the discovery section as a premise.

2. **p=2 / odd-carrier floors.** Discovery §6cp–§6cr contains strong partial
   mechanisms and exact checks, but the carrier-existence and powerful-value lemmas
   remain open. Package only a fully stated conditional theorem or a smaller
   unconditional subfamily.

3. **Determinantal rank-count floor.** Discovery §6g states a linear floor for the
   top Smith invariant of the on-line matrix. A package must distinguish this from
   the still-open fixed-vector transfer to `q_min`.

4. **OB-44.** The original combined prompt is superseded by two focused sends:
   `OB-44A-OP1-powerful-binary-quartic.md` (pure powerful-values core) and
   `OB-44B-OP1-poisoned-carrier-aggregate-floor.md` (CRT node-poisoning and
   aggregate floor). Neither has a returned solution, so neither promotes OP1.

## External-review status

- OB-41 was externally **REFUTED**, and the counterexample was replayed exactly.
  This invalidated one intermediate incidence-lag claim, not the whole OP1 program.
- No `outsource/solutions/OB-44-*` verdict exists in the repository.
- Therefore any positive external assessment of OP1's importance or reduction is not
  evidence that full OP1 is solved.

## Paper policy

Paper A v2 may describe `q_min` as a quantitative invariant and state the proved
Gaussian no-collision theorem, but it must present full OP1 as open. A dedicated
arithmetic-complexity paper should wait until at least J and K (and preferably one
consolidated p-adic floor) have passed independent whole-theorem review.

## Current external-send policy

Only two paid OP1 sends are currently justified:

1. `outsource/OB-44A-OP1-powerful-binary-quartic.md`
2. `outsource/OB-44B-OP1-poisoned-carrier-aggregate-floor.md`

The original combined `OB-44` prompt is retained for provenance but marked
superseded. OB-42 and OB-43 are held until revised against the newer OP1 state.
The OP2 compact-support question is not yet sent because no sharp, self-contained
arithmetic class of `C_c^∞` test functions has been frozen; calling all Paley--Wiener
values periods without such a class would be an unjustified convention.

## 2026-08-17 OB-44A structural reduction

The quartic factors exactly as

```
N=(a²+n²)((a−n)²+n²)=|a+ni|² |(a−n)+ni|².
```

The two rational factors have gcd `1` or `5`. Thus a powerful `N` requires both
factors to be powerful away from `5`. This simultaneous-shift Gaussian formulation
is now the preferred internal target and is incorporated into OB-44A. A deposited
exact scan through `n<5000` found no powerful `N` and no simultaneous
powerful-away-from-5 pair.

## 2026-08-17 OB-44B rectangular-node correction

The full relation size, not `q_min`, is the resource-bounded quantity. For the
Row-3 anchor `(a,n)=(1,10)`:

```
(t_1,t_2)=(19286,26164):
    q_min=18, v_101(q_min)=v_181(q_min)=0,
    relation sup-norm=3292056116081922725.

(t_1,t_2,t_3)=(1005,7883,-10398), m=2, K=3:
    q_min=1, v_101(q_min)=v_181(q_min)=0,
    relation sup-norm=16156893919328.
```

Thus every node poisons both simple carriers, and with one extra node the
`q_min`-only floor disappears. OB-44B therefore targets the full integer
relation size and allows `K≥m`.

## 2026-08-17 publication override

Paper A v2 is draft-only. Do not submit or deposit it while OP1-A/OP1-B and OP2-B
remain open. The Gaussian theorem may be retained in the draft, but publication is
blocked until its normalization audit and Gate-A review are complete.
