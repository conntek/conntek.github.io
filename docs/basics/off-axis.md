---
title: "离轴 / Off-axis · 技术 Wiki"
description: "芯片不在转轴中心，从磁铁或磁环侧面读取磁场"
aside: false
pageClass: "c-page c-page--wiki"
---

<nav class="c-crumbs"><a href="/msite/">首页</a><i>/</i><a href="/msite/basics/">技术 Wiki</a><i>/</i><span>离轴 / Off-axis</span></nav>

<p class="c-kicker">角度测量与安装</p>

# 离轴 / Off-axis

<p class="c-lead">芯片不在转轴中心，从磁铁或磁环侧面读取磁场</p>

## 是什么

离轴（也称旁轴、侧轴）指芯片放在磁铁或磁环的外缘附近，读取切向、径向或轴向的磁场分量，适用于中空轴、穿轴走线以及轴端被占用的机械结构。

离轴位置上的磁场轨迹不是理想圆：两路分量的幅值与相位一般不相等，还叠加谐波，直接做反正切会得到一圈内周期性起伏的角度误差，需要经过校正才能达到与在轴接近的线性度。

## 为什么要用离轴

中空关节、电机后端要留出刹车与走线空间、旋钮与操作杆结构件占住中心线——这些场合在轴无解，只能离轴。

离轴还可以配合多对极磁环使用：芯片读到的是电角度，机械一圈对应多个周期，适合直接给电机换向提供电角度。

## 误差从哪来

**几何误差**：读取半径为 r、偏心量为 δ 时，机械角误差约为 δ/r 弧度量级，读取半径越小越敏感；换算到电角度还要乘极对数。

**磁场梯度**：离轴位置的磁场随位置变化陡，轴跳动、轴向窜动都会直接变成幅值与相位变化。

**杂散场**：离轴结构离电机、抱闸等干扰源往往更近，差分抗扰的前提（干扰场均匀）也更容易被破坏。

## 怎么装

按手册推荐的相对位置固定读取半径与轴向高度，尽量靠近磁环以提高场强；结构件要能长期保持这个位置，不随温度与负载变化。装配完成后在最终结构里做一次校准。

::: tip 要点提示
离轴对偏心的敏感度明显高于在轴，同样的装配公差带来的角度误差更大。规格表里在轴与离轴的 INL 通常分别给出，比较时不要混用。
:::

## 常见误区

<p class="c-sec-lead">每条标题是常听到的说法，下方是工程上的实际情况。</p>

<div class="c-features c-pitfalls"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>离轴天生不可靠</h3><p>离轴与在轴是两种误差模型，不是两个可靠性等级。真正要管住的是偏心量、跳动与杂散场，这些是可以设计和校正的。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>在轴的校准参数可以直接用于离轴</h3><p>两者的误差形式不同，混用模型可能越校越差。支架倾斜时还会出现半圈像在轴、半圈像离轴的中间状态，要按实测数据选择校正方式。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>离轴测出来比在轴差，就是离轴原理的问题</h3><p>先排查外因：附近被磁化的钢件、导磁支架、结构松动、测试台联轴器，都会让离轴结果变差。</p></div></div></div>

## 相关系列

<p class="c-sec-lead">正文涉及的原理与指标，在这些产品系列上用得到。</p>

<div class="c-grid c-grid--3"><a class="c-card" href="/msite/products/3d-hall/kth57"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth57.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57 系列</span><h3>三轴线性霍尔传感器</h3><p>测量 X、Y、Z 三轴磁场，I2C / SPI 可选，工作模式在线配置，兼顾性能与功耗</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/encoder/ktm53"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/ktm53.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM53 系列</span><h3>离轴 AMR 角度编码器</h3><p>AMR 配合垂直霍尔与数字算法实现离轴测量，校准后 INL ±0.03°（典型值）</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/encoder/ktm59"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/ktm59.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM59 系列</span><h3>高速 TMR 磁编码器</h3><p>双 16 bit 2M SAR ADC，单对极细分 24 bit，最高 180,000 rpm</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/encoder/kth78"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth78.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH78 系列</span><h3>低延时霍尔绝对角度编码器</h3><p>16 位分辨率，系统延时 1 μs 并做延时补偿，全系支持在轴与离轴应用</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/encoder/kth71"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth71.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH71 系列</span><h3>自校准霍尔磁编码器</h3><p>内置自动非线性校准（ANLC），无需复杂外部干预，在轴 INL 优于 ±0.1°</p><span class="c-card__more">查看产品</span></div></a></div>

## 相关词条

<div class="c-grid c-grid--3"><a class="c-card" href="/msite/basics/in-axis"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>在轴 / In-axis</h3><p>磁铁装在轴端，芯片感应中心与转轴同心</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/eccentricity"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>偏心与安装公差</h3><p>转动中心、磁铁中心与芯片感应中心不重合，是最常见的系统误差来源</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/pole-pairs"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>对极数 / Pole pairs</h3><p>磁环沿圆周的 N-S 磁极对数，一对极为一个信号周期</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/self-calibration"><div class="c-card__body"><span class="c-card__kicker">精度、噪声与动态</span><h3>自校准 / Self-calibration</h3><p>器件在实装状态下测量并补偿角度非线性误差</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/air-gap"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>气隙 / Air gap</h3><p>磁铁工作面到芯片感应面之间的距离</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/magnet"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>磁体 / Magnet</h3><p>提供被测磁场的永磁体，看材料、充磁方式与几何公差三类参数</p><span class="c-card__more">阅读词条</span></div></a></div>

<div class="c-wiki-pager">

<div class="c-grid c-grid--2"><a class="c-card" href="/msite/basics/in-axis"><div class="c-card__body"><span class="c-card__kicker">← 上一条</span><h3>在轴 / In-axis</h3><p>磁铁装在轴端，芯片感应中心与转轴同心</p></div></a><a class="c-card" href="/msite/basics/eccentricity"><div class="c-card__body"><span class="c-card__kicker">下一条 →</span><h3>偏心与安装公差</h3><p>转动中心、磁铁中心与芯片感应中心不重合，是最常见的系统误差来源</p></div></a></div>

</div>

<div class="c-cta"><div><h2 class="c-cta__title">还有拿不准的参数？</h2><p>选型、磁路与接口对接上的问题，欢迎直接找我们的技术团队确认。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/msite/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
