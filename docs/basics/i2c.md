---
title: "I2C 总线 · 技术 Wiki"
description: "两线制（时钟 + 数据）的多器件总线，适合低速读写传感器数据与配置"
aside: false
pageClass: "c-page c-page--wiki"
---

<nav class="c-crumbs"><a href="/msite/">首页</a><i>/</i><a href="/msite/basics/">技术 Wiki</a><i>/</i><span>I2C 总线</span></nav>

<p class="c-kicker">输出接口</p>

# I2C 总线

<p class="c-lead">两线制（时钟 + 数据）的多器件总线，适合低速读写传感器数据与配置</p>

## 是什么

I2C 用 SCL（时钟）与 SDA（数据）两根线连接主机与多个从机，每个从机有独立地址，主机按地址读写寄存器。两根线都是开漏结构，靠上拉电阻拉高，常见速率档位有 100 kbit/s、400 kbit/s 以及更高速的扩展模式。

三轴霍尔、磁场测量类器件常用 I2C 输出测量值并接受工作模式配置，走线少，便于多个传感器共用一组总线。

## 设计要点

**上拉电阻**：阻值与总线电容共同决定上升沿速度。总线越长、挂的器件越多，电容越大，要么减小上拉电阻，要么降低速率。

**地址规划**：同一总线上的器件地址不能冲突，多颗同型号器件要确认是否支持地址配置。

**异常恢复**：从机在传输中途复位或受干扰时可能把 SDA 拉住不放，主机侧要有超时检测和发送时钟脉冲释放总线的恢复流程。

## 怎么选接口

I2C 适合几十到几百赫兹的读写、配置和低功耗轮询；需要高刷新率、确定读取时刻或长线传输时，优先选择 SPI 或专用的串行编码器接口。

::: tip 要点提示
多个传感器共用 I2C 总线时，各自的读取时刻不同。需要多轴数据时间一致时，优先使用器件自带的同步测量或触发模式。
:::

## 常见误区

<p class="c-sec-lead">每条标题是常听到的说法，下方是工程上的实际情况。</p>

<div class="c-features c-pitfalls"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>I2C 也适合高速闭环</h3><p>I2C 速率低、帧开销大、读取时刻受总线占用影响，不适合高带宽电机控制环。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>上拉电阻随便选一个常用值</h3><p>上拉电阻要按总线电容与速率核算，边沿太慢会出现偶发读错。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>总线挂死只能断电</h3><p>主机检测超时后发送若干个时钟脉冲，通常就能让从机释放数据线，恢复流程应写进驱动。</p></div></div></div>

## 相关系列

<p class="c-sec-lead">正文涉及的原理与指标，在这些产品系列上用得到。</p>

<div class="c-grid c-grid--3"><a class="c-card" href="/msite/products/3d-hall/kth57"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth57.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57 系列</span><h3>三轴线性霍尔传感器</h3><p>测量 X、Y、Z 三轴磁场，I2C / SPI 可选，工作模式在线配置，兼顾性能与功耗</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/3d-hall/kth55"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth55.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH55 系列</span><h3>垂直霍尔绝对角度传感器</h3><p>垂直霍尔配合 16 位 ADC，0 ~ 360° 绝对角度输出，符合 AEC-Q100</p><span class="c-card__more">查看产品</span></div></a></div>

## 相关词条

<div class="c-grid c-grid--3"><a class="c-card" href="/msite/basics/spi-ssi"><div class="c-card__body"><span class="c-card__kicker">输出接口</span><h3>SPI / SSI 串行绝对值接口</h3><p>主控按时钟读走绝对角度的两种同步串行方式</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/3d-hall"><div class="c-card__body"><span class="c-card__kicker">磁敏原理</span><h3>三轴霍尔 / 3D Hall</h3><p>一颗芯片同时测 X、Y、Z 三个方向的磁场分量</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/crc"><div class="c-card__body"><span class="c-card__kicker">输出接口</span><h3>CRC 帧校验</h3><p>附在数据帧末尾的校验位，用来发现传输中出错的帧</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/pwm"><div class="c-card__body"><span class="c-card__kicker">输出接口</span><h3>PWM 角度输出</h3><p>用固定频率方波的占空比表示绝对角度</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/absolute-incremental"><div class="c-card__body"><span class="c-card__kicker">输出接口</span><h3>绝对值输出 / 增量输出</h3><p>绝对值上电即知当前角度，增量只给出位移量</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/abz"><div class="c-card__body"><span class="c-card__kicker">输出接口</span><h3>ABZ 增量输出</h3><p>A、B 两路正交方波，加每圈一个 Z 索引脉冲</p><span class="c-card__more">阅读词条</span></div></a></div>

<div class="c-wiki-pager">

<div class="c-grid c-grid--2"><a class="c-card" href="/msite/basics/crc"><div class="c-card__body"><span class="c-card__kicker">← 上一条</span><h3>CRC 帧校验</h3><p>附在数据帧末尾的校验位，用来发现传输中出错的帧</p></div></a><a class="c-card" href="/msite/basics/pwm"><div class="c-card__body"><span class="c-card__kicker">下一条 →</span><h3>PWM 角度输出</h3><p>用固定频率方波的占空比表示绝对角度</p></div></a></div>

</div>

<div class="c-cta"><div><h2 class="c-cta__title">还有拿不准的参数？</h2><p>选型、磁路与接口对接上的问题，欢迎直接找我们的技术团队确认。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/msite/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
