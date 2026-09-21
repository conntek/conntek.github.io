---
title: "SPI / SSI 串行绝对值接口 · 技术 Wiki"
description: "主控按时钟读走绝对角度的两种同步串行方式"
aside: false
pageClass: "c-page c-page--wiki"
ld: "{\"@context\": \"https://schema.org\", \"@type\": \"DefinedTerm\", \"name\": \"SPI / SSI 串行绝对值接口\", \"description\": \"主控按时钟读走绝对角度的两种同步串行方式\", \"inDefinedTermSet\": {\"@type\": \"DefinedTermSet\", \"name\": \"昆泰芯技术 Wiki\", \"url\": \"https://conntek.github.io/basics/\"}, \"url\": \"https://conntek.github.io/basics/spi-ssi\"}"
---

<nav class="c-crumbs"><a href="/">首页</a><i>/</i><a href="/basics/">技术 Wiki</a><i>/</i><span>SPI / SSI 串行绝对值接口</span></nav>

<p class="c-kicker">输出接口</p>

# SPI / SSI 串行绝对值接口

<p class="c-lead">主控按时钟读走绝对角度的两种同步串行方式</p>

## 是什么

SPI 是四线全双工（CLK、MOSI、MISO、CS），既能读角度，也能读写配置寄存器与诊断标志，适合需要在线改参数的场合。

SSI 是两线单向同步串行（CLK、DATA），从机只在时钟驱动下移出位置数据、不接受写入，接线少、时序简单，是工业伺服编码器常见的读出接口。一帧结束后数据线保持一段单稳时间（monoflop time）才允许开始下一帧，主机读取间隔不能短于它。更复杂的工业协议（例如 BiSS-C）在类似的时钟与数据线上加入了起始、应答、状态与校验等帧结构。

## 对接时要确认的东西

帧格式：位宽、位序（高位先还是低位先）、角度数据左对齐还是右对齐、状态位与错误位的位置和极性；校验：有无 CRC 以及它的参数；时序：时钟极性与相位、最高时钟速率、帧间最小间隔。

即便都叫「标准协议」，不同设备的位定义、校验参数也可能不同。拿到逐位定义表与校验参数再开始写主机代码，比先看波形再猜省时间。

## 读取时刻与现场可靠性

串行口读到的角度属于某个采样时刻，这个时刻由帧结构与主机软件决定。用软件 GPIO 拉片选、两帧之间被任务调度切开、多颗器件轮询，都会让采样时刻不固定。对时间敏感的闭环，应在固定中断里、与电流采样对齐地读取。

外接线较长、靠近电机时，要区分两类问题：**误码**（重新上电能恢复）属于信号完整性，靠缩短走线、降低速率、差分传输、改善地线解决；**端口损坏**（重新上电不能恢复）属于静电或浪涌，改通信参数无效，必须加 TVS 等外部保护。

::: tip 要点提示
高速读取时要核对一帧里的位序与对齐方式，以及是否带 CRC 校验位；总线可用速率还受线缆长度与驱动能力限制。
:::

## 常见误区

<p class="c-sec-lead">每条标题是常听到的说法，下方是工程上的实际情况。</p>

<div class="c-features c-pitfalls"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>标准协议即插即用</h3><p>帧骨架是标准的，位定义、状态位极性与校验参数常常各家不同，要单独索取文档。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>SPI 读到的就是此刻的角度</h3><p>读到的是某个采样时刻的值，这个时刻由帧时序和主机软件决定，高速下要算进延时。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>芯片有内置 ESD 保护，现场不用再加</h3><p>内置保护是按标准测试模型给出的器件级数值，电机附近的外接接口通常仍需要外部保护器件。</p></div></div></div>

## 相关系列

<p class="c-sec-lead">正文涉及的原理与指标，在这些产品系列上用得到。</p>

<div class="c-grid c-grid--3"><a class="c-card" href="/products/3d-hall/kth57"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth57.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57 系列</span><h3>三轴线性霍尔传感器</h3><p>测量 X、Y、Z 三轴磁场，I2C / SPI 可选，工作模式在线配置，兼顾性能与功耗</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/3d-hall/kth55"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth55.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH55 系列</span><h3>垂直霍尔绝对角度传感器</h3><p>垂直霍尔配合 16 位 ADC，0 ~ 360° 绝对角度输出，符合 AEC-Q100</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/encoder/ktm52"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm52.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM52 系列</span><h3>21 位高精度 AMR 角度编码器</h3><p>21 位分辨率，一键自校准后 INL ±0.015°（典型值），最高 60000 rpm</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/encoder/ktm53"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm53.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM53 系列</span><h3>离轴 AMR 角度编码器</h3><p>AMR 配合垂直霍尔与数字算法实现离轴测量，校准后 INL ±0.03°（典型值）</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/encoder/ktm58"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm58.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM58 系列</span><h3>30 bit 绝对角度细分器</h3><p>最大 4096 对极输入，30 bit 绝对角度细分，适配磁电阻与光编、光栅、磁栅</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/encoder/ktm59"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm59.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM59 系列</span><h3>高速 TMR 磁编码器</h3><p>双 16 bit 2M SAR ADC，单对极细分 24 bit，最高 180,000 rpm</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/encoder/kth78"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth78.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH78 系列</span><h3>低延时霍尔绝对角度编码器</h3><p>16 位分辨率，系统延时 1 μs 并做延时补偿，全系支持在轴与离轴应用</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/encoder/kth71"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth71.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH71 系列</span><h3>自校准霍尔磁编码器</h3><p>内置自动非线性校准（ANLC），无需复杂外部干预，在轴 INL 优于 ±0.1°</p><span class="c-card__more">查看产品</span></div></a></div>

## 相关词条

<div class="c-grid c-grid--3"><a class="c-card" href="/basics/crc"><div class="c-card__body"><span class="c-card__kicker">输出接口</span><h3>CRC 帧校验</h3><p>附在数据帧末尾的校验位，用来发现传输中出错的帧</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/latency"><div class="c-card__body"><span class="c-card__kicker">精度、噪声与动态</span><h3>延时与动态误差 / Latency</h3><p>磁场变化到角度输出之间的时间，转速越高，它造成的角度滞后越大</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/absolute-incremental"><div class="c-card__body"><span class="c-card__kicker">输出接口</span><h3>绝对值输出 / 增量输出</h3><p>绝对值上电即知当前角度，增量只给出位移量</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/i2c"><div class="c-card__body"><span class="c-card__kicker">输出接口</span><h3>I2C 总线</h3><p>两线制（时钟 + 数据）的多器件总线，适合低速读写传感器数据与配置</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/abz"><div class="c-card__body"><span class="c-card__kicker">输出接口</span><h3>ABZ 增量输出</h3><p>A、B 两路正交方波，加每圈一个 Z 索引脉冲</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/uvw"><div class="c-card__body"><span class="c-card__kicker">输出接口</span><h3>UVW 换向输出</h3><p>三路互差 120° 电角度的方波，供电机换向定扇区</p><span class="c-card__more">阅读词条</span></div></a></div>

<div class="c-wiki-pager">

<div class="c-grid c-grid--2"><a class="c-card" href="/basics/uvw"><div class="c-card__body"><span class="c-card__kicker">← 上一条</span><h3>UVW 换向输出</h3><p>三路互差 120° 电角度的方波，供电机换向定扇区</p></div></a><a class="c-card" href="/basics/crc"><div class="c-card__body"><span class="c-card__kicker">下一条 →</span><h3>CRC 帧校验</h3><p>附在数据帧末尾的校验位，用来发现传输中出错的帧</p></div></a></div>

</div>

<div class="c-cta"><div><h2 class="c-cta__title">还有拿不准的参数？</h2><p>选型、磁路与接口对接上的问题，欢迎直接找我们的技术团队确认。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
