---
title: "什么是 ABZ？KTH7816 做的很不错！"
description: "ABZ 接口是增量式编码器常见的输出格式。本文以 KTH7816 为例，介绍 A、B、Z 三个通道的定义，用时钟秒针类比解释方向判断与零点参考，并介绍 KTH7816 的 ABZ 输出特性与应用场景。"
outline: [2, 3]
pageClass: "c-page c-page--post"
---

<nav class="c-crumbs"><a href="/msite/">首页</a><i>/</i><a href="/msite/blog/">博客</a><i>/</i><span>什么是 ABZ？<a class="c-xref" href="/msite/products/encoder/kth78/kth7816-x-n-qn16">KTH7816</a> 做的很不错！</span></nav>

<p class="c-kicker">技术科普</p>

# 什么是 ABZ？KTH7816 做的很不错！

<p class="c-post-meta"><span>2023-09-08</span><span>·</span><span>昆泰芯微电子</span><span>·</span><span>阅读约 3 分钟</span></p>

<p class="c-lead">ABZ 接口是增量式编码器常见的输出格式。本文以 <a class="c-xref" href="/msite/products/encoder/kth78/kth7816-x-n-qn16">KTH7816</a> 为例，介绍 A、B、Z 三个通道的定义，用时钟秒针类比解释方向判断与零点参考，并介绍 <a class="c-xref" href="/msite/products/encoder/kth78/kth7816-x-n-qn16">KTH7816</a> 的 ABZ 输出特性与应用场景。</p>

<div class="c-takeaways"><b>本文要点</b><ul><li>A、B 通道输出正交脉冲，由变化顺序判断旋转方向</li><li>Z 通道每转输出一个脉冲，作为新周期的参考点</li><li><a class="c-xref" href="/msite/products/encoder/kth78/kth7816-x-n-qn16">KTH7816</a> 的 ABZ 输出默认最高频率 8 MHz，并加入磁滞抗噪</li></ul></div>

<figure class="c-blog-fig c-blog-fig--hero"><img src="/msite/blog/what-is-abz/11.webp" alt="什么是 ABZ？KTH7816 做的很不错！"></figure>

在工业自动化和电子控制领域中，传感器和编码器的接口标准至关重要。ABZ 接口是编码器输出的一种常见格式，经常被应用在多种工业设备中。在这篇文章中，我们将以 <a class="c-xref" href="/msite/products/encoder/kth78/kth7816-x-n-qn16">KTH7816</a> 编码器为实例详细介绍 ABZ 接口的定义，并使用时钟为例来形象解释其工作原理。

<figure class="c-blog-fig"><img src="/msite/blog/what-is-abz/1.webp" alt="KTH7816 说明书封面" loading="lazy"><figcaption><a class="c-xref" href="/msite/products/encoder/kth78/kth7816-x-n-qn16">KTH7816</a> 说明书封面</figcaption></figure>

## ABZ 接口简介

ABZ 是一种增量式编码器输出格式。编码器是一种传感器，能够将机械位置转换为电子信号。增量式编码器输出相对位置变化，而不是绝对位置。

ABZ 接口由三个通道组成：A、B 和 Z。A 和 B 通道输出正交脉冲，Z 通道（也称为零点或索引通道）在每个转动周期中输出一个脉冲。通过读取 A 和 B 通道的脉冲，可以确定旋转的方向和位置。而 Z 通道则提供一个参考点，用于确定绝对位置。

## 以时钟为例的形象解释

理解 ABZ 信号的工作原理，就像理解一个旋转的时钟面。时钟有时、分和秒针，但在此例中，我们将主要关注秒针和一个特殊的标记。

<figure class="c-blog-fig"><img src="/msite/blog/what-is-abz/6.webp" alt="时钟两根秒针相隔 1/4 秒示意" loading="lazy"><figcaption>时钟两根秒针相隔 1/4 秒示意</figcaption></figure>

### A 和 B 信号

- A 和 B 信号的相位差异：想象一下，你有一个特制的时钟，它有两个秒针：秒针 A（红色）和秒针 B（蓝色）。它们不是完全重合的，但它们总是有固定的时间差或「间隔」。
- 判断方向：假设你每次看秒针 A 移动后，秒针 B 都会紧随其后。当时钟正常转动时（顺时针），秒针 A 先经过一个特定点，然后 B 跟随经过。但是，如果时钟反向旋转，那么秒针 B 会首先通过该点，紧接着是秒针 A。
- 利用 A 和 B 信号的相位差异：正如你可以通过观察两个秒针的移动顺序来判断时钟是顺时针旋转还是逆时针旋转一样，编码器也可以通过观察 A 和 B 信号的变化顺序来判断其旋转方向。

### Z 信号

- 标记一个完整的循环：现在，在这个特制的时钟上，想象每当秒针 A 指向 12 点时，时钟上的一个特别的 LED 灯会亮一次。这个 LED 灯就代表 Z 信号，它为我们提供了一个清晰的参考，告诉我们何时开始一个新的旋转周期。
- 在编码器上的应用：每当编码器旋转一圈，Z 信号就发出一个脉冲，这提供了一个开始新周期的清晰点，使我们可以重新开始计数或重新定位。

ABZ 信号提供了编码器旋转方向和位置的完整信息。正如一个时钟能够为我们提供确切的时间信息一样，编码器通过 ABZ 信号为我们提供了精确的旋转信息。当这些信号被正确读取和解释时，它们使得对机器的精确控制成为可能。

<figure class="c-blog-fig"><img src="/msite/blog/what-is-abz/11.webp" alt="顺时针与逆时针旋转时的 ABZ 波形" loading="lazy"><figcaption>顺时针与逆时针旋转时的 ABZ 波形</figcaption></figure>

## KTH7816 ABZ 接口

<figure class="c-blog-fig"><img src="/msite/blog/what-is-abz/14.webp" alt="KTH7816 说明书中 ABZ 输出引脚说明" loading="lazy"><figcaption><a class="c-xref" href="/msite/products/encoder/kth78/kth7816-x-n-qn16">KTH7816</a> 说明书中 ABZ 输出引脚说明</figcaption></figure>

<a class="c-xref" href="/msite/products/encoder/kth78/kth7816-x-n-qn16">KTH7816</a> 是一款高性能的编码器，它具有 ABZ 输出。这意味着 <a class="c-xref" href="/msite/products/encoder/kth78/kth7816-x-n-qn16">KTH7816</a> 不仅能够提供位置信息，还能够提供旋转的方向和零点参考。此外，<a class="c-xref" href="/msite/products/encoder/kth78/kth7816-x-n-qn16">KTH7816</a> 的 ABZ 输出默认最高频率达到了业界最高水准的 8 MHz。客户可以根据需求选择一圈内有 4096 个 A 信号和 4096 个 B 信号，或者选择 4 ~ 4096 之间的任意整数。此外，为了确保高精度，<a class="c-xref" href="/msite/products/encoder/kth78/kth7816-x-n-qn16">KTH7816</a> 在设计中加入了磁滞来避免由于微小噪声引起的扰动。

<figure class="c-blog-fig"><img src="/msite/blog/what-is-abz/15.webp" alt="KTH7816 装在磁铁下方读出磁场角度" loading="lazy"><figcaption><a class="c-xref" href="/msite/products/encoder/kth78/kth7816-x-n-qn16">KTH7816</a> 装在磁铁下方读出磁场角度</figcaption></figure>

## KTH7816 的应用场景

凭借精确和可靠的 ABZ 输出，<a class="c-xref" href="/msite/products/encoder/kth78/kth7816-x-n-qn16">KTH7816</a> 可以为各种应用赋能：

- 自动化制造线：通过 ABZ 输出，机器臂可以精确移动到指定位置，确保高效和准确的组装。
- 电梯控制系统：<a class="c-xref" href="/msite/products/encoder/kth78/kth7816-x-n-qn16">KTH7816</a> 可以确保电梯准确停在所选楼层，提供更好的乘客体验。
- 数控机床：高精度的切割和雕刻得益于 <a class="c-xref" href="/msite/products/encoder/kth78/kth7816-x-n-qn16">KTH7816</a> 的精确位置反馈。
- 自动售货机：确保机械臂能够准确抓取所选产品，增加用户满意度。
- 自动化仓库：提高货物的选择和存储效率，减少错误，增加生产率。
- 风力涡轮机：优化叶片的位置，确保最大的能源输出。

ABZ 输出不仅提供了旋转的位置信息，还提供了方向和参考点。这些功能为许多应用提供了必要的反馈，确保了机器和设备的高效、安全和精确运行。而 <a class="c-xref" href="/msite/products/encoder/kth78/kth7816-x-n-qn16">KTH7816</a>，凭借其高性能的 ABZ 输出，确保了多种应用场景的优越表现。

<p class="c-post-source">本文首发于微信公众号「昆泰芯微电子」，2023-09-08。<a href="https://mp.weixin.qq.com/s/k3txrAS7LG1YgwCXCLtQWw" target="_blank" rel="noopener">查看原文</a></p>

<div class="c-grid c-grid--2"><a class="c-card" href="/msite/blog/kth78-coreless-motor"><div class="c-card__body"><span class="c-card__kicker">上一篇</span><h3>昆泰芯 KTH78 系列在空心杯领域的创新应用</h3><span class="c-card__more">阅读</span></div></a><a class="c-card" href="/msite/blog/kth5701-off-axis"><div class="c-card__body"><span class="c-card__kicker">下一篇</span><h3>离轴安装：昆泰芯 KTH5701/3D 霍尔芯片，让你的创意自由驰骋！</h3><span class="c-card__more">阅读</span></div></a></div>

## 同栏目文章

<div class="c-grid c-grid--3"><a class="c-card" href="/msite/blog/how-to-evaluate-magnetic-encoder-accuracy"><div class="c-card__media c-media--photo"><img src="/msite/img/tt/5.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">2023-10-31</span><h3>如何评价磁编的准确性？以昆泰芯 KTH78 为例</h3><p>很多工程师在测量物理量时容易混淆精度和可重复性。本文以打靶为例解释两者的区别，说明传感器噪声特性越好、可重复性越好，并以 KTH78 系列为例介绍其约 0.086° 的重复输出差异与多对极磁铁技术。</p><span class="c-card__more">阅读全文</span></div></a><a class="c-card" href="/msite/blog/crc-in-kth78"><div class="c-card__media c-media--photo"><img src="/msite/img/tt/9.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">2023-10-13</span><h3>数据的安全守护者：CRC 校验在 KTH78 系列中的应用</h3><p>KTH78 系列的 SPI 输出由 12 bit 位置数据和 4 bit CRC 校验码组成。本文用写信的比喻解释 CRC 校验码，再以 KTH7816 为例演示 CRC-4/ITU 的计算过程。</p><span class="c-card__more">阅读全文</span></div></a><a class="c-card" href="/msite/blog/hall-effect-explained"><div class="c-card__media c-media--photo"><img src="/msite/img/tt/14.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">2023-08-25</span><h3>神奇的霍尔效应</h3><p>霍尔效应源于洛伦兹力使载流子偏转并积累电荷，从而产生霍尔电压。本文介绍其物理原理，霍尔开关、线性霍尔、2D/3D 霍尔与高速霍尔编码器四类传感器及昆泰芯相关产品，并讨论霍尔传感器面临的技术挑战。</p><span class="c-card__more">阅读全文</span></div></a></div>

<div class="c-cta"><div><h2 class="c-cta__title">需要选型建议、样品或技术支持？</h2><p>昆泰芯提供芯片选型、磁场仿真与方案设计支持，欢迎与我们的销售和技术团队联系。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/msite/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
