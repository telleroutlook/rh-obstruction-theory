# DISCOVERY TIER — conjecture / evidence only.  NOT a proof, NOT a witness.
# Never imported into proof steps or theorem statements.
#
# Probe log for Paper A **Open Problem 1** (arithmetic-information-barriers-rh.tex:1067):
#   resource-bounded finite Li-observation barrier.
# Scripts: probe_resource_bounded_collision.py, probe_overdetermined_collision.py

## Question

Theorem A gives EXACT Li-collisions Z_+ (P=1) / Z_- (P=0) matching Li_1..Li_m.
Open Problem 1 asks: does such a collision survive a POLYNOMIAL size budget
#Z <= T^A (total atom count OR denominator height) as the number of matched
observations K=K(T)=m grows?

Collision size is governed by  M = max|n_k|  and  R = |q|  (off-line multiplicity),
with #Z ~ 2 m M.  A collision matching the first m Li-observations is exactly an
INTEGER linear relation among the on-line building-block vectors
b(t_k) = (C_1(t_k),...,C_m(t_k)),  C_j(t)=4(1-T_j(x)),  x=(4t^2-1)/(4t^2+1),
and the off-line quartet vector d = O(Q):   sum_k n_k b(t_k) + q d = 0,  q != 0.

## Findings (all exact rational; LLL used only to FIND short relations)

1. STANDARD (rigid, m nodes = m equations) construction: super-polynomial.
   log2 M grows ~ c*m*log m  (M: 1.4e4 at m=2  ->  1.1e62 at m=11).
   Calibrated against the certified anchor (m=2 -> R=6375, M=14518: PASS).

2. OVER-DETERMINED (K>m nodes) construction: over-determination REDUCES size a
   lot, but an exponential FLOOR persists.  For m=4, adding nodes drives the
   shortest relation from 2^38 down to a hard floor 2^21.56 (reached at K=11,
   stable through K=16).  m=6 still descending at K=12 (2^59.5); floor ~ 2^{5.4 m}.

3. OFF-LINE PLACEMENT sweep (m=4, fixed good node set): the floor is ROBUST.
   Minimum is at small-denominator, moderate-height quartets (sigma=3/4,tau=1
   -> 2^21.56 ; sigma=5/6,tau=1/2 -> 2^21.60).  EVERY other placement is worse:
   large height tau (tau=10 -> 2^91), or real part near 1/2 with large
   denominator (sigma=51/100 -> 2^121).  No off-line choice escapes the floor.

## Mechanism (partially provable; identified via the boundedness contrast)

* ON-LINE atoms rho=1/2+it satisfy  |1 - 1/rho| = |rho-1|/|rho| = 1  EXACTLY
  (since |rho-1| = |-1/2+it| = |1/2+it| = |rho|).  Hence C_j(t)=4(1-T_j(x)) is
  BOUNDED: |x|<=1 => |T_j(x)|<=1 => C_j in [0,8], for ALL j.   [verified exactly]
* OFF-LINE atoms (Re != 1/2) have |1 - 1/rho| != 1, so the off-line observation
  d_j = 8 - sum_rho (1-1/rho)^j  has an ENVELOPE growing like gamma^j,
  gamma = max_rho |1-1/rho| > 1, times a cosine oscillation cos(j*theta).

=> Bounding inequality (SOUND, verified on real collisions):
     8 * sum|n_k|  >=  |q| * max_{j<=m} |d_j|.
   For a FIXED off-line configuration with gamma>1, the envelope gives
     sum|n_k|  >=  c_gamma * gamma^m   — SUPER-POLYNOMIAL in m.
   This is a clean, elementary, PROVABLE barrier for the fixed-target case:
   no fixed off-line multiset can be Li-confused with an on-line one using
   sub-exponentially many atoms.  (Complementary to Theorem A, which only
   shows a collision of SOME size exists.)

## Why the FULL Open Problem 1 is hard (honest limitation — do not overclaim)

The archimedean bound is QUANTITATIVELY WEAK and defeatable:
* max|d_j| SATURATES (~17.6 for sigma=3/4,tau=1) because gamma=1.213 is close to
  1; the OBSERVED exponential floor (sum|n_k| ~ gamma^{~50 m}) is driven by the
  ARITHMETIC (denominator) channel, NOT the archimedean one.
* The adversary can push gamma -> 1 by taking the off-line height tau large
  (exactly Theorem B's move) — but large tau inflates d_j's denominators, so the
  ARITHMETIC channel then bites (tau=10 -> 2^91).
=> Open Problem 1 is a genuine TWO-CHANNEL lower bound: archimedean cost when the
   off-line atom is near the critical line, arithmetic (denominator) cost when it
   is far out.  Proving that NEITHER can be made small SIMULTANEOUSLY, over ALL
   node sets and ALL off-line configurations, is the real (hard) content.  The
   probes give strong evidence the floor is exponential, but no proof over all
   constructions.

## Status

* CLEAN PROVABLE nugget: fixed-off-line-target => exponential (gamma^m) collision
  size, via on-line boundedness vs off-line geometric growth.  A genuine new
  barrier theorem, modest scope.
* CONJECTURE + strong evidence: the exponential floor holds for ALL constructions
  (full Open Problem 1) — the moving-target / two-channel case remains OPEN.
* RH stays [OUT].  These are finite exact-arithmetic statements about explicit
  multisets; nothing here assumes or implies RH.
