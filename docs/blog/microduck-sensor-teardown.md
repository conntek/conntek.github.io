---
title: "一只 399 美元的「机器鸭」Microduck， 身上藏着多少颗传感器芯片？"
description: "Pollen Robotics 发布 399 美元开源双足机器人 Microduck。本文从传感器芯片角度拆解其约 20 颗以上的感知芯片，重点看 15 个关节里的磁角度传感芯片，并推演国产方案选型。"
outline: [2, 3]
pageClass: "c-page c-page--post"
---

<nav class="c-crumbs"><a href="/msite/">首页</a><i>/</i><a href="/msite/blog/">博客</a><i>/</i><span>一只 399 美元的「机器鸭」Microduck， 身上藏着多少颗传感器芯片？</span></nav>

<p class="c-kicker">行业观察</p>

# 一只 399 美元的「机器鸭」Microduck， 身上藏着多少颗传感器芯片？

<p class="c-post-meta"><span>2026-09-04</span><span>·</span><span>昆泰芯微电子</span><span>·</span><span>阅读约 10 分钟</span></p>

<p class="c-lead">Pollen Robotics 发布 399 美元开源双足机器人 Microduck。本文从传感器芯片角度拆解其约 20 颗以上的感知芯片，重点看 15 个关节里的磁角度传感芯片，并推演国产方案选型。</p>

<div class="c-takeaways"><b>本文要点</b><ul><li>按模块级估算，Microduck 约有 20 颗以上传感器/感知芯片</li><li>15 个 XL330 舵机各内置一颗非接触式绝对磁角度传感芯片</li><li>消费级双足机器人关节感知推演主选 <a class="c-xref" href="/msite/products/3d-hall/kth57">KTH5701</a></li></ul></div>

<figure class="c-blog-fig c-blog-fig--hero"><img src="/msite/blog/microduck-sensor-teardown/2.webp" alt="一只 399 美元的「机器鸭」Microduck， 身上藏着多少颗传感器芯片？"></figure>

真正决定这只鸭子「能不能站稳、会不会走路」的，不是那颗会说话的芯片，而是藏在 15 个关节里、几乎没人注意的磁角度传感芯片。

8 月 27 日，AI 开源社区 Hugging Face 旗下机器人团队 Pollen Robotics 正式发布开源双足机器人 Microduck（昵称「机器鸭」），售价 399 美元（约合人民币 2681 元）。开售 24 小时内订单金额即突破 260 万美元（约 6500 台），峰值时每 4 秒卖出一台。

一只 25 厘米高、不足 800 克、只会「卖萌」的小鸭子，凭什么引爆全球极客圈？当大家都在讨论「开源 + 强化学习」时，我们换一个更硬核的视角：从传感器芯片的角度拆解 Microduck——它身上到底有多少颗传感器芯片？这些芯片各自在忙什么？如果这类「关节感知」芯片换成国产方案，又该怎么选型？

## Microduck 硬件概况

| 项目 | 公开资料口径 |
| --- | --- |
| 尺寸 / 重量 | 高约 25 厘米，不足 800 克 |
| 形态 | 独眼双足「鸭形」，鸭嘴为可活动夹爪（可叼起约 800 克轻物） |
| 关节 | 15 个 Dynamixel XL330 智能舵机（双腿 + 颈部 + 鸭嘴等） |
| 主控 | 瑞芯微 RK3566（四核 A55），板载运行神经网络策略 |
| 控制节奏 | 50 Hz 控制环，驱动舵机执行策略输出的关节指令 |
| 感知配置 | 广角摄像头、ToF 深度/测距传感器、双 IMU、麦克风/扬声器、NFC 等 |
| 技能来源 | 行走、坐下、踢球、跌倒自恢复等行为均由 MuJoCo 仿真 + PPO 强化学习训练，导出 ONNX 后部署到真机 |
| 开源 | SDK/运行时与 RL 训练栈均以 Apache 2.0 开源（pollen-robotics/microduck 与 microduck\_rl） |

一个容易被忽略的细节是：走路这件事，本质上是「在正确的时刻，把 15 个关节转到正确的角度」。强化学习策略在每个控制周期输出 15 路关节角度指令，而策略「看」到的世界——自己现在是什么姿势、每条腿转到哪了、身体倾了多少——全部来自传感器。可以说，传感器的质量，直接决定这只鸭子学不学得会走路。

## 传感器芯片盘点

这是一个口径问题。若按「功能模块」统计（每处感知功能计 1 颗/模块），公开资料给出的硬件配置可以整理为：

| 感知环节 | 数量 | 说明（公开资料口径） |
| --- | --- | --- |
| 关节角度/位置传感 | 15 | 藏在 15 个智能舵机内部，每只舵机内置一颗非接触式绝对磁角度传感芯片 |
| 惯性测量 IMU | 2 | 陀螺仪 + 加速度计，感知身体倾角、角速度与加速度 |
| ToF 深度/测距 | 1 | 前方测距/避障、交互触发 |
| 视觉（摄像头） | 1 | 广角摄像头，用于物体/宠物/人检测与视频流 |
| 拾音（麦克风） | ≥1 | 语音交互（唱歌等），精确颗数以官方资料为准 |
| NFC 近场通信 | 2 | 公开报道称配两个 NFC 读卡器，用于配件/身份识别 |
| 合计（核心感知） | 约 20+ | 其中与「站稳、走路」直接相关的关节 + IMU 感知即达 17 颗 |

直接回答：「Microduck 有多少颗传感器芯片？」按公开资料口径，一台 Microduck 身上的传感器/感知芯片大约在 20 颗以上；其中数量最大、也最核心的一类，是 15 颗藏在关节里的「磁角度传感芯片」。（注：以上为模块级估算，精确到单板 IC 的完整清单请以官方开源 BOM 为准。）

<figure class="c-blog-fig"><img src="/msite/blog/microduck-sensor-teardown/2.webp" alt="Microduck 传感器芯片构成（模块级估算）" loading="lazy"><figcaption>Microduck 传感器芯片构成（模块级估算）</figcaption></figure>

尤其值得指出的是，Microduck 选用的 ROBOTIS Dynamixel XL330 智能舵机，官方规格明确写着其位置传感器为「非接触式绝对编码器（12 bit/360°）」——也就是说，这只鸭子的每个关节，都内置了一颗「读磁铁角度」的磁角度传感芯片，配合舵机内 Cortex-M0+ 完成 PID 位置闭环，再把位置、速度等状态回传给主控，构成强化学习的观测输入。

## 各类芯片的职责

把 Microduck 的传感器芯片按职责分为两类，就很好理解：

### 管自己的本体感知

- 15 颗关节磁角度传感芯片：上报每个关节的实际角度与运动状态。绝对角度意味着上电即知当前姿态——鸭子被推倒后，能立刻「知道」自己现在是仰是趴，从而执行跌倒自恢复策略；走路、踢球、坐下等动作的位置闭环也全靠它。
- 2 颗 IMU：感知躯干倾斜、旋转角速度与加速度，是步态平衡反馈的关键输入，双 IMU 也提供了冗余。

有媒体拆解指出，Microduck 的强化学习观测向量高达 61 维——其中绝大部分来自关节与 IMU 的本体感知。换句话说：机器人「学走路」，吃的第一口「数据」就是关节角度与姿态。

<figure class="c-blog-fig"><img src="/msite/blog/microduck-sensor-teardown/3.webp" alt="磁角度传感闭环原理示意（通用原理）" loading="lazy"><figcaption>磁角度传感闭环原理示意（通用原理）</figcaption></figure>

### 管外界的交互感知

- 摄像头 + ToF：认球、找人、检测宠物、避障与测距，让人能通过手柄/手机「看着」它玩耍；
- 麦克风/扬声器：语音交互与拟声；
- NFC：配件识别与个性化配置（例如搭配 39 美元的滚轮套件）。

两类合起来，才构成一只「既能站稳、又能互动」的完整机器鸭。而对所有双足机器人而言，最密集、最刚需的传感器芯片，永远是关节角度传感器。

## 关节感知芯片选型推演

### 关节感知芯片技术画像

<figure class="c-blog-fig"><img src="/msite/blog/microduck-sensor-teardown/4.webp" alt="单台关节芯片用量与潜在需求估算" loading="lazy"><figcaption>单台关节芯片用量与潜在需求估算</figcaption></figure>

把视角拉回产业：当「开源 + 平价 + 强化学习」把双足机器人从「数万美元的实验室设备」变成「399 美元的开发玩具」，最先受益的，正是这类藏在关节里、单价不高却用量极大的感知芯片。

而这类芯片的技术画像非常清晰，昆泰芯（CONNTEK）的产品定义与之高度吻合：

- 绝对角度、上电不丢位：跌倒自恢复、开机即动都依赖「上电就知道关节在哪」；
- 非接触、抗冲击：鸭子会摔、会自己爬起来，接触式电位器方案寿命与可靠性都不够；
- 小型化、低功耗：25 厘米机身 + 电池续航，芯片要小、要省电；
- 装配容差大、一致性好：消费级量产，磁铁装歪一点、摔过几次，角度依然要准；
- 成本敏感：399 美元整机、15 个关节，单颗芯片必须「够用就好」。

### 场景判断与选型结论

先做场景判断。Microduck 的关节感知，本质是「用一颗磁角度传感芯片读取随轴旋转的磁铁角度，输出 0 ~ 360° 绝对位置」。它的关节是低速、消费级（舵机输出轴转速约百转/分级别，控制环仅 50 Hz），最看重的是「绝对角度 + 一致性 + 成本 + 装配容差」，而非工业伺服那种 120,000 rpm 的极限转速。

再看昆泰芯产品矩阵，给出选型结论：

| 应用层次 | 推荐型号 | 判断依据 |
| --- | --- | --- |
| 消费级双足/桌面机器人关节角度反馈（本次推演主选） | <a class="c-xref" href="/msite/products/3d-hall/kth57">KTH5701</a>（<a class="c-xref" href="/msite/products/3d-hall/kth57">KTH57</a> 系列 3D 霍尔角度传感器芯片） | 3D 磁场感知、360° 绝对角度、16 bit ADC、μA 级功耗、在轴/离轴安装容差大、QFN3×3/DFN 小封装、配套径向充磁磁钢——与「读磁铁角度的关节传感芯片」场景高度契合 |
| 更高动态/工业伺服级关节 | <a class="c-xref" href="/msite/products/encoder/kth71">KTH71</a> / <a class="c-xref" href="/msite/products/encoder/kth78">KTH78</a> 系列磁编码器 | 16 bit、1 μs 低延时、ABZ/UVW 等多接口，面向高速高精度伺服 |
| 极限位置/到位检测（鸭嘴夹爪、舱门等） | <a class="c-xref" href="/msite/products/switch/ktm13/ktm1331ta">KTM1331</a> 系列 TMR 锁存开关 | 非接触到位与磁开关检测 |

在本次「给 Microduck 这类消费级双足机器人做关节感知」的推演场景下，最适合的是 <a class="c-xref" href="/msite/products/3d-hall/kth57">KTH5701</a>。

### 为什么是 KTH5701

1. 同赛道、可对标：它与 Microduck 关节舵机内置的芯片同属「磁角度传感芯片」赛道，均以非接触方式读取磁铁角度、输出绝对位置——这正是国产替代与国产方案最容易切入、也最被需要的环节；
2. 消费级机器人「够用且更好」：鸭子级关节对精度的真实要求并不苛刻（其仿真甚至把 ±1° 的齿轮背隙都建模了进去），<a class="c-xref" href="/msite/products/3d-hall/kth57">KTH5701</a> 的 ±1° 角度精度完全够用，而 3D 磁场感知带来的安装容差反而比单轴方案更适合「摔来摔去」的消费级量产；
3. 绝对角度 = 跌倒自恢复的前提：掉电不丢位、上电即可读，正好支撑「推倒了自己爬起来」这类标志性功能；
4. 低功耗契合电池机身：鸭子待机/玩耍全靠可充电电池，芯片功耗越低，续航越从容；
5. 国产供应链：批量供货、技术支持与配套磁钢一站式服务，是出海产品与国产机器人绕不开的供应链安全考量。

### KTH5701 产品特性速览

<a class="c-xref" href="/msite/products/3d-hall/kth57">KTH5701</a> 是昆泰芯 <a class="c-xref" href="/msite/products/3d-hall/kth57">KTH57</a> 系列的代表型号，一款数字输出的 3D 霍尔传感器芯片：内部集成 X、Y、Z 三轴独立霍尔感应单元并内置温度传感器，信号链采用高精度运放配合 16 bit ADC，主机可通过 SPI 或 I2C 直接读取测量数据与角度。

| 参数 | 规格 |
| --- | --- |
| 传感维度 | 3D（X/Y/Z 三轴独立霍尔）+ 内置温度传感器 |
| 角度输出 | 内置 CORDIC 算法，原生输出 XY/XZ/YZ 三平面 360° 绝对角度，无需主控运算 |
| 角度测量误差 | ±1°（@B = 40 mT），绝对位置、掉电不丢失 |
| ADC | 16 bit，XY 轴 RMS 噪声最低可至 0.01 mT |
| 磁场量程 | XY 轴 ±130 mT、Z 轴 ±80 mT（典型） |
| 工作模式/功耗 | 持续感应 61.7 μA / 唤醒睡眠 2.4 μA / 空闲低至 1.4 μA |
| 接口 | SPI 或 I2C 可选 |
| 供电 | 2.8 ~ 5.5 V，IO 供电可低至 1.8 V |
| 工作温度 | AQ2 工业级 -40 ~ 105 ℃ / AQ3 消费级 -40 ~ 85 ℃ |
| ESD（HBM） | ±5 kV |
| 封装 | QFN3×3-16L / DFN2×2.5-8L |
| 附加能力 | 磁场阈值检测与唤醒、按键/触发输出、幅值修调（在轴/离轴）、OTP 烧写 |
| 配套磁钢 | 径向 2 极充磁圆柱磁钢系列（N48H，Ø4.0 ~ Ø10.0 mm） |

六大特性回扣机器人关节需求：

- 真 3D + 原生角度输出：三轴同步采集、片上直接算好角度，主控（如 RK3566）无需再做三角函数，50 Hz 控制环读取「零负担」；
- 在轴/离轴都支持，装配容差大：加装幅值修调寄存器，磁铁装偏一点也能修正——消费级大批量组装、以及摔打后的轻微移位，都不至于让「鸭子」站不稳；
- μA 级功耗：待机 1.4 μA，让玩具级电池把更多电量留给舵机与主控；
- 16 bit ADC + 低噪声：微弱磁场也能稳定读出角度，数据不飘；
- 小封装、宽温宽压：QFN3×3 / DFN2×2.5 能塞进紧凑舵机或关节结构，-40 ~ 105 ℃ 覆盖室内外玩耍场景；
- 高可靠性：ESD ±5 kV、磁钢配套与 OTP 一次校准，量产一致性有保障。

### 推演小结

若一台「Microduck 级别」的消费级双足机器人采用昆泰芯方案做关节感知，按每关节一颗 <a class="c-xref" href="/msite/products/3d-hall/kth57">KTH5701</a> 估算，单台即 15 颗；若参考其 2 万台的销量目标，仅关节角度传感一项，对应的潜在需求即在 30 万颗量级——这还只是「关节」这一个环节。

## 全文总结

Microduck 的意义，不只是「399 美元的鸭子」。它把双足机器人的门槛从实验室拉到了极客的桌面上，也把「关节里那颗毫不起眼的磁角度传感芯片」从配角推到了聚光灯下：没有它们，再聪明的策略也不知道自己的腿在哪。

当开源生态把「算法」免费化之后，硬件里的芯片，尤其是用量大、壁垒高的感知芯片，正在成为机器人产业链上最确定的增量。作为国产传感器信号链芯片的深耕者，昆泰芯微电子（CONNTEK）将持续以 <a class="c-xref" href="/msite/products/3d-hall/kth57">KTH57</a> 系列 3D 霍尔传感器芯片、<a class="c-xref" href="/msite/products/3d-hall/kth55">KTH55</a> 系列高精度 3D 角度传感器芯片、<a class="c-xref" href="/msite/products/switch/ktm13/ktm1331ta">KTM1331</a> TMR 锁存开关芯片，以及 <a class="c-xref" href="/msite/products/encoder/kth71">KTH71</a>/KTH78/KTM52/53/KTM59 磁编码器系列芯片，为桌面机器人、双足/人形机器人、伺服关节提供「测得准、靠得住、供得上」的国产感知芯。

### 重要声明

1. 本文关于 Microduck 的产品信息（尺寸、重量、售价、销量、硬件配置、开源信息等）均来自公开新闻报道、官方产品页与开源仓库（pollen-robotics/microduck、microduck\_rl），不构成对上述信息的保证，具体以官方发布为准；
2. 文中「昆泰芯选型适配」内容为基于公开规格的假设性技术推演，用于科普与选型参考，不构成 Microduck 或任何第三方产品已采用昆泰芯芯片的事实陈述，亦不构成对任何第三方产品的贬损或替换承诺；
3. 昆泰芯型号的具体参数以正式数据手册为准。

<p class="c-post-source">本文首发于微信公众号「昆泰芯微电子」，2026-09-04。<a href="https://mp.weixin.qq.com/s/L3z812seoZr7qN7-_261bA" target="_blank" rel="noopener">查看原文</a></p>

<div class="c-grid c-grid--2"><a class="c-card" href="/msite/blog/wrc-2026-observations"><div class="c-card__body"><span class="c-card__kicker">上一篇</span><h3>从「炫技」到「干活」 2026 世界机器人大会观察</h3><span class="c-card__more">阅读</span></div></a><a class="c-card" href="/msite/blog/kto9348-launch-ciif-2026"><div class="c-card__body"><span class="c-card__kicker">下一篇</span><h3>昆泰芯 KTO9348 光编芯片将在 2026 中国国际工业博览会正式发布</h3><span class="c-card__more">阅读</span></div></a></div>

## 同栏目文章

<div class="c-grid c-grid--3"><a class="c-card" href="/msite/blog/wrc-2026-observations"><div class="c-card__media c-media--photo"><img src="/msite/blog/wrc-2026-observations/cover.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">2026-08-31</span><h3>从「炫技」到「干活」 2026 世界机器人大会观察</h3><p>2026 世界机器人大会在北京亦庄落幕，机器人正从舞台表演走向产线、仓库里的真实作业。本文回顾大会数据与产业风向，梳理关节感知的三个朴素问题，并介绍昆泰芯面向机器人的磁编码器芯片方案。</p><span class="c-card__more">阅读全文</span></div></a><a class="c-card" href="/msite/blog/physical-ai-sensing-foundation"><div class="c-card__media c-media--photo"><img src="/msite/blog/physical-ai-sensing-foundation/cover.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">2026-07-24</span><h3>感知底座筑牢物理 AI 根基：全球 AI 浪潮下昆泰芯产品价值与行业解决方案</h3><p>本文以 2026 世界人工智能大会为背景，梳理具身智能落地在关节感知、终端功耗、严苛环境与供应链上的痛点，介绍昆泰芯磁传感芯片的技术优势及其可解决的行业问题。</p><span class="c-card__more">阅读全文</span></div></a></div>

<div class="c-cta"><div><h2 class="c-cta__title">需要选型建议、样品或技术支持？</h2><p>昆泰芯提供芯片选型、磁场仿真与方案设计支持，欢迎与我们的销售和技术团队联系。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/msite/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
