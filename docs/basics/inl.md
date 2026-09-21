---
title: "INL / 积分非线性 · 技术 Wiki"
description: "输出角度对真实角度的最大偏差，即角度准确度"
aside: false
pageClass: "c-page c-page--wiki"
ld: "{\"@context\": \"https://schema.org\", \"@type\": \"DefinedTerm\", \"name\": \"INL / 积分非线性\", \"description\": \"输出角度对真实角度的最大偏差，即角度准确度\", \"inDefinedTermSet\": {\"@type\": \"DefinedTermSet\", \"name\": \"昆泰芯技术 Wiki\", \"url\": \"https://conntek.github.io/basics/\"}, \"url\": \"https://conntek.github.io/basics/inl\"}"
---

<nav class="c-crumbs"><a href="/">首页</a><i>/</i><a href="/basics/">技术 Wiki</a><i>/</i><span>INL / 积分非线性</span></nav>

<p class="c-kicker">精度、噪声与动态</p>

# INL / 积分非线性

<p class="c-lead">输出角度对真实角度的最大偏差，即角度准确度</p>

## 是什么

把一圈内每个位置的「读数减真值」画出来，扣掉零点偏置后剩下的曲线，其峰值（或峰峰值的一半）就是 INL，单位是角度。它描述的是系统性、可重复的误差，随机噪声另用角度噪声描述。

## 从误差曲线的形状读出原因

误差曲线通常是一圈内重复出现的低次谐波，每一阶对应一类原因：

**一圈一次**：两路信号直流失调、在轴偏心。**一圈两次**：两路幅值不等、相位不正交、磁铁倾斜。**与极对数同频**：多对极磁环的极内误差。**不规则起伏**：充磁不均、各极宽度不一致、结构件磁化。

先按谐波阶次分类，再去对应的环节找原因，比直接换芯片高效得多。

## 怎么测

用精度高一个数量级以上的参考编码器同轴对拖，在低速下采整圈，避免把延时带来的动态滞后算进 INL。参考编码器与被测轴之间的联轴器偏心和回差会直接进入结果，要先确认测试台自身的误差。

报告 INL 时写清测试条件：是否校准、在轴还是离轴、单对极还是整圈、磁场强度与温度、典型值还是最大值。

::: tip 要点提示
比较 INL 必须先对齐三件事：是否经过校准、在轴还是离轴、算的是单对极还是整圈。规格里常见的是「校准后 INL（典型值）」，与未校准值可能相差一个数量级。
:::

## 常见误区

<p class="c-sec-lead">每条标题是常听到的说法，下方是工程上的实际情况。</p>

<div class="c-features c-pitfalls"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>INL 小就等于重复定位好</h3><p>INL 衡量对真值的偏差，重复性衡量回到同一点的离散。只做相对定位的系统，更该看重复性与噪声。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>不同手册的 INL 可以直接比大小</h3><p>校准前后、在轴离轴、典型值与最大值、单对极与整圈，任何一项口径不同，数字都不可比。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>INL 是芯片单独决定的</h3><p>实装 INL 由芯片、磁铁、安装与校准共同决定，芯片手册上的数字是给定磁场与安装条件下的结果。</p></div></div></div>

## 相关系列

<p class="c-sec-lead">正文涉及的原理与指标，在这些产品系列上用得到。</p>

<div class="c-grid c-grid--3"><a class="c-card" href="/products/3d-hall/kth55"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth55.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH55 系列</span><h3>垂直霍尔绝对角度传感器</h3><p>垂直霍尔配合 16 位 ADC，0 ~ 360° 绝对角度输出，符合 AEC-Q100</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/encoder/ktm52"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm52.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM52 系列</span><h3>21 位高精度 AMR 角度编码器</h3><p>21 位分辨率，一键自校准后 INL ±0.015°（典型值），最高 60000 rpm</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/encoder/ktm53"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm53.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM53 系列</span><h3>离轴 AMR 角度编码器</h3><p>AMR 配合垂直霍尔与数字算法实现离轴测量，校准后 INL ±0.03°（典型值）</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/encoder/ktm58"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm58.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM58 系列</span><h3>30 bit 绝对角度细分器</h3><p>最大 4096 对极输入，30 bit 绝对角度细分，适配磁电阻与光编、光栅、磁栅</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/encoder/ktm59"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm59.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM59 系列</span><h3>高速 TMR 磁编码器</h3><p>双 16 bit 2M SAR ADC，单对极细分 24 bit，最高 180,000 rpm</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/encoder/kth78"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth78.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH78 系列</span><h3>低延时霍尔绝对角度编码器</h3><p>16 位分辨率，系统延时 1 μs 并做延时补偿，全系支持在轴与离轴应用</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/encoder/kth71"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth71.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH71 系列</span><h3>自校准霍尔磁编码器</h3><p>内置自动非线性校准（ANLC），无需复杂外部干预，在轴 INL 优于 ±0.1°</p><span class="c-card__more">查看产品</span></div></a></div>

## 相关词条

<div class="c-grid c-grid--3"><a class="c-card" href="/basics/resolution"><div class="c-card__body"><span class="c-card__kicker">精度、噪声与动态</span><h3>分辨率 / Resolution</h3><p>输出能区分的最小角度步距，与准确度是两回事</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/noise"><div class="c-card__body"><span class="c-card__kicker">精度、噪声与动态</span><h3>角度噪声 / Angle noise</h3><p>静止时角度读数的随机起伏，通常以 1σ（均方根）表示</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/self-calibration"><div class="c-card__body"><span class="c-card__kicker">精度、噪声与动态</span><h3>自校准 / Self-calibration</h3><p>器件在实装状态下测量并补偿角度非线性误差</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/eccentricity"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>偏心与安装公差</h3><p>转动中心、磁铁中心与芯片感应中心不重合，是最常见的系统误差来源</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/latency"><div class="c-card__body"><span class="c-card__kicker">精度、噪声与动态</span><h3>延时与动态误差 / Latency</h3><p>磁场变化到角度输出之间的时间，转速越高，它造成的角度滞后越大</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/vernier"><div class="c-card__body"><span class="c-card__kicker">精度、噪声与动态</span><h3>游标 / Vernier（Nonius）</h3><p>用两条周期数不同的码道拼出高分辨率的单圈绝对位置</p><span class="c-card__more">阅读词条</span></div></a></div>

<div class="c-wiki-pager">

<div class="c-grid c-grid--2"><a class="c-card" href="/basics/resolution"><div class="c-card__body"><span class="c-card__kicker">← 上一条</span><h3>分辨率 / Resolution</h3><p>输出能区分的最小角度步距，与准确度是两回事</p></div></a><a class="c-card" href="/basics/noise"><div class="c-card__body"><span class="c-card__kicker">下一条 →</span><h3>角度噪声 / Angle noise</h3><p>静止时角度读数的随机起伏，通常以 1σ（均方根）表示</p></div></a></div>

</div>

<div class="c-cta"><div><h2 class="c-cta__title">还有拿不准的参数？</h2><p>选型、磁路与接口对接上的问题，欢迎直接找我们的技术团队确认。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
