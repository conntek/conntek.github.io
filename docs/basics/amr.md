---
title: "AMR / 各向异性磁阻 · 技术 Wiki"
description: "电阻随磁化方向与电流夹角变化，工作在饱和区"
aside: false
pageClass: "c-page c-page--wiki"
---

<nav class="c-crumbs"><a href="/msite/">首页</a><i>/</i><a href="/msite/basics/">技术 Wiki</a><i>/</i><span>AMR / 各向异性磁阻</span></nav>

<p class="c-kicker">磁敏原理</p>

# AMR / 各向异性磁阻

<p class="c-lead">电阻随磁化方向与电流夹角变化，工作在饱和区</p>

## 是什么

坡莫合金薄膜的电阻取决于其磁化方向与电流方向的夹角，按 cos²θ 规律变化。外场足够强（饱和区）时磁化方向完全跟随外场方向，输出只与磁场方向有关、与幅值无关，因此对磁体加工误差与安装距离误差的容忍度较高。

角度测量中常用两组互成 45° 的惠斯通电桥取出两路正交信号。

## 为什么要留足场强

薄膜本身有各向异性场，它像一根「橡皮筋」，想把磁化方向拉回易磁化轴。外场远强于它时，磁化方向几乎完全跟随外场；外场减弱到与它可比时，磁化方向停在两者之间，角度误差以谐波形式出现，并且随场强下降迅速增大，而不是线性变差。

这就是手册里「最小工作磁场」的来历：它不是保守余量，而是保证磁化充分跟随外场的条件。高温、最大气隙、磁体批次下限叠加时，场强仍要高于这个值。

## 适合做什么

高精度在轴测角、高转速电机角度检测，以及只关心磁场方向、不在乎磁极极性的开关（例如气缸活塞位置检测）。

::: tip 要点提示
AMR 的角度依赖周期是 180°，单靠磁阻桥只能唯一确定半圈；要覆盖 0 ~ 360°，需要另一路信息来区分是哪半圈。
:::

## 常见误区

<p class="c-sec-lead">每条标题是常听到的说法，下方是工程上的实际情况。</p>

<div class="c-features c-pitfalls"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>AMR 单独就能给出 0 ~ 360° 角度</h3><p>AMR 的角度依赖周期是 180°，需要另一路信息（例如霍尔）区分半圈。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>场强略低于最小工作磁场，只是精度差一点</h3><p>跌破门槛后误差增长很快，必须按最坏情况保证场强。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>只测方向就完全不受磁体影响</h3><p>磁场方向本身受偏心、充磁不均和杂散场影响，这些仍会进入角度误差。</p></div></div></div>

## 相关系列

<p class="c-sec-lead">正文涉及的原理与指标，在这些产品系列上用得到。</p>

<div class="c-grid c-grid--3"><a class="c-card" href="/msite/products/encoder/ktm52"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/ktm52.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM52 系列</span><h3>21 位高精度 AMR 角度编码器</h3><p>21 位分辨率，一键自校准后 INL ±0.015°（典型值），最高 60000 rpm</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/encoder/ktm53"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/ktm53.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM53 系列</span><h3>离轴 AMR 角度编码器</h3><p>AMR 配合垂直霍尔与数字算法实现离轴测量，校准后 INL ±0.03°（典型值）</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/switch/ktm28"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/ktm28.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM28 系列</span><h3>AMR 高压气缸开关</h3><p>SIP 集成 AMR 与 ASIC，支持两线 / 三线气缸位置检测，任意极性感应水平磁场</p><span class="c-card__more">查看产品</span></div></a></div>

## 相关词条

<div class="c-grid c-grid--3"><a class="c-card" href="/msite/basics/tmr"><div class="c-card__body"><span class="c-card__kicker">磁敏原理</span><h3>TMR / 隧道磁电阻</h3><p>隧道结电阻随自由层与钉扎层的磁化夹角变化</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/air-gap"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>气隙 / Air gap</h3><p>磁铁工作面到芯片感应面之间的距离</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/stray-field"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>杂散场 / Stray field</h3><p>靶磁铁以外叠加到芯片上的磁场，会改变合成磁场方向</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/hall-effect"><div class="c-card__body"><span class="c-card__kicker">磁敏原理</span><h3>霍尔效应 / Hall effect</h3><p>载流薄片在垂直磁场下产生横向电压</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/chopper"><div class="c-card__body"><span class="c-card__kicker">磁敏原理</span><h3>斩波与旋转电流 / Chopper</h3><p>周期性切换激励或信号极性，把失调与低频漂移从信号里分离出去</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/vertical-hall"><div class="c-card__body"><span class="c-card__kicker">磁敏原理</span><h3>垂直霍尔 / Vertical Hall</h3><p>敏感方向落在芯片平面内的霍尔结构</p><span class="c-card__more">阅读词条</span></div></a></div>

<div class="c-wiki-pager">

<div class="c-grid c-grid--2"><a class="c-card" href="/msite/basics/3d-hall"><div class="c-card__body"><span class="c-card__kicker">← 上一条</span><h3>三轴霍尔 / 3D Hall</h3><p>一颗芯片同时测 X、Y、Z 三个方向的磁场分量</p></div></a><a class="c-card" href="/msite/basics/tmr"><div class="c-card__body"><span class="c-card__kicker">下一条 →</span><h3>TMR / 隧道磁电阻</h3><p>隧道结电阻随自由层与钉扎层的磁化夹角变化</p></div></a></div>

</div>

<div class="c-cta"><div><h2 class="c-cta__title">还有拿不准的参数？</h2><p>选型、磁路与接口对接上的问题，欢迎直接找我们的技术团队确认。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/msite/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
