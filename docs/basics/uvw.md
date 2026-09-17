---
title: "UVW 换向输出 · 技术 Wiki"
description: "三路互差 120° 电角度的方波，供电机换向定扇区"
aside: false
pageClass: "c-page c-page--wiki"
---

<nav class="c-crumbs"><a href="/msite/">首页</a><i>/</i><a href="/msite/basics/">技术 Wiki</a><i>/</i><span>UVW 换向输出</span></nav>

<p class="c-kicker">输出接口</p>

# UVW 换向输出

<p class="c-lead">三路互差 120° 电角度的方波，供电机换向定扇区</p>

## 是什么

U、V、W 三路方波互差 120° 电角度，一个电周期内组合出六个扇区（000 与 111 两个组合为非法状态），驱动器据此判断转子所处的换向区间，做六步换向或为 FOC 提供起动相位。

## 分立霍尔与编码器合成

传统方案用三颗霍尔沿定子错开 120° 电角度贴装，换向角误差取决于贴装位置，而且必须用锁存型霍尔：单极型在磁极转走时会在阈值附近抖动，全极型对 N、S 极输出相同状态，扇区码会重码。

由角度编码器合成 UVW 时，换向角精度取决于编码器角度精度，极对数变成可配置参数，同一颗芯片可以适配不同极对数的电机，省去霍尔贴装与标定工序。

## 怎么配

按顺序确认三件事：**极对数**等于电机极对数（U 相电周期数与机械圈数之比正确）；**方向**与电机相序一致；**零位偏置**使 U 相跳变与转子磁极位置对齐。

极对数配错，表现为转速越高越乱；方向或零位配错，表现为与转速无关的固定偏差、起动方向不对或堵转抖动。

::: tip 要点提示
UVW 的角度分辨能力只有 60° 电角度量级，用途是起动换向与粗定位；精确位置仍取自 ABZ 或串行绝对值输出。
:::

## 常见误区

<p class="c-sec-lead">每条标题是常听到的说法，下方是工程上的实际情况。</p>

<div class="c-features c-pitfalls"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>极对数配对了，换向就对了</h3><p>极对数只决定一圈有几个换向周期，不决定从哪个角度开始。方向与零位偏置同样要标定。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>单极或全极霍尔也能做换向</h3><p>换向需要记住上一次经过的磁极，只有锁存型能满足；单极会抖动，全极会重码。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>UVW 可以用于位置控制</h3><p>UVW 的分辨能力只有 60° 电角度，只适合起动换向与粗定位。</p></div></div></div>

## 相关系列

<p class="c-sec-lead">正文涉及的原理与指标，在这些产品系列上用得到。</p>

<div class="c-grid c-grid--3"><a class="c-card" href="/msite/products/encoder/ktm52"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/ktm52.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM52 系列</span><h3>21 位高精度 AMR 角度编码器</h3><p>21 位分辨率，一键自校准后 INL ±0.015°（典型值），最高 60000 rpm</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/encoder/ktm53"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/ktm53.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM53 系列</span><h3>离轴 AMR 角度编码器</h3><p>AMR 配合垂直霍尔与数字算法实现离轴测量，校准后 INL ±0.03°（典型值）</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/encoder/ktm58"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/ktm58.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM58 系列</span><h3>30 bit 绝对角度细分器</h3><p>最大 4096 对极输入，30 bit 绝对角度细分，适配磁电阻与光编、光栅、磁栅</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/encoder/ktm59"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/ktm59.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM59 系列</span><h3>高速 TMR 磁编码器</h3><p>双 16 bit 2M SAR ADC，单对极细分 24 bit，最高 180,000 rpm</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/encoder/kth78"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth78.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH78 系列</span><h3>低延时霍尔绝对角度编码器</h3><p>16 位分辨率，系统延时 1 μs 并做延时补偿，全系支持在轴与离轴应用</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/encoder/kth71"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth71.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH71 系列</span><h3>自校准霍尔磁编码器</h3><p>内置自动非线性校准（ANLC），无需复杂外部干预，在轴 INL 优于 ±0.1°</p><span class="c-card__more">查看产品</span></div></a></div>

## 相关词条

<div class="c-grid c-grid--3"><a class="c-card" href="/msite/basics/pole-pairs"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>对极数 / Pole pairs</h3><p>磁环沿圆周的 N-S 磁极对数，一对极为一个信号周期</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/latching"><div class="c-card__body"><span class="c-card__kicker">开关与线性器件</span><h3>锁存型 / Latch</h3><p>一个极性置位、相反极性复位，撤磁后保持原状态</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/abz"><div class="c-card__body"><span class="c-card__kicker">输出接口</span><h3>ABZ 增量输出</h3><p>A、B 两路正交方波，加每圈一个 Z 索引脉冲</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/latency"><div class="c-card__body"><span class="c-card__kicker">精度、噪声与动态</span><h3>延时与动态误差 / Latency</h3><p>磁场变化到角度输出之间的时间，转速越高，它造成的角度滞后越大</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/absolute-incremental"><div class="c-card__body"><span class="c-card__kicker">输出接口</span><h3>绝对值输出 / 增量输出</h3><p>绝对值上电即知当前角度，增量只给出位移量</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/spi-ssi"><div class="c-card__body"><span class="c-card__kicker">输出接口</span><h3>SPI / SSI 串行绝对值接口</h3><p>主控按时钟读走绝对角度的两种同步串行方式</p><span class="c-card__more">阅读词条</span></div></a></div>

<div class="c-wiki-pager">

<div class="c-grid c-grid--2"><a class="c-card" href="/msite/basics/abz"><div class="c-card__body"><span class="c-card__kicker">← 上一条</span><h3>ABZ 增量输出</h3><p>A、B 两路正交方波，加每圈一个 Z 索引脉冲</p></div></a><a class="c-card" href="/msite/basics/spi-ssi"><div class="c-card__body"><span class="c-card__kicker">下一条 →</span><h3>SPI / SSI 串行绝对值接口</h3><p>主控按时钟读走绝对角度的两种同步串行方式</p></div></a></div>

</div>

<div class="c-cta"><div><h2 class="c-cta__title">还有拿不准的参数？</h2><p>选型、磁路与接口对接上的问题，欢迎直接找我们的技术团队确认。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/msite/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
