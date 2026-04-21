# niyien-lens-data

Canonical data repository for the NiYien fork of Gyroflow. Hosts two independently versioned datasets:

- `camera_db/` — Camera sensor / distortion / frame-readout database (one JSON per vendor)
- `lens_presets/` — Lens presets (anamorphic squeeze ratio / distortion coeffs / etc.) plus `index.json`

This repository is decoupled from [NiYien/gyroflow](https://github.com/NiYien/gyroflow). The Gyroflow client fetches version information from its manifest endpoint (`www.niyien.com/api/manifest`), downloads the hot-update bundle, and activates it under `<data_dir>/lens/versions/<N>/`. Gyroflow's `src/core/build.rs` pulls `lens_presets.tar.gz` and `camera_db.tar.gz` from this repo's Releases at compile time as the built-in fallback.

## Layout

```
niyien-lens-data/
├── camera_db/             ← Camera database JSONs (canonical source)
│   ├── blackmagic.json
│   ├── canon.json
│   ├── ...   (12 vendors total)
│   └── zcam.json
├── lens_presets/          ← Lens preset JSONs + index
│   ├── index.json
│   ├── aivascope_58mm_1_50x.json
│   └── ...   (10 anamorphic presets)
├── _scripts/
│   ├── package_data.py    ← Packaging script, produces 4 artifacts
│   └── package_lens.py    ← Thin shim, equivalent to package_data.py lens
├── .github/workflows/
│   └── release.yml        ← Triggered on data-v* tag push
├── niyien-lens-data.toml  ← Packaging config
├── .gitignore
└── README.md
```

## Release artifacts

Every `data-v*` tag push triggers CI and produces four artifacts:

| Artifact | Purpose |
|---|---|
| `gyroflow-niyien-lens.cbor.gz` | Client runtime hot-update bundle (CBOR + gzip) |
| `gyroflow-niyien-lens.cbor.gz.json` | Metadata (version / sha256 / file_count) |
| `lens_presets.tar.gz` | Consumed by Gyroflow `build.rs` at compile time |
| `camera_db.tar.gz` | Consumed by Gyroflow `build.rs` at compile time |

## Release workflow

1. **Edit data**: modify or add JSONs under `camera_db/` or `lens_presets/`.
2. **Local validation** (optional):
   ```bash
   python _scripts/package_lens.py --version 1
   ls _deployment/_binaries/
   # Expect 4 artifacts + JSON metadata
   ```
3. **PR / commit**: standard git flow.
4. **Tag**:
   ```bash
   git tag data-v20260421.1
   git push origin data-v20260421.1
   ```
5. **CI auto-publish**: Actions runs `package_lens.py`, publishes the GitHub Release, and (optionally) mirrors to the domestic CDN.
6. **Update Vercel env**: note the `version` / `sha256` from the Release's `.cbor.gz.json`, then set the following env vars in the docs repo's Vercel project:
   - `NIYIEN_CONTENT_RELEASE_TAG=data-v20260421.1`
   - `NIYIEN_LENS_VERSION=<version>`
   - `NIYIEN_LENS_SHA256=<sha256>`

On next startup, clients call `fetch_manifest`, discover the new version, and auto-download.

## Compile-time tag pinning in Gyroflow

Gyroflow's `src/core/build.rs` pins a tag via the `NIYIEN_LENS_DATA_DEFAULT_TAG` constant for reproducible builds. The `NIYIEN_LENS_DATA_TAG` environment variable overrides it. To make a Gyroflow release ship with the latest data here, bump that constant in the Gyroflow release PR.

## Mirror secrets (optional)

To sync artifacts to `download.niyien.com`, configure the following secrets in this repo's GitHub Settings → Secrets:

- `NIYIEN_MIRROR_HOST`
- `NIYIEN_MIRROR_USER`
- `NIYIEN_MIRROR_KEY` (SSH private key)
- `NIYIEN_MIRROR_PATH`

Without them the mirror step is skipped automatically; GitHub Release distribution is unaffected.

## Data provenance

- `camera_db/` — Initial contents migrated from [AdrianEddy/telemetry-parser](https://github.com/AdrianEddy/telemetry-parser)'s `camera_db/` directory on 2026-04-21. Canonical source now lives here; the telemetry-parser copy is downgraded to a test fixture for that crate.
- `lens_presets/` — Initial contents migrated from `resources/anamorphic_presets/` in the NiYien Gyroflow fork on 2026-04-21, directory renamed to accommodate future non-anamorphic preset types.
