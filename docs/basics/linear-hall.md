---
title: "线性霍尔 / 比例式输出 · 技术 Wiki"
description: "输出电压随磁通密度线性变化，灵敏度档位同时决定量程"
aside: false
pageClass: "c-page c-page--wiki"
ld: "{\"@context\": \"https://schema.org\", \"@type\": \"DefinedTerm\", \"name\": \"线性霍尔 / 比例式输出\", \"description\": \"输出电压随磁通密度线性变化，灵敏度档位同时决定量程\", \"inDefinedTermSet\": {\"@type\": \"DefinedTermSet\", \"name\": \"昆泰芯技术 Wiki\", \"url\": \"https://conntek.grosso.link/basics/\"}, \"url\": \"https://conntek.grosso.link/basics/linear-hall\"}"
---

<nav class="c-crumbs"><a href="/">首页</a><i>/</i><a href="/basics/">技术 Wiki</a><i>/</i><span>线性霍尔 / 比例式输出</span></nav>

<p class="c-kicker">开关与线性器件</p>

# 线性霍尔 / 比例式输出

<p class="c-lead">输出电压随磁通密度线性变化，灵敏度档位同时决定量程</p>

## 是什么

线性霍尔把磁通密度转换成连续变化的模拟电压。比例式（ratiometric）器件的零磁场输出在电源电压的一半附近，灵敏度与电源电压成正比，一个极性的磁场让输出升高，另一个极性让输出降低。

与电源成比例的好处是：如果 ADC 的参考电压取自同一电源，电源波动会在输出与参考中同时出现并被抵消。

## 灵敏度档位就是量程档位

输出只能在电源轨以内摆动，而且上下各有一段到不了轨的余量。可测磁场上限约为「零点到可用输出边界的电压 ÷ 灵敏度」：灵敏度越高，量程越小。同一系列里最灵敏的档位，磁铁稍微靠近就会削顶。

选型时先算出磁铁在行程两端、在最坏公差与温度下产生的场强，选一个量程能覆盖最大场、同时在最小变化量上仍有足够分辨率的档位。

## 误差预算

零点失调与温漂、灵敏度温漂、磁体剩磁温度系数（钕铁硼约 -0.1 %/℃ 量级）都会进入测量结果；按幅值测量的器件对气隙变化直接敏感。需要高精度时，可以用差分布置两颗传感器，或在系统里做两点、多点标定。

::: tip 要点提示
比例式输出配合同一电源做参考的 ADC 效果最好；若 ADC 参考与传感器电源不同源，电源波动会直接变成测量误差。
:::

## 常见误区

<p class="c-sec-lead">每条标题是常听到的说法，下方是工程上的实际情况。</p>

<div class="c-features c-pitfalls"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>灵敏度越高越好</h3><p>高灵敏度意味着小量程，磁场稍强就削顶，整段行程作废。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>换一个供电电压，量程与灵敏度都不变</h3><p>比例式器件的灵敏度随电源变化；输出到轨的余量是绝对电压，量程也不严格等比。以对应电压下的规格为准。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>输出电压只和磁铁位置有关</h3><p>磁体温度、气隙公差与电源电压都会改变输出，需要在全温度与公差范围内核算。</p></div></div></div>

## 相关系列

<p class="c-sec-lead">正文涉及的原理与指标，在这些产品系列上用得到。</p>

<div class="c-grid c-grid--3"><a class="c-card" href="/products/switch/kth31"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth31.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH31 系列</span><h3>比例式线性霍尔传感器</h3><p>按比例响应磁通密度，30 kHz 高速带宽、轨到轨模拟输出，多灵敏度可选</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/switch/linear-hall"><div class="c-card__media c-media--icon"><img src="/img/icons-web/linear-hall.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH564 系列</span><h3>线性霍尔芯片</h3><p>零磁场输出 1/2 VCC，输出随磁通密度线性变化，多档灵敏度匹配不同检测范围</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/3d-hall/kth57"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth57.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57 系列</span><h3>三轴线性霍尔传感器</h3><p>测量 X、Y、Z 三轴磁场，I2C / SPI 可选，工作模式在线配置，兼顾性能与功耗</p><span class="c-card__more">查看产品</span></div></a></div>

## 相关词条

<div class="c-grid c-grid--3"><a class="c-card" href="/basics/hall-effect"><div class="c-card__body"><span class="c-card__kicker">磁敏原理</span><h3>霍尔效应 / Hall effect</h3><p>载流薄片在垂直磁场下产生横向电压</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/air-gap"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>气隙 / Air gap</h3><p>磁铁工作面到芯片感应面之间的距离</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/chopper"><div class="c-card__body"><span class="c-card__kicker">磁敏原理</span><h3>斩波与旋转电流 / Chopper</h3><p>周期性切换激励或信号极性，把失调与低频漂移从信号里分离出去</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/3d-hall"><div class="c-card__body"><span class="c-card__kicker">磁敏原理</span><h3>三轴霍尔 / 3D Hall</h3><p>一颗芯片同时测 X、Y、Z 三个方向的磁场分量</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/unipolar-omnipolar"><div class="c-card__body"><span class="c-card__kicker">开关与线性器件</span><h3>单极型 / 全极型</h3><p>按触发磁极区分：单极只认一个极，全极两极都认</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/latching"><div class="c-card__body"><span class="c-card__kicker">开关与线性器件</span><h3>锁存型 / Latch</h3><p>一个极性置位、相反极性复位，撤磁后保持原状态</p><span class="c-card__more">阅读词条</span></div></a></div>

<div class="c-wiki-pager">

<div class="c-grid c-grid--2"><a class="c-card" href="/basics/bop-brp"><div class="c-card__body"><span class="c-card__kicker">← 上一条</span><h3>BOP / BRP 与回差</h3><p>动作阈值与释放阈值，两者之差称为回差</p></div></a></div>

</div>

<div class="c-cta"><div><h2 class="c-cta__title">还有拿不准的参数？</h2><p>选型、磁路与接口对接上的问题，欢迎直接找我们的技术团队确认。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
