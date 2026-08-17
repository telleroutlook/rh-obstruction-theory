# Limitations of Theorem M

## What is proved

Theorem M proves: for every Row-3 pair (a,n), it is impossible that both
A⁺ = a²+n² and A⁻ = (n−a)²+n² are simultaneously square-based powerful-away-from-5
(i.e., of the form 5^e·m²).

For the 4|n sub-family, odd exponents e are impossible individually, and the
remaining simultaneous even-exponent case is excluded. Individual even-e
representations remain possible.

## What is NOT proved

### M1 — Cube-factor powerful case (NT-C full) remains open

Theorem M handles only t=1 (square-only) powerful numbers. The full NT-C claim
requires excluding t≥2 (cube-factor powerful: s²t³ with t>1). The growing-S
Evertse obstacle from OE-01 has not been circumvented.

### M2 — Does not prove OP1-A

OP1-A asks: is N = A⁺·A⁻ ever powerful? Theorem M rules out the t=1 case for
both A⁺ and A⁻ simultaneously, strengthening the NT-C partial results. But full
NT-C (t≥2) would also be needed to conclude OP1-A.

### M3 — No individual-square exclusion for 4|n

For `4|n`, odd `e` is individually impossible by the mod-8/16 obstruction, but
individual even `e` is not excluded. Indeed, the Row-3 pair `(a,n)=(15,8)` has
`A⁺=15²+8²=17²` (an `e=0` individual square), while `A⁻=113`. Theorem M claims
only that both `A⁺` and `A⁻` cannot simultaneously be square-based powerful.

## Summary table

| Claim | Status |
|---|---|
| t=1 case of NT-C, 4\|n (Theorem M/E part i) | PROOF-DRAFT (elementary mod 8/16 + Theorem L) |
| t=1 case of NT-C, 4∤n — (5□,5□) case (Theorem M/E part ii) | PROOF-DRAFT (direct 5-conic reduction to E: Y²=X³−32X+64; PARI/GP rank/torsion replay complete) |
| t=1 case of NT-C complete | PROOF-DRAFT (both sub-families covered) |
| t≥2 case of NT-C (cube factors) | OPEN — via OE-01 |
| OP1-A (N not powerful) | OPEN — requires full NT-C |
