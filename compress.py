#!/usr/bin/env python3
import argparse
import hkd_compress

def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--compress", metavar="INPUT")
    g.add_argument("--decompress", metavar="INPUT.hkd")
    args = ap.parse_args()
    try:
        result = hkd_compress.compress(args.compress) if args.compress else hkd_compress.decompress(args.decompress)
        for k, v in result.items():
            print("%s=%s" % (k, v))
    except Exception as e:
        print("ERROR: %s" % e)
        raise SystemExit(2)

if __name__ == "__main__":
    main()
