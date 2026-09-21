---
title: "自校准 / Self-calibration · 技术 Wiki"
description: "器件在实装状态下测量并补偿角度非线性误差"
aside: false
pageClass: "c-page c-page--wiki"
ld: "{\"@context\": \"https://schema.org\", \"@type\": \"DefinedTerm\", \"name\": \"自校准 / Self-calibration\", \"description\": \"器件在实装状态下测量并补偿角度非线性误差\", \"inDefinedTermSet\": {\"@type\": \"DefinedTermSet\", \"name\": \"昆泰芯技术 Wiki\", \"url\": \"https://conntek.github.io/basics/\"}, \"url\": \"https://conntek.github.io/basics/self-calibration\"}"
---

<nav class="c-crumbs"><a href="/">首页</a><i>/</i><a href="/basics/">技术 Wiki</a><i>/</i><span>自校准 / Self-calibration</span></nav>

<p class="c-kicker">精度、噪声与动态</p>

# 自校准 / Self-calibration

<p class="c-lead">器件在实装状态下测量并补偿角度非线性误差</p>

## 是什么

磁体与装配的不理想会让两路正弦、余弦信号出现失调、幅值不等与正交误差，并叠加谐波，表现为一圈内重复出现的角度误差。

自校准是在实际装配状态下转动，采集这些偏差、算出补偿参数并写入片内非易失存储器（EEPROM / MTP），之后实时修正输出角度，省去在产线上用外部高精度仪器逐台标定。

## 能补什么，不能补什么

**能补**：装配完成后固定不变、每圈重复出现的系统误差——信号失调、幅值失配、正交误差、磁铁偏心与充磁不均造成的周期误差。

**不能补**：随机噪声；随温度、负载、磨损变化的偏心与跳动；正反转回差；杂散场；高速下的延时滞后。这些要靠结构、磁路与系统时序解决。

## 怎么做

在最终结构、最终磁铁、最终气隙下执行，不要在临时工装上校准后再装进整机。按手册规定的转速范围、圈数与执行步骤操作，执行期间保持转动平稳，避免负载突变。

校准完成后要验证：在工作转速下复测一圈误差，确认改善达到预期。返修、更换磁铁、调整安装关系之后需要重做。

::: tip 要点提示
校准结果对应校准时的气隙、偏心与温度条件。返修、更换磁体或改动安装关系之后需要重做。校准只改善系统性误差，对随机噪声无效。
:::

## 常见误区

<p class="c-sec-lead">每条标题是常听到的说法，下方是工程上的实际情况。</p>

<div class="c-features c-pitfalls"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>校准一次永远有效</h3><p>校准结果绑定当时的气隙、偏心与磁铁。结构变动、更换零件或长期磨损后需要重新校准。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>执行条件差一点没关系</h3><p>手册规定的转速窗口与转动条件是校准成立的前提，条件不满足时结果可能不如不校准。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>校准后任何工况都一样准</h3><p>校准只改善静态的系统误差，对噪声、温漂变化的偏心和高速延时无效。</p></div></div></div>

## 相关系列

<p class="c-sec-lead">正文涉及的原理与指标，在这些产品系列上用得到。</p>

<div class="c-grid c-grid--3"><a class="c-card" href="/products/encoder/ktm52"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm52.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM52 系列</span><h3>21 位高精度 AMR 角度编码器</h3><p>21 位分辨率，一键自校准后 INL ±0.015°（典型值），最高 60000 rpm</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/encoder/ktm53"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm53.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM53 系列</span><h3>离轴 AMR 角度编码器</h3><p>AMR 配合垂直霍尔与数字算法实现离轴测量，校准后 INL ±0.03°（典型值）</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/encoder/ktm58"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm58.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM58 系列</span><h3>30 bit 绝对角度细分器</h3><p>最大 4096 对极输入，30 bit 绝对角度细分，适配磁电阻与光编、光栅、磁栅</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/encoder/ktm59"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm59.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM59 系列</span><h3>高速 TMR 磁编码器</h3><p>双 16 bit 2M SAR ADC，单对极细分 24 bit，最高 180,000 rpm</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/encoder/kth71"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth71.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH71 系列</span><h3>自校准霍尔磁编码器</h3><p>内置自动非线性校准（ANLC），无需复杂外部干预，在轴 INL 优于 ±0.1°</p><span class="c-card__more">查看产品</span></div></a></div>

## 相关词条

<div class="c-grid c-grid--3"><a class="c-card" href="/basics/inl"><div class="c-card__body"><span class="c-card__kicker">精度、噪声与动态</span><h3>INL / 积分非线性</h3><p>输出角度对真实角度的最大偏差，即角度准确度</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/eccentricity"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>偏心与安装公差</h3><p>转动中心、磁铁中心与芯片感应中心不重合，是最常见的系统误差来源</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/off-axis"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>离轴 / Off-axis</h3><p>芯片不在转轴中心，从磁铁或磁环侧面读取磁场</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/noise"><div class="c-card__body"><span class="c-card__kicker">精度、噪声与动态</span><h3>角度噪声 / Angle noise</h3><p>静止时角度读数的随机起伏，通常以 1σ（均方根）表示</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/resolution"><div class="c-card__body"><span class="c-card__kicker">精度、噪声与动态</span><h3>分辨率 / Resolution</h3><p>输出能区分的最小角度步距，与准确度是两回事</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/latency"><div class="c-card__body"><span class="c-card__kicker">精度、噪声与动态</span><h3>延时与动态误差 / Latency</h3><p>磁场变化到角度输出之间的时间，转速越高，它造成的角度滞后越大</p><span class="c-card__more">阅读词条</span></div></a></div>

<div class="c-wiki-pager">

<div class="c-grid c-grid--2"><a class="c-card" href="/basics/latency"><div class="c-card__body"><span class="c-card__kicker">← 上一条</span><h3>延时与动态误差 / Latency</h3><p>磁场变化到角度输出之间的时间，转速越高，它造成的角度滞后越大</p></div></a><a class="c-card" href="/basics/vernier"><div class="c-card__body"><span class="c-card__kicker">下一条 →</span><h3>游标 / Vernier（Nonius）</h3><p>用两条周期数不同的码道拼出高分辨率的单圈绝对位置</p></div></a></div>

</div>

<div class="c-cta"><div><h2 class="c-cta__title">还有拿不准的参数？</h2><p>选型、磁路与接口对接上的问题，欢迎直接找我们的技术团队确认。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
