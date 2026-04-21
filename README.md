# niyien-lens-data

NiYien fork 专用的 lens 数据仓库。承载两类独立发版的数据：

- `camera_db/` — 相机传感器 / 畸变 / 帧读取时间数据库（每个厂商一个 JSON）
- `lens_presets/` — 镜头预设（anamorphic 压缩比 / 畸变系数等）+ `index.json` 索引

本仓库与 [NiYien/gyroflow](https://github.com/NiYien/gyroflow) 解耦发版。gyroflow 客户端通过 manifest（`www.niyien.com/api/manifest`）获取最新版本号，下载热更新包并在 `<data_dir>/lens/versions/<N>/` 解压激活；gyroflow 编译期通过 `src/core/build.rs` 从本仓库 Release 下载 `lens_presets.tar.gz` 与 `camera_db.tar.gz` 作为内置快照。

## 目录结构

```
niyien-lens-data/
├── camera_db/             ← 相机数据库 JSON（canonical 源）
│   ├── blackmagic.json
│   ├── canon.json
│   ├── ...（12 家厂商）
│   └── zcam.json
├── lens_presets/          ← 镜头预设 JSON + index.json
│   ├── index.json
│   ├── aivascope_58mm_1_50x.json
│   └── ...（10 个 anamorphic 预设）
├── _scripts/
│   ├── package_data.py    ← 打包脚本，产出 4 份 artifact
│   └── package_lens.py    ← shim，等价于 package_data.py lens
├── .github/workflows/
│   └── release.yml        ← data-v* tag 触发发版
├── niyien-lens-data.toml  ← 打包配置
├── .gitignore
└── README.md
```

## 打包产物

每次 `data-v*` tag 触发 CI，产出 4 份 artifact：

| 产物 | 用途 |
|---|---|
| `gyroflow-niyien-lens.cbor.gz` | 客户端运行时热更新包（CBOR + gzip） |
| `gyroflow-niyien-lens.cbor.gz.json` | 元数据（version / sha256 / file_count） |
| `lens_presets.tar.gz` | gyroflow build.rs 编译期下载 |
| `camera_db.tar.gz` | gyroflow build.rs 编译期下载 |

## 发版流程

1. **改数据**：在 `camera_db/` 或 `lens_presets/` 修改 / 新增 JSON
2. **本地验证**（可选）：
   ```bash
   python _scripts/package_lens.py --version 1
   ls _deployment/_binaries/
   # 期望看到 4 个产物 + JSON 元数据
   ```
3. **PR / commit**：正常 git 流程
4. **打 tag**：
   ```bash
   git tag data-v20260421.1
   git push origin data-v20260421.1
   ```
5. **CI 自动发布**：Actions 运行 `package_lens.py`、发 GitHub Release、(可选) 同步国内镜像
6. **通知 Vercel**：从 Release 页面记下 `gyroflow-niyien-lens.cbor.gz.json` 的 `version` / `sha256`，填入 docs 仓库的 Vercel env：
   - `NIYIEN_CONTENT_RELEASE_TAG=data-v20260421.1`
   - `NIYIEN_LENS_VERSION=<version>`
   - `NIYIEN_LENS_SHA256=<sha256>`

客户端下次 `fetch_manifest` 时拿到新版本号，自动下载激活。

## gyroflow 编译期锁定 tag

gyroflow `src/core/build.rs` 的常量 `NIYIEN_LENS_DATA_DEFAULT_TAG` 固定一个 tag 值（保证编译可重现）；`env NIYIEN_LENS_DATA_TAG` 可覆盖。想让 gyroflow 新版本带上本仓库的最新数据，需要在 gyroflow 发版 PR 中 bump 该常量。

## 镜像 secrets（可选）

如需把产物同步到 `download.niyien.com`，在本仓库 GitHub Settings → Secrets 配置：

- `NIYIEN_MIRROR_HOST`
- `NIYIEN_MIRROR_USER`
- `NIYIEN_MIRROR_KEY`（SSH 私钥）
- `NIYIEN_MIRROR_PATH`

缺失时 workflow 自动跳过 mirror 步骤，GitHub Release 分发不受影响。

## 数据源

- `camera_db/` 初始内容来源于 [AdrianEddy/telemetry-parser](https://github.com/AdrianEddy/telemetry-parser) 的同名目录（已于 2026-04-21 迁入）。此后以本仓库为 canonical 源，telemetry-parser 那份降级为独立 crate 的 test fixture。
- `lens_presets/` 初始内容来源于 gyroflow `resources/anamorphic_presets/`（已于 2026-04-21 迁入并重命名）。未来可容纳非 anamorphic 类预设。
