---
title: "杂散场 / Stray field · 技术 Wiki"
description: "靶磁铁以外叠加到芯片上的磁场，会改变合成磁场方向"
aside: false
pageClass: "c-page c-page--wiki"
ld: "{\"@context\": \"https://schema.org\", \"@type\": \"DefinedTerm\", \"name\": \"杂散场 / Stray field\", \"description\": \"靶磁铁以外叠加到芯片上的磁场，会改变合成磁场方向\", \"inDefinedTermSet\": {\"@type\": \"DefinedTermSet\", \"name\": \"昆泰芯技术 Wiki\", \"url\": \"https://conntek.github.io/basics/\"}, \"url\": \"https://conntek.github.io/basics/stray-field\"}"
---

<nav class="c-crumbs"><a href="/">首页</a><i>/</i><a href="/basics/">技术 Wiki</a><i>/</i><span>杂散场 / Stray field</span></nav>

<p class="c-kicker">角度测量与安装</p>

# 杂散场 / Stray field

<p class="c-lead">靶磁铁以外叠加到芯片上的磁场，会改变合成磁场方向</p>

## 是什么

芯片只能测到感应点处的总磁场，分不清哪一部分来自靶磁铁。电机绕组与永磁转子的漏磁、抱闸线圈、大电流线缆、相邻的其他磁铁、被磁化的钢件，乃至地磁场，都会作为杂散场叠加进来。

## 它怎么变成角度误差

一个与靶磁场垂直的均匀干扰场，会把合成方向拧过一个角度，误差约为 arctan(B干扰 / B靶)：干扰场是靶磁场的 2% 时，角度误差约 1.1°。

由此可以得出最直接的对策：**提高芯片处的靶磁场强度**，同样的干扰带来的误差成比例下降。

电机电流相关的干扰随负载变化，堵转、急加速时最严重，并且往往与电角度、电流方向相关，表现为结构化的周期误差，而不是随机噪声。

## 怎么抗

**差分（梯度）感应**：在几个位置感应磁场并相减，均匀的外部干扰场被大部分抵消。它对远处来的均匀场有效，对紧贴芯片、空间变化剧烈的近场干扰效果会打折。

**多对极磁环**：均匀干扰造成的电角度误差折算到机械角后缩小为 1/p，前提是干扰场远小于磁环工作场。

**布局与屏蔽**：拉开与干扰源的距离、让大电流线缆远离感应点。导磁屏蔽罩要离靶磁铁足够远，否则会吸走靶磁场、自身被磁化后反而变成新的干扰源。

## 怎么排查

保持同一转速，分别在电机不通电（外部拖动）与带载运行下测量角度误差。误差随电流、负载明显变化，或与电角度、扇区锁定，说明问题在电磁环境，不在芯片精度。

::: tip 要点提示
评估杂散场影响时，看的是干扰场与靶磁场的比值，而不是干扰场的绝对值。靶磁场越强，同样的干扰越不明显。
:::

## 常见误区

<p class="c-sec-lead">每条标题是常听到的说法，下方是工程上的实际情况。</p>

<div class="c-features c-pitfalls"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>磁编码器直接测磁场，对杂散场天然没有办法</h3><p>差分感应、提高靶场强、多对极与布局设计都是成熟手段，杂散场容限可以设计和验证。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>加一圈铁皮就屏蔽了</h3><p>距离不当的导磁罩会改变靶磁场分布，还可能被磁化。屏蔽方案要连同靶磁场一起仿真或实测。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>台架上精度合格，装到整机也一样</h3><p>台架通常没有电机电流、抱闸与大电流线缆，整机的杂散场只有在带载运行时才会出现。</p></div></div></div>

## 相关系列

<p class="c-sec-lead">正文涉及的原理与指标，在这些产品系列上用得到。</p>

<div class="c-grid c-grid--3"><a class="c-card" href="/products/encoder/kth78"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth78.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH78 系列</span><h3>低延时霍尔绝对角度编码器</h3><p>16 位分辨率，系统延时 1 μs 并做延时补偿，全系支持在轴与离轴应用</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/encoder/kth71"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth71.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH71 系列</span><h3>自校准霍尔磁编码器</h3><p>内置自动非线性校准（ANLC），无需复杂外部干预，在轴 INL 优于 ±0.1°</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/encoder/ktm52"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm52.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM52 系列</span><h3>21 位高精度 AMR 角度编码器</h3><p>21 位分辨率，一键自校准后 INL ±0.015°（典型值），最高 60000 rpm</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/encoder/ktm59"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm59.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM59 系列</span><h3>高速 TMR 磁编码器</h3><p>双 16 bit 2M SAR ADC，单对极细分 24 bit，最高 180,000 rpm</p><span class="c-card__more">查看产品</span></div></a></div>

## 相关词条

<div class="c-grid c-grid--3"><a class="c-card" href="/basics/air-gap"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>气隙 / Air gap</h3><p>磁铁工作面到芯片感应面之间的距离</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/pole-pairs"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>对极数 / Pole pairs</h3><p>磁环沿圆周的 N-S 磁极对数，一对极为一个信号周期</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/off-axis"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>离轴 / Off-axis</h3><p>芯片不在转轴中心，从磁铁或磁环侧面读取磁场</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/latency"><div class="c-card__body"><span class="c-card__kicker">精度、噪声与动态</span><h3>延时与动态误差 / Latency</h3><p>磁场变化到角度输出之间的时间，转速越高，它造成的角度滞后越大</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/in-axis"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>在轴 / In-axis</h3><p>磁铁装在轴端，芯片感应中心与转轴同心</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/eccentricity"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>偏心与安装公差</h3><p>转动中心、磁铁中心与芯片感应中心不重合，是最常见的系统误差来源</p><span class="c-card__more">阅读词条</span></div></a></div>

<div class="c-wiki-pager">

<div class="c-grid c-grid--2"><a class="c-card" href="/basics/pole-pairs"><div class="c-card__body"><span class="c-card__kicker">← 上一条</span><h3>对极数 / Pole pairs</h3><p>磁环沿圆周的 N-S 磁极对数，一对极为一个信号周期</p></div></a><a class="c-card" href="/basics/resolution"><div class="c-card__body"><span class="c-card__kicker">下一条 →</span><h3>分辨率 / Resolution</h3><p>输出能区分的最小角度步距，与准确度是两回事</p></div></a></div>

</div>

<div class="c-cta"><div><h2 class="c-cta__title">还有拿不准的参数？</h2><p>选型、磁路与接口对接上的问题，欢迎直接找我们的技术团队确认。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
