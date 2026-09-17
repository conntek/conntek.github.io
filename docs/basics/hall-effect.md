---
title: "霍尔效应 / Hall effect · 技术 Wiki"
description: "载流薄片在垂直磁场下产生横向电压"
aside: false
pageClass: "c-page c-page--wiki"
---

<nav class="c-crumbs"><a href="/msite/">首页</a><i>/</i><a href="/msite/basics/">技术 Wiki</a><i>/</i><span>霍尔效应 / Hall effect</span></nav>

<p class="c-kicker">磁敏原理</p>

# 霍尔效应 / Hall effect

<p class="c-lead">载流薄片在垂直磁场下产生横向电压</p>

## 是什么

通有电流的半导体薄片受到垂直于片面的磁场时，洛伦兹力使载流子横向偏移，在两侧形成与磁通密度成正比的霍尔电压。

平面霍尔盘响应的是垂直于芯片表面的分量，可用标准 CMOS 工艺与放大、补偿、ADC 和数字电路集成在同一颗芯片内，成本低、线性好，是开关、线性传感器与角度编码器的通用基础。

## 它的短板与对策

霍尔元件灵敏度较低，输出信号在微伏到毫伏量级，工艺失配带来的失调电压与 1/f 噪声相对信号不可忽略，灵敏度还随温度变化。

对策是片上信号处理：旋转电流（spinning current）与斩波消除失调、温度补偿修正灵敏度漂移、多个霍尔元件差分排布抑制外部均匀场。器件级精度更多取决于这些处理，而不只是霍尔元件本身。

## 与磁阻器件怎么选

霍尔器件按磁场幅值工作，量程宽、不饱和、可以测三个方向（配合垂直霍尔），适合线性测量、宽气隙与三维检测；磁阻器件（AMR、TMR）灵敏度高、在饱和区只跟随方向，适合高信噪比测角与低场检测。实际选择还要看成本、功耗、温度范围与系统精度预算。

::: tip 要点提示
霍尔按磁场幅值工作，输出受温度与气隙影响较大，因此规格里普遍带有温度补偿以及失调抵消（如斩波、自旋电流）相关指标。
:::

## 常见误区

<p class="c-sec-lead">每条标题是常听到的说法，下方是工程上的实际情况。</p>

<div class="c-features c-pitfalls"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>霍尔元件就是惠斯通电桥</h3><p>电桥只是分析失调时用的等效模型。霍尔效应可以用旋转电流法消除失调，真正的电阻电桥做不到，这正是两者原理不同的标志。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>霍尔一定不如磁阻准</h3><p>系统精度由前端处理、校准、磁路与安装共同决定，不能只按敏感元件类型判断。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>一个霍尔元件能感应任意方向的磁场</h3><p>平面霍尔只感应垂直于芯片表面的分量，平面内分量需要垂直霍尔或磁通引导结构。</p></div></div></div>

## 相关系列

<p class="c-sec-lead">正文涉及的原理与指标，在这些产品系列上用得到。</p>

<div class="c-grid c-grid--3"><a class="c-card" href="/msite/products/switch/kth16"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth16.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH13/16/17 系列</span><h3>微功耗 1D 霍尔开关</h3><p>CMOS 工艺集成霍尔元件，1 μA 超低功耗，温度补偿优良，覆盖全极、单极与锁存型</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/switch/kth25"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth25.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH25 系列</span><h3>车规级高压霍尔开关</h3><p>斩波技术（内置零漂移放大器），失调电压小于 10 μV，宽压工作，反接保护电压高达 -32 V</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/switch/kth31"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth31.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH31 系列</span><h3>比例式线性霍尔传感器</h3><p>按比例响应磁通密度，30 kHz 高速带宽、轨到轨模拟输出，多灵敏度可选</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/switch/linear-hall"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/linear-hall.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH564 系列</span><h3>线性霍尔芯片</h3><p>零磁场输出 1/2 VCC，输出随磁通密度线性变化，多档灵敏度匹配不同检测范围</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/switch/kth460"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth460.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH460 系列</span><h3>微功耗 3D 霍尔开关</h3><p>X、Y、Z 三维全极检测，SPIN 与数字滤波技术保证稳定的工作点与开关频率</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/switch/kth462"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth462.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH462 系列</span><h3>超灵敏 2D 霍尔开关</h3><p>检测二维磁场，两路独立数字输出，可直接给出速度与方向或每轴独立锁存信号</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/3d-hall/kth57"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth57.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57 系列</span><h3>三轴线性霍尔传感器</h3><p>测量 X、Y、Z 三轴磁场，I2C / SPI 可选，工作模式在线配置，兼顾性能与功耗</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/encoder/kth78"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth78.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH78 系列</span><h3>低延时霍尔绝对角度编码器</h3><p>16 位分辨率，系统延时 1 μs 并做延时补偿，全系支持在轴与离轴应用</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/msite/products/encoder/kth71"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth71.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH71 系列</span><h3>自校准霍尔磁编码器</h3><p>内置自动非线性校准（ANLC），无需复杂外部干预，在轴 INL 优于 ±0.1°</p><span class="c-card__more">查看产品</span></div></a></div>

## 相关词条

<div class="c-grid c-grid--3"><a class="c-card" href="/msite/basics/chopper"><div class="c-card__body"><span class="c-card__kicker">磁敏原理</span><h3>斩波与旋转电流 / Chopper</h3><p>周期性切换激励或信号极性，把失调与低频漂移从信号里分离出去</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/vertical-hall"><div class="c-card__body"><span class="c-card__kicker">磁敏原理</span><h3>垂直霍尔 / Vertical Hall</h3><p>敏感方向落在芯片平面内的霍尔结构</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/3d-hall"><div class="c-card__body"><span class="c-card__kicker">磁敏原理</span><h3>三轴霍尔 / 3D Hall</h3><p>一颗芯片同时测 X、Y、Z 三个方向的磁场分量</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/linear-hall"><div class="c-card__body"><span class="c-card__kicker">开关与线性器件</span><h3>线性霍尔 / 比例式输出</h3><p>输出电压随磁通密度线性变化，灵敏度档位同时决定量程</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/amr"><div class="c-card__body"><span class="c-card__kicker">磁敏原理</span><h3>AMR / 各向异性磁阻</h3><p>电阻随磁化方向与电流夹角变化，工作在饱和区</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/tmr"><div class="c-card__body"><span class="c-card__kicker">磁敏原理</span><h3>TMR / 隧道磁电阻</h3><p>隧道结电阻随自由层与钉扎层的磁化夹角变化</p><span class="c-card__more">阅读词条</span></div></a></div>

<div class="c-wiki-pager">

<div class="c-grid c-grid--2"><a class="c-card" href="/msite/basics/pwm"><div class="c-card__body"><span class="c-card__kicker">← 上一条</span><h3>PWM 角度输出</h3><p>用固定频率方波的占空比表示绝对角度</p></div></a><a class="c-card" href="/msite/basics/chopper"><div class="c-card__body"><span class="c-card__kicker">下一条 →</span><h3>斩波与旋转电流 / Chopper</h3><p>周期性切换激励或信号极性，把失调与低频漂移从信号里分离出去</p></div></a></div>

</div>

<div class="c-cta"><div><h2 class="c-cta__title">还有拿不准的参数？</h2><p>选型、磁路与接口对接上的问题，欢迎直接找我们的技术团队确认。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/msite/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
