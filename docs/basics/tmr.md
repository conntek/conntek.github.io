---
title: "TMR / 隧道磁电阻 · 技术 Wiki"
description: "隧道结电阻随自由层与钉扎层的磁化夹角变化"
aside: false
pageClass: "c-page c-page--wiki"
ld: "{\"@context\": \"https://schema.org\", \"@type\": \"DefinedTerm\", \"name\": \"TMR / 隧道磁电阻\", \"description\": \"隧道结电阻随自由层与钉扎层的磁化夹角变化\", \"inDefinedTermSet\": {\"@type\": \"DefinedTermSet\", \"name\": \"昆泰芯技术 Wiki\", \"url\": \"https://conntek.github.io/basics/\"}, \"url\": \"https://conntek.github.io/basics/tmr\"}"
---

<nav class="c-crumbs"><a href="/">首页</a><i>/</i><a href="/basics/">技术 Wiki</a><i>/</i><span>TMR / 隧道磁电阻</span></nav>

<p class="c-kicker">磁敏原理</p>

# TMR / 隧道磁电阻

<p class="c-lead">隧道结电阻随自由层与钉扎层的磁化夹角变化</p>

## 是什么

磁性隧道结由钉扎层、绝缘势垒与自由层构成，自由层磁化方向随外场转动，隧穿电阻随两层磁化夹角变化，变化率比 AMR、GMR 高一个数量级以上。

## 带来什么

输出幅值大，前端放大需求低，信噪比高；桥臂阻值可以做得很高，工作电流小、功耗低；角度依赖周期为 360°，单组桥即可区分整圈。

用作开关时可以做到很低的工作电流与较小的回差；很多 TMR 开关感应的是平行于封装表面的磁场，与常见霍尔开关的感应方向不同。

## 需要注意什么

灵敏度高也意味着对杂散场同样敏感，布局与差分设计更重要。阻值与灵敏度有温度系数，需要补偿；强场下存在饱和，自由层还有一定磁滞，可能表现为正反转读数的微小差异。

::: tip 要点提示
TMR 的阻值与温度系数需要补偿，强场下存在饱和与磁滞。用作开关时回差（BOP 与 BRP 之差）可以做得比霍尔更小。
:::

## 常见误区

<p class="c-sec-lead">每条标题是常听到的说法，下方是工程上的实际情况。</p>

<div class="c-features c-pitfalls"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>灵敏度越高越适合测角</h3><p>测角看的是工作磁场窗口内的线性度、磁滞与温漂，高灵敏度同时放大杂散场与安装误差。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>TMR 开关可以直接替换同封装的霍尔开关</h3><p>两者的感应方向可能不同，替换前要确认磁体方向与安装位置是否需要调整。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>TMR 没有温漂</h3><p>阻值与灵敏度都随温度变化，精度指标要看全温度范围的数据。</p></div></div></div>

## 相关系列

<p class="c-sec-lead">正文涉及的原理与指标，在这些产品系列上用得到。</p>

<div class="c-grid c-grid--3"><a class="c-card" href="/products/encoder/ktm59"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm59.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM59 系列</span><h3>高速 TMR 磁编码器</h3><p>双 16 bit 2M SAR ADC，单对极细分 24 bit，最高 180,000 rpm</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/switch/ktm13"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm13.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM13 系列</span><h3>TMR 磁阻开关</h3><p>TMR 阻桥与 ASIC 单芯片集成，平行磁场感应，回差可小于 3 高斯</p><span class="c-card__more">查看产品</span></div></a></div>

## 相关词条

<div class="c-grid c-grid--3"><a class="c-card" href="/basics/amr"><div class="c-card__body"><span class="c-card__kicker">磁敏原理</span><h3>AMR / 各向异性磁阻</h3><p>电阻随磁化方向与电流夹角变化，工作在饱和区</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/stray-field"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>杂散场 / Stray field</h3><p>靶磁铁以外叠加到芯片上的磁场，会改变合成磁场方向</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/bop-brp"><div class="c-card__body"><span class="c-card__kicker">开关与线性器件</span><h3>BOP / BRP 与回差</h3><p>动作阈值与释放阈值，两者之差称为回差</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/hall-effect"><div class="c-card__body"><span class="c-card__kicker">磁敏原理</span><h3>霍尔效应 / Hall effect</h3><p>载流薄片在垂直磁场下产生横向电压</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/chopper"><div class="c-card__body"><span class="c-card__kicker">磁敏原理</span><h3>斩波与旋转电流 / Chopper</h3><p>周期性切换激励或信号极性，把失调与低频漂移从信号里分离出去</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/vertical-hall"><div class="c-card__body"><span class="c-card__kicker">磁敏原理</span><h3>垂直霍尔 / Vertical Hall</h3><p>敏感方向落在芯片平面内的霍尔结构</p><span class="c-card__more">阅读词条</span></div></a></div>

<div class="c-wiki-pager">

<div class="c-grid c-grid--2"><a class="c-card" href="/basics/amr"><div class="c-card__body"><span class="c-card__kicker">← 上一条</span><h3>AMR / 各向异性磁阻</h3><p>电阻随磁化方向与电流夹角变化，工作在饱和区</p></div></a><a class="c-card" href="/basics/unipolar-omnipolar"><div class="c-card__body"><span class="c-card__kicker">下一条 →</span><h3>单极型 / 全极型</h3><p>按触发磁极区分：单极只认一个极，全极两极都认</p></div></a></div>

</div>

<div class="c-cta"><div><h2 class="c-cta__title">还有拿不准的参数？</h2><p>选型、磁路与接口对接上的问题，欢迎直接找我们的技术团队确认。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
