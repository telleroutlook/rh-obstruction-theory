#!/usr/bin/env python3
"""Validate baseline/CLAIM_LEDGER.yaml against schemas/claim-ledger-v1 core rules.

stdlib-only (project discipline: checker/ takes no third-party deps). Parses the tiny
YAML subset the ledger uses without PyYAML. Exit codes: 0 = all valid, 1 = violations,
2 = malformed input.

The point is not to re-implement JSON Schema, but to enforce the load-bearing DERIVED
rules the ledger must satisfy (program §6.A.2, CLAUDE.md two-axis discipline):
  - required fields present; enum axes valid;
  - usable_as_premise=true  =>  mathematical in {INDEPENDENTLY-CHECKED, REFEREED};
  - gate_a_status=PENDING    =>  usable_as_premise=false.
"""
from __future__ import annotations
import sys
from pathlib import Path

MATH = {"DEFINITION", "CONJECTURE", "PROOF-DRAFT", "INDEPENDENTLY-CHECKED", "REFEREED"}
COMP = {"NONE", "EXPLORATORY", "REPRODUCIBLE", "INDEPENDENT-CHECKER", "FORMALIZED"}
REQUIRED = ("id", "statement", "source", "peer_reviewed",
            "mathematical", "computational", "usable_as_premise")


def _strip_comment(v: str) -> str:
    """Drop an unquoted trailing '# ...' comment (YAML requires a space before it)."""
    if v and v[0] in ("'", '"'):
        return v  # quoted scalar: leave as-is
    i = v.find(" #")
    if i != -1:
        v = v[:i]
    if v.rstrip().endswith(" #"):
        v = v.rstrip()[:-1]
    return v.strip()


def _coerce(v: str):
    s = _strip_comment(v.strip()).strip('"').strip("'")
    if s.lower() in ("true", "false"):
        return s.lower() == "true"
    return s


def load_claims(path: Path) -> list[dict]:
    """Parse the flat 'claims:' list of scalar key: value items (block scalars folded)."""
    claims: list[dict] = []
    cur: dict | None = None
    pending_key: str | None = None
    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        stripped = raw.strip()
        if stripped.startswith("- id:"):
            if cur is not None:
                claims.append(cur)
            cur = {}
            pending_key = None
            k, _, v = stripped[2:].partition(":")
            cur[k.strip()] = _coerce(v)
            continue
        if cur is None:
            continue  # pre-claims header (version:, domain:, claims:)
        indent = len(raw) - len(raw.lstrip())
        if indent < 4:  # left the claims list
            claims.append(cur)
            cur = None
            continue
        if ":" in stripped and not stripped.startswith(">"):
            k, _, v = stripped.partition(":")
            v = _strip_comment(v.strip())
            if v in (">", "|", ">-", "|-"):
                pending_key = k.strip()
                cur[pending_key] = ""
            else:
                cur[k.strip()] = _coerce(v)
                pending_key = None
        elif pending_key is not None:
            cur[pending_key] = (cur[pending_key] + " " + stripped).strip()
    if cur is not None:
        claims.append(cur)
    return claims


def validate(claim: dict) -> list[str]:
    errs: list[str] = []
    for k in REQUIRED:
        if k not in claim:
            errs.append(f"missing '{k}'")
    if claim.get("mathematical") not in MATH:
        errs.append(f"bad mathematical={claim.get('mathematical')!r}")
    if claim.get("computational") not in COMP:
        errs.append(f"bad computational={claim.get('computational')!r}")
    if claim.get("usable_as_premise") is True and claim.get("mathematical") not in (
        "INDEPENDENTLY-CHECKED", "REFEREED"):
        errs.append("usable_as_premise=true but mathematical axis below INDEPENDENTLY-CHECKED")
    if claim.get("gate_a_status") == "PENDING" and claim.get("usable_as_premise") is not False:
        errs.append("gate_a_status=PENDING but usable_as_premise is not false")
    return errs


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    ledger = root / "baseline" / "CLAIM_LEDGER.yaml"
    if not ledger.exists():
        print(f"[FAIL] ledger not found: {ledger}", file=sys.stderr)
        return 2
    claims = load_claims(ledger)
    if not claims:
        print("[FAIL] no claims parsed", file=sys.stderr)
        return 2
    bad = 0
    for c in claims:
        errs = validate(c)
        if errs:
            bad += 1
            print(f"[INVALID] {c.get('id', '<no id>')}: " + "; ".join(errs))
    print(f"claims: {len(claims)}  invalid: {bad}", flush=True)
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
