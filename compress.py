#!/usr/bin/env python3
"""HKD Compress V4 Universal — exact byte-stream compressor.

Works on arbitrary files: ASCII/text, binary, serialized/intermediate datasets,
images, media, archives, etc. Compression is lossless and content-agnostic.

Examples:
  python3 hkd_compress_v4_universal.py kjv.txt
  python3 hkd_compress_v4_universal.py model.bin
  python3 hkd_compress_v4_universal.py --decompress kjv.txt.hkd
  python3 hkd_compress_v4_universal.py --audit input.dat
"""
from __future__ import annotations
import argparse, bz2, hashlib, json, lzma, os, struct, time, zlib
from pathlib import Path

BUILD = 'HKD_COMPRESS_V4_UNIVERSAL_20260830'
MAGIC = b'HKDU4\0\0\0'
MODE_RAW, MODE_ZLIB, MODE_BZ2, MODE_LZMA = range(4)
HEADER = struct.Struct('>8sBQQ32s')  # magic, mode, original bytes, payload bytes, sha256
MODE_NAME = {MODE_RAW:'raw', MODE_ZLIB:'zlib', MODE_BZ2:'bzip2', MODE_LZMA:'lzma'}


def sha256_bytes(data: bytes) -> bytes:
    return hashlib.sha256(data).digest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        while True:
            b = f.read(4 << 20)
            if not b: break
            h.update(b)
    return h.hexdigest()


def encode_candidates(data: bytes):
    return [
        (MODE_RAW, data),
        (MODE_ZLIB, zlib.compress(data, 9)),
        (MODE_BZ2, bz2.compress(data, compresslevel=9)),
        (MODE_LZMA, lzma.compress(data, preset=9)),
    ]


def encode_best(data: bytes):
    # Select based on final archive payload size; deterministic ties favor simpler mode.
    return min(encode_candidates(data), key=lambda x: (len(x[1]), x[0]))


def decode(mode: int, payload: bytes) -> bytes:
    if mode == MODE_RAW: return payload
    if mode == MODE_ZLIB: return zlib.decompress(payload)
    if mode == MODE_BZ2: return bz2.decompress(payload)
    if mode == MODE_LZMA: return lzma.decompress(payload)
    raise ValueError('unknown HKD codec mode %r' % mode)


def default_archive(src: Path) -> Path:
    return Path(str(src) + '.hkd')


def default_decoded(archive: Path) -> Path:
    s = str(archive)
    return Path((s[:-4] if s.endswith('.hkd') else s) + '.dec')


def compress(src: Path, out: Path):
    t0 = time.perf_counter()
    data = src.read_bytes()
    mode, payload = encode_best(data)
    digest = sha256_bytes(data)
    with out.open('wb') as f:
        f.write(HEADER.pack(MAGIC, mode, len(data), len(payload), digest))
        f.write(payload)
    out_bytes = out.stat().st_size
    ratio = out_bytes / float(len(data)) if data else 0.0
    return {
        'build': BUILD, 'operation':'compress', 'kind':'arbitrary_bytes',
        'input':str(src), 'output':str(out), 'codec':MODE_NAME[mode],
        'input_bytes':len(data), 'output_bytes':out_bytes,
        'actual_ratio':ratio, 'compression_x':(1.0/ratio if ratio else 0.0),
        'sha256':digest.hex(), 'exact':True,
        'seconds':time.perf_counter()-t0,
    }


def decompress(archive: Path, out: Path):
    t0 = time.perf_counter()
    with archive.open('rb') as f:
        raw = f.read(HEADER.size)
        if len(raw) != HEADER.size: raise ValueError('truncated HKD header')
        magic, mode, original_size, payload_size, digest = HEADER.unpack(raw)
        if magic != MAGIC: raise ValueError('not an HKD V4 Universal archive')
        payload = f.read(payload_size)
        if len(payload) != payload_size: raise ValueError('truncated HKD payload')
        if f.read(1): raise ValueError('trailing bytes after HKD payload')
    data = decode(mode, payload)
    if len(data) != original_size: raise ValueError('decoded size mismatch')
    if sha256_bytes(data) != digest: raise ValueError('decoded SHA-256 mismatch')
    out.write_bytes(data)
    return {
        'build':BUILD, 'operation':'decompress', 'input':str(archive), 'output':str(out),
        'codec':MODE_NAME[mode], 'output_bytes':len(data), 'sha256':digest.hex(),
        'sha256_ok':True, 'exact':True, 'seconds':time.perf_counter()-t0,
    }


def audit(src: Path):
    data = src.read_bytes(); n = len(data)
    rows=[]
    for mode,payload in encode_candidates(data):
        archive_bytes = HEADER.size + len(payload)
        rows.append({'codec':MODE_NAME[mode], 'archive_bytes':archive_bytes,
                     'ratio':archive_bytes/float(n) if n else 0.0,
                     'compression_x':n/float(archive_bytes) if archive_bytes else 0.0})
    best=min(rows,key=lambda r:(r['archive_bytes'], list(MODE_NAME.values()).index(r['codec'])))
    return {'build':BUILD,'operation':'audit','input':str(src),'input_bytes':n,
            'sha256':hashlib.sha256(data).hexdigest(),'candidates':rows,'best':best}


def main():
    ap=argparse.ArgumentParser(description=BUILD)
    ap.add_argument('input', help='any file / byte stream')
    ap.add_argument('-o','--output')
    ap.add_argument('--decompress', action='store_true')
    ap.add_argument('--audit', action='store_true', help='measure all exact codecs without keeping an archive')
    ap.add_argument('--verify', action='store_true', help='compress then decode and compare SHA-256')
    a=ap.parse_args()
    src=Path(a.input)
    if not src.is_file(): raise SystemExit('not found: %s' % src)
    if a.decompress:
        out=Path(a.output) if a.output else default_decoded(src)
        print(json.dumps(decompress(src,out),sort_keys=True)); return
    if a.audit:
        print(json.dumps(audit(src),sort_keys=True)); return
    out=Path(a.output) if a.output else default_archive(src)
    result=compress(src,out)
    if a.verify:
        temp=Path(str(out)+'.verify.dec')
        try:
            d=decompress(out,temp)
            result['verify_sha256_ok']=(sha256_file(src)==sha256_file(temp)==d['sha256'])
            if not result['verify_sha256_ok']: raise RuntimeError('verification mismatch')
        finally:
            try: temp.unlink()
            except OSError: pass
    print(json.dumps(result,sort_keys=True))

if __name__ == '__main__':
    main()
