---
title: "气隙 / Air gap · 技术 Wiki"
description: "磁铁工作面到芯片感应面之间的距离"
aside: false
pageClass: "c-page c-page--wiki"
ld: "{\"@context\": \"https://schema.org\", \"@type\": \"DefinedTerm\", \"name\": \"气隙 / Air gap\", \"description\": \"磁铁工作面到芯片感应面之间的距离\", \"inDefinedTermSet\": {\"@type\": \"DefinedTermSet\", \"name\": \"昆泰芯技术 Wiki\", \"url\": \"https://conntek.grosso.link/basics/\"}, \"url\": \"https://conntek.grosso.link/basics/air-gap\"}"
---

<nav class="c-crumbs"><a href="/">首页</a><i>/</i><a href="/basics/">技术 Wiki</a><i>/</i><span>气隙 / Air gap</span></nav>

<p class="c-kicker">角度测量与安装</p>

# 气隙 / Air gap

<p class="c-lead">磁铁工作面到芯片感应面之间的距离</p>

## 是什么

气隙是磁铁工作面到芯片感应面的距离。它决定芯片处的磁通密度：永磁体的场随距离衰减很快，气隙增大会同时压低信号幅值与信噪比，因此它是角度精度、开关可靠动作与线性输出不失真的共同前提。

核算气隙要把封装厚度、感应面在封装内的深度、PCB 与外壳的装配公差一起计入，而不是只量磁铁到外壳的距离。

## 怎么定气隙

从芯片规格给出的**磁场检测范围**反推，并按两端最坏情况核算：

**场强下限**：最大气隙 + 最高工作温度 + 磁体批次下限，芯片处的场仍不低于规格下限。钕铁硼剩磁温度系数约为 -0.1 %/℃ 量级，高温下场强会明显下降。

**场强上限**：最小气隙 + 最低工作温度，场强不超过规格上限，线性器件不削顶。

气隙过小也有代价：磁场空间分布不均匀程度增大，对偏心更敏感，装配碰撞风险也更高。

## 不同原理对气隙的敏感度

按幅值工作的器件（线性霍尔、开关阈值）直接受气隙影响；只测磁场方向的角度器件（例如工作在饱和区的磁阻器件）在场强足够时对气隙变化更宽容。但场强一旦跌出规格范围，这个优势就不存在了。

::: tip 要点提示
工作在饱和区的磁阻类器件只跟随磁场方向，对气隙变化的容忍度高于按幅值工作的线性霍尔；但气隙过大、跌出规格给定的磁场检测范围之后，这一优势同样不成立。
:::

## 常见误区

<p class="c-sec-lead">每条标题是常听到的说法，下方是工程上的实际情况。</p>

<div class="c-features c-pitfalls"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>气隙越小越好</h3><p>场强可能超过规格上限，线性器件会削顶；磁场不均匀性与装配风险也随之增加。气隙应落在规格范围的中段并留出公差余量。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>量到外壳表面就是气隙</h3><p>芯片感应面在封装内部还有一段深度，PCB、焊料与支架也有厚度公差，都要算进去。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>只测方向的器件完全不在乎气隙</h3><p>场强低于器件最小工作磁场后，角度误差会快速增大，不是线性地「差一点」。</p></div></div></div>

## 相关系列

<p class="c-sec-lead">正文涉及的原理与指标，在这些产品系列上用得到。</p>

<div class="c-grid c-grid--3"><a class="c-card" href="/products/encoder/ktm52"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm52.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM52 系列</span><h3>21 位高精度 AMR 角度编码器</h3><p>21 位分辨率，一键自校准后 INL ±0.015°（典型值），最高 60000 rpm</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/encoder/ktm59"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm59.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM59 系列</span><h3>高速 TMR 磁编码器</h3><p>双 16 bit 2M SAR ADC，单对极细分 24 bit，最高 180,000 rpm</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/encoder/kth78"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth78.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH78 系列</span><h3>低延时霍尔绝对角度编码器</h3><p>16 位分辨率，系统延时 1 μs 并做延时补偿，全系支持在轴与离轴应用</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/encoder/kth71"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth71.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH71 系列</span><h3>自校准霍尔磁编码器</h3><p>内置自动非线性校准（ANLC），无需复杂外部干预，在轴 INL 优于 ±0.1°</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/switch/kth31"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth31.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH31 系列</span><h3>比例式线性霍尔传感器</h3><p>按比例响应磁通密度，30 kHz 高速带宽、轨到轨模拟输出，多灵敏度可选</p><span class="c-card__more">查看产品</span></div></a></div>

## 相关词条

<div class="c-grid c-grid--3"><a class="c-card" href="/basics/magnet"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>磁体 / Magnet</h3><p>提供被测磁场的永磁体，看材料、充磁方式与几何公差三类参数</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/in-axis"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>在轴 / In-axis</h3><p>磁铁装在轴端，芯片感应中心与转轴同心</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/amr"><div class="c-card__body"><span class="c-card__kicker">磁敏原理</span><h3>AMR / 各向异性磁阻</h3><p>电阻随磁化方向与电流夹角变化，工作在饱和区</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/linear-hall"><div class="c-card__body"><span class="c-card__kicker">开关与线性器件</span><h3>线性霍尔 / 比例式输出</h3><p>输出电压随磁通密度线性变化，灵敏度档位同时决定量程</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/off-axis"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>离轴 / Off-axis</h3><p>芯片不在转轴中心，从磁铁或磁环侧面读取磁场</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/eccentricity"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>偏心与安装公差</h3><p>转动中心、磁铁中心与芯片感应中心不重合，是最常见的系统误差来源</p><span class="c-card__more">阅读词条</span></div></a></div>

<div class="c-wiki-pager">

<div class="c-grid c-grid--2"><a class="c-card" href="/basics/eccentricity"><div class="c-card__body"><span class="c-card__kicker">← 上一条</span><h3>偏心与安装公差</h3><p>转动中心、磁铁中心与芯片感应中心不重合，是最常见的系统误差来源</p></div></a><a class="c-card" href="/basics/magnet"><div class="c-card__body"><span class="c-card__kicker">下一条 →</span><h3>磁体 / Magnet</h3><p>提供被测磁场的永磁体，看材料、充磁方式与几何公差三类参数</p></div></a></div>

</div>

<div class="c-cta"><div><h2 class="c-cta__title">还有拿不准的参数？</h2><p>选型、磁路与接口对接上的问题，欢迎直接找我们的技术团队确认。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
