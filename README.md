# A baseball card encoded as a prime number

This repository contains prime numbers whose digits **are** a baseball card.

The card is the **2025 Topps Update Series CJ Alexander — card #US143, Halloween
parallel, serial-numbered 3/5, rookie card (RC)** (Athletics, third baseman).
Each prime here, decoded, reproduces that card's image bit-for-bit.

## How it works

1. The card image is raw RGB pixel bytes. Lined up big-endian, those bytes form
   one very large integer `N`.
2. `N` itself is almost never prime, so we find the next prime above it:
   `P = N + nonce`, where `nonce` is the (small) gap to the nearest prime.
3. Because `N` is astronomically large, adding `nonce` only changes the final
   few digits — i.e. the **single bottom-right corner pixel**. Every other pixel
   of `P`, decoded, is exactly the card.
4. `P` is a prime number. `P - nonce` is the card, exactly.

This is the "illegal prime" / "prime portrait" technique (cf. Phil Carmody's
2001 illegal prime; the 2017 Trinity Hall Prime) applied to a full-color,
licensed sports trading card — which, to our knowledge, has not been done before.

## The primes

| File | Resolution | Digits | Verified |
|------|-----------|--------|----------|
| `alexander_front_50px` | 36×50 | 13,005 | yes |
| `alexander_back_50px`  | 50×32 | 13,004 | yes |
| `alexander_front_64px` | 46×64 | 21,270 | yes |
| `alexander_back_64px`  | 64×41 | 21,269 | yes |
| `alexander_front_80px` | 57×80 | 32,945 | yes |
| `alexander_back_80px`  | 80×51 | 32,944 | yes |

Higher resolutions (100px and up) are being added as they finish.

Each card ships as:
- `<name>.prime.txt` — the prime, in full
- `<name>.meta.json` — nonce, dimensions, color mode, byte count, SHA-256 of the
  original image, and the primality method used
- `<name>_reconstructed.png` — the decoded image

## Verify it yourself

Requires `pip install pillow gmpy2`.

Rebuild the image from the prime (instant):

    python decode.py alexander_front_80px.meta.json

Rebuild **and** re-prove primality (slower — runs Miller–Rabin again):

    python verify.py alexander_front_80px.meta.json

`verify.py` confirms two things independently: that the number is prime, and
that `prime − nonce` reconstructs an image whose SHA-256 matches the recorded
original.

## A note on "prime"

These are **probable primes** by the Baillie–PSW test plus additional
Miller–Rabin rounds (via GMP/gmpy2) — the same standard used for essentially all
large general primes. A deterministic ECPP proof would be a separate, far larger
computation.

## Homage

This project is a deliberate homage to two ideas that made it possible:

- **Moneyball, and Billy Beane.** The card is an **Athletics** player — the
  franchise Billy Beane turned into the definitive story of mathematics winning
  baseball (Michael Lewis, *Moneyball*). Turning an A's rookie card into a prime
  number is a tip of the cap to that marriage of the diamond and the equation.
- **Illegal numbers.** It stands in the lineage of Phil Carmody's 2001 *illegal
  prime* — the idea that meaning, data, even a picture can live inside a prime
  number. This is that idea, wearing an Athletics uniform.

## Provenance

This folder is committed to Git and its manifest is anchored with
OpenTimestamps (`MANIFEST.sha256.ots`), establishing the date these primes
existed. Author: Brandon.
