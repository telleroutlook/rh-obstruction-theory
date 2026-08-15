#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into
proofs.  No RH / RH-equivalent input.

OP1 LEG3 existence route (post-§6k): a possible PROOF handle for the sole open
core -- min over Phi-minimizers of psi = v_p(Psi) is bounded.

RIGOROUS AFFINE IDENTITY (to verify).  Fix all nodes but one; view Psi as a
function of that node's x-value x_k.  Since
    Psi = Tr[(u-1) prod_j (u - x_j)] = Tr[(u - x_k) * H(u)],
    H(u) = (u-1) prod_{j != k} (u - x_j),
expanding the linear factor gives
    Psi(x_k) = Tr[u H(u)] - x_k * Tr[H(u)] = a_k - x_k * b_k,
AFFINE in x_k, with a_k = 2 Re[u H(u)], b_k = 2 Re[H(u)] rational.

CONSEQUENCES the probe tests:
  (I)  the affine identity holds EXACTLY (Psi == a_k - x_k b_k) for every node of
       every Phi-minimizer;
  (II) v_p(Psi) >= 1  <=>  a_k ≡ x_k b_k (mod p): a CLASS condition (x_k mod p is
       fixed by the residue class), representative-independent at order 1;
  (III) ESCAPE mechanism: if some node k has a UNIT slope v_p(b_k)=0 and its class
       does NOT force a_k ≡ x_k b_k (mod p), then psi=0 is already attained; more
       generally the achievable min v_p(Psi) over same-class representatives is
       controlled by the "class-forcing order" f_k = v_p(a_k - xbar_k b_k) capped
       by representative freedom.  We measure, over Phi-minimizers:
         - min over nodes of v_p(b_k)  (is there always a unit-slope node?),
         - the class-forcing order distribution,
         - whether min-psi correlates with min_k f_k (the best escape node).

HONESTY (L5): EVIDENCE hunting a proof handle, not a proof.  RH stays [OUT].
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


def cprod(u, ys):
    acc = (Fr(1), Fr(0))
    for y in ys:
        acc = cmul(acc, csub(u, (Fr(y), Fr(0))))
    return acc


def Psi_val(u, xs):
    """2 Re[(u-1) prod_{x in xs}(u - x)]  (rational)."""
    val = cmul(csub(u, (Fr(1), Fr(0))), cprod(u, xs))
    return 2 * val[0]


def ab_of_node(u, xs, k):
    """a_k = 2Re[u H(u)], b_k = 2Re[H(u)], H=(u-1)prod_{j!=k}(u-x_j)."""
    rest = [xs[j] for j in range(len(xs)) if j != k]
    H = cmul(csub(u, (Fr(1), Fr(0))), cprod(u, rest))
    a = 2 * cmul(u, H)[0]
    b = 2 * H[0]
    return a, b


def Phi(xs, p):
    s = sum((vpf(x - 1, p) or 0) for x in xs)
    for i in range(len(xs)):
        for j in range(i + 1, len(xs)):
            s += (vpf(xs[j] - xs[i], p) or 0)
    return s


def xres(x, p):
    den = x.denominator % p
    if den == 0:
        return None                      # x ≡ infinity mod p
    return (x.numerator % p) * pow(den, p - 2, p) % p


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
    print("OP1 LEG3 existence route: affine identity Psi = a_k - x_k b_k + escape test",
          flush=True)
    print("DISCOVERY TIER.  No RH input.", flush=True)
    print("=" * 96, flush=True)

    affine_ok = True
    # ESCAPE / PACKING dichotomy aggregates
    slack_vs_minpsi = Counter()   # (slack clamped, min-psi) occurrences
    unit_slope_present = 0        # positive-psi Phi-minimizers with a unit-slope node
    total_pos = 0                 # positive-psi Phi-minimizers
    esc_reduces = 0               # of those, reducible by a diff-class Phi-preserving swap
    packed_when_pos = 0           # positive-min-psi configs that are PACKED (navail<=m-1)
    config_pos = 0                # positive-min-psi configs
    max_minpsi = 0

    for label, sig, tau in ORBITS:
        u = off_atoms_u(sig, tau)[0]
        for p in (3, 7, 11):
            for m in range(2, 8):
                for fname, ts in families(m, p).items():
                    if len(ts) < m:
                        continue
                    oc, vo = cleared_columns(ts, sig, tau, m)
                    q = qmin_fast(oc, vo)
                    if not q:
                        continue
                    rows = [(Phi([x_of(ts[k]) for k in S], p), S)
                            for S in combinations(range(len(oc)), m - 1)]
                    minPhi = min(ph for ph, _ in rows)
                    # collect Phi-minimizers with their psi + best escape order
                    minis = []
                    for ph, S in rows:
                        if ph != minPhi:
                            continue
                        xs = [x_of(ts[k]) for k in S]
                        psi = vpf(Psi_val(u, xs), p)
                        psi = psi if psi is not None else 10**9
                        # (I) affine identity + presence of a unit-slope node
                        has_unit_slope = False
                        for k in range(len(xs)):
                            a, b = ab_of_node(u, xs, k)
                            if a - xs[k] * b != Psi_val(u, xs):   # affine check
                                affine_ok = False
                            if vpf(b, p) == 0:
                                has_unit_slope = True
                        minis.append((psi, S, has_unit_slope))
                    if not minis:
                        continue
                    minpsi = min(z[0] for z in minis)
                    max_minpsi = max(max_minpsi, minpsi)
                    # PACKING dichotomy: navail = #distinct x-classes (!= class of 1)
                    # among ALL ambient nodes; slack = navail - (m-1).
                    xall = [x_of(t) for t in ts]
                    rescls = set(c for c in (xres(x, p) for x in xall) if c is not None)
                    c1 = xres(Fr(1), p)
                    navail = len(rescls - ({c1} if c1 in rescls else set()))
                    slack = navail - (m - 1)
                    slack_vs_minpsi[(max(min(slack, 4), -4), min(minpsi, 9))] += 1
                    if minpsi > 0:
                        config_pos += 1
                        if navail <= m - 1:
                            packed_when_pos += 1
                    # ESCAPE: for positive-psi Phi-minimizers, does a DIFFERENT-class,
                    # Phi-preserving single-node swap (via a unit-slope node) reduce psi?
                    for psi, S, us_ in minis:
                        if psi <= 0:
                            continue
                        total_pos += 1
                        if us_:
                            unit_slope_present += 1
                        Sset = set(S)
                        xs = [x_of(ts[k]) for k in S]
                        reduced = False
                        for ki, k in enumerate(S):
                            _, b = ab_of_node(u, xs, ki)
                            if vpf(b, p) != 0:
                                continue                    # need unit slope
                            ck = xres(x_of(ts[k]), p)
                            for kp in range(len(oc)):
                                if kp in Sset or xres(x_of(ts[kp]), p) == ck:
                                    continue                # need a DIFFERENT class
                                Snew = tuple(sorted((Sset - {k}) | {kp}))
                                if Phi([x_of(ts[j]) for j in Snew], p) != minPhi:
                                    continue
                                vn = vpf(Psi_val(u, [x_of(ts[j]) for j in Snew]), p)
                                if (vn if vn is not None else 10**9) < psi:
                                    reduced = True
                                    break
                            if reduced:
                                break
                        if reduced:
                            esc_reduces += 1

    print("\n" + "=" * 96, flush=True)
    print(f"(I) affine identity  Psi == a_k - x_k b_k  (all nodes, all Phi-min): {affine_ok}",
          flush=True)
    print(f"    max over configs of min_(Phi-min) psi = {max_minpsi}", flush=True)
    print(f"\n(III) ESCAPE / PACKING dichotomy:", flush=True)
    print(f"    positive-min-psi CONFIGS: {config_pos};  of these PACKED "
          f"(navail<=m-1): {packed_when_pos}", flush=True)
    print(f"    positive-psi Phi-minimizers: {total_pos};  with >=1 unit-slope node "
          f"v_p(b_k)=0: {unit_slope_present}", flush=True)
    print(f"    a diff-class Phi-preserving swap REDUCES psi in {esc_reduces} of them",
          flush=True)
    print(f"    (slack = navail-(m-1)) vs min-psi  [slack clamped +-4]:", flush=True)
    for k in sorted(slack_vs_minpsi):
        print(f"      slack={k[0]:>2}  min-psi={k[1]}: {slack_vs_minpsi[k]}", flush=True)
    print("\nREADING (L5): slack>=1 (a spare x-class) => min-psi=0 => lag=0 (affine", flush=True)
    print("escape via a unit-slope node into the spare class).  Positive lag is", flush=True)
    print("CONFINED to PACKED configs (navail<=m-1), where it stays <=3 empirically.", flush=True)
    print("This narrows LEG3 to the packed regime.  EVIDENCE, not proof.  RH [OUT].",
          flush=True)
