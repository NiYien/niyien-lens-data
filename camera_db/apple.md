# iPhone 12–18 metadata and readout coverage

The phone parser recognizes iPhone identity from the recording, without a model whitelist. This table explicitly covers 28 models and 67 native rear-camera lens labels: iPhone 12/mini/Pro/Pro Max; 13/mini/Pro/Pro Max; 14/Plus/Pro/Pro Max; 15/Plus/Pro/Pro Max; 16/Plus/Pro/Pro Max/16e; 17/Pro/Pro Max/17e and iPhone Air; 18 Pro/Pro Max. Apple lists the 18 Pro models in its current [model catalogue](https://support.apple.com/en-au/108044). Other iPhone names remain readable through the same parser; an absent row never prevents identity, date or focal metadata from being read.

## iPhone 12 and 13 families

These entries cover native rear-camera labels in 35mm-equivalent millimetres. They do not override focal lengths recorded in a clip.

| Model | Main | Ultra-wide | Telephoto |
|---|---|---|---|
| iPhone 12 / 12 mini | 26mm | 13mm | — |
| iPhone 12 Pro | 26mm | 13mm | 52mm |
| iPhone 12 Pro Max | 26mm | 13mm | 65mm |
| iPhone 13 / 13 mini | 26mm | 13mm | — |
| iPhone 13 Pro / 13 Pro Max | 26mm | 13mm | 77mm |

Sources: Apple's [12 Pro / Pro Max announcement](https://www.apple.com/newsroom/2020/10/apple-introduces-iphone-12-pro-and-iphone-12-pro-max-with-5g/) and [13 Pro / Pro Max announcement](https://www.apple.com/au/newsroom/2021/09/apple-unveils-iphone-13-pro-and-iphone-13-pro-max-more-pro-than-ever-before/); DXOMARK's camera reviews for [12 / 12 mini](https://www.dxomark.com/apple-iphone-12-mini-camera-review-performance-in-your-pocket/), [12 Pro](https://www.dxomark.com/apple-iphone-12-pro-camera-review-great-smartphone-video/), [13 / 13 mini](https://www.dxomark.com/apple-iphone-13-mini-camera-review-powerful-mobile-imaging-in-pocket-format/) and [13 Pro](https://www.dxomark.com/apple-iphone-13-pro-camera-review-outstanding-video/).

All 20 new rows retain null readout times: no reference with a verified matching model, lens, encoded dimensions and recording FPS was established for this addition. The [slashCAM 13 Pro test](https://www.slashcam.de/artikel/Test/Apple-iPhone-13-Pro---Sensor-Qualitaet-in-4K-10-Bit-ProRes-inkl--Dynamik-und-Rolling-Shutter---alles-.html) reports 6.8ms for the main camera and 5ms for ultra-wide and telephoto in its 4K/FiLMiC Pro investigation, but does not specify the recording FPS for those measurements. Keep these as manual references; do not assign them to automatic FPS columns or to 13 Pro Max. A recording's own readout tag still takes priority over this table.

## Focal length

Blackmagic Camera's legacy model/lens suffix is 35mm equivalent. Prefer Apple's explicit `com.apple.quicktime.camera.focal_length.35mm_equivalent` when present, including track-level values such as `50.00mm`. Preserve `com.apple.quicktime.camera.lens_model` as a description; its physical millimetres must not be interpreted as equivalent focal length. See [Apple's metadata definition](https://developer.apple.com/documentation/avfoundation/avmetadataidentifier/quicktimemetadatacamerafocallength35mmequivalent).

The encoded width / 36 conversion remains an estimated projection, with no fabricated sensor width. Missing focal metadata still allows manual equivalent-millimetre entry. Recorded digital-zoom focal lengths are not remapped to another lens's readout entry. A known front-camera label is excluded from the rear-camera table even if its equivalent focal length happens to match.

## Automatically usable readout references

All populated numbers retain the existing negative/estimated convention. Columns match encoded dimensions and recording FPS exactly; integer and NTSC-equivalent rates share a column. Null means no matching reference, not zero readout or unsupported identity. Data describes metadata handling, not a new RAW codec implementation.

| Recorded model | Lens | Mode | Reference (ms) | Source |
|---|---|---|---|---|
| 15 Pro / 15 Pro Max | 24mm / 13mm | 3840×2160, 25fps | 5.3 / 4.7 | CineD per-model tables |
| 15 Pro | 77mm | 3840×2160, 25fps | 5.0 | CineD |
| 15 Pro Max | 120mm | 3840×2160, 25fps | 5.0 | CineD |
| 16 Pro Max | 24mm | 3840×2160, 24–120fps listed columns | 2.4 | slashCAM |
| 16 Pro Max | 13mm / 120mm | 3840×2160, 24–60fps listed columns | 5.8 / 5.5 | slashCAM |
| 17 Pro | 13mm / 100mm | 3840×2160, 25fps | 6.0 / 5.8 | CineD, H.265 |
| 17 Pro | 13mm / 100mm | 4224×2240, 25fps | 5.6 / 5.6 | CineD, ProRes RAW |
| 17 Pro | 13mm / 100mm | 4224×3024, 25fps | 7.4 / 7.5 | CineD, ProRes RAW Open Gate |
| 17 Pro Max | 24mm | 4224×2240, 24–60fps listed columns | 2.3 | slashCAM, ProRes RAW |

Sources: [15 Pro](https://www.cined.com/camera-database/?camera=iPhone-15-Pro), [15 Pro Max](https://www.cined.com/camera-database/?camera=iPhone-15-Pro-Max), [16 Pro Max](https://www.slashcam.de/artikel/Test/iPhone-16-Pro-Max---Sensortest---Rolling-Shutter-und-Dynamik--alles-.html), [17 Pro](https://www.cined.com/camera-database/?camera=iPhone-17-Pro), [17 Pro Max](https://www.slashcam.de/artikel/Test/iPhone-17-Pro-Max-mit-ProRes-RAW---Rolling-Shutter-und-Dynamik-Sensortest--alles-.html).

## References deliberately not turned into automatic values

- [14 Pro](https://www.slashcam.de/artikel/Test/Apple-iPhone-14-Pro---Sensor-Qualitaet-in-4K-10-Bit-ProRes-inkl--Dynamik-und-Rolling-Shutter---alles-.html): roughly 9ms main, 7ms ultra-wide and 6ms telephoto, with inconsistent measurements in Filmic Pro. A matching recording frame rate is not established, so these remain manual calibration references; they are not copied to Blackmagic Camera modes or 14 Pro Max.
- [17 Pro article](https://www.cined.com/lab-test-of-the-iphone-17-pro-rolling-shutter-dynamic-range-trials-and-exposure-challenges/): the main camera is reported as below 3ms. The database rounds it to 3ms; an upper bound is not inserted as a measured point.
- 17 Pro Max Open Gate: the source reports 3.1ms at 4224×3024, without establishing its exact recording FPS in that passage. No automatic rate is inferred.
- No matching readout measurements were verified for the standard/Plus/e/Air models, 14 Pro Max, 16 Pro, or 18 Pro/Pro Max. Keep their rows null instead of copying another sensor. [18 Pro specifications](https://www.apple.com/iphone-18-pro/specs/) identify 24mm, 13mm and 100mm rear cameras but do not supply the corresponding scan times.
- No 1080p, front-camera, digital-zoom or additional-rate values are inferred. Source differences between Pro/Pro Max, HEVC, ProRes and RAW are preserved by the recorded model and dimensions; the populated entries are reference estimates, not a guarantee that every recording path with those dimensions is identical.

## Verification

Existing parser fixtures cover the 20 iPhone 14–18 models under both legacy and modern metadata layouts. The eight iPhone 12/13 models add database rows only and use the same parser without a model whitelist; their original recordings have not been validated. These are synthetic metadata fixtures, not recordings from all listed phones. The two original 16 Pro Max clips remain the real-file regression cases. `PHONE_CAMERA_DB` enables the authoritative-table test; `PHONE_SAMPLE_DIR` enables original-file tests.
