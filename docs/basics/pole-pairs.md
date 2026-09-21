---
title: "对极数 / Pole pairs · 技术 Wiki"
description: "磁环沿圆周的 N-S 磁极对数，一对极为一个信号周期"
aside: false
pageClass: "c-page c-page--wiki"
ld: "{\"@context\": \"https://schema.org\", \"@type\": \"DefinedTerm\", \"name\": \"对极数 / Pole pairs\", \"description\": \"磁环沿圆周的 N-S 磁极对数，一对极为一个信号周期\", \"inDefinedTermSet\": {\"@type\": \"DefinedTermSet\", \"name\": \"昆泰芯技术 Wiki\", \"url\": \"https://conntek.grosso.link/basics/\"}, \"url\": \"https://conntek.grosso.link/basics/pole-pairs\"}"
---

<nav class="c-crumbs"><a href="/">首页</a><i>/</i><a href="/basics/">技术 Wiki</a><i>/</i><span>对极数 / Pole pairs</span></nav>

<p class="c-kicker">角度测量与安装</p>

# 对极数 / Pole pairs

<p class="c-lead">磁环沿圆周的 N-S 磁极对数，一对极为一个信号周期</p>

## 是什么

多对极磁环一圈有 p 对 N-S 极，传感器读到的是电角度：机械转一圈出现 p 个完全相同的信号周期。相同的细分位数下，极内的细分误差折算到机械角要除以 p，分辨率与重复性随之改善。

代价是电角度不唯一。仅凭一个多对极读头无法判断当前处在第几个周期，整圈绝对位置要靠索引信号、单对极通道、游标双码道或上电后的换向流程另行确定。

## 多对极能买到什么，买不到什么

能买到：更细的机械角分辨率；外部均匀干扰场造成的电角度误差折算到机械角后缩小 p 倍；直接为电机换向提供电角度。

买不到：磁环自身的分度误差（各极宽度不一致、充磁不均）不会被 p 分摊，它以机械一圈为周期直接叠加在结果上。多对极方案的精度上限由充磁精度决定，增加极对数换来的有效精度会打折扣，不能按 log₂p 位直接累加。

## 怎么选

给电机换向用时，常见做法是让磁环极对数与电机极对数一致，读到的电角度即可对应电机电周期，但零位偏置与方向仍需在装配后标定一次。

需要上电即知整圈位置、回零、限位或断电保持位置时，要叠加单对极通道、游标码道或参考开关。

芯片的感应元件间距与磁环极距要匹配，极距过小时单个感应元件本身就跨越了一大段磁极，信号幅值与谐波都会变差。

::: tip 要点提示
输入磁铁的对极数与 UVW 输出设定的对极数是两件事：后者按电机极对数配置，用于换向，不代表磁体本身的极数。
:::

## 常见误区

<p class="c-sec-lead">每条标题是常听到的说法，下方是工程上的实际情况。</p>

<div class="c-features c-pitfalls"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>p 对极就多拿 log₂p 位精度</h3><p>分辨率可以这样算，精度不行。极间误差来自充磁，不随极对数增加而消失。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>各对极的误差都一样</h3><p>各极的宽度与场强分布不同，误差按极对逐个变化，验收要覆盖整圈，不能只测一个极对。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>UVW 设置的对极数就是磁环的对极数</h3><p>UVW 的对极数按电机极对数设置，用于换向，与磁体本身的极数是两件事。</p></div></div></div>

## 相关系列

<p class="c-sec-lead">正文涉及的原理与指标，在这些产品系列上用得到。</p>

<div class="c-grid c-grid--3"><a class="c-card" href="/products/encoder/ktm58"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm58.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM58 系列</span><h3>30 bit 绝对角度细分器</h3><p>最大 4096 对极输入，30 bit 绝对角度细分，适配磁电阻与光编、光栅、磁栅</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/encoder/ktm59"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm59.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM59 系列</span><h3>高速 TMR 磁编码器</h3><p>双 16 bit 2M SAR ADC，单对极细分 24 bit，最高 180,000 rpm</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/encoder/kth78"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth78.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH78 系列</span><h3>低延时霍尔绝对角度编码器</h3><p>16 位分辨率，系统延时 1 μs 并做延时补偿，全系支持在轴与离轴应用</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/encoder/kth71"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth71.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH71 系列</span><h3>自校准霍尔磁编码器</h3><p>内置自动非线性校准（ANLC），无需复杂外部干预，在轴 INL 优于 ±0.1°</p><span class="c-card__more">查看产品</span></div></a></div>

## 相关词条

<div class="c-grid c-grid--3"><a class="c-card" href="/basics/vernier"><div class="c-card__body"><span class="c-card__kicker">精度、噪声与动态</span><h3>游标 / Vernier（Nonius）</h3><p>用两条周期数不同的码道拼出高分辨率的单圈绝对位置</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/uvw"><div class="c-card__body"><span class="c-card__kicker">输出接口</span><h3>UVW 换向输出</h3><p>三路互差 120° 电角度的方波，供电机换向定扇区</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/magnet"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>磁体 / Magnet</h3><p>提供被测磁场的永磁体，看材料、充磁方式与几何公差三类参数</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/eccentricity"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>偏心与安装公差</h3><p>转动中心、磁铁中心与芯片感应中心不重合，是最常见的系统误差来源</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/in-axis"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>在轴 / In-axis</h3><p>磁铁装在轴端，芯片感应中心与转轴同心</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/off-axis"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>离轴 / Off-axis</h3><p>芯片不在转轴中心，从磁铁或磁环侧面读取磁场</p><span class="c-card__more">阅读词条</span></div></a></div>

<div class="c-wiki-pager">

<div class="c-grid c-grid--2"><a class="c-card" href="/basics/magnet"><div class="c-card__body"><span class="c-card__kicker">← 上一条</span><h3>磁体 / Magnet</h3><p>提供被测磁场的永磁体，看材料、充磁方式与几何公差三类参数</p></div></a><a class="c-card" href="/basics/stray-field"><div class="c-card__body"><span class="c-card__kicker">下一条 →</span><h3>杂散场 / Stray field</h3><p>靶磁铁以外叠加到芯片上的磁场，会改变合成磁场方向</p></div></a></div>

</div>

<div class="c-cta"><div><h2 class="c-cta__title">还有拿不准的参数？</h2><p>选型、磁路与接口对接上的问题，欢迎直接找我们的技术团队确认。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
