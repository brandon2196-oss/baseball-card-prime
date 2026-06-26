#!/usr/bin/env python3
"""Standalone verifier. Usage: python verify.py <name>.meta.json
Reconstructs the card image from (prime - nonce), checks the SHA-256, and
re-tests primality. Requires: pip install gmpy2 pillow"""
import sys, json, hashlib
from pathlib import Path
import gmpy2
from PIL import Image
sys.set_int_max_str_digits(0)

meta = json.load(open(sys.argv[1]))
P = int(open(Path(sys.argv[1]).with_name(meta['prime_file'])).read().strip())
N = P - meta['nonce']
img_bytes = N.to_bytes(meta['bytes'], 'big')
ok_hash = hashlib.sha256(img_bytes).hexdigest() == meta['original_hash']
ok_prime = bool(gmpy2.is_prime(P, 50))
print("digits        :", meta['digits'])
print("dimensions    :", meta['dimensions'], meta['mode'])
print("prime (BPSW)  :", "PASS" if ok_prime else "FAIL")
print("reconstruction:", "PASS (bit-perfect)" if ok_hash else "FAIL")
Image.frombytes(meta['mode'], tuple(meta['dimensions']), img_bytes).save(
    Path(sys.argv[1]).with_name(meta['image'].replace('.png','_verified.png')))
print("wrote verified image. overall:", "PASS" if (ok_prime and ok_hash) else "FAIL")
