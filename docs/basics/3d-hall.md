---
title: "三轴霍尔 / 3D Hall · 技术 Wiki"
description: "一颗芯片同时测 X、Y、Z 三个方向的磁场分量"
aside: false
pageClass: "c-page c-page--wiki"
ld: "{\"@context\": \"https://schema.org\", \"@type\": \"DefinedTerm\", \"name\": \"三轴霍尔 / 3D Hall\", \"description\": \"一颗芯片同时测 X、Y、Z 三个方向的磁场分量\", \"inDefinedTermSet\": {\"@type\": \"DefinedTermSet\", \"name\": \"昆泰芯技术 Wiki\", \"url\": \"https://conntek.grosso.link/basics/\"}, \"url\": \"https://conntek.grosso.link/basics/3d-hall\"}"
---

<nav class="c-crumbs"><a href="/">首页</a><i>/</i><a href="/basics/">技术 Wiki</a><i>/</i><span>三轴霍尔 / 3D Hall</span></nav>

<p class="c-kicker">磁敏原理</p>

# 三轴霍尔 / 3D Hall

<p class="c-lead">一颗芯片同时测 X、Y、Z 三个方向的磁场分量</p>

## 是什么

三轴霍尔传感器在同一颗芯片上集成对三个正交方向敏感的霍尔结构（例如平面霍尔测 Z、垂直霍尔测 X 与 Y），加上放大、ADC 与数字接口，输出三个方向的磁通密度。有了三个分量，就可以计算磁场方向与强度，推算磁体的位置、角度或姿态。

## 适合做什么

摇杆与多向操作杆（两个倾角加按压）、旋钮与转盘、线性行程与到位检测、不同安装方式下的角度测量，以及磁场强度监测与防磁干扰检测。

三维开关类器件则在片内直接比较三个方向的磁场与阈值，输出开关量，省去主控计算，适合对方向不敏感的检测。

## 设计要点

**量程与灵敏度**：量程要覆盖最近距离下的最大磁场，同时保证最远位置仍有足够分辨率。

**工作模式**：采样率、平均次数与功耗可配置，电池设备常用低频唤醒测量，交互设备需要更高刷新率。

**校准**：三轴之间的灵敏度、失调与轴间正交误差，以及磁体本身的不均匀，都会进入位置计算。量产前应在最终结构里建立磁场与位置的对应关系。

::: tip 要点提示
用三轴霍尔推算位置时，先用磁场仿真或实测确认位置与三个分量之间是一一对应的，否则算法再好也会在某些位置出现多解。
:::

## 常见误区

<p class="c-sec-lead">每条标题是常听到的说法，下方是工程上的实际情况。</p>

<div class="c-features c-pitfalls"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>三轴数据直接反正切就是精确角度</h3><p>各轴灵敏度与失调不一致、磁场分布不理想时，需要校准与磁路匹配才能得到可用精度。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>灵敏度越高越好</h3><p>高灵敏度量程小，磁体稍微靠近就会超量程，要按磁体行程两端的场强选择。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>三个分量是同一时刻测的</h3><p>部分器件按顺序测量各轴，运动较快时轴间存在时间差，高速应用要确认测量时序。</p></div></div></div>

## 相关系列

<p class="c-sec-lead">正文涉及的原理与指标，在这些产品系列上用得到。</p>

<div class="c-grid c-grid--3"><a class="c-card" href="/products/3d-hall/kth57"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth57.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57 系列</span><h3>三轴线性霍尔传感器</h3><p>测量 X、Y、Z 三轴磁场，I2C / SPI 可选，工作模式在线配置，兼顾性能与功耗</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/3d-hall/kth55"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth55.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH55 系列</span><h3>垂直霍尔绝对角度传感器</h3><p>垂直霍尔配合 16 位 ADC，0 ~ 360° 绝对角度输出，符合 AEC-Q100</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/switch/kth460"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth460.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH460 系列</span><h3>微功耗 3D 霍尔开关</h3><p>X、Y、Z 三维全极检测，SPIN 与数字滤波技术保证稳定的工作点与开关频率</p><span class="c-card__more">查看产品</span></div></a></div>

## 相关词条

<div class="c-grid c-grid--3"><a class="c-card" href="/basics/vertical-hall"><div class="c-card__body"><span class="c-card__kicker">磁敏原理</span><h3>垂直霍尔 / Vertical Hall</h3><p>敏感方向落在芯片平面内的霍尔结构</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/hall-effect"><div class="c-card__body"><span class="c-card__kicker">磁敏原理</span><h3>霍尔效应 / Hall effect</h3><p>载流薄片在垂直磁场下产生横向电压</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/i2c"><div class="c-card__body"><span class="c-card__kicker">输出接口</span><h3>I2C 总线</h3><p>两线制（时钟 + 数据）的多器件总线，适合低速读写传感器数据与配置</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/linear-hall"><div class="c-card__body"><span class="c-card__kicker">开关与线性器件</span><h3>线性霍尔 / 比例式输出</h3><p>输出电压随磁通密度线性变化，灵敏度档位同时决定量程</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/chopper"><div class="c-card__body"><span class="c-card__kicker">磁敏原理</span><h3>斩波与旋转电流 / Chopper</h3><p>周期性切换激励或信号极性，把失调与低频漂移从信号里分离出去</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/amr"><div class="c-card__body"><span class="c-card__kicker">磁敏原理</span><h3>AMR / 各向异性磁阻</h3><p>电阻随磁化方向与电流夹角变化，工作在饱和区</p><span class="c-card__more">阅读词条</span></div></a></div>

<div class="c-wiki-pager">

<div class="c-grid c-grid--2"><a class="c-card" href="/basics/vertical-hall"><div class="c-card__body"><span class="c-card__kicker">← 上一条</span><h3>垂直霍尔 / Vertical Hall</h3><p>敏感方向落在芯片平面内的霍尔结构</p></div></a><a class="c-card" href="/basics/amr"><div class="c-card__body"><span class="c-card__kicker">下一条 →</span><h3>AMR / 各向异性磁阻</h3><p>电阻随磁化方向与电流夹角变化，工作在饱和区</p></div></a></div>

</div>

<div class="c-cta"><div><h2 class="c-cta__title">还有拿不准的参数？</h2><p>选型、磁路与接口对接上的问题，欢迎直接找我们的技术团队确认。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
