# Provenance anchor — the "first" milestone

This folder permanently preserves the **first** Bitcoin-confirmed timestamp for this
project: the original set of six primes (CJ Alexander, front + back, at 50px / 64px /
80px). It is the immutable proof of *when* a baseball card was first encoded as a
provable prime number and published.

- `milestone-2026-06-26.MANIFEST.sha256` — the exact manifest (SHA-256 of every file in
  that original set) as it stood on 2026-06-26.
- `milestone-2026-06-26.MANIFEST.sha256.ots` — its OpenTimestamps proof, **confirmed in
  the Bitcoin blockchain** (BitcoinBlockHeaderAttestation, block **955541**; a second
  anchor in block 955536).

These two files never change. The top-level `../MANIFEST.sha256` and
`../MANIFEST.sha256.ots` roll forward to cover the full, growing set (100px and beyond)
and are re-stamped as new primes are minted — but this milestone stays frozen so the
priority claim is always independently verifiable.

## Verify it yourself

```sh
pip install opentimestamps-client
ots verify milestone-2026-06-26.MANIFEST.sha256.ots
# attests the SHA-256 of milestone-2026-06-26.MANIFEST.sha256 was committed to
# Bitcoin block 955541 on 2026-06-26.
```

> Note: this manifest is stored with CRLF line endings — the exact bytes that were
> timestamped. `.gitattributes` pins it (`-text`) so the hash, and therefore the
> Bitcoin proof, keeps verifying.
