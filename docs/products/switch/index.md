---
title: "开关芯片"
description: "霍尔、TMR、AMR 开关与线性霍尔，从微功耗到车规高压"
aside: false
pageClass: "c-page"
---

<nav class="c-crumbs"><a href="/msite/">首页</a><i>/</i><a href="/msite/products/">产品中心</a><i>/</i><span>开关芯片</span></nav>

<p class="c-kicker">产品中心</p>

# 开关芯片

<p class="c-lead">霍尔、TMR、AMR 开关与线性霍尔，从微功耗到车规高压</p>

<div class="c-stats"><div class="c-stat"><b>8</b><span>产品系列</span></div><div class="c-stat"><b>35</b><span>份技术文档</span></div><div class="c-stat"><b>0</b><span>个产品视频</span></div></div>

开关芯片回答的是「到位没有」：磁铁靠近到设定阈值（BOP）时输出翻转，离开到释放点（BRP）时复位，整个过程无机械触点、无磨损。选型的核心是三件事——响应哪个方向的磁场、响应哪种磁极、以及在目标工作频率下的平均功耗。

本类目按感磁原理分成两条线：1D 霍尔开关响应垂直穿过芯片表面的磁场（KTH13/16/17 系列、KTH25），TMR 与 AMR 响应平行于芯片表面的磁场（KTM13、KTM28）；KTH462、KTH460 则在片内放多个霍尔盘，分别覆盖二维与三维磁场，不再只看单一方向。此外还收录比例式线性霍尔 KTH31 与线性霍尔 KTH564，它们输出随磁通密度线性变化的模拟电压而非开关量，用于需要读出磁场大小的场合。

## 怎么选

<p class="c-sec-lead">按下面几步缩小范围。</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>先定感磁原理</h3><p>垂直穿过芯片的磁场用霍尔的KTH13/16/17 系列、KTH25；平行磁场用 KTM13（TMR）、KTM28（AMR）。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>再定检测维度</h3><p>单方向用KTH13/16/17 系列、KTM13、KTH25；二维用 KTH462，可直接输出速度与方向；三维全极用 KTH460。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>按磁极选类型</h3><p>全极、单 S 极、单 N 极、锁存四类，KTH13/16/17 系列与 KTM13 各型号分别对应；KTH25 为双极锁存。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>核对电压与功耗</h3><p>电池供电取 KTM13（160 nA @ 3 V）或KTH13/16/17 系列（1 μA）；宽压取 KTH25。</p></div></div><div class="c-feature"><span class="c-feature__no">05</span><div><h3>需要模拟量输出</h3><p>读磁场大小而非开关量时用 KTH31（1.00 ~ 8.90 mV/Gs @ 3.3 V 六档，带宽 30 kHz）或 KTH564（1.5 ~ 13 mV/Gs）。</p></div></div></div>

## 系列对照

<div class="c-table c-table--links"><table><thead><tr><th>型号</th><th>技术与检测方式</th><th>工作电压</th><th>平均功耗</th><th>工作温度</th></tr></thead><tbody><tr><td><a href="/msite/products/switch/kth16">KTH13/16/17 系列</a></td><td>霍尔，单方向，全极 / 单极 / 锁存</td><td>1.7 ~ 5.5 V</td><td>1 μA</td><td>-40 ~ 85 / 125 ℃（视型号）</td></tr><tr><td><a href="/msite/products/switch/ktm13">KTM13 系列</a></td><td>TMR，平行磁场，全极 / 单极 / 锁存</td><td>1.8 ~ 5.5 V</td><td>160 nA @ 3 V</td><td>-40 ~ 125 ℃</td></tr><tr><td><a href="/msite/products/switch/kth25">KTH25 系列</a></td><td>霍尔，数字双极锁存，开漏高压</td><td>2.7 ~ 32 V</td><td>2.7 mA</td><td>-40 ~ 125 ℃</td></tr><tr><td><a href="/msite/products/switch/ktm28">KTM28 系列</a></td><td>AMR，水平磁场，气缸两线 / 三线</td><td>3 ~ 30 V</td><td>70 μA</td><td>-40 ~ 105 ℃</td></tr><tr><td><a href="/msite/products/switch/kth462">KTH462 系列</a></td><td>霍尔，二维锁存，两路独立输出</td><td>2.5 ~ 5.5 V</td><td>32.3 μA @ 2.5 V（30 Hz 版）</td><td>-40 ~ 125 ℃</td></tr><tr><td><a href="/msite/products/switch/kth460">KTH460 系列</a></td><td>霍尔，X、Y、Z 三维全极</td><td>2.5 ~ 5.5 V</td><td>4.5 μA @ 2.5 V（2.5 Hz 版）</td><td>-40 ~ 125 ℃</td></tr><tr><td><a href="/msite/products/switch/kth31">KTH31 系列</a></td><td>霍尔，比例式线性，模拟电压输出</td><td>3.0 ~ 5.5 V</td><td>4.5 mA @ 3.3 V</td><td>-40 ~ 125 ℃</td></tr></tbody></table></div>

## 产品系列

<p class="c-sec-lead">包括 1D/2D/3D 霍尔开关、车规级高压霍尔开关、TMR 磁阻开关、AMR 高压气缸开关及线性霍尔传感器，功耗低至 160 nA，适用于消费、工业与汽车领域。</p>

<div class="c-rows"><a class="c-row" href="/msite/products/switch/kth16"><div class="c-row__media c-media--icon"><img src="/msite/img/icons-web/kth16.webp" alt="" loading="lazy"></div><div class="c-row__body"><span class="c-card__kicker">KTH13/16/17 系列</span><h3>微功耗 1D 霍尔开关</h3><p>CMOS 工艺集成霍尔元件，1 μA 超低功耗，温度补偿优良，覆盖全极、单极与锁存型</p><div class="c-minispecs"><span><b>1.7 ~ 5.5 V</b>电压</span><span><b>1 μA</b>功耗</span><span><b>2.5 Hz ~ 40 kHz</b>频率</span><span><b>-40 ~ 85 / 125 ℃</b>温度（视型号）</span></div><span class="c-card__more">查看详情</span></div></a><a class="c-row" href="/msite/products/switch/kth25"><div class="c-row__media c-media--icon"><img src="/msite/img/icons-web/kth25.webp" alt="" loading="lazy"></div><div class="c-row__body"><span class="c-card__kicker">KTH25 系列</span><h3>车规级高压霍尔开关</h3><p>斩波技术（内置零漂移放大器），失调电压小于 10 μV，宽压工作，反接保护电压高达 -32 V</p><div class="c-minispecs"><span><b>2.7 ~ 32 V</b>电压</span><span><b>2.7 mA</b>功耗</span><span><b>30 kHz</b>频率</span><span><b>-40 ~ 125 ℃</b>温度</span></div><span class="c-card__more">查看详情</span></div></a><a class="c-row" href="/msite/products/switch/ktm13"><div class="c-row__media c-media--icon"><img src="/msite/img/icons-web/ktm13.webp" alt="" loading="lazy"></div><div class="c-row__body"><span class="c-card__kicker">KTM13 系列</span><h3>TMR 磁阻开关</h3><p>TMR 阻桥与 ASIC 单芯片集成，平行磁场感应，回差可小于 3 高斯</p><div class="c-minispecs"><span><b>1.8 ~ 5.5 V</b>电压</span><span><b>160 nA @ 3 V</b>功耗</span><span><b>最高 5000 Hz</b>频率</span><span><b>-40 ~ 125 ℃</b>温度</span></div><span class="c-card__more">查看详情</span></div></a><a class="c-row" href="/msite/products/switch/ktm28"><div class="c-row__media c-media--icon"><img src="/msite/img/icons-web/ktm28.webp" alt="" loading="lazy"></div><div class="c-row__body"><span class="c-card__kicker">KTM28 系列</span><h3>AMR 高压气缸开关</h3><p>SIP 集成 AMR 与 ASIC，支持两线 / 三线气缸位置检测，任意极性感应水平磁场</p><div class="c-minispecs"><span><b>3 ~ 30 V</b>电压</span><span><b>70 μA</b>功耗</span><span><b>4 kHz</b>频率</span><span><b>-40 ~ 105 ℃</b>温度</span></div><span class="c-card__more">查看详情</span></div></a><a class="c-row" href="/msite/products/switch/kth31"><div class="c-row__media c-media--icon"><img src="/msite/img/icons-web/kth31.webp" alt="" loading="lazy"></div><div class="c-row__body"><span class="c-card__kicker">KTH31 系列</span><h3>比例式线性霍尔传感器</h3><p>按比例响应磁通密度，30 kHz 高速带宽、轨到轨模拟输出，多灵敏度可选</p><div class="c-minispecs"><span><b>3.0 ~ 5.5 V</b>电压</span><span><b>4.5 mA @ 3.3 V</b>功耗</span><span><b>1.00 ~ 8.90 mV/Gs（@ 3.3 V）</b>灵敏度</span><span><b>-40 ~ 125 ℃</b>温度</span></div><span class="c-card__more">查看详情</span></div></a><a class="c-row" href="/msite/products/switch/kth460"><div class="c-row__media c-media--icon"><img src="/msite/img/icons-web/kth460.webp" alt="" loading="lazy"></div><div class="c-row__body"><span class="c-card__kicker">KTH460 系列</span><h3>微功耗 3D 霍尔开关</h3><p>X、Y、Z 三维全极检测，SPIN 与数字滤波技术保证稳定的工作点与开关频率</p><div class="c-minispecs"><span><b>2.5 ~ 5.5 V</b>电压</span><span><b>4.5 μA @ 2.5 V</b>功耗</span><span><b>BOP 25 Gs</b>灵敏度</span><span><b>-40 ~ 125 ℃</b>温度</span></div><span class="c-card__more">查看详情</span></div></a><a class="c-row" href="/msite/products/switch/kth462"><div class="c-row__media c-media--icon"><img src="/msite/img/icons-web/kth462.webp" alt="" loading="lazy"></div><div class="c-row__body"><span class="c-card__kicker">KTH462 系列</span><h3>超灵敏 2D 霍尔开关</h3><p>检测二维磁场，两路独立数字输出，可直接给出速度与方向或每轴独立锁存信号</p><div class="c-minispecs"><span><b>2.5 ~ 5.5 V</b>电压</span><span><b>32.3 μA @ 2.5 V</b>功耗</span><span><b>BOP 25 Gs</b>灵敏度</span><span><b>-40 ~ 125 ℃</b>温度</span></div><span class="c-card__more">查看详情</span></div></a><a class="c-row" href="/msite/products/switch/linear-hall"><div class="c-row__media c-media--icon"><img src="/msite/img/icons-web/linear-hall.webp" alt="" loading="lazy"></div><div class="c-row__body"><span class="c-card__kicker">KTH564 系列</span><h3>线性霍尔芯片</h3><p>零磁场输出 1/2 VCC，输出随磁通密度线性变化，多档灵敏度匹配不同检测范围</p><div class="c-minispecs"><span><b>2.8 ~ 6.0 V</b>电压</span><span><b>3.3 mA @ 5 V</b>功耗</span><span><b>1.5 ~ 13 mV/Gs</b>灵敏度</span><span><b>-40 ~ 125 ℃</b>温度</span></div><span class="c-card__more">查看详情</span></div></a></div>

## 应用案例

<p class="c-sec-lead">采用开关芯片的终端产品。</p>

<div class="c-grid c-grid--4"><a class="c-card" href="/msite/applications/consumer-electronics/e-chessboard"><div class="c-card__media c-media--case"><img src="/msite/img/case/consumer-electronics-1.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH1604</span><h3>电子棋盘</h3></div></a><a class="c-card" href="/msite/applications/industry4/circuit-breaker"><div class="c-card__media c-media--case"><img src="/msite/img/case/industry4-1.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH16xx</span><h3>断路器</h3></div></a><a class="c-card" href="/msite/applications/consumer-electronics/stylus"><div class="c-card__media c-media--case"><img src="/msite/img/case/consumer-electronics-0.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM13xx</span><h3>触控笔</h3></div></a><a class="c-card" href="/msite/applications/intelligent-life/robot-vacuum-water-level"><div class="c-card__media c-media--case"><img src="/msite/img/case/intelligent-life-4.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM13xx</span><h3>扫地机-水位监测</h3></div></a><a class="c-card" href="/msite/applications/intelligent-life/smart-toilet-water-level"><div class="c-card__media c-media--case"><img src="/msite/img/case/intelligent-life-10.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM13xx</span><h3>智能马桶-水位监测</h3></div></a><a class="c-card" href="/msite/applications/industry4/gas-meter"><div class="c-card__media c-media--case"><img src="/msite/img/case/industry4-2.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM13xx</span><h3>燃气表</h3></div></a><a class="c-card" href="/msite/applications/industry4/mechanical-meter"><div class="c-card__media c-media--case"><img src="/msite/img/case/industry4-5.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM13xx</span><h3>机械电表</h3></div></a><a class="c-card" href="/msite/applications/consumer-electronics/game-controller"><div class="c-card__media c-media--case"><img src="/msite/img/case/consumer-electronics-4.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH564X</span><h3>游戏手柄</h3></div></a></div>

## 常见问题

::: details 全极、单极、锁存怎么选

全极对 N、S 极都动作；单 S 极、单 N 极只响应一种极性；锁存型由一个极性置位、必须相反极性才复位，撤磁后保持原状态，因此适合旋转计数，但不能用来判断「有没有磁体」。KTH13/16/17 系列与 KTM13 各型号覆盖这四类。

:::

::: details TMR 开关与霍尔的差别

KTM13 回差可小于 3 高斯，平均功耗低至 160 nA @ 3 V，工作频率最高 5000 Hz，且感应的是平行穿过芯片的磁场而非垂直磁场。

:::

::: details 工作频率影响什么

频率决定采样间隔与平均功耗：KTH13/16/17 系列覆盖 2.5 Hz ~ 40 kHz，KTM13 提供 50 Hz、1600 Hz、5000 Hz 三档。

:::

::: details 气缸位置检测选哪颗

KTM28 以 SIP 把 AMR 与 ASIC 集成在一颗 IC 内，支持两线与三线应用，开漏输出可上拉 / 下拉负载自适应，输出过流保护 220 mA。

:::

## 其他产品线

<div class="c-grid c-grid--4"><a class="c-card" href="/msite/products/3d-hall/"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/cat-3d-hall.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">2 个系列</span><h3>3D霍尔芯片</h3><p>感知 X、Y、Z 三轴磁场，用于角度与位移检测</p><span class="c-card__more">浏览产品线</span></div></a><a class="c-card" href="/msite/products/encoder/"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/cat-encoder.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">7 个系列</span><h3>编码器芯片</h3><p>霍尔、AMR、TMR 与光学路线的高速高精度编码器芯片</p><span class="c-card__more">浏览产品线</span></div></a><a class="c-card" href="/msite/products/other/"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/cat-other.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">1 个系列</span><h3>其他芯片</h3><p>面向传感器信号放大的零温漂高精度运放</p><span class="c-card__more">浏览产品线</span></div></a><a class="c-card" href="/msite/products/knob/"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/cat-knob.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">1 个系列</span><h3>旋钮系列</h3><p>磁-电分离的磁旋钮，隔空检测角度，防水防尘 IP67</p><span class="c-card__more">浏览产品线</span></div></a></div>

<div class="c-cta"><div><h2 class="c-cta__title">需要选型建议、样品或技术支持？</h2><p>昆泰芯提供芯片选型、磁场仿真与方案设计支持，欢迎与我们的销售和技术团队联系。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/msite/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
