---
title: "3D霍尔芯片"
description: "感知 X、Y、Z 三轴磁场，用于角度与位移检测"
aside: false
pageClass: "c-page"
---

<nav class="c-crumbs"><a href="/">首页</a><i>/</i><a href="/products/">产品中心</a><i>/</i><span>3D霍尔芯片</span></nav>

<p class="c-kicker">产品中心</p>

# 3D霍尔芯片

<p class="c-lead">感知 X、Y、Z 三轴磁场，用于角度与位移检测</p>

<div class="c-stats"><div class="c-stat"><b>2</b><span>产品系列</span></div><div class="c-stat"><b>18</b><span>份技术文档</span></div><div class="c-stat"><b>3</b><span>个产品视频</span></div></div>

3D 霍尔芯片同时感知磁场在 X、Y、Z 三个方向的分量。相比只测单方向磁场的开关或线性霍尔，它拿到的是磁场矢量，因此可以在一颗芯片上完成 0 ~ 360° 的绝对角度、摇杆的二维偏摆或直线位移的判读，而磁铁与芯片之间不需要任何机械接触。

本类目有两条路线：<a class="c-xref" href="/products/3d-hall/kth57">KTH57</a> 系列把 X、Y、Z 三轴磁场原始数据通过 I2C / SPI 交给主控，角度或位移由用户侧软件算法提取，适合摇杆、旋钮、位移测量这类运动形式各异的场合；<a class="c-xref" href="/products/3d-hall/kth55">KTH55</a> 系列用垂直霍尔配合 16 位 ADC，直接输出 XY 平面内的绝对角度，供电 1.7 ~ 3.6 V，符合 AEC-Q100。两者工作温度均为 -40 ~ 125 ℃。

## 怎么选

<p class="c-sec-lead">按下面几步缩小范围。</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>先定角度还是磁场</h3><p>要芯片直接给 0 ~ 360° 绝对角度，选 <a class="c-xref" href="/products/3d-hall/kth55">KTH55</a>；要三轴磁场原始数据、由主控软件算运动量，选 <a class="c-xref" href="/products/3d-hall/kth57">KTH57</a>。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>再定磁铁摆放</h3><p><a class="c-xref" href="/products/3d-hall/kth57">KTH57</a> 支持在轴、离轴两种摆放，检测范围 360°；<a class="c-xref" href="/products/3d-hall/kth55">KTH55</a> 为在轴安装，最高转速 5000 rpm。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>核对供电与功耗</h3><p><a class="c-xref" href="/products/3d-hall/kth55">KTH55</a> 供电 1.7 ~ 3.6 V、电流 4 ~ 6 mA；<a class="c-xref" href="/products/3d-hall/kth57">KTH57</a> 供电 2.8 ~ 5.5 V。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>对接口与后级</h3><p>需要 AB 正交编码（最高 1024 线/圈）、PWM 或模拟电压直接进后级，选 <a class="c-xref" href="/products/3d-hall/kth55">KTH55</a>。</p></div></div><div class="c-feature"><span class="c-feature__no">05</span><div><h3>确认封装与等级</h3><p>封装：<a class="c-xref" href="/products/3d-hall/kth57">KTH57</a> QFN3x3-16L / DFN2*2.5-8L，<a class="c-xref" href="/products/3d-hall/kth55">KTH55</a> SOP-8L / DFN2×2-8L。</p></div></div></div>

## 系列对照

<div class="c-table c-table--links"><table><thead><tr><th>型号</th><th>感磁方式与安装</th><th>输出接口</th><th>分辨率与精度</th><th>供电电压</th></tr></thead><tbody><tr><td><a href="/products/3d-hall/kth57">KTH57 系列</a></td><td>三轴线性霍尔（X、Y、Z），在轴、离轴</td><td>I2C / SPI 数字输出</td><td>16 bit（输出磁场原始数据）</td><td>2.8 ~ 5.5 V</td></tr><tr><td><a href="/products/3d-hall/kth55">KTH55 系列</a></td><td>X、Y 垂直霍尔 + Z 水平霍尔，在轴</td><td>I²C、SPI、AB 正交编码、PWM、模拟电压</td><td>16 bit，角度 INL ±1°</td><td>1.7 ~ 3.6 V</td></tr></tbody></table></div>

## 产品系列

<p class="c-sec-lead">包括 <a class="c-xref" href="/products/3d-hall/kth57">KTH57</a> 三轴线性霍尔传感器与 <a class="c-xref" href="/products/3d-hall/kth55">KTH55</a> 垂直霍尔绝对角度传感器，支持 I2C、SPI 等接口，工作温度 -40 ~ 125 ℃，适用于摇杆、旋钮与位移测量。</p>

<div class="c-rows"><a class="c-row" href="/products/3d-hall/kth57"><div class="c-row__media c-media--icon"><img src="/img/icons-web/kth57.webp" alt="" loading="lazy"></div><div class="c-row__body"><span class="c-card__kicker">KTH57 系列</span><h3>三轴线性霍尔传感器</h3><p>测量 X、Y、Z 三轴磁场，I2C / SPI 可选，工作模式在线配置，兼顾性能与功耗</p><div class="c-minispecs"><span><b>16 bit</b>分辨率</span><span><b>I2C / SPI</b>接口</span><span><b>1000 Hz</b>频率</span><span><b>2.8 ~ 5.5 V</b>电压</span></div><span class="c-card__more">查看详情</span></div></a><a class="c-row" href="/products/3d-hall/kth55"><div class="c-row__media c-media--icon"><img src="/img/icons-web/kth55.webp" alt="" loading="lazy"></div><div class="c-row__body"><span class="c-card__kicker">KTH55 系列</span><h3>垂直霍尔绝对角度传感器</h3><p>垂直霍尔配合 16 位 ADC，0 ~ 360° 绝对角度输出，符合 AEC-Q100</p><div class="c-minispecs"><span><b>16 bit</b>分辨率</span><span><b>±1°（INL）</b>精度</span><span><b>5000 rpm</b>转速</span><span><b>1.7 ~ 3.6 V</b>电压</span></div><span class="c-card__more">查看详情</span></div></a></div>

## 应用案例

<p class="c-sec-lead">采用3D霍尔芯片的终端产品。</p>

<div class="c-grid c-grid--4"><a class="c-card" href="/applications/consumer-electronics/wheelchair-joystick"><div class="c-card__media c-media--case"><img src="/img/case/consumer-electronics-2.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57xx</span><h3>轮椅摇杆</h3></div></a><a class="c-card" href="/applications/consumer-electronics/washing-machine"><div class="c-card__media c-media--case"><img src="/img/case/consumer-electronics-3.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57xx</span><h3>洗衣机</h3></div></a><a class="c-card" href="/applications/consumer-electronics/handheld-joystick"><div class="c-card__media c-media--case"><img src="/img/case/consumer-electronics-5.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57xx</span><h3>掌机摇杆</h3></div></a><a class="c-card" href="/applications/consumer-electronics/smart-watch"><div class="c-card__media c-media--case"><img src="/img/case/consumer-electronics-6.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57xx</span><h3>智能手表</h3></div></a><a class="c-card" href="/applications/intelligent-life/coffee-machine"><div class="c-card__media c-media--case"><img src="/img/case/intelligent-life-0.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57xx</span><h3>咖啡机</h3></div></a><a class="c-card" href="/applications/intelligent-life/companion-robot"><div class="c-card__media c-media--case"><img src="/img/case/intelligent-life-1.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57xx</span><h3>陪伴机器人</h3></div></a><a class="c-card" href="/applications/intelligent-life/gas-stove-knob"><div class="c-card__media c-media--case"><img src="/img/case/intelligent-life-2.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57xx</span><h3>燃气灶-旋钮</h3></div></a><a class="c-card" href="/applications/intelligent-life/robot-vacuum"><div class="c-card__media c-media--case"><img src="/img/case/intelligent-life-3.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57xx</span><h3>扫地机器人-真空吸尘器</h3></div></a></div>

## 常见问题

::: details <a class="c-xref" href="/products/3d-hall/kth57">KTH57</a> 能直接读到角度吗

不能。<a class="c-xref" href="/products/3d-hall/kth57">KTH57</a> 输出 X、Y、Z 三轴磁场原始数据，运动信息由主控侧软件算法提取；要芯片直接给绝对角度请选 <a class="c-xref" href="/products/3d-hall/kth55">KTH55</a>。

:::

::: details 两颗都支持离轴安装吗

<a class="c-xref" href="/products/3d-hall/kth57">KTH57</a> 支持在轴、离轴两种磁铁摆放方式，检测范围 360°；<a class="c-xref" href="/products/3d-hall/kth55">KTH55</a> 规格为在轴安装。

:::

::: details 可测的磁场范围多大

<a class="c-xref" href="/products/3d-hall/kth57">KTH57</a> 的 XY 轴典型工作范围 ±130 mT、Z 轴 ±80 mT；<a class="c-xref" href="/products/3d-hall/kth55">KTH55</a> 的 XYZ 轴典型工作范围 ±100 mT。

:::

::: details 工作温度与车规等级

两者工作温度均为 -40 ~ 125 ℃。<a class="c-xref" href="/products/3d-hall/kth55">KTH55</a> 符合 AEC-Q100；<a class="c-xref" href="/products/3d-hall/kth57">KTH57</a> 产品手册按汽车（AQ1）、消费与工业（AQ2 / AQ3）分册。

:::

## 其他产品线

<div class="c-grid c-grid--4"><a class="c-card" href="/products/encoder/"><div class="c-card__media c-media--icon"><img src="/img/icons-web/cat-encoder.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">7 个系列</span><h3>编码器芯片</h3><p>霍尔、AMR、TMR 与光学路线的高速高精度编码器芯片</p><span class="c-card__more">浏览产品线</span></div></a><a class="c-card" href="/products/switch/"><div class="c-card__media c-media--icon"><img src="/img/icons-web/cat-switch.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">8 个系列</span><h3>开关芯片</h3><p>霍尔、TMR、AMR 开关与线性霍尔，从微功耗到车规高压</p><span class="c-card__more">浏览产品线</span></div></a><a class="c-card" href="/products/other/"><div class="c-card__media c-media--icon"><img src="/img/icons-web/cat-other.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">1 个系列</span><h3>其他芯片</h3><p>面向传感器信号放大的零温漂高精度运放</p><span class="c-card__more">浏览产品线</span></div></a><a class="c-card" href="/products/knob/"><div class="c-card__media c-media--icon"><img src="/img/icons-web/cat-knob.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">1 个系列</span><h3>旋钮系列</h3><p>磁-电分离的磁旋钮，隔空检测角度，防水防尘 IP67</p><span class="c-card__more">浏览产品线</span></div></a></div>

<div class="c-cta"><div><h2 class="c-cta__title">需要选型建议、样品或技术支持？</h2><p>昆泰芯提供芯片选型、磁场仿真与方案设计支持，欢迎与我们的销售和技术团队联系。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
