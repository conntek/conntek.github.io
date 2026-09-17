---
title: "延时与动态误差 / Latency · 技术 Wiki"
description: "磁场变化到角度输出之间的时间，转速越高，它造成的角度滞后越大"
aside: false
pageClass: "c-page c-page--wiki"
---

<nav class="c-crumbs"><a href="/msite/">首页</a><i>/</i><a href="/msite/basics/">技术 Wiki</a><i>/</i><span>延时与动态误差 / Latency</span></nav>

<p class="c-kicker">精度、噪声与动态</p>

# 延时与动态误差 / Latency

<p class="c-lead">磁场变化到角度输出之间的时间，转速越高，它造成的角度滞后越大</p>

## 是什么

延时是从磁场变化到输出端给出对应角度之间的时间，由传感前端、ADC、角度解算、数字滤波与接口输出逐段累加。转动时，输出角度落后于真实角度，滞后量 = 角速度 × 延时。

例如 6000 rpm 即 36000 °/s，10 μs 延时对应约 0.36° 机械角滞后；对 4 对极电机换向，就是约 1.4° 电角度。

## 为什么台架上看不出来

静态精度通常在低速或停点下标定，此时角速度接近零，延时带来的滞后也接近零，所以器件在台架上「很准」，误差只在高速现场才出现。

手册上的「最高转速」通常表示内部跟踪不丢、输出不漏脉冲的上限，并不保证在该转速下角度精度仍等于静态指标。部分器件在内部按转速做延时补偿，匀速时滞后很小，但加减速期间的补偿效果要单独评估。

## 系统里还有哪些「延时」

**读取时刻**：串行接口读到的角度是在哪一刻采样的，取决于帧结构与主机读取的时序。中断打断、任务调度、多颗传感器轮询，都会让这段时间变得不固定，变成一个随转速放大的随机误差。

**采样对齐**：电机控制中电流在 PWM 周期的固定时刻采样，如果角度在另一个时刻读取，两者的时间差在数学上与传感器延时完全同形。先对齐采样时刻，往往比换更快的传感器便宜得多。

## 怎么评估

找出手册中延时的定义（是否含滤波、是否匀速条件），按最高工作转速与极对数折算一次滞后角，与静态精度比较；验收在目标转速下做，量端到端延时，而不只看芯片单项。

::: tip 要点提示
机械角滞后换算到电机换向时要乘极对数。极对数越多的电机，对编码器延时越敏感。
:::

## 常见误区

<p class="c-sec-lead">每条标题是常听到的说法，下方是工程上的实际情况。</p>

<div class="c-features c-pitfalls"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>标称最高转速下精度不变</h3><p>最高转速是跟踪边界，不是精度边界。高速下的滞后要按延时单独折算。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>延时是一个固定的数</h3><p>芯片内部延时可以很稳定，但主机读取时刻不固定时，系统看到的延时是一个分布，低速看不见，转速上来才暴露。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>角度滞后只能靠换更快的传感器解决</h3><p>先检查角度与电流采样是否在同一时刻、读取是否被中断打断。时序对齐通常只需改控制软件。</p></div></div></div>

## 相关系列

<p class="c-sec-lead">正文涉及的原理与指标，在这些产品系列上用得到。</p>

<div class="c-grid c-grid--3"><a class="c-card" href="/msite/products/encoder/kth78"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth78.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH78 系列</span><h3>低延时霍尔绝对角度编码器</h3><p>16 位分辨率，系统延时 1 μs 并做延时补偿，全系支持在轴与离轴应用</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/encoder/ktm59"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/ktm59.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM59 系列</span><h3>高速 TMR 磁编码器</h3><p>双 16 bit 2M SAR ADC，单对极细分 24 bit，最高 180,000 rpm</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/encoder/ktm52"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/ktm52.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM52 系列</span><h3>21 位高精度 AMR 角度编码器</h3><p>21 位分辨率，一键自校准后 INL ±0.015°（典型值），最高 60000 rpm</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/encoder/kth71"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth71.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH71 系列</span><h3>自校准霍尔磁编码器</h3><p>内置自动非线性校准（ANLC），无需复杂外部干预，在轴 INL 优于 ±0.1°</p><span class="c-card__more">查看产品</span></div></a></div>

## 相关词条

<div class="c-grid c-grid--3"><a class="c-card" href="/msite/basics/noise"><div class="c-card__body"><span class="c-card__kicker">精度、噪声与动态</span><h3>角度噪声 / Angle noise</h3><p>静止时角度读数的随机起伏，通常以 1σ（均方根）表示</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/spi-ssi"><div class="c-card__body"><span class="c-card__kicker">输出接口</span><h3>SPI / SSI 串行绝对值接口</h3><p>主控按时钟读走绝对角度的两种同步串行方式</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/uvw"><div class="c-card__body"><span class="c-card__kicker">输出接口</span><h3>UVW 换向输出</h3><p>三路互差 120° 电角度的方波，供电机换向定扇区</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/stray-field"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>杂散场 / Stray field</h3><p>靶磁铁以外叠加到芯片上的磁场，会改变合成磁场方向</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/resolution"><div class="c-card__body"><span class="c-card__kicker">精度、噪声与动态</span><h3>分辨率 / Resolution</h3><p>输出能区分的最小角度步距，与准确度是两回事</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/inl"><div class="c-card__body"><span class="c-card__kicker">精度、噪声与动态</span><h3>INL / 积分非线性</h3><p>输出角度对真实角度的最大偏差，即角度准确度</p><span class="c-card__more">阅读词条</span></div></a></div>

<div class="c-wiki-pager">

<div class="c-grid c-grid--2"><a class="c-card" href="/msite/basics/noise"><div class="c-card__body"><span class="c-card__kicker">← 上一条</span><h3>角度噪声 / Angle noise</h3><p>静止时角度读数的随机起伏，通常以 1σ（均方根）表示</p></div></a><a class="c-card" href="/msite/basics/self-calibration"><div class="c-card__body"><span class="c-card__kicker">下一条 →</span><h3>自校准 / Self-calibration</h3><p>器件在实装状态下测量并补偿角度非线性误差</p></div></a></div>

</div>

<div class="c-cta"><div><h2 class="c-cta__title">还有拿不准的参数？</h2><p>选型、磁路与接口对接上的问题，欢迎直接找我们的技术团队确认。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/msite/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
