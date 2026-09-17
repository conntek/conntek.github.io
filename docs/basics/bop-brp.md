---
title: "BOP / BRP 与回差 · 技术 Wiki"
description: "动作阈值与释放阈值，两者之差称为回差"
aside: false
pageClass: "c-page c-page--wiki"
---

<nav class="c-crumbs"><a href="/msite/">首页</a><i>/</i><a href="/msite/basics/">技术 Wiki</a><i>/</i><span>BOP / BRP 与回差</span></nav>

<p class="c-kicker">开关与线性器件</p>

# BOP / BRP 与回差

<p class="c-lead">动作阈值与释放阈值，两者之差称为回差</p>

## 是什么

BOP（operate point）是输出翻转到动作状态所需的磁通密度，BRP（release point）是恢复所需的磁通密度，两者之差称为回差（磁滞）。回差的作用是抑制阈值附近磁场抖动造成的输出反复跳变。

规格表通常按型号给出多档 BOP / BRP，并分别标出 N、S 两个方向对应的数值。单位常混用，1 mT = 10 Gs（高斯）。

## 怎么按最坏情况核算

**能否可靠动作**：磁体在动作位置、最大安装距离、最高温度、磁体批次下限时，芯片处的磁场仍大于 BOP 的最大值。

**能否可靠复位**：磁体在离开位置、最小安装距离、最低温度时，芯片处的磁场小于 BRP 的最小值。

动作点与复位点之间的行程差就是回差在机械上的体现：回差越大越抗抖动，但开关位置的重复性与灵敏度越差。

## 响应速度

微功耗开关按固定周期唤醒采样，磁场越过阈值到输出翻转之间最长可能相隔一个采样周期。测转速、计数时，要按最高磁极通过频率核对采样频率，避免漏计。

::: tip 要点提示
单位常混用，换算关系是 1 mT = 10 Gs（高斯）。选型要按最坏情况核算：用 BOP 的最大值校核能否可靠动作，用 BRP 的最小值校核能否可靠复位，不要拿典型值算裕量。
:::

## 常见误区

<p class="c-sec-lead">每条标题是常听到的说法，下方是工程上的实际情况。</p>

<div class="c-features c-pitfalls"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>按典型值算裕量</h3><p>阈值有批次与温度分布，动作用 BOP 最大值、复位用 BRP 最小值核算。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>回差越小越好</h3><p>回差太小，阈值附近的振动与噪声会让输出抖动。回差要与机械抖动幅度匹配。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>同一个档位字母在不同型号里含义相同</h3><p>档位代号是各系列自己的编号，具体数值以对应型号的规格表为准。</p></div></div></div>

## 相关系列

<p class="c-sec-lead">正文涉及的原理与指标，在这些产品系列上用得到。</p>

<div class="c-grid c-grid--3"><a class="c-card" href="/msite/products/switch/kth16"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth16.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH13/16/17 系列</span><h3>微功耗 1D 霍尔开关</h3><p>CMOS 工艺集成霍尔元件，1 μA 超低功耗，温度补偿优良，覆盖全极、单极与锁存型</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/switch/ktm13"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/ktm13.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM13 系列</span><h3>TMR 磁阻开关</h3><p>TMR 阻桥与 ASIC 单芯片集成，平行磁场感应，回差可小于 3 高斯</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/switch/kth25"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth25.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH25 系列</span><h3>车规级高压霍尔开关</h3><p>斩波技术（内置零漂移放大器），失调电压小于 10 μV，宽压工作，反接保护电压高达 -32 V</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/switch/ktm28"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/ktm28.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM28 系列</span><h3>AMR 高压气缸开关</h3><p>SIP 集成 AMR 与 ASIC，支持两线 / 三线气缸位置检测，任意极性感应水平磁场</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/switch/kth462"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth462.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH462 系列</span><h3>超灵敏 2D 霍尔开关</h3><p>检测二维磁场，两路独立数字输出，可直接给出速度与方向或每轴独立锁存信号</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/switch/kth460"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth460.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH460 系列</span><h3>微功耗 3D 霍尔开关</h3><p>X、Y、Z 三维全极检测，SPIN 与数字滤波技术保证稳定的工作点与开关频率</p><span class="c-card__more">查看产品</span></div></a></div>

## 相关词条

<div class="c-grid c-grid--3"><a class="c-card" href="/msite/basics/unipolar-omnipolar"><div class="c-card__body"><span class="c-card__kicker">开关与线性器件</span><h3>单极型 / 全极型</h3><p>按触发磁极区分：单极只认一个极，全极两极都认</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/latching"><div class="c-card__body"><span class="c-card__kicker">开关与线性器件</span><h3>锁存型 / Latch</h3><p>一个极性置位、相反极性复位，撤磁后保持原状态</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/chopper"><div class="c-card__body"><span class="c-card__kicker">磁敏原理</span><h3>斩波与旋转电流 / Chopper</h3><p>周期性切换激励或信号极性，把失调与低频漂移从信号里分离出去</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/tmr"><div class="c-card__body"><span class="c-card__kicker">磁敏原理</span><h3>TMR / 隧道磁电阻</h3><p>隧道结电阻随自由层与钉扎层的磁化夹角变化</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/linear-hall"><div class="c-card__body"><span class="c-card__kicker">开关与线性器件</span><h3>线性霍尔 / 比例式输出</h3><p>输出电压随磁通密度线性变化，灵敏度档位同时决定量程</p><span class="c-card__more">阅读词条</span></div></a></div>

<div class="c-wiki-pager">

<div class="c-grid c-grid--2"><a class="c-card" href="/msite/basics/latching"><div class="c-card__body"><span class="c-card__kicker">← 上一条</span><h3>锁存型 / Latch</h3><p>一个极性置位、相反极性复位，撤磁后保持原状态</p></div></a><a class="c-card" href="/msite/basics/linear-hall"><div class="c-card__body"><span class="c-card__kicker">下一条 →</span><h3>线性霍尔 / 比例式输出</h3><p>输出电压随磁通密度线性变化，灵敏度档位同时决定量程</p></div></a></div>

</div>

<div class="c-cta"><div><h2 class="c-cta__title">还有拿不准的参数？</h2><p>选型、磁路与接口对接上的问题，欢迎直接找我们的技术团队确认。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/msite/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
