---
title: "偏心与安装公差 · 技术 Wiki"
description: "转动中心、磁铁中心与芯片感应中心不重合，是最常见的系统误差来源"
aside: false
pageClass: "c-page c-page--wiki"
---

<nav class="c-crumbs"><a href="/msite/">首页</a><i>/</i><a href="/msite/basics/">技术 Wiki</a><i>/</i><span>偏心与安装公差</span></nav>

<p class="c-kicker">角度测量与安装</p>

# 偏心与安装公差

<p class="c-lead">转动中心、磁铁中心与芯片感应中心不重合，是最常见的系统误差来源</p>

## 是什么

偏心指三个中心不重合：转轴的转动中心、磁铁（或磁环）的几何与充磁中心、芯片的感应中心。与它一起出现的还有倾斜（磁铁平面与芯片平面不平行）、径向跳动与轴向窜动。

这些量来自一整条公差链：轴承游隙、磁铁座同心度、磁铁粘接位置、PCB 定位孔、芯片焊接后的偏移，以及外壳与支架的装配间隙。

## 它怎么变成角度误差

在轴单对极结构中，偏心主要贡献一圈一次的误差，倾斜与幅值失配多表现为一圈两次。

离轴与多对极磁环中，偏心量 δ 与读取半径 r 之比近似决定机械角误差（弧度量级为 δ/r），换算成电角度再乘极对数。例如 r = 10 mm、δ = 0.05 mm 时机械角误差约 0.3°，对 8 对极电机的换向就是约 2.3° 电角度。

机械偏心还会带来方向相关的误差：轴承间隙、联轴器回差在正转与反转时靠向不同一侧，同一个位置正反转读数不同。

## 怎么控制

磁路仿真与公差分析要输入**装配前的机械公差带**，而不是对准之后的残差，否则算出来的结果偏乐观。

校准能补掉装配完成后固定不变、每圈重复的那部分误差；随温度、负载、磨损变化的跳动补不掉，只能靠结构刚性与公差控制。

判断是否装配引起：拆装一次、换一个磁铁或换一个安装位置，误差曲线的一次、二次谐波明显变化，就是装配问题而不是芯片问题。

::: tip 要点提示
偏心误差对读取半径和极对数都敏感：离轴读取半径越小、极对数越多，同样的偏心量对换向电角度的影响越大。
:::

## 常见误区

<p class="c-sec-lead">每条标题是常听到的说法，下方是工程上的实际情况。</p>

<div class="c-features c-pitfalls"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>偏心可以全部校准掉</h3><p>只有可重复的部分能补。受热膨胀、负载与轴承游隙影响而每次不同的偏心，校准后仍会留在结果里。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>分辨率够高就能弥补安装误差</h3><p>分辨率只决定读数刻得多细，偏心带来的是读数与真实角度的系统偏差，位数再多也补不回来。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>测试台上的联轴器不影响测量结果</h3><p>参考编码器与被测轴之间的联轴器偏心、回差会原样叠加到测得的误差曲线里。评估芯片之前先确认测试台自身的误差。</p></div></div></div>

## 相关系列

<p class="c-sec-lead">正文涉及的原理与指标，在这些产品系列上用得到。</p>

<div class="c-grid c-grid--3"><a class="c-card" href="/msite/products/encoder/kth78"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth78.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH78 系列</span><h3>低延时霍尔绝对角度编码器</h3><p>16 位分辨率，系统延时 1 μs 并做延时补偿，全系支持在轴与离轴应用</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/encoder/kth71"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth71.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH71 系列</span><h3>自校准霍尔磁编码器</h3><p>内置自动非线性校准（ANLC），无需复杂外部干预，在轴 INL 优于 ±0.1°</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/encoder/ktm52"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/ktm52.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM52 系列</span><h3>21 位高精度 AMR 角度编码器</h3><p>21 位分辨率，一键自校准后 INL ±0.015°（典型值），最高 60000 rpm</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/encoder/ktm53"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/ktm53.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM53 系列</span><h3>离轴 AMR 角度编码器</h3><p>AMR 配合垂直霍尔与数字算法实现离轴测量，校准后 INL ±0.03°（典型值）</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/encoder/ktm59"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/ktm59.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM59 系列</span><h3>高速 TMR 磁编码器</h3><p>双 16 bit 2M SAR ADC，单对极细分 24 bit，最高 180,000 rpm</p><span class="c-card__more">查看产品</span></div></a></div>

## 相关词条

<div class="c-grid c-grid--3"><a class="c-card" href="/msite/basics/in-axis"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>在轴 / In-axis</h3><p>磁铁装在轴端，芯片感应中心与转轴同心</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/off-axis"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>离轴 / Off-axis</h3><p>芯片不在转轴中心，从磁铁或磁环侧面读取磁场</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/inl"><div class="c-card__body"><span class="c-card__kicker">精度、噪声与动态</span><h3>INL / 积分非线性</h3><p>输出角度对真实角度的最大偏差，即角度准确度</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/self-calibration"><div class="c-card__body"><span class="c-card__kicker">精度、噪声与动态</span><h3>自校准 / Self-calibration</h3><p>器件在实装状态下测量并补偿角度非线性误差</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/air-gap"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>气隙 / Air gap</h3><p>磁铁工作面到芯片感应面之间的距离</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/magnet"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>磁体 / Magnet</h3><p>提供被测磁场的永磁体，看材料、充磁方式与几何公差三类参数</p><span class="c-card__more">阅读词条</span></div></a></div>

<div class="c-wiki-pager">

<div class="c-grid c-grid--2"><a class="c-card" href="/msite/basics/off-axis"><div class="c-card__body"><span class="c-card__kicker">← 上一条</span><h3>离轴 / Off-axis</h3><p>芯片不在转轴中心，从磁铁或磁环侧面读取磁场</p></div></a><a class="c-card" href="/msite/basics/air-gap"><div class="c-card__body"><span class="c-card__kicker">下一条 →</span><h3>气隙 / Air gap</h3><p>磁铁工作面到芯片感应面之间的距离</p></div></a></div>

</div>

<div class="c-cta"><div><h2 class="c-cta__title">还有拿不准的参数？</h2><p>选型、磁路与接口对接上的问题，欢迎直接找我们的技术团队确认。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/msite/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
