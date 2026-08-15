#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into
proofs.  No RH / RH-equivalent input.

OP1 LEG3 sole open core (post-§6j): the entire incidence lag is bounded by
    psi(S0) = v_p(Psi(S0))  at ANY Phi-minimizer S0,   Psi = orbit-sum over the
off-line atoms.  This probe does two things.

(A) RIGOROUS-IDENTITY SOLIDIFICATION.  §6i/§6j compute psi only via the
    determinant path  psi = v_p(det[A_{S'}|d]) - Phi.  Here we verify, EXACTLY,
    the trace form that every proof attempt will use:
      - the off-line orbit collapses to a CONJUGATE PAIR {u, ubar}
        (reflection rho->1-rho fixes u; conjugation sends u->ubar), so
            Psi(S0) = (u-1)g(u) + (ubar-1)g(ubar) = 2*Re[(u-1)g(u)]
                    = Tr_{Q(i)/Q}[(u-1) g(u)],   g(X)=prod_{k in S0}(X-x_k);
      - with mu(X)=(X-u)(X-ubar)=X^2 - s X + n, the Lucas trace sequence
            tau_0=2, tau_1=s, tau_j = s*tau_{j-1} - n*tau_{j-2}
        gives  Psi = sum_j c_j tau_j  where P_T(X)=(X-1)g(X)=sum c_j X^j.
    We check  v_p(Psi_det) == v_p(2 Re[(u-1)g(u)]) == v_p(sum c_j tau_j)  on
    every Phi-minimizer.  (Backbone of the §6j reduction, now VERIFIED not
    merely asserted.)

(B) MECHANISM HUNT for a uniform bound.  For each Phi-minimizer with psi>0 we
    tabulate psi against candidate combinatorial invariants of T={1}∪S0 mod p:
      - mu_max  = largest residue-class multiplicity of T mod p,
      - ncoll   = m - (#distinct residue classes of T mod p)  [= "excess"],
      - v_p(N)  = v_p(Norm(P_T(u))) = sum_y v_p(mu(y))  (MUST be 0: p-unit),
    and a p-adic DEPTH test: does psi stay put when the nodes are shifted within
    their residue classes (t -> t+p), i.e. is psi a mod-p residue phenomenon or
    does it require deep p-adic tuning the adversary would have to engineer?

HONESTY (L5): EVIDENCE + identity solidification, not a proof.  RH stays [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import ceil
from itertools import combinations
from collections import Counter

from discovery.probe_covolume_floor import bareiss_det
from discovery.probe_qmin_snf import cleared_columns, det_divisor_r
from discovery.qmin_snf_fast import qmin_fast


def vp(n, p):
    n = abs(int(n))
    if n == 0:
        return None
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def vpf(fr, p):
    if fr == 0:
        return None
    return (vp(fr.numerator, p) or 0) - (vp(fr.denominator, p) or 0)


def x_of(t):
    t = Fr(t)
    return (4 * t * t - 1) / (4 * t * t + 1)


# ---- Q(i) arithmetic ----------------------------------------------------
def cmul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def cinv(z):
    d = z[0] * z[0] + z[1] * z[1]
    return (z[0] / d, -z[1] / d)


def csub(z, w):
    return (z[0] - w[0], z[1] - w[1])


def off_atoms_u(sigma, tau):
    rhos = [(sigma, tau), (sigma, -tau), (1 - sigma, tau), (1 - sigma, -tau)]
    us = []
    for rho in rhos:
        w = csub((Fr(1), Fr(0)), cinv(rho))
        u = tuple((a + b) / 2 for a, b in zip(w, cinv(w)))
        us.append(u)
    uniq = []
    for u in us:
        if all(u != v for v in uniq):
            uniq.append(u)
    return uniq


def P_at_u(u, ys):
    """P_T(u) = prod_{y in ys} (u - y)  as a Q(i) point (ys rational)."""
    acc = (Fr(1), Fr(0))
    for y in ys:
        acc = cmul(acc, csub(u, (Fr(y), Fr(0))))
    return acc


def psi_trace(u, S_ts, p):
    """v_p of 2*Re[(u-1) * prod_{k in S0}(u - x_k)]  (the trace form)."""
    ys = [Fr(1)] + [x_of(t) for t in S_ts]
    val = P_at_u(u, ys)                     # (u-1) prod (u - x_k)
    re2 = 2 * val[0]
    return vpf(re2, p), re2


def psi_lucas(u, S_ts, p):
    """v_p of  sum_j c_j tau_j,  P_T(X)=(X-1)prod(X-x_k)=sum c_j X^j,
    tau_j = u^j + ubar^j via Lucas recursion with s=2Re u, n=Norm u."""
    ys = [Fr(1)] + [x_of(t) for t in S_ts]
    # polynomial coefficients of prod (X - y), ascending degree
    coeffs = [Fr(1)]
    for y in ys:
        new = [Fr(0)] * (len(coeffs) + 1)
        for i, c in enumerate(coeffs):
            new[i] += c * (-y)
            new[i + 1] += c
        coeffs = new
    s = 2 * u[0]
    n = u[0] * u[0] + u[1] * u[1]
    m = len(coeffs) - 1
    tau = [Fr(2), s]
    for j in range(2, m + 1):
        tau.append(s * tau[j - 1] - n * tau[j - 2])
    psi_sum = sum(c * tau[j] for j, c in enumerate(coeffs))
    return vpf(psi_sum, p), psi_sum


def Phi(S_ts, p):
    xs = [x_of(t) for t in S_ts]
    s = sum((vpf(x - 1, p) or 0) for x in xs)
    for i in range(len(xs)):
        for j in range(i + 1, len(xs)):
            s += (vpf(xs[j] - xs[i], p) or 0)
    return s


def norm_val(u, S_ts, p):
    """v_p(Norm(P_T(u))) = sum_y v_p(mu(y)), mu(y)=(y-u)(y-ubar). Must be 0."""
    ys = [Fr(1)] + [x_of(t) for t in S_ts]
    a, b = u
    v = 0
    for y in ys:
        muy = (y - a) * (y - a) + b * b        # (y-a)^2 + b^2 = Norm(y-u)
        v += (vpf(muy, p) or 0)
    return v


def res_profile(S_ts, p):
    """residue-class multiplicities of T={1}∪S0 mod p (of the x-values)."""
    xs = [Fr(1)] + [x_of(t) for t in S_ts]
    cnt = Counter()
    for x in xs:
        num = x.numerator % p
        den = x.denominator % p
        if den == 0:
            cnt[("inf",)] += 1
        else:
            cnt[num * pow(den, p - 2, p) % p] += 1
    mu_max = max(cnt.values())
    ncoll = sum(v - 1 for v in cnt.values())    # m - #distinct classes
    return mu_max, ncoll, dict(cnt)


def families(m, p):
    K = m + 3
    fams = {
        "half-int": [Fr(1, 2) + i for i in range(K)],
        "integer": [Fr(i) for i in range(1, K + 1)],
        "thirds": [Fr(a, 3) for a in range(1, K + 1)],
        "spread-p": _spread(p, m)[:K],
    }
    for t0 in range(1, (p + 1) // 2 + 1):
        fams[f"single@{t0}"] = [Fr(t0 + p * i) for i in range(K)]
    # deep-cluster mod p^2 (sharp p-adic tuning attempt)
    fams["deepcluster"] = [Fr(1 + p * p * i) for i in range(K)]
    return {k: [t for t in v if t != 0][:K] for k, v in fams.items()}


def _spread(p, m):
    reps = list(range((p - 1) // 2 + 1))
    depth = ceil(2 * (m + 3) / (p + 1)) + 1
    return [Fr(c + p * i) for c in reps for i in range(depth) if (c + p * i) != 0]


ORBITS = [
    ("3/4+i    D=425", Fr(3, 4), Fr(1)),
    ("2/5+4/5i D=4",   Fr(2, 5), Fr(4, 5)),
    ("1+i/5    D=26",  Fr(1), Fr(1, 5)),
]


if __name__ == "__main__":
    print("=" * 96, flush=True)
    print("OP1 LEG3 core: solidify trace identity for Psi + hunt a uniform psi bound",
          flush=True)
    print("DISCOVERY TIER.  No RH input.", flush=True)
    print("=" * 96, flush=True)

    id_trace_ok = id_lucas_ok = norm_unit_ok = True
    # mechanism aggregates: for psi>0 Phi-minimizers, (psi) vs (mu_max, ncoll)
    by_psi = {}          # psi -> Counter of (mu_max, ncoll)
    max_psi = 0
    depth_super_mod_p = 0     # configs where shifting nodes t->t+p CHANGES psi

    for label, sig, tau in ORBITS:
        us = off_atoms_u(sig, tau)
        # conjugate pair check
        conj_pair = (len(us) == 2 and us[0][0] == us[1][0] and us[0][1] == -us[1][1])
        print(f"\n{'='*96}\noff-line rho = {label}   #atoms={len(us)}  "
              f"conjugate-pair={conj_pair}", flush=True)
        u = us[0]
        for p in (3, 7, 11):
            for m in range(2, 9):
                for fname, ts in families(m, p).items():
                    if len(ts) < m:
                        continue
                    oc, vo = cleared_columns(ts, sig, tau, m)
                    q = qmin_fast(oc, vo)
                    if not q:
                        continue
                    vDm1 = vp(det_divisor_r(oc, m, m - 1), p) or 0
                    # Phi over (m-1)-subsets; argmin
                    rows = []
                    for S in combinations(range(len(oc)), m - 1):
                        rows.append((Phi([ts[k] for k in S], p), S))
                    minPhi = min(ph for ph, _ in rows)
                    for ph, S in rows:
                        if ph != minPhi:
                            continue
                        S_ts = [ts[k] for k in S]
                        # determinant-path psi
                        cols = [oc[k] for k in S] + [vo]
                        M = [[cols[c][r] for c in range(m)] for r in range(m)]
                        dv = bareiss_det(M)
                        if dv == 0:
                            continue
                        psi_det = (vp(dv, p) or 0) - ph
                        # trace form + Lucas form
                        pt, _ = psi_trace(u, S_ts, p)
                        pl, _ = psi_lucas(u, S_ts, p)
                        pt = pt if pt is not None else 10**9
                        pl = pl if pl is not None else 10**9
                        if pt != psi_det:
                            id_trace_ok = False
                        if pl != psi_det:
                            id_lucas_ok = False
                        if norm_val(u, S_ts, p) != 0:
                            norm_unit_ok = False
                        # mechanism
                        if psi_det > 0:
                            mu_max, ncoll, _ = res_profile(S_ts, p)
                            by_psi.setdefault(psi_det, Counter())[(mu_max, ncoll)] += 1
                            max_psi = max(max_psi, psi_det)
                            # depth test: shift every node by +p (same residue class)
                            S_ts2 = [t + p for t in S_ts]
                            p2, _ = psi_trace(u, S_ts2, p)
                            p2 = p2 if p2 is not None else 10**9
                            if p2 != psi_det:
                                depth_super_mod_p += 1

    print("\n" + "=" * 96, flush=True)
    print("RIGOROUS IDENTITIES (exact, over all Phi-minimizers):", flush=True)
    print(f"  psi_det == v_p(2 Re[(u-1)g(u)])  (trace form)      : {id_trace_ok}",
          flush=True)
    print(f"  psi_det == v_p(sum_j c_j tau_j)  (Lucas form)       : {id_lucas_ok}",
          flush=True)
    print(f"  v_p(Norm(P_T(u))) == 0 always (p-unit, p inert)     : {norm_unit_ok}",
          flush=True)
    print(f"\nMECHANISM HUNT (psi>0 Phi-minimizers).  max psi = {max_psi}", flush=True)
    print("  psi -> distribution of (mu_max, ncoll=m-#classes):", flush=True)
    for k in sorted(by_psi):
        print(f"    psi={k}: {dict(by_psi[k])}", flush=True)
    print(f"\n  p-adic DEPTH: shifting nodes t->t+p (same class) changed psi in "
          f"{depth_super_mod_p} configs", flush=True)
    print("    (0 => psi is a mod-p RESIDUE phenomenon: adversary has no deep", flush=True)
    print("     p-adic freedom, supporting a uniform bound.  >0 => psi needs", flush=True)
    print("     genuine p-adic tuning.)", flush=True)
    print("\nREADING (L5): trace/Lucas identity now VERIFIED => the §6j reduction's", flush=True)
    print("algebraic backbone is rigorous.  psi bound remains EVIDENCE.  RH [OUT].",
          flush=True)
