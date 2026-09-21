---
title: "PWM 角度输出 · 技术 Wiki"
description: "用固定频率方波的占空比表示绝对角度"
aside: false
pageClass: "c-page c-page--wiki"
ld: "{\"@context\": \"https://schema.org\", \"@type\": \"DefinedTerm\", \"name\": \"PWM 角度输出\", \"description\": \"用固定频率方波的占空比表示绝对角度\", \"inDefinedTermSet\": {\"@type\": \"DefinedTermSet\", \"name\": \"昆泰芯技术 Wiki\", \"url\": \"https://conntek.github.io/basics/\"}, \"url\": \"https://conntek.github.io/basics/pwm\"}"
---

<nav class="c-crumbs"><a href="/">首页</a><i>/</i><a href="/basics/">技术 Wiki</a><i>/</i><span>PWM 角度输出</span></nav>

<p class="c-kicker">输出接口</p>

# PWM 角度输出

<p class="c-lead">用固定频率方波的占空比表示绝对角度</p>

## 是什么

一个 PWM 周期内高电平所占的比例与角度成正比，接收端测量高电平时间与周期之比即可还原角度。只需一根信号线，可直接接主控的捕获口，不需要时钟与片选，适合走线受限或需要隔离的场合。

## 怎么读

同时测量高电平时间与整个周期，用两者的比值计算角度。芯片内部振荡器存在频率偏差与温漂，只测高电平时间、按标称周期换算，会把频率误差直接变成角度误差。

部分器件在占空比的最低端与最高端各保留一小段，用于表示零位边界或故障状态，角度的有效区间以手册的换算公式为准。

## 频率、分辨率与模拟化

角度更新率等于 PWM 频率；接收端能分辨的角度步数约等于「一个周期内定时器能数到的计数值」。频率越高更新越快，但每周期可数的计数变少，分辨率随之下降。

需要模拟电压时，可以用 RC 低通把 PWM 滤成直流：截止频率越低纹波越小，响应越慢，要在纹波与响应之间折中。

::: tip 要点提示
角度更新率等于 PWM 频率，而分辨率受接收端定时器计数频率限制：频率调高更新更快，但每周期可数的计数值变少，分辨率反而下降，两者需要折中。
:::

## 常见误区

<p class="c-sec-lead">每条标题是常听到的说法，下方是工程上的实际情况。</p>

<div class="c-features c-pitfalls"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>只测高电平时间就够了</h3><p>周期本身会随温度与芯片个体变化，必须用高电平时间与周期的比值。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>PWM 频率越高越好</h3><p>频率高则接收端每周期计数少，分辨率下降，长线上边沿失真的影响也更大。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>占空比 0% 到 100% 对应 0° 到 360°</h3><p>很多器件两端保留有诊断区，直接线性换算会引入偏置与刻度误差。</p></div></div></div>

## 相关系列

<p class="c-sec-lead">正文涉及的原理与指标，在这些产品系列上用得到。</p>

<div class="c-grid c-grid--3"><a class="c-card" href="/products/3d-hall/kth55"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth55.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH55 系列</span><h3>垂直霍尔绝对角度传感器</h3><p>垂直霍尔配合 16 位 ADC，0 ~ 360° 绝对角度输出，符合 AEC-Q100</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/encoder/ktm52"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm52.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM52 系列</span><h3>21 位高精度 AMR 角度编码器</h3><p>21 位分辨率，一键自校准后 INL ±0.015°（典型值），最高 60000 rpm</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/encoder/ktm53"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm53.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM53 系列</span><h3>离轴 AMR 角度编码器</h3><p>AMR 配合垂直霍尔与数字算法实现离轴测量，校准后 INL ±0.03°（典型值）</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/encoder/ktm58"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm58.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM58 系列</span><h3>30 bit 绝对角度细分器</h3><p>最大 4096 对极输入，30 bit 绝对角度细分，适配磁电阻与光编、光栅、磁栅</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/encoder/ktm59"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm59.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM59 系列</span><h3>高速 TMR 磁编码器</h3><p>双 16 bit 2M SAR ADC，单对极细分 24 bit，最高 180,000 rpm</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/encoder/kth78"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth78.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH78 系列</span><h3>低延时霍尔绝对角度编码器</h3><p>16 位分辨率，系统延时 1 μs 并做延时补偿，全系支持在轴与离轴应用</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/encoder/kth71"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth71.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH71 系列</span><h3>自校准霍尔磁编码器</h3><p>内置自动非线性校准（ANLC），无需复杂外部干预，在轴 INL 优于 ±0.1°</p><span class="c-card__more">查看产品</span></div></a></div>

## 相关词条

<div class="c-grid c-grid--3"><a class="c-card" href="/basics/absolute-incremental"><div class="c-card__body"><span class="c-card__kicker">输出接口</span><h3>绝对值输出 / 增量输出</h3><p>绝对值上电即知当前角度，增量只给出位移量</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/resolution"><div class="c-card__body"><span class="c-card__kicker">精度、噪声与动态</span><h3>分辨率 / Resolution</h3><p>输出能区分的最小角度步距，与准确度是两回事</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/latency"><div class="c-card__body"><span class="c-card__kicker">精度、噪声与动态</span><h3>延时与动态误差 / Latency</h3><p>磁场变化到角度输出之间的时间，转速越高，它造成的角度滞后越大</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/abz"><div class="c-card__body"><span class="c-card__kicker">输出接口</span><h3>ABZ 增量输出</h3><p>A、B 两路正交方波，加每圈一个 Z 索引脉冲</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/uvw"><div class="c-card__body"><span class="c-card__kicker">输出接口</span><h3>UVW 换向输出</h3><p>三路互差 120° 电角度的方波，供电机换向定扇区</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/spi-ssi"><div class="c-card__body"><span class="c-card__kicker">输出接口</span><h3>SPI / SSI 串行绝对值接口</h3><p>主控按时钟读走绝对角度的两种同步串行方式</p><span class="c-card__more">阅读词条</span></div></a></div>

<div class="c-wiki-pager">

<div class="c-grid c-grid--2"><a class="c-card" href="/basics/i2c"><div class="c-card__body"><span class="c-card__kicker">← 上一条</span><h3>I2C 总线</h3><p>两线制（时钟 + 数据）的多器件总线，适合低速读写传感器数据与配置</p></div></a><a class="c-card" href="/basics/hall-effect"><div class="c-card__body"><span class="c-card__kicker">下一条 →</span><h3>霍尔效应 / Hall effect</h3><p>载流薄片在垂直磁场下产生横向电压</p></div></a></div>

</div>

<div class="c-cta"><div><h2 class="c-cta__title">还有拿不准的参数？</h2><p>选型、磁路与接口对接上的问题，欢迎直接找我们的技术团队确认。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
