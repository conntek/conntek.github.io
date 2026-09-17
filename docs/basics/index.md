---
title: "技术 Wiki"
description: "磁传感与角度编码器的技术词条：安装、精度、接口、磁敏原理与开关器件，每条讲清是什么、为什么重要、怎么选与常见误区。"
aside: false
pageClass: "c-page c-page--wiki"
---

<nav class="c-crumbs"><a href="/msite/">首页</a><i>/</i><span>技术 Wiki</span></nav>

<p class="c-kicker">昆泰芯微电子</p>

# 技术 Wiki

<p class="c-lead">产品页里反复出现的术语，在这里逐条讲透：是什么、为什么重要、怎么装怎么选，以及工程上最常见的误区。</p>

<div class="c-stats"><div class="c-stat"><b>30</b><span>词条</span></div><div class="c-stat"><b>5</b><span>主题</span></div><div class="c-stat"><b>90</b><span>常见误区</span></div></div>

## 角度测量与安装

<p class="c-sec-lead">磁铁放在哪、离芯片多远、偏了多少、周围还有什么磁场，决定了芯片能读到多干净的信号。</p>

<div class="c-grid c-grid--3"><a class="c-card" href="/msite/basics/in-axis"><div class="c-card__body"><h3>在轴 / In-axis</h3><p>磁铁装在轴端，芯片感应中心与转轴同心</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/off-axis"><div class="c-card__body"><h3>离轴 / Off-axis</h3><p>芯片不在转轴中心，从磁铁或磁环侧面读取磁场</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/eccentricity"><div class="c-card__body"><h3>偏心与安装公差</h3><p>转动中心、磁铁中心与芯片感应中心不重合，是最常见的系统误差来源</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/air-gap"><div class="c-card__body"><h3>气隙 / Air gap</h3><p>磁铁工作面到芯片感应面之间的距离</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/magnet"><div class="c-card__body"><h3>磁体 / Magnet</h3><p>提供被测磁场的永磁体，看材料、充磁方式与几何公差三类参数</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/pole-pairs"><div class="c-card__body"><h3>对极数 / Pole pairs</h3><p>磁环沿圆周的 N-S 磁极对数，一对极为一个信号周期</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/stray-field"><div class="c-card__body"><h3>杂散场 / Stray field</h3><p>靶磁铁以外叠加到芯片上的磁场，会改变合成磁场方向</p><span class="c-card__more">阅读词条</span></div></a></div>

## 精度、噪声与动态

<p class="c-sec-lead">分辨率、精度、噪声、延时是四个不同的量。比较两颗器件之前，先确认比的是哪一个。</p>

<div class="c-grid c-grid--3"><a class="c-card" href="/msite/basics/resolution"><div class="c-card__body"><h3>分辨率 / Resolution</h3><p>输出能区分的最小角度步距，与准确度是两回事</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/inl"><div class="c-card__body"><h3>INL / 积分非线性</h3><p>输出角度对真实角度的最大偏差，即角度准确度</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/noise"><div class="c-card__body"><h3>角度噪声 / Angle noise</h3><p>静止时角度读数的随机起伏，通常以 1σ（均方根）表示</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/latency"><div class="c-card__body"><h3>延时与动态误差 / Latency</h3><p>磁场变化到角度输出之间的时间，转速越高，它造成的角度滞后越大</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/self-calibration"><div class="c-card__body"><h3>自校准 / Self-calibration</h3><p>器件在实装状态下测量并补偿角度非线性误差</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/vernier"><div class="c-card__body"><h3>游标 / Vernier（Nonius）</h3><p>用两条周期数不同的码道拼出高分辨率的单圈绝对位置</p><span class="c-card__more">阅读词条</span></div></a></div>

## 输出接口

<p class="c-sec-lead">角度怎么交给主控：增量脉冲、换向信号、串行绝对值、总线与 PWM，以及帧校验。</p>

<div class="c-grid c-grid--3"><a class="c-card" href="/msite/basics/absolute-incremental"><div class="c-card__body"><h3>绝对值输出 / 增量输出</h3><p>绝对值上电即知当前角度，增量只给出位移量</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/abz"><div class="c-card__body"><h3>ABZ 增量输出</h3><p>A、B 两路正交方波，加每圈一个 Z 索引脉冲</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/uvw"><div class="c-card__body"><h3>UVW 换向输出</h3><p>三路互差 120° 电角度的方波，供电机换向定扇区</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/spi-ssi"><div class="c-card__body"><h3>SPI / SSI 串行绝对值接口</h3><p>主控按时钟读走绝对角度的两种同步串行方式</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/crc"><div class="c-card__body"><h3>CRC 帧校验</h3><p>附在数据帧末尾的校验位，用来发现传输中出错的帧</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/i2c"><div class="c-card__body"><h3>I2C 总线</h3><p>两线制（时钟 + 数据）的多器件总线，适合低速读写传感器数据与配置</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/pwm"><div class="c-card__body"><h3>PWM 角度输出</h3><p>用固定频率方波的占空比表示绝对角度</p><span class="c-card__more">阅读词条</span></div></a></div>

## 磁敏原理

<p class="c-sec-lead">霍尔、垂直霍尔、三轴霍尔、AMR、TMR 各自感应哪个方向、怕什么、适合做什么。</p>

<div class="c-grid c-grid--3"><a class="c-card" href="/msite/basics/hall-effect"><div class="c-card__body"><h3>霍尔效应 / Hall effect</h3><p>载流薄片在垂直磁场下产生横向电压</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/chopper"><div class="c-card__body"><h3>斩波与旋转电流 / Chopper</h3><p>周期性切换激励或信号极性，把失调与低频漂移从信号里分离出去</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/vertical-hall"><div class="c-card__body"><h3>垂直霍尔 / Vertical Hall</h3><p>敏感方向落在芯片平面内的霍尔结构</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/3d-hall"><div class="c-card__body"><h3>三轴霍尔 / 3D Hall</h3><p>一颗芯片同时测 X、Y、Z 三个方向的磁场分量</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/amr"><div class="c-card__body"><h3>AMR / 各向异性磁阻</h3><p>电阻随磁化方向与电流夹角变化，工作在饱和区</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/tmr"><div class="c-card__body"><h3>TMR / 隧道磁电阻</h3><p>隧道结电阻随自由层与钉扎层的磁化夹角变化</p><span class="c-card__more">阅读词条</span></div></a></div>

## 开关与线性器件

<p class="c-sec-lead">开关型与线性霍尔的读法：极性逻辑、动作阈值、回差，以及灵敏度与量程的关系。</p>

<div class="c-grid c-grid--3"><a class="c-card" href="/msite/basics/unipolar-omnipolar"><div class="c-card__body"><h3>单极型 / 全极型</h3><p>按触发磁极区分：单极只认一个极，全极两极都认</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/latching"><div class="c-card__body"><h3>锁存型 / Latch</h3><p>一个极性置位、相反极性复位，撤磁后保持原状态</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/bop-brp"><div class="c-card__body"><h3>BOP / BRP 与回差</h3><p>动作阈值与释放阈值，两者之差称为回差</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/msite/basics/linear-hall"><div class="c-card__body"><h3>线性霍尔 / 比例式输出</h3><p>输出电压随磁通密度线性变化，灵敏度档位同时决定量程</p><span class="c-card__more">阅读词条</span></div></a></div>

<div class="c-cta"><div><h2 class="c-cta__title">还有拿不准的参数？</h2><p>选型、磁路与接口对接上的问题，欢迎直接找我们的技术团队确认。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/msite/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
