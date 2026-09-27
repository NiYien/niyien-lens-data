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
- **MAVO LF:** -17ms at 3172 lines for FULL, from the 6K 17/16:9 column of [slashCAM's 2019-10-14 measurements](https://www.slashcam.de/artikel/Test/Rolling-Shutter-Werte-von-Blackmagic--Canon--Fuji--Nikon--Panasonic--Kinefinity-und-Sony--alles-.html). Height-scaled results are estimates, not independent measurements.
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
