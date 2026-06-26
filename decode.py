#!/usr/bin/env python3
"""Rebuild the card image from its prime. Instant - no primality test.
Usage:  python decode.py <name>.meta.json
Needs:  pip install pillow
"""
import sys, json
from pathlib import Path
from PIL import Image
sys.set_int_max_str_digits(0)

meta = json.load(open(sys.argv[1]))
prime_path = Path(sys.argv[1]).with_name(meta['prime_file'])
P = int(prime_path.read_text().strip())      # the prime number

N = P - meta['nonce']                         # exact original integer
img_bytes = N.to_bytes(meta['bytes'], 'big')  # integer -> raw RGB bytes
img = Image.frombytes(meta['mode'], tuple(meta['dimensions']), img_bytes)

out = Path(sys.argv[1]).with_name(meta['image'].replace('.png', '_decoded.png'))
img.save(out)
print(f"wrote {out}  ({img.size[0]}x{img.size[1]} {img.mode})")
