---
title: "在轴 / In-axis · 技术 Wiki"
description: "磁铁装在轴端，芯片感应中心与转轴同心"
aside: false
pageClass: "c-page c-page--wiki"
---

<nav class="c-crumbs"><a href="/msite/">首页</a><i>/</i><a href="/msite/basics/">技术 Wiki</a><i>/</i><span>在轴 / In-axis</span></nav>

<p class="c-kicker">角度测量与安装</p>

# 在轴 / In-axis

<p class="c-lead">磁铁装在轴端，芯片感应中心与转轴同心</p>

## 是什么

在轴安装指对径充磁（diametric，沿直径方向一半 N、一半 S）的圆片或圆柱磁铁装在轴端，芯片正对磁铁端面，其感应中心落在转轴的延长线上。磁铁转动时，芯片平面内得到两路幅值相等、相位差 90° 的正弦分量，角度由这两路分量的反正切得到。

单对极磁铁转一圈对应一个信号周期，不需要拼接即可给出 0 ~ 360° 的单圈绝对角度，上电即可读出当前位置。

## 为什么它的误差来源最少

感应点位于磁铁中心附近、磁场最对称的区域，两路分量天然等幅、正交，剩余误差主要来自偏心、倾斜与充磁不均，形态上以一圈一次、两次的低次谐波为主，校准模型简单。

这也意味着在轴精度的前提是「真的同心」。芯片感应中心一旦离开磁铁转动中心，两路分量就开始不等幅、不正交，误差形式向离轴靠拢。

## 怎么装

对准的是芯片的**感应中心**，不是封装外形中心。封装中心、晶圆（die）中心与感应中心可能是三个不同的点，感应中心的位置以数据手册的封装图为准。

磁铁直径相对芯片感应区留出余量，中心附近的均匀区越大，对偏心越宽容。转轴与磁铁座优先选用非导磁材料，或让导磁零件远离磁铁，否则磁通被分流、磁场被扭曲。

带中心通孔的环形磁铁，正对芯片的恰是没有磁体的区域：场强与均匀区都与实心磁铁不同，气隙和公差要按实际几何重新核算，不能沿用实心磁铁的经验值。

::: tip 要点提示
在轴的前提是轴端可用。轴要贯穿、或轴端已被联轴器、刹车、线束占据时，只能改用离轴。
:::

## 常见误区

<p class="c-sec-lead">每条标题是常听到的说法，下方是工程上的实际情况。</p>

<div class="c-features c-pitfalls"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>差不多对准就算在轴</h3><p>在轴与离轴的分界是感应中心是否落在转动中心上。偏出去的量越大，越要按离轴的误差模型评估，偏多少必须算出来，不能靠「看着对上了」。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>按封装外形居中贴装就对准了</h3><p>部分器件的感应中心有意偏离封装中心，按外形居中反而引入偏心。以手册标注的感应中心坐标为准。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>转轴贯通到芯片一侧也能做在轴</h3><p>芯片与转轴要占同一条中心线。轴必须穿过芯片所在位置时，只能改用离轴或中空轴方案。</p></div></div></div>

## 相关系列

<p class="c-sec-lead">正文涉及的原理与指标，在这些产品系列上用得到。</p>

<div class="c-grid c-grid--3"><a class="c-card" href="/msite/products/3d-hall/kth57"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth57.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57 系列</span><h3>三轴线性霍尔传感器</h3><p>测量 X、Y、Z 三轴磁场，I2C / SPI 可选，工作模式在线配置，兼顾性能与功耗</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/3d-hall/kth55"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth55.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH55 系列</span><h3>垂直霍尔绝对角度传感器</h3><p>垂直霍尔配合 16 位 ADC，0 ~ 360° 绝对角度输出，符合 AEC-Q100</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/encoder/ktm52"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/ktm52.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM52 系列</span><h3>21 位高精度 AMR 角度编码器</h3><p>21 位分辨率，一键自校准后 INL ±0.015°（典型值），最高 60000 rpm</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/encoder/ktm59"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/ktm59.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM59 系列</span><h3>高速 TMR 磁编码器</h3><p>双 16 bit 2M SAR ADC，单对极细分 24 bit，最高 180,000 rpm</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/encoder/kth78"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth78.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH78 系列</span><h3>低延时霍尔绝对角度编码器</h3><p>16 位分辨率，系统延时 1 μs 并做延时补偿，全系支持在轴与离轴应用</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/encoder/kth71"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth71.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH71 系列</span><h3>自校准霍尔磁编码器</h3><p>内置自动非线性校准（ANLC），无需复杂外部干预，在轴 INL 优于 ±0.1°</p><span class="c-card__more">查看产品</span></div></a></div>

## 相关词条

<div class="c-grid c-grid--3"><a class="c-card" href="/msite/basics/off-axis"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>离轴 / Off-axis</h3><p>芯片不在转轴中心，从磁铁或磁环侧面读取磁场</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/eccentricity"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>偏心与安装公差</h3><p>转动中心、磁铁中心与芯片感应中心不重合，是最常见的系统误差来源</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/air-gap"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>气隙 / Air gap</h3><p>磁铁工作面到芯片感应面之间的距离</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/magnet"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>磁体 / Magnet</h3><p>提供被测磁场的永磁体，看材料、充磁方式与几何公差三类参数</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/pole-pairs"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>对极数 / Pole pairs</h3><p>磁环沿圆周的 N-S 磁极对数，一对极为一个信号周期</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/stray-field"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>杂散场 / Stray field</h3><p>靶磁铁以外叠加到芯片上的磁场，会改变合成磁场方向</p><span class="c-card__more">阅读词条</span></div></a></div>

<div class="c-wiki-pager">

<div class="c-grid c-grid--2"><a class="c-card" href="/msite/basics/off-axis"><div class="c-card__body"><span class="c-card__kicker">下一条 →</span><h3>离轴 / Off-axis</h3><p>芯片不在转轴中心，从磁铁或磁环侧面读取磁场</p></div></a></div>

</div>

<div class="c-cta"><div><h2 class="c-cta__title">还有拿不准的参数？</h2><p>选型、磁路与接口对接上的问题，欢迎直接找我们的技术团队确认。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/msite/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
