#!/usr/bin/env python3
from __future__ import print_function

import hashlib
import os
import sys
import hkd_compress

FREE_BYTES = 5242880
LARGE_BYTES = 5242881
FREE_FILE = "dataset_free.npz"
LARGE_FILE = "dataset_large.npz"


def _sha256(path):
    h = hashlib.sha256()
    f = open(str(path), "rb")
    try:
        while True:
            block = f.read(1024 * 1024)
            if not block:
                break
            h.update(block)
    finally:
        f.close()
    return h.hexdigest()


def _value(name, default=None):
    if hasattr(hkd_compress, name):
        return getattr(hkd_compress, name)
    return default


def _remove(path):
    if path and os.path.exists(str(path)):
        os.remove(str(path))


def main():
    edition = _value("EDITION", "UNKNOWN")
    limit = _value("FREE_MAX_FILE_BYTES", None)

    print("edition=%s" % edition)
    print("limit=%s" % limit)

    free_size = os.path.getsize(FREE_FILE)
    large_size = os.path.getsize(LARGE_FILE)
    print("dataset_free_bytes=%d" % free_size)
    print("dataset_large_bytes=%d" % large_size)

    if free_size != FREE_BYTES or large_size != LARGE_BYTES:
        print("PASS=False")
        return 2

    compressed = None
    restored = None
    try:
        result = hkd_compress.compress(FREE_FILE)
        compressed = str(result["output"])
        decoded = hkd_compress.decompress(compressed)
        restored = str(decoded["output"])

        exact = _sha256(FREE_FILE) == _sha256(restored)
        print("compressed_output=%s" % compressed)
        print("compressed_bytes=%s" %
              result.get("output_bytes", os.path.getsize(compressed)))
        print("exact=%s" % exact)
        print("PASS=%s" % exact)
        return 0 if exact else 1
    except Exception as exc:
        print("PASS=False")
        print("ERROR=%s" % exc)
        return 1
    finally:
        _remove(restored)
        _remove(compressed)


if __name__ == "__main__":
    sys.exit(main())
