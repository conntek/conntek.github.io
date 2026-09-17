---
title: "ABZ 增量输出 · 技术 Wiki"
description: "A、B 两路正交方波，加每圈一个 Z 索引脉冲"
aside: false
pageClass: "c-page c-page--wiki"
---

<nav class="c-crumbs"><a href="/msite/">首页</a><i>/</i><a href="/msite/basics/">技术 Wiki</a><i>/</i><span>ABZ 增量输出</span></nav>

<p class="c-kicker">输出接口</p>

# ABZ 增量输出

<p class="c-lead">A、B 两路正交方波，加每圈一个 Z 索引脉冲</p>

## 是什么

A、B 两路方波相位差 90°，对边沿计数得到位移，两路的先后顺序给出转向；四倍频后每个信号周期得到 4 步。Z（索引）每机械圈输出一个脉冲，用来确定圈内的参考点。

指标通常写成「线/圈」（PPR），四倍频后的「步/圈」是它的 4 倍，比较两颗器件时要先确认写的是哪个口径。

## 频率与接收端

单路 A 的频率 = 线数 × 转速(rpm) / 60。例如 4096 线、6000 rpm 时 A 相频率约 410 kHz，四倍频后的计数速率约 1.6 MHz。接收端的计数器带宽、光耦或隔离器的传输延迟、长线上的边沿变缓，都要按这个最坏频率核算。

长距离或强干扰环境下，一般配合差分线驱动（RS-422 电平）传输，接收端使用带迟滞的差分接收器。

## Z 脉冲宽度怎么选

Z 窄，回零位置定得准，但高速下脉冲持续时间极短，慢速接收端容易采丢；Z 宽，容易被捕获，但零点本身变得模糊。先确定 Z 给谁用（精确回零、换向粗定位、兼容旧驱动器），再按最高转速算出脉冲时长，与接收端最小可识别脉宽比较。

如果 Z 宽度按 LSB 个数配置，改变线数后它对应的物理角度和持续时间会跟着变。

::: tip 要点提示
脉冲频率等于线数乘以转速。高线数与高转速同时提出时，容易超过接收端的计数带宽，需要下调线数。
:::

## 常见误区

<p class="c-sec-lead">每条标题是常听到的说法，下方是工程上的实际情况。</p>

<div class="c-features c-pitfalls"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>线数就是四倍频后的步数</h3><p>PPR 是线数，步数是它的 4 倍。报价与验收时要写清口径。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>Z 脉冲就是机械零点</h3><p>Z 的位置可以配置，也可能因方向位、边沿选择与安装而偏移。回零精度要在系统里实测确认。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>回零偶尔失败是干扰问题</h3><p>先按最高转速算一下 Z 的持续时间，接收端来不及采是更常见、也更容易验证的原因。</p></div></div></div>

## 相关系列

<p class="c-sec-lead">正文涉及的原理与指标，在这些产品系列上用得到。</p>

<div class="c-grid c-grid--3"><a class="c-card" href="/msite/products/3d-hall/kth55"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth55.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH55 系列</span><h3>垂直霍尔绝对角度传感器</h3><p>垂直霍尔配合 16 位 ADC，0 ~ 360° 绝对角度输出，符合 AEC-Q100</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/encoder/ktm52"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/ktm52.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM52 系列</span><h3>21 位高精度 AMR 角度编码器</h3><p>21 位分辨率，一键自校准后 INL ±0.015°（典型值），最高 60000 rpm</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/encoder/ktm53"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/ktm53.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM53 系列</span><h3>离轴 AMR 角度编码器</h3><p>AMR 配合垂直霍尔与数字算法实现离轴测量，校准后 INL ±0.03°（典型值）</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/encoder/ktm58"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/ktm58.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM58 系列</span><h3>30 bit 绝对角度细分器</h3><p>最大 4096 对极输入，30 bit 绝对角度细分，适配磁电阻与光编、光栅、磁栅</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/encoder/ktm59"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/ktm59.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM59 系列</span><h3>高速 TMR 磁编码器</h3><p>双 16 bit 2M SAR ADC，单对极细分 24 bit，最高 180,000 rpm</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/encoder/kth78"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth78.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH78 系列</span><h3>低延时霍尔绝对角度编码器</h3><p>16 位分辨率，系统延时 1 μs 并做延时补偿，全系支持在轴与离轴应用</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/encoder/kth71"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth71.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH71 系列</span><h3>自校准霍尔磁编码器</h3><p>内置自动非线性校准（ANLC），无需复杂外部干预，在轴 INL 优于 ±0.1°</p><span class="c-card__more">查看产品</span></div></a></div>

## 相关词条

<div class="c-grid c-grid--3"><a class="c-card" href="/msite/basics/absolute-incremental"><div class="c-card__body"><span class="c-card__kicker">输出接口</span><h3>绝对值输出 / 增量输出</h3><p>绝对值上电即知当前角度，增量只给出位移量</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/uvw"><div class="c-card__body"><span class="c-card__kicker">输出接口</span><h3>UVW 换向输出</h3><p>三路互差 120° 电角度的方波，供电机换向定扇区</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/resolution"><div class="c-card__body"><span class="c-card__kicker">精度、噪声与动态</span><h3>分辨率 / Resolution</h3><p>输出能区分的最小角度步距，与准确度是两回事</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/latency"><div class="c-card__body"><span class="c-card__kicker">精度、噪声与动态</span><h3>延时与动态误差 / Latency</h3><p>磁场变化到角度输出之间的时间，转速越高，它造成的角度滞后越大</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/spi-ssi"><div class="c-card__body"><span class="c-card__kicker">输出接口</span><h3>SPI / SSI 串行绝对值接口</h3><p>主控按时钟读走绝对角度的两种同步串行方式</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/crc"><div class="c-card__body"><span class="c-card__kicker">输出接口</span><h3>CRC 帧校验</h3><p>附在数据帧末尾的校验位，用来发现传输中出错的帧</p><span class="c-card__more">阅读词条</span></div></a></div>

<div class="c-wiki-pager">

<div class="c-grid c-grid--2"><a class="c-card" href="/msite/basics/absolute-incremental"><div class="c-card__body"><span class="c-card__kicker">← 上一条</span><h3>绝对值输出 / 增量输出</h3><p>绝对值上电即知当前角度，增量只给出位移量</p></div></a><a class="c-card" href="/msite/basics/uvw"><div class="c-card__body"><span class="c-card__kicker">下一条 →</span><h3>UVW 换向输出</h3><p>三路互差 120° 电角度的方波，供电机换向定扇区</p></div></a></div>

</div>

<div class="c-cta"><div><h2 class="c-cta__title">还有拿不准的参数？</h2><p>选型、磁路与接口对接上的问题，欢迎直接找我们的技术团队确认。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/msite/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
