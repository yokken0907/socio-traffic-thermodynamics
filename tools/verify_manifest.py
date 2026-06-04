#!/usr/bin/env python3
"""Verify FILE_MANIFEST.csv for this repository package."""
from __future__ import annotations
import csv, hashlib, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "FILE_MANIFEST.csv"
EXCLUDE = {"FILE_MANIFEST.csv", "FILE_MANIFEST.json"}

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def main() -> int:
    if not MANIFEST.exists():
        print("FAIL: FILE_MANIFEST.csv not found")
        return 1
    rows = []
    with MANIFEST.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    ok = True
    seen = set()
    for row in rows:
        rel = row["path"]
        seen.add(rel)
        path = ROOT / rel
        if not path.exists():
            print(f"FAIL missing: {rel}")
            ok = False
            continue
        size = path.stat().st_size
        digest = sha256(path)
        if str(size) != row["size_bytes"]:
            print(f"FAIL size: {rel} manifest={row['size_bytes']} actual={size}")
            ok = False
        if digest != row["sha256"]:
            print(f"FAIL sha256: {rel}")
            ok = False
    actual = set()
    for p in ROOT.rglob("*"):
        if p.is_file():
            rel = p.relative_to(ROOT).as_posix()
            if rel in EXCLUDE or rel.startswith(".git/"):
                continue
            actual.add(rel)
    extra = sorted(actual - seen)
    stale = sorted(seen - actual)
    for rel in extra:
        print(f"FAIL unlisted: {rel}")
        ok = False
    for rel in stale:
        print(f"FAIL stale-listed: {rel}")
        ok = False
    if ok:
        print(f"PASS: manifest verified ({len(rows)} files)")
        return 0
    return 1

if __name__ == "__main__":
    raise SystemExit(main())
