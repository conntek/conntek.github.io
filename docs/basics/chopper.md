---
title: "斩波与旋转电流 / Chopper · 技术 Wiki"
description: "周期性切换激励或信号极性，把失调与低频漂移从信号里分离出去"
aside: false
pageClass: "c-page c-page--wiki"
ld: "{\"@context\": \"https://schema.org\", \"@type\": \"DefinedTerm\", \"name\": \"斩波与旋转电流 / Chopper\", \"description\": \"周期性切换激励或信号极性，把失调与低频漂移从信号里分离出去\", \"inDefinedTermSet\": {\"@type\": \"DefinedTermSet\", \"name\": \"昆泰芯技术 Wiki\", \"url\": \"https://conntek.grosso.link/basics/\"}, \"url\": \"https://conntek.grosso.link/basics/chopper\"}"
---

<nav class="c-crumbs"><a href="/">首页</a><i>/</i><a href="/basics/">技术 Wiki</a><i>/</i><span>斩波与旋转电流 / Chopper</span></nav>

<p class="c-kicker">磁敏原理</p>

# 斩波与旋转电流 / Chopper

<p class="c-lead">周期性切换激励或信号极性，把失调与低频漂移从信号里分离出去</p>

## 是什么

传感元件与放大器都有失调电压和 1/f 噪声，它们集中在低频，正好和缓慢变化的磁场信号混在一起。斩波的思路是按固定频率周期性翻转信号的极性，把有用信号调制到斩波频率上，与低频失调分开，处理后再解调回来。

旋转电流（spinning current）是霍尔元件上的对应做法：轮流改变霍尔片的激励电流方向，失调电压在不同相位下符号不同、霍尔信号符号保持一致，组合之后失调被抵消。

## 为什么重要

失调电压决定了开关阈值的一致性与温漂、线性霍尔的零点稳定性、角度传感器的一次谐波误差。对于微弱信号，不做失调消除，温度一变，零点就跟着漂。

同样的原理也用在精密运放上：零温漂运放通过斩波或自校准，把输入失调压到很低，并且几乎不随温度与时间变化。

## 代价

斩波会在斩波频率及其谐波处留下残余纹波，信号链后端需要滤波，部分器件手册会要求在输出端增加滤波。

斩波与滤波需要时间：信号带宽与响应速度受斩波频率约束。低功耗开关器件还会周期性唤醒、采样、比较，响应时间取决于唤醒周期，平均电流也大致随采样频率上升。

::: tip 要点提示
对比零点温漂或阈值一致性时，要同时看器件的采样频率与带宽：失调抑制越彻底，往往意味着需要更多的时间做调制与滤波。
:::

## 常见误区

<p class="c-sec-lead">每条标题是常听到的说法，下方是工程上的实际情况。</p>

<div class="c-features c-pitfalls"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>有斩波就没有噪声了</h3><p>斩波消除的是失调与低频漂移，宽带热噪声仍在，甚至在斩波频率附近留下纹波。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>低功耗霍尔开关是实时响应的</h3><p>微功耗器件按固定周期唤醒采样，磁场变化到输出翻转之间至少隔一个采样周期，高速计数要核对采样频率。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>斩波器件输出直接接 ADC 就行</h3><p>要按手册确认输出端是否需要滤波，以及 ADC 采样频率与斩波频率的关系，避免混叠。</p></div></div></div>

## 相关系列

<p class="c-sec-lead">正文涉及的原理与指标，在这些产品系列上用得到。</p>

<div class="c-grid c-grid--3"><a class="c-card" href="/products/switch/kth25"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth25.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH25 系列</span><h3>车规级高压霍尔开关</h3><p>斩波技术（内置零漂移放大器），失调电压小于 10 μV，宽压工作，反接保护电压高达 -32 V</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/switch/kth16"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth16.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH13/16/17 系列</span><h3>微功耗 1D 霍尔开关</h3><p>CMOS 工艺集成霍尔元件，1 μA 超低功耗，温度补偿优良，覆盖全极、单极与锁存型</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/switch/kth31"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth31.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH31 系列</span><h3>比例式线性霍尔传感器</h3><p>按比例响应磁通密度，30 kHz 高速带宽、轨到轨模拟输出，多灵敏度可选</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/switch/linear-hall"><div class="c-card__media c-media--icon"><img src="/img/icons-web/linear-hall.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH564 系列</span><h3>线性霍尔芯片</h3><p>零磁场输出 1/2 VCC，输出随磁通密度线性变化，多档灵敏度匹配不同检测范围</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/other/ktax33"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktax33.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTAx333 系列</span><h3>零温漂高精度运放</h3><p>自校准 CMOS 运放，失调电压 2 μV（典型值），轨到轨输入 / 输出</p><span class="c-card__more">查看产品</span></div></a></div>

## 相关词条

<div class="c-grid c-grid--3"><a class="c-card" href="/basics/hall-effect"><div class="c-card__body"><span class="c-card__kicker">磁敏原理</span><h3>霍尔效应 / Hall effect</h3><p>载流薄片在垂直磁场下产生横向电压</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/noise"><div class="c-card__body"><span class="c-card__kicker">精度、噪声与动态</span><h3>角度噪声 / Angle noise</h3><p>静止时角度读数的随机起伏，通常以 1σ（均方根）表示</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/bop-brp"><div class="c-card__body"><span class="c-card__kicker">开关与线性器件</span><h3>BOP / BRP 与回差</h3><p>动作阈值与释放阈值，两者之差称为回差</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/linear-hall"><div class="c-card__body"><span class="c-card__kicker">开关与线性器件</span><h3>线性霍尔 / 比例式输出</h3><p>输出电压随磁通密度线性变化，灵敏度档位同时决定量程</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/vertical-hall"><div class="c-card__body"><span class="c-card__kicker">磁敏原理</span><h3>垂直霍尔 / Vertical Hall</h3><p>敏感方向落在芯片平面内的霍尔结构</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/3d-hall"><div class="c-card__body"><span class="c-card__kicker">磁敏原理</span><h3>三轴霍尔 / 3D Hall</h3><p>一颗芯片同时测 X、Y、Z 三个方向的磁场分量</p><span class="c-card__more">阅读词条</span></div></a></div>

<div class="c-wiki-pager">

<div class="c-grid c-grid--2"><a class="c-card" href="/basics/hall-effect"><div class="c-card__body"><span class="c-card__kicker">← 上一条</span><h3>霍尔效应 / Hall effect</h3><p>载流薄片在垂直磁场下产生横向电压</p></div></a><a class="c-card" href="/basics/vertical-hall"><div class="c-card__body"><span class="c-card__kicker">下一条 →</span><h3>垂直霍尔 / Vertical Hall</h3><p>敏感方向落在芯片平面内的霍尔结构</p></div></a></div>

</div>

<div class="c-cta"><div><h2 class="c-cta__title">还有拿不准的参数？</h2><p>选型、磁路与接口对接上的问题，欢迎直接找我们的技术团队确认。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
