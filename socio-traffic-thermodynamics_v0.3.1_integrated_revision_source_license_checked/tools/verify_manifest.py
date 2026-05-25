#!/usr/bin/env python3
import csv, hashlib, sys
from pathlib import Path
root = Path(__file__).resolve().parents[1]
manifest = root / 'FILE_MANIFEST.csv'
ok = True
with open(manifest, newline='', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        p = root / row['path']
        if not p.exists():
            print('MISSING', row['path']); ok=False; continue
        h = hashlib.sha256(p.read_bytes()).hexdigest()
        if h != row['sha256']:
            print('HASH_MISMATCH', row['path']); ok=False
print('PASS manifest verification' if ok else 'FAIL manifest verification')
sys.exit(0 if ok else 1)
