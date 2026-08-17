# Checker — Theorem M

`verify_OE02_pari_replay.py` is the independent finite elliptic-curve replay.
By default it verifies the pinned raw PARI/GP transcript. With `--run`, it
reruns PARI/GP and requires byte-identical output. It verifies:

- original, translated, 2-isogenous, and corrected-quartic model discriminants;
- PARI `ellrank` lower and upper rank bounds both equal `0`;
- torsion structures;
- `2(0,8)=(4,0)` and `4(0,8)=O`;
- the exact translated model coefficients;
- the 2-isogenous coefficient formula;
- the coefficient translation from the corrected-quartic Jacobian to `E`.

`verify_M.py` is an exact finite scan and `verify_OE02_elliptic.py` checks
elementary torsion/group-law identities. `verify_OE02_quartic_map.py` replays
the 5-conic parameterization, corrected quartic derivation, forward/inverse
polynomial identities, torsion pullback toys, and the exact `(15,8)` boundary
example showing that individual `4|n` squares are not excluded. None of these
finite checks alone proves the analytic reduction. PARI/GP is optional at test
time; the offline checker
validates the pinned transcript, while `--run` provides live CAS replay.

This closes the formerly recorded finite CAS replay gap. It does not close
Gate A for the analytic proof.
