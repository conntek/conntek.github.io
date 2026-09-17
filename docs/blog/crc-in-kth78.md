---
title: "数据的安全守护者：CRC 校验在 KTH78 系列中的应用"
description: "KTH78 系列的 SPI 输出由 12 bit 位置数据和 4 bit CRC 校验码组成。本文用写信的比喻解释 CRC 校验码，再以 KTH7816 为例演示 CRC-4/ITU 的计算过程。"
outline: [2, 3]
pageClass: "c-page c-page--post"
---

<nav class="c-crumbs"><a href="/msite/">首页</a><i>/</i><a href="/msite/about/">关于昆泰</a><i>/</i><a href="/msite/blog/">博客</a><i>/</i><span>数据的安全守护者：CRC 校验在 <a class="c-xref" href="/msite/products/encoder/kth78">KTH78</a> 系列中的应用</span></nav>

<p class="c-kicker">技术科普</p>

# 数据的安全守护者：CRC 校验在 KTH78 系列中的应用

<p class="c-post-meta"><span>2023-10-13</span><span>·</span><span>昆泰芯微电子</span><span>·</span><span>阅读约 3 分钟</span></p>

<p class="c-lead"><a class="c-xref" href="/msite/products/encoder/kth78">KTH78</a> 系列的 SPI 输出由 12 bit 位置数据和 4 bit CRC 校验码组成。本文用写信的比喻解释 CRC 校验码，再以 <a class="c-xref" href="/msite/products/encoder/kth78/kth7816-x-n-qn16">KTH7816</a> 为例演示 CRC-4/ITU 的计算过程。</p>

<div class="c-takeaways"><b>本文要点</b><ul><li>CRC 校验码按一定规则由全部内容算出，用来检查数据是否完整无误</li><li><a class="c-xref" href="/msite/products/encoder/kth78/kth7816-x-n-qn16">KTH7816</a> 的生成多项式为 X⁴ + X + 1，二进制表示为 10011</li><li><a class="c-xref" href="/msite/products/encoder/kth78">KTH78</a> 系列采用 CRC-4/ITU 标准，带输入反转和输出反转</li></ul></div>

<figure class="c-blog-fig c-blog-fig--hero"><img src="/msite/blog/crc-in-kth78/10.webp" alt="数据的安全守护者：CRC 校验在 KTH78 系列中的应用"></figure>

## CRC 校验的概念

想象你正在写一封重要的信，里面有你想告诉朋友的秘密代码。但是你担心这封信在传送过程中可能被风吹散，或者有人拿错了某一页。

为了确保你的朋友能准确无误地读到你的秘密代码，你决定在每一页的底部都写下一个小标记，这个标记是这一页上所有文字的字数。只要内容没错，计算出的字数就会与你写下的匹配。这样，你的朋友在阅读信时，只要检查每一页的内容与字数是否匹配，就可以确保这封信的内容是完整且没有错误的。

这里，信件的内容代表数据，而你写在每一页底部的标记就是 CRC 校验码。在信号传输领域更加复杂，并不是数字数，而是将所有内容按照一定规则算出来一个编码。

<figure class="c-blog-fig"><img src="/msite/blog/crc-in-kth78/2.webp" alt="KTH7816 SPI 输出帧格式" loading="lazy"><figcaption><a class="c-xref" href="/msite/products/encoder/kth78/kth7816-x-n-qn16">KTH7816</a> SPI 输出帧格式</figcaption></figure>

<a class="c-xref" href="/msite/products/encoder/kth78/kth7816-x-n-qn16">KTH7816</a> 说明书对 SPI 输出 CRC 校验的规定是：MISO 上的输出帧先是 12 bit 位置数据（MSB 在前），然后是 4 bit CRC 校验字；CRC 标准为 CRC-4/ITU，多项式为 X⁴ + X + 1，初始值为 00，结果异或值为 00，输入反转为 true，输出反转为 true。例如位置数据为 0FF 时，CRC 校验值为 2，接收到的数据为 0FF2。

## CRC 计算过程演示

以下演示 <a class="c-xref" href="/msite/products/encoder/kth78/kth7816-x-n-qn16">KTH7816</a> 的 CRC 计算过程。

### 输入数据

假设我们现在有一个 12 位的数据，其十六进制形式是「3EB」。转换为二进制后，它是：0011 1110 1011。

为了便于接下来的计算，我们需要将这 12 位数据补齐至 16 位。这样，我们的数据就变成了：0000 0011 1110 1011。

### 输入反转

在开始 CRC 计算之前，我们需要先对每 8 位的数据进行反转。原因是 CRC 算法需要从低位到高位进行计算。因此：

0000 0011 1110 1011 反转后为：1100 0000 1101 0111

### 生成多项式

CRC 是基于多项式运算的，所以我们需要一个多项式来进行计算。这个多项式在这里被称为「生成多项式」。

<a class="c-xref" href="/msite/products/encoder/kth78/kth7816-x-n-qn16">KTH7816</a> 的生成多项式是：X⁴ + X + 1。

这个多项式的意思是：1X⁴ + 0X³ + 0X² + 1X + 1

提取其系数后，我们可以得到这个多项式的二进制表示：10011。

### 异或除法

接下来，我们要进行异或除法。首先，我们将反转后的数据末尾加上 4 个 0，使其与多项式的位数对齐。然后开始异或运算，步骤如下：

1. 将数据与多项式对齐。
2. 进行异或运算。

<figure class="c-blog-fig"><img src="/msite/blog/crc-in-kth78/9.webp" alt="第一次对齐与异或运算" loading="lazy"><figcaption>第一次对齐与异或运算</figcaption></figure>

将得到的结果再与多项式对齐。重复上述步骤，直到所有位都进行了计算。

<figure class="c-blog-fig"><img src="/msite/blog/crc-in-kth78/10.webp" alt="逐位异或除法的完整过程" loading="lazy"><figcaption>逐位异或除法的完整过程</figcaption></figure>

### 输出反转

最后 1110 反转为 0111。注意一般大于 8 位的 CRC，依然是 8 位 8 位分别内部反转；对于这里 4 位 CRC，只在 4 位内反转。

### 最后输出

<a class="c-xref" href="/msite/products/encoder/kth78/kth7816-x-n-qn16">KTH7816</a> 最后会将 12 bit 原始数据与 4 bit CRC 结果连成一个 16 bit 数据，发送给用户：

0011 1110 1011 0111

## KTH78 的 CRC 校验

<a class="c-xref" href="/msite/products/encoder/kth78">KTH78</a> 系列产品以其先进的 CRC 校验功能著称。这一系列具有卓越的数据传输准确性和可靠性。它的 12 bit 位置数据提供了足够的精度，满足了大多数应用的需求，而 4 bit 的 CRC 校验确保了数据的完整性和真实性。

<a class="c-xref" href="/msite/products/encoder/kth78">KTH78</a> 系列也采用了 CRC-4/ITU 标准（上节计算演示就是基于此标准），这是一个广泛认可和使用的标准，提供了稳定和可靠的校验功能。与其他品牌的类似产品相比，<a class="c-xref" href="/msite/products/encoder/kth78">KTH78</a> 在数据处理速度和准确率方面都表现出色。

此外，其输入反转和输出反转的特点进一步增强了其校验功能，确保了即使在嘈杂的数据环境中，数据传输也不会出现错误。这种高度的精度和可靠性使 <a class="c-xref" href="/msite/products/encoder/kth78">KTH78</a> 系列成为了许多行业专家和技术人员的首选。

<p class="c-post-source">本文首发于微信公众号「昆泰芯微电子」，2023-10-13。<a href="https://mp.weixin.qq.com/s/tQmrBJUceExCsu5WR-ZCwA" target="_blank" rel="noopener">查看原文</a></p>

<div class="c-grid c-grid--2"><a class="c-card" href="/msite/blog/hall-sensor-automotive-switch"><div class="c-card__body"><span class="c-card__kicker">上一篇</span><h3>如何借助霍尔效应传感器打造车规级智能「开-关」监测系统</h3><span class="c-card__more">阅读</span></div></a><a class="c-card" href="/msite/blog/kth1601-door-sensor"><div class="c-card__body"><span class="c-card__kicker">下一篇</span><h3>智能门磁开关 KTH1601：守护家园的静默守卫</h3><span class="c-card__more">阅读</span></div></a></div>

## 同栏目文章

<div class="c-grid c-grid--3"><a class="c-card" href="/msite/blog/how-to-evaluate-magnetic-encoder-accuracy"><div class="c-card__media c-media--photo"><img src="/msite/img/tt/5.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">2023-10-31</span><h3>如何评价磁编的准确性？以昆泰芯 KTH78 为例</h3><p>很多工程师在测量物理量时容易混淆精度和可重复性。本文以打靶为例解释两者的区别，说明传感器噪声特性越好、可重复性越好，并以 KTH78 系列为例介绍其约 0.086° 的重复输出差异与多对极磁铁技术。</p><span class="c-card__more">阅读全文</span></div></a><a class="c-card" href="/msite/blog/what-is-abz"><div class="c-card__media c-media--photo"><img src="/msite/img/tt/12.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">2023-09-08</span><h3>什么是 ABZ？KTH7816 做的很不错！</h3><p>ABZ 接口是增量式编码器常见的输出格式。本文以 KTH7816 为例，介绍 A、B、Z 三个通道的定义，用时钟秒针类比解释方向判断与零点参考，并介绍 KTH7816 的 ABZ 输出特性与应用场景。</p><span class="c-card__more">阅读全文</span></div></a><a class="c-card" href="/msite/blog/hall-effect-explained"><div class="c-card__media c-media--photo"><img src="/msite/img/tt/14.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">2023-08-25</span><h3>神奇的霍尔效应</h3><p>霍尔效应源于洛伦兹力使载流子偏转并积累电荷，从而产生霍尔电压。本文介绍其物理原理，霍尔开关、线性霍尔、2D/3D 霍尔与高速霍尔编码器四类传感器及昆泰芯相关产品，并讨论霍尔传感器面临的技术挑战。</p><span class="c-card__more">阅读全文</span></div></a></div>

<div class="c-cta"><div><h2 class="c-cta__title">需要选型建议、样品或技术支持？</h2><p>昆泰芯提供芯片选型、磁场仿真与方案设计支持，欢迎与我们的销售和技术团队联系。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/msite/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
