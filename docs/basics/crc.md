---
title: "CRC 帧校验 · 技术 Wiki"
description: "附在数据帧末尾的校验位，用来发现传输中出错的帧"
aside: false
pageClass: "c-page c-page--wiki"
ld: "{\"@context\": \"https://schema.org\", \"@type\": \"DefinedTerm\", \"name\": \"CRC 帧校验\", \"description\": \"附在数据帧末尾的校验位，用来发现传输中出错的帧\", \"inDefinedTermSet\": {\"@type\": \"DefinedTermSet\", \"name\": \"昆泰芯技术 Wiki\", \"url\": \"https://conntek.grosso.link/basics/\"}, \"url\": \"https://conntek.grosso.link/basics/crc\"}"
---

<nav class="c-crumbs"><a href="/">首页</a><i>/</i><a href="/basics/">技术 Wiki</a><i>/</i><span>CRC 帧校验</span></nav>

<p class="c-kicker">输出接口</p>

# CRC 帧校验

<p class="c-lead">附在数据帧末尾的校验位，用来发现传输中出错的帧</p>

## 是什么

CRC（循环冗余校验）由发送端按约定的多项式对数据位计算出几位校验码附在帧尾，接收端用同样的规则重算并比对，不一致即判定这一帧在传输中出错。它能以很低的开销发现绝大多数突发误码。

## 对接时要对齐的四个参数

**多项式**、**初始值**、**覆盖范围**（只算角度位，还是连同状态位一起算）、**输出是否取反**。任何一个不一致，波形完全正确，校验却永远失败，或者偶尔碰巧通过。

还要确认写配置时是否也有校验。写方向没有校验时，主机写入后应读回比对，确认写入成功。

## 校验失败之后怎么办

丢弃出错帧，沿用上一帧或按速度外推一拍，同时计数；连续多帧失败或错误率超过阈值时上报故障。偶发出错不应直接停机，持续出错应进入安全状态。

CRC 只保护传输过程：它不能说明角度本身是否正确，也管不到采样时刻。传感器侧的磁场过弱、过强等异常要看帧内的状态位与诊断标志。

::: tip 要点提示
CRC 参数要写进接口文档并在主机侧做成可配置项，更换器件或固件版本时逐项核对。
:::

## 常见误区

<p class="c-sec-lead">每条标题是常听到的说法，下方是工程上的实际情况。</p>

<div class="c-features c-pitfalls"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>CRC 能纠正错误</h3><p>CRC 只负责发现错误，不负责纠正。出错帧要由主机决定丢弃、重读或外推。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>波形正常但 CRC 不过，一定是线路干扰</h3><p>更常见的原因是多项式、初始值、覆盖范围或取反参数与发送端不一致，先核对参数。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>CRC 通过就说明角度可信</h3><p>CRC 只说明这一帧没在路上被改写。磁场异常、内部故障要看状态位。</p></div></div></div>

## 相关系列

<p class="c-sec-lead">正文涉及的原理与指标，在这些产品系列上用得到。</p>

<div class="c-grid c-grid--3"><a class="c-card" href="/products/encoder/kth78"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth78.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH78 系列</span><h3>低延时霍尔绝对角度编码器</h3><p>16 位分辨率，系统延时 1 μs 并做延时补偿，全系支持在轴与离轴应用</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/encoder/kth71"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth71.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH71 系列</span><h3>自校准霍尔磁编码器</h3><p>内置自动非线性校准（ANLC），无需复杂外部干预，在轴 INL 优于 ±0.1°</p><span class="c-card__more">查看产品</span></div></a></div>

## 相关词条

<div class="c-grid c-grid--3"><a class="c-card" href="/basics/spi-ssi"><div class="c-card__body"><span class="c-card__kicker">输出接口</span><h3>SPI / SSI 串行绝对值接口</h3><p>主控按时钟读走绝对角度的两种同步串行方式</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/i2c"><div class="c-card__body"><span class="c-card__kicker">输出接口</span><h3>I2C 总线</h3><p>两线制（时钟 + 数据）的多器件总线，适合低速读写传感器数据与配置</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/absolute-incremental"><div class="c-card__body"><span class="c-card__kicker">输出接口</span><h3>绝对值输出 / 增量输出</h3><p>绝对值上电即知当前角度，增量只给出位移量</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/pwm"><div class="c-card__body"><span class="c-card__kicker">输出接口</span><h3>PWM 角度输出</h3><p>用固定频率方波的占空比表示绝对角度</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/abz"><div class="c-card__body"><span class="c-card__kicker">输出接口</span><h3>ABZ 增量输出</h3><p>A、B 两路正交方波，加每圈一个 Z 索引脉冲</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/uvw"><div class="c-card__body"><span class="c-card__kicker">输出接口</span><h3>UVW 换向输出</h3><p>三路互差 120° 电角度的方波，供电机换向定扇区</p><span class="c-card__more">阅读词条</span></div></a></div>

<div class="c-wiki-pager">

<div class="c-grid c-grid--2"><a class="c-card" href="/basics/spi-ssi"><div class="c-card__body"><span class="c-card__kicker">← 上一条</span><h3>SPI / SSI 串行绝对值接口</h3><p>主控按时钟读走绝对角度的两种同步串行方式</p></div></a><a class="c-card" href="/basics/i2c"><div class="c-card__body"><span class="c-card__kicker">下一条 →</span><h3>I2C 总线</h3><p>两线制（时钟 + 数据）的多器件总线，适合低速读写传感器数据与配置</p></div></a></div>

</div>

<div class="c-cta"><div><h2 class="c-cta__title">还有拿不准的参数？</h2><p>选型、磁路与接口对接上的问题，欢迎直接找我们的技术团队确认。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
