#!/usr/bin/env python3
"""quicksum-cli – sum numbers from the command line.

Usage:
    python3 quicksum.py 1 2 3.5
    => 6.5
"""
import sys

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    if not argv:
        print("Usage: quicksum.py <num1> <num2> ...")
        return 1
    try:
        total = sum(float(x) for x in argv)
    except ValueError as e:
        print(f"Error: {e}")
        return 2
    print(total)
    return 0

if __name__ == "__main__":
    sys.exit(main())
