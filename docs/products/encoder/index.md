---
title: "编码器芯片"
description: "霍尔、AMR、TMR 与光学路线的高速高精度编码器芯片"
aside: false
pageClass: "c-page"
---

<nav class="c-crumbs"><a href="/">首页</a><i>/</i><a href="/products/">产品中心</a><i>/</i><span>编码器芯片</span></nav>

<p class="c-kicker">产品中心</p>

# 编码器芯片

<p class="c-lead">霍尔、AMR、TMR 与光学路线的高速高精度编码器芯片</p>

<div class="c-stats"><div class="c-stat"><b>7</b><span>产品系列</span></div><div class="c-stat"><b>25</b><span>份技术文档</span></div><div class="c-stat"><b>2</b><span>个产品视频</span></div></div>

编码器芯片解决的是「转到哪了」——把电机轴或旋转机构的绝对角位置变成数字量，供伺服环路闭环。衡量它的三个量是分辨率（一圈分成多少份）、精度 INL（读数与真实角度的偏差）与最高转速，三者往往不能同时拉满，选型就是在这三者与安装条件之间取舍。

本类目覆盖三种感磁路线加一条光学路线：霍尔的 <a class="c-xref" href="/products/encoder/kth78">KTH78</a>、<a class="c-xref" href="/products/encoder/kth71">KTH71</a> 胜在低延时与在轴离轴通吃；AMR 的 <a class="c-xref" href="/products/encoder/ktm52">KTM52</a>、<a class="c-xref" href="/products/encoder/ktm53">KTM53</a> 工作在饱和区（饱和磁场约 300 高斯），主要响应磁场方向而非强度，因而对磁铁加工误差与安装距离误差容忍度较高；TMR 的 <a class="c-xref" href="/products/encoder/ktm59">KTM59</a> 与细分器 <a class="c-xref" href="/products/encoder/ktm58">KTM58</a> 做到 180,000 rpm 与 30 bit；<a class="c-xref" href="/products/encoder/kto95">KTO95</a> 是光学前端，输出正弦 / 余弦供后级插值。

## 怎么选

<p class="c-sec-lead">按下面几步缩小范围。</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>先定信号来源</h3><p>自带感磁选 <a class="c-xref" href="/products/encoder/kth78">KTH78</a>、<a class="c-xref" href="/products/encoder/kth71">KTH71</a>、<a class="c-xref" href="/products/encoder/ktm52">KTM52</a>、<a class="c-xref" href="/products/encoder/ktm53">KTM53</a>、<a class="c-xref" href="/products/encoder/ktm59">KTM59</a>；已有正余弦信号用 <a class="c-xref" href="/products/encoder/ktm58">KTM58</a>。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>再按精度定档</h3><p>校准后典型值：<a class="c-xref" href="/products/encoder/kth78">KTH78</a> ±0.35°，<a class="c-xref" href="/products/encoder/kth71">KTH71</a> ±0.1°，<a class="c-xref" href="/products/encoder/ktm52">KTM52</a> ±0.015°，其余见下表。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>核对转速上限</h3><p>转速上限：<a class="c-xref" href="/products/encoder/ktm52">KTM52</a>、<a class="c-xref" href="/products/encoder/ktm53">KTM53</a> 为 60000 rpm，<a class="c-xref" href="/products/encoder/ktm58">KTM58</a>、<a class="c-xref" href="/products/encoder/ktm59">KTM59</a> 为 180,000 rpm，详见下表。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>确认安装方式</h3><p>离轴精度已给出的是 <a class="c-xref" href="/products/encoder/ktm53">KTM53</a>（±0.03°）、<a class="c-xref" href="/products/encoder/ktm59">KTM59</a>（±0.05°）与 <a class="c-xref" href="/products/encoder/kth78">KTH78</a>、<a class="c-xref" href="/products/encoder/kth71">KTH71</a>；在轴优先选 <a class="c-xref" href="/products/encoder/ktm52">KTM52</a>。</p></div></div><div class="c-feature"><span class="c-feature__no">05</span><div><h3>对上后级接口</h3><p>替代增量光电编码器看 ABZ / UVW 位数；<a class="c-xref" href="/products/encoder/ktm58">KTM58</a>、<a class="c-xref" href="/products/encoder/ktm59">KTM59</a> 支持 36M SPI。</p></div></div></div>

## 系列对照

<div class="c-table c-table--links"><table><thead><tr><th>型号</th><th>技术与安装</th><th>分辨率</th><th>精度（INL）</th><th>最高转速</th></tr></thead><tbody><tr><td><a href="/products/encoder/ktm52">KTM52 系列</a></td><td>AMR，在轴（产品页标注轴向安装）</td><td>21 bit</td><td>±0.015°（校准后典型值）</td><td>60000 rpm</td></tr><tr><td><a href="/products/encoder/ktm53">KTM53 系列</a></td><td>AMR + 垂直霍尔，离轴</td><td>21 bit</td><td>±0.03°（离轴校准后典型值）</td><td>60000 rpm</td></tr><tr><td><a href="/products/encoder/ktm58">KTM58 系列</a></td><td>细分器，接 AMR/TMR 或光编、光栅、磁栅</td><td>30 bit（单对极最高 18 bit）</td><td>±0.02°（非线性误差）</td><td>180,000 rpm</td></tr><tr><td><a href="/products/encoder/ktm59">KTM59 系列</a></td><td>TMR，在轴 / 离轴</td><td>24 bit</td><td>在轴 ±0.02°，离轴 ±0.05°</td><td>180,000 rpm</td></tr><tr><td><a href="/products/encoder/kth78">KTH78 系列</a></td><td>霍尔，在轴 / 离轴</td><td>16 bit</td><td>±0.35°（在轴）</td><td>120,000 rpm</td></tr><tr><td><a href="/products/encoder/kth71">KTH71 系列</a></td><td>霍尔，在轴 / 离轴</td><td>16 bit</td><td>在轴 ±0.1°，离轴 ±0.2°（校准后）</td><td>120,000 rpm</td></tr><tr><td><a href="/products/encoder/kto95">KTO95 系列</a></td><td>光学，3 码道游标，26 mm 码盘</td><td>24 bit（三通道 Nonius 插值）</td><td>—</td><td>—</td></tr></tbody></table></div>

## 产品系列

<p class="c-sec-lead">覆盖霍尔（<a class="c-xref" href="/products/encoder/kth78">KTH78</a>、<a class="c-xref" href="/products/encoder/kth71">KTH71</a>）、AMR（<a class="c-xref" href="/products/encoder/ktm52">KTM52</a>、<a class="c-xref" href="/products/encoder/ktm53">KTM53</a>）、TMR（<a class="c-xref" href="/products/encoder/ktm59">KTM59</a>）磁编码器，<a class="c-xref" href="/products/encoder/ktm58">KTM58</a> 细分器与 <a class="c-xref" href="/products/encoder/kto95">KTO95</a> 光学编码器，分辨率 16 ~ 30 bit。</p>

<div class="c-rows"><a class="c-row" href="/products/encoder/ktm52"><div class="c-row__media c-media--icon"><img src="/img/icons-web/ktm52.webp" alt="" loading="lazy"></div><div class="c-row__body"><span class="c-card__kicker">KTM52 系列</span><h3>21 位高精度 AMR 角度编码器</h3><p>21 位分辨率，一键自校准后 INL ±0.015°（典型值），最高 60000 rpm</p><div class="c-minispecs"><span><b>21 bit</b>分辨率</span><span><b>±0.015°（校准后典型值）</b>精度</span><span><b>60000 rpm</b>转速</span><span><b>3 ~ 5.5 V</b>电压</span></div><span class="c-card__more">查看详情</span></div></a><a class="c-row" href="/products/encoder/ktm53"><div class="c-row__media c-media--icon"><img src="/img/icons-web/ktm53.webp" alt="" loading="lazy"></div><div class="c-row__body"><span class="c-card__kicker">KTM53 系列</span><h3>离轴 AMR 角度编码器</h3><p>AMR 配合垂直霍尔与数字算法实现离轴测量，校准后 INL ±0.03°（典型值）</p><div class="c-minispecs"><span><b>21 bit</b>分辨率</span><span><b>±0.03°（离轴校准后典型值）</b>精度</span><span><b>60000 rpm</b>转速</span><span><b>3 ~ 5.5 V</b>电压</span></div><span class="c-card__more">查看详情</span></div></a><a class="c-row" href="/products/encoder/ktm58"><div class="c-row__media c-media--icon"><img src="/img/icons-web/ktm58.webp" alt="" loading="lazy"></div><div class="c-row__body"><span class="c-card__kicker">KTM58 系列</span><h3>30 bit 绝对角度细分器</h3><p>最大 4096 对极输入，30 bit 绝对角度细分，适配磁电阻与光编、光栅、磁栅</p><div class="c-minispecs"><span><b>30 bit</b>分辨率</span><span><b>±0.02°（非线性误差）</b>精度</span><span><b>180,000 rpm</b>转速</span><span><b>3 ~ 5.5 V</b>电压</span></div><span class="c-card__more">查看详情</span></div></a><a class="c-row" href="/products/encoder/ktm59"><div class="c-row__media c-media--icon"><img src="/img/icons-web/ktm59.webp" alt="" loading="lazy"></div><div class="c-row__body"><span class="c-card__kicker">KTM59 系列</span><h3>高速 TMR 磁编码器</h3><p>双 16 bit 2M SAR ADC，单对极细分 24 bit，最高 180,000 rpm</p><div class="c-minispecs"><span><b>24 bit</b>分辨率</span><span><b>±0.02°（在轴）</b>精度</span><span><b>180,000 rpm</b>转速</span><span><b>3 ~ 5.5 V</b>电压</span></div><span class="c-card__more">查看详情</span></div></a><a class="c-row" href="/products/encoder/kth78"><div class="c-row__media c-media--icon"><img src="/img/icons-web/kth78.webp" alt="" loading="lazy"></div><div class="c-row__body"><span class="c-card__kicker">KTH78 系列</span><h3>低延时霍尔绝对角度编码器</h3><p>16 位分辨率，系统延时 1 μs 并做延时补偿，全系支持在轴与离轴应用</p><div class="c-minispecs"><span><b>16 bit</b>分辨率</span><span><b>±0.35°（在轴）</b>精度</span><span><b>120,000 rpm</b>转速</span><span><b>3.3 V / 5 V</b>电压</span></div><span class="c-card__more">查看详情</span></div></a><a class="c-row" href="/products/encoder/kth71"><div class="c-row__media c-media--icon"><img src="/img/icons-web/kth71.webp" alt="" loading="lazy"></div><div class="c-row__body"><span class="c-card__kicker">KTH71 系列</span><h3>自校准霍尔磁编码器</h3><p>内置自动非线性校准（ANLC），无需复杂外部干预，在轴 INL 优于 ±0.1°</p><div class="c-minispecs"><span><b>16 bit</b>分辨率</span><span><b>±0.1°（在轴校准后）</b>精度</span><span><b>120,000 rpm</b>转速</span><span><b>3.3 V / 5 V</b>电压</span></div><span class="c-card__more">查看详情</span></div></a><a class="c-row" href="/products/encoder/kto95"><div class="c-row__media c-media--icon"><img src="/img/icons-web/kto95.webp" alt="" loading="lazy"></div><div class="c-row__body"><span class="c-card__kicker">KTO95 系列</span><h3>游标绝对值光学编码器</h3><p>集成高清相位阵列光电传感器，三通道 Nonius 插值实现最高 24 位单圈分辨率</p><div class="c-minispecs"><span><b>24 bit</b>分辨率</span><span><b>6 对模拟差分输出</b>接口</span><span><b>32-pin optoQFN</b>封装</span><span><b>4.1 ~ 5.5 V（模拟）</b>电压</span></div><span class="c-card__more">查看详情</span></div></a></div>

## 应用案例

<p class="c-sec-lead">采用编码器芯片的终端产品。</p>

<div class="c-grid c-grid--4"><a class="c-card" href="/applications/industry4/servo-motor"><div class="c-card__media c-media--case"><img src="/img/case/industry4-servo-motor.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM58xx</span><h3>伺服电机</h3></div></a><a class="c-card" href="/applications/industry4/linear-motor"><div class="c-card__media c-media--case"><img src="/img/case/industry4-linear-motor.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM58xx</span><h3>直线电机</h3></div></a><a class="c-card" href="/applications/industry4/robot-joint"><div class="c-card__media c-media--case"><img src="/img/case/industry4-robot-joint.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM59xx</span><h3>机器人关节</h3></div></a><a class="c-card" href="/applications/consumer-electronics/drone-rotor"><div class="c-card__media c-media--case"><img src="/img/case/consumer-electronics-drone-rotor.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH78xx</span><h3>无人机旋翼</h3></div></a><a class="c-card" href="/applications/industry4/bldc-motor"><div class="c-card__media c-media--case"><img src="/img/case/industry4-bldc-motor.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH78xx</span><h3>无刷直流电机</h3></div></a><a class="c-card" href="/applications/industry4/closed-loop-stepper"><div class="c-card__media c-media--case"><img src="/img/case/industry4-closed-loop-stepper.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH78xx</span><h3>步进闭环</h3></div></a><a class="c-card" href="/applications/industry4/coreless-motor"><div class="c-card__media c-media--case"><img src="/img/case/industry4-coreless-motor.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH78xx</span><h3>空心杯电机</h3></div></a><a class="c-card" href="/applications/industry4/elevator"><div class="c-card__media c-media--case"><img src="/img/case/industry4-elevator.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH78xx</span><h3>电梯</h3></div></a></div>

## 常见问题

::: details <a class="c-xref" href="/products/encoder/ktm58">KTM58</a> 和 <a class="c-xref" href="/products/encoder/ktm59">KTM59</a> 差在哪

<a class="c-xref" href="/products/encoder/ktm59">KTM59</a> 自带 TMR 感磁，直接输出 24 bit 绝对角度；<a class="c-xref" href="/products/encoder/ktm58">KTM58</a> 不感磁，需外接 AMR/TMR 或光编、光栅、磁栅的正余弦信号。

:::

::: details 自校准要做什么操作

<a class="c-xref" href="/products/encoder/ktm52">KTM52</a>、<a class="c-xref" href="/products/encoder/ktm53">KTM53</a> 为用户侧一键自校准，补偿磁铁不理想与安装偏差引入的非线性误差；<a class="c-xref" href="/products/encoder/kth71">KTH71</a> 内置 ANLC，写寄存器或引脚触发，结果存入片内 MTP。

:::

::: details 能替代增量光电编码器吗

<a class="c-xref" href="/products/encoder/ktm52">KTM52</a>、<a class="c-xref" href="/products/encoder/ktm53">KTM53</a> 的增量 ABZ 最高 65,536 脉冲/圈、UVW 1 ~ 64 对极；<a class="c-xref" href="/products/encoder/kth78">KTH78</a> 为 ABZ 4 ~ 4096 步/圈。

:::

::: details <a class="c-xref" href="/products/encoder/kto95">KTO95</a> 输出的是角度吗

不是。<a class="c-xref" href="/products/encoder/kto95">KTO95</a> 输出 6 对模拟差分正弦 / 余弦信号，由后续设备插值，具体型号经三通道 Nonius 插值可达 24 位单圈分辨率。

:::

## 其他产品线

<div class="c-grid c-grid--4"><a class="c-card" href="/products/3d-hall/"><div class="c-card__media c-media--icon"><img src="/img/icons-web/cat-3d-hall.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">2 个系列</span><h3>3D霍尔芯片</h3><p>感知 X、Y、Z 三轴磁场，用于角度与位移检测</p><span class="c-card__more">浏览产品线</span></div></a><a class="c-card" href="/products/switch/"><div class="c-card__media c-media--icon"><img src="/img/icons-web/cat-switch.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">8 个系列</span><h3>开关芯片</h3><p>霍尔、TMR、AMR 开关与线性霍尔，从微功耗到车规高压</p><span class="c-card__more">浏览产品线</span></div></a><a class="c-card" href="/products/other/"><div class="c-card__media c-media--icon"><img src="/img/icons-web/cat-other.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">1 个系列</span><h3>其他芯片</h3><p>面向传感器信号放大的零温漂高精度运放</p><span class="c-card__more">浏览产品线</span></div></a><a class="c-card" href="/products/knob/"><div class="c-card__media c-media--icon"><img src="/img/icons-web/cat-knob.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">1 个系列</span><h3>旋钮系列</h3><p>磁-电分离的磁旋钮，隔空检测角度，防水防尘 IP67</p><span class="c-card__more">浏览产品线</span></div></a></div>

<div class="c-cta"><div><h2 class="c-cta__title">需要选型建议、样品或技术支持？</h2><p>昆泰芯提供芯片选型、磁场仿真与方案设计支持，欢迎与我们的销售和技术团队联系。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
