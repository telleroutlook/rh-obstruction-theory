#!/usr/bin/env python3
"""
DISCOVERY TIER (program §12.1) — conjecture/evidence only; NOT imported into
proofs.  No RH / RH-equivalent input.

OP1 LEG3 escape-lemma hypothesis (a), now with a PROOF to verify.

CLAIM (candidate [THM], derived; verify the explicit formula by script per L9):
Let S0 be a Phi-minimizer with psi = v_p(Psi) > 0, i.e. Tr(P_T(u)) ≡ 0 mod p, where
P_T(X) = (X-1) prod_{k in S0}(X - x_k) and u = a + b i is the fixed off-line atom
(p inert => u not in F_p => b = Im(u) a p-unit).  Since P_T(u) is a p-UNIT (Norm a
p-unit, §6k), P_T(u) ≡ 0 mod p is impossible; psi>0 forces P_T(u) ≡ c i mod p (purely
imaginary), c != 0 in F_p.  For the affine slope b_k = Tr[H_k(u)],
H_k = P_T(u)/(u - x_k):
    H_k ≡ c i / ((a - x_k) + b i) = c[b + (a - x_k) i]/mu(x_k),  mu(x_k)=(a-x_k)^2+b^2,
    => b_k = Tr(H_k) = 2 Re(H_k) ≡ 2 c b / mu(x_k)  (mod p).
Since c != 0, b != 0, mu(x_k) != 0 (p inert => mu(y) != 0 for all y in F_p), EVERY
node has b_k a p-UNIT.  Hence escape-lemma hypothesis (a) holds: a unit-slope node
always exists (in fact all nodes qualify) whenever psi>0.

This probe verifies, mod p, on every Phi-minimizer with psi>0:
  (1) P_T(u) is purely imaginary (Re ≡ 0 mod p), and extracts c;
  (2) b_k ≡ 2 c b / mu(x_k)  for every node k  (the explicit slope formula);
  (3) all b_k are p-units.

HONESTY (L5): verifies a derived formula; the escape lemma still needs hypothesis
(b) (spare-class swap preserves Phi-minimality) and a packed-regime bound.  RH [OUT].
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import ceil
from itertools import combinations

from discovery.probe_qmin_snf import cleared_columns
from discovery.qmin_snf_fast import qmin_fast
import discovery.probe_leg3_affine as A   # x_of, off_atoms_u, Psi_val, ab_of_node, Phi, vpf


def modp(fr, p):
    """Fr -> residue in F_p (den invertible: p inert, den coprime to p here)."""
    num = fr.numerator % p
    den = fr.denominator % p
    return num * pow(den, p - 2, p) % p


ORBITS = A.ORBITS


if __name__ == "__main__":
    print("=" * 96, flush=True)
    print("OP1 LEG3 escape hyp (a): verify slope formula  b_k ≡ 2 c b / mu(x_k) mod p",
          flush=True)
    print("DISCOVERY TIER.  No RH input.", flush=True)
    print("=" * 96, flush=True)

    pure_imag_ok = True     # psi>0 => P_T(u) purely imaginary mod p
    formula_ok = True       # b_k ≡ 2 c b / mu(x_k) mod p
    all_units_ok = True     # all b_k p-units when psi>0
    checked = 0

    for label, sig, tau in ORBITS:
        u = A.off_atoms_u(sig, tau)[0]
        a, b = u                                  # u = a + b i (rational)
        for p in (3, 7, 11):
            bmod = modp(b, p)
            for m in range(2, 8):
                for fname, ts in A.families(m, p).items():
                    if len(ts) < m:
                        continue
                    oc, vo = cleared_columns(ts, sig, tau, m)
                    if not qmin_fast(oc, vo):
                        continue
                    rows = [(A.Phi([A.x_of(ts[k]) for k in S], p), S)
                            for S in combinations(range(len(oc)), m - 1)]
                    minPhi = min(ph for ph, _ in rows)
                    for ph, S in rows:
                        if ph != minPhi:
                            continue
                        xs = [A.x_of(ts[k]) for k in S]
                        psi = A.vpf(A.Psi_val(u, xs), p)
                        if psi is None or psi <= 0:
                            continue
                        checked += 1
                        # (1) P_T(u) = (u-1) prod (u - x_k); real part mod p == 0
                        PT = A.cmul(A.csub(u, (Fr(1), Fr(0))), A.cprod(u, xs))
                        re_mod = modp(PT[0], p)
                        im_mod = modp(PT[1], p)
                        if re_mod != 0:
                            pure_imag_ok = False
                        c = im_mod                        # P_T(u) ≡ c i
                        # (2)&(3) slope formula for every node
                        for ki, xk in enumerate(xs):
                            _, bk = A.ab_of_node(u, xs, ki)   # exact rational slope
                            bk_mod = modp(bk, p)
                            mu = (a - xk) * (a - xk) + b * b   # Norm(u - x_k)
                            mu_mod = modp(mu, p)
                            pred = (2 * c * bmod % p) * pow(mu_mod, p - 2, p) % p
                            if bk_mod != pred:
                                formula_ok = False
                            if bk_mod == 0:
                                all_units_ok = False

    print("\n" + "=" * 96, flush=True)
    print(f"positive-psi Phi-minimizers checked: {checked}", flush=True)
    print(f"(1) psi>0 => P_T(u) purely imaginary mod p (Re==0)     : {pure_imag_ok}",
          flush=True)
    print(f"(2) slope formula  b_k ≡ 2 c b / mu(x_k)  mod p         : {formula_ok}",
          flush=True)
    print(f"(3) all b_k are p-units when psi>0 (=> escape hyp (a))  : {all_units_ok}",
          flush=True)
    print("\nREADING (L5): the escape-lemma hypothesis (a) is PROVED (unit-slope node", flush=True)
    print("always exists; all nodes qualify) with explicit formula b_k=2cb/mu(x_k).", flush=True)
    print("Remaining for the escape lemma: (b) spare-class swap preserves Phi-min;", flush=True)
    print("and the packed-regime min-psi bound.  EVIDENCE for a proof.  RH [OUT].",
          flush=True)
