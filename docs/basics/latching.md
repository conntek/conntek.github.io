---
title: "锁存型 / Latch · 技术 Wiki"
description: "一个极性置位、相反极性复位，撤磁后保持原状态"
aside: false
pageClass: "c-page c-page--wiki"
ld: "{\"@context\": \"https://schema.org\", \"@type\": \"DefinedTerm\", \"name\": \"锁存型 / Latch\", \"description\": \"一个极性置位、相反极性复位，撤磁后保持原状态\", \"inDefinedTermSet\": {\"@type\": \"DefinedTermSet\", \"name\": \"昆泰芯技术 Wiki\", \"url\": \"https://conntek.github.io/basics/\"}, \"url\": \"https://conntek.github.io/basics/latching\"}"
---

<nav class="c-crumbs"><a href="/">首页</a><i>/</i><a href="/basics/">技术 Wiki</a><i>/</i><span>锁存型 / Latch</span></nav>

<p class="c-kicker">开关与线性器件</p>

# 锁存型 / Latch

<p class="c-lead">一个极性置位、相反极性复位，撤磁后保持原状态</p>

## 是什么

锁存型（双极锁存）有两个极性相反的阈值：一个极性的磁场越过动作阈值把输出置位，只有相反极性越过释放阈值才能把它复位，其间磁场消失时输出保持不变。输出状态取决于「上一次越过的是哪个阈值」。

## 为什么电机离不开它

转子上 N、S 交替排列的磁环经过锁存型器件时，会得到占空比稳定的方波，因此它是测转速、计数与电机换向的常用器件。

三颗锁存霍尔沿圆周错开 120° 电角度，组成六步换向所需的三位扇区码。单极型在磁极转走时会在阈值附近抖动，全极型对 N、S 输出相同状态导致扇区码重码，两者都会让驱动器在错误的时刻给错误的相通电。

## 怎么用

磁环要保证 N、S 两极在芯片处都能越过对应阈值；两个阈值之间的磁滞带吸收抖动，但也让输出边沿相对磁极中性区有一定偏移，换向相位标定时要计入。

上电时如果磁场正处在两个阈值之间，输出状态由器件的上电默认值决定，系统要在转动后才以实际边沿为准。

::: tip 要点提示
锁存型不能用来判断「有没有磁体」——磁体移走后输出不回位。现场只有单一极性可用时，应改选单极型或全极型。
:::

## 常见误区

<p class="c-sec-lead">每条标题是常听到的说法，下方是工程上的实际情况。</p>

<div class="c-features c-pitfalls"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>锁存型可以判断有没有磁体</h3><p>磁体移走后输出不回位，无法判断有无，应改选单极型或全极型。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>上电时锁存型的输出就代表磁极位置</h3><p>磁场处在两个阈值之间时，上电输出是默认状态，不代表真实磁极。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>输出边沿正好在磁极交界处</h3><p>动作与释放阈值不为零，边沿会偏离磁极中性区，偏移量随磁场强度与温度变化。</p></div></div></div>

## 相关系列

<p class="c-sec-lead">正文涉及的原理与指标，在这些产品系列上用得到。</p>

<div class="c-grid c-grid--3"><a class="c-card" href="/products/switch/kth16"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth16.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH13/16/17 系列</span><h3>微功耗 1D 霍尔开关</h3><p>CMOS 工艺集成霍尔元件，1 μA 超低功耗，温度补偿优良，覆盖全极、单极与锁存型</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/switch/ktm13"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm13.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM13 系列</span><h3>TMR 磁阻开关</h3><p>TMR 阻桥与 ASIC 单芯片集成，平行磁场感应，回差可小于 3 高斯</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/switch/kth25"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth25.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH25 系列</span><h3>车规级高压霍尔开关</h3><p>斩波技术（内置零漂移放大器），失调电压小于 10 μV，宽压工作，反接保护电压高达 -32 V</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/switch/kth462"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth462.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH462 系列</span><h3>超灵敏 2D 霍尔开关</h3><p>检测二维磁场，两路独立数字输出，可直接给出速度与方向或每轴独立锁存信号</p><span class="c-card__more">查看产品</span></div></a></div>

## 相关词条

<div class="c-grid c-grid--3"><a class="c-card" href="/basics/unipolar-omnipolar"><div class="c-card__body"><span class="c-card__kicker">开关与线性器件</span><h3>单极型 / 全极型</h3><p>按触发磁极区分：单极只认一个极，全极两极都认</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/bop-brp"><div class="c-card__body"><span class="c-card__kicker">开关与线性器件</span><h3>BOP / BRP 与回差</h3><p>动作阈值与释放阈值，两者之差称为回差</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/uvw"><div class="c-card__body"><span class="c-card__kicker">输出接口</span><h3>UVW 换向输出</h3><p>三路互差 120° 电角度的方波，供电机换向定扇区</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/pole-pairs"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>对极数 / Pole pairs</h3><p>磁环沿圆周的 N-S 磁极对数，一对极为一个信号周期</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/linear-hall"><div class="c-card__body"><span class="c-card__kicker">开关与线性器件</span><h3>线性霍尔 / 比例式输出</h3><p>输出电压随磁通密度线性变化，灵敏度档位同时决定量程</p><span class="c-card__more">阅读词条</span></div></a></div>

<div class="c-wiki-pager">

<div class="c-grid c-grid--2"><a class="c-card" href="/basics/unipolar-omnipolar"><div class="c-card__body"><span class="c-card__kicker">← 上一条</span><h3>单极型 / 全极型</h3><p>按触发磁极区分：单极只认一个极，全极两极都认</p></div></a><a class="c-card" href="/basics/bop-brp"><div class="c-card__body"><span class="c-card__kicker">下一条 →</span><h3>BOP / BRP 与回差</h3><p>动作阈值与释放阈值，两者之差称为回差</p></div></a></div>

</div>

<div class="c-cta"><div><h2 class="c-cta__title">还有拿不准的参数？</h2><p>选型、磁路与接口对接上的问题，欢迎直接找我们的技术团队确认。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
