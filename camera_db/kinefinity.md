# Kinefinity sensor geometry and readout references

The optional `models.<name>.kinefinity` object is consumed by the Kinefinity resolver in telemetry-parser. Older parsers ignore it. The historical top-level readout table remains available for older clients; it is not an independently verified set of scan-height references.

## Fields

- `sensor_size`: maximum native pixel extent, used for crop geometry and bounds. Edge 8K includes the historical 5456-line extent; newer 5288-line modes have explicit oversampling mappings. MAVO LF accepts the historical 4016-line extent as well as 3984-line recordings. Horizontal pitch is derived from `sw / sensor_size[0]`.
- `native_format`: image format for recordings that use the native width or height, allowing a unique full-sensor format to be recovered when a sidecar is absent.
- `sensor_widths`: optional manufacturer nominal physical widths for specific source widths. These rounded dimensions are not optical calibration measurements.
- `oversampling`: exact output size, recorded image format, and source sensor region. Resolve these before computing either pixel focal length or readout time. Some KineOS descriptions call a 1:1 S35 mode oversampling; those mappings retain equal source/output dimensions. An unknown oversampled mode must not fall through to native-crop geometry.
- `readout`: references with source `height`, time `ms`, and optional `format` / sensor `fps` interval. Negative `ms` uses the existing estimated-value convention. The resolver scales by source height, not output height or playback fps.

## Adopted references

- **VISTA:** -18ms at 3984 lines, applied as the user-approved constant-row-time estimate. This is a provisional reference from the publisher's description of [Rory Anderson's Cine Gear video, 2026-06-11](https://www.youtube.com/watch?v=gPf7UicN2pI), not a verified measurement of firmware 10.1.44. All derived values remain estimated. The 3840×2464 mapping uses a 1.5× source (5760×3696); the approximately corresponding 3700-line native format must not be presented as an exact source-height measurement.
- **MAVO Edge 6K:** -20.7ms at 3984 lines for FULL; -12ms at 2160 lines for S35. Source: [slashCAM's original 2022-03-29 test](https://www.slashcam.de/artikel/Test/Kinefinity-MAVO-Edge-6K---ProRes-statt-compressed-RAW--Signalverarbeitung---Rolling-Shutter---4K-Debayering.html). The article also reports approximately 16.5ms at 3172 lines and states that matching oversampled formats retain the sensor scan time. Because the S35 reference does not establish high-speed behavior, its use is conservatively restricted to sensor rates up to 60fps; other scan classes remain unknown.
- **MAVO LF:** -20ms at 3984 lines for FULL, from [slashCAM's original 2019-08-20 sensor test](https://www.slashcam.de/artikel/Test/Kinefinity-MAVO-LF---Der-Large-Format-Preisbrecher---Rolling-Shutter---4K-Debayering---Fazit.html). It explicitly measures approximately 20ms for the full 3984-line scan and approximately 16.5ms for 3240 rows, and states that matching ProRes oversampling uses the same scan time. The later 17ms overview groups 17:9 and 16:9 without an exact scan height; it must not be anchored to 3172 rows. The original full-height measurement is the more explicit basis. The rounded values imply slightly different row-time estimates, so height-scaled results remain estimates, not independent measurements of firmware 6503. Per the user's explicit rule, native S35/M43/S16 crops at sensor rates up to 60fps reuse this full-height baseline and scale linearly by the actual crop height. These are constant-row-time estimates, not separate crop-mode measurements. Higher-speed crop classes and unrecognized image formats remain unknown; no faster ADC/readout clock is inferred.
- **Other models:** retain legacy table lookup with the estimated flag. Oversampling looks up the source pixel width rather than the encoded output class. No reference height is invented for old values. MAVO still has no known readout row; sensor geometry and manual focal length remain available, while readout is unknown in automatic parsing.

## Geometry sources and limits

- [VISTA specifications](https://kinefinity.com/zh/products/vista/specs), [firmware 10.1.44](https://kinefinity.com/firmware/vista-firmware-101)
- [MAVO Edge 8K specifications](https://kinefinity.com/zh/products/mavo-edge-8k/specs)
- [MAVO Edge 6K specifications](https://kinefinity.com/products/mavo-edge-6k/specs)
- [MAVO mark2 specifications](https://kinefinity.com/zh/products/mavo-mark2/specs)
- [KineOS 8.0 recording modes](https://kinefinity.com/support/guides/kineos-8-0-notes)
- [TERRA 4K specifications](https://kinefinity.com/products/terra-4k/specs)
- [MAVO KineOS 6.0](https://kinefinity.com/firmware/mavo-kineos6p0)

Source regions are reconstructed from matching optical formats or the documented/native oversampling ratios. Encoder alignment can make the ratios non-integral, so this file must not be treated as a per-mode hardware measurement log. The 2944-wide legacy MAVO/MAVO LF mappings preserve the earlier tool's 2× sampling assumption. Update these entries when original files establish a different source region.

Do not alias VISTA to another model, copy an 18ms baseline to other sensors, infer ADC readout mode from ProRes bit depth, or infer scan time as the inverse of a mode's maximum frame rate. Missing image-format information can make the same output size ambiguous; such cases must remain unresolved rather than selecting a crop silently.

Data-package validation is provided by the parser's ignored `kinefinity::tests::authoritative_database_modes` test, with `KINEFINITY_CAMERA_DB` pointing to this directory. That test verifies mappings and calculations, not physical readout accuracy.

## FF / S35 / M43 oversampling coverage audit (2026-10-20)

Always resolve the camera model, recorded image format, and exact encoded dimensions together. FF alone does not mean oversampling: 5K crops can still be labelled FF. Resolution alone is also insufficient: identical 3K/4K/2K outputs can be a native crop in a smaller image format. A matching explicit oversampling flag keeps its existing precedence.

The eight registered models were checked against the current manufacturer recording tables and older manufacturer manuals. Twelve missing mappings were added; all 59 existing entries were preserved. A subsequent readout review replaces only MAVO LF's ambiguous -17ms-at-3172 reference with the explicit -20ms-at-3984 reference described above; the other models' readout references are unchanged:

| Model | Added modes | Evidence |
|---|---|---|
| MAVO LF | FF 3840x2672 and 2944x2000 open-gate oversampling | KineOS 6.2 release notes introduce 4K/3K open-gate oversampling for MAVO LF and MAVO. Four original firmware-6503 clips record FF, 2944x2000, 48fps in their matching slates. |
| MAVO | S35 3840x2672 and 2944x2000 open-gate oversampling | Same manufacturer KineOS 6.2 feature; the format is S35 for this sensor, not FF. No original clip was available for this model. |
| MAVO Edge 6K | Legacy FF 3840x2672, 2944x2000, 2944x1620, 2944x1200 | Manufacturer KineOS 7.0 manual, pages 44 and 46; retained alongside the newer KineOS 7.1 modes. |
| MAVO mark2 S35 | M43 2048x1080, 2048x832, 1920x1080, 1920x784 | Current manufacturer specification table. Source regions follow the matching native M43 modes. S16 with the same output remains a native crop. |
| MAVO Edge 8K, MAVO mark2 LF, TERRA 4K, VISTA | No additional missing oversampling modes found in the checked tables | Current manufacturer recording-mode tables and KineOS 8.0 notes. This is not a claim about every firmware revision. |

For the added legacy open-gate mappings, the source height is the documented 3984-line native open-gate extent, not output height multiplied by a nominal scale. Horizontal source widths of 5760 / 5888 follow the documented nominal 4K / 3K optical widths and the existing 1.5x / 2x legacy width assumptions. These reconstructed source regions are estimates, not metadata read from the clip or a new optical/scan-time calibration. The manufacturer's rounded KineOS 6.2 description says all 24M pixels; it does not establish an exact per-mode source rectangle. Do not invent 4000 / 4008 active sensor rows from encoder alignment.

For MAVO LF FF 2944x2000 this gives an estimated source of 5888x3984, crop factor 6016/5888, and pixel focal length per mm 6016/72. The revised full-height reference gives approximately 20ms, replacing the earlier 21.35ms extrapolation from an ambiguous height. This is a published measurement used as an estimate for the supplied firmware-6503 clips, not timing recorded in their MOV or slate. MAVO retains unknown readout time when no reference exists.

Readout belongs to the actual sensor scan, not the encoded raster or a fixed oversampling multiplier. For example, MAVO Edge 6K's 3840x2160 FULL mode scans 5760x3240 and estimates about 16.83ms, whereas the same 3840x2160 output in native S35 mode uses its independent 12ms-at-2160 reference. Conversely, MAVO LF native 5760x3240 and oversampled 3840x2160 share the same 5760x3240 sensor scan and estimate of about 16.27ms. Its FF 2944x2000 open-gate oversampling uses all 3984 source rows and retains the full 20ms estimate. Native M43 2944x1620 at ordinary sensor rates uses 20ms * 1620/3984, about 8.13ms; native S35 4096x2160 uses 20ms * 2160/3984, about 10.84ms. Crop scaling uses vertical scan rows, never the horizontal focal-length crop factor. An explicitly forced 2944x2000 native FULL crop estimates about 10.04ms; this is a calculation guard, not evidence that the camera offers that exact native mode. Existing independently referenced scan classes keep their own baselines. Unsupported high-speed crops remain unknown rather than extrapolating an unverified faster readout clock. Models with legacy-only timing tables still have estimates with limited mode resolution; no independent scan timings were invented for them.

Missing image format stays unresolved for ambiguous mapped outputs. Explicit non-oversampling stays a native crop. Tests cover both automatic slate parsing and manual camera selection, original MOVs with/without their matching sidecars, and all 71 data mappings. Saved projects containing older embedded geometry require re-import from the original clip; a data-table update does not rewrite them.

Sources:
- [KineOS 6.2, open-gate oversampling for MAVO / MAVO LF](https://kinefinity.com/firmware/kineos6p2)
- [MAVO LF manufacturer manual, KineOS 6.4, page 27](https://gafpagear.com/wp-content/uploads/2021/01/Operation-Manual_MAVO_LF_KineOS6.4_en.pdf#page=27)
- [MAVO Edge 6K manufacturer manual, KineOS 7.0, page 44](https://www.bhphotovideo.com/lit_files/1123257.pdf#page=44)
- [Current MAVO Edge 6K recording formats](https://kinefinity.com/products/mavo-edge-6k/specs)
- [Current MAVO mark2 S35 / LF recording formats](https://kinefinity.com/zh/products/mavo-mark2/specs)
- [Current MAVO Edge 8K recording formats](https://kinefinity.com/zh/products/mavo-edge-8k/specs)
- [TERRA 4K recording formats](https://kinefinity.com/products/terra-4k/specs)
- [VISTA recording formats](https://kinefinity.com/zh/products/vista/specs)
- [KineOS 8.0 recording formats](https://kinefinity.com/support/guides/kineos-8-0-notes)
