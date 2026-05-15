#!/usr/bin/env python3
"""Verify FILE_MANIFEST.csv for this repository.

The manifest intentionally excludes FILE_MANIFEST.csv and FILE_MANIFEST.json.
"""
from __future__ import annotations

import csv
import hashlib
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "FILE_MANIFEST.csv"
EXCLUDED = {"FILE_MANIFEST.csv", "FILE_MANIFEST.json"}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    rows = []
    with MANIFEST.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    ok = True
    manifest_paths = {row["path"] for row in rows}
    actual_paths = {
        str(p.relative_to(ROOT)).replace("\\", "/")
        for p in ROOT.rglob("*")
        if p.is_file() and str(p.relative_to(ROOT)).replace("\\", "/") not in EXCLUDED
    }

    missing = sorted(actual_paths - manifest_paths)
    extra = sorted(manifest_paths - actual_paths)
    if missing or extra:
        ok = False
        print("Manifest path mismatch")
        if missing:
            print("Missing from manifest:", missing)
        if extra:
            print("Extra in manifest:", extra)

    for row in rows:
        rel = row["path"]
        path = ROOT / rel
        if not path.exists():
            ok = False
            print(f"MISSING: {rel}")
            continue
        size = path.stat().st_size
        sha = sha256_file(path)
        if int(row["size_bytes"]) != size or row["sha256"] != sha:
            ok = False
            print(f"MISMATCH: {rel}")
            print(f"  manifest size={row['size_bytes']} sha={row['sha256']}")
            print(f"  actual   size={size} sha={sha}")

    if ok:
        print("PASS: manifest verification succeeded")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
