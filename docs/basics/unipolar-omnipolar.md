---
title: "单极型 / 全极型 · 技术 Wiki"
description: "按触发磁极区分：单极只认一个极，全极两极都认"
aside: false
pageClass: "c-page c-page--wiki"
ld: "{\"@context\": \"https://schema.org\", \"@type\": \"DefinedTerm\", \"name\": \"单极型 / 全极型\", \"description\": \"按触发磁极区分：单极只认一个极，全极两极都认\", \"inDefinedTermSet\": {\"@type\": \"DefinedTermSet\", \"name\": \"昆泰芯技术 Wiki\", \"url\": \"https://conntek.github.io/basics/\"}, \"url\": \"https://conntek.github.io/basics/unipolar-omnipolar\"}"
---

<nav class="c-crumbs"><a href="/">首页</a><i>/</i><a href="/basics/">技术 Wiki</a><i>/</i><span>单极型 / 全极型</span></nav>

<p class="c-kicker">开关与线性器件</p>

# 单极型 / 全极型

<p class="c-lead">按触发磁极区分：单极只认一个极，全极两极都认</p>

## 是什么

单极型只在指定极性（单 N 极或单 S 极）的磁场超过阈值时动作，反向磁场不响应，适合磁极朝向固定、需要防止反向误触发的场合。

全极型对 N、S 任一极性达到阈值都动作，装配时不必区分磁体极性，常用于翻盖检测、到位检测、液位浮子这类只关心「有没有磁体靠近」的场合。

## 怎么选

先问这一路信号需不需要区分极性：只判断接近与离开，选全极型，装配最省心；要防止反装或反向磁场误触发，选单极型；要记住交替磁极、做计数或换向，选锁存型。

电池设备还要看平均工作电流与采样频率：微功耗开关按周期唤醒，采样频率越高，响应越快，平均电流也越大。

## 安装时注意

确认器件的感应方向（垂直于封装表面还是平行于封装表面），再决定磁体朝向；按最坏情况核算动作与复位距离，不用典型阈值计算。

::: tip 要点提示
单极与全极都是「来磁动作、去磁复位」，与锁存型的状态保持行为完全不同。互换时不能只比对阈值数值，要先确认动作逻辑一致。
:::

## 常见误区

<p class="c-sec-lead">每条标题是常听到的说法，下方是工程上的实际情况。</p>

<div class="c-features c-pitfalls"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>单极、全极、锁存只是阈值不同，可以互换</h3><p>三者的动作逻辑不同。锁存型撤磁后保持状态，单极、全极撤磁后复位，互换前先确认逻辑。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>全极型更高级，什么场合都用它</h3><p>需要区分极性或做换向的场合，全极型反而会出错。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>磁体朝向无所谓</h3><p>感应方向决定了哪个分量起作用，磁体转 90° 可能完全不动作。</p></div></div></div>

## 相关系列

<p class="c-sec-lead">正文涉及的原理与指标，在这些产品系列上用得到。</p>

<div class="c-grid c-grid--3"><a class="c-card" href="/products/switch/kth16"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth16.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH13/16/17 系列</span><h3>微功耗 1D 霍尔开关</h3><p>CMOS 工艺集成霍尔元件，1 μA 超低功耗，温度补偿优良，覆盖全极、单极与锁存型</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/switch/ktm13"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm13.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM13 系列</span><h3>TMR 磁阻开关</h3><p>TMR 阻桥与 ASIC 单芯片集成，平行磁场感应，回差可小于 3 高斯</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/switch/ktm28"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm28.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM28 系列</span><h3>AMR 高压气缸开关</h3><p>SIP 集成 AMR 与 ASIC，支持两线 / 三线气缸位置检测，任意极性感应水平磁场</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/switch/kth460"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth460.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH460 系列</span><h3>微功耗 3D 霍尔开关</h3><p>X、Y、Z 三维全极检测，SPIN 与数字滤波技术保证稳定的工作点与开关频率</p><span class="c-card__more">查看产品</span></div></a></div>

## 相关词条

<div class="c-grid c-grid--3"><a class="c-card" href="/basics/latching"><div class="c-card__body"><span class="c-card__kicker">开关与线性器件</span><h3>锁存型 / Latch</h3><p>一个极性置位、相反极性复位，撤磁后保持原状态</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/bop-brp"><div class="c-card__body"><span class="c-card__kicker">开关与线性器件</span><h3>BOP / BRP 与回差</h3><p>动作阈值与释放阈值，两者之差称为回差</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/chopper"><div class="c-card__body"><span class="c-card__kicker">磁敏原理</span><h3>斩波与旋转电流 / Chopper</h3><p>周期性切换激励或信号极性，把失调与低频漂移从信号里分离出去</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/tmr"><div class="c-card__body"><span class="c-card__kicker">磁敏原理</span><h3>TMR / 隧道磁电阻</h3><p>隧道结电阻随自由层与钉扎层的磁化夹角变化</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/linear-hall"><div class="c-card__body"><span class="c-card__kicker">开关与线性器件</span><h3>线性霍尔 / 比例式输出</h3><p>输出电压随磁通密度线性变化，灵敏度档位同时决定量程</p><span class="c-card__more">阅读词条</span></div></a></div>

<div class="c-wiki-pager">

<div class="c-grid c-grid--2"><a class="c-card" href="/basics/tmr"><div class="c-card__body"><span class="c-card__kicker">← 上一条</span><h3>TMR / 隧道磁电阻</h3><p>隧道结电阻随自由层与钉扎层的磁化夹角变化</p></div></a><a class="c-card" href="/basics/latching"><div class="c-card__body"><span class="c-card__kicker">下一条 →</span><h3>锁存型 / Latch</h3><p>一个极性置位、相反极性复位，撤磁后保持原状态</p></div></a></div>

</div>

<div class="c-cta"><div><h2 class="c-cta__title">还有拿不准的参数？</h2><p>选型、磁路与接口对接上的问题，欢迎直接找我们的技术团队确认。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
