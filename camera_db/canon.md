# Canon readout references

## EOS R5 Mark II: 4K SRAW in CRM

The additional `SRAW24`, `SRAW25`, `SRAW30`, `SRAW50`, and `SRAW60` values are mode-specific reference estimates for 4096 x 2160 SRAW. They are not camera-recorded timing metadata and are not a calibration of the local sample camera. Negative values retain the database's estimated-value convention.

| Recording rate | Selected reference (ms) | Evidence scope |
|---|---:|---|
| 23.976 / 23.98 / 24 | 17.3 | DPReview reports 24/30p SRAW at 17.3; 23.98 uses the same 24p class. |
| 25 | 17.3 | CineD explicitly measures 4096 x 2160 Canon SRAW at 25p. |
| 29.97 / 30 | 17.3 | DPReview explicitly measures 29.97p and groups 24/30p together. |
| 50 | 12.8 | Uses the same high-rate reference as 59.94p; slashCAM independently groups 50/60p at about 13.1. This exact 12.8 value at 50p is an estimate. |
| 59.94 / 60 | 12.8 | DPReview explicitly measures 59.94p SRAW at 12.8. |

Primary tests disagree in absolute values: slashCAM gives approximately 17.7 ms at 24/25/30p and 13.1 ms at 50/60p; Optyczne gives 15.0 ms at 25p and 11.5 ms at 50p. The choice above follows DPReview/CineD, which agree on the lower-rate reference, rather than silently averaging different test conditions. These sources establish a slower low-rate scan and a faster high-rate scan, not an exact universal readout for every firmware or Standard/Light setting. The latter is not separately calibrated by these records.

Sources checked 2026-10-14:

- [DPReview detailed video test](https://www.dpreview.com/articles/4207856702/canon-eos-r5-ii-video-detail-levels-impress/), 2024-08-09: explicit 29.97p and 59.94p SRAW measurements.
- [DPReview full review](https://www.dpreview.com/reviews/canon-eos-r5-mark-ii-review/), 2024-09-12: SRAW 24/30p and 60p table; full-width sampling.
- [CineD camera database](https://www.cined.com/camera-database/?camera=EOS-R5-Mark-II), and [lab article](https://www.cined.com/canon-eos-r5-mark-ii-lab-test-rolling-shutter-dynamic-range-and-exposure-latitude/), 2025-03-10: SRAW 25p at 17.3 ms; 9.7 ms belongs to ordinary XF-AVC/XF-HEVC 4K.
- [slashCAM original test](https://www.slashcam.de/artikel/Test/Canon-EOS-R5-II---Sensor-Bildqualitaet--Rolling-Shutter-und-SRAW-unter-der-Lupe--alles-.html), 2024-10-03: the same slower/faster timing classes for RAW and SRAW.
- [Optyczne original test](https://www.optyczne.pl/101.4-Inne_testy-Canon_EOS_R5_Mark_II_-_test_trybu_filmowego_Jako%C5%9B%C4%87_obrazu.html), 2025-03-07: lower measured results, retained here as conflicting evidence.
- [Canon recording size manual](https://cam.start.canon/en/C017/manual/html/UG-03_Shooting-2_0040.html): SRAW size/rates and image-area diagrams. Do not infer an additional sensor crop merely because SRAW has half the output dimensions of 8K RAW.

Selection requires a native CRM container, CMT CameraSettings record mode 11 and image size 147, and a 4096 x 2160 video track. The mode-specific readout lookup is limited to the matched R5 Mark II model. A native readout tag keeps priority. Missing SRAW entries, unsupported rates, invalid values, or no database leave this readout unknown rather than borrowing ordinary 4K timings. Ordinary MP4, standalone proxies, 8K RAW, other cameras, and focal/crop calculations retain their existing paths.
