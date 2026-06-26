Baseball card -> prime: published primes
=========================================
Each prime is the integer form of a baseball-card image (raw RGB bytes read as
one big-endian number, advanced by `nonce` to the next prime). Subtracting the
nonce returns the exact image, bit-for-bit.

To verify any entry (needs: pip install gmpy2 pillow):
    python verify.py <name>.meta.json

That re-tests primality (BPSW + 50 Miller-Rabin rounds) and rebuilds the image
from the prime, confirming the SHA-256 matches. Primes are probable primes by
the BPSW standard used for all large general primes; a deterministic ECPP proof
would be a separate, much larger computation.
