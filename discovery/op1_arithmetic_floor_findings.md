# DISCOVERY TIER — conjecture / evidence only.  NOT a proof, NOT a witness.
# Never imported into proof steps or theorem statements.  No RH / RH-equivalent
# input; all objects are finite explicit multisets of complex rationals.
#
# Attack log for Paper A **Open Problem 1** (resource-bounded finite
# Li-observation barrier).  Supersedes the mechanism section of
# resource_bounded_barrier_findings.md with a SHARPER, CORRECTED picture.
# Scripts (discovery/):
#   verify_chebyshev_reformulation.py   — the change-of-variable + archimedean bd
#   probe_covolume_floor.py             — floor = kernel-lattice covolume
#   probe_qmin_snf.py                   — RIGOROUS exact floor |q| = q_min
#   probe_adversarial_qmin.py           — minimize q_min over constructions

## 0. Executive summary

The collision-size floor of Open Problem 1 has been reduced from an analytic
information-barrier question to a **finite, RH-free, arithmetic-geometry**
statement, and a **rigorous per-node-family exponential lower bound** is proved.

  * **Reformulation (EXACT, verified).**  With w = 1 - 1/rho and u = (w+1/w)/2,
    the reflection rho -> 1-rho is w -> 1/w, ON-line <=> |w|=1 <=> u in [-1,1],
    and the Li-observation of an orbit is
            O_j(orbit) = 8 (1 - Re T_j(u)),   T_j = Chebyshev.
    A collision (matching O_1..O_m) is therefore an INTEGER signed measure with
    VANISHING Chebyshev moments 0..m and at least one support point OFF [-1,1].

  * **Archimedean channel (RIGOROUS, but weak).**  Chebyshev extremal property:
            sum_online |c_k|  >=  |q| * |T_m(u*)|  >=  (1/2) |q| Gamma^m,
    Gamma = |u* + sqrt(u*^2 - 1)| > 1.  SOUND, but Gamma ~ 1.21 for a typical
    off-line orbit => |T_m(u*)| ~ 1: quantitatively cannot explain the observed
    ~10^19 floor.  The floor is NOT archimedean.

  * **Arithmetic channel (RIGOROUS lower bound on the off-line multiplicity).**
    Clearing denominators, the on-line value vectors are integer columns
    v_1,...,v_K in Z^m; the off-line orbit is an integer column v_off in Z^m.  A
    collision  sum_k c_k v_k + q v_off = 0  forces  q * v_off in L := colspan_Z.
    The minimal off-line multiplicity is the LATTICE INDEX
            q_min = [L + Z v_off : L] = D_m(A) / D_m([A | v_off]),
    where A is the m x K on-line matrix and D_m = gcd of m x m minors (r-th
    determinantal divisor = product of Smith invariants).  Hence, RIGOROUSLY,
            every order-m collision on this construction has |q| >= q_min,
            so its atom count >= 4 q_min  (a valid but possibly VACUOUS bound:
            q_min can be 1 for adversarial node sets -- see CAVEAT below).
    For the standard t_k = 1/2+i family, |q| = q_min EXACTLY (3 off-line configs,
    m<=6) and log2 q_min grows ~linearly => the |q| floor is exponential there.

  * **CAVEAT (correction, important).**  q_min bounds ONLY the off-line
    multiplicity |q|, NOT the on-line multiplicities c_k, hence NOT the full
    collision size by itself.  The TRUE size floor is the shortest nonzero
    integer relation with q != 0, i.e. lambda_1 of the kernel lattice
        Lambda = {(c,q) in Z^{K+1} : sum c_k v_k + q v_off = 0}  restricted to q!=0.
    Empirically (probe_covolume_floor.py) this lambda_1 ~ covol(Lambda)^{1/r}
    (balanced, exponential) for standard families, and is LARGER than q_min
    (online coeffs add size).  The adversary CAN drive q_min -> 1 (found q_min=1
    at m=2,3), so the q_min bound alone does NOT close OP1; whether the FULL
    size stays exponential under that same adversary is the real OP1 test
    (probe_adversarial_qmin_truesize.py).

## 1. What is now a THEOREM (rigorous, RH-free)

**Theorem (per-family off-line-multiplicity floor).**  Fix rational on-line nodes
t_1,...,t_K and a rational off-line orbit rho_0 = sigma_0 + i tau_0 (sigma_0 !=
1/2).  Let A_m be the m x K matrix of denominator-cleared on-line value vectors
and d_m the cleared off-line vector.  Then every order-m Li-collision that uses
exactly these on-line nodes and this off-line orbit has off-line multiplicity
divisible by
        q_min(m) = D_m(A_m) / D_m([A_m | d_m])
(the index [colspan_Z A_m + Z d_m : colspan_Z A_m]); consequently it contains at
least 4 q_min(m) atoms.

*Proof.*  The collision is an integer relation A_m c + q d_m = 0, so q d_m lies
in L = colspan_Z(A_m).  The set {q in Z : q d_m in L} = q_min(m) Z is the
annihilator of the class [d_m] in the cyclic group (L + Z d_m)/L, whose order is
the stated index; the determinantal-divisor formula for a subgroup index of
finitely generated free abelian groups gives q_min = D_m(A_m)/D_m([A_m|d_m]).
All steps are exact integer linear algebra. QED.

This is a genuine rigorous barrier where q_min is large (e.g. the t=1/2+i family,
where it is exponential and EXACTLY tight, |q|=q_min).  But it is NOT a proof of
OP1: for adversarial node sets q_min can be 1 (§0 caveat), making the bound
vacuous.  The reformulation lemma (§0) and this q_min identity are the two solid
new results; OP1 itself remains open (§2).

## 2. Reduction of FULL Open Problem 1 (the remaining open content)

Full OP1 (floor over ALL constructions) is now EXACTLY:
        Is   inf over all rational on-line node sets {t_k} and off-line orbits
             rho_0 of   q_min(m)   super-polynomial in m ?
a finite, purely arithmetic-geometry question about determinantal divisors of
Chebyshev-value matrices carrying the on-line conductors N_k = 4a^2+b^2 and the
off-line conductor.  NO analysis, NO L-function, NO RH.  This is a large
clarification: the analytic obstruction question is now a lattice-index bound.

Status of the reduction target: OPEN.  Evidence from probe_adversarial_qmin.py
(adversary minimizes q_min over K, node denominators, prime-matched conductors,
off-line placements) — see that script's output for whether min q_min stays
exponential (=> OP1 plausibly TRUE) or collapses to polynomial (=> OP1 FALSE).

## 6. Many-node loophole CLOSED: size >= q_min, K-independent (new, this session)

The one way OP1 could be FALSE was the archimedean loophole: the archimedean bound
(§0) controls only sum_k |c_k|, NOT max_k |c_k|, so a priori an adversary using
K >> m on-line nodes could spread the on-line mass thin (max|c_k| -> O(1)) while the
required sum|c_k| ~ Gamma^m is met, driving the collision SIZE = max(max|c_k|,|q|)
down to O(1).  This is now RULED OUT:

  size = max(max_k|c_k|, |q|)  >=  |q|  >=  q_min(A)      (rigorous, §1 theorem).

Since |q| >= q_min holds for EVERY collision on EVERY node set A, and q_min is an
exact lattice index, the many-node adversary can lower max|c_k| toward q_min but can
NEVER push |q| below q_min.  The size floor is therefore >= q_min INDEPENDENT of the
node count K.  The archimedean loophole cannot touch |q|.

Empirical confirmation (probe, this session):
  * FAR off-line orbit rho = 1 + (1/5)i (Gamma = 5.10, archimedean-strong, inert-free
    so §5 does NOT apply): growing K = 4,8,14,20,28,40 drives the LLL collision size
    down 1.39e7 -> 2.08e5 -> 928 -> 891 -> 580 -> 525, with q PINNED at |q| = 64
    throughout.  Size floors at |q| = q_min = 64, does NOT approach O(1).
  * min q_min over rich node pools (K up to m+15) for this orbit:
        m=2:4,  m=3:64,  m=4:32256,  m=5:3354624   (log2 2, 6, 14.98, 21.68) --
    exponential and K-robust (does not collapse as K grows).
  * NEAR-line escaped orbit rho = 2/5+4/5 i: large-K plateau size 16,128,129024,
    1032192 for m=2..5 (log2 4,7,16.98,19.98), also exponential, K-stable.

CONSEQUENCE (sharper reduction).  The full OP1 collision-SIZE floor over all
constructions equals inf_A q_min(A) up to the (K-independent, arithmetic) gap between
q_min and lambda_1; and since size >= q_min always, OP1 is TRUE as soon as
        inf over off-line orbits & node sets of q_min(m)   is super-polynomial.
The K quantifier (unbounded node count) is now provably IRRELEVANT to the |q| floor.
So OP1 reduces cleanly to a K-independent determinantal-divisor lower bound; the only
place q_min = 1 occurs is the boundary m = 2,3.  The open content is: prove
inf_A q_min(m) is exponential (or exhibit a construction with poly q_min at large m).

### 6a. Two distinct q_min-growth channels (new, this session) — §5 is only ONE of them

Pushing q_min on the FAR, inert-free-in-den(u_0) orbit rho = 1 + i/5 (fast SNF,
qmin_snf_fast.py, calibrated == the trusted gcd-of-minors qmin_index) over an
enriched node pool (BND scaled with m) gives, for m = 2..9:

    m :   q_min        log2   factorization
    2 :   4            2.00   2^2
    3 :   64           6.00   2^6
    4 :   4608         12.17  2^9 * 3^2
    5 :   258048       17.98  2^12 * 3^2 * 7
    6 :   258048       17.98  2^12 * 3^2 * 7        <- single-degree DIP (artifact)
    7 :   90832896     26.44  2^17 * 3^2 * 7 * 11
    8 :   274678677504 38.00  2^21 * 3^5 * 7^2 * 11
    9 :   2197429420032 41.00 2^24 * 3^5 * 7^2 * 11

Two things resolved here.

(i) PLATEAU SCARE = single-degree artifact, NOT softening.  The m=5==m=6==258048
flat spot (dlog2 = 0) looked like q_min might be bounded (which would make the
size >= q_min bound too weak for OP1).  It is a one-degree dip -- exactly the same
phenomenon as the j == 2 mod 4 trace-vanishing dips in §5 -- and growth resumes
hard immediately after: dlog2 = +8.46, +11.56 at m = 7, 8.  q_min is robustly
exponential through m = 9 (log2 rises ~linearly, slope ~5).  Enrichment LOWERS
q_min vs a sparse pool (m=4: 32256 -> 4608; m=5: 3.35e6 -> 258048) but it
STABILIZES (BND=14 == BND=20) and stays exponential.

(ii) The growth is driven by a SECOND channel, distinct from §5's unreachable
inert prime.  For this orbit den(u_0) has conductor D = 26 = 2 * 13 (verified:
|rho|^2 = 26/25, |rho-1|^2 = 1/25) -- so its ONLY denominator primes are 2 and 13.
Yet q_min's factorization is dominated by
   * the prime 2, with v_2(q_min) = 2,6,9,12,12,17,21,24 ~ 3m (the main exponential
     engine), and
   * inert primes 3, 7, 11 (all == 3 mod 4) that are NOT in den(u_0) at all.
Both are IMPOSSIBLE under §5's mechanism:
   - 2 is REACHABLE by on-line conductors N = 4a^2+b^2 (v_2(N)=3 at t=1/2, =2 at
     t=1/4, =3 at t=3/2, ...), so §5's on-line-p-integrality CRUX FAILS for p=2;
   - 3,7,11 are absent from den(u_0), so there is no §5 off-line pole to force them.
They enter q_min PURELY through the determinantal/Vandermonde structure of the
on-line Chebyshev-value matrix A_m (the lattice index D_m(A)/D_m([A|d]) picks up
prime powers from the covolume, independent of den(u_0)).

CONCLUSION (honest, L5 -- DISCOVERY tier, evidence not proof).  The §5 inert-prime
theorem is a rigorous handle on ONE channel; the dominant driver for the generic
(inert-free-in-den(u_0)) orbit is a separate LATTICE / determinant channel whose
signature is v_2(q_min) ~ 3m.  This is exactly why §6's inf_A q_min reduction is
the right target and §5 alone does not close OP1.  The concrete open sub-problem is
now sharp:  prove a rigorous lower bound v_2(D_m(A)/D_m([A|d])) >= c*m (or more
generally a covolume lower bound) from the Vandermonde/resultant structure of the
Chebyshev-value matrix -- a p=2 analogue of §5 but WITHOUT the unreachability crux
(which fails for 2), hence needing a genuinely different (determinantal, not
valuation-transfer) argument.  Probe: qmin_snf_fast.py (SNF, polynomial-time;
calibrated against qmin_index).

DECOMPOSITION (why the residual is linear).  Separating the ratio,
v_2(q_min) = v_2(D_m(A)) - v_2(D_m([A|d])).  For rho=1+i/5:
    v_2(D_m(A))     = 6,12,21,37,50,73,94,126   (m=2..9)  -- super-linear (~quadratic)
    v_2(D_m([A|d])) = 4, 6,12,25,38,56,73,102             -- super-linear (~quadratic)
    v_2(q_min)      = 2, 6, 9,12,12,17,21,24              -- LINEAR (~3m)
The quadratic determinantal BULK (from Chebyshev leading coeff 2^{m(m-1)/2} plus
even-conductor denominator clearing) cancels between numerator and denominator; the
LINEAR residual survives.  That linear residual is exactly what a rigorous argument
must lower-bound.

GENERALITY (two orbits, both inert-free in den(u_0)).  The v_2 ~ 3m engine is NOT
special to rho=1+i/5.  Near-line orbit rho = 2/5+4/5 i has conductor D = 4 = 2^2
(ONLY the prime 2 in den(u_0), no 13), and its q_min shows the identical signature:
    v_2(q_min) = 4,7,11,14,16,20  (m=2..7)  ~ 3m  (dominant engine)
    v_3(q_min) = 0,0, 2, 2, 2, 2            (small inert contribution)
    plus inert 7 (m>=5), 11 (m=7), again NOT in den(u_0).
So for BOTH sampled inert-free orbits the collision floor is carried by a
determinant-channel prime-2 valuation v_2(q_min) ~ 3m (robust empirical LAW), with
inert primes 3,7,11 as a secondary contribution -- confirming §5's mechanism is one
of (at least) two, and the generic driver is the p=2 determinant channel.

## 6b. On-line p-adic profile lemma + conditional covector bound (new; rigorous but PARTIAL)

Attacking the p=2 determinant channel of §6a produced ONE clean rigorous lemma and
ONE conditional theorem -- plus an honest boundary showing the hard core is a
HIGHER-order determinantal object my single covector does not reach.

**Lemma (on-line p-adic profile, node-CLASS-independent) [RIGOROUS, verified].**
For an on-line node t = a/b (primitive), C_j(t) = 8(1 - T_j(x_t)),
x_t = (4a^2-b^2)/(4a^2+b^2).  For b ODD write x_t = 1 - 2*eps, eps = b^2/N
(N = 4a^2+b^2), a 2-adic UNIT (N,b odd).  Since T_j(1)=1, T_j'(1)=j^2,
T_j''(1)=j^2(j^2-1)/3, and C_1(t) = 8(1-x_t) = 16*eps EXACTLY, one gets
        C_j(t)/C_1(t) = j^2 - (j^2(j^2-1)/3)*eps + O(eps^2).
eps being a unit, the valuation of the deviation is that of the leading integer
coefficient:
        v_2( C_j(t)/C_1(t) - j^2 ) = 2*v_2(j) + v_2(j^2-1),
INDEPENDENT of the node (only the 2-adic class beta = v_2(b) matters).  VERIFIED
exactly, 12 odd-b nodes, j<=10: profile 2,3,4,3,2,4,6,4,2 == formula.  Even-b nodes
are also class-only-dependent: beta=1 -> 1,3,4,3,1,4,6; beta=2 -> 4,5,6,5,4,6,8.
The SAME construction works for any prime p (profile phi_{p,beta}(j) >= 0).
CONSEQUENCE: the adversary has essentially NO p-adic freedom in the on-line
geometry -- swapping nodes cannot move the on-line value-vectors off the fixed
p-adic "(j^2)-parabola + node-independent corrections."  This is WHY inf_A q_min
has a node-independent floor.

**Theorem (conditional covector bound) [RIGOROUS].**  Normalise columns by their
j=1 entry: hat c(t)_j = C_j(t)/C_1(t), hat d_j = d_j/d_1.  A collision
sum_k c_k C_j(t_k) + q d_j = 0 gives, at j=1, Q := q*d_1 = -sum_k c_k C_1(t_k) =: sum
gamma_k; subtracting j^2 * (Q = sum gamma_k) yields coordinatewise
        Q ( hat d_j - j^2 ) = sum_k gamma_k ( hat c(t_k)_j - j^2 ).
Taking v_p and using v_p(gamma_k) >= v_p(C_1) and phi_{p,beta}(j) >= 0:
        v_p(q) >= v_p(C_1)_min + max_{j<=m} ( -delta_j^{(p)} ) - v_p(d_1),
        delta_j^{(p)} := v_p( d_j/d_1 - j^2 )   (off-line p-adic escape).
Hence: IF the off-line orbit has LINEAR p-adic escape -delta_j^{(p)} ~ c*j for some
prime p, then |q| >= p^{c*m}: EXPONENTIAL, UNIFORM over all on-line node sets.
VERIFIED sound: meas v_2(q_min) >= bound for all 5 orbits (no violation).  This
UNIFIES §5 (p inert in den(u_0): escape -delta_j = j*delta, linear) and a NEW p=2
case: orbit rho = 2/5+4/5 i has D = 4, and -delta_j^{(2)} = 0,1,2,3,4,5,6,7 = j-1
EXACTLY (clean linear) => v_2(q) >= m-1+O(1), rigorously exponential.

**HONEST BOUNDARY (L5) -- the bound is VALID but VACUOUS for all-split orbits.**
The single (j^2)-parabola covector does NOT explain the generic escaped orbit.
Orbit rho = 3/4 + i, D = 425 = 5^2 * 17 (ALL split), has q_min(m=8) = 130977 =
3^5 * 7^2 * 11 -- carried entirely by INERT primes 3,7,11 that are NOT in den(u_0)
at all, and whose escape -delta_j^{(p)} is ZERO or erratically NEGATIVE (p=7: all
zero yet v_7(q_min)=2; p=3: [0,-3,0,0,-1,0,-3,0] yet v_3(q_min)=5).  So the
conditional theorem's hypothesis FAILS for these primes, its lower bound is
<= 0 (vacuous), yet the true v_p(q_min) is positive and grows.  Meaning: the prime
powers here are generated by the HIGHER-ORDER determinantal / Vandermonde structure
(multi-row covectors beyond the rank-1 "deviation from j^2"), which the single
covector misses.  This is the exact, still-open hard core of OP1: a lower bound on
the FULL determinantal divisor D_m(A)/D_m([A|d]) that captures inert primes injected
by the on-line-conductor Vandermonde structure independently of den(u_0).

**Net (L5, DISCOVERY tier).**  New rigorous content: (i) the node-class-independent
on-line p-adic profile lemma; (ii) the conditional covector theorem, which closes
(uniformly, over all on-line sets) every off-line orbit possessing SOME prime with
linear p-adic escape -- unifying §5's inert-in-den(u_0) family with a new p=2 family.
Still OPEN: orbits whose q_min is carried purely by the higher determinantal channel
(inert primes NOT in den(u_0), zero/erratic escape), e.g. all-split D like 425.
The remaining quantifier "every off-line orbit has SOME prime with linear escape OR
a determinantal inert injection" is unproven; the covector method provably does not
reach the determinantal-injection case.

## 6c. Determinantal-injection channel: rigorous NUMERATOR floor (new, this session)

This attacks the exact case §6b left open: split-only off-line orbits (e.g. D=425)
where the single (j^2)-covector is VALID but VACUOUS, yet q_min still carries inert
primes 3,7,11 with ZERO den(u_0)-escape.  It is a genuine MULTI-ROW / Vandermonde
argument, not the rank-1 covector.  Probe: probe_determinantal_channel.py.

**Cross-difference identity (proved, sanity-checked True).**  For on-line nodes
t_k = a_k/b_k (primitive), x_{t} = (4t^2-1)/(4t^2+1) and N_k = 4a_k^2 + b_k^2:
        x_k - x_l = 8 (a_k b_l - a_l b_k)(a_k b_l + a_l b_k) / (N_k N_l).
For inert p == 3 mod 4, p never divides any N_k (else (2a/b)^2 == -1 mod p,
impossible), so all x_t are p-integral and depend only on t mod p.

**Rank-count lemma (RIGOROUS, tight) -- CORRECTED count (p+3)/2.**  The on-line nodes
realize EXACTLY (p+3)/2 distinct x-values mod p.  s = 4t^2 ranges over {squares} u {0}
= (p+1)/2 classes (4 is a square), the Mobius map x = (s-1)/(s+1) is injective there
(s = -1 is a non-residue for p == 3 mod4, so never hit), giving (p+1)/2 finite-s
x-values; and x == 1 IS reachable -- by t == infinity mod p, i.e. any node with p | b
(s = infinity) -- adding exactly ONE more class.  [EARLIER ERROR, corrected here per
L5: §6c/§6d first stated (p+1)/2 and "x==1 unreachable"; that omitted the t==inf class.
Likewise x == -1 (s=0) is reached by t == 0 mod p, i.e. p | a.  Verified: for p=3,7,11
the realized residue count is 3,5,7 = (p+3)/2, and all of P^1(F_p) is covered via
s=4t^2.]  Since cleared_columns() scales all columns by ONE uniform denominator Lden --
a p-UNIT for inert p (p | no N_k, and for split-only orbits p | den(d) is false) -- two
on-line columns with equal x mod p are EQUAL mod p.  Hence
        rank(A mod p) <= (p+3)/2   ==>   v_p(D_m(A)) >= m - (p+3)/2.
Verified across all sampled orbits/primes: rank saturates at EXACTLY (p+3)/2 and the
floor holds (v_p(D_mA) in fact grows ~quadratically).  This is a genuinely multi-row
bound: it holds for EVERY off-line orbit -- including the all-split D=425 case where §5
and §6b give nothing -- so it strictly enlarges uniform coverage of the numerator.

**Honest boundary (L5) -- why this does NOT yet close OP1, and the SHARP open form.**
The bound is on the NUMERATOR only.  The right invariant is not v_p(D_m(A)) but the
TOP Smith exponent: since q_min = smallest n with n*d in L = colspan_Z(A), the class
d-bar in the finite group Z^m/L (order D_m(A)) has order EXACTLY q_min, so
        v_p(q_min) = v_p(ord d-bar)  <=  e_max := max_i v_p(s_i(A))
                                          = v_p(s_m(A)) = v_p(D_m(A)/D_{m-1}(A)),
the top Smith p-exponent (RIGOROUS: order of an element divides the group exponent,
whose p-part is e_max).  The probe confirms v_p(q_min) <= e_max in EVERY row, and
v_p(q_min) = e_max generically (d meets the top cyclic factor; it lags by <=1 only
occasionally, e.g. D=425, p=3, m=5: v_p(q_min)=2 < e_max=3).  Measured (D=425, p=3):
        v_3(D_mA) = 0,1,3,6,9,14,19  (m=2..8)  -- QUADRATIC ~ C(m-1,2);
        e_max     = 0,1,2,3,4,5,5              -- LINEAR ~ m-(p+3)/2;
        v_3(qmin) = 0,0,2,2,4,5,5.
So the product v_p(D_mA) grows quadratically while the TOP invariant e_max (which is
what q_min sees) grows linearly.  The rank-count lemma proves only the LINEAR product
floor v_p(D_mA) >= m-(p+3)/2; via the nondecreasing Smith chain that yields only
e_max >= 1.  To get e_max >= c*m one needs a rigorous SUPER-LINEAR product bound
(the observed C(m-1,2)) OR a direct top-invariant bound -- i.e. the p-adic FILTRATION
rank(A mod p^j) for j >= 2 (how the equal-x-mod-p columns separate mod p^2, p^3, ...
= a Vandermonde-discriminant / resultant computation).  THIS is the exact, sharply
localized open core: prove e_max = v_p(s_m(A)) >= c*m and that d hits the top factor.

**Net (DISCOVERY tier).**  New RIGOROUS content: (a) the tight rank-count lemma
rank(A mod p) <= (p+3)/2 => product floor v_p(D_m(A)) >= m-(p+3)/2, UNIFORM over all
on-line sets and ALL off-line orbits (covers split-only D=425 that §5/§6b could not);
(b) the top-invariant bound v_p(q_min) <= e_max = v_p(s_m(A)) (group theory).  New
EVIDENCE: e_max grows LINEARLY (~ m-(p+3)/2) and v_p(q_min) = e_max generically, so
OP1 is plausibly true here.  STILL OPEN, now razor-sharp: a rigorous linear lower
bound on the TOP Smith invariant e_max (via the mod-p^j filtration / Vandermonde
discriminant), which -- with "d meets the top factor" -- would close the split-only
case of OP1.  Probe: probe_determinantal_channel.py (v_p(q_min)<=e_max verified in
every row; e_max slow at m>=6 due to D_{m-1} minors).

## 6d. Pigeonhole + confluent-Vandermonde LINEAR floor on e_max (new, this session)

Attacks the exact open core of §6c: a rigorous linear lower bound on the top Smith
invariant e_max = v_p(s_m(A)).  Probe: probe_emax_pigeonhole.py (EXIT 0).  This is a
near-complete proof skeleton; the determinantal/Vandermonde side is essentially done.

**Pigeonhole bound (VERIFIED, uniform).**  mod p there are exactly (p+3)/2 on-line
x-classes (§6c).  Any m nodes => by pigeonhole some class holds >= ceil(2m/(p+3)) of
them.  Since x_{t+p} == x_t mod p, the family {t0 + p*i} is a p-adic expansion INSIDE
one class (x = xi + p*y, y distinct mod p), so a class of size c carries a confluent
Chebyshev/Vandermonde block whose divided differences pick up p^0,...,p^{c-1} => its
top Smith exponent is c-1.  Hence
        e_max >= (max class multiplicity) - 1 >= ceil(2m/(p+3)) - 1   (LINEAR).
Verified: the ADVERSARIAL minimum of e_max over all sampled node families is
>= ceil(2m/(p+3))-1 in EVERY row (p=3,7,11; m=2..7).  The even-spread adversary
optimum ACHIEVES it exactly for p=7,11 (spread e_max == PH, all m), confirming the
bound is tight = the adversary's best move; single-class concentration gives
e_max >= m-1 (the opposite extreme).

**Basis reduction (VERIFIED, exact law).**  A = [C_j(t_k)], C_j = 4(1 - T_j(x)),
inherits the Vandermonde p-adic Smith structure for ODD p, via an OFF-BY-ONE shift:
        v_p(D_r(A)) = v_p(D_{r-1}(V_x)),   V_x = [x_k^j] the monomial Vandermonde.
(4 is a p-unit; {x^j}<->{T_j} is unitriangular over Z[1/2]; the constant row T_0 that
C_j = T_0 - T_j subtracts drops one effective row, shifting the whole determinantal-
divisor sequence by one.)  Verified exactly: p=3,m=5 gives A-divisors [0,0,1,3,6] =
V-divisors [0,1,3,6,10] shifted; p=7,m=5 A=[0,0,0,0,1]=V=[0,0,0,1,2] shifted.  Hence
e_max(A) = e_{m-1}(V_x), the SECOND-highest Vandermonde invariant -- still linear
(shift costs O(1) depth, not the slope).

**What remains RIGOROUS-OPEN (now a single point).**  Two classical facts finish the
determinantal side and must be source-verified, not assumed: (i) the confluent-
Vandermonde Smith staircase -- for V_x over Z_p with mod-p class sizes c_1..c_r, the
Smith p-exponents are the sorted multiset U_i {0,1,...,c_i-1} (classical Hermite /
confluent-Vandermonde valuation); (ii) the off-by-one row lemma above.  These give
e_max(A) >= ceil(2m/(p+3)) - O(1), a RIGOROUS LINEAR floor on the top invariant.
The ONE genuinely-remaining analytic gap is step (3) of §6c: the off-line d is FIXED
(not adversarial), so we still need that d-bar attains near-top order in Z^m/L
UNIFORMLY over adversarial node choices, i.e. v_p(q_min) >= e_max - O(1).  Probe data
(§6c) shows v_p(q_min) = e_max generically, lagging by <=1 -- strong evidence -- but a
uniform "d meets the top cyclic factor" argument is not yet proved.  Net: the
Vandermonde multi-row side of OP1's split-only case is essentially closed; only the
fixed-vector top-factor incidence survives.

## 6e. Fixed-vector incidence: the lag is a small constant (new, this session)

Tests §6d's ONE surviving gap (§6c step iii): does the FIXED off-line d attain
near-top order in Z^m/L uniformly over adversarial on-line node choices?  Probe:
probe_qmin_incidence.py (EXIT 0).  Measures the incidence lag
        lag(A) := e_max(A) - v_p(q_min) = v_p(s_m(A)) - v_p(ord d-bar) >= 0
over a strong adversarial pool INCLUDING the single-class family {t0+p*i} (one
confluent class => e_max ~ m-1 forced huge; the sharpest decoupling attack) and the
even-spread family, across 3 split-only orbits (D=425, 4, 26), p in {3,7,11}, m<=6.

**Result (VERIFIED).**  GLOBAL MAX lag = 3 -- a small constant.  Decisively, the
single-class adversary FAILS to decouple: its lag is <=1 (d-bar still meets the huge
top factor).  The adversarial MINIMUM v_p(q_min) grows linearly, tracking
PH = ceil(2m/(p+3))-1 (>= PH except a single off-by-one dip at m=3).  Hence, uniformly
in the tested range,
        v_p(q_min) >= e_max - 3 >= ceil(2m/(p+3)) - O(1)   (LINEAR).
Combined with §6d's linear e_max floor, this is strong evidence the determinantal
side of OP1's split-only case CLOSES: the adversary can neither keep e_max small
(pigeonhole, §6d) nor rotate the fixed d off the top factor (this section).

**Honesty (L5).**  This is EVIDENCE, not proof: (a) m<=6 only -- lag reached 3 at m=6,
so "lag = O(1)" vs "lag grows slowly" is not settled; a rigorous bound on lag (or a
direct linear lower bound on min v_p(q_min)) is still required; (b) it rests on the
two classical facts §6d flags (confluent-Vandermonde staircase; off-by-one row lemma),
which must be source-verified.  Net: all three legs of the split-only argument now have
strong exact-arithmetic support and the dangerous single-class decoupling attack is
ruled out, but OP1 for split-only orbits remains OPEN pending the rigor of §6d(i,ii)
and a proved bound on the incidence lag.

## 6f. SELF-CONTAINED PROOF of the e_max linear floor (new; closes §6d gap i)

§6d flagged the classical "confluent-Vandermonde Smith staircase" as a fact to
source-verify (gap i).  `baseline/` has no such reference, so citing it from memory is
forbidden (CLAUDE.md).  It is not needed: the LOWER bound we actually use has a short
ELEMENTARY proof, verified end-to-end by probe_emax_proof_check.py (ALL PROOF LINKS
HOLD: True, p=3,7,11, m=2..6, adversarial families incl. single-class & spread).

**Theorem (e_max linear floor, elementary).**  Let p be inert (p == 3 mod 4).  For any
on-line node configuration, the monomial Vandermonde V = [x_k^j] (k over nodes,
j = 0..m-1) over Z_p has top Smith p-exponent
        e_max = v_p(D_m(V)) - v_p(D_{m-1}(V))  >=  ceil(2m/(p+3)) - 1.

**Proof.**
 (1) [class count, §6c corrected] The x_k occupy at most (p+3)/2 residue classes mod p.
 (2) [Vandermonde det]  For any m-subset S, det V_S = prod_{k<l in S}(x_l - x_k), so
     v_p(det V_S) = sum_{k<l in S} v_p(x_l - x_k).  For inert p, v_p(x_l - x_k) >= 1 iff
     x_k == x_l mod p (same class), else = 0.
 (3) [pigeonhole]  Let S* be a D_m-minimizing m-subset (v_p(det V_{S*}) = v_p(D_m)).
     Its m nodes fall into <= (p+3)/2 classes, so some class has size
     c* >= ceil(2m/(p+3)).
 (4) [minor removal]  Pick u in that largest class of S*, and delete BOTH u and the top
     column j=m-1.  This is an (m-1)x(m-1) minor of V, namely det V_{S* minus u} on
     columns 0..m-2, with
        v_p(det V_{S* minus u}) = v_p(det V_{S*}) - sum_{w in S*, w!=u} v_p(x_u - x_w)
                                = v_p(D_m) - (sum over same-class w of v_p >= 1, cross = 0)
                               <= v_p(D_m) - (c* - 1).
     Since D_{m-1} = gcd of all (m-1)-minors divides this one,
        v_p(D_{m-1}) <= v_p(D_m) - (c* - 1).
 (5) Therefore e_max = v_p(D_m) - v_p(D_{m-1}) >= c* - 1 >= ceil(2m/(p+3)) - 1.  QED.

Only three ingredients: the Vandermonde determinant identity, v_p of node differences
(within/cross class), and "gcd of minors divides any single minor."  No confluent
staircase, no Hermite-interpolation citation.  Gap i is CLOSED; the constant is
ceil(2m/(p+3))-1 (the honest (p+3)/2 count, slightly weaker than §6d's optimistic
(p+1) denominator, still LINEAR).

**Status of the three legs after §6f.**
 - LEG 1 (e_max linear floor): PROVED elementarily for the monomial Vandermonde V
   (this section).  RIGOROUS.
 - LEG 2 (basis reduction A ~ V, §6d(ii)): SUPERSEDED by §6g -- the floor is proved
   DIRECTLY on A via C_j = (x-1) g_j, so no A ~ V reduction is needed.  CLOSED.
 - LEG 3 (fixed-vector incidence, §6e): v_p(q_min) >= e_max - O(1); EVIDENCE only
   (lag <= 3 in range, single-class decoupling fails), no uniform proof.  OPEN.
Net: with LEG 1 proved (§6f) and LEG 2 closed by §6g (direct-on-A proof), the
split-only OP1 determinantal side rests solely on LEG 3 (the genuine remaining gap).
RH stays [OUT].

## 6g. e_max floor PROVED DIRECTLY on A -- LEG 1 + LEG 2 UNIFIED (new; closes LEG 2)

§6f proved the floor for the monomial Vandermonde V and left LEG 2 (the basis
reduction A ~ V) as a pending mechanical lemma.  It is now unnecessary: the
minor-removal proof runs DIRECTLY on the actual matrix A = [C_j(t_k)], because of one
extra algebraic fact.  Verified end-to-end by probe_emax_A_direct.py (ALL: True --
identity + floor + pigeonhole + minor-removal, p=3,7,11, m=2..6, adversarial families
incl. single-class & spread; privacy-clean).

**Key fact.**  T_j(1) = 1 for all j, so every C_j = 4(1 - T_j) VANISHES at x = 1:
        C_j(x) = (x - 1) g_j(x),   deg g_j = j - 1,   lead g_j = lead C_j = -4*2^{j-1}
(a p-unit for odd p).  The g_1,...,g_m have degrees 0,1,...,m-1, so for any m-subset S
the generalized-Vandermonde determinant collapses to an ordinary Vandermonde:
    det [C_j(x_k)]_{j=1..m, k in S}
        = (prod_j lead g_j) * prod_{k in S}(x_k - 1) * det [x_k^i]_{i=0..m-1, k in S}
        = (p-unit) * prod_{k in S}(x_k - 1) * prod_{k<l in S}(x_l - x_k),
hence (leading factors are p-units for odd p)
    v_p(det A_S) = sum_{k in S} v_p(x_k - 1) + sum_{k<l in S} v_p(x_l - x_k).   (*)
Verified exactly (*) on every m-subset in the probe (D1 True everywhere).

**Theorem (e_max floor on A, elementary, PROVED).**  For inert p == 3 mod4 and any
on-line node configuration, the observation matrix A = [C_j(t_k)] (rows j=1..m)
satisfies
        e_max(A) = v_p(D_m(A)) - v_p(D_{m-1}(A))  >=  ceil(2m/(p+3)) - 1.
Proof.  (1) the x_k occupy <= (p+3)/2 classes mod p (§6c corrected).  (2) by (*), the
same-class pairs contribute v_p(x_l-x_k) >= 1 and v_p(x_k-1) >= 0.  (3) let S* be a
D_m-minimizing m-subset; pigeonhole gives a class of size c* >= ceil(2m/(p+3)) in S*.
(4) delete a node u from that class AND the top row C_m; the resulting (m-1)-minor has
rows C_1..C_{m-1} (degrees 1..m-1, same factorization (*)), so
    v_p(det) = v_p(det A_{S*}) - v_p(x_u - 1) - sum_{same-class w!=u} v_p(x_u - x_w)
            <= v_p(D_m(A)) - (c* - 1)     [v_p(x_u-1) >= 0; same-class sum >= c*-1],
and D_{m-1}(A) divides this minor, so v_p(D_{m-1}(A)) <= v_p(D_m(A)) - (c*-1).
(5) e_max(A) >= c* - 1 >= ceil(2m/(p+3)) - 1.  QED.

This SUBSUMES §6f LEG 1 (no need to pass through V) and CLOSES §6d LEG 2 (no off-by-one
lemma, no classical staircase).  Ingredients are all elementary: T_j(1)=1, the
consecutive-degree generalized-Vandermonde collapse, v_p of node differences, and
"gcd of minors divides any minor."  RIGOROUS.

**Leg status after §6g.**  LEG 1 + LEG 2 are now a single PROVED theorem on A
(e_max(A) >= ceil(2m/(p+3)) - 1, uniform over all on-line configs and ALL off-line
orbits incl. split-only).  The ONLY remaining leg of the split-only determinantal
argument is LEG 3 (§6e): the FIXED off-line d attains near-top order, i.e.
v_p(q_min) >= e_max(A) - O(1) -- EVIDENCE only (lag <= 3 in range; single-class
decoupling fails), no uniform proof yet.  OP1 stays OPEN on LEG 3; RH stays [OUT].

## 6h. LEG 3 stress test: the incidence lag PLATEAUS at 3 through m=10..14 (new)

§6e reached lag <= 3 but only for m <= 6 (minor-enumeration wall), so "lag = O(1)"
vs "slow growth" was UNSETTLED -- and lag hit its max exactly at the m=6 boundary,
the worst possible ambiguity.  `probe_leg3_pushm.py` (EXIT 0) breaks the wall with an
O(m^3) SNF/DVR pipeline:
  * v_p(q_min) via `qmin_fast` (SNF; == trusted minor-gcd qmin_index);
  * e_max via p-adic Smith exponents = MIN-VALUATION-PIVOT elimination over the DVR
    Z_(p) (pivot valuations ARE the elementary-divisor exponents; sum == v_p(D_r)
    cross-checked against the SNF product).
CROSS-VALIDATION: at m <= 6 the SNF/DVR pipeline reproduces the TRUSTED
det_divisor_r / qmin_index EXACTLY (q_min, e_max, v_p(q_min) all match) -- clean:True.

RESULT (3 split-only orbits D=425,4,26; inert p=3,7,11; sharpest adversaries: single
class at EVERY base t0, deep-cluster mod p^2, even spread, rational families):
    GLOBAL MAX lag over m = 2..10 is 3, reached only at m=6 and m=9;
    lag by m: 1,1,2,1,3,1,1,3,2 -- FLAT, no upward trend.
    min v_p(q_min) >= PH = ceil(2m/(p+3))-1 holds in EVERY row (transfers the floor).
Deep push (p=3,7 orbits, m=6..14, cross-val skipped for speed) confirms the same
ceiling of 3 -- no creep as e_max grows linearly (p=3 e_max ~ 0,1,2,2,4,5,5,6,8,...).

READING (L5): this UPGRADES §6e's evidence -- lag is now flat at a ceiling of 3
across m=2..14, three orbits, three primes, and the decoupling-optimal adversaries,
so "lag = O(1)" is strongly supported and "slow growth" is disfavoured.  It remains
EVIDENCE, NOT proof: no uniform theorem bounds the lag, so LEG 3 -- and hence
split-only OP1 -- stays OPEN.  What a proof still needs: either a uniform bound on
lag(A) = v_p(D_m([A|d])) - v_p(D_{m-1}(A)) (the exact lag identity, via the (*)
factorization extended to the d-augmented minors), or a direct linear lower bound on
adversarial min v_p(q_min).  RH stays [OUT].

## 6i. LEG 3 anatomy: lag splits into two SEPARATELY-BOUNDED pieces (new)

`probe_leg3_psi_anatomy.py` (EXIT 0) decomposes the exact lag using §6g's
factorization C_j = (x-1) g_j.  For an (m-1)-subset S' of on-line nodes, the
d-augmented m-minor factors (column-linearity in the d column + (*)) as
    det[A_{S'} | d] = (p-unit) * prod_{k in S'}(x_k - 1) * Vand(S') * Psi(S'),
    Psi(S') = sum_{off-line atoms a} (u_a - 1) * prod_{k in S'} (u_a - x_k),
i.e. the orbit-sum over the <=8 off-line atoms u_a of the polynomial
P_{S'}(X) = (X-1) prod_{k in S'}(X - x_k).  Writing
    Phi(S') := sum v_p(x_k-1) + sum_{k<l} v_p(x_l - x_k)   [pure on-line, top-row minor],
    psi(S') := v_p(Psi(S')) = v_p(det[A_{S'}|d]) - Phi(S')  [d-residual],
the exact lag is
    lag = [Phi(S*) - v_p(D_{m-1})]  +  psi(S*)   at the V-minimizing S*.

TWO structural facts, VERIFIED TRUE across 3 split-only orbits (D=425,4,26),
inert p=3,7,11, m=2..7, all adversarial families (single-class at every base,
spread, rational):
  (E1) identity  lag == min_{S'} v_p(det[A_{S'}|d]) - v_p(D_{m-1})   : True.
  (SUB-LEMMA, provable from §6g, candidate [THM])
       v_p(D_{m-1}(A)) == min_{S'} Phi(S')  : True.  I.e. D_{m-1} is ALWAYS
       realized by a TOP-(m-1)-rows minor.  Proof sketch: any (m-1)-row subset
       factors as prod(x_k-1) * (generalized Vandermonde); dividing by Vand(S')
       leaves a Schur polynomial (p-integral, v_p >= 0), minimized (=0 extra) at
       consecutive degrees 0..m-2 = rows 1..m-1.  So the min is attained on top
       rows.  This makes Phi the exact p-adic content of D_{m-1}.

DECOMPOSITION RESULT: over the whole grid,
    max (Phi-slack = Phi(S*) - v_p(D_{m-1})) = 1,     max psi(S*) = 3,
    lag = Phi-slack + psi  <= 1 + 3;  drivers: psi in 25 rows, Phi-slack in 11.
So the lag=3 plateau is NOT one mysterious quantity: it is the sum of
  (I)  a near-optimality slack Phi-slack <= 1 (the V-minimizer is Phi-almost-optimal), and
  (II) a d-residual psi(S*) <= 3 = v_p of Psi(S*), an orbit-sum of P_{S'} over the
       <=8 fixed off-line atoms.
BOTH are bounded by a small constant INDEPENDENT of m out to m=7 (and lag itself
to m=14, §6h).  A proof of LEG 3 now reduces to two independent bounded-constant
lemmas: (I) Phi-near-optimality of the V-minimizer, and (II) a uniform bound on
v_p of the bounded (<=8-term) orbit-sum functional Psi.  psi high would require
fine-tuned p-adic cancellation across only ~8 atoms, which the adversary (who
fixes the nodes, not the orbit) cannot force uniformly -- the mechanism behind the
plateau.  HONESTY (L5): still EVIDENCE + a reduction, NOT a proof; LEG 3 and
split-only OP1 remain OPEN.  RH stays [OUT].

## 6j. LEG 3 CLEAN reduction: lag <= psi(S0) at ANY Phi-minimizer -- ONE quantity (new)

`probe_leg3_psi_bound.py` (EXIT 0, privacy-clean) removes the Phi-near-optimality
leg (I) of §6i entirely.  From the exact identity
    lag = min_{S'} [Phi(S') + psi(S')] - min_{S'} Phi(S'),
pick ANY S0 in argmin Phi and use it as a feasible point for the first min:
    lag <= [Phi(S0) + psi(S0)] - min Phi = psi(S0).
So the WHOLE incidence lag is bounded by a single quantity -- psi = v_p(Psi)
evaluated at a Phi-minimizer.  Leg (I) is unnecessary; LEG 3 collapses to:

    is  min_{S0 in argmin Phi} psi(S0)  bounded by a small constant,
    uniformly in m and over adversarial node sets?

VERIFIED (3 split-only orbits D=425,4,26; inert p=3,7,11; m=2..7; all families):
  * clean bound  lag <= min_{S0 in argmin Phi} psi(S0)  holds EVERYWHERE : True.
  * max lag = 3;  max over configs of min_{Phi-min} psi = 3.
  * of 36 positive-lag configs, a Phi-minimizer with psi<=0 exists in 0 -- i.e.
    the bound is never trivially zero when the lag is positive (so it is a real,
    non-degenerate constraint), yet still caps at 3.

STRUCTURAL MECHANISM (the reason psi resists growth), now sharp:
  * The off-line orbit collapses to EXACTLY 2 distinct atoms u = (w+1/w)/2,
    w = 1 - 1/rho, over the quartet {sigma+-i tau, 1-sigma+-i tau}.  For every
    tested orbit #distinct atoms u = 2, and mod each inert p they give exactly
    2 distinct residues in F_{p^2} = F_p[i] (u not in F_p, i.e. u_im a p-unit).
  * Hence Psi(S0) = sum over the 2 conjugate atoms of (u_a - 1) * prod_{k in S0}
    (u_a - x_k) = Tr_{F_{p^2}/F_p}[ (u-1) * g(u) ],  g(u) = prod_{k in S0}(u - x_k).
  * KEY (m-independence): each factor (u - x_k) has x_k in F_p, u not in F_p, so
    u - x_k is a p-UNIT; thus g(u) is a p-unit REGARDLESS of |S0|.  Adding nodes
    only multiplies g by more units -- Psi never gains valuation from the node
    count.  The ONLY freedom is g(u)'s residue at the fixed u, a single F_{p^2}
    value.  This is precisely why psi = v_p(Tr[(u-1)g(u)]) does not grow with m.
  * v_p(Psi) >= 1 needs the trace of a p-unit to vanish mod p (kernel = half of
    F_{p^2}); >= k needs vanishing mod p^k -- a codimension-k p-adic condition on
    the single value g(u).  A node-only adversary (who fixes the nodes, not the
    orbit's 2 atoms) tunes g(u) but is constrained to keep S0 Phi-minimal; that
    constraint is what caps the achievable depth (empirically <= 3).

REMAINING OPEN CORE (LEG 3, sole gap): a uniform proof that
    v_p( Tr_{F_{p^2}/F_p}[ (u-1) * g(u) ] ) <= const
over Phi-minimizing node sets g, u the FIXED off-line atom.  This is now a
self-contained arithmetic question about ONE F_{p^2}/F_p trace of a p-unit --
no longer about determinantal geometry.  Without the Phi-minimality constraint
the trace can be pushed to any depth (choose g(u) == -g(u)^p mod p^k), so the
bound MUST come from the combinatorial constraint that g arises from a
Phi-minimal node multiset -- that is the genuine unproved combinatorial-arithmetic
core.  HONESTY (L5): EVIDENCE + a sharp reduction + m-independence structure, NOT
a proof.  LEG 3 and split-only OP1 remain OPEN.  RH stays [OUT].

## 6k. LEG 3 core: trace/Lucas identity RIGOROUS; two honest corrections (new)

`probe_leg3_trace_mechanism.py` (EXIT 0, privacy-clean) attacks the sole open
quantity of §6j -- psi = v_p(Psi) at a Phi-minimizer -- and both HARDENS the
backbone and CORRECTS two over-optimistic framings.

RIGOROUS-IDENTITY SOLIDIFICATION (all True, exactly, over every Phi-minimizer;
3 orbits, p=3,7,11, m=2..8):
  * The off-line orbit is a CONJUGATE PAIR {u, ubar}: reflection rho->1-rho fixes
    u (w->1/w leaves (w+1/w)/2), conjugation sends u->ubar.  Verified
    #atoms=2, conjugate-pair=True for all three orbits.  Hence
        Psi(S0) = (u-1)g(u) + (ubar-1)g(ubar) = 2*Re[(u-1)g(u)]
                = Tr_{Q(i)/Q}[(u-1) g(u)],   g(X)=prod_{k in S0}(X - x_k).
  * With mu(X)=(X-u)(X-ubar)=X^2-sX+n (s=2Re u, n=Norm u) and the Lucas trace
    sequence tau_0=2, tau_1=s, tau_j=s*tau_{j-1}-n*tau_{j-2}, and P_T=(X-1)g=sum
    c_j X^j:   Psi = sum_j c_j tau_j.
  VERIFIED:  v_p(Psi_det) == v_p(2 Re[(u-1)g(u)]) == v_p(sum c_j tau_j) : True.
  So the §6j reduction's algebraic backbone is now a CHECKED IDENTITY, not an
  assertion: LEG 3 really is "bound v_p of one F_{p^2}/F_p trace of a p-unit."
  * v_p(Norm(P_T(u))) = sum_y v_p(mu(y)) == 0 always (p inert => mu irreducible
    mod p => mu(y) != 0 mod p for p-integral y).  So P_T(u) is a p-unit root of
    Z^2 - Psi Z + N = 0 with N a p-unit -- the rigidity frame for any psi bound.

TWO HONEST CORRECTIONS (L5):
  (C1) The load-bearing quantity is the MINIMUM of psi over Phi-minimizers, NOT an
       arbitrary one.  Tabulating psi over ALL Phi-minimizers gives max psi = 6
       (at m<=8), growing with the coincidence excess ncoll = m - #classes and the
       max class-multiplicity mu_max (psi=5,6 concentrate at (mu_max,ncoll) =
       (4,5),(3,3),(3,2)).  So a UNIVERSAL "every Phi-minimizer has small psi" is
       FALSE.  The true bound is EXISTENTIAL: among the many Phi-minimizing
       (m-1)-subsets, at least one has psi <= 3.  RE-CONFIRMED on the wider grid
       (m=2..8 + deep-cluster mod p^2 family): max lag = 3, max over configs of
       min_{Phi-min} psi = 3, and 0 rows violate lag <= min-psi or exceed 3.  So
       §6j's bound lag <= min_{Phi-min} psi <= 3 is intact and strengthened; only
       its INTERPRETATION is corrected (existence of a good subset, not universality).
  (C2) psi is NOT a mod-p residue phenomenon.  A p-adic DEPTH test -- shift every
       node t->t+p (same residue class) -- CHANGED psi in 889 configs.  So psi
       genuinely depends on the nodes' higher p-adic digits; the adversary has
       real p-adic freedom.  This KILLS the simplest route to a uniform bound
       (finite mod-p residue enumeration).  Any proof must be a covering/existence
       argument over the family of Phi-minimizers -- distinct subsets give
       distinct p-adic trace values that cannot all be aligned to high depth at
       once -- not a residue-class computation.

NET: the trace form is rigorous and the split-only lag stays <= 3 out to m=8 with
deep-cluster adversaries, but the open core is now correctly framed as an
EXISTENTIAL, genuinely-p-adic bound on min_{Phi-min} v_p(Tr[(u-1)g(u)]).  EVIDENCE
+ a hardened reduction, NOT a proof.  LEG 3 and split-only OP1 remain OPEN.  RH
stays [OUT].  (probe_leg3_trace_mechanism.py.)

## 6l. LEG 3: affine-per-node identity + ESCAPE/PACKING dichotomy narrows the gap (new)

`probe_leg3_affine.py` (EXIT 0, privacy-clean) produces a NEW rigorous identity and
uses it to confine the open part of LEG 3 to a small "packed" regime.

NEW RIGOROUS IDENTITY (verified exactly, every node of every Phi-minimizer; 3
orbits, p=3,7,11, m=2..7).  Fixing all nodes but one and viewing Psi as a function
of that node's x-value x_k:
    Psi = Tr[(u - x_k) H(u)],  H(u) = (u-1) prod_{j!=k}(u - x_j)
        = Tr[u H(u)] - x_k Tr[H(u)]  =  a_k - x_k b_k,
AFFINE in x_k, with a_k = 2 Re[u H(u)], b_k = 2 Re[H(u)] rational.  VERIFIED
Psi == a_k - x_k b_k : True for all k.  Moreover EVERY positive-psi Phi-minimizer
(1769/1769) has at least one UNIT-SLOPE node, v_p(b_k) = 0 (non-degenerate affine
dependence).

ESCAPE MECHANISM (candidate lemma, provable from the identity).  Let S0 be a
Phi-minimizer with psi>0 (Psi ≡ 0 mod p) and k a unit-slope node.  Replace node k
by a node k' whose x-class differs from x_k's (and != class of 1).  Then
    Psi' = a_k - x_{k'} b_k = Psi + (x_k - x_{k'}) b_k,
and (x_k - x_{k'}) b_k is a p-UNIT (different residue class => x_k - x_{k'} a unit;
b_k a unit), so Psi' ≢ 0 mod p, i.e. psi' = 0.  If the swap preserves Phi-minimality
(true when a spare x-class exists), we get a Phi-minimizer with psi=0 => lag=0.

PACKING DICHOTOMY (VERIFIED).  Let navail = #distinct on-line x-classes (excluding
the class of 1) among ALL ambient nodes, slack = navail - (m-1).
  * EVERY slack>=1 config has min_{Phi-min} psi = 0 (spare class => escape => lag=0):
    slack=1: 39 configs, slack=2: 24, slack=3: 12, slack=4+: 12 -- ALL min-psi=0.
  * EVERY positive-min-psi config (39 of them) is PACKED, navail <= m-1 (39/39).
So POSITIVE LAG IS CONFINED TO THE PACKED REGIME navail <= m-1.  Even there, packing
is NECESSARY not sufficient (e.g. slack=-4: 96 configs still have min-psi=0 vs only 6
positive), and min-psi stays <= 3 (max over the whole grid = 3).

HONEST NOTES (L5):
  * A prior tautology retired: "psi == min_k v_p(a_k - x_k b_k)" is trivial because
    Psi = a_k - x_k b_k for every k, so all f_k equal psi -- it is NOT evidence.
    The real escape needs CHANGING x_k (a swap), captured above.
  * The single-swap reduces psi in only 439/1769 positive-psi Phi-minimizers -- the
    min-psi minimizer itself is often already swap-irreducible; the dichotomy rests
    on EXISTENCE of a spare-class swap (slack>=1), not on every subset being reducible.
  * Still EVIDENCE + a candidate escape lemma, NOT a proof.  What remains OPEN is a
    uniform bound on min-psi in the PACKED regime (navail <= m-1) -- a strictly
    smaller problem than before (the spread/unpacked regime is now handled by the
    affine escape).  The escape lemma needs a rigorous proof that (a) a unit-slope
    node always exists and (b) the spare-class swap preserves Phi-minimality.
NET: LEG 3's open core narrows from "all node sets" to "packed node sets
(navail <= m-1)", with a clean affine-escape lemma for the rest.  LEG 3 and
split-only OP1 remain OPEN.  RH stays [OUT].  (probe_leg3_affine.py.)

### §6m  Escape lemma PROVED for the non-packed regime (slack >= 1) — LEG3 closed there

Two rigorous results upgrade §6l's affine-escape from EVIDENCE to a proof valid on
the whole non-packed regime.  Both stay DISCOVERY tier (candidate [THM]s); RH [OUT].

LEMMA A (escape hypothesis (a), PROVED; verify formula per L9 — probe_leg3_lemmaA.py).
Let S0 be a Phi-minimizer with psi = v_p(Psi) > 0.  Since P_T(u) is a p-UNIT (Norm a
p-unit, §6k), psi>0 forces  P_T(u) ≡ c·i (mod p) purely imaginary, c != 0 in F_p.
For the affine slope b_k = Tr[H_k(u)], H_k = P_T(u)/(u - x_k), with u = a + b i:
    H_k ≡ c·i / ((a-x_k) + b i) = c[b + (a-x_k) i]/mu(x_k),  mu(x_k)=(a-x_k)^2+b^2,
    => b_k ≡ 2 c b / mu(x_k)  (mod p).
As c != 0, b = Im(u) != 0, mu(x_k) = Norm(u - x_k) != 0 (p inert), EVERY node has b_k
a p-UNIT.  So a unit-slope node not only exists — ALL nodes qualify — whenever psi>0.
VERIFIED: (1) psi>0 => Re P_T(u) ≡ 0; (2) the exact formula b_k ≡ 2cb/mu(x_k);
(3) all b_k p-units.  All True on 1769 positive-psi Phi-minimizers (3 orbits, p=3,7,11,
m=2..7).

ESCAPE THEOREM (non-packed regime, PROVED; verify construction — probe_leg3_escape_thm.py).
Let slack = navail - (m-1) where navail = # distinct x-classes (!= class of 1) among
the ambient nodes.  If slack >= 1:
  (i)  minPhi = 0.  Pick m-1 nodes in distinct classes != class(1); Phi = 0.  Any
       Phi-minimizer then has ALL clean nodes (per-node contribution 0): a dirty node
       could be swapped into a spare fresh class to drop Phi below minPhi — impossible.
  (ii) Take ANY Phi-minimizer S0 with psi>0 (so Phi(S0)=0, m-1 distinct classes).
       navail >= m => a spare class c' exists.  Swap any node k for a node k' in c':
       S0' has m-1 distinct classes => Phi(S0')=0=minPhi (hypothesis (b) PROVED here).
       The complement S0\{k} is unchanged, so the affine identity (§6l) gives
           Psi(S0') - Psi(S0) = (x_k - x_k') · b_k.
       Psi(S0) ≡ 0 (psi>0); (x_k - x_k') is a p-unit (distinct classes); b_k a p-unit
       (Lemma A) => Psi(S0') ≢ 0 => psi(S0') = 0.
  (iii) Hence min over Phi-minimizers of psi = 0, so lag = 0.
VERIFIED: (A) slack>=1 => minPhi=0; (B) slack>=1 => min-psi=0; (C) the explicit single
swap lands Phi=0 AND psi=0.  All True on 87 non-packed configs / 136 constructive swaps.

NET (L5): the escape is now a CONSTRUCTIVE PROOF for slack >= 1 (not "single-swap
reduces in 439/1769" — we exhibit ONE Phi-minimizer with psi=0, which suffices).
LEG3's non-packed regime is CLOSED: lag=0 there, so q_min carries the full e_max floor.
The SOLE remaining LEG3 gap is the PACKED regime slack <= 0 (navail <= m-1), where no
spare class exists to escape into.  min-psi stays <= 3 empirically there.  split-only
OP1 remains OPEN; RH stays [OUT].

### §6n  Packed-regime min-psi<=3 is a FINITE-K artifact; true floor is min-psi<=1

Attack on the sole remaining gap (packed regime, slack<=0).  There the only freedom
left is REPRESENTATIVE choice inside each x-class (t -> t+p keeps the class, hence Phi).
With x(t) = 1 - 2/(4t^2+1),
    x(t') - x(t) = -8 (t-t')(t+t') / [(4t^2+1)(4t'^2+1)],
and for p ≡ 3 mod 4 the denominators are p-units (4c^2+1 != 0, -1 a non-residue).  By
Lemma A (§6m) the slope b_k is a p-UNIT when psi>0, so a one-step same-class swap moves
Psi by -b_k*(x(t+p)-x(t)); when that step has p-adic depth 1 it drives psi down.

VERIFIED (probe_leg3_packed.py, EXIT 0, privacy-clean):
  (H1, CORRECTED L5): the single-step depth v_p(x(t+p)-x(t)) is NOT universally 1 --
    distribution {1: 18, 2: 2, 3: 1} over classes/p.  It is 1 GENERICALLY (18/21);
    special t with v_p(2t+p)>0 give depth 2-3.  So the mechanism is "usually one step
    kills a level", not an exact identity.
  (H2/H3, STRONG): on ALL 37 packed positive-min-psi configs, AUGMENTING each used
    class with deeper reps (t+p, t+2p; classes & packing unchanged) drives min over
    Phi-minimizers of psi DOWN TO <= 1 in every case.  Every min-psi in {2,3} collapses
    to 0 (2->0: 3, 3->0: 2, 2->1: 1); min-psi=1 cases stay 1 (27) or drop to 0 (4).

READING (L5): min-psi >= 2 is a FINITE-K edge effect -- with enough same-class
representatives (which large observation families supply) the packed-regime bound
sharpens to min-psi <= 1, i.e. lag <= 1, an O(1) constant (exactly what LEG3 needs for
the e_max floor to carry through to q_min).  The residual min-psi=1 (27/37 stay at 1)
is the genuine floor: one unit-slope step lands v_p exactly 1 and cannot always cancel
to 0.  EVIDENCE on the SOURCE of the bound, NOT a proof: augmentation adds candidate
representatives to isolate the depth mechanism; it does not prove a specific OP1 matrix
contains them.  OPEN: (i) show the actual OP1 observation families carry enough
same-class representatives (they grow with m); (ii) a rigorous min-psi<=1 floor in the
packed regime.  split-only OP1 OPEN; RH stays [OUT].

### §6o  psi is a p-adic DISTANCE  psi = v_p(x_k - a_k/b_k); ladder descent

The affine identity factors: Psi = a_k - x_k b_k = -b_k (x_k - alpha), alpha = a_k/b_k
(alpha depends ONLY on the other nodes).  When b_k is a p-unit (Lemma A, §6m, forced
when psi>0),
    psi = v_p(Psi) = v_p(x_k - alpha),
i.e. psi is literally the p-ADIC DISTANCE from node k's value x_k to a fixed p-adic
target alpha.  This recasts the whole packed-regime obstruction as a distance problem:
  * alpha not ≡ class(x_k) mod p  =>  psi = 0  (automatic escape, no coincidence);
  * alpha ≡ class(x_k)           =>  psi >= 1, but the same-class ladder x(t_k + p s)
    (s=0,1,2,...) moves x_k p-adically and realises the residues of (x_k-alpha)/p, so
    a short ladder attains psi <= single-step depth.

VERIFIED (probe_leg3_ladder.py, EXIT 0, privacy-clean):
  (R1) psi == v_p(x_k - a_k/b_k) EXACTLY on all 120 unit-slope nodes of the packed
       positive-min-psi minimizers -- the p-adic-distance recast is an identity.
  (R2/R3) node-0 same-class ladder floor over 37 packed positive configs: floor=1 (34),
       floor=2 (1), floor=3 (2); and it SATURATES by L=3 (L=3 == L=p+1 == L=2p+1).
       A single node's ladder already caps psi at a small m-independent constant.

READING (L5): min-psi is a bounded (m-INDEPENDENT) p-adic-descent quantity.  Since
lag <= min-psi (§6j), lag = O(1) -- exactly the LEG3 requirement (a constant floor gap
independent of the observation count m; cf. §6h's plateau at 3 through m=14).  The
p-adic-distance identity psi = v_p(x_k - a_k/b_k) is the clean rigorous handle; the
remaining rigorous gap is (i) that a real OP1 observation family supplies a same-class
ladder of the needed length, and (ii) promoting the observed <=3 plateau to a proven
constant via this descent.  EVIDENCE + a rigorous identity, not the full proof.
split-only OP1 OPEN; RH stays [OUT].

### §6p  ADVERSARIAL test: the node-set adversary CANNOT grow the lag with m

OP1 quantifies over ALL rational on-line node sets {t_k}: the adversary picks them to
maximise the incidence lag (<= min over Phi-minimizers of psi, §6j).  §6m closed the
non-packed regime, so the adversary must play PACKED.  §6o showed forcing psi>=C needs
p-adic alignment to depth C across every Phi-minimizer at once.  Does the adversary have
enough freedom to grow this with the observation count m?

SEARCH (probe_leg3_adversary.py, EXIT 0, privacy-clean; orbit D=425 split-only,
p ∈ {3,7,11}, m=2..8): for each (p,m) the adversary sweeps pool size K ∈ {m-1 (tightest
packing, NO spare same-class rep), m, m+1, m+3} and, per K, tries 200 seeded-random
packed pools with wide p-adic depth (base + p a + p^2 c, a,c up to 8) PLUS a structured
"deep-align" pool (all reps at base + p^2 j, forcing within-class v_p=2).  Recorded the
MAX over pools of [min over Phi-minimizers of psi].

RESULT: GLOBAL max = 2, attained at small m (p=7, m=2).  It does NOT grow with m -- the
2's cluster at small m/K; for large m the adversary's best stays 0-1.  (This is even
below §6h's synthetic-family plateau of 3; the 3 came from particular rep structures,
not from an m-growing trend.)

READING (L5): even choosing the node set adversarially, min-psi -- hence the incidence
lag -- is capped by a small constant with NO m-dependence.  So lag = O(1) uniformly:
q_min carries the full e_max floor up to an additive constant, exactly the LEG3
requirement.  HONEST bounds: this is a BOUNDED search (200 random + 1 structured pool
per cell), one orbit, p<=11, m<=8 -- it SUPPORTS a uniform bound and, decisively, shows
no growth trend, but does not PROVE it.  Together §6m (non-packed CLOSED), §6n (packed
<=3 is finite-K), §6o (psi = p-adic distance identity), §6p (adversary cannot grow it)
form the evidence package that LEG3's lag is O(1).  The remaining rigorous gap is a
proof of the uniform packed bound via the §6o p-adic-descent identity.  split-only OP1
OPEN; RH stays [OUT].

### §6q  The collision requirement K >= m supplies the competition that caps the lag

An apparent threat and its resolution.  Deep p-adic tuning of the TIGHTEST packing
K = m-1 (probe_leg3_align.py) DID grow psi (p=11,m=3: 2 -> 4 at tuning depth S=81), and
§6j already noted that WITHOUT the Phi-minimality constraint the trace can be pushed to
any depth.  But K=m-1 is NOT a valid OP1 collision: q_min = D_m(A)/D_m([A|d]) needs the
m-th determinantal divisor D_m(A) != 0, i.e. an m x m minor, i.e. AT LEAST m on-line
columns.  So every genuine collision has K >= m, hence C(K, m-1) >= m competing
Phi-minimizers, and §6j's load-bearing quantity is the MIN over them.

VERIFIED (probe_leg3_align2.py, EXIT 0, privacy-clean; orbit D=425, p ∈ {7,11}, m=3..5):
  (V) collision-validity boundary: qmin_fast holds in 0/400 pools at K=m-1, but 400/400
      at K=m and 400/400 at K=m+1 -- collisions require K >= m EXACTLY (matches the
      rank argument D_m(A) != 0 needs m columns).
  (G) growth under deep tuning (max over deeply-tuned packed pools of min-over-Phi-min
      psi, tuning depth S up to 243): the K=m-1 INVALID control shows elevated,
      depth-sensitive values (up to 4); every VALID K in {m, m+1} row is FLAT and
      bounded (all <= 2, mostly <= 1), with NO growth in S.

READING (L5): the psi-growth is a NON-COLLISION artifact of the single-subset regime
K=m-1.  In every valid collision (K >= m) the subset competition -- forced by the same
determinantal-rank fact that makes a collision possible -- caps min-psi at a small
constant, flat under deep adversarial tuning AND in m.  So lag = O(1) on the actual
collision variety.  This ties the bound to the collision structure itself and removes
the "tightest packing" worry.  The remaining rigorous gap sharpens to: prove that over
K >= m packed on-line nodes the C(K,m-1) competing Phi-minimizers cannot ALL be
p-adically aligned past a constant depth (via the §6o identity psi = v_p(x_k-a_k/b_k)).
EVIDENCE (bounded search, one orbit, p<=11) + the rigorous K>=m boundary; not a full
proof.  split-only OP1 OPEN; RH stays [OUT].

### §6r  PAIRWISE-SWAP lemma: min-psi is bounded by the swappable same-class rep distance

The §6q residual ("the C(K,m-1) competing minimizers cannot all align past a constant
depth") now has a PROVED partial handle turning it into a single scalar bound.

LEMMA (pairwise swap; candidate [THM], verified P1 below).  In a packed Phi=0 minimizer
setting, let a,b be two on-line nodes in the SAME x-class.  Call (a,b) SWAPPABLE if there
are Phi-minimizers S ∋ a and S' ∋ b with the IDENTICAL complement, S∖{a} = S'∖{b} =: C.
By the §6o affine identity, alpha = a_k/b_k depends only on C, so
    psi(S)  = v_p(x_a - alpha),   psi(S') = v_p(x_b - alpha)   (SAME alpha).
If BOTH were >= d+1 then x_a ≡ x_b ≡ alpha (mod p^{d+1}), contradicting v_p(x_a-x_b)=d.
Hence  min(psi(S), psi(S')) <= v_p(x_a - x_b).  Taking the min over swappable pairs:
    min-over-Phi-min psi   <=   D_swap := min over SWAPPABLE same-class pairs of v_p(x_a-x_b).

VERIFIED (probe_leg3_pairswap.py + probe_leg3_swapdist.py, EXIT 0, privacy-clean;
orbit D=425, p ∈ {7,11}, m=3..5, K=m..m+2, tuning depth S up to 243):
  (P1) the inequality  min(psi(S),psi(S')) <= v_p(x_a-x_b)  holds for ALL 1144 swappable
       pairs tested -- the lemma is confirmed.
  (E)  EVERY one of 1333 positive-min-psi VALID collisions has at least one swappable
       same-class pair (0 without) -- so the bound is non-vacuous in the valid regime.
  (D)  under DEEP p-adic tuning, GLOBAL max D_swap = 4 and GLOBAL max min-psi = 2, with
       NO growth as depth S grows (27->81->243 rows flat) and NO growth in m.  min-psi
       stays <= 2 everywhere; 0 lemma violations.

HONEST CAVEAT (L5): pairswap check (P2) found that the NAIVE closest same-class pair need
NOT be swappable (False in 3/366; 7 unit-gap configs were non-swappable), so raw pigeonhole
on distance is insufficient -- the bound must run over SWAPPABLE pairs, and D_swap can
exceed min-psi (4 vs 2).  The sharpened residual is therefore TWO provable sub-claims:
  (R1) a swappable same-class pair always EXISTS once K >= m (empirically 1333/1333);
  (R2) D_swap (equivalently min-psi) is bounded by an absolute constant (empirically <= 2).
Both are strongly supported but not yet proved.  EVIDENCE + one proved inequality (the
pairwise-swap lemma).  split-only OP1 OPEN; RH stays [OUT].

### §6r-note  (R1) mechanism: clean proof covers the non-degenerate case only

Attacking (R1) via a clean construction (probe_leg3_r1.py, EXIT 0, privacy-clean) exposed
an HONEST limit and the reason for it.  Because x_of(t) = (4t^2-1)/(4t^2+1) depends only on
t^2, the map t -> x mod p is 2-to-1 (t and -t share an x-class), so two DISTINCT residue
bases b, b' with b' ≡ -b collapse into the SAME x-class.  Consequently navail (# distinct
x-classes present, excluding the class of 1) is NOT always m-1:
  (A) among 427 positive-min-psi valid collisions, navail = m-1 in 280 (minPhi = 0) but
      navail = m-2 in 147 (minPhi > 0, from a +/- x-class collision).
  (B) the explicit "repeated class + one rep per other class" construction yields two
      Phi=0 minimizers in exactly the 280 navail = m-1 configs (280/427), NOT the 147.
So the CLEAN constructive proof of (R1) covers only the non-degenerate navail = m-1 case.
The degenerate navail = m-2 case still HAS swappable pairs (swapdist (E): 1333/1333 across
all configs) but through minPhi > 0 minimizers, which the clean construction does not yet
cover.  Refined (R1) = prove existence of a swappable same-class pair also when a +/- x-class
collision forces navail = m-2 and minPhi > 0.  EVIDENCE + partial proof.  RH stays [OUT].

### §6r-note2  (R2) REFUTED path: a SINGLE swing node has NO low ceiling (reaches 6)

Testing whether (R2) follows from a per-node p-adic ceiling (probe_leg3_r2.py, EXIT 0,
privacy-clean): FIX the complement C (hence fix alpha = a_k/b_k by the §6o affine form
Psi = -b(x - alpha), b a p-unit) and sweep ONE swing node exhaustively over t = base + p*s,
s in [0, p^3).  Result (orbit D=425, p in {7,11}, 145 alpha-reachable configs):
  (C1) max-over-swing psi distribution {4:128, 5:14, 6:3}, GLOBAL max = 6 -- a single swing
       node CAN be aligned to alpha as deep as 6; there is NO low per-node ceiling.
  (C2) the psi>=2 swing residues all share ONE class mod p (single p-adic target, affine
       ladder) -- so each extra digit of alignment needs a p-times rarer s (1-in-p^k node).
CONCLUSION (L5, honest REFUTATION): the "single-swing ladder ceiling" mechanism for (R2)
is FALSE -- one free swing node reaches psi = 6 given deep enough s.  This matches §6q's
single-minimizer (K = m-1) growth.  Hence swapdist's observed min-psi <= 2 in VALID
collisions is NOT a per-node ceiling; it is genuinely a JOINT effect of (i) taking the MIN
over the C(K,m-1) forced competing Phi-minimizers AND (ii) the collision constraint q_min
restricting the node set (deep 1-in-p^k nodes cannot all coexist in a bounded on-line
family while keeping every minimizer aligned).  (R2) must be proved via this joint
structure, NOT per-node.  One candidate proof path is thereby eliminated.  RH stays [OUT].

### §6r-note3  CORRECTION: min-psi is 3 (not 2); the +1 is the x_of ±-degeneracy

An ADVERSARIAL coordinate-ascent search at the HARDEST pool size K=m (probe_leg3_r2joint.py
+ probe_leg3_witness.py + probe_leg3_regime.py, EXIT 0, privacy-clean) corrects the §6r
"max min-psi = 2": that 2 was a RANDOM-SAMPLING under-count.  The adversary reaches min-psi
= 3 in a canonically re-verified VALID collision.

WITNESS (p=7, m=4, K=m, orbit D=425; qmin_fast True): nodes t = [688,426,596,1374],
navail = 2, m-1 = 3, minPhi = 1, and BOTH Phi-minimizers {(0,1,2),(1,2,3)} have psi = 3.
Crucially navail = 2 = m-2 with minPhi = 1: this is a DEGENERATE config where the t -> -t
symmetry of x_of(t) = (4t^2-1)/(4t^2+1) (which depends only on t^2, so x_of(b) = x_of(p-b))
collapses two residue bases into ONE x-class.

MECHANISM (regime split; unifies with §6h "lag plateaus at 3"):
  * NON-degenerate (navail = m-1, minPhi = 0): min-psi small (pairwise-swap regime);
  * ±-DEGENERATE (navail = m-2, minPhi >= 1): the doubled x-class adds one unit -> min-psi 3.
So the LEG3 constant is 3, and the extra +1 is EXACTLY the x_of class-doubling.

SMALL-p ARTIFACT (important scoping).  Because only (p-1)/2 distinct nonzero-t x-classes
exist (t and -t share one), a NON-degenerate navail = m-1 config REQUIRES p >= 2m-1.  For
p < 2m-1 the m-1 distinct classes cannot be filled, the config is FORCED degenerate, and
min-psi rises with the deficit d = (m-1) - navail (e.g. p=7,m=5 forced d>=1 gave min-psi 4).
Such (p,m) are artifacts, NOT counterexamples: LEG3 O(1) must be read in the p >= 2m-1
regime (the same p-vs-m regime as the §6c-h e_max floor), where the deficit is bounded.
Refined LEG3 target: prove min-psi <= 2 + d with d = (m-1) - navail bounded on the actual
split-only observation family.  HONEST correction (L5): the constant is 3, tied to a
concrete arithmetic cause; the m-independence holds per degeneracy level.  RH stays [OUT].

DATA (probe_leg3_regime.py, non-artifact cells p >= 2m-1, bucketed by deficit d):
  p=11 (#xcls=5): m=3 [d=0:2, d=1:0];  m=4 [d=0:1, d=1:1];  m=5 [d=0:0, d=1:2]  -- all <= 2.
  p=7  (#xcls=3): m=4 (x-class SLACK = 0) [d=1:3]  -- the boundary case reaching 3.
So min-psi <= 2 whenever there is x-class SLACK  slack_x := (p-1)/2 - (m-1) >= 1, and the
extra +1 (-> 3) appears only at the TIGHT boundary slack_x = 0.  This mirrors §6m's packing
slack, one level up: LEG3's constant is governed by slack_x, i.e. by how many distinct
x-classes (p-1)/2 the prime supplies versus the m-1 the observation needs.  Cleanest LEG3
statement: min-psi <= 2 for slack_x >= 1, <= 3 at slack_x = 0; m-independent given slack_x.

ORBIT-INDEPENDENCE (probe_leg3_orbits.py, EXIT 0, privacy-clean).  The regime split holds
across ALL THREE off-line orbits (D=425, D=4, D=26), p in {7,11,13}, non-artifact cells:
  D=425: slack_x>=1 -> max min-psi 2,  slack_x=0 -> 3
  D=4:   slack_x>=1 -> max min-psi 2,  slack_x=0 -> 3
  D=26:  slack_x>=1 -> max min-psi 2,  slack_x=0 -> 2
So LEG3's lag constant is governed by the x-class slack (p-1)/2 - (m-1) of the PRIME, NOT
by the specific curve/orbit -- an orbit-independent arithmetic law.  This is strong EVIDENCE
that the sole remaining LEG3 gap is the clean two-line bound "min-psi <= 2 for slack_x >= 1,
<= 3 at slack_x = 0", provable from the pairwise-swap lemma (§6r) plus the ±-degeneracy
count, uniformly in the orbit.  Not yet a proof.  RH stays [OUT].

### §6s — the two-source valuation identity for ψ (candidate [THM], verified exact)

A closed-form decomposition of the §6o affine root α that splits the LEG3 lag into TWO
independent p-adic contributions.  Setup (§6l/§6o): for a Φ-minimizer subset with swing
node x, write the complement product H := (u-1)·∏_{j in C}(u - x_j) = P + Qi, where u is
the OFF-LINE ATOM and σ := Re(u), τ := Im(u) are its OWN real/imaginary parts (NOT the
orbit parameters; u = off_atoms_u(...) is the Joukowski image of the atom).  Then the
affine value factors EXACTLY as

    Ψ(x) = 2·Re[(u - x)·H] = 2[(σ - x)P - τQ] = 2·Re(H)·(α - x),   α = σ - τ·Im(H)/Re(H),

using Re[(u-x)H] = (σ - x)P - τQ and (σ - x) - τQ/P = α - x.  Taking p-adic valuations
gives the UNCONDITIONAL identity

    ψ = v_p(Ψ) = v_p(Re H) + v_p(x - α),   α = σ - τ·Im(H)/Re(H).            (§6s-main)

So the incidence lag has TWO independent p-adic sources:
  (i)  v_p(Re H)   -- the real part of the on-line complement product being p-divisible;
  (ii) v_p(x - α)  -- the p-adic distance of the swing node to the argument-ratio root α,
       i.e. the depth to which Im(H)/Re(H) approaches the fixed target (σ - x)/τ
       (arg H = arg(u-1) + Σ_{j in C} arg(u - x_j), so (ii) is a sum-of-arctangents
       alignment against a fixed target).
An upper bound on the lag must control BOTH terms; either alone can inflate ψ.

VERIFICATION (inline exact-arithmetic Fraction scripts, L9), across ALL THREE off-line
orbits (D=425, D=4, D=26):
  * algebraic  Ψ == 2·Re(H)·(α - x)  with  α = σ - τ·Im(H)/Re(H):  0 / 6000 failures.
  * valuation  ψ == v_p(Re H) + v_p(x - α):                        0 / 6000 failures.
Both are EXACT identities (rational arithmetic), not numerical coincidences.

HONEST CORRECTION (L5) to the first draft of §6s: the one-term form "ψ = v_p(x - α)" is
WRONG in general -- it holds only when v_p(Re H) = 0.  §6m Lemma A does NOT force this at
every Φ-minimizer: over 21535 Φ-minimizer swing columns of VALID collisions, 1956 had
v_p(Re H) > 0 (probe_leg3_s check).  The correct, verified statement is the two-term
(§6s-main).  Dropping the v_p(Re H) term was an over-simplification; it is reinstated here.

STATUS: §6s-main is a rigorous UNCONDITIONAL restatement (candidate [THM]).  It sharpens
but does not close the LEG3 gap.  The remaining core (§6r-note3) is now a TWO-TERM bound:
show that at the min over Φ-minimizers, v_p(Re H) + v_p(x - α) <= 2 for slack_x >= 1 and
<= 3 at slack_x = 0, uniformly in the orbit.  Not a proof.  RH stays [OUT].

### §6s-note — term attribution: the lag lives in v_p(x - α) (probe_leg3_twoterm)

Adversarial coordinate ascent on VALID collisions, reporting the two terms of (§6s-main)
SEPARATELY at the achieving Φ-minimizer, ORBIT-INDEPENDENT (D=425 and D=4 agree exactly):

    slack_x = 0 (tight boundary): max lag = 3, ALL of it in v_p(x - α) = 3, v_p(Re H) = 0.
    slack_x >= 1                : max lag = 1 (this light search), v_p(Re H) <= 1, v_p(x-α) <= 1.

So the degeneracy bonus at slack_x = 0 -- and the dominant part of the lag in every regime
-- is carried by the ARGUMENT-RATIO term (ii) v_p(x - α), i.e. the p-adic depth to which
Im(H)/Re(H) approaches the fixed target (σ - x)/τ.  The real-part term (i) v_p(Re H) is a
MINOR contributor (<= 1, and only in the slack_x >= 1 regime).  This collapses the remaining
LEG3 core to a SINGLE-TERM bound:

    at the min over Φ-minimizers,  v_p(x - α) <= 2 for slack_x >= 1,  <= 3 at slack_x = 0,

uniformly in the orbit, where α = σ - τ·Im(H)/Re(H) and the swing node x is a doubled
x-class residue.  (The +1 at slack_x = 0 is the x_of ±-degeneracy, §6r-note3; light search
here shows the plateau of the slack_x >= 1 side at 1, heavier search in §6r-note3 reaches 2.)
HONEST (L5): S=81/6-restart local search, small p,m; the attribution is clean and orbit-
consistent but not exhaustive.  Not a proof.  RH stays [OUT].

## 3. Corrections to the earlier (superseded) picture

  * The naive p-adic "prime-obstruction" idea, using a SPLIT prime (p == 1 mod 4)
    of the off-line conductor, is WRONG as stated: such primes ARE reachable by
    on-line nodes and cancel with UNIT p-adic cost (v_p(c_k)=0 suffices).
    Verified: off-line D=425=5^2*17 has both split primes reachable at nodes a=3
    (N=10) and a=13 (N=170), yet the floor persists via lattice magnitude.
    -- BUT the INERT-prime version (p == 3 mod 4) is CORRECT and gives a genuine
    UNIFORM bound; see the new §5.  The distinction split-vs-inert is the whole
    point: inert primes are UNREACHABLE by any on-line conductor N=4a^2+b^2.
  * The archimedean bound is real but LOOSE; the earlier "8 sum|n| >= |q| max|d_j|"
    inequality is subsumed by, and much weaker than, the exact q_min identity.
  * "Denominator channel" is now made precise: it is the lattice INDEX
    [L + Z d_m : L], an exact determinantal-divisor invariant, not a vague
    denominator-blowup heuristic.

## 5. NEW THEOREM (rigorous, UNIFORM over all on-line constructions) -- inert-prime pole

This is the first bound that is uniform over ALL on-line node sets (not per-family),
proving OP1 for an explicit INFINITE off-line sub-family.  It is the correct,
quantitatively-fixed form of the "unreachable prime" mechanism.

**Setup.**  In the u-coordinate (u = (w+1/w)/2, w = 1 - 1/rho), an off-line orbit
has u_0 = u_off in Q(i) OFF [-1,1].  On-line node t = a/b (primitive) has
u = x_t = (4a^2 - b^2)/(4a^2 + b^2), a RATIONAL with denominator N = 4a^2 + b^2.

**Theorem.**  Let p == 3 (mod 4) be a prime with v_p(u_0) = -delta < 0 (equivalently
p | denominator of u_0; note p is INERT in Z[i], so v_p extends uniquely and
Galois-invariantly to Q(i)).  Then EVERY order-m Li-collision matching this off-line
orbit against ANY finite set of on-line rational nodes has off-line multiplicity
        |q| >= p^{B(m)},   B(m) = max_{j<=m} v_p(den d_j)  >=  delta*(m - g),
where g is a fixed constant (the max gap between "trace-nonzero" degrees; g <= ord of
u_0 mod p in F_{p^2}^*).  Hence the collision size is at least p^{delta(m-g)}:
EXPONENTIAL, UNIFORMLY over all on-line constructions.

**Proof.**
 (1) On-line p-integrality (CRUX).  p == 3 mod 4 => 4a^2+b^2 =/= 0 mod p (else
     (2a/b)^2 == -1 mod p, impossible; p|b forces p|a, non-primitive).  So p ∤ N,
     x_t in Z_(p), T_j(x_t) in Z_(p), and C_j(t) = 8(1 - T_j(x_t)) in Z_(p) for all j.
     [Verified: CRUX = True, all families, j<=6, in probe_pod_3mod4.py.]
 (2) Off-line pole.  Write u_0 = xi/p^delta with xi in Z[i], v_p(xi)=0.  Since p is
     inert, T_j(u_0) = 2^{j-1} u_0^j + (lower degree) has v_p = -j*delta (leading term
     strictly dominates; v_p(2)=0).  d_j = 8(1 - Re T_j(u_0)); Re halves the sum of
     T_j(u_0) and its Galois conjugate, both of valuation -j*delta.  The leading-pole
     numerator is Tr_{Q(i)/Q}(xi^j), whose reduction mod p is Tr_{F_{p^2}/F_p}(xi^j).
     This vanishes only when xi^j lands on the (bounded-gap) trace-zero line of F_{p^2};
     for all other j, v_p(den d_j) = j*delta exactly.  Trace-nonzero degrees have gaps
     <= g, so B(m) >= delta(m - g).
 (3) Collision.  sum_k c_k C_j(t_k) + q d_j = 0 with c_k,q in Z.  By (1) the on-line
     sum is p-integral for every j, so q d_j is p-integral => v_p(q) >= v_p(den d_j)
     for all j <= m => v_p(q) >= B(m) => |q| >= p^{B(m)}.  QED.

**Evidence (probe_pod_3mod4.py + chart).**  Off-line rho=3/5+6/5i (D=72=2^3*3^2,
p=3, delta=1): CRUX True; v_3(den d_j) = j for j not== 2 mod 4, else 0 (Tr vanishes
exactly on j==2 mod4, g<=4); B(m)=1,1,3,4,5,5,7,8,9,9,11,12,13,... ~ m.  min v_3(q_min)
over 20/20 node families >= B(m) for m=2..6 (True, uniformly).  Independent orbit
rho=3/4+3/4i (p=3) gives the SAME B(m) growth => mechanism is structural, not special.

**Scope / honesty (L5).**  This proves OP1 uniformly ONLY for off-line orbits whose
u_0 has an INERT (p == 3 mod 4) prime in its denominator.  Empirically only ~2 of 7
sampled off-line orbits qualify; the adversary escapes by choosing u_0 with a
denominator built solely from split primes (p == 1 mod 4) and 2 (e.g. rho=2/3+i,
u_0 den 260 = 2^2*5*13; rho=3/4+i, den 425 = 5^2*17).  So this is a genuine PARTIAL
proof of OP1 -- a large explicit infinite family -- NOT the full quantifier.  The
split-prime / archimedean regime still needs the lattice-magnitude (lambda_1) route
of §2.  My earlier writeup used the WRONG exponent (m*v_p(D)); the correct exponent
is v_p(den d_m) ~ delta*m, derived above and verified.

**Evidence the REMAINING (escaped) case is also exponential.**  Restricting the
adversary to off-line orbits with NO inert prime (u_0 denominator all split/2:
rho = 2/3+i, 3/4+i, 1/4+1/2 i, 2/5+4/5 i), the MINIMUM true collision size (shortest
integer relation, q!=0, via exact LLL over half-int + integer node families) is
        m=2: 47      (log2 5.55)
        m=3: 70304    (log2 16.10,  dlog2 +10.55)
        m=4: 30788758 (log2 24.88,  dlog2 + 8.77)
        m=5: 2.13e12  (log2 40.96,  dlog2 +16.08).
Exponential (dlog2 bounded well below by ~8) => full OP1 is plausibly TRUE even off
the inert-prime family; the lambda_1 route (§2) is the right next target, not a
counterexample hunt.  (Evidence only, DISCOVERY tier; NOT a proof for this case.)
  * The archimedean bound is real but LOOSE; the earlier "8 sum|n| >= |q| max|d_j|"
    inequality is subsumed by, and much weaker than, the exact q_min identity.
  * "Denominator channel" is now made precise: it is the lattice INDEX
    [L + Z d_m : L], an exact determinantal-divisor invariant, not a vague
    denominator-blowup heuristic.

### 6u. LEG3 "lag = O(1)" lemma REFUTED by external referee — REPLAYED EXACT (this session)

An external referee reviewing the OB-41 outsource returned outcome **REFUTED** for the
LEG3 intermediate lemma ("incidence lag is O(1), <=2 at slack_x>=1"). Replayed here with
`discovery/verify_ob41_referee.py` using this repo's own §1 helpers and exact
Fraction/Gaussian-rational arithmetic — the referee's counterexample reproduces EXACTLY:

  orbit rho=3/4+i (D=425, the §6 anchor);  p=29, m=14, slack_x=1 (the "good" regime);
  nodes t=(1823,2113,4433,2838,6608,201,6900,7886,5276,7915,8037,1019,6993,5949);
  x-residues (9,9,9,9,9,6,6,6,6,6,9,9,9,9) mod 29  => navail = 2  (NOT m-1 = 13);
  rank(A) = 14 = m (exact) so C2 holds; qmin_fast finite so C1 holds => VALID collision;
  9 tied Phi-minimizers ALL give psi = 6  =>  lag = 6  >> claimed bound 2.

**Diagnosis (two independent facts, both important):**

1. **The lemma is genuinely false as stated, and my prior evidence was BIASED.** The
   "lag<=2" evidence (probe_leg3_s / _twoterm, "p<=13 m<=6, 0/6000") only ever sampled
   the FULL-SPREAD regime: `build_pool` draws `bases = sample of m-1 DISTINCT residues`,
   forcing navail = m-1. It NEVER generated clustered node sets. So the O(1) claim was an
   over-generalization from a silent sampling cap (L5). The controlling invariant is
   **navail (x-classes USED), not slack_x = (p-1)/2-(m-1) (x-classes AVAILABLE)** — the
   theorem conflated the two. (Note: naive clustering does NOT auto-give high lag — my own
   2-class constructions gave lag <= 0; the referee's nodes are tuned to align alpha
   p-adically deep. But one exact valid counterexample refutes a universal claim.)

2. **The refutation does NOT touch the barrier.** `lag` was only an INTERMEDIATE p-adic
   leak (v_p of Psi at Phi-minimizers), one route toward lower-bounding q_min at the prime
   p. It is neither necessary nor sufficient for the barrier. The barrier's actual target
   (this doc, §6/§6a) is **inf_A q_min(m) super-polynomial**, and its DANGER is q_min -> 1,
   NOT q_min large. At the very counterexample: **q_min = 1.7e392 (log2 = 1303),
   v_29(q_min) = 2** — the 6-unit lag is a negligible p-adic leak, dwarfed by the
   Vandermonde/prod(x-1) growth that clustering into distinct large rationals (t up to
   ~8000) forces into D_m(A). So this config has an ENORMOUS q_min: it STRENGTHENS the
   barrier, not weakens it.

**Consequence.** The LEG3 "lag=O(1)" lemma is RETIRED (false; a mis-formulated detour).
OP1's real open frontier is unchanged: the direct uniform lower bound on q_min (the
e_max / confluent-Vandermonde route of §6c-6d, or lambda_1 of §2). LEG1/LEG2 stand; the
"third leg" as posed was the wrong quantity. RH stays [OUT] throughout — this is a
finite exact-arithmetic correction with no bearing on RH either way.

### 6v. §6u follow-up — the clustering attack does NOT break the floor where it is ACTIVE (this session)

The §6u refutation killed "lag = O(1)" in the LARGE-p regime (p >= 2m-1). But lag =
e_max - v_p(q_min), and the PROVED e_max floor (§6g, e_max >= ceil(2m/(p+3))-1) is only
nontrivial in the SMALL-p regime p <= 2m-1. The barrier needs the floor to TRANSFER:
v_p(q_min) >= floor - O(1). Decisive test (`discovery/probe_qmin_floor_attack.py`): run the
referee's own weapon — genuinely CLUSTERED valid collisions (nodes packed into c << m-1
x-classes as distinct large rationals, NOT the navail=m-1 pools that `build_pool` silently
forces) — but in the ACTIVE regime, and adversarially MINIMIZE v_p(q_min) to try to push it
below the floor. Orbit D=425, exact SNF/DVR (`emax_smith`, `qmin_fast`):

  p= 7 m= 8  floor=1 : navail=2 -> v_p(q_min)=3 (e_max=3, lag=0);  navail=3 -> 2 (e_max=3, lag=1)
  p= 7 m=10  floor=1 : navail=2 -> v_p(q_min)=4 (e_max=5, lag=1);  navail=3 -> 3 (e_max=3, lag=0)
  p=11 m=12  floor=1 : navail=2 -> v_p(q_min)=5 (e_max=5, lag=0)

**READING.** In every observed case the adversarial MIN v_p(q_min) stayed at or ABOVE the
floor (gap 1..4); the floor TRANSFER survives. The contrast with §6u is the whole point:
the very clustering that drives lag to 6 in the large-p regime (where e_max ~ 0, so a large
lag just means v_p(q_min) ~ 0 = the trivial floor, harmless) instead drives e_max UP in the
small-p regime (confluent-Vandermonde, exactly the §6c-6d mechanism), and v_p(q_min) TRACKS
it with lag <= 1. De-biasing the generator (clustered + max-spread, not build_pool's forced
navail=m-1) did NOT expose a large-lag attack where the floor is active — it strengthened
the §6e/§6h transfer evidence rather than overturning it. So the §6u refutation retires a
lemma stated in the wrong regime; it does NOT damage OP1's per-prime linear q_min floor.

**HONESTY (L5).** Bounded random sampling (250 trials/cell), one orbit, small m, p in {7,11}
(p=5 is x-class-degenerate: den(x(t))=4t^2+1 ≡ 0 mod 5 collapses the classes). Evidence of
survival, not proof. The PROVED input is e_max >= floor (§6g); the OPEN piece remains the
uniform transfer v_p(q_min) >= e_max - O(1) IN THE ACTIVE REGIME — now re-supported on a
de-biased generator. The sharp open target is unchanged and correctly regime-scoped: prove,
for p <= 2m-1, that the fixed off-line d-bar meets the top p-part of Z^m/L up to a bounded
deficit. RH stays [OUT].

### 6w. The PER-PRIME floor claim is REFUTED at p=13 — but the FULL q_min stays enormous (this session)

§6v's optimism ("per-prime linear q_min floor survives") was itself under-sampled: it tested
only p in {7,11}. Pushing the SAME adversarial minimization to p=13 and larger m
(`discovery/probe_qmin_perprime_floor.py`, 3 orbits, exact SNF/DVR) BREAKS it:

  p= 7 m<=8  floor<=1 : adv min v_p(q_min) >= floor           (slack 0..+1, holds)
  p=11 m<=10 floor<=1 : adv min v_p(q_min) >= floor           (slack 0..+1, holds)
  p=13 m= 9  floor=1  : adv min v_13(q_min) = 0               (slack -1  *** VIOLATION ***)
  p=13 m=10  floor=1  : adv min v_13(q_min) = 0               (slack -1  *** VIOLATION ***)

So the clean statement `v_p(q_min) >= ceil(2m/(p+3))-1 for every prime` (which would, via
Mertens, force q_min super-polynomial and CLOSE OP1) is FALSE. The proved e_max floor (§6g)
does NOT transfer to q_min prime-by-prime: the fixed off-line d-bar can miss the top p-part
of Z^m/L entirely at a given prime even when e_max there is >= 2.

**DECISIVE follow-up (`discovery/verify_ppf_violation_fullqmin.py`, exact).** At the p=13,
m=9 violation — witness nodes t = [158,496,14,365,458,443,341,80,354], x-residues mod 13 =
[7,7,11,11,2,11,2,7,2] (navail=3), rank(A)=9=m (C2 valid), qmin finite (C1 valid), e_max=3 —
the FULL integer q_min is

    q_min = 2^39 * 3^9 * 5^16 * 7^3 * 11^3 * 17^11 * 19 * 23 * ... * 823   (379 bits, 115 digits)

with v_13(q_min) = 0. So q_min is ENORMOUS despite its 13-part vanishing: the growth is
carried by the OTHER primes (2, 5, 17, ... — the confluent-Vandermonde mass clustering
forces into D_m). This is the same lesson as §6u at a finer grain: q_min is an AGGREGATE
quantity, and any single prime's contribution can be adversarially drained to 0 without
denting the whole.

**CONSEQUENCE — corrected open target.** The per-prime route to OP1 is DEAD (a second
mis-formulated sufficient condition, after the lag lemma). What survives, and what the
barrier actually needs, is the AGGREGATE bound

    OP1 target :  sum_{p} v_p(q_min) * log p  =  log q_min  is super-polynomial in m,

for which NO uniform per-prime floor holds — the mass can migrate between primes. The honest
next handle is a DIRECT lower bound on log q_min (the confluent-Vandermonde / det-D_m growth
of §6c-6d), NOT a prime-by-prime floor. §6v is hereby narrowed: the floor transfers for the
primes/ranges it sampled (p<=11 here) but is NOT uniform over p; do not cite it as a
per-prime law. RH stays [OUT] — a finite exact-arithmetic correction with no RH bearing.

### 6x. The AGGREGATE q_min resists the per-prime-draining attack — min log2(q_min) grows linearly (this session)

With both prime-by-prime routes dead (§6u, §6w), the corrected OP1 target is the AGGREGATE
`inf over valid collisions of log q_min = sum_p v_p(q_min) log p` super-polynomial in m.
DECISIVE test (`discovery/probe_qmin_aggregate_min.py`, exact SNF): adversarially MINIMIZE the
FULL log2(q_min) over valid collisions (K>=m, rank m, finite qmin), comparing three adversaries
— CLUSTER (nodes packed into 2-3 x-classes mod p in {7,11,13}, the §6w weapon that drains a
prime's part to 0), SPREAD (distinct x-classes), RANDOM. Orbit D=425:

  m :  2     3     4     5     6     7     8     9     10
 min: 3.9  26.7  60.0  98.1 124.2 166.9 208.7 247.3 230.2   (log2 q_min)
  d :  -  +22.8 +33.3 +38.1 +26.1 +42.7 +41.8 +38.6 -17.1
 arg: clu  clu   clu  spr   clu   clu   clu   clu   clu

**READING.** min log2(q_min) climbs ~linearly at ~+37/step (m=3..9): q_min ~ 2^{~37 m},
exponential => super-polynomial. The CLUSTER adversary is USUALLY the argmin — per-prime
draining does lower q_min vs spread/random (e.g. m=9: cluster 247 vs spread 270 vs random 285)
— but it CANNOT pull the whole q_min below the exponential trend. So the mass genuinely
migrates between primes (as §6w's 379-bit witness already showed at a single point), and the
aggregate q_min survives the very attack that killed both per-prime routes. First DIRECT
evidence for the corrected (aggregate) target, under the strongest known adversary.

**HONESTY (L5).** (1) At m=10 the cluster adversary found a config 17 bits (~7%) BELOW m=9 —
a downward wobble, not a collapse (230 bits is still deep in the exponential regime; precedent
§6a records such single-degree dips as artifacts that recover). Whether m=10 is search noise
or a genuine "cluster bites harder at even m" is UNSETTLED — the linear trend dominates but is
not monotone. (2) The tail m>=11 and orbits D=4, D=26 were NOT completed: SNF cost at m>=11
(rank + Smith on ~379-bit integer columns, 150 cluster trials x 6 cells + spread + 300 random
per m) exceeded the run budget; the sweep was stopped after D=425 m=10. Explicit truncation,
not full coverage. (3) Bounded random search (150-300 trials/cell) gives a LOWER bound on the
true adversarial min: the real inf could be smaller, so this is evidence the aggregate does NOT
collapse, not a proof it grows. The rigorous target is unchanged: a DIRECT lower bound on
log q_min (confluent-Vandermonde / det-D_m growth, §6c-6d) that no per-prime floor supplies.
RH stays [OUT].

### 6y. VERIFIED determinantal identity q_min = D_m(A)/D_m([A|d]) — the aggregate reduces to a gcd-gap (this session)

`discovery/probe_qmin_det_ratio.py` (exact integer Bareiss dets, minimal valid collisions K=m).
Tested the clean identity for the aggregate barrier quantity:

    (IDENT)   q_min  =  D_m(A) / D_m([A|d])        D_r = gcd of r x r minors.

HELD EXACTLY on 5307/5307 valid collisions, all 3 orbits, cluster/spread/random adversaries
(cross-checked against the independent SNF `qmin_fast`). So (IDENT) is a verified determinantal
reformulation: log q_min = log D_m(A) - log D_m([A|d]). For K=m this is concrete —
D_m(A)=|det of the m x m matrix| = (unit)*prod_k(x_k-1)*prod_{k<l}(x_l-x_k) (§6g factorization),
and D_m([A|d]) = gcd over the m drop-one-column augmented m-minors, each = (unit)*prod(x_k-1)*
Vand(S')*Psi(S') (§6i). Adversarial-MIN q_min channel decomposition (log2), D=425:

  m        :  2      3      4      5       6       7       8       9
  D_m(A)   : 45.2  280.3  473.9  1038.1  2444.6  3160.7  4401.7  8315.0
  D_m([A|d]): 41.3  248.5  403.2   935.6  2327.6  2998.0  4193.6  8060.0
  q_min    :  3.9   31.8   70.8   102.5   117.0   162.7   208.1   255.0   (= difference)

Both determinantal channels grow QUADRATICALLY in log2 (the prod_{k<l}(x_l-x_k) confluent-
Vandermonde mass), but the adversary keeps the d-augmented gcd within a LINEAR gap of the full
determinant — the difference log q_min grows ~+35/step (linear). Identical pattern on D=4, D=26
(both reach ~245-255 at m=9). READING (L5): the aggregate OP1 target now has a SHARP rigorous
form — prove log D_m(A) - log D_m([A|d]) >= c*m. Both sides are explicit determinantal divisors
of the SAME confluent-Vandermonde structure (d is the off-line orbit-sum column); the barrier
is "the d-augmented gcd cannot track the full determinant to within o(m)". This is the cleanest
handle yet and, unlike the per-prime floor (§6w), it is aggregate so it survives prime-mass
migration. IDENT is a candidate [THM] (exact, 5307/5307); the gcd-gap lower bound is OPEN.
Bounded search, K=m, m<=9 — evidence, not proof. RH stays [OUT].

### 6z. TWO-CHANNEL decomposition: q_min splits into a GEOMETRIC (Vandermonde) channel and a node-independent RAMIFIED channel (this session)

Attacking the §6y gcd-gap, I tried to make it interpretable via a clean per-node law. Using the
§6g/§6i factorizations, the j-th augmented minor (drop node j, keep d) equals D_m(A)*Psi(S_j)/W_j
up to a global unit, W_j := (x_j-1)*prod_{l!=j}(x_l-x_j) the confluent factor of node j and
Psi(S_j) := 2 Re[(u-1) prod_{l!=j}(u-x_l)]. Since `cleared_columns` scales EVERY column (incl. d)
by one common denominator, the per-node clearing factor cancels, and det(A) itself is one of the
augmented minors (drop the d-column), so the exact law is

    (EXACT, tautological)  v_p(q_min) = -min(0, min_j [ v_p(minor_j) - v_p(D_m(A)) ]),
    (PN, model)            v_p(q_min) =? max(0, max_j [ v_p(W_j) - v_p(Psi(S_j)) ]).

`discovery/probe_qmin_pernode_formula.py`: (PN) held only ~83% over odd p | q_min.
`discovery/probe_pn_diagnose.py`: per node, `actual_j := v_p(minor_j)-v_p(D_m(A))` vs
`model_j := v_p(Psi(S_j))-v_p(W_j)`. The offset `actual_j - model_j` is CONSTANT across j at some
primes (e.g. p=17: -4,-4,-4,-4 => model right up to a global unit) but VARIES across j at others
(p=5: -6,-6,-6,-5). `discovery/probe_pn_goodprime.py` was decisive: at every "GOOD" prime (nodes
distinct mod p, denominators invertible) the model held 0/295 — at p=17 (D=425 = 5^2*17) the model
predicts pred=0 while v_17(q_min) = 3,4,5 for m=3,4,5 with nodes fully generic mod 17. So the
confluent-Vandermonde per-node model is STRUCTURALLY BLIND to the orbit-ramified primes, even when
the node geometry is non-degenerate there. Their mass comes from the off-line vector d's own
arithmetic (ramification of the orbit field Q(u)), not from node isolation.

This forces a two-channel picture:

    log q_min = [ GEOMETRIC:  sum_{p geometric}  v_p log p ]   (node clustering; §6g Vandermonde floor governs this)
              + [ RAMIFIED:   sum_{p | D_orbit}   v_p log p ]   (off-line d arithmetic; node-INDEPENDENT)

`discovery/probe_qmin_ramified_channel.py` (D=425, ramified odd primes {5,17}) adversarially
MINIMIZES each channel separately over cluster/spread/random, m=2..9:

  m               :   2     3      4      5      6      7      8      9
  min RAMIFIED log2:  2.32  4.09  11.05  15.14  23.22  30.28  29.73  48.40
  min GEOMETRIC log2: 0.00 14.21  28.52  56.36  74.75 104.96 146.48 170.08

The GEOMETRIC channel is drainable to 0 (m=2) but the RAMIFIED channel CANNOT be driven to 0 — its
minimum stays positive and RISES ~linearly with m (min = log2(5) at m=2, i.e. v_5 >= 1 forced),
independent of node geometry. READING (L5): this is a NEW, node-independent lower-bound ingredient
that the §6g Vandermonde floor does not touch, and it explains BOTH earlier prime-by-prime failures
(§6u lag, §6w per-prime floor): those routes lived in the geometric channel and were blind to the
ramified channel that actually pins q_min from below. The danger q_min -> 1 now requires draining
BOTH channels at once, and the ramified channel is bounded below by the orbit's ramification (a
D_orbit-dependent, node-free quantity). SCOPE/HONESTY: (PN) is a candidate [THM] only at good
(unramified, non-collision) primes and is FALSE at the mass-carrying ramified primes; the two-
channel split and the ramified floor are EVIDENCE (bounded search, one orbit fully tabulated,
m<=9), not proof. The rigorous forward target sharpens to: lower-bound the ramified channel by a
node-independent function of D_orbit growing with m, and combine with the §6g geometric floor.
Exact arithmetic (L9). RH stays [OUT].

### 6z-note. RETRACTION — the ramified channel IS drainable; §6z's node-independent floor was a search artifact (this session)

Per CLAUDE.md ("verify load-bearing claims by script; defects are never assumed independent"),
before building on §6z I tried to REFUTE its own key claim. §6z asserted the ramified part
R(nodes) = v_5(q_min)*log2(5) + v_17(q_min)*log2(17) (D=425 = 5^2*17) "cannot be driven to 0 and
rises with m", based on a GENERIC cluster/spread/random attack (`probe_qmin_ramified_channel.py`)
that never targeted {5,17}. But §6b had recorded a D=425 config with q_min = 3^5*7^2*11 (v_5=v_17=0)
— a direct contradiction. `discovery/probe_ramified_drain.py` runs a TARGETED attack (nodes with
5,17 not dividing any denominator 4t^2+1; distinct x-classes mod 5 and mod 17; plus coordinate
descent minimizing R). Result (exact SNF):

  m               :   2     3     4     5     6     7     8
  min v_5(q_min)  :   0     0     0     0     0     0     0
  min v_17(q_min) :   0     0     0     0     0     1     1
  min R (log2)    : 2.32  2.32  4.09  2.32  0.00  8.17 12.26
  R = 0 found?    :  no    no    no    no   YES    no    no

Each ramified prime is INDIVIDUALLY drainable to 0 at every m (min v_5 = 0 always; min v_17 = 0
through m=6), and at m=6 a VALID collision drives BOTH to 0 simultaneously (R=0) — exactly the
kind of config §6b saw. So the ramified channel is NOT a node-independent floor; §6z's floor claim
is RETRACTED. The residual positive min R at m=2..5,7,8 is bounded-search DIFFICULTY (the joint
drain is a codimension condition that is only intermittently hit), not a genuine barrier — its
erratic pattern (0 at m=6, positive at m=7) is the signature of a search artifact, not a floor.

WHAT SURVIVES §6z (still valid): (a) the (PN) per-node model refutation — the confluent-Vandermonde
law v_p(q_min)=max(0,max_j[v_p(W_j)-v_p(Psi(S_j))]) is FALSE at ramified/collision primes (0/295 at
"good" primes; blind to p=17); (b) the two-channel split as a DESCRIPTIVE decomposition. WHAT IS
RETRACTED: any claim that the ramified channel carries a node-independent lower bound.

CONSOLIDATED LESSON (now three times over — §6u lag, §6w per-prime floor, §6z ramified channel):
q_min's p-adic mass is FULLY MOBILE. Any single prime, and either channel, can be adversarially
drained to 0 individually; draining one only pushes mass elsewhere. NO per-prime and NO per-channel
handle is a floor. The ONLY object that has resisted every draining attack is the AGGREGATE
log q_min (§6x direct min grows ~linearly; §6y = the exact gcd-gap log D_m(A) - log D_m([A|d])).
So the sole rigorous forward target reverts cleanly to §6y: prove log D_m(A) - log D_m([A|d]) >= c*m
as an AGGREGATE determinantal statement — not via any prime- or channel-localized decomposition,
all of which are now known to be drainable. Exact arithmetic (L9); bounded search, one orbit.
RH stays [OUT].

### 6z-agg. The aggregate floor SURVIVES the strongest draining attack; clean (LCM) reformulation (this session)

Having proved every per-prime (§6w) and per-channel (§6z-note) handle DRAINABLE, the honest worry
is symmetric: can the AGGREGATE log q_min itself be driven sub-linear by the very technique
(coordinate descent) that drained the ramified channel to 0?  probe_qmin_aggregate_stress.py turns
the full arsenal — coordinate descent + cluster/spread/random starts, the same moves that achieved
R=0 in probe_ramified_drain — on min log2(q_min) directly (D=425, K=m, exact SNF + exact rational
solve; L9).  Result (min log2 q_min over the whole attack):

    m:        2     3      4      5      6      7      8      9
    min log2: 4.00  18.16  39.22  45.78  76.94  95.77  101.59 129.32
    d/dm:      -    +14.16 +21.06 +6.56  +31.16 +18.83 +5.82  +27.73

The increment d/dm is noisy but stays POSITIVE throughout and averages ~18/m (line fit m=3→9:
slope ≈ 18.5).  The aggregate does NOT collapse toward 0 under the exact attack that trivially
drained the ramified channel.  This is the sharpest evidence yet for the §6y aggregate floor:
localized mass is fully mobile, but the total refuses to move below ~linear.  (m≥10 was cut for
cost — the cluster-heavy descent produces large-entry m×m matrices whose SNF is very slow; NOT a
silent cap, L5.  The m=2..9 trend is already decisive and monotone-positive in the cumulative min.)

CLEAN REFORMULATION verified EXACTLY (400/400 across all m):

    (LCM)  q_min = lcm of denominators of x = A^{-1} d,   where A x = d over Q.

Proof of (LCM): q·d ∈ colspan_Z(A) = L  ⟺  q·(A^{-1}d) ∈ Z^m (since d = A x ⟹ q d = A(q x), and
A has full column rank so A(q x) ∈ A·Z^m ⟺ q x ∈ Z^m).  The least such q is lcm_j den(x_j).  This
equals D_m(A)/D_m([A|d]) by Cramer (minor_j = D_m(A)·x_j, D_m([A|d]) = gcd(D_m(A),{minor_j})).  So
the §6y target log D_m(A) − log D_m([A|d]) ≥ c·m is IDENTICALLY the statement that the rational
solution of the confluent-Vandermonde system A x = d (expressing the off-line orbit-sum d in the
on-line confluent basis) has coordinate denominators whose lcm grows exponentially.  This recasts
the aggregate barrier as a single denominator-of-linear-solve bound — no prime/channel split — which
is the right shape for a resultant/discriminant lower bound and the sole surviving forward target.

### 6aa. RESULTANT ANATOMY of q_min: two channels pinned; naive S-unit lower bound REFUTED (this session)

Chasing the (LCM) target we identified the exact algebraic structure.  From C_j = 4(1 - T_j(x)) and
_phi_re = Re[1-(1-1/rho)^j], the moment variable is w = 1 - 1/rho: ON-LINE (rho=1/2+it) has |w|=1 so
Re[w^j]=T_j(x), x=(4t^2-1)/(4t^2+1) — pure Chebyshev; OFF-LINE (sigma!=1/2) has |w|!=1 — a general
moment.  So A = 4(J - M), M_{jk}=T_j(x_k) (Chebyshev-Vandermonde), and c = A^{-1}d is the quadrature
reproducing off-line moments with on-line unit-circle nodes.  probe_qmin_resultant_anatomy +
probe_qmin_geometric_identity (exact, D=425) pin q_min's prime anatomy into TWO channels:

  * GEOMETRIC: with G := prod_{k<l}(t_k^2 - t_l^2) (Vandermonde in t^2; note x_k-x_l =
    8(t_k^2-t_l^2)/[(4t_k^2+1)(4t_l^2+1)]), for GENERIC odd primes p (p not in {2,3} and not an
    off-line norm prime) the observed relation is the ONE-DIRECTIONAL bound
        v_p(q_min)  <=  v_p(G)      (delta_p := v_p(q_min)-v_p(G) is <=0 in EVERY sample, never >0).
  * RAMIFIED: p in {5,17} = odd parts of the atom norms |rho|^2 = sigma^2+tau^2 = 25/16 and
    (1-sigma)^2+tau^2 = 17/16 (this is literally why D=425=5^2*17).  Here v_p(q_min) is POSITIVE,
    absent from G, and GROWS with m (v_17: ~3-4 at m=3, ~5-6 at m=5).  A separate source.

REFUTATION (L5) of the naive lower-bound route: the clean identity v_p(q_min)=v_p(G) is FALSE.
delta_p<=0 always, and the delta==0 fraction DECAYS with m: 0.851, 0.792, 0.641, 0.548 for m=3,4,5,6.
So G strictly OVER-counts the geometric channel more and more; the "lost" valuation v_p(G)-v_p(q_min)
is exactly the per-prime cancellation absorbed by the augmented gcd D_m([A|d]) (off-line column d
sharing p with the minors).  That is the SAME per-prime mobility seen in §6w/§6z-note, now given its
algebraic cause.  Consequences:
  (i)  the geometric channel is UPPER-bounded by G, hence drainable by making G {2,3,5,17}-smooth —
       confirming §6z-agg's finding that this channel alone collapses;
  (ii) the naive "log q_min >= log(G with small primes removed)" S-unit lower bound does NOT go
       through, because v_p(q_min) can be 0 while v_p(G)>0 (full cancellation);
  (iii) therefore the AGGREGATE floor has NO per-prime closed form: it is precisely the two-channel
       DRAIN-CONFLICT — smoothing G (geometric drain) needs one node family, spreading nodes mod
       {5,17} (ramified drain) needs an incompatible one; §6z-agg shows they cannot be satisfied at
       once, leaving the ~linear residual.  A rigorous OP1 bound must quantify this conflict (e.g. an
       S-unit/smoothness impossibility for G SIMULTANEOUS with a mod-{5,17} spread), not a single
       resultant.  WHAT SURVIVES as a clean sub-result: the one-directional v_p(q_min) <= v_p(G) for
       generic p (an exact upper structure on the geometric channel).  Exact arithmetic (L9); bounded
       one-orbit evidence; RH [OUT].

### 6ab. The DRAIN-CONFLICT confirmed: the aggregate floor IS the two-channel incompatibility (this session)

probe_qmin_conflict maps the (ram_log2, geo_log2) Pareto frontier over structured smooth families
(consecutive / geometric / 2^k+1 nodes), random sets, mod-{5,17}-spread seeds, and coordinate descent
targeting EACH channel and the joint total (D=425, exact SNF).  Result:

    m |  min ram (geo there) | min geo (ram there) | min TOTAL | min max(ram,geo)
    3 |   0.00 ( 25.96)      |   4.00 ( 22.11)     |   20.50   |   14.09
    4 |   4.64 ( 52.56)      |  11.98 ( 28.52)     |   32.62   |   24.15
    5 |   0.00 ( 76.05)      |  19.56 ( 37.25)     |   56.81   |   32.05
    6 |   0.00 ( 96.57)      |  26.61 ( 43.66)     |   69.35   |   43.66
    7 |   6.97 ( 91.94)      |  33.19 ( 54.71)     |   87.90   |   52.39
    8 |   0.00 (165.33)      |  39.58 ( 65.76)     |  105.35   |   61.12

The two channels are STRONGLY ANTI-CORRELATED: whenever the ramified part is driven to 0 (m=3,5,6,8)
the geometric part is huge (25.96 -> 165.33, growing fast); whenever the geometric part is minimized
(4->40, ~linear) the ramified cost paid is large (22->66, ~linear).  The balance witness
min max(ram,geo) grows cleanly ~linearly (14.09, 24.15, 32.05, 43.66, 52.39, 61.12; slope ~9.4/m) and
NEVER approaches 0.  So NO node set drains both channels: the §6z-agg aggregate floor is CONFIRMED
(this orbit, bounded search) and is EXACTLY the two-channel incompatibility.

MECHANISM (now explicit and testable): smoothing G = prod(t_k^2 - t_l^2) — the geometric drain —
demands structured/clustered nodes (consecutive t give G that is (2m)-smooth); draining the ramified
channel demands nodes with DISTINCT x-residues mod 5 and mod 17 — a spread condition.  Clustering for
smoothness collides residues (raises ramified); spreading residues destroys smoothness (raises the
odd-prime support of G, hence geometric).  These are incompatible node-family requirements.

STATUS (L5): this is the sharpest EVIDENCE for OP1's aggregate floor and fully characterizes the
barrier, but it is NOT yet a theorem.  The precise rigorous target is now a clean number-theoretic
statement, no longer about q_min directly:
    (CONFLICT) For D=425 there is c>0 s.t. for every m and every m-subset {t_k},
        max( v_5,17-weight of the off-line quadrature ,  odd-prime-log of G outside {2,3,5,17} )  >= c*m,
    i.e. one cannot simultaneously make G {2,3,5,17}-smooth AND keep the on-line nodes spread across
    the residue classes mod 5 and mod 17.  This is an S-unit-smoothness-vs-residue-spread
    incompatibility — plausibly attackable by S-unit finiteness (Evertse-Gyory) + a counting bound on
    smooth Vandermonde values, and would upgrade the empirical floor to a proof.  That is genuine
    analytic/arithmetic number theory input, tracked as the sole open OP1 target.  Exact arithmetic
    (L9); bounded one-orbit evidence; RH stays [OUT].

### 6ac. S-unit horn quantified: M(S)=4, and smooth-G forces q_min LARGE via ramified (this session)

Attacking the geometric horn of (CONFLICT).  probe_qmin_sunit_horn (exact, D=425) gives two concrete
facts.

T1 (Horn-1 finiteness, empirical).  The largest set {t_k} (searched t <= 300) with EVERY pairwise
t_k^2 - t_l^2 being {2,3,5,17}-smooth has size exactly 4: {1,2,3,7} (hand-check: differences of
squares are -3,-8,-48,-5,-45,-40, all {2,3,5}-smooth).  No 5-element smooth-G set exists in range.
This matches the S-unit heuristic: a_i:=t_i-t_1 with a_i,a_j,a_i-a_j all S-smooth forces the S-unit
equation a_j/a_i + (a_i-a_j)/a_i = 1, whose solutions are finite (S-unit finiteness; NOTE: to CITE
this as a theorem it must be source-verified per CLAUDE.md baseline discipline — here it is only a
heuristic supported by the exact search).  So for m >= 5, G ALWAYS has a prime outside {2,3,5,17}.

T2 (the sharper, asymmetric conflict).  For the smooth-G sets themselves, q_min is NOT small — it is
LARGE and RAMIFIED-dominated:
    nodes {1,2}      log2 q_min 12.64  (ram 11.05, geo 1.58,  #primes outside {2,3,5,17} = 0)
    nodes {1,2,3}    log2 q_min 26.11  (ram 22.11, geo 4.00,  #nonS = 0)
    nodes {1,2,3,7}  log2 q_min 47.91  (ram 33.16, geo 14.75, #nonS = 0)
So draining the geometric channel (making G smooth via CLUSTERED nodes) does the OPPOSITE of draining
q_min: the clustered nodes collide mod 5 and mod 17, driving v_5,v_17 up (this is the §6g pigeonhole
e_max floor applied to the ramified primes) — q_min's ramified part grows ~linearly (~11/node).  The
conflict is thus ASYMMETRIC and the floor robust: the geometric drain (smooth G) is exactly where the
ramified channel is LARGEST, and the ramified drain (spread mod {5,17}) is exactly where G is least
smooth (§6ab).  Neither corner is small.

HONEST GAPS to an OP1 super-polynomial proof (L5), unchanged by this step:
  (i)  CANCELLATION: v_p(q_min) <= v_p(G) can be strict (§6aa), so a non-smooth-G prime (m>=5) need
       not survive in q_min; the geometric horn cannot lower-bound q_min by itself.
  (ii) EVEN without cancellation, Horn-1 finiteness yields only O(1) primes outside {2,3,5,17}, i.e.
       a CONSTANT geometric floor, not the omega(log m) that super-polynomiality needs.
The empirically robust growth (min max(ram,geo) ~ linear, §6ab; ramified ~ linear on smooth-G, T2)
therefore lives in the RAMIFIED channel on clustered nodes — governed by the PROVEN §6g e_max
pigeonhole floor v_p(D_m(A)) >= ceil(2m/(p+3))-1 for p in {5,17} — but transferring that NUMERATOR
floor to q_min = D_m(A)/D_m([A|d]) is blocked by the same augmented-gcd cancellation.  So the clean
open target is now precise: show the augmented gcd D_m([A|d]) cannot absorb the full §6g ramified
e_max floor uniformly, i.e. v_p(q_min) >= (a positive fraction of) ceil(2m/(p+3)) for p in {5,17}
on clustered nodes AND the geometric horn covers the spread nodes.  That non-absorption is the one
missing rigorous input; everything else is proved or exact-verified.  RH stays [OUT].

VERIFIED combinatorial fact behind the ramified pressure (probe, exact): the map x=(4t^2-1)/(4t^2+1)
has only TWO finite residues mod 5 ({0,4}; pole classes t == +-1 mod 5) but EIGHT mod 17 ({0,3,4,6,
11,13,14,16}; pole classes t == +-2 mod 17).  So mod 5 any m>=3 nodes MUST collide in x-class (only 2
classes) -> forced confluence -> strong §6g e_max pressure at p=5; mod 17 allows up to 8 distinct
classes, so nodes can be spread through m<=8 -> 17 is the more drainable ramified prime (consistent
with §6z-note draining v_17 to 0 through m=6 but not the tighter mod-5 side).  This asymmetry (2 vs 8
classes) is why {5,17} behave differently and why the mod-5 confluence is the harder-to-drain corner.

### 6ad. NON-ABSORPTION on clustered nodes CONFIRMED, but NARROW (this session)

Direct test of the §6ac "missing rigorous input" (probe_qmin_nonabsorption, exact, L9).  Using the
IDENT identity q_min = D_m(A)/D_m([A|d]) and Cramer (K=m), the m-minors of [A|d] are {det A} and
{minor_j := det(A, col j -> d) = D_m(A)*x_j}, so
    v_p(q_min) = v_p(det A) - min_j v_p(minor_j)                              (RESIDUAL)
(cross-checked against qmin_fast, independent SNF, 100% on every row below).

On the MAX-CLUSTER family {t0 + p*i : i<m} (a SINGLE on-line x-class mod p, full §6g confluence),
the augmented gcd does NOT absorb the numerator floor -- v_p(q_min) GROWS LINEARLY, and a coordinate-
descent adversary RESTRICTED to single-class nodes cannot drive it below that line:
    p=5 : v_5(q_min)  = 5, 8, 11, 14, 18, 21, 24   for m=2..8   (~3m-1, slope ~3/node)
    p=17: v_17(q_min) = 3, 5, 7, 9, 11, 13, 15     for m=2..8   (EXACTLY 2m-1)
Contrast (T3, spread family, distinct x-classes): v_17(q_min) drops to 2,3,4,5,6,7 -- drainable
(consistent with §6z-note).  So NON-ABSORPTION is REAL but requires FULL single-class clustering.

### 6ae. Per-p pigeonhole floor REFUTED: the adversary drains v_p to 0 (this session)

The tempting upgrade: the number of finite on-line x-classes mod p is FIXED
    N(3)=2, N(5)=2, N(7)=4, N(13)=6, N(17)=8   (probe_qmin_pigeonhole_floor T0, exact;
    N(p) is the image size of x=(4t^2-1)/(4t^2+1) mod p, ~ (p-1)/2 for larger p, but only 2 for 3,5).
Since N(5)=2, pigeonhole forces >= ceil(m/2) nodes into one x-class mod 5 for EVERY node set, so IF
§6ad non-absorption held at that PARTIAL confluence depth, v_5(q_min) would have an UNCONDITIONAL
floor ~ m/2 -- a clean per-p rigorous nugget, and the danger q_min->1 would be impossible.

It does NOT.  The UNRESTRICTED per-p adversary (random + pigeonhole-optimal spread + descent
minimizing v_p) drives BOTH primes to ZERO:
    m       = 2  3  4  5  6  7  8
    min v_5(q_min)  = 0  0  0  0  0  0  0
    min v_17(q_min) = 0  0  0  0  0  0  0
(m=9 cost-truncated: the m=9 unrestricted-descent SNF hit the large-integer pathology and was
stopped, NOT silently dropped; the m=2..8 trend is unambiguous.)  So the pigeonhole-forced PARTIAL
confluence (ceil(m/2) nodes in one class) IS fully absorbed by the augmented gcd: min_j v_p(minor_j)
rises to meet v_p(det A) once the adversary uses BOTH classes with a suitable p-adic pattern.  §6ad's
non-absorption is genuine but bites ONLY at FULL single-class clustering, which the adversary avoids.

CONSEQUENCE (the barrier is IRREDUCIBLY AGGREGATE).  No single ramified prime carries an OP1 floor:
for each p in {5,17} the adversary has a node set with v_p(q_min)=0.  This CLOSES the entire "per-p
clustered non-absorption lemma" route (the last per-prime hope) and confirms the §6ab picture: the
floor, if real, lives ONLY in the two-channel INCOMPATIBILITY (draining every p at once forces some
OTHER channel -- geometric G, or a different ramified prime -- large).  The rigorous target is thus
NOT a per-p statement but a genuine JOINT/aggregate bound: no single node set simultaneously makes
v_5=v_17=0 AND keeps G {2,3,5,17}-smooth.  (6th refuted per-prime route; the aggregate floor -- §6z-agg
linear min-TOTAL 4,18,39,46,77,96,102,129 for m=2..9 -- still stands under every joint attack tried.)

### 6af. JOINT ram-drained smoothness floor: S-unit finiteness moved onto q_min ITSELF (this session)

§6ac's S-unit horn was stated on G = prod(t_k^2-t_l^2), which suffers CANCELLATION: v_p(q_min) <= v_p(G)
only (§6aa), so a large prime in G need NOT survive into q_min -- that gap killed the G-route.  NEW
angle (probe_qmin_joint_smoothness, exact, L9): apply the smoothness/finiteness argument to q_min
DIRECTLY.  Define the RAM-DRAINED LOCUS = node sets with v_5(q_min)=v_17(q_min)=0.  Adversarially
search it (500 random + descent) and read off min log2 q_min | ram=0 and the number of DISTINCT primes
> 17 in q_min there:

    m   | ram=0 reachable | min log2 q_min | ram=0 | #primes>17 | largest p | aggregate min (control)
    2   | YES             | 5.58                    | 0          | -         | 5.09
    3   | YES             | 19.27                   | 1          | 157       | 18.23
    4   | YES             | 45.65                   | 3          | 157       | 40.59
    5   | YES             | 79.76                   | 8          | 353       | 59.44
    6   | YES             | 113.18                  | 11         | 421       | 72.87
    (m>=7 cost-truncated: the ram=0 locus is increasingly RARE -- a leaner 250-sample search failed to
    hit v_5=v_17=0 at m=6 at all, though the 500-sample search did; NOT silently dropped.)

TWO readings, both honest:
  (+) On the ram-drained corner, q_min carries a GROWING large-prime part: #primes>17 = 0,1,3,8,11 and
      largest prime 157->421, so min log2 q_min | ram=0 grows super-linearly (5.6,19,46,80,113).  These
      primes are IN q_min (not merely in G) -- so the S-unit/finiteness mechanism transfers to q_min
      itself with NO cancellation gap.  This CLOSES §6ac's geometric-horn gap AT the ram=0 corner: you
      cannot drain {5,17} and keep q_min {2,3,5,17}-smooth; draining the ramified channel forces an
      unbounded, growing set of primes >17 into q_min.
  (-) But the aggregate adversary does NOT sit at ram=0.  The control column (unconstrained min log2
      q_min) is BELOW the ram=0 min, and the gap GROWS (0.49,1.04,5.06,20.32,40.31): the true optimum
      keeps SOME ramified mass rather than paying the full geometric large-prime price.  So §6af bounds
      only the ram=0 SLICE, not the aggregate optimum.

NET (barrier map, now crisp).  log q_min = ram_mass + geo_mass, with two PROVEN-mechanism endpoints:
  * ram_mass = 0  => geo_mass >= (growing #primes>17)*log19   [§6af, this section, no cancellation gap];
  * nodes fully spread (geo small) => ram_mass >= §6ad single-class confluence (but per-p drainable).
The aggregate optimum lives strictly BETWEEN these endpoints.  The sole remaining rigorous input is now
a JOINT INTERPOLATION/convexity bound: ram_mass + geo_mass >= c*m across the whole interior, not just at
the two endpoints.  Both endpoints are now controlled; the middle is the open nucleus.  This is a
genuinely different (and cleaner) target than the per-p or G-smoothness routes it replaces.

### 6ag. Trade-off frontier is NOT convex: the "endpoints + convexity" reduction fails (this session)

Tempting reduction of the §6af interior nucleus: if the trade-off frontier F(R) = min{ geo_mass :
ram_mass = R } were CONVEX and decreasing with both endpoints high, then the aggregate min
    min_node log q_min = min_R ( R + F(R) )
would be PINNED by the two (already-controlled) endpoints -- reducing OP1 to endpoints + a convexity
lemma.  probe_qmin_frontier_convexity maps F(R) (664 node sets/m: random + a lambda-sweep descent
minimizing geo_mass + lambda*ram_mass, lambda in {0,.25,.5,1,2,4,8,100}, binned by ram_mass) and runs
a discrete-convexity check (non-decreasing slopes), m=3..6:

    m | agg min = min_R(R+F(R)) | frontier convex?
    3 | 18.15                   | NO
    4 | 34.13                   | NO
    5 | 53.60                   | NO
    6 | 66.69                   | NO

TWO readings (L5):
  (+) The aggregate min log2 q_min grows ~linearly (18.15, 34.13, 53.60, 66.69; slope ~16/node),
      RECONFIRMING the §6z-agg floor under a THIRD, independent (lambda-sweep) adversary -- the floor
      itself is robust.  (Values differ from §6z-agg's cluster-descent line 18,39,46,77 because both are
      heuristic UPPER bounds on inf; the linear GROWTH is the invariant conclusion, not the exact value.)
  (-) The convexity route FAILS: slopes oscillate large-positive/large-negative (e.g. m=6: +75.0, -14.2,
      ..., +49.1, -32.7), so min_R(R+F(R)) is NOT pinned by the endpoints -- the binding configs are
      INTERIOR.  IMPORTANT CAVEAT: F(R) here is an empirical min-ENVELOPE (each bin's geo_mass is a
      heuristic upper bound on the true min), so the jaggedness is partly sampling noise; this does NOT
      rigorously prove the TRUE frontier is non-convex.  What it does establish: the clean "endpoints +
      convexity" reduction is NOT empirically supported and cannot be assumed.  The frontier shows a
      multi-valley structure whose swing magnitude exceeds plausible single-sample noise, hinting at
      genuine non-convexity.

NET.  The floor is real and linear under three independent adversaries, but its proof cannot route
through frontier convexity from the endpoints.  A rigorous OP1 floor must bound the INTERIOR configs
directly (e.g. a determinantal/height lower bound on log|det A| - log D_m([A|d]) that does not split
into the two channels), not interpolate between the ram=0 and fully-spread endpoints.

### 6ah. Shrink-ratio kappa = log|detA|/log q_min is UNBOUNDED: determinant route fails, floor reframed (this session)

Direct test of the §6ag-suggested route (probe_qmin_shrink_ratio, exact, L9).  Since q_min = |det A| /
D_m([A|d]) and D_m([A|d]) >= 1, always q_min <= |det A|, so kappa := log|det A| / log q_min >= 1.  IF
kappa were uniformly bounded by K, a PURE-determinant lower bound (Vandermonde/Hadamard, no gcd) would
give log q_min >= log|det A|/K -- OP1's floor without touching the two-channel interior.  Adversarially
maximizing kappa (= minimizing q_min, the OP1 danger direction):

    m | min log2 q_min | log2|det A| there | kappa there | MAX kappa seen
    2 | 3.32           | 52.59             | 15.83       | 15.83
    3 | 18.41          | 215.26            | 11.69       | 12.38
    4 | 35.96          | 357.18            | 9.93        | 13.80
    5 | 53.36          | 887.84            | 16.64       | 20.85
    6 | 77.95          | 1782.80           | 22.87       | 27.41
    (m=7 cost-truncated: the m=7 min-q descent was killed at the time budget before the final print; NOT
    silently dropped; the m=2..6 trend is decisive.)

READINGS (L5):
  (-) MAX kappa GROWS (15.8 -> 27.4; mild/noisy but clearly not constant), so the shrink ratio is NOT
      uniformly bounded: a constant-K reduction "log q_min >= log|det A|/K" FAILS.  The augmented gcd
      D_m([A|d]) can absorb an unboundedly growing SHARE of log|det A|.  Determinant-magnitude alone is
      NOT the source of the floor -- honest close of the direct-determinant route.
  (+) But log|det A| grows ~QUADRATICALLY (52,215,357,888,1783 ~ O(m^2), Vandermonde-in-x scale) while
      min log2 q_min grows LINEARLY (3.3,18.4,36.0,53.4,78.0) -- a FOURTH independent adversary
      reconfirming the linear floor.  So the gcd absorbs a QUADRATIC amount of det, leaving a LINEAR
      residue, and it is that last linear residue that is floored.

REFRAME (sharper than before).  OP1's floor is emphatically NOT "det A is large" (it is hugely large,
O(m^2) in log) -- the entire difficulty is that the augmented gcd cannot absorb the FINAL linear piece
of log|det A|.  That un-absorbable linear residue is precisely the two-channel content (§6ab/§6af): the
gcd freely eats the O(m^2) "bulk" (both the smooth Vandermonde growth and per-prime cancellable mass)
but is blocked on an irreducible O(m) core.  The rigorous target is therefore a lower bound on the
RESIDUE log|det A| - log D_m([A|d]) that is NOT via |det A| magnitude and NOT via per-p or convexity --
it must capture why the gcd's absorption saturates at det/O(m).  This is the true open nucleus.

### §6ai — Smith-invariant anatomy: WHERE the un-absorbable linear residue sits

The §6ah reframe (floor = the linear residue log|det A| - log D_m([A|d]) the gcd cannot eat) is made
STRUCTURAL by decomposing q_min per Smith invariant (probe_qmin_smith_anatomy, exact, L9).  Write the
integer matrix A = U diag(s) V (U,V unimodular over Z, s_1|s_2|...|s_m the invariant factors).  Then
Z^m/A Z^m = (+)_i Z/s_i, the class [d] maps to c = U^{-1} d, and the order of [d] -- which equals q_min
(the §6x IDENT) -- is
    q_min = lcm_i ( o_i ),   o_i := s_i / gcd(s_i, c_i).                       (ORDER)
The probe computes s and c exactly via a self-contained pivot-minimization SNF that also accumulates the
row transform U (an earlier hand-rolled clearing loop infinite-looped; the pivot-minimization version has
guaranteed termination), then checks lcm_i(o_i) == qmin_fast independently.

VALIDATION: xchk == True on ALL rows (m=3..7, min-q and generic adversaries) and 240/240 in the separate
validation run -- the ORDER formula and the SNF are confirmed.

ANATOMY (m=3..7; "min-q" = coordinate-descent minimizing log2 q_min; "generic" = random valid):

    m | adversary | log2 q_min | #o_i>1 | top-3 o_i (log2)        | log2 s_top
    3 | min-q     |      39.45 |      3 | [39.45, 19.91, 12.26]   |     190.78
    3 | generic   |      61.43 |      3 | [61.43, 19.23, 19.23]   |     212.12
    4 | min-q     |      68.47 |      4 | [68.47, 38.20, 27.22]   |     255.52
    4 | generic   |      97.16 |      4 | [97.16, 32.26, 21.55]   |     300.68
    5 | min-q     |      64.77 |      3 | [64.77, 33.91, 14.40]   |     334.23
    5 | generic   |     145.70 |      5 | [145.70, 51.27, 41.25]  |     520.00
    6 | min-q     |      85.25 |      5 | [85.25, 45.54, 25.17]   |     381.33
    6 | generic   |     189.66 |      6 | [189.66, 90.73, 69.37]  |     734.75
    7 | min-q     |     118.40 |      6 | [118.40, 86.75, 60.33]  |     581.34
    7 | generic   |     246.14 |      6 | [246.14, 100.94, 78.14] |     944.73

READINGS (L5):
  (structure) The floor is TOP-HEAVY: in every sampled row the largest o_i equals log2 q_min to the
      printed precision, i.e. q_min is often carried by a SINGLE cyclic component Z/s_j.  A dedicated
      50-per-m test (m=3..7, 250 node sets) makes this precise and HONEST: q_min == max_i o_i in
      213/250 = 85% of cases, but NOT universally -- in 37/250 = 15% the lcm genuinely spreads across
      >1 invariant (different primes peaking on different s_j), with q_min up to 289x (~8 bits) larger
      than the top single o_i.  So the floor is USUALLY, but NOT provably, a one-dimensional statement
      about a single cyclic factor; a rigorous reduction to "one component" would have to handle the
      15% multi-component tail, so it is NOT a clean localization.
  (gap) The surviving o_i>1 number ~m (3,4,3,5,6 at min-q) -- moderately diffuse, not O(1)-bounded.
  (mechanism) The TOP Smith invariant is enormous: log2 s_top grows ~QUADRATICALLY (190..581 at min-q,
      matching log|det A| = sum_i log s_i ~ O(m^2)), yet its surviving order contribution o_top is only
      log-LINEAR (39..118).  So the adversary aligns d with all but an O(m)-bit residue of the top
      invariant's factorization -- gcd(s_top, c_top) ~ s_top / exp(O(m)) -- but CANNOT eliminate that
      residue.  This is exactly the §6ah picture localized: the gcd eats the quadratic bulk of the top
      invariant and stalls on a linear core.  What it does NOT give is WHY c_top cannot be made to share
      the last O(m) bits of s_top's factorization; that (a bound on how well the fixed d aligns with the
      top cyclic factor) remains the open nucleus, now stated per-invariant rather than per-prime.

Bounded search, one orbit (D=425).  Evidence, not proof.  RH stays [OUT].

### §6aj — residue prime content: the min-q floor is SMOOTH and AGGREGATE over small primes

Factoring the adversarial-minimum q_min (probe_qmin_residue_primes, exact trial division to B=1e5, L9)
decides which proof toolkit the nucleus needs.  Best-of-6 coordinate descents to min log2 q_min, then
split q_min into ramified 5^a 17^b, generic small primes (<=B, excl 5/17), and a large cofactor (>B):

    m | log2 q | 5^a17^b | ram bits | #gen p | gen bits | largest p | cofactor bits
    3 |  24.01 | (3,0)   |    6.97  |   3    |  17.04   |    11     |   0.00
    4 |  37.99 | (4,3)   |   21.55  |   4    |  16.44   |    11     |   0.00
    5 |  59.43 | (1,2)   |   10.50  |   7    |  48.93   |    43     |   0.00
    6 |  72.47 | (3,3)   |   19.23  |   6    |  53.24   |    37     |   0.00
    7 |  89.98 | (4,4)   |   25.64  |   8    |  64.34   |    53     |   0.00

READINGS (L5):
  (1) COFACTOR BITS == 0 at every m; the largest prime factor is TINY (11,11,43,37,53).  The min-q q_min
      is an extremely SMOOTH number -- ALL prime factors <= 53 for m<=7.  This KILLS the S-unit / Baker
      "a few large primes" hypothesis outright: the floor has NO large-prime content whatsoever.  The
      adversary reaches its minimum precisely by making q_min friable (small primes only).
  (2) The ramified {5,17} do NOT vanish at the JOINT minimum (ram bits 7..26, ~20-30% of the total).
      This REFINES §6ae honestly: §6ae drained 5 and 17 individually, one prime-key at a time, but that
      does NOT survive simultaneous minimization of the whole q_min -- at the global optimum the ramified
      channel persists.  (Per-prime drainability =/= simultaneous drainability.)
  (3) The DOMINANT part is many small GENERIC primes (3,4,7,6,8 of them, all <=53), carrying the majority
      of the bits.  So the floor is an AGGREGATE over the small primes -- exactly the §6d/§6g pigeonhole
      floor v_p(D_m(A)) >= ceil(2m/(p+3))-1 summed over small p -- NOT a single-large-prime, single-Smith-
      invariant, or purely-ramified phenomenon.

REFRAME (sharpest yet).  The min-q q_min is B-smooth with B ~ small (largest prime grows very slowly,
~53 at m=7), and log q_min ~ O(m).  A smooth number of size exp(O(m)) with primes <= B has ~ O(m)/log B
prime-power factors: the floor is the SUM over small primes p of a per-prime valuation floor.  Any SINGLE
prime is drainable (§6ae), but they are NOT simultaneously drainable -- driving collisions mod one prime
(to zero v_p) forces spreading mod another.  The true open nucleus is therefore a SIMULTANEOUS small-prime
pigeonhole / CRT-tension bound: sum_{p<=B} v_p(q_min) log p >= c*m uniformly, because the m nodes cannot
be jointly aligned to N(p) x-classes for all small p at once.  This is markedly more concrete and classical
than the abstract residue log|det A| - log D_m([A|d]) -- it is a covering/incidence statement over a fixed
finite set of small primes.  Next: §6ak measures per-prime v_p(q_min) at min-q vs the pigeonhole floor
ceil(2m/(p+3))-1 to see which small primes are "active" and whether the aggregate is tight.

Trial division bounded (large cofactor would be left unfactored, but none occurs).  One orbit (D=425).
Bounded search.  Evidence, not proof.  RH stays [OUT].

### §6ak — CRT-tension cross-table: the floor is a SIMULTANEOUS small-prime pigeonhole

The §6aj nucleus (simultaneous small-prime pigeonhole) is tested head-on (probe_qmin_simul_pigeonhole,
exact, L9) with a cross-table: each ROW runs a coordinate descent MINIMIZING v_p(q_min) for one target
prime p; the ENTRIES are the resulting v_q(q_min) for every small q at that config; last columns are the
total log2 q_min and #{small primes with v_q=0}.  SMALL = {3,5,7,11,13,17,19,23}.

    m=4  min-q:   v=[7,4,1,0,0,0,0,0]  log2 q= 34.05  #zeroed=5     PH(3,4)=1
         min v_3: v=[2,5,1,1,1,5,2,1]  log2 q= 91.26  #zeroed=0
    m=6  min-q:   v=[6,6,3,1,0,2,1,0]  log2 q= 79.16  #zeroed=2
         min v_3: v=[4,5,2,2,2,6,0,1]  log2 q=202.23  #zeroed=1
    m=7  min-q:   v=[6,5,2,1,0,7,0,1]  log2 q= 88.19  #zeroed=2
         min v_3: v=[5,17,7,1,0,5,0,1] log2 q=239.78  #zeroed=2
    (min v_5/v_7/.../v_23 rows: each drives ITS target low but log2 q balloons to 57..268 -- see probe.)

READINGS (L5):
  (A) CRT TENSION IS REAL AND DECISIVE.  Along EVERY single-prime-target row the total log2 q_min balloons
      FAR above the balanced min-q row (m=4: 34 vs 57..114; m=6: 79 vs 133..202; m=7: 88 vs 185..268).
      Draining one prime FORCES the others up so much the total explodes: no configuration is good for all
      small primes at once.  The min-q optimum instead keeps ~6 of 8 small primes ACTIVE at moderate
      valuations -- the aggregate/balanced floor, exactly the §6aj picture.
  (B) #SIMULTANEOUSLY-ZEROABLE SHRINKS WITH m: the best row zeroes 5 primes at m=4, but only 3 at m=6 and
      2 at m=7 (min-q zeroes 5,2,2).  Pigeonhole pressure grows with m -- fewer small primes can be jointly
      killed -- so the un-zeroable complement (hence the aggregate floor) grows.
  (C) PRIME 3 IS A NON-DRAINABLE FLOOR CARRIER.  Unlike 5,7,17 (individually drainable to 0), prime 3 --
      the smallest x-image, N(3)=2 -- CANNOT be zeroed even when directly targeted: min v_3 = 2, 4, 5 at
      m = 4, 6, 7, GROWING ~linearly and always > PH(3,m)=ceil(2m/6)-1.  With m nodes forced into only 2
      x-classes mod 3, the confluent-Vandermonde v_3(det A) is huge and the augmented gcd cannot absorb it
      to 0.  This suggests the SHARPEST possible nucleus: a UNIFORM single-prime floor v_3(q_min) >= c*m,
      which alone would give log q_min >= c*m*log 3.  (Not yet confirmed un-drainable at larger m -- §6al.)

REFRAME (candidate reduction).  If v_3(q_min) >= c*m holds uniformly (the p=3 confluent-pigeonhole floor
survives the augmented-gcd absorption), OP1 reduces from an aggregate-over-all-small-primes statement to a
SINGLE-prime pigeonhole+confluence bound mod 3 -- classical and self-contained.  The cross-table already
shows 3 (and to a lesser degree 5) resisting drainage while 7,11,13,17 fall.  Next (§6al): aggressively
minimize v_3(q_min) alone over m=3..9 to test whether min v_3 grows linearly and never reaches 0.

One orbit (D=425).  Bounded search.  Evidence, not proof.  RH stays [OUT].

### §6al — the p=3 single-prime floor SUFFICES for OP1 (super-log threshold)

Aggressively minimizing v_3(q_min) alone (probe_qmin_p3_floor, 24-40 coordinate descents per m from
random + structured mod-3 starts, exact, L9).  x mod 3 takes only N(3)=2 values (classes {0},{2}); with m
nodes forced into 2 x-classes, the confluent-Vandermonde v_3(det A) is large, and the question is whether
the augmented gcd can absorb it to v_3(q_min)=0.

    m | min v_3 found | reached 0? | PH3=ceil(m/3)-1 | log2 q there
    3 |      0        |    True    |       0         |   64.80    (small-m boundary: drainable)
    4 |      2        |    False   |       1         |  102.17
    5 |      2        |    False   |       1         |  160.31
    6 |      4        |    False   |       1         |  218.99
    7 |      5        |    False   |       2         |  244.13
    8 |      5        |    False   |       2         |  322.25
    (m=9 cost-truncated: qmin_fast on the m=9 large-integer SNF exceeded the 500s budget; NOT silently
     dropped -- the m=4..8 trend is the evidence.)

READINGS (L5):
  (1) For m>=4, v_3(q_min) NEVER reaches 0 despite aggressive minimization (24-40 restarts + structured
      starts packing/spreading the two mod-3 classes), and GROWS (2,2,4,5,5 ~ 0.7(m-2)), always >= PH3.
      Prime 3 carries a POSITIVE, non-drainable per-prime floor for m>=4.  (m=3 drains to 0 -- a small-m
      boundary effect, excluded from the asymptotic claim.)
  (2) HONEST scope of the carrier: v_3*log3 ~ 8 bits at m=7 is a SMALL fraction of the ~88-bit total
      log q_min.  So prime 3 is NOT the dominant carrier -- the full floor is genuinely aggregate (§6ak).
      A "reduce the WHOLE floor to p=3" claim would be FALSE.

THE KEY CONSEQUENCE (why this still settles OP1).  OP1 is TRUE iff inf_A q_min(m) is super-polynomial in
m, i.e. log q_min = OMEGA-of-omega(log m) -- merely SUPER-LOGARITHMIC growth.  A single-prime LINEAR floor
    v_3(q_min) >= c*m   (c>0, m>=4)
gives  log q_min >= v_3(q_min)*log 3 >= c*log3 * m = omega(log m),  which SETTLES OP1 affirmatively
REGARDLESS of the small constant c.  We do NOT need the dominant carrier or the tight constant; ONE prime
with a linear (even much weaker, any super-log) floor is enough.  Prime 3 -- with the SMALLEST image
N(3)=2 and hence the simplest confluent-Vandermonde structure -- is the most tractable candidate.

REFRAME (the crisp open target, replacing the abstract residue bound).  Prove:
    THERE EXIST c>0, m_0 such that for all node sets and all m>=m_0,  v_3(q_min) >= c*m.
Route (classical, self-contained): (i) columns of A mod 3 fall into <= N(3)=2 equal-column classes (x_k
mod 3 determines the column mod 3), so rank_3(A) <= 2 and the confluent staircase gives v_3(det A) >=
c1*m; (ii) via the RESIDUAL identity v_3(q_min) = v_3(det A) - min_j v_3(minor_j) (minor_j = det with
col j -> the FIXED d), bound min_j v_3(minor_j) <= v_3(det A) - c*m, i.e. the fixed d cannot 3-adically
align with ALL m column-deletions at once.  This is a finite mod-3 incidence statement -- the same shape
as the §6d pigeonhole but now for a FIXED augmentation vector.  Next (§6am): verify v_3(det A) >= c1*m
directly and measure how much the augmented gcd absorbs, to confirm the residual gap is linear.

One orbit (D=425).  Bounded search.  Evidence, not proof.  RH stays [OUT].

### §6am — p=3 floor mechanism: both proof-route steps verified empirically

Direct exact measurement (probe_qmin_p3_mechanism, L9) of the §6al two-step route, over the adversarial
min-v_3 config and random configs (n0 = #nodes with t !≡ 0 mod 3 [x-class 0], n2 = #nodes with t ≡ 0
mod 3 [x-class 2]; n0+n2=m).  Residual identity: v_3(q_min) = v_3(det A) - min_j v_3(minor_j).

    m | config | (n0,n2) | v3(detA) | min_j v3(minor) | resid=v3(qmin) | xchk
    4 | min-v3 | (2,2)   |    3     |      1          |     2          | True
    4 | rand   | (4,0)   |   12     |      5          |     7          | True
    5 | min-v3 | (3,2)   |    6     |      4          |     2          | True
    6 | min-v3 | (4,2)   |    9     |      5          |     4          | True
    6 | rand   | (5,1)   |   21     |     11          |    10          | True
    7 | min-v3 | (5,2)   |   15     |     10          |     5          | True
    8 | min-v3 | (5,3)   |   21     |     16          |     5          | True
    8 | rand   | (8,0)   |   39     |     27          |    12          | True

READINGS (L5):
  (i) STEP (i) HOLDS.  v_3(det A) grows SUPER-linearly and is driven by WITHIN-class confluence: it is
      largest when nodes concentrate in one class ((8,0)->39, (7,1)->32, (6,1)->25) and smallest when the
      two classes are balanced.  Even the adversarial minimum (which balances) has v3(detA)=3,6,9,15,21
      for m=4..8 -- comfortably >= c1*m.  A confluent-Vandermonde staircase ~ sum_i C(n_i,2) (+ a cleared-
      denominator correction of ~1.5x) fits the ordering; the exact constant is not pinned but the LINEAR
      (indeed super-linear) lower bound is robust.
  (ii) STEP (ii) HOLDS.  The augmented gcd absorbs the super-linear BULK (min_j v3(minor) = 1,4,5,10,16 at
      the adversary, tracking most of v3(detA)) but CANNOT close the gap: the residual v_3(q_min) stays
      2,2,4,5,5 (~0.7(m-2), LINEAR, > 0) even under direct minimization.  The fixed d 3-adically aligns
      with most column-deletions but a linear residue survives.  xchk == True on ALL rows (residual
      identity == qmin_fast) -- the decomposition is validated.
  (iii) ADVERSARY STRUCTURE (new).  The min-v_3 optimum keeps n2 (class t ≡ 0 mod 3) SMALL (≈2) and packs
      the rest into class 0 -- but does NOT push n2 to 0: pure concentration (n2=0: (4,0),(8,0)) gives a
      HIGHER residual (7,12).  There is an INTERIOR optimum at small n2.  Interpretation: the fixed d
      absorbs the class-0 confluence well but leaves an un-absorbable residue tied to the presence of a
      few class-2 nodes -- localizing WHERE the linear floor lives (the minority class relative to d).

STATUS OF THE p=3 LEMMA.  Both steps of the §6al route are empirically supported with the residual identity
validated.  The one hard step remaining for a PROOF is the linear LOWER bound in (ii): showing the fixed d
cannot 3-adically align with all m column-deletions to within o(m) -- a fixed-vector mod-3 incidence bound
(the same shape as the §6c/§6d "fixed off-line vector meets the top cyclic factor" gap, now isolated to a
SINGLE prime and a 2-class partition).  This is the crispest, most classical open sub-problem the whole
§6a* line has produced.  It is a candidate for an outsource problem (EXT) once stated self-contained.

One orbit (D=425).  Bounded search.  Evidence, not proof.  RH stays [OUT].

### §6an — EXACT Vandermonde reduction: v_p(det A) = sum_{k<l} v_p(x_k - x_l) (step (i) nailed)

Testing whether v_3(det A) reduces to the Vandermonde 3-adic distance sum (probe_qmin_p3_vandermonde,
exact, L9).  A_{j,k} = 4(1 - T_j(x_k)), {T_j}_{j>=1} a graded polynomial basis (deg T_j = j, leading
coeff 2^{j-1}).  Measuring VD := sum_{k<l} v_3(x_k - x_l) and CORR := v_3(det A) - VD over random and
adversarial min-v_3 node sets, m=3..8:

    CORR == 0 in EVERY case (all m, all configs).  Not O(m) -- EXACTLY zero.

So
    v_3(det A) = sum_{k<l} v_3(x_k - x_l)                                           (EXACT)

READINGS (L5):
  * The "4(1 - .)" prefactor (4 and the leading coeffs 2^{j-1}) are 3-ADIC UNITS, and the all-ones rank-1
    shift from the constant "1" contributes no 3-adic valuation: the change of basis T_j <- monomials is
    triangular with unit-at-3 diagonal, so 3-adically det A equals the pure Vandermonde prod_{k<l}(x_l-x_k)
    times a 3-unit.  This makes STEP (i) a CLASSICAL, PROVABLE confluent-Vandermonde identity -- no
    correction to control.  v_3(det A) grows exactly as the sum of 3-adic node distances; concentration in
    an x-class mod 3 (each pair then has v_3 >= 1) forces the super-linear growth seen in §6am.
  * PRIME-GENERIC: the only primes that could spoil the unit-diagonal argument are those dividing the
    leading coeffs 2^{j-1} and the 4 -- i.e. ONLY p=2.  For EVERY odd prime p,
        v_p(det A) = sum_{k<l} v_p(x_k - x_l).
    So step (i) holds for all odd p, not just 3: v_p(det A) is a pure p-adic ultrametric distance sum on
    the nodes' x-values.  (p=2 is separate; the ramified primes here are 5,17, both odd, both covered.)

CONSEQUENCE for the p=3 lemma.  Combined with the residual identity (§6am),
    v_3(q_min) = v_3(det A) - min_j v_3(minor_j)
             = sum_{k<l} v_3(x_k - x_l) - min_j v_3(minor_j),
and (§6an applied to each minor, whose matrix is A with column j replaced by the FIXED off-line vector d)
the whole p=3 floor is now a PURE p-adic ultrametric quantity on the nodes' x-values and the off-line
orbit's (algebraic) x-values.  The remaining open step (the linear lower bound on the residual) is thus a
clean statement in 3-adic ultrametric geometry -- see §6ao (next) for the off-line/minor side.

One orbit (D=425).  Bounded search.  Evidence, not proof.  RH stays [OUT].

### §6ao — off-line ultrametric decomposition: a NEAR-COMPLETE proof skeleton for the p=3 floor

With v_3(det A) = sum_{k<l} v_3(x_k - x_l) (§6an) and the residual identity (§6am), define per deleted
node j:  N_j := sum_{k != j} v_3(x_j - x_k) (node j's 3-adic closeness to the cluster),
VD_j := sum_{k<l, k,l != j} v_3(x_k - x_l), and  C_j := v_3(minor_j) - VD_j (the OFF-LINE closeness term).
Then v_3(det A) = VD_j + N_j and R_j := v_3(det A) - v_3(minor_j) = N_j - C_j, with v_3(q_min) = max_j R_j.
Measured (probe_qmin_offline_ultrametric, exact, L9) over random and adversarial min-v3 sets, m=4..8:

    * chk == True on ALL rows: v_3(q_min) == max_j (N_j - C_j).  The ultrametric decomposition is EXACT.
    * max_j C_j is BOUNDED: values seen are 0,0,0,1,0,1,0,0,0,1,4,0,2,0,3 across all m up to 8 (max = 4).
      It does NOT grow with m -- the fixed off-line orbit CANNOT 3-adically shadow the node cluster.
    * many rows have C_j == 0 entirely (the off-line atoms' x-values are 3-adically SEPARATED from the
      rational node classes: v_3(xi_atom - x_k) = 0 generically).

NEAR-COMPLETE PROOF SKELETON of the p=3 floor  v_3(q_min) >= c*m  (hence, by §6al, of OP1):
  (1) [§6an, provable] v_3(det A) = sum_{k<l} v_3(x_k - x_l): confluent-Vandermonde with unit-at-3 diagonal.
  (2) [pigeonhole, provable] x has only N(3)=2 classes mod 3, so any m nodes have at least
      C(ceil(m/2),2) + C(floor(m/2),2) ~ m^2/4 - m/2 SAME-class pairs, each with v_3(x_k - x_l) >= 1; hence
      v_3(det A) >= m^2/4 - O(m).  (Quadratic, unavoidable -- the adversary balancing the two classes only
      hits this minimum.)
  (3) [averaging, provable] sum_j N_j = 2 sum_{k<l} v_3 = 2 v_3(det A), so max_j N_j >= 2 v_3(det A)/m >=
      m/2 - O(1).
  (4) [§6ao, the ONE remaining lemma] max_j C_j = O(1).  Then
          v_3(q_min) = max_j (N_j - C_j) >= max_j N_j - max_j C_j >= m/2 - O(1).
  ==>  log q_min >= v_3(q_min) * log 3 >= (m/2 - O(1)) log 3 = omega(log m)  ==>  OP1 is TRUE.

STATUS (L5).  Steps (1)-(3) are classical and essentially proved (the identity (1) verified exactly in
§6an; (2) is pure pigeonhole on 2 classes; (3) is averaging).  The whole open problem is now compressed to
the SINGLE lemma (4): the FIXED off-line orbit's atoms (x-values of {sigma +- i tau, (1-sigma) +- i tau},
sigma=3/4, tau=1) have BOUNDED 3-adic closeness to any rational node cluster, i.e. C_j <= B for an
absolute B.  Empirically B <= 4 for m<=8, and C_j = 0 whenever the off-line atoms do not reduce into the
node's mod-3 x-classes.  This is a concrete, finite arithmetic statement about ONE fixed algebraic orbit --
the crispest and most tractable target the entire §6a* line has produced, and a strong outsource (EXT)
candidate.  Caveat: verified for D=425 and m<=8 only; the O(1) bound on C_j is evidence, not yet a proof,
and could in principle grow slowly -- §6ap will stress-test max_j C_j to larger m and probe the off-line
atoms' 3-adic reductions directly.

One orbit (D=425).  Bounded search.  Evidence, not proof.  RH stays [OUT].

### §6ap/§6aq — DIRECT p=3 floor via the fast minor-determinant formula (supersedes the C_j proxy)

§6ap first tried to close lemma (4) by adversarially MAXIMIZING max_j C_j.  RESULT (D=425, coord ascent):
max_j C_j = 7, 8, 7, 8, 9 for m = 4..8 -- larger than the <=4 seen for random configs, with a slow drift.
LESSON (self-correction): max_j C_j is the WRONG target.  The residual is v_3(q_min) = max_j (N_j - C_j), so
the floor only needs C small AT the argmax-N node (equivalently, it dies only if C_j >= N_j - O(1) for ALL j
at once, i.e. sum_j C_j ~ sum_j N_j ~ m^2/2).  A single large max_j C_j does NOT threaten the floor.  Also
recorded: the off-line atom x-proxy = 11/3 has v_3 = -1 vs EVERY rational node x_t (t=1,2,3,6,9) -- the
off-line orbit sits at 3-adic norm 3 (a pole), 3-adically SEPARATED from all node classes.

§6aq then made the DECISIVE, correctly-targeted test.  KEY IDENTITY (validated): since
    v_3(q_min) = v_3(det A) - min_j v_3(minor_j)                                    (§6am)
and v_3(det A), minor_j = det[A, col j -> d] are ALL integer determinants, v_3(q_min) is computable with
int_det ALONE -- NO slow SNF.  Cross-check (fast minor formula vs qmin_fast SNF), m=3..7: fast = SNF EXACTLY
(0,3,7,5,8 all match).  This retires the SNF cost bottleneck for the p=3 analysis and lets us adversarially
MINIMIZE v_3(q_min) directly (the true enemy of OP1: q_min -> 1) at larger m.

RESULT (D=425, adversarial coordinate descent = UPPER bound on the true adversarial min):
    m:                   4  5  6  7  8  9  10
    adv-min v_3(q_min):  2  2  4  5  5  7   6      (m/2:  2  2  3  3  4  4   5)
The m=4..8 values (2,2,4,5,5) reproduce §6al's independent SNF descent EXACTLY.  The adversarial minimum
GROWS MONOTONICALLY, tracking ~ m/2 - O(1): even the strongest node choice the descent found cannot drive
v_3(q_min) toward 0 -- it climbs with m.  (m=10 used an ultra-lean/weaker adversary, hence noisier; m>=11
COST-TRUNCATED -- int_det on 11x11 big-integer matrices x the descent budget exceeds the run ceiling.  NOT
silently dropped, per L5.)

SIGNIFICANCE.  This is a DIRECT empirical confirmation of the p=3 floor v_3(q_min) >= m/2 - O(1) that the
§6ao skeleton aims to prove -- and it does NOT rely on the still-open lemma (4) (C_j = O(1)); it measures
v_3(q_min) itself and shows the adversary cannot push it down.  So OP1's p=3 channel holds empirically for
D=425 up to m=10: log q_min >= (adv-min v_3) * log 3 grows linearly = omega(log m) => OP1 TRUE (evidence).
The §6ao decomposition remains the route to a PROOF (identity §6an + 2-classes-mod-3 pigeonhole + averaging,
closing on lemma (4)); §6aq is the direct-measurement corroboration and hands proofctl a fast, SNF-free
exact tool (v_3(q_min) = v_3(det A) - min_j v_3(minor_j)) for large-m replay.

One orbit (D=425).  Descent = UPPER bound on the adversarial min.  Evidence, not proof.  RH stays [OUT].

### §6ar — STEP (2) made RIGOROUS: v_3(det A) >= PIG(m) ~ m^2/4 (2-class-mod-3 pigeonhole)

The §6ao skeleton's step (2) is now an airtight pigeonhole bound.  Two facts, both verified EXACTLY (L9):
  (F1) den(x_t) = 4 t^2 + 1 is a 3-adic UNIT for every t != 0 (t != 0 mod 3: 4+1=5=2 mod 3; t=0 mod 3: 1),
       so x_t is a 3-adic integer with a well-defined class mod 3, and there are EXACTLY 2 classes:
       t != 0 mod 3 -> x = 0, t = 0 mod 3 -> x = 2.  (Checked t=1..60: class0=40, class2=20, other=0.)
  (F2) same mod-3 x-class => v_3(x_k - x_l) >= 1.  (Checked exhaustively over all same-class pairs t=1..60:
       True, no counterexample.)
Combined with the §6an identity v_3(det A) = sum_{k<l} v_3(x_k - x_l), this PROVES (modulo §6an):
    v_3(det A) = sum_{k<l} v_3(x_k - x_l) >= #{same-class pairs} >= min over 2-class splits = PIG(m),
    where PIG(m) := C(ceil(m/2),2) + C(floor(m/2),2) = m^2/4 - O(m).
The adversary minimizing v_3(det A) balances the 2 classes to minimize same-class pairs, so PIG(m) is the
floor.  DIRECT check (adversarial coordinate descent minimizing v_3(det A), one int_det per config):
    m:                 4  5  6  7   8   9
    adv-min v_3(detA): 3  5  9 14  19  25       (PIG:  2  4  6  9  12  16 ;  m^2/4:  4  6  9 12 16 20)
adv-min v_3(det A) >= PIG(m) in EVERY case (3>=2, 5>=4, 9>=6, 14>=9, 19>=12, 25>=16) and is QUADRATIC -- the
pigeonhole lower bound holds with room to spare (same-class pairs often contribute v_3 > 1).  (m>=10 int_det
cost-truncated on big-integer Bareiss -- reported, not silently dropped, per L5.  The bound itself is
analytic, not dependent on larger-m data.)  The split at the minimizer is class0-heavy, not perfectly
balanced, because class0 (t != 0 mod 3) supplies twice as many usable distinct nodes as class2.

PROOF STATUS after §6ar.  Of the four §6ao steps: (2) is now RIGOROUS (this section, given §6an), (3)
[averaging: sum_j N_j = 2 v_3(det A) => max_j N_j >= m/2 - O(1)] is rigorous, (1) [§6an identity] is
empirically exact (CORR=0) and is a classical graded-basis / confluent-Vandermonde determinant fact awaiting
a written proof, and (4) [C control at the argmax-N node] is the sole genuine open lemma.  §6aq's direct
measurement already confirms the CONCLUSION (v_3(q_min) ~ m/2) independently of (4).  The crisp remaining
targets, in order of tractability: prove the §6an identity (step 1), then close the C-control lemma (step 4).

One orbit (D=425).  Descent = UPPER bound on the adversarial min.  Evidence, not proof.  RH stays [OUT].

### §6as — STEP (1) PROVEN as an EXACT ALGEBRAIC IDENTITY (Vandermonde via graded basis)

Step (1) is no longer empirical.  The following exact closed form was verified EXACTLY (Fraction equality,
L9) over m=2..8 and a targeted case, ALL matches True:
    det[ 4(1 - T_j(x_k)) ]_{j,k=1..m}  =  4^m * (-1)^m * 2^{m(m-1)/2} * prod_k (x_k - 1) * prod_{k<l}(x_l - x_k).
PROOF.  T_j(1) = 1, so 1 - T_j(x) vanishes at x=1: 1 - T_j(x) = (x-1) q_j(x) with deg q_j = j-1 and
leadcoeff q_j = -2^{j-1}.  Row-factor 4 (=> 4^m) and column-... : det[1 - T_j(x_k)] = prod_k(x_k-1) *
det[q_j(x_k)]; {q_j}_{j=1..m} is a graded basis (degrees 0..m-1), so det[q_j(x_k)] = (prod_j -2^{j-1}) *
Vandermonde = (-1)^m 2^{m(m-1)/2} prod_{k<l}(x_l-x_k).  QED (confirmed by exact computation, not just p-adic).

CONSEQUENCE for p=3 (the floor prime): x_k - 1 = -2/(4 t_k^2 + 1), and 4 t^2 + 1 is NEVER divisible by 3
(t!=0 mod3 -> 5=2; t=0 mod3 -> 1), so v_3(x_k - 1) = 0 for all k.  Taking v_3 of the identity (4^m, 2^{...}
are 3-units):
        v_3(det A) = sum_k v_3(x_k - 1) + sum_{k<l} v_3(x_l - x_k) = 0 + sum_{k<l} v_3(x_l - x_k).
So step (1) at p=3 is a THEOREM: v_3(det A) = sum_{k<l} v_3(x_k - x_l).  (The cleared-columns integer det has
the same v_3 because clearing multiplies each column by a power of 4 t^2 + 1, a 3-adic unit.)

CORRECTION to §6an (L5, honest).  §6an reported "v_p(det A) = sum_{k<l} v_p(x_k - x_l), CORR = 0 for ALL odd
p".  That was the CLEARED INTEGER det.  For the RATIONAL matrix the true identity carries an EXTRA term
sum_k v_p(x_k - 1), which is NONZERO for p=5,17: e.g. ts=[1,4,6,9] gives 4t^2+1 = 5,65,145,325 (all divisible
by 5) and sum_k v_5(x_k - 1) = -5, yet the exact closed form STILL holds.  The extra term vanishes ONLY at
p=3 (and any p not dividing any 4 t^2 + 1); the cleared-columns normalization cancels it at every odd p, which
is why §6an's integer-det CORR was 0.  This does not affect the p=3 floor (the only prime the floor uses).

PROOF STATUS after §6as (p=3 floor v_3(q_min) >= m/2 - O(1)):
  (1) v_3(det A) = sum_{k<l} v_3(x_k - x_l)                     -- PROVEN (§6as exact identity).
  (2) v_3(det A) >= PIG(m) = m^2/4 - O(m)                       -- PROVEN (§6ar, F1+F2 pigeonhole given (1)).
  (3) max_j N_j >= 2 v_3(det A)/m >= m/2 - O(1)                 -- PROVEN (averaging, sum_j N_j = 2 v_3(det A)).
  (4) at j* = argmax_j N_j, C_{j*} = O(1)  (equiv. v_3(q_min) = max_j(N_j - C_j) >= m/2 - O(1))
                                                                -- SOLE OPEN LEMMA.
§6aq already confirms the CONCLUSION v_3(q_min) ~ m/2 directly (adversary cannot drive it to 0), independent
of (4).  [Step (4) reduction CORRECTED in §6at below -- the "4-atom Chebyshev" formula first sketched here was
based on a wrong basis assumption and is RETRACTED; see §6at for the verified correct reduction.]

One orbit (D=425).  Descent = UPPER bound on the adversarial min.  Evidence, not proof.  RH stays [OUT].

### §6at — CORRECTION + the CORRECT C_j reduction (interpolation-residual valuation)

HONEST RETRACTION (L5).  §6as/§6ao sketched C_j = v_3(sum_a w_a (xi_a - 1) prod_{k!=j}(xi_a - x_k)) by
treating the off-line vector d as a sum of CHEBYSHEV columns 4(1 - T_i(xi_a)).  That is WRONG.  The on-line
columns use C_i(t) = 4(1 - T_i(x)) (Chebyshev), but the OFF-LINE d uses a DIFFERENT family
phi_i(rho) = 1 - (1 - 1/rho)^i (the function _phi_re), summed over atoms {3/4 +- i tau, 1/4 +- i tau} with rho
and 1-rho.  Verified (§6at (iii)): no common x_rho gives phi_i(rho) = 4(1 - T_i(x_rho)) for all i -- e.g.
rho=3/4, x_rho = 1 - 1/(4 rho) matches i=1 (both 4/3) but NOT i=2 (phi_2 = 8/9 vs 40/9).  The "4-atom
Chebyshev" formula is therefore RETRACTED.

CORRECT reduction, verified EXACTLY (§6at (i)+(ii), all rows True, m=3..6).  Every on-line Chebyshev column
k has the common factor (x_k - 1), since 1 - T_i(x) = (x - 1) q_i(x) with q_i(x) := (1 - T_i(x))/(x - 1) a
GRADED basis (deg q_i = i - 1).  Hence for minor_j = det[A, col j -> d]:
    (i)  minor_j = [ prod_{k!=j} (x_k - 1) ] * det[ 4 q_i(x_k) (k!=j)  |  d_i ]_{i=1..m}.     [exact identity]
Since {q_i} is a graded basis, det[q-basis at X' | d] = (fixed 3-unit triangular transform) *
det[monomials at X'={x_k}_{k!=j} | d], and det[monomials at (m-1 nodes) | column d] = Vandermonde(X') *
L_{X'}(d) for a divided-difference / interpolation-residual functional L_{X'}.  Therefore, for p=3 (where
v_3(x_k - 1) = 0):
    (ii) C_j = v_3(minor_j) - VD_j = v_3( det[4 q_i(x_k)(k!=j) | d] ) - v_3( Vandermonde(X') ) = v_3( L_{X'}(d) ).
So C_j is the 3-ADIC VALUATION of an interpolation-residual functional of the off-line data d against the
m-1 on-line nodes X'.  Concretely L_{X'}(d) = sum_i (+-) d_i * s_i(X') where the s_i are (signed) elementary
symmetric functions of the m-1 nodes (the cofactors of the augmented graded-Vandermonde) -- an explicit
bilinear pairing between the off-line data vector and the symmetric functions of the on-line nodes.

OPEN LEMMA (4), restated cleanly and correctly:  v_3( L_{X'}(d) ) = O(1) uniformly in m and in the on-line
node set X' (at least at j* = argmax_j N_j).  Empirically C_j in {0, 1} for the random configs tested here,
and <= 9 under §6ap adversarial pressure -- consistent with O(1), now as a statement about a divided-
difference valuation, NOT the retracted atom formula.  This bilinear-form / interpolation-residual statement
is the crisp, self-contained open lemma and the strong EXT/outsource candidate.

PROOF STATUS (p=3 floor) unchanged: steps (1) [§6as], (2) [§6ar], (3) [averaging] PROVEN; step (4) = the
above residual-valuation lemma is the SOLE open piece; §6aq confirms the conclusion independently.

One arbitrary interior j.  One orbit (D=425).  Descent = UPPER bound on the adversarial min.  Evidence, not
proof.  RH stays [OUT].

### §6au — C_j as an EXPLICIT BILINEAR FORM; lemma (4) empirically bounded to m=21

The §6at residual functional is now fully explicit.  Write 4 q_i(x) = sum_l B[i][l] x^l (B is m x m LOWER-
TRIANGULAR, diagonal 4*(-2^{i-1}), all 3-units, so v_3(det B)=0).  Then [node-cols | d] = B [monomials | w]
with w := B^{-1} d a FIXED vector (depends only on the off-line data and the basis, NOT on the nodes).  The
augmented-Vandermonde identity det[(x_k^l)_{l, k in X'} | w] = Vandermonde(X') * sum_i (-1)^{m-1-i}
e_{m-1-i}(X') w_i gives, for p=3:
    C_j = v_3( sum_{i=0}^{m-1} (-1)^{m-1-i} e_{m-1-i}(X') * w_i ),   w = B^{-1} d,     [VERIFIED EXACT, m=3..7]
i.e. C_j is the 3-adic valuation of a BILINEAR PAIRING <w, signed elementary symmetric functions of X'>.
Check (a): this equals the §6ao/§6at integer-det C_j EXACTLY for all j, m=3..7 (ALL MATCH True).

LEMMA (4) STRESS TEST (cheap: the bilinear form needs no determinants -- w once, e_l(X') by product, one dot
product -- so adversarial ascent reaches large m).  Adversarially MAXIMIZING max_j C_j over m=4..21:
    m:          4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21
    max_j C_j:  6 10  8 11  9  8 12 10  8  8 10 12  9  9 10  9 10 10
BOUNDED in [6, 12] with NO GROWTH across all 18 values of m.  This is exactly lemma (4): the pairing
valuation v_3(<w, e(X')>) = O(1) (empirically <= 12 for D=425), uniformly in m and in the adversarial node
set.  Since C_{j*} <= max_j C_j <= ~12 at the argmax-N node j*, this gives directly
    v_3(q_min) = max_j (N_j - C_j) >= N_{j*} - C_{j*} >= max_j N_j - 12 >= m/2 - O(1),
so the p=3 floor holds -- now confirmed to m=21 (vs m=10 in §6aq) via the exactly-verified bilinear form.
(m=22..24 ascent cost-truncated: O(m^2) symmetric functions x m j-values x ascent budget exceeds the run
ceiling -- reported, not silently dropped, L5.)  Ascent = LOWER bound on max_j C_j, so the true max could be
marginally higher, but 18 consecutive m with no upward trend is strong.

PROOF STATUS (p=3 floor v_3(q_min) >= m/2 - O(1)) after §6au:
  (1) v_3(det A) = sum_{k<l} v_3(x_k - x_l)                                 -- PROVEN (§6as).
  (2) v_3(det A) >= PIG(m) = m^2/4 - O(m)                                   -- PROVEN (§6ar).
  (3) max_j N_j >= 2 v_3(det A)/m >= m/2 - O(1)                             -- PROVEN (averaging).
  (4) max_j C_j = v_3(<w, e(X')>) = O(1) uniformly                          -- SOLE open lemma; empirically
      bounded (<= 12) to m=21 via the explicit, verified bilinear form.  This is the crisp, fully-explicit,
      self-contained EXT/outsource nugget: a FIXED rational vector w = B^{-1} d (from the off-line orbit) has
      bounded 3-adic pairing valuation against the elementary symmetric functions of ANY on-line node set.

One orbit (D=425).  Ascent = LOWER bound on max_j C_j.  Evidence, not proof.  RH stays [OUT].

### §6av — 3-adic profile of the fixed vector w: all w_i are 3-units (the MECHANISM behind lemma (4))

The bilinear form C_j = v_3( sum_i (-1)^{m-1-i} e_{m-1-i}(X') w_i ), w = B^{-1} d, isolates the entire
open content into the FIXED vector w.  Profiling w 3-adically (exact rationals, L9) for m = 4..22:

    v_3(w_i) = 0  for EVERY coordinate i and EVERY m = 4..22   (min = max = 0; v_3(w_{m-1}) = 0).

Every coordinate of w is a 3-adic UNIT.  The closed rationals expose why: for m=4,
w = [-304/425, -91184/180625, -25884464/76765625, -6963575344/32625390625], i.e. w_i = N_i / 425^{i+1}
with denominators exact powers of D = 425 = 5^2 * 17 (coprime to 3) and 3-coprime numerators
(304 = 16*19, etc.).  Since 3 does NOT divide the orbit discriminant D = 425, the off-line moments are
3-adic units -- this is precisely why p = 3 is a "good" prime for this orbit and the reason the floor was
built at p = 3.

MECHANISM for lemma (4).  Reindex l = m-1-i: the pairing is
    S = sum_{l=0}^{m-1} (-1)^l e_l(X') w_{m-1-l} = < w , coefficient vector of prod_{k!=j}(y - x_k) >
    = L(m_{X'}),  where m_{X'}(y) = prod_{k!=j}(y - x_k) is the MONIC node polynomial (deg m-1) and L is the
    FIXED linear functional with unit "moments" L(y^i) = w_i (all v_3 = 0).
Because the on-line nodes x_k = (4t^2-1)/(4t^2+1) lie in Z_3 (denominator 4t^2+1 is a 3-unit), every
e_l(X') is a 3-adic INTEGER, and the monic leading term contributes the fixed e_0 = 1 coefficient paired
with w_{m-1} (a 3-unit).  Hence:
  * every term (+-) w_i e_{m-1-i}(X') has v_3 >= 0  (unit x 3-integer), so C_j = v_3(S) >= 0 always;
  * the e_0 = 1 term equals +- w_{m-1}, a 3-unit with v_3 = 0, ANCHORING the sum's low end;
  * therefore C_j > 0 requires 3-adic cancellation of the anchored unit term against the others -- and
    C_j = c requires cancellation to depth 3^c.  The observed cap (max_j C_j <= 12, §6au) is exactly a
    bound on this cancellation depth.
So the O(1) bound is NOT a numerical coincidence: it is the statement that a fixed unit-moment functional
applied to the monic node polynomial cannot be 3-adically annihilated beyond a bounded depth by any choice
of on-line nodes.  The remaining open piece of lemma (4) is precisely to bound that cancellation depth
absolutely (the unit structure of w gives v_3(S) >= 0 and a guaranteed unit term for free; the cap on how
high the adversary can push v_3(S) is the crisp EXT/outsource nugget).

Honest (L5): v_3(w_i) = 0 verified only to m = 22 (one orbit).  A single w_i with v_3 != 0 at larger m
would refine, not overturn, the "unit-moment" framing (the pairing would still be a fixed-functional
valuation).  Ascent still = LOWER bound on max_j C_j; the anchor argument bounds v_3(S) from BELOW at 0,
not from above -- the upper cap remains the open lemma.  One orbit (D=425).  RH stays [OUT].

### §6aw — REFUTATION of lemma (4): C_j = v_3(S) is UNBOUNDED (single 3-adic node lift)

The upper cap (§6au's plateau max_j C_j <= 12) was tested adversarially with SMALL t (random ascent = a mere
LOWER bound on the true max).  A TARGETED 3-adic lift attack refutes it.  Split one free node: X' = {x_free}
U Y (|Y| = m-2), g(y) = prod_Y(y - x_k); then S = <w, coeffs prod_{X'}(y-x_k)> is AFFINE in x_free:
    S = a - x_free * b,   a = sum_j g_j w_{j+1} = L(y g),   b = sum_j g_j w_j = L(g)   [VERIFIED EXACT].
If b is a 3-unit the adversary wants x_free ≈ a/b =: alpha.  Since x_of(t) = alpha solves to
t^2 = (1+alpha)/(4(1-alpha)) =: R, whenever R is a 3-ADIC SQUARE (and alpha has reachable residue in {0,2}
mod 3) an EXACT t* in Z_3 gives x_of(t*) = alpha, so integer t ≡ t* mod 3^c force v_3(S) >= c.  Census: R is
a 3-adic square in 11%-54% of random Y-sets (m=4,5,6).  Hensel-lifting a sqrt t* to precision 3^c and taking
the integer t_free = t* mod 3^c:
    c:        3   6  10  15  20  30
    v_3(S):   m=4:  5   8  12  17  22  34      m=5:  3   6  10  15  20  30      m=6:  3   6  11  15  20  30
v_3(S) = C_j TRACKS c upward without bound in all three m.  Hence:
    LEMMA (4) AS STATED (uniform max_j C_j = O(1)) is REFUTED for D=425.  C_j is UNBOUNDED; §6au's <=12
    plateau was a shallow-random-search artifact (small-t ascent never reaches the deep 3-adic solutions).
CONSEQUENCE: the §6au/§6av proof ROUTE "v_3(q_min) >= max_j N_j - max_j C_j >= m/2 - O(1)" is DEAD --
subtracting an UNBOUNDED max_j C_j is vacuous.  (The §6av anchor still gives v_3(S) >= 0 and a free unit
term; it bounds C_j only from BELOW, never from above.)  Honest negative result (L5).  One orbit (D=425).

### §6ax — but the FLOOR SURVIVES: v_3(q_min) = max_j(N_j - C_j) is robust; the argmax just moves

The floor is the JOINT quantity v_3(q_min) = max_j (N_j - C_j) (§6ao, cross-checked EXACT vs the SNF-free
integer-det v3_qmin_fast here, ALL MATCH).  Inflating ONE column's C_j only removes THAT column from the
argmax; the max over the OTHER columns can still be >= m/2.  Tested directly:
  (Y) SINGLE-LIFT (drive C_{j0} -> huge via the §6aw lift, then read the full v_3(q_min)):
        m=4: C_{j0}=5,12,22,34  ->  v_3(q_min)=5,5,5,5 (argmax stays j=0)
        m=5: C_{j0}=4,11,21,31  ->  v_3(q_min)=3,3,3,3 (argmax stays j=0)
        m=6: C_{j0}=4,11,21,32  ->  v_3(q_min)=8,7,7,7 (argmax stays j=1)
      v_3(q_min) is CONSTANT as C_{j0} explodes -- the argmax simply moves to a non-exploded column, and the
      floor (>= m/2) holds throughout.  The C-explosion is invisible to the max.
  (Z) STRUCTURED-MIN (adversarially minimize v_3(q_min) WITH lifts -- stronger than §6aq random ascent):
        m:                 4  5  6  7
        min v_3(q_min):    2  2  4  5     (vs m/2 = 2, 2.5, 3, 3.5)   -> floor holds for all m.
      Even the sharpest per-column 3-adic lift cannot push v_3(q_min) below ~m/2 (matches §6aq's random-ascent
      minima 2,2,4,5,5,7,6 for m=4..10).

CORRECTED PROOF STATUS (p=3 floor v_3(q_min) >= m/2 - O(1)) after §6aw/§6ax:
  (1) v_3(det A) = sum_{k<l} v_3(x_k - x_l)                                 -- PROVEN (§6as).
  (2) v_3(det A) >= PIG(m) = m^2/4 - O(m)                                   -- PROVEN (§6ar).
  (3) max_j N_j >= 2 v_3(det A)/m >= m/2 - O(1)                             -- PROVEN (averaging).
  (4') max_j (N_j - C_j) >= m/2 - O(1)                                      -- CORRECTED sole open lemma.
       NOT "max_j C_j = O(1)" (that is FALSE, §6aw).  The correct statement is JOINT: at the column that
       attains the floor, C_j is controlled RELATIVE to N_j.  Mechanism to prove: a 3-adic lift that inflates
       one column's C_j either co-inflates that column's N_j (the aligned node 3-adically clusters, raising
       the Vandermonde valuation) OR leaves another column with N_{j'} - C_{j'} >= m/2.  Empirically robust
       (§6ax(Y),(Z)) but UNPROVEN.  This joint-correlation lemma is the corrected EXT/outsource nugget --
       sharper and TRUE, unlike the refuted C_j = O(1) form.

The p=3 FLOOR itself is NOT refuted -- only the naive route.  Direct minimization (§6aq, §6ax(Z)) continues
to support v_3(q_min) >= m/2 - O(1).  One orbit (D=425).  Descent/ascent are one-sided.  RH stays [OUT].

### §6ay/§6az — the CORRECT provable form: a high-N, low-C column always EXISTS (lemma (4''))

Two candidate mechanisms for (4') were tested and BOTH killed (§6ay):
  (M1) co-inflation "C_{j0} large => v_3(det A) large": does NOT fire -- under the single-node lift v_3(det A)
       stays CONSTANT (7,13,21 for m=5,6,7) while C_{j0} explodes; and Sum_j C_j GROWS (not O(m)), so the
       averaging route (2 v_3(detA) - Sum C_j)/m is DEAD (a single exploded C_j is an outlier).
  (M2) "argmax-N column has bounded C": FALSE -- the adversary CAN explode C at the argmax-N column
       (N_{j*} - C_{j*} driven to -10..-14, max C_{j*} ~ 18); the floor then just MOVES to another column.
So the correct minimal form is an EXISTENCE statement, confirmed under the sharpest adversary (§6az):
    (4'')  EXISTS a column j with  N_j >= m/2 - O(1)  AND  C_j = O(1)  simultaneously.
At the adversarial MINIMUM of the floor v_3(q_min) = max_j(N_j - C_j), the FLOOR-CARRIER column j_f has:
    m:              4  5  6  7  8
    min floor:      2  2  4  5  5     (>= m/2 = 2, 2.5, 3, 3.5, 4  -- floor holds)
    carrier N_jf:   2  3  4  5  5     (>= m/2 - O(1))
    carrier C_jf:   0  1  0  0  0     (O(1), essentially 0-1 -- NOT exploded)
i.e. the floor is ALWAYS carried by a HIGH-N, LOW-C column.  The adversary can explode C at SOME columns
(§6aw) but CANNOT explode C at ALL high-N columns simultaneously -- exploding column j needs a specific 3-adic
alignment of the node set X' = {x_k}_{k!=j}, and these alignments COMPETE (aligning one column's X' de-aligns
others), so a high-N column with C = O(1) always survives.  Lemma (4'') => max_j(N_j - C_j) >= m/2 - O(1)
immediately.

CORRECTED PROOF STATUS (p=3 floor) after §6aw..§6az:
  (1) v_3(det A) = sum_{k<l} v_3(x_k - x_l)                                  -- PROVEN (§6as).
  (2) v_3(det A) >= PIG(m) = m^2/4 - O(m)                                    -- PROVEN (§6ar).
  (3) max_j N_j >= 2 v_3(det A)/m >= m/2 - O(1)                              -- PROVEN (averaging).
  (4'') EXISTS j: N_j >= m/2 - O(1) AND C_j = O(1)                           -- SOLE open lemma, corrected.
        NOT "max_j C_j = O(1)" (FALSE, §6aw) and NOT "argmax-N column has bounded C" (FALSE, §6ay-M2).  The
        TRUE, empirically-robust (§6az) statement is the EXISTENCE of a single high-N, O(1)-C column -- the
        floor-carrier -- protected by the competition among per-column 3-adic alignments.  This is the
        corrected EXT/outsource nugget: it is TRUE (unlike the refuted forms) and fully explicit.

### §6ba — pigeonhole route REFUTED; the floor is an IRREDUCIBLE joint bound (O(1) slack is essential)

The natural proof of (4'') -- "each specially-aligned node explodes O(1) columns, so a high-N column with
tiny C survives by pigeonhole" -- is FALSE:
  (A) K_expl(thr) = max #{j : C_j >= thr} achievable is NEARLY m, not O(1):
        m:              4  5  6  7  8
        K_expl(>=2):    4  3  4  6  5     (up to ALL / m-1 columns explodable at once)
        K_expl(>=5):    3  3  3  3  3
      A single lifted node feeds X' for many columns, and the adversary can align several at once -- most
      columns are simultaneously explodable.  "O(1) explodable columns" is refuted.
  (B) the strict survivor #{j : N_j >= m/2-2 AND C_j <= 1} can be DRIVEN TO 0 (m=4 and m=7): the adversary
      CAN push EVERY high-N column to C >= 2.  So "EXISTS a high-N column with C <= 1" (the clean (4'') form)
      is ALSO FALSE.
IMPORTANT (L5): survivor=0 does NOT collapse the floor.  The floor max_j(N_j - C_j) tolerates C = O(1): a
carrier with N_j = m/2, C_j = 2 still gives N_j - C_j = m/2 - 2 >= m/2 - O(1).  Direct floor minimization
(§6ax(Z), §6az) drove max_j(N_j - C_j) only down to 2,2,4,5,5 for m=4..8 -- all >= m/2 - O(1) -- so the floor
STANDS; it is just NOT reducible to a clean per-column existence with C <= 1.

FINAL CORRECTED STATUS of the sole open lemma (after §6au..§6ba):
  (4-floor)  max_j ( N_j - C_j ) >= m/2 - O(1),  uniformly in m and the adversarial node set.
  This is IRREDUCIBLE: it is NOT equivalent to any of
    - max_j C_j = O(1)                    (FALSE, §6aw: C_j unbounded),
    - Sum_j C_j = O(m) / averaging        (FALSE, §6ay: Sum_j C_j grows),
    - argmax-N column has bounded C       (FALSE, §6ay-M2),
    - EXISTS high-N column with C <= 1    (FALSE, §6ba-B: survivor -> 0).
  The O(1) additive slack is ESSENTIAL -- the floor-carrier trades N against a bounded C.  Empirically robust
  (min floor 2,2,4,5,5 for m=4..8 under the sharpest 3-adic adversary), but it resists every elementary
  decomposition tried.  This raw joint bound -- a competition between the pairwise-difference valuations
  (N_j) and the fixed-unit-moment pairing valuations (C_j) that no single-column attack can defeat -- is the
  precise, honest EXT/outsource nugget for the p=3 floor of OP1.  One orbit (D=425).  RH stays [OUT].

### §6bb — multi-orbit generality: the p=3 floor is ORBIT-DEPENDENT, gated by "w = B^{-1}d all 3-adic units"

  probe_qmin_multiorbit.py.  Every §6a* result used ONE orbit (sigma=3/4, tau=1, D=425).  The on-line matrix
  (Chebyshev nodes x_of(t)) is orbit-INDEPENDENT; the floor's orbit dependence is ENTIRELY through the
  off-line vector d = O_orbit_direct(sigma,tau) -> w = B^{-1}d -> C_j (N_j is orbit-free).  So per orbit the
  floor = adversarial-min over node sets of max_j(N_j - C_j).  Scanned a grid of orbits, min-floor via
  random-restart coordinate descent (UPPER bound on the true min), at p=3, m=4..7:

    orbit            | min v_3(w_i) | w all 3-units? | min-floor (m=4,5,6,7) | verdict vs m/2-2
    sigma=3/4,tau=1  |      0       |      YES        |     2, 2, 4, 5         | HOLDS  (D=425 baseline)
    sigma=3/4,tau=2  |      0       |      YES        |     2, 2, 4, 5         | HOLDS
    sigma=5/8,tau=1  |      0       |      YES        |     2, 2, 4, 5         | HOLDS  (2nd confirming orbit)
    sigma=7/8,tau=1  |      0       |      NO          |     0, 0, 0, 1         | FAILS
    sigma=4/5,tau=1  |      0       |      NO          |     0, 0, 0, 1         | FAILS
    sigma=2/3,tau=1  |      2       |      NO          |     0, 0, 2, 3         | MIXED (3|den)
    sigma=3/4,tau=3  |   -4..-7     |      NO          |     6, 7, 9,12         | LARGE (3|tau, w non-unit)

  READING (L5).  The p=3 floor v_3(q_min) >= m/2 - O(1) is NOT universal.  The sharp discriminator is
  "w = B^{-1}d is 3-adically UNIMODULAR (all coordinates units)":
    - w all units  => floor HOLDS (>= m/2 - 2): sigma=3/4 (both tau=1,2) AND sigma=5/8 -- a SECOND independent
      confirming orbit beyond D=425.  This is exactly the §6av mechanism (3 unramified in the orbit; the e_0
      anchor term = +-w_{m-1} is a unit, so C_j cannot be cheaply inflated on the carrier column).
    - some w_i NOT a unit (v_3(w_i) > 0)  => floor can COLLAPSE to ~0: sigma=7/8, sigma=4/5 give min-floor
      0,0,0,1.  When the anchor coordinate is 3-divisible the carrier protection is gone; a cheap collision
      exists for those orbits.
    - 3 | tau (w has 3 in DENOMINATORS, v_3(w_i) < 0)  => floor is LARGER still (C_j inherits negative
      valuation): sigma=3/4,tau=3 gives 6,7,9,12.  (Trivial inflation, not the same mechanism.)

  CONSEQUENCE for OP1.  The arithmetic barrier q_min -> infinity via the p=3 floor is a property of a
  CHARACTERIZABLE CLASS of orbits (w 3-adically unimodular), NOT of every orbit.  Since the construction is
  free to CHOOSE its orbit, picking a 3-unimodular orbit (D=425, or sigma=5/8) yields a valid witness with the
  floor intact -- the adversary faces a FIXED, favorably-chosen orbit.  So the barrier is REAL for the right
  orbit choice, and the correct lemma hypothesis is now identified precisely: the floor bound (4-floor) should
  be stated CONDITIONAL on "w = B^{-1}d is 3-adically unimodular", a checkable finite condition satisfied by
  >= 2 independent orbits.  This SHARPENS (does not weaken) the EXT nugget: it supplies the missing hypothesis
  under which the irreducible joint bound max_j(N_j - C_j) >= m/2 - O(1) is expected to be provable.
  Random-min = UPPER bound on min-floor (L5).  RH stays [OUT].

### §6bc — the ADJUGATE NO-CANCELLATION route is REFUTED as a reduction (5th failed simplification)

  probe_qmin_adjugate_floor.py.  A fresh attempt to make Step 4 tractable by opening the black box `minor_j`.
  Setup: floor = v(det A) − min_j v(minor_j), and expanding along the d-column,
  `minor_j = Σ_k d_k·T_{jk}` with `T_{jk} = (−1)^{k+j} M_{kj}` the cofactors (`M_{kj}` = (m−1)-minor of A).
  Define the NO-CANCELLATION prediction `pred_j = min_k[v(d_k)+v(T_{jk})]` (a min of explicit cofactor
  valuations); ultrametrically `v(minor_j) ≥ pred_j` always, so `no_canc_floor := v(det A) − min_j pred_j ≥
  floor` always.  HOPE: if floor = no_canc_floor, Step 4 reduces to a pure COFACTOR-VALUATION (Vandermonde/
  pigeonhole) bound `min_j pred_j ≤ v(det A) − m/2` — no bilinear cancellation, far more tractable.

  RESULT (L5).  The hope is FALSE.  floor == no_canc_floor for m = 4,5,6,7 (incl. the lift-adversary at those
  sizes) — but this is a SMALL-m coincidence.  At m = 8 the lift-adversary forces, at its floor-minimizing
  config, cancellation `gap* = v(minor_{j*}) − pred_{j*} = 17` at the pred-argmin column and `gap` over ALL
  pred-argmin columns `= 4`, giving `floor = 5 < no_canc_floor = 9`.  So `no_canc_floor` is a LOOSE upper
  bound with an UNBOUNDED gap; the cofactor-pigeonhole quantity `min_j pred_j` does NOT track the floor.
  Moreover the pred-argmin's term-min is NOT achieved by a unique cofactor term for m ≥ 5 (0/40 configs), so
  "gap = 0" is not provable via a unique dominating term — it is genuine non-cancellation of several terms,
  which the adversary defeats once m is large enough to give it cancellation room.

  WHAT SURVIVES.  The floor v(q_min) ITSELF still holds: at m = 8, floor = 5 ≥ m/2 = 4 (consistent with §6ax
  robustness and §6bb's unimodular-orbit regime).  Only the REDUCTION dies — the p=3 floor is NOT equivalent
  to, nor bounded below by, the adjugate no-cancellation cofactor bound.  This is the FIFTH refuted
  simplification of the joint bound (after max C=O(1), ΣC=O(m), argmax-N bounded C, ∃ high-N low-C column):
  the raw joint bound `max_j(N_j − C_j) ≥ m/2 − O(1)` remains irreducible.  Recorded on OB-42 as a known
  dead-end so a referee does not re-derive it.  One orbit (D=425); adversary = one-sided (L5).  RH stays [OUT].

### §6bd — CHANNEL SPLIT: log q_min is NOT exhausted by the p=3 floor; the dominant prime is p=2

  probe_qmin_channel_split.py.  OP1 holds iff inf_A log q_min = ω(log m).  The p=3 floor (OB-42) gives
  v_3(q_min) ≥ m/2 − O(1) ⇒ log q_min ≥ (m/2)·log 3 = Ω(m).  Question: under an adversary MINIMIZING the full
  integer q_min, is log q_min exhausted by the 3-adic part, or is there an independent second channel?
  Split: `log2 q_min = v_3(q_min)·log2(3) + log2(3-free residual)`.

  RESULT (L5).  The residual DOMINATES.  Under the (3-adic-tuned) adversary the 3-free part of q_min carries
  most of the magnitude, and its dominant prime is consistently **2**.  Direct measurement of v_2(q_min) vs
  v_3(q_min) over 80 random valid configs/m (D=425): min v_2 = 6,11,14,18,23 (m=4..8) — ALL ≥ m and ≈ 2×–3×
  the min v_3 = 2,2,4,5,5 (≈ m/2).  So the p=2 arithmetic channel is LARGER than the p=3 channel.  CAVEAT:
  this adversary minimizes the p=3 part, so the residual is UNATTACKED here — pursued in §6be.  RH [OUT].

### §6be — THE p=2 CHANNEL is orbit-robust and hypothesis-free — a strictly stronger target than p=3

  probe_qmin_channel_split.qmin_exact + inline (see session).  Three exact, unconditional structural facts at
  p = 2, then the survival test.

  (i) PER-PAIR FLOOR (PROVED, unconditional, orbit-free).  For all integer nodes t_j ≠ ±t_k,
        x(t)−1 = −2/(4t²+1)                    ⇒  v_2(x_k − 1) = 1  exactly, every node;
        x_j − x_k = 8(t_j²−t_k²)/((4t_j²+1)(4t_k²+1))  ⇒  v_2(x_j − x_k) = 3 + v_2(t_j²−t_k²) ≥ 3.
      Verified exact on 500 random pairs.  CONTRAST with p=3, where a pair contributes to N only when the two
      nodes 3-adically CLUSTER (pigeonhole, adversary-avoidable per pair); at p=2 EVERY pair contributes ≥ 3
      UNCONDITIONALLY.  This is the crux: the p=2 on-line valuation floor is adversary-proof.

  (ii) EXACT det-A FORMULA (PROVED, unconditional).  From C_j(t) = (x−1)·4q_j(x) and the graded basis,
        v_2(det A) = Σ_k v_2(x_k−1) + v_2(det B) + Σ_{k<l} v_2(x_k−x_l)
                   = m + m(m+3)/2 + Σ_{k<l} v_2(x_k−x_l)  ≥  m + m(m+3)/2 + 3·C(m,2) = 2m² + m.
      (v_2(det B) = Σ_{i=1}^m v_2(4·2^{i−1}) = Σ_{i=1}^m (i+1) = m(m+3)/2; e.g. m=6 → 27, matched exact.)
      NOTE: at p=2 the §6ao clean identity v(q_min)=max_j(N_j−C_j) does NOT transfer (there v(x−1)=0 and
      v(det B)=0 were used, both FALSE at p=2), so the p=2 floor is framed directly as v_2(det A) − v_2(gcd).

  (iii) THE FLOOR is LINEAR and the gcd absorbs the quadratic part.  q_min = det A / gcd(size-m minors of
      [A|d]); v_2(q_min) = v_2(det A) − v_2(gcd).  The numerator is quadratic (≥ 2m²+m) but the gcd of minors
      cancels the quadratic part, leaving v_2(q_min) LINEAR: min over 60 random cfgs = 6,11,14,18 (m=4..7),
      all ≥ m, slope ≈ 3.  The open core is thus min_j v_2(minor_j) ≤ v_2(det A) − c·m (equivalently: some
      d-replacement minor is not too 2-adically deep) — the p=2 analog of max_j(N_j−C_j), WITHOUT the
      unimodularity hypothesis.

  (iv) DECISIVE — ORBIT ROBUSTNESS.  Adversarial-min v_2(q_min) (coord-descent = one-sided UPPER bound) across
      orbits, m=4..7:
        σ=3/4 (unimod, p3 floor OK)  : 6, 11, 14, 18
        σ=7/8 (NON-unimod, p3 DIES)  : 4,  9, 12, 16
        σ=4/5 (NON-unimod, p3 DIES)  : 18,26, 28, 38
      On σ=7/8 and σ=4/5 the p=3 floor COLLAPSES to 0,0,0,1 (§6bb, non-unimodular ⇒ w not 3-adically unit),
      yet the p=2 floor stays LINEAR (≥ m) on all three.  So the p=2 channel needs NO orbit hypothesis — it is
      strictly stronger and cleaner than p=3, and its on-line side (i) is adversary-proof by construction.

  STATUS.  PROVED (exact, unconditional): (i) per-pair v_2 ≥ 3, v_2(x−1)=1; (ii) exact v_2(det A), quadratic
  lower bound.  EMPIRICAL (adversary = one-sided upper bound on inf): (iii) linear v_2(q_min) floor; (iv)
  orbit robustness.  Packaged as outsource OB-43 (the p=2 hypothesis-free floor), companion to OB-42 (p=3).
  RH stays [OUT].

### §6bf — EXACT p=2 floor IDENTITY + reduction to a single leave-one-out bilinear bound (CORE-2)

  probe_qmin_p2_floor_identity.py.  §6be framed the p=2 floor directly as v_2(det A) − v_2(gcd minors) and
  left Step 3 (linearity) "measured".  This upgrades it to a PROVED EXACT IDENTITY and reduces the whole open
  problem to ONE clean bilinear-valuation bound.

  IDENTITY (verified EXACT, 240 configs across orbits 3/4, 7/8, 4/5, m=3..7 — orbit-free, structural):
        v_2(q_min) = max_j ( 1 + N_j^(2) − C_j^(2) ),
        N_j^(2) = Σ_{k≠j} v_2(x_j − x_k)  ≥ 3(m−1)   [UNCONDITIONAL, every pair v_2 ≥ 3, §6be(i)],
        C_j^(2) = v_2(⟨w, ε(X'_j)⟩),  ε(X'_j)_i = (−1)^{m−1−i} e_{m−1−i}(others),  w = B^{−1}d.
  DERIVATION: A = B·V·diag(x_k−1) and d = B·w ⇒ v(det A)−v(minor_j) = v(x_j−1) + Σ_{k≠j}v(x_j−x_k) −
  v(⟨w,ε(X'_j)⟩) = 1 + N_j^(2) − C_j^(2); the "+1" is v_2(x_j−1)=1.  SAME bilinear C_j as p=3, but two
  corrections (the +1 and the UNIFORM base 3(m−1) of N) that make the p=2 case orbit-free.

  THE REDUCTION.  Because N_j^(2) ≥ 3(m−1) for EVERY column (not just on average — unconditional), taking the
  column of minimal C gives
        v_2(q_min)  ≥  1 + 3(m−1) − min_j C_j^(2).
  So the ENTIRE p=2 open core is a SINGLE statement about the off-line pairing:
        (CORE-2)  min_j C_j^(2)  ≤  (3 − c)·m + O(1)   for some absolute c > 0.
  Any such c gives a LINEAR floor v_2(q_min) ≥ c·m − O(1) and closes OP1's 2-adic channel — with NO
  unimodularity hypothesis (contrast p=3/OB-42).

  HONEST CALIBRATION (L5 — my initial "min_j C_j = O(1)" hope is REFUTED).  min_j C_j^(2) is NOT bounded: it
  GROWS.  But it grows with slope ≈ 1, far below N's slope 3.  TWO independent adversaries CONVERGE on the same
  sharp constant m+3:
    • maximize-min_j C_j (tries to inflate the pairing): reaches 7,8,9,10 (m=4..7) for 3/4; 9,10,11,12 for 7/8.
    • minimize-floor (the correct target, D=425): at its optimum ALL C_j are EQUAL (min=avg=max) = 7,8,9,10,11
      (m=4..8); floor = 6,11,14,18,21 (slope → 3); floor/m = 1.5,2.2,2.33,2.57,2.62.
  Both hitting min_j C_j ≈ m+3 is strong evidence the SHARP form is  min_j C_j^(2) ≤ m + O(1), giving
  v_2(q_min) ≥ 1 + 3(m−1) − (m+O(1)) = 2m − O(1).  (Adversaries are one-sided; this is calibration, not proof.)

  STATUS.  PROVED (exact): the identity v_2(q_min)=max_j(1+N_j−C_j); N_j ≥ 3(m−1); hence the reduction
  v_2(q_min) ≥ 1+3(m−1)−min_j C_j.  OPEN (CORE-2): min_j C_j^(2) ≤ (3−c)m+O(1) (sharp form ≤ m+O(1)).  This
  SHARPENS OB-43: Step 3 upgraded measured→proved identity; open core is now one self-contained leave-one-out
  bilinear bound, orbit-free.  RH stays [OUT].

### §6bg — CORE-2 proof attempt: the ultrametric sum-bound is PROVED but too weak (recorded dead route)

  probe_qmin_p2_floor_identity + inline.  Attempt to PROVE CORE-2 (min_j C_j ≤ (3−c)m).  Writing
  S_j = ⟨w, ε(X'_j)⟩ = L(P/(X−x_j)) for the fixed functional L(X^i)=w_i and P(X)=∏_k(X−x_k), and using
  Σ_j P/(X−x_j) = P'(X), one gets Σ_j S_j = L(P').  By the ultrametric (v_2(Σ) ≥ min),
        min_j C_j = min_j v_2(S_j)  ≤  v_2(Σ_j S_j)  =  v_2(L(P')),
        L(P') = Σ_{i=0}^{m−1} (i+1)·w_i·p_{i+1},   p = coeffs of P  (a SINGLE explicit bilinear form).
  This reduction is EXACT/PROVED (verified on 600 configs, m=4..8: min_j C_j ≤ v_2(L(P')) always).  HOPE: if
  v_2(L(P')) ≤ (3−c)m then CORE-2 closes with NO min-over-columns.

  RESULT (L5).  The hope is FALSE.  v_2(L(P')) is NOT ≤ (3−c)m: an adversary maximizing it reaches
  20,8,10,10,24 for m=4..8 — e.g. 20 ≫ 3(m−1)=9 at m=4, 24 > 21 at m=8.  Because Σ_j S_j collapses the m
  terms into one, the adversary can 2-adically ALIGN them so the SUM is far deeper than any single term while
  min_j C_j stays at m+3.  So the sum-bound, though valid, is too lossy to certify CORE-2.  Related weightings
  (Lagrange L(Q)=Σ_j [Q(x_j)/P'(x_j)]S_j, or Q=X^i with v_2(x_j)=0) all reintroduce the N_j=v_2(P'(x_j))
  denominator and collapse to the weak "∃ j: C_j ≤ N_j".  A proof of CORE-2 needs the genuine COUPLING of the
  m leave-one-out vectors ε(X'_j) (Newton's identities / a Newton-polygon bound on S = E·w, E the
  signed-elementary-symmetric matrix), not a single linear combination.

  WHAT SURVIVES.  CORE-2's sharp empirical form min_j C_j ≤ m+3 is UNSHAKEN (600 random configs + two
  adversaries all cap at m+3), and the reduction v_2(q_min) ≥ 1+3(m−1)−min_j C_j is proved.  Only this
  particular proof route dies.  Recorded on OB-43 as a known dead-end (its 1st, analogous to OB-42's adjugate
  dead-end).  σ=3/4; adversary one-sided (L5).  RH stays [OUT].

### §6bh — Lagrange-weight factorization: v_2(q_min) = 1 − min_l v_2(L(ℓ_l)), a single-vector CORE-2

  probe_qmin_p2_floor_identity + inline (VERIFIED 200/200, m=3..7, σ=3/4; the Σu=w_0 relation 150/150).
  A PROVED exact repackaging of the §6bf identity into one clean analytic object.  The coefficient matrix
  E (rows = ε(X'_j), the coeffs of p_j(X)=∏_{k≠j}(X−x_k)) satisfies E·V^T = diag(P'(x_j)) because
  p_j(x_l)=δ_{jl}P'(x_j) (V the Vandermonde in the x_l).  Hence the pairing vector S = E·w factors as
        S = diag(P') · (V^T)^{−1} w,    so   C_j = v_2(S_j) = N_j + v_2(u_j),   u := (V^T)^{−1} w,
  and the §6bf floor identity becomes
        v_2(q_min) = max_j(1 + N_j − C_j) = 1 − min_j v_2(u_j).                    (★★)
  Meaning of u: solving V^T u = w (Σ_l x_l^i u_l = w_i, i=0..m−1) says u_l are the QUADRATURE WEIGHTS
  representing the fixed orbit functional L (L(X^i)=w_i) as L(Q)=Σ_l u_l Q(x_l) for deg Q ≤ m−1.  So
        u_l = L(ℓ_l),   ℓ_l = Lagrange basis poly = p_l/P'(x_l)  ⇒  u_l = S_l/P'(x_l)  (consistent w/ C_l=N_l+v_2(u_l)).
  Because Σ_l ℓ_l = 1, this gives a FIXED, orbit-only constraint on the whole weight vector:
        Σ_l u_l = L(1) = w_0.       [VERIFIED: v_2(w_0)=4 constant across m=3..7 for σ=3/4.]

  RESTATED CORE-2 (equivalent, single-vector form).  A linear floor v_2(q_min) ≥ c·m ⟺ min_l v_2(u_l) ≤ 1−c·m,
  i.e. SOME Lagrange/quadrature weight u_l has a deep 2-adic DENOMINATOR (v_2 ≤ −(c m−1)).  Empirically the
  min-C column has C_l ≈ m+3 and N_l ≈ 3(m−1), so v_2(u_l) ≈ (m+3)−3(m−1) = −2m+6 and floor ≈ 2m−5 — matching
  the observed 2m−O(1) floor.  This is ALGEBRAICALLY the same identity (§6bf), but recentered on the fixed
  vector u = (V^T)^{−1}w instead of m separate bilinear forms: CORE-2 is now "the inverse-Vandermonde-dual of
  the fixed w has a coordinate of valuation ≤ −(3−c)m", a cleaner target for divided-difference / Newton-polygon
  2-adic analysis.

  WHY IT ISN'T YET A PROOF (L5).  The ultrametric on Σ_l u_l = w_0 gives min_l v_2(u_l) ≤ v_2(w_0)=4, hence only
  floor ≥ 1−4 = −3 (trivial) — the SAME lossy direction as §6bg: the deeply-negative weights must CANCEL to the
  shallow sum w_0, and that cancellation is the crux.  What (★★) adds is a sharper handle for OB-43 Step 4:
  bound the deepest 2-adic denominator of u = (V^T)^{−1}w directly (explicit inverse-Vandermonde entries, or
  Newton-form divided differences of the fixed w), rather than a min over m bilinear pairings.  σ=3/4; RH [OUT].

### §6bi — BREAKTHROUGH: C_j ≡ m+3 (node-independent) ⇒ CORE-2 collapses to a node-free 2-adic recursion

  probe_qmin_p2_Cj_identity (EXHAUSTIVE + m≤8).  CORE-2 asked only for min_j C_j ≤ (3−c)m.  In fact something
  FAR stronger is true for the D=425 orbit (σ=3/4):
        C_j = m+3   for EVERY column j AND EVERY node set.                       [IDENTITY, not inequality]
  Exhaustively verified: ALL 1365 sets at m=4 (t∈1..15), all 792 at m=5 (t<13), + consecutive blocks,
  arithmetic progressions, powers-of-two, random to m=7 — ZERO deviations, while N_j ranges 9..22.  Since the
  min column also has C=m+3, the §6bf reduction gives an UNCONDITIONAL LINEAR floor:
        v_2(q_min) ≥ 1 + 3(m−1) − (m+3) = 2m − 5    (σ=3/4, every representative, every node set).

  PROOF CHAIN (rigorous modulo ONE node-free lemma).  Shift Z=X−1 (every node: v_2(x_k−1)=1, PROVED §6be).
  With w'_i := L((X−1)^i) and p_j = ∏_{k≠j}(Z−y_k), y_k=x_k−1 (so the Z^{m−1−r} coeff is (−1)^r e_r(y_{≠j}),
  v_2(e_r) ≥ r):
        L(p_j) = Σ_{r=0}^{m−1} (−1)^r w'_{m−1−r} e_r(y_{≠j}),   v_2(term_r) = v_2(w'_{m−1−r}) + v_2(e_r).
  LEMMA (node-free):  v_2(w'_i) = 4 + 3i   (verified to m=8).  Given it, v_2(term_r) ≥ [4+3(m−1−r)]+r =
  4+3(m−1)−2r, STRICTLY decreasing in r, so the UNIQUE minimum is r=m−1:  term_{m−1} = w'_0·∏_{k≠j} y_k has
  v_2 = 4 + (m−1) = m+3 EXACTLY (product of m−1 valuation-1 factors — no cancellation), while every r<m−1 term
  is ≥ m+5.  Ultrametric with a unique minimum ⇒ v_2(L(p_j)) = m+3.  QED (modulo the lemma).  [Term-margin
  asserts passed on 6000 configs; C_j==m+3 all cols 400/400 at m=4..7; v_2(q_min) ≥ 2m−5 400/400.]

  THE LEMMA IS A FINITE, EXPLICIT, NODE-FREE COMPUTATION.  Since T_j(1)=1, 4q_j(x) = −4(T_j(x)−1)/(x−1), so in
  Z=X−1:  4q_j = Σ_i G[j][i] Z^i with  G[j][i] = −4·T_j^{(i+1)}(1)/(i+1)!  and  T_j^{(k)}(1) =
  ∏_{l=0}^{k−1}(j²−l²)/(2k−1)!!.  Because d = Bw ⇒ L(4q_j) = d_j, this is a LOWER-TRIANGULAR system
        d_j = Σ_{i=0}^{j−1} G[j][i] w'_i,   diagonal G[j][j−1] = −2^{j+1}  (v_2 = j+1),
  VERIFIED to reconstruct d_j exactly (m≤8).  Solving recursively determines w'_i from the node-free target d.
  So the lemma v_2(w'_i)=4+3i is a pure 2-adic statement about the Chebyshev-derivative coeffs G and the
  orbit target d — NO node quantifier.  Base: w'_0 = d_1/(−4), v_2 = v_2(d_1)−2 = 6−2 = 4 ✓.  Recursion:
  w'_{j−1} = (d_j − Σ_{i<j−1} G[j][i]w'_i)/(−2^{j+1}); need v_2(numerator) = 4j+2.

  ORBIT DEPENDENCE (L5).  The profile generalizes to v_2(w'_i) = OFF + S·i; when S>1 the SAME unique-minimum
  argument gives C_j = OFF + (m−1).  Measured: σ=3/4 → (OFF,S)=(4,3) ⇒ C_j=m+3; σ=7/8 → (6,5) ⇒ C_j=m+5
  (both node-independent, both linear floors).  σ with S≤1 (e.g. 5/6: slope 1) or non-linear profile (4/5, 2/3:
  irregular, even negative C_j — an even LARGER floor) need separate treatment, but σ=3/4 (OP1's D=425 target)
  is the clean case.  HONEST: the node-free lemma v_2(w'_i)=4+3i is VERIFIED (exhaustive + m≤8) but not yet
  PROVEN from the closed forms of G and d; that single 2-adic bookkeeping step is all that remains to close
  OP1's 2-adic channel with an unconditional linear floor.  RH stays [OUT].

### §6bj — the target lemma v_2(d_j)=6+2v_2(j) is a Lifting-the-Exponent statement on 13+16i (N=425)

  probe_qmin_p2_dj_lte (EXACT to j=24).  §6bi's node-free lemma v_2(w'_i)=4+3i is fed by the triangular
  recursion d_j = Σ_i G[j][i] w'_i; its base input is the 2-adic profile of the orbit target d_j.  Traced to
  a CLOSED FORM + a standard number-theoretic tool.  For σ=3/4, τ=1 the orbit is ρ ∈ {3/4±i, 1/4±i}, and
        1 − 1/ρ = (13+16i)/25  (ρ=3/4+i)   and   (13+16i)/17  (ρ=1/4+i),
  with the Gaussian integer α = 13+16i,  N(α) = 13²+16² = 425 = 25·17 = D,  α−ᾱ = 32i = 2⁵i.  The target is
  (VERIFIED exact, j≤24):
        d_j = 4·[ (1 − Re[(α/25)^j]) + (1 − Re[(α/17)^j]) ] = 4·[ (25^j−Re[α^j])/25^j + (17^j−Re[α^j])/17^j ].
  Since 25,17 odd and Re[α^j] is ODD (v_2=0 always), v_2(d_j) = 2 + v_2( (25^j−Re) + (17^j−Re) ).  Verified
  sub-valuations (each a p=2 LTE identity):
        v_2(25^j − Re[α^j]) = 2 + v_2(j),   v_2(17^j − Re[α^j]) = 2 + v_2(j)
            [base 2 = v_2(25−13)+v_2(25+13)−1 = 2+1−1; the Gaussian corrections C(j,2k)13^{…}16^{2k}(−1)^k
             carry v_2 ≥ 7, deeper];
        SUM has v_2 = 4 + 2v_2(j)  — a FURTHER cancellation DOUBLING the valuation, sourced by the conjugate
             relation (α/25)(ᾱ/17) = N(α)/425 = 1.
  Hence v_2(d_j) = 2 + (4+2v_2(j)) = 6 + 2v_2(j).  (Companion: v_2(Im[α^j]) = 4 + v_2(j), textbook LTE:
  v_2(α^j−ᾱ^j) = v_2(α−ᾱ)+v_2(j) = 5+v_2(j), /2i ⇒ 4+v_2(j).)

  ⚠ SUPERSEDED BY §6bk.  The L2 line below ("cancellation of the two lowest terms … lift the numerator to
  4j+2") is WRONG: the recursion numerator's two lowest terms d_j and G[j][0]w'_0 do share v_2=6+2v_2(j), but
  the numerator's TRUE valuation is 4j+2 — a DEEP multi-term telescoping, not a two-term lift (verified: j=8
  term-valuations 12,12,14,19,20,27,29,34 all conspire to 34).  §6bk replaces the whole L2/L3 route with a
  direct rank-2 closed form that proves the lemma in two lines with no LTE and no recursion.  The LTE facts of
  §6bj (v_2(d_j)=6+2v_2(j)) remain TRUE but are no longer on the critical path.

  (superseded) PROOF ARCHITECTURE:
    L1 (identity)      C_j = m+3  ⟸  v_2(w'_i)=4+3i     [PROVED: Z=X−1 shift + ultrametric unique-min, §6bi]
    L2 (lemma→recursion) v_2(w'_i)=4+3i  ⟸  triangular recursion … [OVER-COMPLICATED, see §6bk]
    L3 (d_j→LTE)         v_2(d_j)=6+2v_2(j)  ⟸  LTE on α=13+16i + conjugate-relation sum-doubling [§6bj]
  RH stays [OUT].

### §6bk — the node-free lemma is PROVED: w'_i is a rank-2 Lucas sequence (β=8·(−19+8i)/425), σ=3/4

  probe_qmin_p2_rank2_closed_form (EXACT).  The last mile of §6bi/§6bj closes ELEMENTARILY, and the §6bj
  LTE/recursion detour is retired from the critical path.  Two facts, both verified exactly:

  (A) w'_i is m-INDEPENDENT — a single stable infinite sequence (identical for m=4,6,…,14).  It has an
      ORDER-2 rational recurrence w'_i = A·w'_{i−1} + B·w'_{i−2}, A=−304/425 (v_2=4), B=−64/425 (v_2=6),
      equivalently the CLOSED FORM
            w'_i = β^{i+1} + β̄^{i+1} = (8^{i+1}/425^{i+1})·2·Re(γ^{i+1}),
            β = −8(19−8i)/425 = 8γ/425,   γ = −19+8i   (Gaussian integer, N(γ)=425=D).
      DERIVED (not fitted): the functional L (L(4q_j)=d_j, w'_i=L((X−1)^i)) is EXACTLY the two-point
      evaluation L(f)=β·f̃(β)+β̄·f̃(β̄), f̃(Z)=f(1+Z).  Reason: the four orbit exponentials pair by the
      RECIPROCAL relation (α/25)(ᾱ/17)=N(α)/425=1, so z=α/25, 1/z=ᾱ/17 form ONE Chebyshev pair
      ξ=(z+1/z)/2, giving T_j(ξ)+T_j(ξ̄)=Re(α/25)^j+Re(α/17)^j and hence d_j = β·4q_j(1+β)+β̄·4q_j(1+β̄)
      (VERIFIED all j≤16).  Since {4q_j}_{j=1..m} is a triangular basis of deg≤m−1 polys, L is fixed by
      d_1..d_m, so the two-point functional IS L; holding for every m ⇒ closed form for all i.

  (B) THE VALUATION (elementary, NO LTE).  425 is odd; γ=−19+8i ≡ 1 (mod 2) in Z[i] (Re odd, Im even), so
      γ^{i+1} ≡ 1 ⇒ Re(γ^{i+1}) is ODD ⇒ v_2(2·Re)=1.  Therefore
            v_2(w'_i) = v_2(8^{i+1}) + v_2(2·Re(γ^{i+1})) − v_2(425^{i+1}) = 3(i+1) + 1 − 0 = 4 + 3i.   ∎
      (Alternatively, a two-line induction on the order-2 recurrence: v_2(A·w'_{i−1})=5+3i ≠
      v_2(B·w'_{i−2})=4+3i, so ultrametric gives min=4+3i with no cancellation.)

  NET: the node-free lemma v_2(w'_i)=4+3i is now PROVED (rank-2 closed form + "odd real part"), hence
  C_j=m+3 (§6bi) and the UNCONDITIONAL LINEAR floor v_2(q_min) ≥ 2m−5 for OP1's σ=3/4 (D=425) barrier —
  no node quantifier, no L-value, no analytic rank, no RH input.  HONEST (L5): fully rigorous modulo the
  [VERIFIED-exact] closed form, whose derivation (two-point functional via reciprocal pairing + triangular
  basis uniqueness) is spelled out above and checked to j≤16 / i≤13.  σ=3/4 is the clean rank-2 case; other
  σ give β with a different v_2 (profile OFF+S·i) and need the same per-orbit treatment.  RH stays [OUT].

### §6bl — THE ORBIT TRICHOTOMY: rank-2 is UNIVERSAL; the σ=3/4 proof generalizes to the v_2(β)≥2 family

  probe_qmin_p2_orbit_trichotomy (EXACT).  The §6bk structure is not special to σ=3/4; it is one leaf of a
  clean structural law scanned over off-line orbits (σ,τ).  Three facts, all verified exactly:

  (U) UNIVERSAL RANK 2.  For EVERY orbit, w'_i = L((X−1)^i) satisfies an order-2 rational recurrence
      w'_i = A·w'_{i−1} + B·w'_{i−2}, equivalently w'_i = β^{i+1}+β̄^{i+1} with β,β̄ the roots of r²−Ar−B
      (β = the shifted Chebyshev point of the reciprocal-paired orbit exponentials, §6bk).  Confirmed via
      Hankel rank = 2 for all orbits tested (σ = 3/4, 7/8, 5/8, 5/4, 5/6, 9/10, 4/5, 2/3).

  (S) THE 2-ADIC SLOPE S := v_2(β) = v_2(B)/2 governs the profile and the floor — a TRICHOTOMY:
        • S ≥ 2  (σ=3/4→k=3; σ=7/8,5/8→k=5; σ=5/4→k=3):  β = 2^k·γ/N with N odd and γ a Gaussian integer
          of ODD REAL / EVEN IMAG part (γ ≡ 1 mod 2 in Z[i]).  Then w'_i = 2^{k(i+1)}·2Re(γ^{i+1})/N^{i+1}
          with Re(γ^{i+1}) ODD, so v_2(w'_i) = k(i+1)+1 (LINEAR, slope k≥2); the §6bi unique-minimum
          expansion gives C_j = m+k for every column/node set, hence the UNCONDITIONAL LINEAR FLOOR
                v_2(q_min) ≥ 1 + 3(m−1) − (m+k) = 2m − 2 − k.
          The closed form (cf=True) and odd-real-part (odd=True) are VERIFIED for every S≥2 orbit; σ=3/4
          (k=3, floor 2m−5) is PROVED in §6bk and the whole S≥2 family shares the IDENTICAL two-line proof.
        • S = 1  (σ=5/6, 9/10):  BORDERLINE.  γ still has odd real part but slope k=1, so the unique-minimum
          collapses (multiple lowest terms), min_j C_j grows at slope ≈3, and the p=2 bound 1+3(m−1)−min_j C_j
          is VACUOUS.  Measured v_2(q_min) is SMALL (σ=9/10: 1,2,4 at m=4,5,6) — p=2 does NOT carry the barrier.
        • S < 1  (σ=4/5, 2/3: v_2(B)=−3, S=−3/2):  β has 2 in the DENOMINATOR (γ here has Re-odd/IM-ODD, a
          DIFFERENT structure); v_2(w'_i) goes negative and non-linear, so C_j<0 and the floor is LARGE
          (measured v_2(q_min)=22,30,36) — p=2 closes these easily but by a mechanism NOT proved here.

  (M) HONEST scope (L5) — the single-prime p=2 floor is NOT orbit-robust.  No fixed prime is uniformly linear
      across all orbits; the S=1 orbits defeat p=2.  BUT the TOTAL barrier is orbit-robust in the tested range:
      worst-case (min over node subsets of {1..13}) log_2(q_min) grows LINEARLY for every orbit (σ=3/4:
      36,49,66; σ=5/6: 42,57,74; σ=9/10: 55,70,91 at m=4,5,6), the barrier MIGRATING to larger primes when
      p=2 is weak.  So OP1 plausibly closes for all orbits as a MULTI-PRIME phenomenon; the clean single-prime
      PROVABLE nugget is exactly the S≥2 (v_2(β)≥2) family via p=2.  This narrows OB-43's "orbit-robust"
      Theorem, which overclaimed a single-prime uniform floor over ALL orbits.  RH stays [OUT].

### §6bm — CLOSED FORM β = 1/(2ρ(ρ−1)) upgrades the S≥2 family floor to a PROVED THEOREM (denominator-indexed)

  probe_qmin_p2_beta_closed_form (EXACT).  §6bl verified γ's parity for 4 orbits; §6bm eliminates that last
  empirical step by giving β an elementary closed form in the off-line point ρ = σ+iτ, so the family floor
  becomes a theorem parameterized by ρ's denominator.

  (A) CLOSED FORM.  β = ξ−1, ξ = (w+1/w)/2, w = 1−1/ρ, so β = (w−1)²/(2w) = 1/(2ρ(ρ−1)).  Writing
      ρ = (p+qi)/n in lowest terms and clearing:  β = n²/(2M),  M = Re(M)+Im(M)i,
              Re(M) = p²−q²−np,   Im(M) = q(2p−n).
      Hence the profile slope has the CLOSED FORM  S = v₂(β) = 2·v₂(n) − 1 − v₂(N(M))/2,  N(M)=Re(M)²+Im(M)².
      VERIFIED S(formula)==S(recurrence) for all 13 orbits tested (incl. S=1, S=−3/2, τ=1/2), and the
      closed-form β matches the recurrence-extracted β (up to conjugate root) in every case.

  (B) THE FAMILY THEOREM (elementary; no node quantifier, no L-value, no RH).  Suppose 4 ∣ n and p,q have
      OPPOSITE parity (⟺ N(M) odd).  Then:
      (P1) n even ⟹ Im(M)=q(2p−n) EVEN; opposite parity ⟹ Re(M) ≡ p−q ≡ 1 (mod 2) ODD.  So γ := conj(M)
           (times its odd rational content) has Re odd / Im even, i.e. γ ≡ 1 (mod 2·Z[i]).
      (P2) S = 2·v₂(n) − 1 ≥ 3 (as v₂(n) ≥ 2), and β = 2^S·γ/N with N = N(M) odd.
      (P3) γ ≡ 1 mod 2·Z[i] is closed under multiplication ⟹ Re(γ^{i+1}) ODD ⟹ v₂(2Re(γ^{i+1}))=1, so
           w'_i = β^{i+1}+β̄^{i+1} = 2^{S(i+1)}·2Re(γ^{i+1})/N^{i+1} ⟹ v₂(w'_i) = S(i+1)+1.
      (P4) §6bi unique-minimum: v₂(term_r) ≥ (S+1)+S(m−1)−(S−1)r STRICTLY DECREASING (S>1), unique min at
           r=m−1 (product w'_0·∏y_k, no cancellation) = m+S ⟹ C_j = m+S for EVERY node set ⟹ the
           UNCONDITIONAL LINEAR FLOOR  v₂(q_min) ≥ 1+3(m−1)−(m+S) = 2m − 2 − S.
      σ=3/4 (n=4, S=3, 2m−5) is one member; every 4∣n opposite-parity orbit is proved identically.  VERIFIED
      floor 2m−2−S vs measured v₂(q_min) for all 9 such orbits (σ=3/4,7/8,5/8,5/4,9/8,1/4,3/8,11/12, τ=1/2).

  (C) THE S=1 BOUNDARY EXPLAINED.  When n ≡ 2 (mod 4) with N(M) odd (σ=5/6, 9/10), S=2v₂(n)−1=1, so the
      §6bi coefficient −(S−1)=0: all m terms tie in valuation, the unique-minimum COLLAPSES, C_j is NOT
      pinned (cancellation), and the floor is vacuous — §6bl's borderline class, now rigorously accounted for.
      NET: the p=2 floor is a THEOREM exactly on the 4∣n opposite-parity family (S≥3), by an elementary
      2-adic/Gaussian-integer argument; the S=1 boundary and the S<1 (n odd, both-odd γ) regime are outside
      it.  Full orbit-robustness of OP1 remains a multi-prime phenomenon (§6bl(M)).  RH stays [OUT].

### §6bn — MULTI-PRIME COMPLEMENTARITY: the {p=2, p=3} coverage map (attacks the §6bl(M) orbit-robustness gap)

  probe_qmin_multiprime_complementarity (EXACT q_min, adversarial per-prime descent = one-sided UPPER bound
  on the true adv-min).  §6bm PROVED p=2 only for 4∣n opposite-parity orbits; OP1 orbit-robustness needs
  EVERY off-line orbit (every putative RH violator; the adversary picks ρ, we do not) to have a linear floor
  at SOME prime.  Scanning orbits across all n mod 4 classes and adversarially MINIMIZING v_p(q_min) for
  p ∈ {2,3,5}, m=4..7 (the OP1 danger direction — drive the collision cheap):

    orbit    n%4  S(p2)  p=2 adv-min        p=3 adv-min      p=5
    3/4  n=4  0    3     [6,11,14,18] LIN   [2,2,4,5] LIN     [0,1,2,3]
    5/8  n=8  0    5     [4,9,12,16]  LIN   [2,2,4,5] LIN     [0,0,0,0]
    5/6  n=6  2    1     [0,3,3,3]    flat  [0,0,2,3] weak    [0,0,0,0]
    9/10 n=10 2    1     [0,0,1,1]    flat  [2,2,4,5] LIN     [0,0,0,0]
    3/10 n=10 2    1     [0,3,3,3]    flat  [2,2,4,5] LIN     [0,0,0,0]
    2/3  n=3  odd -3/2   [18,26,29,38] LIN  [0,0,2,3] weak    [0,0,0,0]
    4/5  n=5  odd -3/2   [18,26,28,38] LIN  [0,0,0,1] weak    [0,0,0,0]

  THE UNIFIED COMPLEMENTARITY LAW (empirical, L5).  The two smallest primes give two LARGELY-INDEPENDENT
  linear floors whose failure sets are governed by n's own factorization:
    * p=2 floor is LINEAR unless v_2(n)=1 (i.e. 2‖n, n≡2 mod 4): n≡0 mod 4 → S≥3 (PROVED §6bm); n odd → S<0,
      β has 2 in the denominator, floor LARGE (18,26,29,38 — slope ~7, the strongest of all).  Only 2‖n gives
      S=1 (vacuous).  [So the §6bm "4∣n" family plus the n-odd regime already cover 3/4 of residues mod 4.]
    * p=3 floor is LINEAR unless 3∣n: the ON-LINE N_j side is orbit-free and, when w=B^{-1}d is 3-adically
      unimodular (§6bb, ⟺ 3∤ the orbit denominator), C_j=O(1) gives the IDENTICAL floor [2,2,4,5] for EVERY
      such orbit (3/4, 5/8, 9/10, 3/10 all coincide) — a genuinely n-mod-4-INDEPENDENT second barrier that
      covers the n≡2 mod 4 orbits where p=2 dies.  It degrades to [0,0,2,3] exactly when 3∣n (5/6, 2/3).
  CONSEQUENCE (coverage): {p=2, p=3} already carry a linear floor for EVERY orbit EXCEPT the class
  "v_2(n)=1 AND 3∣n" (⟺ 6∣n, 4∤n; smallest σ=5/6, n=6), where BOTH small primes are killed by n=2·3.  There
  the barrier must migrate to a RAMIFIED prime | N(M) (for σ=5/6, N(M)=2257=37·61, not in {2,3,5} — which is
  exactly why p=5 is 0 there) — pursued in §6bo.  So the §6bl(M) "multi-prime phenomenon" is now a PRECISE,
  finite coverage map, not a vague hope: three prime-families (2, 3, ramified) indexed by n's factorization.
  Descent = UPPER bound (a row that stays >0 and grows is strong floor evidence; a "flat/weak" row is NOT a
  proof the floor fails — only that this descent could not certify it).  One-τ (τ=1) slice.  RH stays [OUT].

### §6bo — the {2,3}-GAP CLOSES: every 6∣n orbit is carried by a RAMIFIED prime ∣ N(M) (coverage map COMPLETE)

  probe_qmin_ramified_gap (EXACT q_min; adversarial per-prime descent = one-sided UPPER bound).  §6bn left
  ONE uncovered orbit class: v_2(n)=1 AND 3∣n (⟺ 6∣n, 4∤n; both small primes killed by n=2·3).  The
  ramified primes of an orbit are the odd primes dividing N(M), M=(p²−q²−np)+q(2p−n)i (the analog of D=425's
  {5,17}, which is N(M) for σ=3/4).  Adversarially minimizing v_p(q_min) at those primes on the n=6 orbits:

    orbit    N(M)          ramified   p=3        best ramified floor (m=4..7)
    5/6  n=6  2257=37·61   {37,61}    [0,0,2,3]  p=61: [2,3,4,5] LINEAR   (p=37: [0,1,2,3])
    1/6  n=6  2257=37·61   {37,61}    [0,0,2,3]  p=61: [2,3,4,5] LINEAR   (p=37: [0,1,2,3])
    7/6  n=6  3145=5·17·37 {5,17,37}  [0,0,2,3]  p=37: [1,2,3,4] LINEAR   (p=17: [0,0,1,2]; p=5: [0,0,0,0])

  RESULT (L5).  For EVERY 6∣n orbit tested, SOME ramified prime ∣ N(M) carries a clean growing (linear) floor
  — p=61 for N(M)=2257, p=37 for N(M)=3145.  NOT every ramified prime works (p=5 is dead for σ=7/6, p=37 is
  only weakly growing for σ=5/6), but at least one always does, so the class is covered.  Notably the ramified
  floor does NOT need a small prime (61 is large) — it is the §6aa "ramified/atom-norm" mechanism (v_p positive,
  absent from the geometric Vandermonde channel, growing with m), not mod-p pigeonhole, so large ramified primes
  still work.

  THE COMPLETE OP1 ORBIT-ROBUSTNESS COVERAGE MAP (empirical, one τ=1 slice, m≤7; the §6bl(M) gap now filled):
        n ≡ 0 mod 4              →  p=2,  S = 2v₂(n)−1 ≥ 3   [PROVED, §6bm]
        n odd                    →  p=2,  S < 0 (β 2-denominator), floor LARGE (~7·m)   [empirical]
        n ≡ 2 mod 4, 3 ∤ n       →  p=3,  3-unimodular w, floor [2,2,4,5]   [empirical; OB-42 mechanism]
        n ≡ 2 mod 4, 3 ∣ n (6∣n) →  a ramified prime ∣ N(M)   [empirical, this section]
  Every off-line orbit (τ=1) falls in exactly one row and has a prime with a linear q_min floor ⇒ inf over
  node sets of log q_min = Ω(m) = ω(log m) ⇒ OP1's arithmetic barrier holds ORBIT-ROBUSTLY (evidence tier).
  This upgrades §6bl(M)'s "plausibly multi-prime" to a concrete, per-orbit-decidable map.  HONEST SCOPE (L5):
  (i) only p=2 is PROVEN (§6bm), and only on its row; p=3 and the ramified rows are one-sided-descent evidence,
  not proofs; (ii) the p=3 row inherits OB-42's still-open irreducible joint bound; (iii) the ramified row has
  no proof at all yet — it is the §6aa mechanism, uncertified; (iv) only τ=1 and m≤7 scanned.  The VALUE is
  structural: it identifies, for each orbit, WHICH single prime a proof should target, turning "prove OP1 for
  all orbits" into four separate single-prime lemmas indexed by n mod 4 and 3∣n.  RH stays [OUT].

### §6bp — ROW 2 (n ODD) UPGRADED to near-proved: the v₂ profile is (1+i)-adically QUASI-LINEAR, C_j is PINNED

  probe_qmin_p2_nodd_ramified + probe_qmin_p2_nodd_confirm (EXACT integer / Gaussian-integer arithmetic, L9).
  §6bl(S)/§6bm(C) dismissed the n-odd row as "v₂(w'_i) goes negative and NON-LINEAR, floor large but by a
  mechanism NOT proved here."  That was too pessimistic: the profile is not chaotic, it is PERIOD-4 quasi-linear,
  and it is governed by the RAMIFIED prime π = 1+i.  Two facts, both verified exactly:

  (A) THE RAMIFIED-PRIME PROFILE.  For n odd, γ (= primitive Gaussian numerator of β = 1/(2ρ(ρ−1))) is
      BOTH-ODD (Re γ, Im γ both odd ⟺ γ ≡ 1+i mod 2), hence v_π(γ)=1 (N(γ) ≡ 2 mod 4).  The trace
      c_j := γʲ + γ̄ʲ (a rational integer) has, VERIFIED to j=30 for 6 orbits (σ=2/3,4/5,1/5,2/5,6/7,3/7):
            v_π(c_j) = (j+1) + a_j,   a_j PERIOD-4 in j:   a_j = (0, A, 0, 1)  for  j ≡ (1,2,3,0) mod 4,
      with the CLOSED FORM  A = 2·v₂(Re(γ)²−Im(γ)²) − 1  (from c₂ = 2(a²−b²) ⟹ v_π(c₂)=2+2v₂(a²−b²)).
      Consequently v₂(w'_i) = v_π(c_{i+1})/2 − (odd-free 2-part) is PERIOD-4 QUASI-LINEAR: each residue class
      i mod 4 is an arithmetic progression with common difference exactly 4S = −6 (S = v₂(β) = −3/2), so the
      average slope is S.  This is the §6bm linear profile "one prime up" — linear in the ramified valuation
      v_π rather than in v₂, the extra period-4 wobble being the ramification (e=2) of π over 2.

  (B) C_j IS NODE-INDEPENDENT (PINNED) with a UNIQUE (1+i)-adic minimum.  The leave-one-out pairing valuation
      C_j = min_r [ v₂(e_r(X'_j)) + v₂(w_{m−1−r}) ] is, under a two-sided adversary (min AND max over node
      sets), PINNED: adv-min == adv-max for every orbit and m=4,5,6,7, with the UNIVERSAL sequence
            min_j C_j = [−5, −7, −6, −10]  at m = [4,5,6,7]   (identical across n=3,5,7 orbits).
      The ultrametric min is UNIQUE (gap ≥ 1 to the 2nd-smallest term) except at m ≡ 2 mod 4, where two terms
      TIE (gap=0) yet the result stays pinned — the one delicate spot a full proof must close (a no-cancellation
      lemma for the tied pair).  Since C_j(m) ~ S·m < 0 (node-independent), the §6bf identity gives the
            LINEAR FLOOR  v₂(q_min) ≥ 1 + 3(m−1) − C_j(m) ~ (3 − S)·m = (9/2)·m − O(1),
      the steepest of all rows (slope ~4.5), matching §6bl's "measured 22,30,36" and §6bn's [18,26,29,38].

  STATUS UPGRADE (L5).  Row 2 moves from "empirical" to NEAR-PROVED: the mechanism is a (1+i)-adic
  unique-minimum, the SAME architecture as §6bm's proof, with two remaining gaps — (i) prove the period-4
  law a_j=(0,A,0,1) in general (a finite Z[i]-recurrence 2-adic induction, A=2v₂(a²−b²)−1), and (ii) the
  m≡2 mod 4 tie no-cancellation lemma.  Both are elementary, finite, RH-free.  Combined with §6bm (Row 1,
  n≡0 mod 4, PROVED), the p=2 channel now covers BOTH n≡0 mod 4 AND n odd — 3/4 of residues mod 4 — leaving
  only n≡2 mod 4 to the p=3 / ramified rows.  Descent = one-sided bound.  RH stays [OUT].

### §6br — FACT A CLOSED: the period-4 profile law PROVED as a polynomial identity (all n-odd orbits)

  probe_qmin_p2_nodd_profile_proof (EXACT symbolic identity in Z[α,β], L9).  §6bp's FACT A — the period-4
  quasi-linear profile — is now a THEOREM, not a fit.  Restated as a valuation law for c_j = γʲ+γ̄ʲ (γ=a+bi,
  a,b ODD):
        j ≡ 1,3 mod 4 :  v₂(c_j) = (j+1)/2                    (a_j = 0)
        j ≡ 0   mod 4 :  v₂(c_j) = j/2 + 1                    (a_j = 1)
        j ≡ 2   mod 4 :  v₂(c_j) = j/2 + v₂(a²−b²)            (a_j = 2·v₂(a²−b²) − 1)
  TWO independent proofs:
  (i) HAND (j odd).  γ = π·u with π=1+i, u ≡ 1 mod π a π-unit; c_j = πʲ·(uʲ+(−i)ʲūʲ); the bracket ≡
      jπ·(unit) mod π² (using −i = 1−π and, mod π, conjugation trivial + i≡1), so v_π(c_j)=j+1 ⟺ v₂(c_j)=(j+1)/2.
  (ii) SYMBOLIC (all j, all orbits).  c_j(a,b) is the integer Lucas trace poly; substituting a=2α+1,b=2β+1,
      each claim becomes a decidable polynomial statement — C_j/2^V ≡ 1 (mod 2) for j odd / j≡0, and for
      j≡2 that C_j/2^{j/2} = (a²−b²)·(odd poly) — VERIFIED for j=1..20 in Z[α,β].  Because these are
      polynomial identities in generic odd a,b, they hold for EVERY n-odd orbit simultaneously; period-4
      induction beyond j=20 is routine (trace recurrence mod 2^K is eventually periodic).
  CONSEQUENCE: v_π(c_j)=(j+1)+a_j with a_j period-4 = (0, 2v₂(a²−b²)−1, 0, 1), so v₂(w'_i) is EXACTLY
  period-4 quasi-linear (common difference 4S=−6 per class).  Row 2's PROFILE half is CLOSED; the only
  remaining gap for a full Row 2 theorem is FACT B's C_j node-independence at m≡2 mod 4 (the ultrametric
  tie, uniq-min gap=0), a node-dependent no-cancellation lemma.  RH stays [OUT].

  UPDATED COVERAGE MAP (superseding §6bo's table on Row 2):
        n ≡ 0 mod 4              →  p=2,  S = 2v₂(n)−1 ≥ 3,  floor 2m−2−S      [PROVED, §6bm]
        n odd                    →  p=2,  π=1+i.  UNIFORM minimax-free floor v₂(q_min) ≥ 1 − W_top = 3m/2 − O(1)
                                          via the VANDERMONDE COUPLING (§6cd): u_j := S_j/P'(x_j) satisfies
                                          V·u = w (V=(x_j^p) unit Vandermonde, Lagrange) ⇒ min_j v₂(u_j) ≤
                                          min_p v₂(w_p) = W_top (FACT A §6br) ⇒ v₂(q_min)=1−min_j v₂(u_j) ≥
                                          1−W_top.  Both parities, NO minimax; supersedes §6ca (m≡0) & the
                                          REFUTED §6cb (m≡2).  log q_min = Ω(m) ≫ ω(log m) ⇒ OP1 CLOSES on Row 2.
                                          [THEOREM CANDIDATE modulo FACT A; verified EXACT m=4..18, n=3,5,7]
        n ≡ 2 mod 4, 3 ∤ n       →  p=3,  3-unimodular w, floor [2,2,4,5]       [empirical; OB-42 mechanism]
        n ≡ 2 mod 4, 3 ∣ n (6∣n) →  a ramified prime ∣ N(M)                     [empirical, §6bo]

### §6bs — the pinned C_j(m) closed form: C_j(m) = ⌊−3m/2⌋ + period4(m); the tie only shifts a bounded O(1)

  probe_qmin_p2_nodd_Cj_form (EXACT, L9; two-sided adversary, m=4..10, orbits (2/3,1),(4/5,1),(6/7,1)).
  Sharpens FACT B by extracting the exact closed form of the node-independent C_j(m) and localizing the tie.
  RESULT — C_j(m) for m=4..10 (orbit (2/3,1)): [−5,−7,−6,−10,−11,−13,−12], and the correction
        C_j(m) − ⌊−3m/2⌋ = [1, 1, 3, 1, 1, 1, 3]  (period-4-in-m).
  READINGS:
   • PINNED (adversary min == max, i.e. C_j node-independent) at EVERY m EXCEPT m ≡ 2 mod 4.  For m ≢ 2 the
     argmin term index r* is UNIQUE (uniq-min gap ≥ 1: gaps 1,4,3,1,5 at m=4,5,7,8,9), so the ultrametric
     minimum is clean and C_j is pinned — the §6bm/§6bi unique-minimum machinery applies verbatim.
   • m ≡ 2 mod 4 is EXACTLY the tie (uniq-min gap = 0): two equal top terms.  There the correction jumps
     (+3 for (2/3); +4→+5 for (4/5) — the per-orbit spike A = 2v₂(a²−b²)−1 of FACT A), and for orbit (6/7)
     at m=6 the two-sided adversary gives C_j ∈ [−4, 0] — pinning genuinely BREAKS (node-dependent) at the tie.
   • DECISIVE for the barrier: even at the tie, the adversary's best (max over node sets) min_j C_j stays
     ≈ ⌊−3m/2⌋ + O(1), the O(1) a bounded per-orbit constant (FACT A's fixed spike, NOT growing in m).  Hence
     the floor 1 + 3(m−1) − C_j(m) ≈ (9/2)m − O(1) is LINEAR at EVERY m.  Measured floors (2/3): 15,20,22,29,
     33,38,40 — clean linear growth, the m≡2 entries only a small constant dip, never a collapse.
  CONSEQUENCE: the m≡2 mod 4 ultrametric tie does NOT break Row 2's floor; it shifts C_j by a bounded per-orbit
  constant (governed by the PROVED FACT A spike).  So Row 2 gives log q_min = Ω(m) ≫ ω(log m) — OP1 closes for
  every n-odd orbit — MODULO one remaining lemma: that the tie's max-over-nodes min_j C_j correction is O(1)
  uniform in m (i.e. the two tied top terms cannot cancel to arbitrary depth as m grows).  This is FACT B in
  its sharpest form: a no-cancellation bound at a SINGLE residue class m ≡ 2 mod 4, not a full node-independence
  proof.  HONEST (L5): adversary one-sided per direction; the (6/7) m=6 [−4,0] spread shows the tie is real,
  and (4/5)'s +4→+5 correction across m=6→10 means the O(1) bound itself is empirical, not yet proved.  RH [OUT].

### §6bt — the m≡2 mod 4 tie correction is BOUNDED in m (FACT B's O(1) confirmed to m=22, 4 orbits)

  probe_qmin_p2_nodd_tie_growth (EXACT, L9).  §6bs left one worry: (4/5)'s correction went +4→+5 across m=6→10
  — real growth (slope degrades) or oscillation?  This probe isolates the tie: for each n-odd orbit it pushes
  m through {6,10,14,18,22} (all ≡2 mod 4) and reports corr(m) = hi − ⌊−3m/2⌋, hi := max over node sets of
  min_j C_j (the adversary's best, which CAPS the floor from below).  RESULT (corr per orbit, m=6..22):
        (2/3,1): 3, 3, 3, 3, 3      — FLAT
        (4/5,1): 4, 5, 4, 5, 4      — bounded oscillation in {4,5}
        (6/7,1): 8, 4, 5, 4, 5      — {4,5} for m≥10 (the m=6 "8" is a one-off small-m tie edge)
        (2/5,1): 8, 4, 5, 4, 5      — same pattern
  DECISIVE: corr(m) is BOUNDED (flat, or period-2 oscillation in a fixed 2-element set) for EVERY orbit through
  m=22 — NO growth.  §6bs's +4→+5 was oscillation, not a trend.  So the floor 1+3(m−1) − C_j(m) = (9/2)m − O(1)
  is LINEAR at every m, and the gap to (9/2)m stays a small constant (5 for (2/3): 27−22, 63−58, …; ~6–7 for the
  others).  This is FACT A's fixed spike A = 2v₂(a²−b²)−1 governing the tie, exactly as predicted — the tie does
  NOT let the correction accumulate with m.
  ROW 2 STATUS: profile PROVED (§6br), C_j(m)=⌊−3m/2⌋+O(1) with the O(1) now confirmed BOUNDED in m ⇒ floor
  (9/2)m − O(1) ⇒ log q_min = Ω(m) ≫ ω(log m).  OP1 closes for every n-odd orbit modulo the SOLE remaining
  rigorous step: prove the m≡2 mod 4 tie's two equal top ultrametric terms cannot cancel beyond a FACT-A-bounded
  depth (a single-residue-class no-cancellation lemma; the constant is pinned by v₂(a²−b²)).  HONEST (L5):
  adversary one-sided (hi = UPPER bound ⇒ corr is a conservative LOWER bound on the true worst correction; a
  bounded hi is strong evidence, not proof); m≤22, 4 orbits.  RH [OUT].

### §6bu — the FACT B quantity ISOLATED: the tie's cancellation depth is a fixed small constant (1–2), ≤ A

  probe_qmin_p2_nodd_cancel_depth (EXACT Fractions, L9).  Pins down exactly what FACT B must bound.  At m≡2
  mod 4 the ultrametric minimum of C_j = v₂(Σ_r (−1)^r w'_{m−1−r} e_r(y_{≠j})) ties; a tie hurts only if the
  tied terms CANCEL, so the crux quantity is
        depth := v₂(sum of tied terms) − V,   V = the (equal) valuation of the tied terms
  i.e. the excess of C_j over the naive tie value.  RESULT (5 n-odd orbits, m∈{6,10,14,18,22}, adversary's-best
  set AND 200 random valid sets):
   • EXACTLY TWO terms tie (ntied = 2) in every case — the two lowest-valuation terms of the pairing.
   • depth is a FIXED SMALL CONSTANT per orbit, EXACTLY constant across m=6..22:
        (2/3,1) γ=−99−27i  A=7 :  depth = 2   (all m)
        (4/5,1) γ=−725−375i A=5 :  depth = 1   (all m)
        (6/7,1) γ=−539−343i A=5 :  depth = 1   (all m)
        (2/5,1) γ=−775−125i A=5 :  depth = 1   (all m)
        (3/5,1) γ=−775−125i A=5 :  depth = 1   (all m)
     The adversary's max and the random-tie max coincide — depth is NOT node-inflatable.  And depth ≤ A =
     2v₂(a²−b²)−1 with room to spare (2≤7, 1≤5): the FACT-A spike is a (loose) ceiling; the true depth is even
     smaller.  Hence C_j = V + depth = ⌊−3m/2⌋ + O(1) with the O(1) = depth, a fixed constant.
  CONSEQUENCE — FACT B in its FINAL, minimal form: "at m≡2 mod 4, exactly two terms tie for the C_j ultrametric
  minimum, and their ratio is ≢ −1 mod 2^{depth+1} for a per-orbit constant depth ≤ A" — a bounded no-cancellation
  bound on a SINGLE PAIR of explicit 2-adic units (leading units of w' from the PROVED FACT A profile, and of the
  two e_r Newton sums), NOT a node-independence statement over all columns.  This is the crispest OP1 outsource
  nugget: prove the two tied top terms cannot 2-adically align past depth A.  With it, Row 2's floor v₂(q_min) =
  1 + 3(m−1) − C_j = (9/2)m − O(1) is PROVED for every n-odd orbit.  HONEST (L5): adversary/random both one-sided
  (max depth = LOWER bound on true worst); 5 orbits, m≤22; the depth-constant equals corr from §6bt as expected.
  RH [OUT].

### §6bv — the tie is r=(0,1); FACT B reduces to a 2-adic DISTANCE v₂(τ−σ) to ONE fixed orbit target

  probe_qmin_p2_nodd_tie_structure (EXACT, L9).  Extracts the two tied term-indices and their leading units.
  DECISIVE STRUCTURE (both orbits (2/3),(4/5), m=6,10, every tie): the two tied terms are ALWAYS the two
  TOP-exponent terms r=0 and r=1 (ADJACENT) of the pairing C_j = v₂(⟨w, ε(X'_j)⟩), where ε = signed
  elem-symm coeffs of ∏_{k≠j}(X−x_k) and w = B⁻¹d is NODE-INDEPENDENT:
        r=0  (X^{m−1} coeff, e_0=1) :  term₀ =  w_{m−1}                     — NODE-INDEPENDENT fixed constant
        r=1  (X^{m−2} coeff, e_1)   :  term₁ = −w_{m−2}·(Σ_{k≠j} x_k)      — node-controlled via the node-sum
  WHY THE TIE SITS AT m≡2 mod 4 (now transparent): each x_k = 1 − 2/(4t_k²+1) is an odd 2-adic unit, so
  e_1 = Σ_{k≠j} x_k is a sum of m−1 odd units ⟹ v₂(e_1) ≡ (m−1) mod 2.  At m≡2 mod 4, m−1 is ODD ⟹ e_1 odd
  (v₂=0) ⟹ v₂(term₁)=v₂(w_{m−2}); the tie v₂(term₀)=v₂(term₁) is then EXACTLY the profile equality
  v₂(w_{m−1})=v₂(w_{m−2}), delivered by the PROVED FACT A period-4 law at this residue.  (At m≢2 mod 4, m−1
  even ⟹ e_1 even ⟹ the two top terms separate ⟹ unique min ⟹ C_j pinned — matches §6bs exactly.)
  DEPTH IS A 2-ADIC DISTANCE (the clean FACT B identity): with W:=w_{m−1}/2^V, W':=w_{m−2}/2^V fixed odd
  units and σ := Σ_{k≠j} x_k the odd node-sum,
        depth = v₂(term₀+term₁) − V = v₂(W − W'σ) = v₂(τ − σ),   τ := W/W' = w_{m−1}/w_{m−2}  (FIXED odd target).
  So the adversary raises C_j by exactly the 2-adic CLOSENESS of the node-sum σ to a FIXED per-orbit target τ —
  the SAME shape as §6o's ψ = v_p(x_k − a_k/b_k) p-adic-distance identity, now for p=2, Row 2, ONE target.
  Verified leading units (mod 32): (2/3) m=6 u₁≡17,u₂≡19,Σ≡4 depth 2; m=10 u₁≡27,u₂≡1,Σ≡28 depth 2;
  (4/5) m=6 u₁≡27,u₂≡15,Σ≡10 depth 1; m=10 u₁≡1,u₂≡25,Σ≡26 depth 1.
  ⚠ FACT B "FINAL FORM" (SUPERSEDED — CORRECTED by §6bw): the tempting statement "σ cannot 2-adically
  approximate τ beyond depth A" is a SINGLE-TARGET, single-column 2-adic bound.  §6bw REFUTES it as stated:
  σ IS freely choosable (any m−1 distinct nodes), and unconstrained it approaches τ to depth ≥ 16–20.  The
  real ceiling is NOT a local approximation bound on σ; it is a MINIMAX-optimum statement (see §6bw).
  Adversary one-sided.  RH [OUT].

### §6bw — the Row 2 depth ceiling is a MINIMAX-optimum fact, NOT a local 2-adic bound (route decision; corrects §6bv)

  probe_qmin_p2_nodd_image_vs_global (EXACT, L9).  Tests which mechanism caps the tie's cancellation depth
  (§6bu: ≤2 under the real optimization): (1) a PURE 2-adic image bound on σ, or (2) the GLOBAL minimax.
  DECISIVE (refutes route 1):
    • Image sizes |U_K| = #{x_t mod 2^K, t=1..400} = 2,2,3,4,7,12,23 for K=4..10 — GROW (≈2^{K/2}), so the
      node-value set is 2-adically rich, not O(1).
    • UNCONSTRAINED max depth = max over (m−1)-subsets of v₂(τ−σ) GROWS, unbounded: (4/5) m=10 → 20;
      (6/7) m=6 → 17, m=14 → 16.  So a single column's cancellation CAN be driven arbitrarily deep.
  KEY REALISATION: in this OP1 setup ANY m distinct nodes form a valid collision, so σ=Σ_{k≠j}x_k IS freely
  choosable — the §6bv "σ can't approach τ" bound is FALSE as a standalone statement.  The reason the REAL
  optimization (§6bu) shows depth ≤ 2 is that the adversary maximizes min_j C_j (a MINIMAX over columns), and
  deepening ONE column's cancellation toward τ is a LOSING move for the min-over-columns objective: it does
  not raise the minimum, and generically lowers other columns.  So the true FACT B is:
        "at the collision that MAXIMIZES min_j C_j, the argmin column's tie-depth is ≤ A"
  — a statement about the STRUCTURE OF THE MINIMAX OPTIMUM (the §6ax "argmax moves" competition), NOT a local
  2-adic Diophantine bound on σ.  ROUTE DECISION (L5): the clean single-target image-lemma route for Row 2 is
  RETIRED; a proof must engage the global column-coupling.  This DOWNGRADES the Row 2 "NEAR-PROVED" claim: the
  profile (§6br) and tie-locus (§6bv) are PROVED, the floor is empirically LINEAR to m=22 (§6bt), but the
  no-cancellation ceiling is a global minimax bound with no known local reduction — a genuine open core, not a
  2-line lemma.  Adversary/hill-climb one-sided (deeper unconstrained depths only strengthen the refutation).
  RH [OUT].

### §6bx — the p=2 floor COLLAPSES to a node-Vandermonde solve: v₂(q_min) = 1 − min_j v₂((V⁻¹w)_j) (verified; NOT prime-agnostic)

  probe_qmin_vandermonde_reduction (EXACT, L9).  The Lagrange interpolation identities
  Σ_j x_j^r·(S_j/P'(x_j)) = w_r (r=0..m−1; S_j = off-line pairing ⟨w, coeffs ∏_{k≠j}(X−x_k)⟩,
  P'(x_j)=∏_{k≠j}(x_j−x_k)) say the vector y_j := S_j/P'(x_j) (whose v_p = C_j − N_j) solves V y = w with
  V[r][j]=x_j^r the NODE VANDERMONDE and w the FIXED off-line vector — i.e. y = V⁻¹w = the Lagrange
  QUADRATURE WEIGHTS of the functional L(Q)=⟨w,coeffs Q⟩ (⟨w,coeffs Q⟩ = Σ_j y_j Q(x_j), deg Q ≤ m−1).
  VERIFIED (all 5 orbits (2/3),(3/4),(4/5),(6/7),(2/5); m=4..7):
    • Lagrange identity y_j == S_j/P'(x_j) HOLDS exactly (y = V⁻¹w confirmed).
    • p=2: off_2 := v₂(q_min)+min_j v₂(y_j) ≡ 1 UNIFORMLY ⇒ v₂(q_min) = 1 − min_j v₂((V⁻¹w)_j).  CONFIRMED,
      matches the PROVED §6bf floor identity, now in closed Vandermonde form.
    • p=3: off_3 ≡ 0 ⇒ v₃(q_min) = −min_j v₃((V⁻¹w)_j).
  REFUTED (honest, L5): the reduction is NOT prime-agnostic — for p=5 the offset is non-constant (∈{0,−1,2,…}),
  so there is NO single universal Vandermonde object across all primes; the offset is p-special.  My "unify all
  4 rows into one V⁻¹w object" hope is thus only valid on the p=2 rows (1,2) and the p=3 row (3), not globally.
  CRAMER FORM (p=2):  v₂(q_min) = 1 + v₂(det V) − min_j v₂(det V^{(j)}),  V^{(j)} = V with column j → w.
  STRUCTURAL READING: v₂(det V) = Σ_{k<l} v₂(x_l−x_k) ≥ 3·C(m,2) is QUADRATIC in m, while the floor is LINEAR
  (~(9/2)m), so the floor is a DELICATE LINEAR GAP between two quadratic-in-m valuations (det V vs min_j det V^{(j)}).
  The one free global identity Σ_j y_j = w_0 gives only min_j v₂(y_j) ≤ v₂(w_0) ⇒ a CONSTANT lower bound on
  v₂(q_min) (loose: the y_j are ~v₂ −3m each and cancel to the small w_0).  So this reframing is CLEAN and
  CORRECT for p=2/p=3 but does NOT dissolve the §6bw hard-minimax difficulty — it re-expresses it as "some
  Lagrange weight of the fixed functional w, on nodes with pairwise v₂≥3 differences, has 2-power denominator
  ≥ 2^{(9/2)m}".  Structural identity check (adversary-free).  RH [OUT].

### §6by — CORE-2 has HUGE SLACK, and min_j C_j is pinned at the profile top W_top = v₂(w_{m−1}) (scaling)

  probe_qmin_p2_nodd_minC_scaling (EXACT, L9).  The §6bf reduction v₂(q_min) ≥ 1 + 3(m−1) − min_j C_j means the
  floor is LINEAR as soon as min_j C_j = o(m); there is HUGE SLACK — any bound min_j C_j ≤ (3−c)m already gives a
  positive-linear floor, so the tight §6bu ceiling (≤2) is NOT needed.  Scaling the adversary that MAXIMIZES
  min_j C_j (n-odd orbits (2/3),(4/5),(6/7); m=4..16) found min_j C_j is not merely o(m) but NEGATIVE-LINEAR,
  pinned at the profile-top valuation W_top := v₂(w_{m−1}), which is ORBIT-INDEPENDENT with closed form
        W_top(m) = 1 − 3m/2   (m ≡ 0 mod 4),      W_top(m) = 2 − 3m/2   (m ≡ 2 mod 4).
  DICHOTOMY: at m ≡ 0 mod 4 EVERY column is "leading-dominated" (max min_j C_j = W_top exactly, #lead = m); at
  m ≡ 2 mod 4 the adversary lifts min_j C_j a BOUNDED amount above W_top (#lead = 0).  So the adversary cannot
  push min_j C_j anywhere near +3m — it is trapped at ≈ −3m/2, giving v₂(q_min) ≈ (9/2)m, NOT via minimax but via
  the fixed off-line profile.  Hill-climb one-sided (lower bound on the true adversarial max).  RH [OUT].

### §6bz — the PROFILE-MINIMUM route: an UNCONDITIONAL exact-floor mechanism for m ≡ 0 mod 4 (no minimax)

  probe_qmin_p2_nodd_profile_minimum (EXACT, L9).  Structural explanation of §6by, orbit-free.  The pairing splits
        S_j = w_{m−1} + Σ_{i<m−1} ±e_{m−1−i}(X'_j)·w_i.
  Each node x_t=(4t²−1)/(4t²+1) is a 2-adic UNIT ⇒ v₂(e_r(X'_j)) ≥ 0 ⇒ v₂(each lower term) ≥ v₂(w_i).  The
  valuation PROFILE v₂(w_i) (i=0..m−1) has period-4 increments [0,−3,−1,−2] (= the PROVED FACT A / §6br spike):
  e.g. m=8 → [−1,−1,−4,−5,−7,−7,−10,−11].  Consequence of the increment pattern:
    • m ≡ 0 mod 4 → top index m−1 ≡ 3 mod 4 is the STRICT unique profile minimum (gap = 1 to w_{m−2});
    • m ≡ 2 mod 4 → top index m−1 ≡ 1 mod 4 TIES w_{m−2} (gap = 0) — exactly the §6bv adjacent r=(0,1) tie.
  At m ≡ 0 mod 4 the strict min ⇒ v₂(rest) > v₂(w_{m−1}), so by the ultrametric  C_j = v₂(S_j) = W_top for EVERY
  column and EVERY collision — UNCONDITIONALLY, no adversary/minimax.  VERIFIED over 120 random collisions × 3
  orbits × m∈{4..16}: all-dom = 120/120 & lifted = 0/120 at m≡0 mod4; all-dom = 0/120 & lifted = 120/120 at
  m≡2 mod4.  Closed form W_top CONFIRMED all orbits.  So the minimax difficulty is CONFINED to m ≡ 2 mod 4.

### §6ca — THEOREM CANDIDATE (m ≡ 0 mod 4, n-odd Row 2): v₂(q_min) ≥ (9/2)m − 3, from proved facts, NO minimax

  probe_qmin_p2_nodd_m0mod4_theorem (EXACT, L9).  Assembling §6bf + §6br(FACT A) + §6bz:
    (i)   FACT A (§6br, PROVED): period-4 profile ⇒ w_{m−1} strict profile min for m≡0 mod4, W_top = 1−3m/2.
    (ii)  nodes are 2-adic units ⇒ v₂(e_r(X'_j)) ≥ 0.
    (iii) ⇒ (ultrametric) C_j = W_top for every column & collision (leading-domination, §6bz).
    (iv)  §6bf EXACT identity v₂(q_min) = max_j(1 + N_j − C_j) with N_j = Σ_{k≠j}v₂(x_j−x_k) ≥ 3(m−1) UNCONDITIONAL.
    ⇒  v₂(q_min) = 1 − W_top + max_j N_j  EXACTLY  ⇒  v₂(q_min) ≥ 1 − W_top + 3(m−1) = (9/2)m − 3   [LINEAR].
  DIRECT VERIFICATION (computing q_min the hard way via integer determinants, guarding against an identity-impl
  error): across 3 orbits × m∈{4,8,12}, the identity "all C_j = W_top  &  v₂(q_min) = 1 − W_top + max_j N_j" is
  OK on every sampled collision, and v₂(q_min) always exceeds (9/2)m−3.  NOTE (L5): the observed MINIMUM of
  v₂(q_min) is STRICTLY ABOVE (9/2)m−3 (e.g. m=4→18 vs 15; m=8→44/45 vs 33; m=12→71 vs 51) because the
  N_j ≥ 3(m−1) bound is LOOSE: node parities force some pairs to v₂(t_j²−t_k²) ≥ 2 (opposite-parity pairs
  cannot cover all C(m,2) pairs), so min-over-collisions of max_j N_j > 3(m−1).  This does NOT weaken the theorem
  — (9/2)m−3 is a valid LINEAR LOWER bound (exactly what OP1 needs); the exact minimum is a separate, HIGHER
  quantity (min over collisions of max_j N_j, a clean parity/clustering sub-question, not required for OP1).
  Period-4 profile & strict-min dichotomy re-confirmed at m=20,24 (W_top=−29,−35; top_gap=1).
  STATUS (L5): Row 2 for m ≡ 0 mod 4 is now a THEOREM CANDIDATE resting ONLY on already-proved facts (FACT A
  §6br + the trivial unit/ultrametric steps) — the minimax core is fully expelled to m ≡ 2 mod 4.  Awaiting a
  formal write-up citing FACT A; until then it is discovery-tier evidence.  RH stays [OUT].

### §6cb — m ≡ 2 mod 4 CLOSES too: the "lift ≤ excess" joint inequality via σ_j = T − x_j (Row 2 complete candidate)

  probe_qmin_p2_nodd_m2mod4_joint (EXACT, L9).  At m≡2 mod4 the top two profile entries TIE (v₂(w_{m−1}) =
  v₂(w_{m−2}) = W_top = 2 − 3m/2), so S_j can cancel; define lift_j := C_j − W_top ≥ 0 (top-two cancellation
  depth) and excess_j := N_j − 3(m−1) ≥ 0 (extra clustering of column j).  The §6bf identity gives
        v₂(q_min) = 9m/2 − 4 − min_j(lift_j − excess_j),
  so the floor is LINEAR iff Q := max over collisions of min_j(lift_j − excess_j) is BOUNDED.
  JOINT PROOF SKETCH: from §6bv, S_j = w_{m−2}(τ − σ_j) + higher, τ = w_{m−1}/w_{m−2}, σ_j = Σ_{k≠j}x_k = T − x_j
  (T = total node sum), so lift_j ≤ v₂(τ − σ_j).  If min_j lift_j ≥ L then v₂(τ − σ_j) ≥ L for every j, and
  σ_j − σ_{j'} = x_{j'} − x_j ⇒ (ultrametric) v₂(x_j − x_{j'}) ≥ L for ALL pairs ⇒ N_j ≥ (m−1)L ⇒ excess_j ≥
  (m−1)(L−3).  Hence min_j(lift − excess) ≤ L − (m−1)(L−3) = 3(m−1) − (m−2)L ≤ 3 for L ≥ 3 (and ≤ L ≤ 2 for
  L < 3).  So Q ≤ 3 ⇒ v₂(q_min) ≥ 9m/2 − 7, LINEAR.  The excess overwhelms the lift by factor (m−2): deep
  cancellation REQUIRES clustering that costs far more than it saves.
  MEASURED (adversary MAXIMIZING min_j(lift_j − excess_j); orbits (2/3),(4/5),(6/7); m=6,10,14): Q is not just
  ≤3 but NEGATIVE (−4 … −21) and decreasing in m; min_j lift_j stays ≤ 3 (adversary cannot even push the MIN
  lift up), min pairwise v₂ = 3 (mechanism "min-lift ≤ min-pairwise-v₂" holds everywhere).  So the floor at
  m≡2 mod4 is ≥ 9m/2 − 7 with large margin.  DIRECT q_min (integer determinants, independent of the identity):
  min over 80 collisions × 3 orbits of v₂(q_min) = 27–29 (m=6), 53–55 (m=10) — all ≥ 9m/2 − 7 (20, 38).  ✓
  STATUS (L5) — DOWNGRADED by §6cc: the JOINT PROOF SKETCH above is REFUTED.  Its load-bearing step
  lift_j ≤ v₂(τ − σ_j) is FALSE (see §6cc: deep lift can come from TAIL cancellation in the higher-order
  R_j terms, decoupled from σ_j).  The FLOOR bound v₂(q_min) ≥ 9m/2 − 7 at m≡2 mod4 remains EMPIRICALLY
  robust (strong lift-seeking adversary maximizing min_j(lift−excess) gives Q ≤ −4, decreasing in m; direct
  q_min ≥ bound) — but it is now an UNPROVEN CONJECTURE for m≡2 mod4, NOT a theorem candidate.  Contrast
  §6ca (m≡0 mod4): that half IS a clean theorem candidate (strict profile min ⇒ lift ≡ 0 unconditionally,
  no σ_j mechanism needed).  So Row 2 is HALF-CLOSED: m≡0 mod4 proved-modulo-FACT-A; m≡2 mod4 empirical
  only, proof mechanism dead.  RH stays [OUT].

### §6cc — REFUTATION of the §6cb mechanism; and RECONCILIATION confirming the m≡2 mod4 floor holds

  probe_qmin_p2_nodd_lift_bound (EXACT, L9), and a strong lift-seeking adversary.  TWO findings:

  (1) REFUTED (§6cb's key step): lift_j ≤ v₂(τ − σ_j) is FALSE.  Writing S_j = w_{m−2}(τ − σ_j) + R_j with
  v₂(R_j) ≥ g := v₂(w_{m−3}) − W_top, the tie can be broken by TAIL cancellation inside R_j at depths ≥ g,
  giving lift_j ≫ v₂(τ − σ_j).  Measured violations (lift, dd=v₂(τ−σ)): orbit 6/7 m=14 → (12, 3); orbit 4/5
  m=10 → (6, 4),(5, 4); orbit 6/7 m=6 → (4, 3).  g = 2 everywhere.  So "deep lift ⇒ σ_j ≈ τ ⇒ clustering ⇒
  excess" collapses: a single column CAN have large lift with NO clustering (excess=0) — verified directly,
  e.g. (lift,excess)=(15,0) at n=7 m=6 and (12,0) at n=5 m=10.  The §6cb σ_j-clustering proof is DEAD.

  (2) RECONCILED (the floor still holds): the floor uses min_j(lift−excess), NOT max_j.  A single high-lift
  column does not lower q_min = det/gcd; the adversary must raise the MINIMUM over ALL m columns.  A strong
  adversary (lift-seeking clustered inits + cluster/align moves, 120 restarts × 14 rounds) MAXIMIZING
  min_j(lift_j − excess_j) achieves only:
        Q = max_collisions min_j(lift−excess):  n=5 → −5(m=6), −11(m=10), −20(m=14);
                                                 n=7 → −4(m=6), −13(m=10), −18(m=14).
  Q is NEGATIVE and DECREASING in m ⇒ floor = 9m/2 − 4 − Q is ABOVE 9m/2 − 7 with growing margin.  The
  earlier "floor violated (15,0)" alarm was a max-over-columns vs min-over-columns conflation: high-lift/
  zero-excess columns exist but are NEVER simultaneous across all columns — some column always keeps
  lift−excess ≤ −4.

  STATUS (L5): m≡2 mod4 floor v₂(q_min) ≥ 9m/2 − 7 is EMPIRICALLY ROBUST (strong adversary + direct q_min)
  but PROOF-OPEN — both the σ_j route (§6cb) and the single-target image-lemma route (§6bw) are RETIRED.
  A valid proof must explain why the m columns cannot SIMULTANEOUSLY carry deep tail-cancellation lift; the
  tail terms R_j are coupled across columns through the shared w-vector, and empirically that coupling
  forbids joint alignment — but no clean argument is in hand.  This is the live open sub-problem for Row 2.
  RH stays [OUT].

### §6cd — the VANDERMONDE-COUPLING floor for Row 2 (n odd): completing §6bh's dismissed ultrametric route

  PROVENANCE / HONEST CREDIT (L5): the factorization is NOT new here — §6bh already proved
        C_j = N_j + v₂(u_j),   u := (V^T)⁻¹ w,   v₂(q_min) = 1 − min_j v₂(u_j)   (★★),
  with u_l = S_l/P'(x_l) the Lagrange/quadrature weights.  §6bh ran the ultrametric on the SINGLE relation
  Σ_l u_l = w_0 (the p=0 row of V^T u = w), got min_l v₂(u_l) ≤ v₂(w_0), and — examining ONLY σ=3/4 (Row 1,
  where the profile v₂(w_i)=4+3i INCREASES so w_0 IS the min) — dismissed the ultrametric as "trivial/lossy."
  §6cd's ACTUAL (smaller) new content is twofold: (1) use ALL m relations Σ_l x_l^p u_l = w_p (p=0..m−1),
  giving min_l v₂(u_l) ≤ min_p v₂(w_p) — accessing w_{m−1} needs the p=m−1 row §6bh never used; (2) the
  observation that for n ODD the profile DECREASES, so min_p v₂(w_p) = W_top = v₂(w_{m−1}) ≈ −3m/2, and the
  same ultrametric §6bh called trivial becomes a LINEAR floor.

  probe_qmin_p2_nodd_vandermonde_floor (EXACT, L9).  With (★★) from §6bh and V = (x_j^p) a UNIT Vandermonde
  (nodes x_j = (4t²−1)/(4t²+1) are 2-adic UNITS), the ultrametric on V·u = w gives v₂(w_p) ≥ min_j v₂(u_j)
  for EVERY p, hence
        min_j v₂(u_j) ≤ min_p v₂(w_p) = W_top       (profile min = TOP index for n odd, since it DECREASES; FACT A §6br).
  Therefore
        ┌─────────────────────────────────────────────────────────────────────────┐
        │  v₂(q_min) ≥ 1 − W_top = 3m/2 − 1 (m≡2 mod4) or 3m/2 (m≡0 mod4)  UNIFORM   │
        └─────────────────────────────────────────────────────────────────────────┘
  LINEAR in m, BOTH parities of m, NO minimax, NO σ_j mechanism.  Since log q_min ≥ (3m/2 − 1)·log 2 = Ω(m)
  ≫ ω(log m), this CLOSES OP1 on the entire n-odd Row 2.  Dependencies: (a) the §6bf/§6bh floor identity (★★),
  (b) classical Lagrange interpolation, (c) FACT A (profile decreasing ⇒ min at top index, §6br PROVED for
  n odd).  It does NOT use §6cb (refuted), §6cc, or §6bw — the minimax core is bypassed.  It is NOT a new
  factorization (that is §6bh); it is the completion of §6bh's route for the n-odd profile.

  MEASURED (EXACT Fraction, orbits (2/3),(4/5),(6/7) i.e. n=3,5,7; m=4..18, both parities):
    • identity V·u = w holds EXACTLY for every p, every collision (id V·u=w = OK), all orbits/m;
    • v₂(u_j) = C_j − N_j EXACTLY (v2u=C−N = OK), all orbits/m;
    • profile min = W_top (pmin==W_top = True) confirmed m=4..18 all orbits — FACT A operative;
    • min_j v₂(u_j) ≤ W_top everywhere; DIRECT q_min (integer determinants, spot-checked m ≤ 10) ≥ 1 − W_top
      with margin ≥ 0 (m=4: q_min 18–19 ≥ 6; m=6: 27–29 ≥ 8; m=8: 44–45 ≥ 12; m=10: 53–55 ≥ 14).
      The proven bound 3m/2 is LOOSER than the true ~9m/2 (whence the large margin), but UNCONDITIONALLY PROVED.
  STATUS (L5): this is a genuine advance — Row 2 (n odd) now has a UNIFORM minimax-free floor proof, superseding
  both the parity-split §6ca and the refuted §6cb.  The two mathematically load-bearing facts (V·u = w; v₂(u_j)
  = C_j − N_j) are ORBIT- and m-INDEPENDENT algebraic identities (verified m=4..12; cannot fail at larger m).
  The only remaining formal dependency is FACT A (§6br, PROVED).  NOT machine-checked, NOT promoted to proof/.
  If one wants the sharp 9m/2 constant, that remains open (needs the cancellation structure) — but OP1 only
  needs ω(log m), which 3m/2 delivers.  RH stays [OUT].

### §6ce — SCOPE of the Vandermonde principle: it is Row-2-specific, NOT a coverage-map unification (L5)

  The §6cd bound v_p(q_min) ≥ 1 − profile_min(w; p) is VALID at any prime p where the nodes are p-adic units
  (the whole derivation needs only: §6bf identity, Lagrange V·u = w, and unit nodes).  Natural question: does
  it UNIFY the 4-row coverage map?  TESTED (EXACT, p=2, τ=1 orbits spanning all n mod 4; m=4,6,8):
        n odd (3,5,7):      profile_min(p=2) = −5,−7,−11 ≈ −3m/2  ⇒ floor 6,8,12 LINEAR — §6cd CARRIES.
        n≡0 mod4 (4,8):     profile_min(p=2) = +4,+6 CONSTANT     ⇒ floor 1−pm ≤ 0, VACUOUS (yet true v₂(q_min)
                            = 6,16,26 IS linear — p=2 carries n≡0 via §6bm, NOT §6cd; here min_j v₂(u_j) dips
                            FAR below profile_min, an extra V⁻¹w cancellation the simple ultrametric can't see).
        n≡2 mod4 (2,6,10):  profile_min(p=2) = +2 CONSTANT        ⇒ floor VACUOUS; true v₂(q_min) = 0,4,5
                            BOUNDED — p=2 genuinely does NOT carry; needs p=3 (Row 3) / ramified prime (Row 4).
  CONCLUSION (L5): §6cd is INTRINSICALLY the Row-2 mechanism.  Its floor is linear ⟺ profile_min(w; p=2) is
  linearly negative ⟺ n odd.  It does NOT collapse the coverage map; the 4-row split is genuine (different
  carrying primes for different n-classes).  The earlier speculation that §6cd might unify OP1 is REFUTED.
  META-PRINCIPLE that DOES survive: "at a prime p of unit nodes, v_p(q_min) ≥ 1 − profile_min(w;p)" is a
  uniform lower-bound tool — but it is only USEFUL (non-vacuous) on the row whose profile at p is linearly
  negative, i.e. Row 2 at p=2.  For Rows 1,3,4 the profile-min bound is loose/vacuous and the existing
  row-specific mechanisms (§6bm; p=3 3-unimodular; ramified §6bo) remain necessary.  RH stays [OUT].

  IDENTITY-SCOPE FOOTNOTE (L9, checked per-collision): the §6bf identity v₂(q_min) = 1 − min_j(C_j − N_j)
  itself holds 25/25 for n≡0 mod4, n odd, and n=6, but FAILS for n=2 (σ=1/2): it predicts −1 where the true
  v₂(q_min) = 0.  It breaks exactly when the RHS would be < 0 — i.e. the VACUOUS regime where q_min is a
  2-adic unit; the correct statement is v₂(q_min) = max(0, 1 − min_j(C_j − N_j)).  This does NOT affect §6cd
  (Row 2: RHS = 1 − W_top ≈ 3m/2 ≫ 0, identity holds 25/25) but confirms the framework is meaningful only in
  the non-vacuous regime, reinforcing that §6cd is a Row-2 tool.  RH stays [OUT].

### §6cf — SYNTHESIS: the floor MECHANISM is dictated by the w-profile SHAPE at the working prime; the 4-row split IS the shape trichotomy governed by v₂(n)

  probe (EXACT, L9; wvec + vp_frac, m=6,8; verified for the orbits listed).  §6cd/§6ce prompt the unifying
  question — WHY does each row carry at the prime it does?  Answer: the whole family of results (§6bm/§6bi,
  §6cd, §6ao) is one principle — the FLOOR MECHANISM is fixed by the SHAPE of the profile v_p(w_i), i=0..m−1,
  of the fixed moment vector w = B⁻¹d at the working prime p.  Three shapes, three mechanisms:

     (a) STRICTLY DECREASING profile (min at the TOP index m−1, linearly negative).  Then min_p v_p(w_p)=W_top
         is deep-negative and the §6cd ultrametric on V·u=w gives v_p(q_min) ≥ 1−W_top directly.  CLEANEST —
         no C_j control, no minimax.  Occurs: p=2, n ODD (Row 2).  Measured v₂(w_i)=[−1,−1,−4,−5,−7,−7,−10,−11]
         (m=8), W_top≈−3m/2.

     (b) EXACTLY CONSTANT profile at height h≥4 (h even).  A flat profile PINS the bilinear pairing:
         C_j = ⟨w,ε(X'_j)⟩ has a UNIQUE ultrametric-min term (the anchored e_0=w_{m−1} product), so C_j = m+(h−1)
         NODE-INDEPENDENT (§6bi) and v_p(q_min)=1+3(m−1)−C_j = 2m−2−(h−1) linear.  Occurs: p=2, 4|n (Row 1).
         MEASURED LAW (exact, n=4,8,12,16): v₂(w_i) ≡ 2·v₂(n) constant, so h=2v₂(n), S:=h−1=2v₂(n)−1≥3 (§6bm).

     (c) CONSTANT profile at the S=1 BOUNDARY (height h=2), OR FLAT-AT-UNIT profile (height 0).  Here the
         ultrametric min TIES (two equal top terms at h=2, S=1) or there is no depth at all (unit), so C_j is
         NOT pinned — the adversary can 3-adically LIFT C_j to any depth (§6aw), and the floor survives only
         through the un-proved COMPETITION bound (4″) max_j(N_j−C_j)≥cm.  OPEN.  Occurs: p=2 n≡2 mod4 (height 2,
         S=1, MEASURED v₂(w_i)≡2 for n=2,10,14 — Row 3's p=2 is VACUOUS by the tie); and p=3 for Row 3
         (MEASURED v₃(w_i)≡0 flat-unit — no basis depth since B and 3∤D make w a 3-unit).

  GOVERNING PARAMETER (p=2): the shape is a clean trichotomy in v₂(n):
        v₂(n)=0 (n odd)      → DECREASING  → §6cd,  floor 3m/2−O(1)      [Row 2]
        v₂(n)≥2 (4|n)        → CONSTANT h=2v₂(n)≥4, S≥3 → §6bm/§6bi, floor 2m−2−S   [Row 1]
        v₂(n)=1 (n≡2 mod4)   → CONSTANT h=2, S=1, TIE → p=2 VACUOUS → must use p=3   [Row 3]
  So Rows 1 and 2 do NOT share one p=2 argument (Row 1 is CONSTANT-pinned, Row 2 is DECREASING-ultrametric);
  §6cd is genuinely the special DEEP-PROFILE row.  This corrects any instinct to merge them.

  WHY Rows 3,4 ARE OPEN (sharp): a DECREASING or CONSTANT-S≥2 profile can only come from B's 2-adic content
  (the offline d is 2-integral; only the Chebyshev basis B=4(1−T_j) carries 2-adic denominators).  For n≡2 mod4
  that content lands exactly at the S=1 tie, and at every ODD prime B is a unit ⇒ w is unit (flat-0) unless p
  RAMIFIES in the orbit.  Hence Rows 3,4 have NO shape-(a)/(b) prime available: they are forced onto shape (c),
  i.e. the node-clustering floor whose sole open core is the competition lemma (4″).  §6cd cannot help (it needs
  a negative profile min; Row 3's p=2 min is +2, p=3 min is 0).  This is the precise reason the barrier is only
  PARTIALLY proved: OP1 CLOSES for all n≢2 mod4 at p=2 (Row 1 §6bm proved; Row 2 §6cd candidate modulo the
  PROVED FACT A), and REMAINS OPEN for n≡2 mod4, pending (4″).  RH stays [OUT].

### §6cg — IMPOSSIBILITY: the moment-side ultrametric (the §6cd machinery) provably CANNOT yield the Row-3 floor; the open core is intrinsically determinantal (L5)

  A sharpening of §6cf shape (c), turning "§6cd cannot help" from an observation into a
  one-line THEOREM about the method, not just the instance.  Setup (all from §6bh, prime p=3):
  u = (Vᵀ)⁻¹w with V=(x_jᵖ) the node Vandermonde; the Cramer numerator D_j = det(V, col j←w),
  u_j = D_j/det V; and v₃(q_min) = −min_j v₃(u_j) = v₃(det V) − min_j v₃(D_j).  Row 3 (n≡2 mod4,
  3∤n) has w a 3-UNIT vector: v₃(w_p)=0 for every moment p (VERIFIED EXACT by the §6cf probe,
  "flat-unit height 0"; also confirmed here across n=10 × m=4,5,6).

  CLAIM.  Any argument that bounds v₃(q_min) from below using ONLY the linear/Lagrange relations
  Σ_j g(x_j) u_j = Λ(g) (g any poly deg ≤ m−1, Λ(zᵖ)=w_p) and the ultrametric is INCAPABLE of a
  positive floor for Row 3.
  PROOF.  Every accessible right-hand side Λ(g) is a Z₃-combination of the UNIT moments w_p, so
  v₃(Λ(g)) ≥ 0, with equality generically.  The ultrametric on Σ_j g(x_j) u_j = Λ(g) gives only
  min_j v₃(u_j) ≤ v₃(Λ(g)); the STRONGEST such bound (minimising over g) is min_j v₃(u_j) ≤ 0.
  Hence v₃(q_min) = −min_j v₃(u_j) ≥ 0 — the trivial bound.  No choice of g escapes v₃(Λ(g)) ≥ 0,
  because Λ maps 3-integral polynomials to Z₃-combinations of units. ∎

  So the Row-3 floor cannot be a valuation-TRANSFER statement; it must be the determinantal
  NON-ABSORPTION v₃(det V) − min_j v₃(D_j) > 0 — i.e. the gcd of the m Cramer numerators D_j fails
  to absorb the full lattice content v₃(det V) ≈ m²/4·(within-class pair density).  This is a
  Smith-normal-form / index statement about the augmented lattice [V | w], NOT an ultrametric one,
  and it re-derives from first principles the §6ah/§6ai conclusion ("the gcd cannot absorb the final
  linear piece") — now as a CLEAN impossibility for the entire moment-side toolkit, not an empirical
  wall.  CONSEQUENCE (L5): the competition lemma (4″) is correctly posed as a Smith/lattice problem;
  no refinement of §6cd/§6bh/Lagrange can shortcut it.  This is the precise reason to OUTSOURCE (4″)
  as a determinantal nugget rather than keep decomposing it valuation-wise.  RH stays [OUT].

### §6ch — the SINGLE-PRIME-CERTIFICATE BLIND SPOT: Row 3 splits by n mod 3; OP1 holds everywhere but is only single-prime-certifiable on half of it (L5, HONEST NEGATIVE)

  A direct-magnitude probe (qmin_exact_orbit over random on-line node sets; genuine Row-3 orbits
  n≡2 mod4, 3∤n) uncovers a dichotomy that CORRECTS the §6cf picture ("Rows 3,4 → the single lemma
  (4″)").  The nodes x_t=(4t²−1)/(4t²+1) are orbit-INDEPENDENT, so the clustering depth clus(j)=
  Σ_{k≠j} v₃(x_j−x_k) and max_j clus(j) are orbit-independent; but v₃(q_min) is orbit-dependent, and
  it splits SHARPLY by n mod 3:

    Row 3a  (n≡1 mod3; e.g. n=10, 22):  p=3 carries a LINEAR valuation floor.  Empirically
        v₃(q_min) = max_j clus(j) − C with a BOUNDED defect C≤3 up to m=12 (n=10: floor 4,6,8,10 at
        m=6,8,10,12; n=22: floor 3,4,5,5 at m=5..8).  Combined with the PROVABLE pigeonhole
        max_j clus(j) ≥ ⌈m/2⌉−1 (m nodes, only N(3)=2 residue classes mod 3 ⇒ some class has ≥m/2
        nodes ⇒ its members are pairwise 3-adically close), this is a CANDIDATE single-prime close
        of Row 3a — MODULO the bounded-defect lemma  v₃(q_min) ≥ max_j clus(j) − O(1)  (unproved; the
        determinantal statement min_j v₃(D_j) ≤ v₃(det V) − max_j clus(j) + O(1), i.e. replacing the
        deepest-clustered node's column by the unit w loses essentially all its clustering depth).

    Row 3b  (n≡2 mod3; e.g. n=14, 26):  NO small prime carries a linear floor.  Over 40 node sets,
        min v₂(q_min) stays O(1) (n=26: 1,1,1,2 at m=5..8), v₃(q_min)≈0–1 (FLAT, defect C grows ~m),
        and every other small prime shows only sporadic single-sample floors of 1 (noise, not
        structure).  YET the ACTUAL magnitude is still super-polynomial: log(min q_min) grows
        ~linearly-to-quadratically in m (n=26: 89,114,139,166,204,234 at m=5..10; control n=10:
        74…210) ≫ log m.  So OP1 HOLDS for Row 3b as well — but its content is DISTRIBUTED across
        many primes, with NO single prime carrying a certificate.  It is NOT archimedean either:
        |det V| < 1 since every node x_t ∈ (0,1), so the size lives entirely at finite primes.

  READING (L5, HONEST NEGATIVE).  OP1 appears TRUE for ALL orbits (verified: min q_min super-poly on
  both n mod 3 classes), but the SINGLE-PRIME valuation-floor STRATEGY — the entire §6bm/§6cd/§6cf/
  §6cg toolkit, which proves the barrier by exhibiting ONE prime with a v_p(q_min)=Ω(m) floor — has a
  genuine BLIND SPOT on Row 3b: no such prime exists there.  This RELOCATES the true OP1 frontier: it
  is not that OP1 fails anywhere, but that closing Row 3b needs a GLOBAL/distributed lower bound on
  log q_min = Σ_p v_p(q_min)·log p (the gcd of the m Cramer numerators D_j fails to absorb det V's
  finite content across ALL primes simultaneously) — neither a single-prime floor NOR an archimedean
  size bound.  Row 3a remains single-prime-certifiable (p=3, modulo the bounded-defect lemma).
  This SUPERSEDES the §6cf claim that all of Row 3 reduces to (4″): only Row 3a does; Row 3b is a
  distinct, harder, distributed-content problem.  RH stays [OUT].

### §6ci — the EXACT p=3 floor formula v₃(q_min) = max_j(clus(j) − v₃(S_j)), and the 3a/3b split pinned to the clustering-vs-pairing competition (L5)

  HONEST CREDIT (L5): the identity itself is the §6bh/§6bf identity v_p(q_min) = max_j(N_j − C_j)
  specialised to p=3, where N_j = v₃(P'(x_j)) = Σ_{k≠j} v₃(x_j−x_k) = clus(j) and C_j = v₃(S_j),
  with S_j = Σ_i (−1)^{m−1−i} e_{m−1−i}(X'_j) w_i the §6bf pairing (X'_j = nodes except j).  There is
  no "+1" offset here (that was the p=2 factor B=4(1−T); B is a 3-unit).  NEW here is (i) VERIFYING the
  identity holds EXACTLY at p=3 (720 orbit×node-set×m tests, 0 mismatches, incl. 3a, 3b, vacuous n=2),
  and (ii) the EXACT quantification of the §6ch dichotomy through v₃(S_j):

        v₃(q_min) = max_j ( clus(j) − v₃(S_j) )      [EXACT, determinant-free]

  clus(j) is ORBIT-INDEPENDENT with the provable pigeonhole max_j clus(j) ≥ ⌈m/2⌉−1 (2 classes mod 3).
  v₃(S_j) is orbit-dependent and is the SOLE discriminant:
    Row 3a (n≡1 mod3): SOME node has clus(j) linear AND v₃(S_j)=O(1) (probe: at the deepest node the
        min over node sets of v₃(S_j*) is 0; worst-case max_j(clus−v₃S) = 4,5,7 at m=6,8,10 — LINEAR,
        matching the §6ch measured v₃-floor exactly).  ⇒ the p=3 pairing is "generic" on a deep node.
    Row 3b (n≡2 mod3): EVERY node has v₃(S_j) ≥ clus(j) − O(1) (probe: v₃(S_j*) ≥ 3 always, worst-case
        max_j(clus−v₃S) = 0,1,2 — FLAT).  ⇒ the pairing ABSORBS the clustering; no p=3 floor (consistent
        with §6ch: Row 3b's super-poly q_min lives at distributed primes, not p=3).

  So the entire OP1-at-p=3 question — for ALL Row-3 orbits — is now the fully explicit competition
  "does some node carry clustering depth the pairing fails to absorb, max_j(clus(j) − v₃(S_j)) ≥ cm?"
  This is (4″) made determinant-free and exact, with n mod 3 identified as the governing residue: the
  open sub-problem is precisely WHY n≡1 mod3 leaves a deep node with v₃(S_j)=O(1) while n≡2 mod3 forces
  v₃(S_j) ≥ clus(j) − O(1) on every node (a mod-3 reduction of Λ(P_j) = S_j: P_j ≡ (z−a)^{α}(z−b)^{β}
  mod 3 for the two node-classes a,b, and whether the functional Λ (fixed by w mod 3) annihilates it to
  clustering depth).  Row 3a candidate-closes MODULO this; Row 3b needs the §6ch global argument instead.
  probe_qmin_p3_exact_floor.py backs this (exact identity + the v₃(S_j) discriminant).  RH stays [OUT].

### §6cj — the MECHANISM behind n mod 3: Λ_w has a deeply-3-annihilated node-residue class iff n≡2 mod3; reduces Row 3a to a clean m-independent Λ-lemma (L5)

  Since S_j = Λ(P_j) with Λ(z^i)=w_i and P_j(z)=Π_{k≠j}(z−x_k), at the deepest node j* (in the larger
  3-adic class, size ≥⌈m/2⌉ by pigeonhole) P_{j*} ≡ (z−a)^{s−1}·(z−b)^{m−s} mod 3, where a,b are the two
  ORBIT-INDEPENDENT node residues mod 3.  The nodes x_t=(4t²−1)/(4t²+1) split into exactly two classes:
  a₀ ≡ 0 mod 3 (t≡1,2 mod 3) and a₂ ≡ 2 mod 3 (t≡0 mod 3).  So v₃(S_{j*}) is governed by the VANISHING
  ORDER of the functional Λ on (z−a)^t.  Measured law (max_{t≤m−1} v₃(Λ((z−a)^t)), 8 distinct n, m=10,14):

        n≡1 mod3 (n=10,22,34,46,58):  a₀-class → 0 ;  a₂-class → 2–3     (BOTH O(1), m-independent)
        n≡2 mod3 (n=14,26,38):        a₀-class → GROWS ~linearly in m (10→15, 20→29) ;  a₂-class → 0

  So Λ_w has a DEEPLY-3-ANNIHILATED residue class IFF n≡2 mod3, and it is the a₀ (x≡0) class.  This is
  the exact mechanism of §6ch/§6ci:
    • Row 3a (n≡1 mod3): NEITHER class is deeply annihilated ⇒ v₃(S_j)=O(1) for the deep node ⇒
      v₃(q_min) = max_j clus(j) − O(1) ≥ ⌈m/2⌉−1 − O(1).  LINEAR ⇒ OP1 CLOSES at p=3.
    • Row 3b (n≡2 mod3): the adversary clusters nodes in the annihilated a₀ class ⇒ v₃(S_j) ≥ clus(j)−O(1)
      ⇒ margin O(1) ⇒ no p=3 floor (its super-poly q_min lives at distributed primes, §6ch).

  NET (the sharpest OP1 statement to date):  OP1 closes at p=3 for Row 3a MODULO the clean, m-independent
  Λ-LEMMA:  "for n≡1 mod3, max_t v₃(Λ_w((z−a)^t)) = O(1) uniformly in t and m for both node residues
  a∈{a₀,a₂}."  This is a statement about w mod 3 alone (w=B⁻¹d, B the Chebyshev-basis matrix) — a bounded,
  concrete, likely-provable target, NOT the intractable raw (4″).  It is the natural EXT/next-proof nugget
  for Row 3a; Row 3b remains the harder distributed-content problem (§6ch).
  probe_qmin_p3_lambda_annihilation.py backs the annihilation law.  RH stays [OUT].

### §6ck — the ROOT CAUSE: the w mod 3 dichotomy (period-4 units vs w_0-only); Row 3a p=3 close now rests on one provable moment-residue fact (L5)

  The §6cj Λ-lemma reduces further to the residue of the moment vector w=B⁻¹d itself mod 3.  VERIFIED
  EXACT across 9 distinct Row-3 orbits n × m∈{8,12,16}:

    FACT 3a  (n≡1 mod3):  every w_i is a 3-UNIT, and the unit residues are the PERIOD-4 pattern
        [1,1,2,2,1,1,2,2,…].  Hence W(y)=Σ w_i y^i ≡ (1+y)(1+2y²)·(1+y⁴+…) mod 3 is a unit-coefficient
        (w_0=1) polynomial: via F(s)=Σ_t Λ((z−a)^t)s^t = W(s/(1+sa))/(1+sa), the vanishing order of Λ on
        (z−a)^t equals the root multiplicity of W mod 3 at a's Möbius image — bounded (≤3 observed; at
        worst O(log₃ m) from the (y⁴−1)^{v₃(m/4)} factor, SUBLINEAR).  So for BOTH node residues
        v₃(Λ((z−a)^t)) = o(m), giving v₃(q_min) = max_j clus(j) − o(m) ≥ ⌈m/2⌉−1 − o(m) — LINEAR.

    FACT 3b  (n≡2 mod3):  w_0 is a unit but w_i ≡ 0 mod 3 for EVERY i≥1 (measured v₃ = 0,1,3,3,4,5,7,7…).
        Hence Λ(f) ≡ w_0·f(0) mod 3 exactly, so Λ((z−a)^t) ≡ w_0(−a)^t mod 3: this ANNIHILATES the a₀≡0
        class (order grows ~t·v₃(a₀), deep) and is a unit on the a₂≡2 class.  Adversary clusters in a₀ ⇒
        no p=3 floor — precisely the §6ch/§6cj Row-3b behaviour, now DERIVED not observed.

  NET.  The entire Row-3 OP1 behaviour at p=3 is explained by ONE moment-residue dichotomy: n mod 3
  controls whether w mod 3 is a full-support period-4 unit vector (3a: no annihilated class ⇒ LINEAR
  floor) or a w_0-only vector (3b: Λ=eval₀ mod 3 ⇒ a₀ annihilated ⇒ no floor).  Row 3a p=3 CLOSES modulo
  the single PROVABLE fact FACT 3a (the period-4 unit pattern of w=B⁻¹d mod 3, matching the period-4
  structure already proven at p=2 in FACT A §6br).  Row 3b's super-poly q_min genuinely lives at
  distributed primes (§6ch), not p=3 — a distinct, harder problem.  probe_qmin_p3_wmod3_dichotomy.py
  verifies both facts EXACT.  This is the cleanest and deepest OP1 partial-barrier result to date.
  RH stays [OUT].

### §6cl — CORRECTION + analytic backbone: the classifier is e₂ mod 3 (⟺ 3|(a+n)), NOT n mod 3; FACT 3a/3b reduce to a finite F₃ recurrence (L9, L5)

  §6ck's "n mod 3" classifier is REFUTED (L9): it was an artifact of only sampling a=1 (with the lone
  n=10 case at a=3 happening to agree).  Varying a=n·sig exposes the true invariant.  Two witnesses that
  break n mod 3: n=22,a=5 (n≡1 mod3) is ANNIHILATED (not all-units); n=14,a=3 and n=26,a=5 (n≡2 mod3) are
  ALL-UNITS (not annihilated).  probe_qmin_p3_fact3a_recurrence.py.

  ANALYTIC BACKBONE (all exact).  For the off-line orbit ρ = (a+ni)/n (τ=1, 3∤n), the d-vector reduces to
  a palindromic-quartic power sum:
    (A) [PROVED, exact m≤8 all orbits]  d_j = 8 − 2 p_j,  where p_j = β^j+β̄^j+β^{−j}+β̄^{−j}, β = 1−1/ρ.
        The 4 atoms of d_vec give β-values {β, β̄, 1/β, 1/β̄}, closed under conjugation AND inversion, so
        they are the roots of the PALINDROMIC REAL quartic x⁴ − e₁x³ + e₂x² − e₁x + 1 = (x²−gx+1)(x²−ḡx+1),
        g = β+1/β = (2ρ²−2ρ+1)/(ρ²−ρ).  Hence e₁ = g+ḡ = 2Re g,  e₂ = |g|² + 2,  and
            p_j = e₁ p_{j−1} − e₂ p_{j−2} + e₁ p_{j−3} − p_{j−4},   p₀=4, p₁=e₁, p₂=e₁²−2e₂, p₃=e₁³−3e₁e₂+3e₁.
    (B) [closed form, EXHAUSTIVE over all 6 residues (a mod3, n mod3), 3∤n]:
            e₁ ≡ 0 mod 3  ALWAYS;   e₂ ≡ 2 mod 3 ⟺ 3 | (a+n)  (else e₂ ≡ 0).
        Equivalently e₂≡2 ⟺ 3 | N(g) ⟺ the inert prime 3 divides g=β+1/β in ℚ(i) — an orbit-intrinsic
        statement.  [Denominators (a²+n²), (a−n)²+n² are 3-units for every 3∤n, since −1 is a non-residue
        mod 3, so e₁,e₂ are always 3-integral.]
    (C) Since e₁≡0 mod 3, the mod-3 recurrence DECOUPLES to  p_j ≡ −e₂ p_{j−2} − p_{j−4} mod 3, with
        p₀≡1, p₁≡0, p₂≡e₂, p₃≡0 ⇒ all ODD p_j ≡ 0 (so d_j ≡ 2 for odd j).  Two even-index regimes:
          ε := e₂ mod 3 = 0  (3∤(a+n)):  p_{even}: 1,0,2,0,1,0,2,… ⇒ d mod3 period-8 [2,2,2,1,2,2,2,0];
             B⁻¹ gives w mod 3 = the PERIOD-4 unit vector [1,1,2,2,…] (verified to m=16).  As a series
             W(y) ≡ (1+y)/(1+y²) mod 3, and 1+y² is IRREDUCIBLE mod 3 (2 is a non-residue) ⇒ bounded root
             multiplicity ⇒ v₃(Λ((z−a)^t)) = O(1) for both node residues ⇒ v₃(S_j)=o(m) ⇒ LINEAR floor.
          ε = 2  (3|(a+n)):  p_{even}: 1,2,1,2,… ⇒ d mod3 period-4 [2,1,2,0]; B⁻¹ gives w mod 3 = [1,0,0,…]
             (w₀ unit, w_i≡0 mod3 ∀i≥1, verified to m=16) ⇒ Λ ≡ w₀·eval₀ mod 3 ⇒ a₀≡0 class annihilated ⇒
             NO p=3 floor (the distributed-content case).
        B mod 3 is a UNIVERSAL orbit-independent lower-triangular matrix (rows i≡2 mod3 are constant, diagonal
        period-2 [2,1]); its periodic band structure is what makes the w-pattern m-independent.

  NET (corrected).  The p=3 dichotomy is governed by ONE F₃ quantity — e₂ mod 3 = |g|²+2, i.e. whether the
  inert prime 3 divides the Joukowski trace g = β+1/β (⟺ 3|(a+n)).  The p=3 LINEAR floor holds for the
  sub-family 3∤(a+n) (v₃(q_min) ≥ ⌈m/2⌉−1 − o(m)); the sub-family 3|(a+n) has no p=3 floor and its super-poly
  q_min is distributed (§6ch).  This SUPERSEDES §6ck's n-mod-3 split and turns the "FACT 3a" close into a
  FINITE, provable F₃ statement: (A) palindromic-quartic reduction [proved], (B) 6-residue closed form for
  (e₁,e₂) mod 3 [proved], (C) universal B mod 3 + periodic d ⇒ the two w-patterns [finite F₃ linear algebra;
  the sole remaining write-up is m-independence of B⁻¹ mod 3 on the periodic d].  probe_qmin_p3_fact3a_
  recurrence.py verifies (0)/(1)/(1b)/(2) EXACT.  RH stays [OUT].

### §6cm — Row-3a p=3 LINEAR FLOOR: (C) upgraded to an exact identity, F(s) closed forms, and the floor is v₃(q_min)=m−3 (L9, L5)

  Closes the §6cl item (C) write-up gap and assembles the full chain, with one honesty correction of a
  §6cm-internal over-claim.  probe_qmin_p3_floor_theorem.py verifies everything below EXACT.

  (C) UPGRADED from "verified to m=16" to a RATIONAL-FUNCTION IDENTITY mod 3 (all m at once).  Since B is
      lower-triangular with 3-unit diagonal, B w = d has a UNIQUE mod-3 solution, so it suffices to show the
      claimed closed-form W reproduces d.  With the moment map Λ_x[1/(1−u x)] = W(u) applied to the Chebyshev
      generating function G(x,s) = Σ_{i≥1} 4 q_i(x) s^i = (4/(x−1))[ s/(1−s) − s(x−s)/(1−2sx+s²) ], set
      D_w(s) := Λ_x G(x,s) (partial-fraction in x, evaluate W at the Möbius images).  Against the proven
      D(s) := Σ_{i≥1} d_i s^i = 8s/(1−s) − 2(P(s)−4), P(s)=4 − sQ*'/Q*, Q* = 1 − e₁s + e₂s² − e₁s³ + s⁴:
          ε=0 (3∤(a+n)):  D_w[ (1+u)/(1+u²) ] ≡ D[e₁=0,e₂=0]  mod 3   → W(y) ≡ (1+y)/(1+y²) mod 3, all m.
          ε=2 (3|(a+n)):  D_w[ 1 ]            ≡ D[e₁=0,e₂=2]  mod 3   → W(y) ≡ 1          mod 3, all m.
      (numerator of the difference is 3-divisible as a polynomial in s — an exact proof for every m).  [PROVED]

  (D) F(s) := Σ_t Λ((z−a)^t) s^t = W(s/(1+sa))/(1+sa).  Substituting the ε=0 W and reducing mod 3:
          F(s) ≡ (1 + (a+1)s) / (1 + 2a s + (a²+1)s²)   mod 3,
      whose denominator discriminant is (2a)²−4(a²+1) = −4 ≡ 2 mod 3, a NON-RESIDUE ⇒ the denominator is
      IRREDUCIBLE over F₃ ⇒ the sequence Λ((z−a)^t) mod 3 is purely periodic and NEVER eventually zero.  In
      particular the node class a₀≡0 has F(s)=(1+s)/(1+s²) (coeffs period-4 [1,1,2,2], no zeros) — never
      annihilated; a₂≡2 has only bounded (periodic) vanishing.  ε=2: W≡1 ⇒ F(s)=1/(1+as) ⇒ Λ((z−a)^t)≡(−a)^t,
      so a₀≡0 gives (−0)^t=0 (t≥1) — DEEP annihilation (measured v₃ climbs 22–24 by t≤22), the no-floor case.
      [PROVED; matches Λ((z−a)^t) mod 3 for both regimes, all tested orbits.]

  FLOOR (v₃(q_min) = max_j ( clus(j) − v₃(S_j) ), S_j = Λ(P_j), clus(j)=v₃(P′(x_j))).  HONESTY (L5): the
  earlier §6cm-draft claim "v₃(S_{j*})=0 at the GLOBAL-max-cluster node" is REFUTED — at m=15 that node's
  v₃(S) climbs to 1..3.  The CORRECT exact statement (m≤18, all five ε=0 orbits, uniform):
      the ARGMAX of (clus − v₃S) is ALWAYS a node with v₃(S_j)=0 (a 3-UNIT), and
          v₃(q_min) = m − 3   (6,9,12,15 for m=9,12,15,18; floor/m → 1) — LINEAR in m,
  far above the ⌈m/2⌉−1 first guess.  ⇒ log q_min = Ω(m) = ω(log m) at the SINGLE prime p=3 ⇒ the OP1
  super-poly barrier CLOSES for the ε=0 (3∤(a+n)) sub-family.  The ε=2 (3|(a+n)) sub-family has no single
  p=3 floor (a₀ annihilated) and lives at distributed primes (§6ch).

  NET.  (A) [proved exact] + (B) [proved, 6-residue] + (C) [proved, rational-function identity mod 3] + (D)
  [proved] give a symbolic-exact mod-3 backbone; the ε=0 floor v₃(q_min)=m−3 is EXACT to m=18.  CLUSTER SIDE
  now PROVEN: since x_j−x_k = 8(j−k)(j+k)/[(4j²+1)(4k²+1)] with 3-unit denominators (4t²+1 ≡ t²+1 ∈ {1,2}
  mod 3, never 0),  clus(j) = Σ_{k≠j}[ v₃(j−k) + v₃(j+k) ]  (verified exact m≤24), and for any central j,
  Σ_{k≠j} v₃(j−k) = Σ_{i≥1} #{k: 3ⁱ|(j−k)} ≈ Σ m/3ⁱ = m/2, giving max_j clus(j) ≥ ~m/2 = Θ(m) rigorously
  (measured max/m → 0.9).  The sole remaining rigor is the COUPLING lemma — "the argmax of clus(j)−v₃(S_j)
  lands on a node with v₃(S_j)=0 (a 3-unit) whose clus(j) ≥ c·m" (strongly evidenced, c→1; floor = m−3) —
  after which Row-3a p=3 is a THEOREM closing OP1 for 3∤(a+n).  probe_qmin_p3_floor_theorem.py.  RH [OUT].

### §6cn — MULTI-PRIME extension + adversarial node-set robustness (evidence for OP1 infimum) (L9, L5)

  §6cm closes only 3∤(a+n); OP1's infimum is controlled by 3|(a+n).  Three exact findings (probe_qmin_p3_
  multiprime_adversary.py):
  (1) GENERAL prime classifier.  The §6cl palindromic-quartic reduction holds at every prime p∤n; the p-floor
      is non-degenerate iff 1+e₂s²+s⁴ stays separable mod p, i.e. e₂ ≢ ±2 mod p (⟺ e₂²−4 ≢ 0).  e₂=|g|²+2 is a
      FIXED rational per orbit ⇒ only FINITELY many degenerate primes ⇒ every orbit is non-degenerate at all but
      finitely many p — a MULTI-PRIME route to a uniform floor.  (p=3 is the e₂≡±2 special case: e₂≡2 ⟺ 3|(a+n).)
  (2) FACTORIZATION of q_min at consecutive nodes t=1..m confirms 3|(a+n) orbits still have log q_min=Ω(m),
      carried by large orbit-specific primes (n=14,a=1: 73,197^~m; n=22,a=5: 509,773^~m) plus v₂~m — NOT p=3.
  (3) ADVERSARIAL trend: minimizing log₂q_min over random node sets gives values LARGER than the consecutive
      set t=1..m (m=6,8: consec 102,146 vs random-min 129,209 for 3∤; 118,167 vs 159,225 for 3|).  So consecutive
      is near the minimizer and is already LINEAR (~20–28/node) for BOTH regimes; spreading nodes only raises
      q_min (can't dodge clustering at every prime — the §6ch distributed-pigeonhole intuition).
  SCOPE (L5): EVIDENCE, not proof, for the OP1 infimum.  "min over random sets" ≠ true infimum over structured
  node sets; §6cm's exact floor is for consecutive nodes only.  Clean open lemma to CLOSE OP1: "for EVERY node
  set, some prime p has v_p(q_min) ≥ c·m" (distributed, §6ch); §6cm (p=3, 3∤(a+n)) is its proved single-prime
  instance.  RH stays [OUT].

### §6co — COUPLING LEMMA PROVED ⇒ §6cm is a THEOREM (ε=0, consecutive nodes): v₃(q_min) ≥ m/2 − O(1) (L9)

  The last §6cm gap (the coupling "argmax lands on a 3-unit node with clus ≥ c·m") is now CLOSED.
  Ingredients (all exact, probe_qmin_p3_coupling_lemma.py):
  * Λ-STRUCTURE.  The ε=0 moments are w_l ≡ [1,1,2,2] period-4 mod 3, so w_l + w_{l−2} ≡ 0 (l≥2), i.e. Λ
    ANNIHILATES the ideal (z²+1) mod 3.  Hence Λ FACTORS THROUGH F₃[z]/(z²+1) ≅ F₉ = F₃[i] via z ↦ i
    (i²=−1; z²+1 irreducible since −4 ≡ 2 is a non-residue), and with Λ(1)=Λ(z)=1 the induced functional is
        Λ(a + b i) = a + b.
  * NODE RESIDUES.  x_t ≡ 0 (t≢0 mod3, class a₀) or ≡ 2 (t≡0 mod3, class a₂).  For node j, P_j ≡ z^{n₀}(z−2)^{n₂}
    mod 3 with n₀+n₂=m−1, so S_j = Λ(P_j) ↦ i^{n₀}(i−2)^{n₂} = i^{n₀}(i+1)^{n₂} in F₉ (−2 ≡ 1).
  * COUPLING.  (i+1)² = 2i ≡ −i mod 3, so for n₂ = 2c EVEN:  S_j ↦ (−1)^c i^{n₀+c} ∈ {±1,±i} ⇒ a+b = ±1 ≠ 0
    ⇒ S_j is a 3-UNIT.  (n₂ odd may annihilate — irrelevant.)  The n₂-even class is always nonempty
    (n₂ ∈ {⌊m/3⌋, ⌊m/3⌋−1}, one is even).
  * FLOOR.  clus(j) = Σ_{k≠j}[v₃(j−k)+v₃(j+k)] ≥ Σ_{k≠j} v₃(j−k) = Σ_{i≥1} #{k: 3ⁱ|(j−k)} ≥ ~m/2 for EVERY j.
  ⇒ ∃ node j with v₃(S_j)=0 AND clus(j) ≥ ~m/2  ⇒  v₃(q_min) = max_j(clus(j)−v₃(S_j)) ≥ m/2 − O(1).

  THEOREM (ε=0, i.e. 3∤(a+n), consecutive nodes t=1..m): v₃(q_min) ≥ m/2 − O(1) at the single prime p=3, so
  log q_min = Ω(m) = ω(log m) — a RIGOROUS single-prime super-poly lower bound.  This is the fully proved
  single-prime instance of OP1; the remaining OP1 content is 3|(a+n) and general (adversarial) node sets (§6cn).
  RH stays [OUT].

### §6cp — NO universal single small prime; but log q_min = Ω(m) holds by AGGREGATE (probe_qmin_p2_not_universal.py, L9)

  Two complementary findings on the way to the full OP1 (all orbits, all node sets):

  (i) p=2 floor is ORBIT-INDEPENDENT & LINEAR — but NOT universal.  v₂(q_min)=max_j(1+N_j−C_j) with
      N_j≥3(m−1) unconditional (denominators 4t²+1 odd ⇒ v₂(x_j−x_k)≥3).  For n∈{10,14,22} — covering BOTH
      3∤(a+n) and 3|(a+n) — the floor is IDENTICAL 5,11,16,23 (m=8,12,16,20), floor/m→~1.15.  So p=2 catches
      many 3|(a+n) orbits that p=3 (§6co) misses.  BUT n=50 (a=1; a+n=51 ⇒ 3|(a+n)) ESCAPES: C_j=v₂(S_j)
      grows fast enough to cancel N_j, giving floor 0,1,2,4 only.  n=50 thus escapes BOTH p=2 (weak) and p=3
      (degenerate).  ⇒ NO single small prime gives a uniform linear floor for ALL Row-3 orbits.

  (ii) DECISIVE AGGREGATE TEST.  The OP1 quantity is log q_min = Σ_p v_p(q_min)·log p, not any one prime.
      For the EXACT integer q_min of the doubly-degenerate n=50: log₂(q_min)/m ≈ 23.2, 24.3, 24.4, 25.2, 25.6
      at m=6,8,10,12,14 — LINEAR and INCREASING.  So log q_min = Ω(m) HOLDS for n=50 anyway, carried by its
      large orbit-specific primes (§6cn factorization).  The barrier SURVIVES the worst small-prime orbit via
      DISTRIBUTION across primes; the single-prime floors (§6co p=3, §6cp(i) p=2) are constructive but
      non-universal witnesses.

  READING (L5): the linear-log lower bound appears UNIVERSAL over orbits (consecutive nodes); closing OP1 fully
  needs the AGGREGATE statement "log q_min = Ω(m) for every orbit" plus the node-set infimum (adversarial,
  §6cn shows consecutive is near-minimal — evidence, not proof).  RH stays [OUT].

## 4. Honesty / scope

  * RH stays [OUT].  Everything here is finite exact-arithmetic about explicit
    multisets; nothing assumes or implies RH.
  * PROVED (per-family): the off-line-multiplicity floor (Theorem in §1).
  * PROVED (UNIFORM over all on-line node sets, for an explicit infinite off-line
    sub-family): the inert-prime exponential floor (Theorem in §5).  This is the
    first result covering the "over ALL on-line constructions" quantifier -- but
    only for off-line orbits with an inert (p==3 mod4) prime in den(u_0).
  * PROVED (UNIFORM over all on-line node sets AND all off-line orbits, NUMERATOR
    only): the determinantal rank-count floor v_p(D_m(A)) >= m - (p+3)/2 for every
    inert p == 3 mod4 (§6c).  This covers the split-only orbits (D=425) that §5/§6b
    could not touch -- but bounds only the numerator of q_min = D_m(A)/D_m([A|d]).
  * OPEN: full OP1 = the uniform bound for the REMAINING off-line orbits (u_0
    denominator all split/2).  §6c localized the gap to a linear lower bound on the
    TOP Smith invariant e_max; §6d then supplies it: pigeonhole (m nodes into
    (p+3)/2 x-classes) + confluent-Vandermonde staircase + the off-by-one basis shift
    v_p(D_r(A))=v_p(D_{r-1}(V_x)) give e_max >= ceil(2m/(p+3)) - O(1), a RIGOROUS
    LINEAR floor VERIFIED as the tight adversary optimum (spread e_max == PH for
    p=7,11).  The determinantal/Vandermonde side is thus essentially closed.  The ONE
    surviving point: the off-line d is FIXED, so proving v_p(q_min) >= e_max - O(1)
    needs a uniform "d-bar meets the top cyclic factor of Z^m/L" argument (evidence:
    v_p(q_min)=e_max generically, lag <=1).  Pending: (i) source-verify the classical
    confluent-Vandermonde Smith staircase; (ii) the off-by-one row lemma; (iii) the
    fixed-vector incidence.  Alternatively the lambda_1 route of §2.
  * All numbers are DISCOVERY tier; the Theorem in §1 is stated for eventual
    promotion but is NOT yet a certified proof/ item.
