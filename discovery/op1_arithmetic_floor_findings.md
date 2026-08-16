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
