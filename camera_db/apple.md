# iPhone 12–18 readout fallbacks

Updated **2026-10-09**. All **28 registered models / 67 native rear-camera lens labels** now have readout fallbacks. The table has **28 mode columns / 1,016 populated cells**, with **no entirely empty lens row**. The previous 116 values are retained; 900 additional cells are explicitly requested guesses. This is complete fallback coverage for the modes declared below, not physical calibration of all phones.

## Meaning and precedence

The user clarified that missing readout speeds must receive usable estimates even when they require guessing. This supersedes the previous restriction against cross-model borrowing. Estimates must remain distinguishable from measurements in their documentation.

- Every table value is negative: the parser returns its absolute duration with `readout_estimated=true`. Even a literature-derived entry is a fallback reference, not a guarantee for every codec/crop/stabilization setting.
- A valid readout tag in the recording takes priority. This change does not override recording metadata or change production parsing code.
- Lookup remains exact for model, native rear-lens focal label, dimensions and nominal/NTSC-equivalent FPS. No runtime nearest-mode fallback or front-camera/digital-zoom remapping is introduced.
- Sources below support only the particular measurements or hardware specifications described. Sibling transfers, the generic 7ms/5ms defaults and the high-speed factor are our engineering guesses, not values published by Apple or a lab.

## Covered modes

| Scope | Dimensions | FPS columns | Rule |
|---|---|---|---|
| Every registered rear lens | 3840×2160 | 24 / 25 / 30 / 48 / 50 / 60 | UHD baseline below; retain existing entries |
| Every registered rear lens | 1920×1080 | 24 / 25 / 30 / 48 / 50 / 60 | Assume the same whole-frame scan as UHD, with the HD exceptions below |
| Main camera of every registered model | 1920×1080 | 100 / 120 | Explicit HD reference where available; otherwise guessed high-speed baseline below |
| Main camera of 16 Pro/Max, 17 Pro/Max, 18 Pro/Max | 3840×2160 | 100 / 120 | Retain the main-camera UHD baseline; transfer to an unmeasured rate is a guess |
| All three rear lenses of 17 Pro/Max and 18 Pro/Max | 4224×2240 and 4224×3024 | 24 / 25 / 30 / 48 / 50 / 60 | Separate RAW baselines below, including explicit guesses |

These columns describe the database fallback envelope. Actual mode availability still depends on camera, app, codec and firmware; this table does not enable a recording mode. Remaining null cells are outside that envelope (for example older-phone RAW and non-main-camera UHD120), not unfilled normal-mode lens rows. 720p, front cameras, digital zoom and rates not listed above are outside this change.

## UHD baselines for every model and lens

Numbers are **milliseconds**, and lens labels are 35mm-equivalent focal lengths. `Reference` identifies a published measurement for that model; extension to other rates still may be guessed. `Sibling/family` and `generic` are explicitly unmeasured fallbacks.

| Model | Main | Ultra-wide | Telephoto | Basis of the baseline |
|---|---|---|---|---|
| iPhone 12 | 26mm: 6.6 | 13mm: 5 | — | Main: assume 1080 output rows for the paper's 164.4kHz row frequency, round 6.57ms to 6.6ms, then assume unchanged whole-frame UHD scan. Ultra-wide: 13 Pro family reference. Both are guesses |
| iPhone 12 mini | 26mm: 6.6 | 13mm: 5 | — | Borrow the iPhone 12 guesses |
| iPhone 12 Pro | 26mm: 6.8 | 13mm: 5 | 52mm: 5 | Main: assume 1080 rows for Side Eye's 160kHz rear-camera row frequency, round 6.75ms to 6.8ms and assume main/UHD mapping. Other lenses: 13 Pro family reference. Guessed mapping |
| iPhone 12 Pro Max | 26mm: 5 | 13mm: 5 | 65mm: 5 | Main: reference [S12]. Other lenses: 13 Pro family reference, guessed |
| iPhone 13 | 26mm: 5 | 13mm: 5 | — | Main: older 12 Pro Max reference; ultra-wide: 13 Pro reference. Family guesses, no claim of identical scan timing |
| iPhone 13 mini | 26mm: 5 | 13mm: 5 | — | Borrow the iPhone 13 guesses |
| iPhone 13 Pro | 26mm: 6.8 | 13mm: 5 | 77mm: 5 | Reference [S13] |
| iPhone 13 Pro Max | 26mm: 6.8 | 13mm: 5 | 77mm: 5 | Sibling transfer from 13 Pro |
| iPhone 14 | 26mm: 6.8 | 13mm: 5 | — | UHD main: 13 Pro family reference; ultra-wide: older 12MP ultra-wide reference. Guesses. Use separate observed HD main value below |
| iPhone 14 Plus | 26mm: 6.8 | 13mm: 5 | — | Sibling transfer from 14, including its separate HD main reference |
| iPhone 14 Pro | 24mm: 9 | 13mm: 7 | 77mm: 6 | Rough reference [S14], which reports inconsistent individual measurements |
| iPhone 14 Pro Max | 24mm: 9 | 13mm: 7 | 77mm: 6 | Sibling transfer from 14 Pro |
| iPhone 15 | 26mm: 7 | 13mm: 5 | — | Generic non-Pro 48MP main / older 12MP ultra-wide starting values; unmeasured |
| iPhone 15 Plus | 26mm: 7 | 13mm: 5 | — | Borrow the iPhone 15 guesses |
| iPhone 15 Pro | 24mm: 5.3 | 13mm: 4.7 | 77mm: 5 | UHD25 references [C15P]; other rates transferred |
| iPhone 15 Pro Max | 24mm: 5.3 | 13mm: 4.7 | 120mm: 5 | UHD25 references [C15M]; other rates transferred. Separate HD main values below |
| iPhone 16 | 26mm: 7 | 13mm: 5 | — | Same generic non-Pro main / 12MP ultra-wide defaults as 15, not a sensor identity claim |
| iPhone 16 Plus | 26mm: 7 | 13mm: 5 | — | Borrow the iPhone 16 guesses |
| iPhone 16 Pro | 24mm: 2.4 | 13mm: 5.8 | 120mm: 5.5 | Sibling transfer from 16 Pro Max |
| iPhone 16 Pro Max | 24mm: 2.4 | 13mm: 5.8 | 120mm: 5.5 | Reference [S16]: main 24–120fps; other lenses 24–60fps, including 48fps |
| iPhone 16e | 26mm: 7 | — | — | Generic non-Pro 48MP main starting value, unmeasured |
| iPhone 17 | 26mm: 7 | 13mm: 6 | — | Main: generic non-Pro default. 48MP ultra-wide: same-generation 17 Pro reference, guessed transfer |
| iPhone 17 Pro | 24mm: 3 | 13mm: 6 | 100mm: 5.8 | UHD25 references [C17]. Main is a rounded upper-bound estimate: article says below 3ms [C17A] |
| iPhone 17 Pro Max | 24mm: 2.3 | 13mm: 6 | 100mm: 5.8 | Main: transfer its own 17:9 RAW duration [S17] to UHD. Other lenses: sibling 17 Pro values. Guesses |
| iPhone 17e | 26mm: 7 | — | — | Generic non-Pro 48MP main starting value, unmeasured |
| iPhone Air | 26mm: 7 | — | — | Generic non-Pro 48MP main starting value, unmeasured |
| iPhone 18 Pro | 24mm: 2.4 | 13mm: 6 | 100mm: 6 | Sibling transfer from 18 Pro Max; mode mapping is guessed |
| iPhone 18 Pro Max | 24mm: 2.4 | 13mm: 6 | 100mm: 6 | Reference [S18], main 2.3–2.4ms rounded to upper end; other modules about 6ms. UHD mapping and unreported rates are guessed |

The **generic 7ms main** value is a deliberately rounded starting point near the middle of the observed 5.3–9ms range of older 48MP Pro main cameras. It is not a sensor-speed prediction derived from megapixels. The **generic 5ms ultra-wide** value uses the approximate older ultra-wide reference range (4.7–5ms). These defaults have the weakest evidence and should be replaced by original-file metadata or actual measurements when available. Apple's [15](https://support.apple.com/en-us/111831), [16](https://www.apple.com/iphone-16/specs/) and [17](https://www.apple.com/iphone-17/specs/) specifications identify the camera classes, not these durations.

## HD and high-speed guesses

- For normal-rate HD, transfer the full-frame UHD baseline without halving it merely because the output height halves. This assumes downsampling of the same scan; it is unmeasured for most phones.
- **14 main:** [B14] measures 1920×1080 BGRA at about 5.5ms (5.1µs/row) for 60/120fps. Keep those entries and use 5.5ms for its other HD rates; borrow this HD baseline for 14 Plus.
- **15 Pro Max main:** [OCB] reports approximately 7.3ms at 30fps over 1080 image rows. Use 7.3ms for normal-rate HD, assuming native 16:9 dimensions and rate transfer. For HD100/120 use **4.5ms as a rough guess** from its mixed 120/240fps slow-motion experiment. The paper reports switching and dropped frames, so this is not validated high-rate calibration. Do not apply 4.5ms at 240fps: it exceeds that frame period.
- **Other main cameras at HD100/120:** choose `round(UHD_baseline × 0.8, 1)` milliseconds. **0.8 is a heuristic chosen here**, not a published universal binning factor. It supplies a concrete high-speed starting value with all assigned durations below the frame interval. No high-speed secondary-camera default is asserted.
- Existing populated values always win over these rules. In particular, the 14 main retains 5.5ms at HD120 and the 16 Pro Max main retains 2.4ms at UHD100/120.

## RAW baselines and Open Gate guesses

Each pair below is **4224×2240 / 4224×3024**, in milliseconds. Apply at 24/25/30/48/50/60fps in the declared envelope; rate transfers beyond the source's specific measurements are guesses.

| Model | 24mm main | 13mm ultra-wide | 100mm telephoto | Basis |
|---|---|---|---|---|
| 17 Pro | 3 / 3 | 5.6 / 7.4 | 5.6 / 7.5 | [C17] at 25fps; main is rounded upper bound [C17A] |
| 17 Pro Max | 2.3 / 3.1 | 5.6 / 7.4 | 5.6 / 7.5 | Main [S17]; other lenses borrowed from 17 Pro |
| 18 Pro | 2.4 / 3 | 6 / 8.1 | 6 / 8.1 | Borrowed from 18 Pro Max, including its Open Gate guesses |
| 18 Pro Max | 2.4 / 3 | 6 / 8.1 | 6 / 8.1 | Main and other modules [S18]; 17:9 mapping for secondary cameras is inferred. Secondary Open Gate is guessed as `6 × 3024 / 2240 = 8.1ms`, assuming unchanged line time |

The Open Gate height ratio is used only for these explicitly documented secondary-camera guesses. It is not added as a general parser scaling rule. This database does not implement RAW decoding or broaden the Blackmagic Camera detection path to other iOS camera apps.

## Source limits and identity checks

- [S12] reports roughly 5ms for 12 Pro Max main in a 4K/FiLMiC Pro test without a separate exact FPS statement. [S13] reports 6.8/5/5ms for 13 Pro. [S14] reports about 9/7/6ms for 14 Pro and warns of inconsistent measurements.
- [C15P]/[C15M] are UHD ProRes at 25fps. Their front-camera 9.3ms measurement is not mapped onto any rear camera. [S16] explicitly spans 24–120fps for main and 24–60fps for ultra-wide/telephoto.
- [C17] provides separate UHD/17:9/Open Gate measurements at 25fps. [S17] provides main RAW 2.3ms at 24–60fps and Open Gate 3.1ms. [S18] reports main 2.3–2.4ms / Open Gate about 3ms, with secondary modules about 6ms.
- [Row12] gives `1/164400 s` **per row**, at 30fps, without sufficient dimensions/lens mapping. [SideEye] gives 160kHz rear-camera row frequency for 12 Pro at 60fps. The 1080-row/main-camera assumptions in our baseline table are now authorized guesses, not recovered recording metadata.
- [OCB]'s scan measurements belong to Smartphone-A (**15 Pro Max**). Smartphone-B is 13 Pro Max. Its 3.04ms figure is an exposure estimate. Do not misattribute either to 13 Pro Max readout.
- [USB-NeRF] mentions 3.70µs scanline timing for 14 Pro; [RollingEvidence] mentions about 1.7µs/row for 16 Pro Max main. Neither is silently inserted as a whole-frame duration. Display response, exposure time, preview latency and maximum frame rate are different quantities.

Focal labels and the parser's equivalent-millimetre convention remain unchanged. Prefer `com.apple.quicktime.camera.focal_length.35mm_equivalent`; physical millimetres in `camera.lens_model` remain descriptive. Encoded width / 36 is an estimated projection, not a fabricated sensor width. Missing focal metadata still permits manual equivalent-millimetre entry. No additional phone model, front-camera label or digital-zoom lens is introduced by this completion.

## Verification and deployment

Structural validation checks all 67 lens rows and the declared mode envelope, preserves all previous 116 numeric cells, requires finite negative values, and confirms every duration is shorter than its assigned frame interval. The authoritative-table regression requires every lens's UHD/HD common-rate lookup and each main camera's HD100/120 fallback to succeed with the estimated flag, while checking excluded modes and known reference values. The existing metadata fixtures cover 28 models / 67 lens labels under both layouts (134 combinations).

Tests verify data loading, matching and estimation flags. The guessed values have not been validated against recordings from all phones or final stabilized footage. `PHONE_CAMERA_DB` enables the authoritative-table regression; `PHONE_SAMPLE_DIR` enables the two existing 16 Pro Max original-file cases. A lens-data release is still required to update installed users; this change alone does not publish or deploy it.

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
[Row12]: https://doi.org/10.1109/ICECE54449.2021.9674666
[SideEye]: https://yanlong.site/files/oakland23-sideeye.pdf
[USB-NeRF]: https://moyangli00.github.io/usb_nerf/docs/USB_NeRF.pdf
[RollingEvidence]: https://www.usenix.org/system/files/usenixsecurity25-qian.pdf
