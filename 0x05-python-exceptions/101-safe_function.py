#!/usr/bin/python3
import sys


def safe_function(fuct, *args):
    try:
        return fuct(*args)
    except Exception as e:
        print(f"Exception: {e}", file=sys.stderr)
        return None
