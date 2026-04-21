#!/usr/bin/env python3
"""
NiYien Lens Data packager.

Reads lens_presets/ and camera_db/ subdirectories, produces:
  - gyroflow-niyien-lens.cbor.gz           (client runtime hot-update)
  - gyroflow-niyien-lens.cbor.gz.json      (metadata with sha256)
  - lens_presets.tar.gz                    (gyroflow build.rs snapshot)
  - camera_db.tar.gz                       (gyroflow build.rs snapshot)

All four are produced from the same in-memory scan to guarantee consistency.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import io
import json
import sys
import tarfile
from datetime import datetime, timezone
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover (Python < 3.11)
    import tomli as tomllib


ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "niyien-lens-data.toml"
OUTPUT_DIR = ROOT / "_deployment" / "_binaries"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("package_key", choices=["lens"], nargs="?", default="lens")
    parser.add_argument(
        "--version",
        type=int,
        default=int(datetime.now(tz=timezone.utc).strftime("%Y%m%d%H%M%S")),
    )
    return parser.parse_args()


def load_config() -> dict:
    with CONFIG_PATH.open("rb") as fh:
        return tomllib.load(fh)


# -------------------- CBOR encoder (no deps) -------------------- #

def encode_cbor(value):
    if isinstance(value, dict):
        items = sorted(value.items(), key=lambda item: item[0])
        return encode_major(5, len(items)) + b"".join(
            encode_cbor(k) + encode_cbor(v) for k, v in items
        )
    if isinstance(value, list):
        return encode_major(4, len(value)) + b"".join(encode_cbor(item) for item in value)
    if isinstance(value, bytes):
        return encode_major(2, len(value)) + value
    if isinstance(value, str):
        raw = value.encode("utf-8")
        return encode_major(3, len(raw)) + raw
    if isinstance(value, int):
        if value >= 0:
            return encode_major(0, value)
        return encode_major(1, -1 - value)
    raise TypeError(f"Unsupported CBOR type: {type(value)!r}")


def encode_major(major: int, value: int) -> bytes:
    if value < 24:
        return bytes([(major << 5) | value])
    if value < 256:
        return bytes([(major << 5) | 24, value])
    if value < 65536:
        return bytes([(major << 5) | 25]) + value.to_bytes(2, "big")
    if value < 4294967296:
        return bytes([(major << 5) | 26]) + value.to_bytes(4, "big")
    return bytes([(major << 5) | 27]) + value.to_bytes(8, "big")


# -------------------- File collection -------------------- #

def collect_files(include_subdirs: list[str]) -> dict[str, bytes]:
    """Scan each subdir under repo root; produce {relative_posix_path: bytes}."""
    files: dict[str, bytes] = {}
    for subdir in include_subdirs:
        base = ROOT / subdir
        if not base.exists():
            print(f"[warn] subdir missing: {base}", file=sys.stderr)
            continue
        for path in sorted(base.rglob("*")):
            if not path.is_file():
                continue
            if path.name.lower() == "readme.md":
                continue
            rel = path.relative_to(ROOT).as_posix()
            files[rel] = path.read_bytes()
    return files


# -------------------- Tar.gz producer -------------------- #

def build_tarball(subdir: str, output_path: Path) -> dict:
    """Create a gzip-compressed tar containing <subdir>/* (paths inside tar
    start with <subdir>/), skipping README.md files."""
    base = ROOT / subdir
    buf = io.BytesIO()
    file_count = 0
    with tarfile.open(fileobj=buf, mode="w:gz", compresslevel=9) as tar:
        for path in sorted(base.rglob("*")):
            if not path.is_file():
                continue
            if path.name.lower() == "readme.md":
                continue
            arcname = path.relative_to(ROOT).as_posix()  # keep subdir/ prefix
            tar.add(path, arcname=arcname)
            file_count += 1
    compressed = buf.getvalue()
    output_path.write_bytes(compressed)
    return {
        "asset": output_path.name,
        "size": len(compressed),
        "sha256": hashlib.sha256(compressed).hexdigest(),
        "file_count": file_count,
    }


# -------------------- Main -------------------- #

def main() -> int:
    args = parse_args()
    config = load_config()
    package_config = config["data"][args.package_key]
    include_subdirs = package_config.get("include_subdirs", ["camera_db", "lens_presets"])
    extra_tarballs = package_config.get("extra_tarballs", include_subdirs)
    output_name = package_config["asset_name"]

    # 1. CBOR + gzip bundle (client runtime)
    files = collect_files(include_subdirs)
    bundle = {
        "__version": args.version,
        "__generated_at": datetime.now(tz=timezone.utc).isoformat(),
        "__package": args.package_key,
        "files": files,
    }
    encoded = encode_cbor(bundle)
    compressed = gzip.compress(encoded, compresslevel=9)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    cbor_path = OUTPUT_DIR / output_name
    cbor_path.write_bytes(compressed)

    # 2. tar.gz per subdir (gyroflow build.rs snapshot)
    tarball_meta = []
    for subdir in extra_tarballs:
        tar_path = OUTPUT_DIR / f"{subdir}.tar.gz"
        info = build_tarball(subdir, tar_path)
        tarball_meta.append(info)
        print(f"[tarball] {info['asset']}: {info['file_count']} files, "
              f"{info['size']} bytes, sha256={info['sha256'][:16]}...")

    # 3. Metadata
    metadata = {
        "package": args.package_key,
        "version": args.version,
        "asset_name": output_name,
        "size": len(compressed),
        "sha256": hashlib.sha256(compressed).hexdigest(),
        "source_dirs": include_subdirs,
        "file_count": len(files),
        "tarballs": tarball_meta,
    }
    (OUTPUT_DIR / f"{output_name}.json").write_text(
        json.dumps(metadata, indent=2), encoding="utf-8"
    )
    print(json.dumps(metadata, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
