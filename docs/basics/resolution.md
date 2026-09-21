---
title: "分辨率 / Resolution · 技术 Wiki"
description: "输出能区分的最小角度步距，与准确度是两回事"
aside: false
pageClass: "c-page c-page--wiki"
ld: "{\"@context\": \"https://schema.org\", \"@type\": \"DefinedTerm\", \"name\": \"分辨率 / Resolution\", \"description\": \"输出能区分的最小角度步距，与准确度是两回事\", \"inDefinedTermSet\": {\"@type\": \"DefinedTermSet\", \"name\": \"昆泰芯技术 Wiki\", \"url\": \"https://conntek.grosso.link/basics/\"}, \"url\": \"https://conntek.grosso.link/basics/resolution\"}"
---

<nav class="c-crumbs"><a href="/">首页</a><i>/</i><a href="/basics/">技术 Wiki</a><i>/</i><span>分辨率 / Resolution</span></nav>

<p class="c-kicker">精度、噪声与动态</p>

# 分辨率 / Resolution

<p class="c-lead">输出能区分的最小角度步距，与准确度是两回事</p>

## 是什么

分辨率由输出位数决定：n bit 对应一圈 2ⁿ 步。12 bit 约 0.088°，14 bit 约 0.022°，16 bit 约 0.0055°，21 bit 约 0.00017°。它只说明数字读数的刻度有多细，不说明这个读数离真实角度有多远——后者由 INL 描述。

## 分辨率、精度、重复性

**分辨率**是刻度细度；**精度**（INL）是读数与真实角度的最大偏差；**重复性**是多次回到同一位置时读数的离散程度。速度环、换向、增量定位主要吃分辨率与重复性；需要和外部绝对基准对齐的场合（精密测角、转台）才主要吃精度。

需求里只写「要 N 位」时，一定要追问是输出位宽还是整圈误差。同一个数字，前者多数磁编码器都能给出，后者可能已经进入光学编码器的范围，方案路线完全不同。

## 怎么选

先做系统精度预算：把减速器回差、结构变形、安装偏心、温漂逐项扣除，再决定需要多少位。当分辨率已经远细于系统误差时，多出来的位数不再转化为有效精度。

分辨率的上限还受噪声限制：最低几位若低于噪声水平，只是在随机跳动。不同接口的口径也不同——SPI 位宽、ABZ 线数、PWM 可分辨的占空比步数，要分别确认。

::: tip 要点提示
当位数高于实际噪声水平时，最低几位是随机跳动的，不携带信息。判断能实际用到第几位，要同时看规格里的角度噪声（均方根值）。
:::

## 常见误区

<p class="c-sec-lead">每条标题是常听到的说法，下方是工程上的实际情况。</p>

<div class="c-features c-pitfalls"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>21 bit 就是准到 0.00017°</h3><p>那是刻度步距，不是误差。整圈误差要看 INL，而且还要叠加安装与磁铁带来的误差。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>需求写「N 位」不必区分口径</h3><p>输出位宽与整圈精度可以相差几个数量级，不问清楚要么丢掉能做的项目，要么在样品阶段翻车。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>芯片内部位数高，输出的每一位都有效</h3><p>低于噪声水平的位是随机的。能实际用到第几位，要结合角度噪声与所用带宽判断。</p></div></div></div>

## 相关系列

<p class="c-sec-lead">正文涉及的原理与指标，在这些产品系列上用得到。</p>

<div class="c-grid c-grid--3"><a class="c-card" href="/products/3d-hall/kth55"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth55.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH55 系列</span><h3>垂直霍尔绝对角度传感器</h3><p>垂直霍尔配合 16 位 ADC，0 ~ 360° 绝对角度输出，符合 AEC-Q100</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/encoder/ktm52"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm52.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM52 系列</span><h3>21 位高精度 AMR 角度编码器</h3><p>21 位分辨率，一键自校准后 INL ±0.015°（典型值），最高 60000 rpm</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/encoder/ktm58"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm58.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM58 系列</span><h3>30 bit 绝对角度细分器</h3><p>最大 4096 对极输入，30 bit 绝对角度细分，适配磁电阻与光编、光栅、磁栅</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/encoder/ktm59"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm59.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM59 系列</span><h3>高速 TMR 磁编码器</h3><p>双 16 bit 2M SAR ADC，单对极细分 24 bit，最高 180,000 rpm</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/encoder/kth78"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth78.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH78 系列</span><h3>低延时霍尔绝对角度编码器</h3><p>16 位分辨率，系统延时 1 μs 并做延时补偿，全系支持在轴与离轴应用</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/encoder/kto95"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kto95.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTO95 系列</span><h3>游标绝对值光学编码器</h3><p>集成高清相位阵列光电传感器，三通道 Nonius 插值实现最高 24 位单圈分辨率</p><span class="c-card__more">查看产品</span></div></a></div>

## 相关词条

<div class="c-grid c-grid--3"><a class="c-card" href="/basics/inl"><div class="c-card__body"><span class="c-card__kicker">精度、噪声与动态</span><h3>INL / 积分非线性</h3><p>输出角度对真实角度的最大偏差，即角度准确度</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/noise"><div class="c-card__body"><span class="c-card__kicker">精度、噪声与动态</span><h3>角度噪声 / Angle noise</h3><p>静止时角度读数的随机起伏，通常以 1σ（均方根）表示</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/abz"><div class="c-card__body"><span class="c-card__kicker">输出接口</span><h3>ABZ 增量输出</h3><p>A、B 两路正交方波，加每圈一个 Z 索引脉冲</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/vernier"><div class="c-card__body"><span class="c-card__kicker">精度、噪声与动态</span><h3>游标 / Vernier（Nonius）</h3><p>用两条周期数不同的码道拼出高分辨率的单圈绝对位置</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/latency"><div class="c-card__body"><span class="c-card__kicker">精度、噪声与动态</span><h3>延时与动态误差 / Latency</h3><p>磁场变化到角度输出之间的时间，转速越高，它造成的角度滞后越大</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/self-calibration"><div class="c-card__body"><span class="c-card__kicker">精度、噪声与动态</span><h3>自校准 / Self-calibration</h3><p>器件在实装状态下测量并补偿角度非线性误差</p><span class="c-card__more">阅读词条</span></div></a></div>

<div class="c-wiki-pager">

<div class="c-grid c-grid--2"><a class="c-card" href="/basics/stray-field"><div class="c-card__body"><span class="c-card__kicker">← 上一条</span><h3>杂散场 / Stray field</h3><p>靶磁铁以外叠加到芯片上的磁场，会改变合成磁场方向</p></div></a><a class="c-card" href="/basics/inl"><div class="c-card__body"><span class="c-card__kicker">下一条 →</span><h3>INL / 积分非线性</h3><p>输出角度对真实角度的最大偏差，即角度准确度</p></div></a></div>

</div>

<div class="c-cta"><div><h2 class="c-cta__title">还有拿不准的参数？</h2><p>选型、磁路与接口对接上的问题，欢迎直接找我们的技术团队确认。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
