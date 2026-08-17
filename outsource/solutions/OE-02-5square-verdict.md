# OE-02 Verdict — corrected internal record

**Date:** 2026-08-17
**Status:** REPAIRED PROOF-DRAFT
**Mathematical:** PROOF-DRAFT
**Computational:** INDEPENDENT-CHECKER for rank/torsion and exact map identities

---

## Verdict

The original external Gaussian-integer solution is **not accepted as written**.
A toy normalization audit found that it dropped the factor `5` when dividing the
two norm equations by `n²`. The corrected internal route below replaces it.

The corrected claim remains: there is no Row-3 pair `(a,n)` with `4∤n` satisfying
both `A⁺=5S²` and `A⁻=5T²`.

## Corrected reduction

Let `b=n-a`, `x=b/n`, `r=T/n`, and `s=S/n`. Then

```
x²+1=5r²,
x²-2x+2=5s².
```

Parametrizing the first 5-conic from `(2,1)` gives

```
x=2(5t²-5t+1)/(5t²-1),
r=-(5t²-4t+1)/(5t²-1).
```

Writing `Y=(5t²-1)s`, the second conic gives

```
Y²=10t⁴-20t³+24t²-12t+2.
```

After `u=t-1`, `v=Y`, an explicit birational map to `E:y²=x³-32x+64` is

```
A=v+2+4u+2u²,
B=v(1+u)+2+6u+6u²,
x_E=4A/u²,
y_E=16B/u³+40.
```

The inverse is

```
u=-4x_E/(4x_E-y_E+8),
v=2(2x_E³-y_E²+16y_E-64)/(4x_E-y_E+8)²,
t=1+u.
```

Both polynomial identities are replayed by
`theorems/M-row3-square-powerful-complete/checker/verify_OE02_quartic_map.py`.

## CAS replay

PARI/GP 2.17.4 returns certified rank bounds `[0,0]` on:

1. `E:y²=x³-32x+64`;
2. the translated 2-torsion model;
3. the 2-isogenous model;
4. the Jacobian `[0,24,0,160,320]` returned by `ellfromeqn` from the corrected quartic.

The torsion subgroup of `E` is cyclic of order 4. The four torsion pullbacks are

```
(t,Y)=(1,2), (1/3,2/9), (1,-2), (1/3,-2/9).
```

Each gives `x=1/2`, hence `a=n/2`; `gcd(a,n)=1` forces `n=2`, contradicting
`n≥4`.

## Evidence boundary

This repairs the external solution's normalization defect, but does not close
Gate A. Independent human review must inspect the corrected 5-conic reduction,
the birational identities, and the use of the rank-zero computation. The finite
computational replay cannot promote the analytic theorem by itself.
