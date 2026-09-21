---
title: "角度噪声 / Angle noise · 技术 Wiki"
description: "静止时角度读数的随机起伏，通常以 1σ（均方根）表示"
aside: false
pageClass: "c-page c-page--wiki"
ld: "{\"@context\": \"https://schema.org\", \"@type\": \"DefinedTerm\", \"name\": \"角度噪声 / Angle noise\", \"description\": \"静止时角度读数的随机起伏，通常以 1σ（均方根）表示\", \"inDefinedTermSet\": {\"@type\": \"DefinedTermSet\", \"name\": \"昆泰芯技术 Wiki\", \"url\": \"https://conntek.github.io/basics/\"}, \"url\": \"https://conntek.github.io/basics/noise\"}"
---

<nav class="c-crumbs"><a href="/">首页</a><i>/</i><a href="/basics/">技术 Wiki</a><i>/</i><span>角度噪声 / Angle noise</span></nav>

<p class="c-kicker">精度、噪声与动态</p>

# 角度噪声 / Angle noise

<p class="c-lead">静止时角度读数的随机起伏，通常以 1σ（均方根）表示</p>

## 是什么

磁铁静止不动时，角度读数仍会在一个小范围内随机跳动，这就是角度噪声。规格里一般给 1σ（均方根）值；按正态分布，读数的峰峰跳动约为 6σ 量级。

噪声来自传感元件热噪声与 1/f 噪声、放大器与 ADC、参考电压与供电，也与芯片处的磁场强度有关：信号幅值越低，折算到角度上的噪声越大。

## 为什么重要

噪声决定读数能「站稳」的最细刻度：低于噪声水平的位数没有意义。

速度通常由相邻两次角度相减再除以时间间隔得到，时间间隔越短，角度噪声被放大得越多。速度环抖动、低速不平稳、电机啸叫，经常能追溯到角度噪声与采样间隔的组合。

## 怎么比较、怎么压

白噪声的均方根与带宽的平方根成正比，所以**噪声数字必须连同带宽或滤波设置一起给**，还要在相同磁场强度下比较。

对独立的随机噪声，N 次平均可把标准差降到 1/√N，但平均窗口越长，数据越旧，延时越大。滤波深度要在噪声与延时之间取舍，高速场合不能一味加深滤波。

::: tip 要点提示
验收时把静态噪声、系统误差（INL）与动态延时分开测、分开签字：静止时看噪声，低速整圈看 INL，目标转速下看延时。
:::

## 常见误区

<p class="c-sec-lead">每条标题是常听到的说法，下方是工程上的实际情况。</p>

<div class="c-features c-pitfalls"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>静止时末位不跳，说明器件更安静</h3><p>截位、死区、深度滤波都能让读数看起来不跳。验收时要问清有没有软件后处理，并在相同带宽下比较。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>平均能消除一切误差</h3><p>平均只对独立随机噪声有效，偏心、谐波、温漂这类系统误差不会因为平均而变小。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>噪声小就是精度高</h3><p>噪声管的是读数稳不稳，INL 管的是读数准不准，两者独立。一颗噪声极小的器件，整圈误差照样可能很大。</p></div></div></div>

## 相关系列

<p class="c-sec-lead">正文涉及的原理与指标，在这些产品系列上用得到。</p>

<div class="c-grid c-grid--3"><a class="c-card" href="/products/encoder/kth78"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth78.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH78 系列</span><h3>低延时霍尔绝对角度编码器</h3><p>16 位分辨率，系统延时 1 μs 并做延时补偿，全系支持在轴与离轴应用</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/encoder/kth71"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth71.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH71 系列</span><h3>自校准霍尔磁编码器</h3><p>内置自动非线性校准（ANLC），无需复杂外部干预，在轴 INL 优于 ±0.1°</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/encoder/ktm52"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm52.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM52 系列</span><h3>21 位高精度 AMR 角度编码器</h3><p>21 位分辨率，一键自校准后 INL ±0.015°（典型值），最高 60000 rpm</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/encoder/ktm59"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm59.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM59 系列</span><h3>高速 TMR 磁编码器</h3><p>双 16 bit 2M SAR ADC，单对极细分 24 bit，最高 180,000 rpm</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/encoder/kto95"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kto95.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTO95 系列</span><h3>游标绝对值光学编码器</h3><p>集成高清相位阵列光电传感器，三通道 Nonius 插值实现最高 24 位单圈分辨率</p><span class="c-card__more">查看产品</span></div></a></div>

## 相关词条

<div class="c-grid c-grid--3"><a class="c-card" href="/basics/resolution"><div class="c-card__body"><span class="c-card__kicker">精度、噪声与动态</span><h3>分辨率 / Resolution</h3><p>输出能区分的最小角度步距，与准确度是两回事</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/inl"><div class="c-card__body"><span class="c-card__kicker">精度、噪声与动态</span><h3>INL / 积分非线性</h3><p>输出角度对真实角度的最大偏差，即角度准确度</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/latency"><div class="c-card__body"><span class="c-card__kicker">精度、噪声与动态</span><h3>延时与动态误差 / Latency</h3><p>磁场变化到角度输出之间的时间，转速越高，它造成的角度滞后越大</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/chopper"><div class="c-card__body"><span class="c-card__kicker">磁敏原理</span><h3>斩波与旋转电流 / Chopper</h3><p>周期性切换激励或信号极性，把失调与低频漂移从信号里分离出去</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/self-calibration"><div class="c-card__body"><span class="c-card__kicker">精度、噪声与动态</span><h3>自校准 / Self-calibration</h3><p>器件在实装状态下测量并补偿角度非线性误差</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/vernier"><div class="c-card__body"><span class="c-card__kicker">精度、噪声与动态</span><h3>游标 / Vernier（Nonius）</h3><p>用两条周期数不同的码道拼出高分辨率的单圈绝对位置</p><span class="c-card__more">阅读词条</span></div></a></div>

<div class="c-wiki-pager">

<div class="c-grid c-grid--2"><a class="c-card" href="/basics/inl"><div class="c-card__body"><span class="c-card__kicker">← 上一条</span><h3>INL / 积分非线性</h3><p>输出角度对真实角度的最大偏差，即角度准确度</p></div></a><a class="c-card" href="/basics/latency"><div class="c-card__body"><span class="c-card__kicker">下一条 →</span><h3>延时与动态误差 / Latency</h3><p>磁场变化到角度输出之间的时间，转速越高，它造成的角度滞后越大</p></div></a></div>

</div>

<div class="c-cta"><div><h2 class="c-cta__title">还有拿不准的参数？</h2><p>选型、磁路与接口对接上的问题，欢迎直接找我们的技术团队确认。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
