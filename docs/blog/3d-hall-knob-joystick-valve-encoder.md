---
title: "一芯感知三维磁场赋能旋钮 · 摇杆 · 阀门 · 编码器全场景"
description: "KTH5701 是一款数字输出的 3D 霍尔传感器，以非接触方式替代机械电位器与接触式开关。本文介绍它的六大核心优势、关键参数、在旋钮、摇杆、阀门等场景的应用，以及配套磁钢选型。"
outline: [2, 3]
pageClass: "c-page c-page--post"
date: "2026-08-21"
ld: "{\"@context\": \"https://schema.org\", \"@type\": \"BlogPosting\", \"headline\": \"一芯感知三维磁场赋能旋钮 · 摇杆 · 阀门 · 编码器全场景\", \"description\": \"KTH5701 是一款数字输出的 3D 霍尔传感器，以非接触方式替代机械电位器与接触式开关。本文介绍它的六大核心优势、关键参数、在旋钮、摇杆、阀门等场景的应用，以及配套磁钢选型。\", \"datePublished\": \"2026-08-21\", \"dateModified\": \"2026-08-21\", \"articleSection\": \"产品解读\", \"inLanguage\": \"zh-CN\", \"image\": \"https://conntek.github.io/blog/3d-hall-knob-joystick-valve-encoder/cover.webp\", \"author\": {\"@type\": \"Organization\", \"name\": \"昆泰芯微电子\", \"alternateName\": \"CONNTEK\", \"url\": \"https://conntek.github.io/\"}, \"publisher\": {\"@type\": \"Organization\", \"name\": \"昆泰芯微电子\", \"alternateName\": \"CONNTEK\", \"url\": \"https://conntek.github.io/\"}, \"mainEntityOfPage\": \"https://conntek.github.io/blog/3d-hall-knob-joystick-valve-encoder\", \"isBasedOn\": \"https://mp.weixin.qq.com/s/fo3AxdP0dOwxVMYysE-JpQ\"}"
---

<nav class="c-crumbs"><a href="/">首页</a><i>/</i><a href="/blog/">博客</a><i>/</i><span>一芯感知三维磁场赋能旋钮 · 摇杆 · 阀门 · 编码器全场景</span></nav>

<p class="c-kicker">产品解读</p>

# 一芯感知三维磁场赋能旋钮 · 摇杆 · 阀门 · 编码器全场景

<p class="c-post-meta"><span>2026-08-21</span><span>·</span><span>昆泰芯微电子</span><span>·</span><span>阅读约 4 分钟</span></p>

<p class="c-lead"><a class="c-xref" href="/products/3d-hall/kth57">KTH5701</a> 是一款数字输出的 3D 霍尔传感器，以非接触方式替代机械电位器与接触式开关。本文介绍它的六大核心优势、关键参数、在旋钮、摇杆、阀门等场景的应用，以及配套磁钢选型。</p>

<div class="c-takeaways"><b>本文要点</b><ul><li>集成 X、Y、Z 三轴霍尔与 CORDIC，直接输出三个平面的角度</li><li>空闲状态电流 1.4 μA，适合电池与太阳能供电设备</li><li>同一颗芯片可同时检测旋钮与按键，支持在轴与离轴安装</li></ul></div>

<figure class="c-blog-fig c-blog-fig--hero"><img src="/blog/3d-hall-knob-joystick-valve-encoder/1.webp" alt="一芯感知三维磁场赋能旋钮 · 摇杆 · 阀门 · 编码器全场景"></figure>

在智能交互与精密控制的浪潮中，传统机械电位器与接触式开关正面临前所未有的挑战。游戏手柄令人抓狂的「摇杆漂移」、无人机遥控器在复杂工况下的信号跳变、户外农业灌溉阀门因粉尘潮湿环境导致的寿命骤降……机械磨损带来的精度衰减与高昂运维成本，已成为制约产品体验升级的瓶颈。

昆泰芯（CONNTEK）<a class="c-xref" href="/products/3d-hall/kth57">KTH5701</a> 系列 3D 霍尔传感器，以非接触式的底层架构创新，为消费电子、工业控制、智慧农业等领域提供了一套极具竞争力的国产化替代方案。

<figure class="c-blog-fig"><img src="/blog/3d-hall-knob-joystick-valve-encoder/1.webp" alt="KTH5701 芯片与磁铁示意渲染图" loading="lazy"><figcaption><a class="c-xref" href="/products/3d-hall/kth57">KTH5701</a> 芯片与磁铁示意渲染图</figcaption></figure>

## 产品概览

<a class="c-xref" href="/products/3d-hall/kth57">KTH5701</a> 是一款数字输出的 3D 霍尔传感器，内部集成 X、Y、Z 三轴独立霍尔感应单元，并内置温度传感器用于磁场温度补偿。信号链采用高精度运放配合 16 bit ADC 将模拟信号转换为数字输出，主机可通过 SPI 或 I2C 灵活读取测量数据。

| 器件型号 | 封装 | 封装尺寸（标称值，mm） |
| --- | --- | --- |
| <a class="c-xref" href="/products/3d-hall/kth57">KTH5701</a> | QFN3x3-16L | 3.00 × 3.00 |
| <a class="c-xref" href="/products/3d-hall/kth57">KTH5701</a> | DFN2x2.5-8L | 2.00 × 2.50 |

## 六大核心优势

### 真 3D 感知与原生角度输出

内部集成 X、Y、Z 三轴独立霍尔传感器，同步采集三维磁场信息，支持在轴与离轴安装。

内置 CORDIC 硬件算法，可直接输出 XY、XZ、YZ 三个平面的 360° 角度数据，无需主控 MCU 做三角函数运算，大幅降低系统负荷、缩短响应延迟。

角度测量误差 ±1°，支持绝对位置检测——掉电不丢失位置，上电即可读取，无需回零校准。

### μA 级超低功耗

支持持续感应、唤醒睡眠、单次测量等多种工作模式，配合可编程间歇测量，功耗表现极为出色：

| 工作模式 | 典型待机电流（μA） |
| --- | --- |
| 持续感应模式 | 61.7 |
| 唤醒睡眠模式 | 2.4 |
| 空闲状态 | 1.4 |

非常适合对电池续航敏感的便携式、可穿戴设备，以及太阳能/电池供电的农业物联网设备——静止时深度休眠，动作时快速响应。

### 16 bit 高精度 ADC

配合可配置过采样率（magnOsr / tempOsr / digCtrl），XY 轴 RMS 噪声最低可至 0.01 mT。

XY 轴典型工作范围 ±130 mT，Z 轴 ±80 mT，宽量程提升安装容错率。

内置温度传感器 + 可配置温度补偿算法，有效抑制灵敏度温漂，长期数据不漂移、不偏差。

### 旋钮与按键同时检测

支持所选平面对应的磁场阈值检测（XY/XZ/YZ 平面），同一颗芯片可同时进行旋钮、按键两种场景检测。

BUTT_OUT/TRIG 引脚可配置为按键输出（检测磁铁靠近）或 Trigger 外部触发（高电平脉冲触发单次测量），兼顾本地操作与远程控制。

### 灵活适应在轴与离轴

内置幅值修调寄存器（gainValue / gainSel），对用于角度计算的两轴磁场幅值进行修正，极大方便在轴、离轴两种常见旋钮应用，简化结构设计与生产工艺。

打破传统 2D 霍尔或 GMR 芯片必须平行安装的限制，支持平面安装或垂直安装；提供 QFN3x3-16L 与 DFN2x2.5-8L 双封装。

### 宽温宽压与高可靠性

供电电压 2.8 ~ 5.5 V，IO 供电可低至 1.8 V，兼容主流低功耗 MCU。

AQ2 工业级：-40 ~ 105 ℃；AQ3 消费级：-40 ~ 85 ℃；ESD（HBM）达 ±5 kV。

支持 OTP 烧写，关键参数一次校准、长期使用，提升量产效率。

## 关键参数速览

| 参数 | 规格 |
| --- | --- |
| 芯片供电电压 | 2.8 ~ 5.5 V |
| IO 供电电压 | 低至 1.8 V |
| XY 轴磁场线性范围 | ±130 mT（@gain=20） |
| Z 轴磁场线性范围 | ±80 mT（@gain=20） |
| ADC 分辨率 | 16 bit |
| 角度测量误差 | ±1°（@B=40 mT） |
| XY 轴 RMS 噪声 | 最低 0.01 mT |
| 通信接口 | SPI 或 I2C 可选 |
| 工作温度（AQ2 工业级） | -40 ~ 105 ℃ |
| 工作温度（AQ3 消费级） | -40 ~ 85 ℃ |
| ESD（HBM） | ±5 kV |
| 封装 | QFN3x3-16L / DFN2x2.5-8L |

## 典型应用场景

<figure class="c-blog-fig"><img src="/blog/3d-hall-knob-joystick-valve-encoder/2.webp" alt="KTH5701 典型应用场景一览" loading="lazy"><figcaption><a class="c-xref" href="/products/3d-hall/kth57">KTH5701</a> 典型应用场景一览</figcaption></figure>

游戏手柄、无人机遥控器、汽车多媒体旋钮——彻底告别摇杆漂移与电位器磨损；智能灌溉阀门——全密封防水防尘、无接触损耗、掉电位置不丢失。

## 配套磁钢选型

昆泰芯同步提供配套径向 2 极充磁圆柱磁钢系列（N48H，NiCuNi 镀层，Ø4.0 ~ Ø10.0 mm），磁场特性与 <a class="c-xref" href="/products/3d-hall/kth57">KTH5701</a> / <a class="c-xref" href="/products/3d-hall/kth57">KTH5774</a> 等 3D 霍尔角度传感器深度匹配，帮助客户快速完成磁路设计与验证，缩短开发周期。

<p class="c-post-source">本文首发于微信公众号「昆泰芯微电子」，2026-08-21。<a href="https://mp.weixin.qq.com/s/fo3AxdP0dOwxVMYysE-JpQ" target="_blank" rel="noopener">查看原文</a></p>

<div class="c-grid c-grid--2"><a class="c-card" href="/blog/kth7113-launch-dexterous-hand"><div class="c-card__body"><span class="c-card__kicker">上一篇</span><h3>2×2 塞进指尖！昆泰芯 KTH7113 超小封装 16 位磁编芯片新品发布，破解灵巧手「多关节并联」终极难题</h3><span class="c-card__more">阅读</span></div></a><a class="c-card" href="/blog/wrc-2026-observations"><div class="c-card__body"><span class="c-card__kicker">下一篇</span><h3>从「炫技」到「干活」 2026 世界机器人大会观察</h3><span class="c-card__more">阅读</span></div></a></div>

## 同栏目文章

<div class="c-grid c-grid--3"><a class="c-card" href="/blog/kth78-accuracy-and-low-latency"><div class="c-card__media c-media--photo"><img src="/img/tt/3.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">2023-11-10</span><h3>解密 KTH78 黑科技：为什么它精度高还能延迟低</h3><p>KTH78 系列磁性编码器芯片在各种外界影响下保持性能稳定，快速的响应时间几乎消除了延迟。本文介绍传感器刚性与延迟的含义、KTH78 内嵌的动态自适应滤波器（动感技术 DDDT）及其精度表现。</p><span class="c-card__more">阅读全文</span></div></a><a class="c-card" href="/blog/kth5701-off-axis"><div class="c-card__media c-media--photo"><img src="/img/tt/11.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">2023-09-15</span><h3>离轴安装：昆泰芯 KTH5701/3D 霍尔芯片，让你的创意自由驰骋！</h3><p>磁编码器芯片一般沿转轴轴线安装，采用 GMR 或 2D Hall 技术的芯片要求磁铁与芯片平行。本文以 KTH5701 三轴霍尔芯片为例，介绍磁编码器的安装方式，以及它的功能、特点与典型应用。</p><span class="c-card__more">阅读全文</span></div></a></div>

<div class="c-cta"><div><h2 class="c-cta__title">需要选型建议、样品或技术支持？</h2><p>昆泰芯提供芯片选型、磁场仿真与方案设计支持，欢迎与我们的销售和技术团队联系。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
