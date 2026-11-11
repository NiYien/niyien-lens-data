# Sony 相机参数

## 初代 α9（ILCE-9）

2026-11-11 补充初代 α9 的常规全画幅视频参数；不适用于 α9 II 或 α9 III。

| 参数／模式 | 数据 | 依据 |
|---|---:|---|
| 传感器宽度 | 35.6mm | Sony 官方规格为 35.6×23.8mm，纠正原表的 35.9mm |
| 3840×2160，24p | 22.8ms | Horshack 原始测量 22.8209ms |
| 3840×2160，30p | 18.1ms | Horshack 原始测量 18.0861ms |
| 1920×1080，24/30/60/120p | 6.4ms | Horshack 各档原始测量为 6.4190/6.4286/6.4095/6.4190ms，按现有精度取一位小数 |
| 全画幅 UHD 30p 视角裁切 | 约 1.2× | Sony 确认仅该档视角变窄；DPReview 的初代 α9 评测给出约 1.2× |

### 来源与适用范围

- [Horshack Camera Sensor Readout Speeds](https://horshack-dpreview.github.io/RollingShutter/)：使用 500Hz 光源测量，初代 `Sony A9` 小节列出逐档条纹计数、测量高度和读出时间。本表仅采用视频测量，不采用照片电子快门的 6.6007ms。
- [Sony ILCE-9 官方规格](https://www.sony.com/electronics/support/e-mount-body-ilce-9-series/ilce-9/specifications)：传感器尺寸、UHD 24/25/30p 和 HD 24/25/30/50/60/100/120p 录制范围。
- [Sony ILCE-9 帮助指南：Record Setting (movie)](https://helpguide.sony.net/ilc/1830/v1/en/contents/TP0002375276.html)：全画幅 UHD 30p 的视角变窄；24/25p 不应用新增的 1.2× 规则。
- [DPReview：Sony a9 Full Review](https://www.dpreview.com/reviews/4934566891/sony-a9-full-review/)：初代 α9 的全宽 24p 和约 1.2× 裁切 30p。裁切系数是近似参考，不是镜头标定。
- `4K24`／`1K24`、`1K60`、`1K120` 按现有查表分组同时覆盖 PAL 的 25、50、100fps；上述测量没有单列 PAL，PAL 沿用对应扫描档参考，不代表已逐帧率、逐固件实测。
- 正数表示对应模式组有初代机型的直接视频测量参考。8K、4K 50/60/100/120/240p 和 HD 200/240p 非本机支持的录制模式，主表对应格保持 null；通用查表仍有既有低档回退，null 不构成录制模式校验。
- 未新增 APS-C/Super 35、S&Q 低速、720p 代理或外录 RAW 专用读出值，也不据此补造原片的陀螺仪、焦距或裁切状态。现有 Sony 自动回退不会识别全画幅机身的 APS-C 状态，本次不修改解析逻辑；手动选择 APS-C 的独立时序也未校准。
- 权威源仍为本仓库 `camera_db/sony.json`；应用 `resources/camera_db/` 是构建快照。发布并安装新版参数包后才会对存量用户生效，旧工程内嵌参数不会自动重写。

## FX3 读出时间

适用于 `sony.json` 中 `ILCE-FX3` 的视频读出兜底。2026-10-14 根据用户要求补齐实际录制、外录 RAW 和代理尺寸；正数表示该模式组有直接测量依据，负数表示估算。数值单位均为毫秒，负号不是扫描方向。原片内有效读出时间优先。

| 尺寸／模式 | 拍摄帧率 | 表中数值 | 依据 |
|---|---|---:|---|
| 3840×2160，常规全画幅 UHD | 23.98/24、25、29.97/30、50、59.94/60 | 9.2 | slashCAM 的 FX3 全宽 4K、24–60fps 实测组 |
| 3840×2160，UHD 高帧率 | 100、119.88/120 | 8.3 | 同一测试的 100–120fps 组 |
| 1920×1080，常规全画幅 HD | 23.98/24、25、29.97/30、50、59.94/60 | 9.2 | 同一测试明确报告 HD 与 UHD 相同 |
| 1920×1080，HD 高帧率 | 100、119.88/120 | 8.3 | 同一测试明确报告 HD 与 UHD 相同 |
| 1920×1080，S&Q 高速 | 200、239.76/240 | -4.15 | 尚无对应实测；按 120fps 参考值 8.3/2 作初值，假设高速模式扫描时间减半 |
| 4096×2160，DCI 4K | 23.98/24、25、29.97/30、48、50、59.94/60 | -9.2 | 借用常规全宽 UHD 的时序；DCI 采集区域和时序尚未单独确认 |
| 4240×2392，Video Assist BRAW | 23.98/24、25、29.97/30、50、59.94/60 | -9.2 | 借用同机全宽 UHD 时序，尚非外录 BRAW 实测 |
| 4264×2408，HDMI RAW／ProRes RAW | 23.98/24、25、29.97/30、50、59.94/60 | -9.2 | Sony 公布的 RAW 输出尺寸；读出值借用全宽 UHD，尚未单独实测 |
| 4288×2408，BRAW 编码采集尺寸 | 同上 | -9.2 | 4240×2392 原片对应的带填充采集尺寸别名，不是另一种光学模式 |
| 1280×720，机内代理 | ≤60 | -9.2 | 借用主片常规全宽扫描时间，不按代理像素高度缩放；代理自身不能确定主片的所有设置 |
| UHD／HD 的低帧率 S&Q | 1、2、3、4、6、8、12、15等低于23.98的拍摄帧率 | -9.2 | 借用常规全宽扫描时序，由 `SLOW` 条目标为估算，不用回放帧率查询 |

### 来源与边界

- [slashCAM：Der Sensor der Sony FX3 – Rolling Shutter und Debayering，2021-02-23](https://www.slashcam.de/artikel/Test/Der-Sensor-der-Sony-FX3---Rolling-Shutter-und-Debayering--alles-.html)：FX3 UHD/HD 24–60fps 约9.2ms，100–120fps 约8.3ms。正数表示有该模式组的测量参考，不代表每一固件、曝光或防抖设置都重新标定过。
- [Sony FX3 官方规格](https://www.sony.com/electronics/support/camcorders-and-video-cameras-interchangeable-lens-camcorders/ilme-fx3/specifications)：DCI/UHD/HD、S&Q及HDMI RAW录制范围。RAW输出为4264×2408，最高59.94/50p；DCI最高59.94/50p；UHD最高119.88/100p；HD的S&Q支持240/200fps。
- [Sony FX3 代理设置](https://helpguide.sony.net/ilc/2035/v1/en/contents/TP1000282137.html)：1920×1080和1280×720代理。代理尺寸本身不代表更短的传感器扫描时间。
- 用户提供的 `Video Assist_0210.braw` 和 `Video Assist_0133.braw` 均为4240×2392、50fps、采集区4288×2408，原始 `sensor_line_time` 为0。第一段已经由原始字节和Blackmagic RAW SDK交叉确认，不能将表内 -9.2 说成从原片读出的值。
- [CineD FX3 数据页](https://www.cined.com/camera-database/?camera=FX3)未测读出时间；其常见8.7ms数据属于A7S III UHD/HEVC/25fps。本次不继续把该数字作为FX3对应模式的确定测量。
- 8K及4K 200/240fps不是FX3支持的录制模式，相关主表格保持null。未增加照片模式、APS-C专属时序或数字防抖专属时序；1920×1080代理与普通HD同尺寸，只有文件记录才能进一步区分。
- 正式数据只在本仓库维护；应用的 `resources/camera_db/` 是构建快照。发布新参数包前，旧包不会自动具有这些新增条目。
- 本次新增的负数 `RES:`／`SLOW:` 覆盖值要求解析器对覆盖条目也执行“绝对值＋估算标记”的转换。旧解析器的覆盖分支会原样返回负数；发布本表前须先接入对应解析器修复，不能仅向旧客户端单独推送这份数据。
