---
title: "绝对值输出 / 增量输出 · 技术 Wiki"
description: "绝对值上电即知当前角度，增量只给出位移量"
aside: false
pageClass: "c-page c-page--wiki"
---

<nav class="c-crumbs"><a href="/msite/">首页</a><i>/</i><a href="/msite/basics/">技术 Wiki</a><i>/</i><span>绝对值输出 / 增量输出</span></nav>

<p class="c-kicker">输出接口</p>

# 绝对值输出 / 增量输出

<p class="c-lead">绝对值上电即知当前角度，增量只给出位移量</p>

## 是什么

绝对值输出（SPI、SSI、PWM）任何时刻读到的都是当前角度本身，断电再上电不必回零。ABZ 给的是脉冲，位置由接收端累加，上电时位置未知，需要回零或找到索引脉冲；UVW 给的不是累加脉冲而是换向扇区状态，它同样不含整圈绝对位置。

多数角度编码器芯片两类输出同时具备，可以一边接驱动器的增量口、一边接主控的串行口。

## 单圈绝对与多圈绝对

单圈绝对值只知道一圈之内的位置，不知道转过了几圈。经过减速器的关节、丝杠、卷绕机构需要多圈位置时，要另有计圈手段：掉电保持的计数、电池或能量采集供电的计圈电路、齿轮多圈结构，或者在上电后执行回零。

## 怎么选

驱动器只认增量口、速度环需要高频边沿时用 ABZ；上电需要立刻知道位置、需要诊断信息时用串行绝对值；只需起动换向时用 UVW；走线受限、只能给一根信号线时用 PWM。

::: tip 要点提示
增量口的位置是接收端算出来的，一旦丢脉冲，误差会一直累积下去直到下一次索引；绝对值口不存在累积误差。
:::

## 常见误区

<p class="c-sec-lead">每条标题是常听到的说法，下方是工程上的实际情况。</p>

<div class="c-features c-pitfalls"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>绝对值编码器就是多圈绝对</h3><p>多数角度芯片给的是单圈绝对值，多圈需要额外的计圈机制。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>增量口加了 Z 就等于绝对值</h3><p>Z 每圈只出现一次，上电后要先转到 Z 才知道位置；Z 之前的这段运动只能靠相对计数。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>两类输出读到的位置天然一致</h3><p>增量位置是接收端累加的结果，丢脉冲、上电初值、方向设置不同都会让两路读数不一致，系统里要有对齐与校验逻辑。</p></div></div></div>

## 相关系列

<p class="c-sec-lead">正文涉及的原理与指标，在这些产品系列上用得到。</p>

<div class="c-grid c-grid--3"><a class="c-card" href="/msite/products/3d-hall/kth55"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth55.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH55 系列</span><h3>垂直霍尔绝对角度传感器</h3><p>垂直霍尔配合 16 位 ADC，0 ~ 360° 绝对角度输出，符合 AEC-Q100</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/encoder/ktm52"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/ktm52.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM52 系列</span><h3>21 位高精度 AMR 角度编码器</h3><p>21 位分辨率，一键自校准后 INL ±0.015°（典型值），最高 60000 rpm</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/encoder/ktm53"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/ktm53.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM53 系列</span><h3>离轴 AMR 角度编码器</h3><p>AMR 配合垂直霍尔与数字算法实现离轴测量，校准后 INL ±0.03°（典型值）</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/encoder/ktm58"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/ktm58.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM58 系列</span><h3>30 bit 绝对角度细分器</h3><p>最大 4096 对极输入，30 bit 绝对角度细分，适配磁电阻与光编、光栅、磁栅</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/encoder/ktm59"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/ktm59.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM59 系列</span><h3>高速 TMR 磁编码器</h3><p>双 16 bit 2M SAR ADC，单对极细分 24 bit，最高 180,000 rpm</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/encoder/kth78"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth78.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH78 系列</span><h3>低延时霍尔绝对角度编码器</h3><p>16 位分辨率，系统延时 1 μs 并做延时补偿，全系支持在轴与离轴应用</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/encoder/kth71"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth71.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH71 系列</span><h3>自校准霍尔磁编码器</h3><p>内置自动非线性校准（ANLC），无需复杂外部干预，在轴 INL 优于 ±0.1°</p><span class="c-card__more">查看产品</span></div></a></div>

## 相关词条

<div class="c-grid c-grid--3"><a class="c-card" href="/msite/basics/abz"><div class="c-card__body"><span class="c-card__kicker">输出接口</span><h3>ABZ 增量输出</h3><p>A、B 两路正交方波，加每圈一个 Z 索引脉冲</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/uvw"><div class="c-card__body"><span class="c-card__kicker">输出接口</span><h3>UVW 换向输出</h3><p>三路互差 120° 电角度的方波，供电机换向定扇区</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/spi-ssi"><div class="c-card__body"><span class="c-card__kicker">输出接口</span><h3>SPI / SSI 串行绝对值接口</h3><p>主控按时钟读走绝对角度的两种同步串行方式</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/pwm"><div class="c-card__body"><span class="c-card__kicker">输出接口</span><h3>PWM 角度输出</h3><p>用固定频率方波的占空比表示绝对角度</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/crc"><div class="c-card__body"><span class="c-card__kicker">输出接口</span><h3>CRC 帧校验</h3><p>附在数据帧末尾的校验位，用来发现传输中出错的帧</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/i2c"><div class="c-card__body"><span class="c-card__kicker">输出接口</span><h3>I2C 总线</h3><p>两线制（时钟 + 数据）的多器件总线，适合低速读写传感器数据与配置</p><span class="c-card__more">阅读词条</span></div></a></div>

<div class="c-wiki-pager">

<div class="c-grid c-grid--2"><a class="c-card" href="/msite/basics/vernier"><div class="c-card__body"><span class="c-card__kicker">← 上一条</span><h3>游标 / Vernier（Nonius）</h3><p>用两条周期数不同的码道拼出高分辨率的单圈绝对位置</p></div></a><a class="c-card" href="/msite/basics/abz"><div class="c-card__body"><span class="c-card__kicker">下一条 →</span><h3>ABZ 增量输出</h3><p>A、B 两路正交方波，加每圈一个 Z 索引脉冲</p></div></a></div>

</div>

<div class="c-cta"><div><h2 class="c-cta__title">还有拿不准的参数？</h2><p>选型、磁路与接口对接上的问题，欢迎直接找我们的技术团队确认。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/msite/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
