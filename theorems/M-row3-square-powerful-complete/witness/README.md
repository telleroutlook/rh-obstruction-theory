# Witness — Theorem M

`oe02_pari_replay_v1.gp` is the raw independent PARI/GP replay script. It
computes `ellrank`, `elltors`, `ellmul`, and `ellisomat` on:

1. the claimed model `E: y^2=x^3-32x+64`;
2. the translated 2-torsion model `y^2=u^3+12u^2+16u`;
3. its 2-isogenous model `y^2=u^3-24u^2+80u`.
4. the Jacobian of the corrected quartic
   `y^2=10t^4-20t^3+24t^2-12t+2`, namely `[0,24,0,160,320]`.

`oe02_pari_replay_v1.txt` is the pinned PARI 2.17.4 output. The transcript is
not a producer summary: `verify_OE02_pari_replay.py` parses the raw key/value
output, requires certified rank bounds `[0,0]`, and independently checks the
translation/isogeny/corrected-quartic coefficient identities. Running the checker with `--run`
reruns GP and requires the same transcript.

The broader finite scans in `checker/verify_M.py` and
`checker/verify_OE02_elliptic.py` are sanity evidence, not proof inputs.
The explicit birational map is replayed by `checker/verify_OE02_quartic_map.py`;
the exact individual-square boundary example `(a,n)=(15,8)` is deliberately
kept there to prevent reviving the false individual `4|n` claim.

Evidence boundary: the CAS replay upgrades only the finite computational axis.
It does not automatically certify the analytic 5-conic reduction or torsion
pullback argument; Theorem M remains mathematically PROOF-DRAFT.
