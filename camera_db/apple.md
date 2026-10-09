# iPhone 12–18 metadata and readout coverage

Readout audit: **2026-10-09**. The registry contains 28 models and 67 native rear-camera lens labels. **10 models / 24 lens labels have at least one adopted readout estimate**, covering 111 model/lens/mode cells; the other 18 models still have no adopted frame-readout reference. A registry entry alone does not add automatic readout support. Identity, date and recorded equivalent focal length are parsed without a model whitelist.

## How estimates are used

The user explicitly chose to use published measurements with incomplete capture conditions as estimates for common recording modes. This replaces the previous policy of leaving every unspecified frame rate null.

- All populated values remain negative in JSON, so the existing parser reports a positive duration with `readout_estimated=true`.
- A 4K measurement without a specified frame rate is assigned to 3840×2160 at 24/25/30fps only. This is an inference, not three independently measured modes. A measured 25fps reference is also used at 24/30fps within the same model, lens and dimensions.
- High rates, alternate dimensions and Open Gate are populated only where the table below states their source or inference. There is no general scaling by frame height and no automatic fallback across table columns.
- No value is transferred to a different phone model, even when specifications look similar. No front-camera or digital-zoom focal label is mapped onto a native rear camera.
- A valid readout tag in the recording takes priority over this fallback table. These references span recording apps and capture pipelines; a matching table cell is an estimate for Blackmagic Camera footage, not validation of every codec, crop or stabilization setting.
- `null` means no adopted reference. It never means 0ms or a global shutter. Absence of an entry never prevents identity or focal metadata from being read.

## Adopted references and exact inference scope

| Source | Recorded model and lens | Published reference | Assigned database scope |
|---|---|---|---|
| [S12] | 12 Pro Max, 26mm main | Approximately 5ms in a 4K/FiLMiC Pro test; exact measurement FPS not stated | UHD 24/25/30fps inferred; no 50/60fps or other lenses |
| [S13] | 13 Pro, 26 / 13 / 77mm | 6.8 / 5 / 5ms in a 4K test; exact measurement FPS not stated | UHD 24/25/30fps inferred |
| [S14] | 14 Pro, 24 / 13 / 77mm | Approximately 9 / 7 / 6ms; author reports inconsistent individual FiLMiC Pro measurements | Rough estimates at UHD 24/25/30fps; not precision calibration |
| [B14] | 14, rear wide / 26mm | 1920×1080 BGRA, about 5.5ms at 60/120fps; 5.1µs per output row | 1080p 60/120fps; transfer from the project's capture app is estimated |
| [C15P], [C15M] | 15 Pro and 15 Pro Max, 24 / 13mm | 5.3 / 4.7ms, UHD ProRes at 25fps | Preserve measured-rate references; add 24/30fps estimates |
| [C15P], [C15M] | 15 Pro 77mm; 15 Pro Max 120mm | 5ms, UHD ProRes at 25fps | Preserve measured-rate references; add 24/30fps estimates |
| [OCB] | 15 Pro Max, 1× / 24mm | 30fps video, 1080 image rows; author extrapolates 5.25ms across 780 rows to about 7.3ms across the frame | 1920×1080 at 30fps only; native 16:9 width and transfer to this recording path inferred. Do not copy to UHD |
| [S16] | 16 Pro Max, 24mm | 2.4ms, explicitly independent of frame rate from 24–120fps | Existing UHD 24/25/30/50/60/100/120fps values retained |
| [S16] | 16 Pro Max, 13 / 120mm | 5.8 / 5.5ms; exact per-rate measurements not individually listed | Existing UHD 24/25/30/50/60fps estimates retained; 100/120fps unknown |
| [C17], [C17A] | 17 Pro, 24mm | Article says **below 3ms**; database rounds to 3ms for UHD H.265, 4224×2240 RAW and 4224×3024 RAW, all at 25fps | Use 3ms as a rounded upper-bound estimate, not an exact measured point; 24/30fps inferred at those same dimensions |
| [C17] | 17 Pro, 13mm | 6ms UHD H.265; 5.6ms 4224×2240 RAW; 7.4ms 4224×3024 RAW, at 25fps | Preserve separate dimensions; add 24/30fps estimates |
| [C17] | 17 Pro, 100mm | 5.8ms UHD H.265; 5.6ms 4224×2240 RAW; 7.5ms 4224×3024 RAW, at 25fps | Preserve separate dimensions; add 24/30fps estimates |
| [S17] | 17 Pro Max, 24mm | 2.3ms at 4224×2240 RAW, 24–60fps; 3.1ms at 4224×3024 Open Gate without separate FPS statement | Keep existing 17:9 24/25/30/50/60fps; add Open Gate 24/25/30fps estimates |
| [S18] | 18 Pro Max, 24mm | 2.3–2.4ms in typical video formats, with 4224×2240 RAW at 24–60fps explicitly described; Open Gate 4224×3024 about 3ms | Use 2.4ms for 17:9 RAW 24/25/30/50/60fps; UHD 24/25/30fps mapping inferred. Open Gate 3ms at 24/25/30fps inferred |
| [S18] | 18 Pro Max, 13 / 100mm | Approximately 6ms for each module, without individual dimension/FPS details | Infer 4224×2240 RAW at 24/25/30fps from the RAW test context. UHD, Open Gate and high-rate values remain unknown |

All 34 previously populated cells are retained. This audit adds 77 cells and five columns: Open Gate 24/30fps, and 1080p 30/60/120fps. A new column does not claim that every phone supports that recording format.

## Status of every registered model

All focal labels below are 35mm-equivalent millimetres. “No adopted reference” means the model was searched during this audit and no sufficiently attributable frame duration was found; it does not assert that no measurement exists anywhere.

| Model | Rear lens labels | Readout result and remaining gaps |
|---|---|---|
| iPhone 12 | 26 / 13 | No adopted reference. Row-time papers found; capture dimensions/lens mapping are incomplete (see below) |
| iPhone 12 mini | 26 / 13 | No adopted reference for either lens |
| iPhone 12 Pro | 26 / 13 / 52 | No adopted reference. Side Eye supplies a rear-camera row frequency, not an attributable full-frame preset |
| iPhone 12 Pro Max | 26 / 13 / 65 | Main UHD common-rate estimate [S12]; ultra-wide, telephoto and other modes unknown |
| iPhone 13 | 26 / 13 | No adopted reference for either lens |
| iPhone 13 mini | 26 / 13 | No adopted reference for either lens |
| iPhone 13 Pro | 26 / 13 / 77 | All three lenses have UHD common-rate estimates [S13]; other modes unknown |
| iPhone 13 Pro Max | 26 / 13 / 77 | No adopted reference; do not copy 13 Pro or the OCB paper's 15 Pro Max measurements |
| iPhone 14 | 26 / 13 | Main 1080p 60/120fps estimate [B14]; ultra-wide and UHD unknown |
| iPhone 14 Plus | 26 / 13 | No adopted reference for either lens |
| iPhone 14 Pro | 24 / 13 / 77 | All three lenses have rough UHD common-rate estimates [S14]; other modes unknown |
| iPhone 14 Pro Max | 24 / 13 / 77 | No adopted reference; no transfer from 14 Pro |
| iPhone 15 | 26 / 13 | No adopted reference for either lens |
| iPhone 15 Plus | 26 / 13 | No adopted reference for either lens |
| iPhone 15 Pro | 24 / 13 / 77 | All three lenses have UHD 24/25/30fps estimates [C15P]; 50/60fps and 1080p unknown |
| iPhone 15 Pro Max | 24 / 13 / 120 | All three lenses have UHD 24/25/30fps estimates [C15M]; main 1080p30 has a separate 7.3ms estimate [OCB] |
| iPhone 16 | 26 / 13 | No adopted reference for either lens |
| iPhone 16 Plus | 26 / 13 | No adopted reference for either lens |
| iPhone 16 Pro | 24 / 13 / 120 | No separately attributable reference found; no transfer from 16 Pro Max |
| iPhone 16 Pro Max | 24 / 13 / 120 | Existing UHD estimates verified [S16]; 1080p not assigned from a row-time-only paper |
| iPhone 16e | 26 | No adopted reference |
| iPhone 17 | 26 / 13 | No adopted reference for either lens |
| iPhone 17 Pro | 24 / 13 / 100 | All three lenses now have separate UHD, RAW 17:9 and Open Gate 24/25/30fps estimates [C17]; other rates unknown |
| iPhone 17 Pro Max | 24 / 13 / 100 | Main RAW 17:9 and Open Gate estimates [S17]; ultra-wide, telephoto and UHD unknown |
| iPhone 17e | 26 | No adopted reference |
| iPhone Air | 26 | No adopted reference |
| iPhone 18 Pro | 24 / 13 / 100 | No separately attributable reference found; no transfer from 18 Pro Max |
| iPhone 18 Pro Max | 24 / 13 / 100 | Main UHD/RAW/Open Gate and other lenses' RAW common-rate estimates [S18]; unlisted modes unknown |

## Investigated references not used as automatic frame durations

- **iPhone 12:** Dong et al., [Readout Time Measurement in Optical Camera Communication using Commercial LED Light Source](https://doi.org/10.1109/ICECE54449.2021.9674666), Table II, gives `1/164400 s` per row at 30fps. Encoded frame dimensions and a native lens label are not established. This is not a 0.006ms frame duration. [PLOS One's smartphone luminescence paper](https://doi.org/10.1371/journal.pone.0293740) uses the 26mm camera for still images, not a matching video preset.
- **iPhone 12 Pro:** [Side Eye](https://yanlong.site/files/oakland23-sideeye.pdf), Table IX, gives a 160kHz rear-camera row frequency at 60fps. Its illustrative 1080-row image size is insufficient to establish this specific model/lens/format combination. No guessed full-frame duration is inserted.
- **iPhone 13 Pro Max:** [Video-Based Cryptanalysis](https://eprint.iacr.org/2023/923) describes 1080p120 and a `1/61400` timing parameter but does not establish a native lens label and usable whole-frame duration for this table. In [OCB], this phone is Smartphone-B; the 7.3ms scan result belongs to Smartphone-A, the **15 Pro Max**. The paper's 3.04ms figure is an exposure estimate, not scan time.
- **iPhone 14 Pro:** [USB-NeRF](https://moyangli00.github.io/usb_nerf/docs/USB_NeRF.pdf) gives a 3.70µs scanline interval at 30Hz, without a sufficiently established native lens/encoded-height mapping here. It is not substituted for the independent rough 4K reference [S14].
- **iPhone 15 Pro Max slow motion:** [OCB] reports approximately 4.5ms while also describing 120/240fps switching and dropped frames. It is not assigned to a high-rate column; 4.5ms even exceeds a 240fps frame period.
- **iPhone 16 Pro Max:** [RollingEvidence](https://www.usenix.org/system/files/usenixsecurity25-qian.pdf), section 4, mentions about 1.7µs per row for the main camera; the mode/FPS linkage is incomplete. Do not write 0.0017ms as a frame duration or silently multiply by an arbitrary output height.
- **15 Pro / Pro Max front camera:** CineD lists 9.3ms at UHD25. The current phone parser deliberately excludes known front-camera labels from this rear-camera lookup. Supporting that measurement requires a separate lens identity path; do not disguise it as a rear-camera row.
- Hardware specifications, display PWM/response times, app preview latency, maximum FPS, and unattributed reposts are not substitutes for sensor frame-readout measurements. References for Pro/Pro Max are not reused for standard/Plus/mini/e/Air models.

## Focal length and parser scope

Blackmagic Camera's legacy model/lens suffix is 35mm equivalent. Prefer Apple's explicit `com.apple.quicktime.camera.focal_length.35mm_equivalent`, including track-level values such as `50.00mm`. Preserve `com.apple.quicktime.camera.lens_model` as a description; its physical millimetres must not become equivalent focal length. See [Apple's metadata definition](https://developer.apple.com/documentation/avfoundation/avmetadataidentifier/quicktimemetadatacamerafocallength35mmequivalent).

The encoded-width / 36 conversion remains an estimated projection, without fabricated sensor width. Missing focal metadata still permits manual equivalent-millimetre entry. New database rows do not broaden the existing Blackmagic Camera detection path to every iOS camera app or add RAW codec decoding.

The 12/13 lens labels remain sourced from Apple's [12 Pro / Pro Max announcement](https://www.apple.com/newsroom/2020/10/apple-introduces-iphone-12-pro-and-iphone-12-pro-max-with-5g/) and [13 Pro / Pro Max announcement](https://www.apple.com/au/newsroom/2021/09/apple-unveils-iphone-13-pro-and-iphone-13-pro-max-more-pro-than-ever-before/), and DXOMARK's [12 mini](https://www.dxomark.com/apple-iphone-12-mini-camera-review-performance-in-your-pocket/), [12 Pro](https://www.dxomark.com/apple-iphone-12-pro-camera-review-great-smartphone-video/), [13 mini](https://www.dxomark.com/apple-iphone-13-mini-camera-review-powerful-mobile-imaging-in-pocket-format/) and [13 Pro](https://www.dxomark.com/apple-iphone-13-pro-camera-review-outstanding-video/) camera reviews. This audit does not change any existing focal label.

## Verification

JSON validation checks all 67 rows against all 18 columns, retains all 34 prior numeric cells, and confirms that every added number uses the estimated convention. Parser metadata fixtures cover 28 models / 67 lens labels in both legacy and modern layouts (134 combinations). The authoritative-table regression checks adopted estimates and modes deliberately left unknown. `PHONE_CAMERA_DB` enables that regression; `PHONE_SAMPLE_DIR` enables the two existing 16 Pro Max original-file cases.

These checks validate data loading, matching and metadata handling. They are not recordings or optical/rolling-shutter validation from all 28 phones. This audit does not deploy a lens-data release or update an installed user's database.

[S12]: https://www.slashcam.de/artikel/Test/Apple-iPhone-12-Pro-Max---Qualitaet-der-10bit-4K-Videofunktion-inkl--Dynamik-und-Rolling-Shutter---alles-.html
[S13]: https://www.slashcam.de/artikel/Test/Apple-iPhone-13-Pro---Sensor-Qualitaet-in-4K-10-Bit-ProRes-inkl--Dynamik-und-Rolling-Shutter---alles-.html
[S14]: https://www.slashcam.de/artikel/Test/Apple-iPhone-14-Pro---Sensor-Qualitaet-in-4K-10-Bit-ProRes-inkl--Dynamik-und-Rolling-Shutter---alles-.html
[B14]: https://github.com/fedepaj/blinko/blob/main/docs/CALIBRATION.md
[C15P]: https://www.cined.com/camera-database/?camera=iPhone-15-Pro
[C15M]: https://www.cined.com/camera-database/?camera=iPhone-15-Pro-Max
[OCB]: https://doi.org/10.1109/ACCESS.2024.3462541
[S16]: https://www.slashcam.de/artikel/Test/iPhone-16-Pro-Max---Sensortest---Rolling-Shutter-und-Dynamik--alles-.html
[C17]: https://www.cined.com/camera-database/?camera=iPhone-17-Pro
[C17A]: https://www.cined.com/lab-test-of-the-iphone-17-pro-rolling-shutter-dynamic-range-trials-and-exposure-challenges/
[S17]: https://www.slashcam.de/artikel/Test/iPhone-17-Pro-Max-mit-ProRes-RAW---Rolling-Shutter-und-Dynamik-Sensortest--alles-.html
[S18]: https://www.slashcam.de/artikel/Test/iPhone-18-Pro-Max-mit-ProRes-RAW---Rolling-Shutter-und-Dynamik-Sensortest.html
