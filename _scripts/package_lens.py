#!/usr/bin/env python3
"""Thin shim that invokes package_data.py with 'lens' package key."""
from pathlib import Path
import runpy
import sys


if __name__ == "__main__":
    sys.argv = [sys.argv[0], "lens", *sys.argv[1:]]
    runpy.run_path(str(Path(__file__).with_name("package_data.py")), run_name="__main__")
