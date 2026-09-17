---
title: "磁体 / Magnet · 技术 Wiki"
description: "提供被测磁场的永磁体，看材料、充磁方式与几何公差三类参数"
aside: false
pageClass: "c-page c-page--wiki"
---

<nav class="c-crumbs"><a href="/msite/">首页</a><i>/</i><a href="/msite/basics/">技术 Wiki</a><i>/</i><span>磁体 / Magnet</span></nav>

<p class="c-kicker">角度测量与安装</p>

# 磁体 / Magnet

<p class="c-lead">提供被测磁场的永磁体，看材料、充磁方式与几何公差三类参数</p>

## 材料怎么选

钕铁硼剩磁高、温度系数约 -0.1 %/℃，高温下有不可逆退磁风险，要按最高工作温度选耐温等级；钐钴剩磁略低但温漂小、耐高温；铁氧体剩磁低、成本低、耐蚀性好。

烧结磁体剩磁高，粘接（注塑、橡胶）磁体易做复杂形状与多极，但剩磁较低、一致性要单独评估。用一种工艺的样品验证出来的结果，不能直接代替另一种工艺的方案验证。

## 充磁方式决定用法

对径（diametric）充磁的圆片或圆柱，一圈只有一对极，用于在轴单对极测角；沿圆周交替充磁的多极磁环用于离轴或多对极场合；轴向充磁的块状磁体多用于开关与到位检测。

「径向（radial）」指沿半径方向充磁，与对径充磁不是一回事，下料时容易搞错。

## 牌号之外还要管什么

牌号只规定剩磁、矫顽力与耐温，不规定**充磁均匀性**与**几何公差**，而这两项直接进入角度误差：充磁中心与几何中心不重合就是偏心，多极磁环各极宽度不一致就是极间误差。采购规格里要把这两项单独写明并抽检。

磁铁座与转轴的材料同样重要。铁素体、马氏体类不锈钢（例如 430）是导磁的，会分流和扭曲磁场；需要非导磁时应选奥氏体不锈钢、铝或工程塑料，并注意加工后可能残留的弱磁性。

::: tip 要点提示
磁体的温度系数会直接进入按幅值工作的器件（线性霍尔、开关阈值）的误差预算；只用磁场方向的角度器件受其影响很小。选型顺序是先看芯片规格给出的磁场检测范围，再反推磁体牌号与尺寸。
:::

## 常见误区

<p class="c-sec-lead">每条标题是常听到的说法，下方是工程上的实际情况。</p>

<div class="c-features c-pitfalls"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>牌号越高，角度越准</h3><p>牌号高只代表场更强、更耐温。角度精度取决于充磁均匀性、几何公差与安装，这些都不在牌号里。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>径向充磁就是对径充磁</h3><p>径向是沿半径方向，对径是沿直径方向一半 N 一半 S。单对极在轴测角需要的是对径充磁。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>不锈钢都不导磁</h3><p>430 等铁素体不锈钢是导磁的，用作转轴或磁铁座会显著改变磁场分布。</p></div></div></div>

## 相关系列

<p class="c-sec-lead">正文涉及的原理与指标，在这些产品系列上用得到。</p>

<div class="c-grid c-grid--3"><a class="c-card" href="/msite/products/encoder/ktm52"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/ktm52.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM52 系列</span><h3>21 位高精度 AMR 角度编码器</h3><p>21 位分辨率，一键自校准后 INL ±0.015°（典型值），最高 60000 rpm</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/encoder/ktm53"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/ktm53.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM53 系列</span><h3>离轴 AMR 角度编码器</h3><p>AMR 配合垂直霍尔与数字算法实现离轴测量，校准后 INL ±0.03°（典型值）</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/encoder/ktm59"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/ktm59.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM59 系列</span><h3>高速 TMR 磁编码器</h3><p>双 16 bit 2M SAR ADC，单对极细分 24 bit，最高 180,000 rpm</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/encoder/kth71"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth71.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH71 系列</span><h3>自校准霍尔磁编码器</h3><p>内置自动非线性校准（ANLC），无需复杂外部干预，在轴 INL 优于 ±0.1°</p><span class="c-card__more">查看产品</span></div></a></div>

## 相关词条

<div class="c-grid c-grid--3"><a class="c-card" href="/msite/basics/air-gap"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>气隙 / Air gap</h3><p>磁铁工作面到芯片感应面之间的距离</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/pole-pairs"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>对极数 / Pole pairs</h3><p>磁环沿圆周的 N-S 磁极对数，一对极为一个信号周期</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/eccentricity"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>偏心与安装公差</h3><p>转动中心、磁铁中心与芯片感应中心不重合，是最常见的系统误差来源</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/in-axis"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>在轴 / In-axis</h3><p>磁铁装在轴端，芯片感应中心与转轴同心</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/off-axis"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>离轴 / Off-axis</h3><p>芯片不在转轴中心，从磁铁或磁环侧面读取磁场</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/stray-field"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>杂散场 / Stray field</h3><p>靶磁铁以外叠加到芯片上的磁场，会改变合成磁场方向</p><span class="c-card__more">阅读词条</span></div></a></div>

<div class="c-wiki-pager">

<div class="c-grid c-grid--2"><a class="c-card" href="/msite/basics/air-gap"><div class="c-card__body"><span class="c-card__kicker">← 上一条</span><h3>气隙 / Air gap</h3><p>磁铁工作面到芯片感应面之间的距离</p></div></a><a class="c-card" href="/msite/basics/pole-pairs"><div class="c-card__body"><span class="c-card__kicker">下一条 →</span><h3>对极数 / Pole pairs</h3><p>磁环沿圆周的 N-S 磁极对数，一对极为一个信号周期</p></div></a></div>

</div>

<div class="c-cta"><div><h2 class="c-cta__title">还有拿不准的参数？</h2><p>选型、磁路与接口对接上的问题，欢迎直接找我们的技术团队确认。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/msite/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
