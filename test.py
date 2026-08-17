#!/usr/bin/env python3
import hashlib, os, sys
sys.path.insert(0, "src")
import hkd_compress

def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            b = f.read(1 << 20)
            if not b: break
            h.update(b)
    return h.hexdigest()

print("edition=%s" % hkd_compress.EDITION)
print("limit=%s" % hkd_compress.FREE_MAX_FILE_BYTES)
print("dataset_free_bytes=%d" % os.path.getsize("dataset_free.npz"))
print("dataset_large_bytes=%d" % os.path.getsize("dataset_large.npz"))

r = hkd_compress.compress("dataset_free.npz")
print("free_result=ALLOWED")
print("free_codec=%s" % r["codec"])
d = hkd_compress.decompress("dataset_free.npz.hkd")
print("free_exact=%s" % (sha("dataset_free.npz") == sha("dataset_free.npz.dec")))

try:
    r2 = hkd_compress.compress("dataset_large.npz")
    print("large_result=ALLOWED")
except Exception as e:
    print("large_result=PAID_REQUIRED")
    print("large_error=%s" % e)
