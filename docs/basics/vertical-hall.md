---
title: "垂直霍尔 / Vertical Hall · 技术 Wiki"
description: "敏感方向落在芯片平面内的霍尔结构"
aside: false
pageClass: "c-page c-page--wiki"
ld: "{\"@context\": \"https://schema.org\", \"@type\": \"DefinedTerm\", \"name\": \"垂直霍尔 / Vertical Hall\", \"description\": \"敏感方向落在芯片平面内的霍尔结构\", \"inDefinedTermSet\": {\"@type\": \"DefinedTermSet\", \"name\": \"昆泰芯技术 Wiki\", \"url\": \"https://conntek.grosso.link/basics/\"}, \"url\": \"https://conntek.grosso.link/basics/vertical-hall\"}"
---

<nav class="c-crumbs"><a href="/">首页</a><i>/</i><a href="/basics/">技术 Wiki</a><i>/</i><span>垂直霍尔 / Vertical Hall</span></nav>

<p class="c-kicker">磁敏原理</p>

# 垂直霍尔 / Vertical Hall

<p class="c-lead">敏感方向落在芯片平面内的霍尔结构</p>

## 是什么

普通平面霍尔盘只感应垂直于芯片表面的 Z 分量。垂直霍尔改变结构，把电流通路做在硅片深度方向，使敏感方向落在芯片平面内，于是同一颗芯片上可以同时取得 X、Y、Z 三个方向的磁场分量。

## 为什么重要

角度测量可以只用平面内的两个分量做反正切：对径充磁磁铁在轴安装时，芯片平面内的磁场方向就是磁铁转角，信号直观。

离轴测量所需的切向与轴向分量，也能由同一颗芯片一次取得，布局更灵活。

## 怎么看它的精度

垂直霍尔的灵敏度通常低于平面霍尔，失调与 X、Y 两路之间的匹配更难控制，所以前端的失调消除、通道增益匹配与温度补偿是关键指标。两路灵敏度不一致会把圆形磁场轨迹读成椭圆，表现为一圈两次的角度误差。

::: tip 要点提示
垂直霍尔结构的失调与通道匹配控制难度高于平面霍尔，实测精度取决于工艺匹配程度与失调抵消手段，不能只按结构类型判断优劣。
:::

## 常见误区

<p class="c-sec-lead">每条标题是常听到的说法，下方是工程上的实际情况。</p>

<div class="c-features c-pitfalls"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>有垂直霍尔就一定能直接测高精度角度</h3><p>精度取决于通道匹配、失调消除与校准，仅凭结构类型无法判断。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>三个方向的灵敏度天然一致</h3><p>平面内与垂直方向的敏感结构不同，灵敏度与温度特性都可能不同，使用多个分量时需要按手册做增益匹配。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>垂直霍尔只能做在轴</h3><p>它可以同时取得平面内与垂直方向分量，在轴、离轴都可以使用，具体取决于磁体布局。</p></div></div></div>

## 相关系列

<p class="c-sec-lead">正文涉及的原理与指标，在这些产品系列上用得到。</p>

<div class="c-grid c-grid--3"><a class="c-card" href="/products/3d-hall/kth55"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth55.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH55 系列</span><h3>垂直霍尔绝对角度传感器</h3><p>垂直霍尔配合 16 位 ADC，0 ~ 360° 绝对角度输出，符合 AEC-Q100</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/encoder/ktm53"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm53.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM53 系列</span><h3>离轴 AMR 角度编码器</h3><p>AMR 配合垂直霍尔与数字算法实现离轴测量，校准后 INL ±0.03°（典型值）</p><span class="c-card__more">查看产品</span></div></a></div>

## 相关词条

<div class="c-grid c-grid--3"><a class="c-card" href="/basics/hall-effect"><div class="c-card__body"><span class="c-card__kicker">磁敏原理</span><h3>霍尔效应 / Hall effect</h3><p>载流薄片在垂直磁场下产生横向电压</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/3d-hall"><div class="c-card__body"><span class="c-card__kicker">磁敏原理</span><h3>三轴霍尔 / 3D Hall</h3><p>一颗芯片同时测 X、Y、Z 三个方向的磁场分量</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/in-axis"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>在轴 / In-axis</h3><p>磁铁装在轴端，芯片感应中心与转轴同心</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/chopper"><div class="c-card__body"><span class="c-card__kicker">磁敏原理</span><h3>斩波与旋转电流 / Chopper</h3><p>周期性切换激励或信号极性，把失调与低频漂移从信号里分离出去</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/amr"><div class="c-card__body"><span class="c-card__kicker">磁敏原理</span><h3>AMR / 各向异性磁阻</h3><p>电阻随磁化方向与电流夹角变化，工作在饱和区</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/tmr"><div class="c-card__body"><span class="c-card__kicker">磁敏原理</span><h3>TMR / 隧道磁电阻</h3><p>隧道结电阻随自由层与钉扎层的磁化夹角变化</p><span class="c-card__more">阅读词条</span></div></a></div>

<div class="c-wiki-pager">

<div class="c-grid c-grid--2"><a class="c-card" href="/basics/chopper"><div class="c-card__body"><span class="c-card__kicker">← 上一条</span><h3>斩波与旋转电流 / Chopper</h3><p>周期性切换激励或信号极性，把失调与低频漂移从信号里分离出去</p></div></a><a class="c-card" href="/basics/3d-hall"><div class="c-card__body"><span class="c-card__kicker">下一条 →</span><h3>三轴霍尔 / 3D Hall</h3><p>一颗芯片同时测 X、Y、Z 三个方向的磁场分量</p></div></a></div>

</div>

<div class="c-cta"><div><h2 class="c-cta__title">还有拿不准的参数？</h2><p>选型、磁路与接口对接上的问题，欢迎直接找我们的技术团队确认。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
