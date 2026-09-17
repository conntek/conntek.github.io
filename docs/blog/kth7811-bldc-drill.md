---
title: "KTH7811 简化电钻（BLDC）设计"
description: "传统电钻多用三个霍尔开关检测和控制无刷直流电机的转动，但多个霍尔开关使设计复杂，并带来对准、机械摩擦、开关损耗等维护难题。本文介绍 KTH7811 霍尔编码器如何替代三个霍尔开关，简化电钻设计。"
outline: [2, 3]
pageClass: "c-page c-page--post"
---

<nav class="c-crumbs"><a href="/msite/">首页</a><i>/</i><a href="/msite/about/">关于昆泰</a><i>/</i><a href="/msite/blog/">博客</a><i>/</i><span><a class="c-xref" href="/msite/products/encoder/kth78">KTH7811</a> 简化电钻（BLDC）设计</span></nav>

<p class="c-kicker">应用方案</p>

# KTH7811 简化电钻（BLDC）设计

<p class="c-post-meta"><span>2023-11-10</span><span>·</span><span>昆泰芯微电子</span><span>·</span><span>阅读约 4 分钟</span></p>

<p class="c-lead">传统电钻多用三个霍尔开关检测和控制无刷直流电机的转动，但多个霍尔开关使设计复杂，并带来对准、机械摩擦、开关损耗等维护难题。本文介绍 <a class="c-xref" href="/msite/products/encoder/kth78">KTH7811</a> 霍尔编码器如何替代三个霍尔开关，简化电钻设计。</p>

<div class="c-takeaways"><b>本文要点</b><ul><li>三个霍尔开关输出间隔 120° 的 U、V、W 信号，但布线复杂、成本高</li><li><a class="c-xref" href="/msite/products/encoder/kth78">KTH7811</a> 可模拟三个霍尔开关的功能，角度精确到 0.35°</li><li>除 UVW 输出外，还可通过 SPI/ABZ/PWM 输出更细致的角度信息</li></ul></div>

<figure class="c-blog-fig c-blog-fig--hero"><img src="/msite/blog/kth7811-bldc-drill/8.webp" alt="KTH7811 简化电钻（BLDC）设计"></figure>

## 电钻设计的挑战与突破

在日常家居和工业制造中，电钻作为一种广泛使用的功率工具，其性能的优劣直接关系到工作效率和结果的质量。传统的电钻设计多使用三个霍尔开关来检测和控制其无刷直流电机的转动。然而，使用多个霍尔开关不仅使得设计复杂，也带来了更多的维护难题，如对准问题、机械摩擦、开关损耗等。

近年来，技术的进步带来了许多创新性的解决方案，其中 <a class="c-xref" href="/msite/products/encoder/kth78">KTH78</a> 系列霍尔编码器便是其中的佼佼者。它以其先进的技术、高效的性能和卓越的可靠性，正在逐渐替代传统的多个霍尔开关设计，特别是 <a class="c-xref" href="/msite/products/encoder/kth78">KTH7811</a> 型号，在电钻设计中发挥了积极的作用。

<figure class="c-blog-fig"><img src="/msite/blog/kth7811-bldc-drill/2.webp" alt="电钻使用场景" loading="lazy"><figcaption>电钻使用场景</figcaption></figure>

## 传统霍尔开关的局限性

你知道电钻的心脏是什么吗？那就是无刷直流电机（BLDC），每次的旋转、每次的启动，都如同一首和谐的交响乐，离不开霍尔开关的精确指引。传统的设计理念告诉我们，三个线圈，三个霍尔开关，它们共同确保电机的流畅运转。

<figure class="c-blog-fig"><img src="/msite/blog/kth7811-bldc-drill/4.webp" alt="BLDC 电机运转示意图（图源搜狐）" loading="lazy"><figcaption>BLDC 电机运转示意图（图源搜狐）</figcaption></figure>

### 传统为什么需要三个开关

- 精确的转子位置信息：这是电机的指南针，每个霍尔开关为控制器勾画出一条清晰的信号线，共同组成间隔 120° 相位的 U、V、W 三个数字信号，让电机知道如何旋转，何时加速。
- 启动与运行的顺畅控制：每当你开启电钻，最多转过 120°，霍尔开关即刻知道如何开始，如何保持最佳的节奏和速度。
- 无浪费的电流供应：这三个开关确保每一次供电都是最高效的，每一次旋转都得到精确的供电，既节能又高效。

<figure class="c-blog-fig"><img src="/msite/blog/kth7811-bldc-drill/6.webp" alt="传统三霍尔开关布置示意" loading="lazy"><figcaption>传统三霍尔开关布置示意</figcaption></figure>

### 三个霍尔开关的局限

然而，每一枚硬币都有两面。三个霍尔开关的设计，虽然带来了精确控制，却也带来了它的局限性。

- 求简求短，但却变得复杂：三个开关意味着更多的组件，更复杂的布线。在追求简约与高效的今天，这似乎已经不再符合现代设计的理念。
- 美好的背后是隐忧：多余的部件可能导致更高的故障率，这意味着更多的维护，更频繁的保养。
- 每一分的价值，每一点的投入：增加的组件、更复杂的设计，都可能提高成本。这无疑增加了用户的购买压力。

我们开始寻找，寻找一个更为高效、简约、持久的解决方案。<a class="c-xref" href="/msite/products/encoder/kth78">KTH7811</a> 霍尔编码器，就是我们寻找的那个答案。

## 选择 KTH7811 的理由

<figure class="c-blog-fig"><img src="/msite/blog/kth7811-bldc-drill/8.webp" alt="单颗 KTH78XX 布置示意" loading="lazy"><figcaption>单颗 <a class="c-xref" href="/msite/products/encoder/kth78">KTH78XX</a> 布置示意</figcaption></figure>

<a class="c-xref" href="/msite/products/encoder/kth78">KTH7811</a> 的魔力，在于它不仅能够完美地模拟出传统三个霍尔开关的功能，更为出色的是，它能提供比它们更加精确的转子位置信息。传统霍尔开关，如同老式钟表，只能报时整点，而 <a class="c-xref" href="/msite/products/encoder/kth78">KTH7811</a> 则如同精密秒表，精确到 0.35°，每一秒，每一刻，都被精确捕捉。对于无刷直流电机或电钻来说，这意味着更加平稳的运转、更低的能耗、以及更高的效率。

更高的分辨率意味着在电机控制中带来了一系列积极的影响。高分辨率使得控制系统可以更精准地指导电机的运动，减少了运动中的震动和不稳定性，从而延长了设备的寿命。此外，高分辨率的角度测量也使得电机能够以更高的效率工作，因为它能够更精确地响应控制信号，避免了能量的浪费和不必要的电流消耗。这对于无刷直流电机或电钻等设备来说，意味着更加平稳的运转、更低的能耗，以及更高的整体效率。

当然，<a class="c-xref" href="/msite/products/encoder/kth78">KTH7811</a> 不仅仅是提供高分辨率。它摒弃了那些不必要的复杂性，剔除了传统三个霍尔开关可能带来的多余成本、更高的故障率、以及更复杂的布线设计。

在 <a class="c-xref" href="/msite/products/encoder/kth78">KTH78</a> 系列中，为何我们会毫不犹豫地选择 <a class="c-xref" href="/msite/products/encoder/kth78">KTH7811</a>？首先，它融合了该系列中最先进的技术，不仅提供了 UVW 输出，还可以通过 SPI/ABZ/PWM 等方式呈现更为细致的角度信息，使用户可以根据实际需求进行选择。<a class="c-xref" href="/msite/products/encoder/kth78">KTH7811</a> 不仅具备高精度和多样的输出接口，还在操作上极为简单，让用户能够迅速上手并体验其卓越性能。

在这个科技的浪潮中，选择 <a class="c-xref" href="/msite/products/encoder/kth78">KTH7811</a>，不仅仅是选择了一款霍尔编码器，更是选择了未来、简约与高效的完美结合。它为电机为代表的 BLDC 应用带来了不可估量的价值，将技术和创新的力量完美地融合，引领着现代科技的潮流。

## KTH78 系列产品

<figure class="c-blog-fig"><img src="/msite/blog/kth7811-bldc-drill/10.webp" alt="在轴、离轴与多对极磁铁安装方式" loading="lazy"><figcaption>在轴、离轴与多对极磁铁安装方式</figcaption></figure>

<a class="c-xref" href="/msite/products/encoder/kth78">KTH7811</a> 霍尔编码器为现代电钻设计提供了一个优越、高效和可靠的解决方案。这种技术不仅大大优化了设计，还提供了更好的性能和稳定性，将电钻的整体质量提升到了一个新的水平。

<figure class="c-blog-fig"><img src="/msite/blog/kth7811-bldc-drill/11.webp" alt="KTH78XX 全系列选型表" loading="lazy"><figcaption><a class="c-xref" href="/msite/products/encoder/kth78">KTH78XX</a> 全系列选型表</figcaption></figure>

<p class="c-post-source">本文首发于微信公众号「昆泰芯微电子」，2023-11-10。<a href="https://mp.weixin.qq.com/s/hW4Ha0DYa5d_N0WyQAGlkQ" target="_blank" rel="noopener">查看原文</a></p>

<div class="c-grid c-grid--2"><a class="c-card" href="/msite/blog/kth78-accuracy-and-low-latency"><div class="c-card__body"><span class="c-card__kicker">上一篇</span><h3>解密 KTH78 黑科技：为什么它精度高还能延迟低</h3><span class="c-card__more">阅读</span></div></a><a class="c-card" href="/msite/blog/kth7812-e-motorcycle"><div class="c-card__body"><span class="c-card__kicker">下一篇</span><h3>昆泰芯 KTH7812 在电摩应用中的优势</h3><span class="c-card__more">阅读</span></div></a></div>

## 同栏目文章

<div class="c-grid c-grid--3"><a class="c-card" href="/msite/blog/kth78-multipole-calibration"><div class="c-card__media c-media--photo"><img src="/msite/img/tt/0.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">2024-01-18</span><h3>昆泰芯 KTH78 系列编码器芯片：在多极对磁铁应用中的校准与精度提升</h3><p>精准的角度和位置检测是自动化和精密工程领域的决定性因素。本文介绍 KTH78 系列编码器芯片如何在多极对磁铁应用中进行高效校准，以及校准对提升系统精度的作用。</p><span class="c-card__more">阅读全文</span></div></a><a class="c-card" href="/msite/blog/kth78-high-torque-motor"><div class="c-card__media c-media--photo"><img src="/msite/img/tt/1.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">2023-12-29</span><h3>昆泰芯 KTH78 编码器在大扭矩电机中的应用</h3><p>本文以筋膜枪为例，探讨无感 FOC 控制电机在低速大扭矩工况下遇到的角度识别、电流控制、谐波损耗和振荡失稳问题，以及用 KTH78 系列霍尔角度编码器配合有感 FOC 控制应对这些挑战的方式。</p><span class="c-card__more">阅读全文</span></div></a><a class="c-card" href="/msite/blog/kth7812-e-motorcycle"><div class="c-card__media c-media--photo"><img src="/msite/img/tt/2.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">2023-12-04</span><h3>昆泰芯 KTH7812 在电摩应用中的优势</h3><p>在电摩的电机系统中，编码器通过精确监测电机转子的位置，优化扭矩输出、提高效率，并提升整体性能和行驶稳定性。本文从扭矩输出、效率和安全性等方面介绍 KTH7812 在电摩应用中的优势。</p><span class="c-card__more">阅读全文</span></div></a></div>

<div class="c-cta"><div><h2 class="c-cta__title">需要选型建议、样品或技术支持？</h2><p>昆泰芯提供芯片选型、磁场仿真与方案设计支持，欢迎与我们的销售和技术团队联系。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/msite/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
