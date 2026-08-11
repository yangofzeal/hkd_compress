# HKD Compress

**HKD Compress** is a self-contained, lossless compression system based on HKD∞ structural reduction. On an English ASCII file, it beat bzip2 by 9.5% in compressed file size. It is designed to identify deterministic or reconstructible structure in an input, represent that structure compactly, and apply lossless compression to the remaining active information.

An `.hkd` archive is **self-contained**: decompression requires only the `.hkd` file. No base file, shared dictionary, receiver-side state, network connection, or external corpus is required.

## Quick Start

HKD Compress exposes an importable Python package:

```python
import hkd_compress

result = hkd_compress.compress("input.dat")
hkd_compress.decompress("input.dat.hkd")
```

The distribution also includes the unobfuscated `compress.py` command-line interface.

### Compress a file

```bash
python compress.py --compress input.dat
```

This creates:

```text
input.dat.hkd
```

### Decompress a file

```bash
python compress.py --decompress input.dat.hkd
```

This creates:

```text
input.dat.dec
```

The decompressed file is reconstructed losslessly.

You can verify it directly on Linux or macOS:

```bash
cmp input.dat input.dat.dec
```

For SHA-256 verification on Linux:

```bash
sha256sum input.dat input.dat.dec
```

On macOS:

```bash
shasum -a 256 input.dat input.dat.dec
```

Matching hashes confirm exact reconstruction.

## KJV Compression Benchmark

A self-contained compression test was performed on `kjv.txt`.

The original file was:

```text
4,638,061 bytes
```

The supplied bzip2 archive was:

```text
962,764 bytes
```

HKD Compress produced:

```text
871,870 bytes
```

Results:

| Format | Compressed Size | Compression Ratio |
|---|---:|---:|
| Original `kjv.txt` | 4,638,061 bytes | 1.000× |
| bzip2 | 962,764 bytes | 4.817× |
| **HKD Compress** | **871,870 bytes** | **5.320×** |

On this benchmark, the HKD archive was:

- **90,894 bytes smaller than bzip2**
- **9.44% smaller than the supplied bzip2 archive**
- **1.104× the bzip2 compression ratio**
- **exactly reversible**

The tested HKD run reported:

```text
HKD_SELF_CONTAINED_COMPRESS
input=kjv.txt
output=kjv.txt.hkd
mode=HKD-structural
input_bytes=4638061
hkd_bytes=871870
compression_x=5.319670
records=31102
books=66
chapters=1189
dictionary_entries=27
base_required=False
self_contained=True
```

Decompression reproduced all **4,638,061 bytes** exactly, with matching SHA-256 output and a successful byte-for-byte comparison.

> **Benchmark scope:** The KJV result demonstrates performance on this particular highly structured text corpus. It should not be interpreted as a guarantee that every file will compress 9.44% better than bzip2. Compression performance depends on the structure and entropy of the input.

## How HKD Compression Works

HKD Compress applies an HKD∞-inspired **structural reduction and active-information encoding** process.

Rather than treating every input byte as equally independent, the compressor searches for structure that can be represented more economically while remaining deterministically reconstructible. Reconstructible structure is represented by compact internal metadata, while the remaining active symbolic information is transformed and encoded losslessly. The archive contains the information necessary to reverse these operations and reproduce the original byte stream exactly.

At a high level:

```text
Input
  |
  v
Structural analysis
  |
  +---- reconstructible structure ----+
  |                                    |
  |                           compact representation
  |
  +---- active information ------------+
                                       |
                              lossless transformation
                                       |
                                       v
                                  HKD archive
```

During decompression, the process is reversed:

```text
HKD archive
     |
     v
Decode active information
     +
Restore structural information
     |
     v
Original byte stream
```

The implementation may select among internal representations according to the input so that applying an HKD transform does not require pretending incompressible data is compressible.

The exact structural models, selection rules, internal transforms, representation strategy, and optimization details are proprietary implementation details and are intentionally not documented here.

## Self-Contained Archives

HKD Compress is different from a stateful network-delta system.

An HKD Compress archive does **not** assume that the decoder already possesses an earlier version of the file:

```text
input.dat
    |
    v
input.dat.hkd
```

Later:

```text
input.dat.hkd
    |
    v
input.dat.dec
```

Everything necessary for reconstruction is contained in `input.dat.hkd`.

This means the archive can be copied, stored, backed up, or transmitted independently.

## Free and Paid Editions

The Free and Paid editions expose the **same compression and decompression API**. The product distinction is the maximum input file size.

### HKD Compress Free

Maximum input file size:

```text
5 MiB
5,242,880 bytes
```

A file of exactly **5,242,880 bytes is accepted**.

A file of:

```text
5,242,881 bytes
```

exceeds the Free limit and requires the Paid edition.

The included test datasets demonstrate this exact boundary:

```text
dataset_free.npz  = 5,242,880 bytes
dataset_large.npz = 5,242,881 bytes
```

### HKD Compress Paid

The Paid edition has **no HKD Compress file-size limit**.

The API and archive behavior remain the same; the size restriction is removed.

## Python API

### Compression

```python
import hkd_compress

result = hkd_compress.compress("myfile.txt")

print(result["output"])
print(result["input_bytes"])
print(result["output_bytes"])
print(result["compression_x"])
```

The default output is:

```text
myfile.txt.hkd
```

### Decompression

```python
import hkd_compress

result = hkd_compress.decompress("myfile.txt.hkd")

print(result["output"])
print(result["exact"])
print(result["sha256"])
```

The default reconstructed output is:

```text
myfile.txt.dec
```

## Distribution Layout

A source distribution is organized as:

```text
free/
├── compress.py
├── test.py
├── dataset_free.npz
├── dataset_large.npz
├── build_pyarmor.sh
└── src/
    └── hkd_compress/

paid/
├── compress.py
├── test.py
├── dataset_free.npz
├── dataset_large.npz
├── build_pyarmor.sh
└── src/
    └── hkd_compress/
```

`compress.py` is the public command-line interface.

The compression implementation is provided through:

```python
import hkd_compress
```

For protected distributions, `src/hkd_compress` can be processed separately while leaving `compress.py` unobfuscated.

## Building a Protected Distribution

From either the Free or Paid directory:

```bash
./build_pyarmor.sh
```

or directly:

```bash
pyarmor gen -O dist -r src/hkd_compress
```

The resulting protected package can then be distributed with the public CLI and test files.

## Testing

Run:

```bash
python test.py
```

The Free test verifies:

1. `dataset_free.npz` is exactly 5 MiB.
2. The file is accepted by HKD Compress Free.
3. Compression and decompression are exact.
4. `dataset_large.npz` is exactly one byte over the Free limit.
5. The one-byte-over file is rejected with the Paid-upgrade message.

The Paid test verifies that both files are accepted.

## Important Compression Note

Lossless compression cannot guarantee a fixed compression ratio for arbitrary input. High-entropy or already-compressed data may not become smaller.

HKD Compress therefore should not be described as guaranteeing the KJV compression ratio—or any fixed compression multiple—on arbitrary files.

The KJV benchmark demonstrates that HKD∞ structural reduction can provide a meaningful advantage when the input contains structure that can be represented and reconstructed more efficiently than by the comparison compressor.

## Summary

HKD Compress provides:

- **Self-contained `.hkd` archives**
- **Exact lossless reconstruction**
- **No base file or shared state**
- **Simple Python API**
- **Command-line compression and decompression**
- **HKD∞-inspired structural reduction**
- **5 MiB Free edition**
- **Unlimited-size Paid edition**
- **5.320× compression on the tested KJV corpus**
- **9.44% smaller output than the supplied bzip2 KJV archive**

The central design principle is simple:

> **Represent reconstructible structure compactly and devote storage to the information that must actually be preserved.**
