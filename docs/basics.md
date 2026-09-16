---
title: "技术基础"
description: "产品页用到的角度测量、精度、接口与磁敏原理术语解释。"
aside: false
pageClass: "c-page"
---

<nav class="c-crumbs"><a href="/msite/">首页</a><i>/</i><span>技术基础</span></nav>

<p class="c-kicker">昆泰芯微电子</p>

# 技术基础

<p class="c-lead">产品页里反复出现的术语，在这里统一解释：怎么装、精度怎么算、接口怎么选、几种磁敏原理有什么区别。</p>

<div class="c-stats"><div class="c-stat"><b>5</b><span>主题</span></div><div class="c-stat"><b>20</b><span>术语</span></div></div>

## 角度测量与安装

<h3 id="in-axis">在轴 / In-axis</h3>

<p class="c-term-short">磁铁装在轴端，芯片正对磁铁端面、与转轴同心</p>

在轴安装指径向充磁的磁铁装在轴端，其旋转中心与芯片的感磁中心同轴。芯片读到的是磁铁端面正下方的旋转磁场矢量，在芯片平面内近似为两路幅值相等、相位差 90° 的正弦分量，角度由这两路分量的反正切得到。

在轴是角度测量中误差来源最少的装配方式：同轴度与气隙控制住之后，单对极磁铁转一圈对应一个信号周期，不需要拼接即可给出 0 ~ 360° 绝对角度。

<p class="c-note">在轴的前提是轴端可用。轴要贯穿、或轴端已被联轴器、刹车、线束占据时，只能改用离轴。</p>

<p class="c-term-rel"><b>相关系列</b><a href="/msite/products/3d-hall/kth57">KTH57 系列</a>、<a href="/msite/products/3d-hall/kth55">KTH55 系列</a>、<a href="/msite/products/encoder/ktm52">KTM52 系列</a>、<a href="/msite/products/encoder/ktm59">KTM59 系列</a>、<a href="/msite/products/encoder/kth78">KTH78 系列</a>、<a href="/msite/products/encoder/kth71">KTH71 系列</a></p>

<h3 id="off-axis">离轴 / Off-axis</h3>

<p class="c-term-short">芯片不在转轴中心，从磁铁或磁环侧面读取磁场</p>

离轴（也称旁轴）指芯片放在磁铁或磁环的外缘附近，读取切向与轴向的磁场分量，适用于中空轴、穿轴以及轴端被占用的机械结构。

离轴位置上的磁场轨迹不是理想圆：两路分量的幅值与相位一般不相等，直接做反正切会得到一圈内周期性起伏的角度误差，需要经过校正才能达到与在轴接近的线性度。

<p class="c-note">离轴对偏心的敏感度明显高于在轴，同样的装配公差带来的角度误差更大。规格表里在轴与离轴的 INL 通常分别给出，比较时不要混用。</p>

<p class="c-term-rel"><b>相关系列</b><a href="/msite/products/3d-hall/kth57">KTH57 系列</a>、<a href="/msite/products/encoder/ktm53">KTM53 系列</a>、<a href="/msite/products/encoder/ktm59">KTM59 系列</a>、<a href="/msite/products/encoder/kth78">KTH78 系列</a>、<a href="/msite/products/encoder/kth71">KTH71 系列</a></p>

<h3 id="pole-pairs">对极数 / Pole pairs</h3>

<p class="c-term-short">磁环沿圆周的 N-S 磁极对数，一对极为一个信号周期</p>

多对极磁环一圈有 p 对 N-S 极，传感器读到的是电角度：机械转一圈出现 p 个完全相同的信号周期。相同的细分位数下，多对极把机械角误差按 p 分摊，分辨率与重复性随之改善。

代价是电角度不唯一。仅凭一个多对极读头无法判断当前处在第几个周期，整圈绝对位置要靠索引信号、单对极通道或上电后的换向流程另行确定。

<p class="c-note">输入磁铁的对极数与 UVW 输出设定的对极数是两件事：后者按电机极对数配置，用于换向，不代表磁体本身的极数。</p>

<p class="c-term-rel"><b>相关系列</b><a href="/msite/products/encoder/ktm58">KTM58 系列</a>、<a href="/msite/products/encoder/ktm59">KTM59 系列</a>、<a href="/msite/products/encoder/kth78">KTH78 系列</a>、<a href="/msite/products/encoder/kth71">KTH71 系列</a></p>

<h3 id="air-gap">气隙 / Air gap</h3>

<p class="c-term-short">磁铁工作面到芯片感磁面之间的距离</p>

气隙决定芯片处的磁通密度。永磁体的场随距离衰减很快，气隙增大同时压低信号幅值与信噪比，因此它是角度精度与开关可靠动作共同的前提条件。

核算气隙要把封装厚度、感磁面在封装内的位置、PCB 与外壳的装配公差一起计入，而不是只量磁铁到外壳的距离。

<p class="c-note">工作在饱和区的磁阻类器件只跟随磁场方向，对气隙变化的容忍度高于按幅值工作的线性霍尔；但气隙过大、跌出规格给定的磁场检测范围之后，这一优势同样不成立。</p>

<h3 id="magnet">磁体 / Magnet</h3>

<p class="c-term-short">提供被测磁场的永磁体，看材料与充磁方式两类参数</p>

常用材料：钕铁硼剩磁高、温度系数约 -0.1 %/℃；钐钴剩磁略低但温漂小、耐高温；铁氧体剩磁低、成本低、耐蚀性好。

充磁方式决定用法：径向（diametric）充磁的圆片或圆柱用于在轴单对极测角；多极充磁磁环用于离轴或多对极场合；轴向充磁的块状磁体多用于开关与到位检测。

<p class="c-note">磁体的温度系数会直接进入按幅值工作的器件（线性霍尔、开关阈值）的误差预算；只用磁场方向的角度器件受其影响很小。选型顺序是先看芯片规格给出的磁场检测范围，再反推磁体牌号与尺寸。</p>

<p class="c-term-rel"><b>相关系列</b><a href="/msite/products/encoder/ktm52">KTM52 系列</a>、<a href="/msite/products/encoder/ktm53">KTM53 系列</a>、<a href="/msite/products/encoder/ktm59">KTM59 系列</a>、<a href="/msite/products/encoder/kth71">KTH71 系列</a></p>

## 精度与分辨率

<h3 id="resolution">分辨率 / Resolution</h3>

<p class="c-term-short">输出能区分的最小角度步距，与准确度是两回事</p>

分辨率由输出位数决定：n bit 对应一圈 2ⁿ 步，16 bit 约 0.0055°，21 bit 约 0.00017°。它只说明数字读数的刻度有多细，不说明这个读数离真实角度有多远——后者由 INL 描述。

<p class="c-note">当位数高于实际噪声水平时，最低几位是随机跳动的，不携带信息。判断能实际用到第几位，要同时看规格里的角度噪声（均方根值）。</p>

<p class="c-term-rel"><b>相关系列</b><a href="/msite/products/3d-hall/kth55">KTH55 系列</a>、<a href="/msite/products/encoder/ktm52">KTM52 系列</a>、<a href="/msite/products/encoder/ktm58">KTM58 系列</a>、<a href="/msite/products/encoder/ktm59">KTM59 系列</a>、<a href="/msite/products/encoder/kth78">KTH78 系列</a>、<a href="/msite/products/encoder/kto95">KTO95 系列</a></p>

<h3 id="inl">INL / 积分非线性</h3>

<p class="c-term-short">输出角度对真实角度的最大偏差，即角度准确度</p>

把一圈内每个位置的「读数减真值」画出来，扣掉零点偏置与增益后剩下的曲线，其峰值就是 INL，单位是角度。

它主要来自磁场不理想（充磁不均、装配偏心、离轴带来的椭圆化）与传感器两路通道之间的失配，形态上多表现为一圈内重复出现的低次谐波。

<p class="c-note">比较 INL 必须先对齐三件事：是否经过校准、在轴还是离轴、算的是单对极还是整圈。规格里常见的是「校准后 INL（典型值）」，与未校准值可能相差一个数量级。</p>

<p class="c-term-rel"><b>相关系列</b><a href="/msite/products/3d-hall/kth55">KTH55 系列</a>、<a href="/msite/products/encoder/ktm52">KTM52 系列</a>、<a href="/msite/products/encoder/ktm53">KTM53 系列</a>、<a href="/msite/products/encoder/ktm58">KTM58 系列</a>、<a href="/msite/products/encoder/ktm59">KTM59 系列</a>、<a href="/msite/products/encoder/kth78">KTH78 系列</a>、<a href="/msite/products/encoder/kth71">KTH71 系列</a></p>

<h3 id="self-calibration">自校准 / Self-calibration</h3>

<p class="c-term-short">器件在实装状态下测量并补偿角度非线性误差</p>

磁体与装配的不理想会让两路正弦、余弦信号出现失调、幅值不等与正交误差，表现为一圈内重复出现的角度误差。

自校准是在实际装配状态下转动采集这些偏差、算出补偿参数并写入片内非易失存储器（EEPROM / MTP），之后实时修正输出角度，省去在产线上用外部仪器逐台标定。

<p class="c-note">校准结果对应校准时的气隙、偏心与温度条件。返修、更换磁体或改动安装关系之后需要重做。校准只改善系统性误差，对随机噪声无效。</p>

<p class="c-term-rel"><b>相关系列</b><a href="/msite/products/encoder/ktm52">KTM52 系列</a>、<a href="/msite/products/encoder/ktm53">KTM53 系列</a>、<a href="/msite/products/encoder/ktm58">KTM58 系列</a>、<a href="/msite/products/encoder/ktm59">KTM59 系列</a>、<a href="/msite/products/encoder/kth71">KTH71 系列</a></p>

## 输出接口

<h3 id="absolute-incremental">绝对值输出 / 增量输出</h3>

<p class="c-term-short">绝对值上电即知当前角度，增量只给出位移量</p>

绝对值输出（SPI、SSI、PWM）任何时刻读到的都是当前角度本身，断电再上电不必回零。增量输出（ABZ、UVW）给的是脉冲，位置由接收端累加，上电时位置未知，需要回零或找到索引脉冲。

多数角度编码器芯片两类输出同时具备，可以一边接驱动器的增量口、一边接主控的串行口。

<p class="c-note">增量口的位置是接收端算出来的，一旦丢脉冲，误差会一直累积下去直到下一次索引；绝对值口不存在累积误差。</p>

<p class="c-term-rel"><b>相关系列</b><a href="/msite/products/3d-hall/kth55">KTH55 系列</a>、<a href="/msite/products/encoder/ktm52">KTM52 系列</a>、<a href="/msite/products/encoder/ktm53">KTM53 系列</a>、<a href="/msite/products/encoder/ktm58">KTM58 系列</a>、<a href="/msite/products/encoder/ktm59">KTM59 系列</a>、<a href="/msite/products/encoder/kth78">KTH78 系列</a>、<a href="/msite/products/encoder/kth71">KTH71 系列</a>、<a href="/msite/products/encoder/kto95">KTO95 系列</a></p>

<h3 id="abz">ABZ 增量输出</h3>

<p class="c-term-short">A、B 两路正交方波，加每圈一个 Z 索引脉冲</p>

A、B 两路方波相位差 90°，对边沿计数得到位移，两路的先后顺序给出转向；四倍频后每个信号周期得到 4 步。Z（索引）每机械圈输出一个脉冲，用来确定圈内的绝对参考点。

指标通常写成「线/圈」（PPR），四倍频后的「步/圈」是它的 4 倍，比较两颗器件时要先确认写的是哪个口径。

<p class="c-note">脉冲频率等于线数乘以转速。高线数与高转速同时提出时，容易超过接收端的计数带宽，需要下调线数。</p>

<p class="c-term-rel"><b>相关系列</b><a href="/msite/products/3d-hall/kth55">KTH55 系列</a>、<a href="/msite/products/encoder/ktm52">KTM52 系列</a>、<a href="/msite/products/encoder/ktm53">KTM53 系列</a>、<a href="/msite/products/encoder/ktm58">KTM58 系列</a>、<a href="/msite/products/encoder/ktm59">KTM59 系列</a>、<a href="/msite/products/encoder/kth78">KTH78 系列</a>、<a href="/msite/products/encoder/kth71">KTH71 系列</a></p>

<h3 id="uvw">UVW 换向输出</h3>

<p class="c-term-short">三路互差 120° 电角度的方波，供电机换向定扇区</p>

U、V、W 三路方波互差 120° 电角度，一个电周期内组合出六个扇区，驱动器据此判断转子所处的换向区间。输出的对极数按电机极对数设定，使其与电机的电周期对齐。

<p class="c-note">UVW 的角度分辨能力只有 60° 电角度量级，用途是起动换向与粗定位；精确位置仍取自 ABZ 或串行绝对值输出。</p>

<p class="c-term-rel"><b>相关系列</b><a href="/msite/products/encoder/ktm52">KTM52 系列</a>、<a href="/msite/products/encoder/ktm53">KTM53 系列</a>、<a href="/msite/products/encoder/ktm58">KTM58 系列</a>、<a href="/msite/products/encoder/ktm59">KTM59 系列</a>、<a href="/msite/products/encoder/kth78">KTH78 系列</a>、<a href="/msite/products/encoder/kth71">KTH71 系列</a></p>

<h3 id="spi-ssi">SPI / SSI 串行绝对值接口</h3>

<p class="c-term-short">主控按时钟读走绝对角度的两种同步串行方式</p>

SPI 是四线全双工（CLK、MOSI、MISO、CS），既能读角度，也能读写配置寄存器与诊断标志，适合需要在线改参数的场合。

SSI 是两线单向同步串行（CLK、DATA），从机只在时钟驱动下移出位置数据、不接受写入，接线少、时序简单，是工业伺服编码器常见的读出接口。

<p class="c-note">高速读取时要核对一帧里的位序与对齐方式，以及是否带 CRC 校验位；总线可用速率还受线缆长度与驱动能力限制。</p>

<p class="c-term-rel"><b>相关系列</b><a href="/msite/products/3d-hall/kth57">KTH57 系列</a>、<a href="/msite/products/3d-hall/kth55">KTH55 系列</a>、<a href="/msite/products/encoder/ktm52">KTM52 系列</a>、<a href="/msite/products/encoder/ktm53">KTM53 系列</a>、<a href="/msite/products/encoder/ktm58">KTM58 系列</a>、<a href="/msite/products/encoder/ktm59">KTM59 系列</a>、<a href="/msite/products/encoder/kth78">KTH78 系列</a>、<a href="/msite/products/encoder/kth71">KTH71 系列</a></p>

<h3 id="pwm">PWM 角度输出</h3>

<p class="c-term-short">用固定频率方波的占空比表示绝对角度</p>

一个 PWM 周期内高电平所占的比例与角度成正比，接收端测量高电平时间与周期之比即可还原角度。只需一根信号线，可直接接主控的捕获口，不需要时钟与片选，适合走线受限或需要隔离的场合。

<p class="c-note">角度更新率等于 PWM 频率，而分辨率受接收端定时器计数频率限制：频率调高更新更快，但每周期可数的计数值变少，分辨率反而下降，两者需要折中。</p>

<p class="c-term-rel"><b>相关系列</b><a href="/msite/products/3d-hall/kth55">KTH55 系列</a>、<a href="/msite/products/encoder/ktm52">KTM52 系列</a>、<a href="/msite/products/encoder/ktm53">KTM53 系列</a>、<a href="/msite/products/encoder/ktm58">KTM58 系列</a>、<a href="/msite/products/encoder/ktm59">KTM59 系列</a>、<a href="/msite/products/encoder/kth78">KTH78 系列</a>、<a href="/msite/products/encoder/kth71">KTH71 系列</a></p>

## 磁敏原理

<h3 id="hall-effect">霍尔效应 / Hall effect</h3>

<p class="c-term-short">载流薄片在垂直磁场下产生横向电压</p>

通有电流的半导体薄片受到垂直于片面的磁场时，洛伦兹力使载流子横向偏移，在两侧形成与磁通密度成正比的霍尔电压。

平面霍尔盘响应的是垂直于芯片表面的分量，可用标准 CMOS 工艺与放大、补偿电路集成在同一颗芯片内，成本低、线性好，是开关、线性传感器与角度编码器的通用基础。

<p class="c-note">霍尔按磁场幅值工作，输出受温度与气隙影响较大，因此规格里普遍带有温度补偿以及失调抵消（如斩波、自旋电流）相关指标。</p>

<p class="c-term-rel"><b>相关系列</b>KTH16 系列、<a href="/msite/products/switch/kth25">KTH25 系列</a>、<a href="/msite/products/switch/kth31">KTH31 系列</a>、<a href="/msite/products/switch/linear-hall">KTH564 系列</a>、<a href="/msite/products/switch/kth460">KTH460 系列</a>、<a href="/msite/products/switch/kth462">KTH462 系列</a>、<a href="/msite/products/3d-hall/kth57">KTH57 系列</a>、<a href="/msite/products/encoder/kth78">KTH78 系列</a>、<a href="/msite/products/encoder/kth71">KTH71 系列</a></p>

<h3 id="vertical-hall">垂直霍尔 / Vertical Hall</h3>

<p class="c-term-short">敏感方向落在芯片平面内的霍尔结构</p>

普通平面霍尔盘只感应垂直于芯片表面的 Z 分量。垂直霍尔改变结构，使敏感方向落在芯片平面内，于是同一颗芯片上可以同时取得 X、Y、Z 三个方向的磁场分量。

角度测量因此可以只用平面内的两个分量做反正切；离轴测量所需的切向与轴向分量，也能由同一颗芯片一次取得。

<p class="c-note">垂直霍尔结构的失调与通道匹配控制难度高于平面霍尔，实测精度取决于工艺匹配程度与失调抵消手段，不能只按结构类型判断优劣。</p>

<p class="c-term-rel"><b>相关系列</b><a href="/msite/products/3d-hall/kth55">KTH55 系列</a>、<a href="/msite/products/encoder/ktm53">KTM53 系列</a></p>

<h3 id="amr">AMR / 各向异性磁阻</h3>

<p class="c-term-short">电阻随磁化方向与电流夹角变化，工作在饱和区</p>

坡莫合金薄膜的电阻取决于其磁化方向与电流方向的夹角，按 cos²θ 规律变化。外场足够强（饱和区，约 300 高斯量级）时磁化方向完全跟随外场方向，输出只与磁场方向有关、与幅值无关，因此对磁体加工误差与安装距离误差的容忍度较高。

角度测量中常用两组互成 45° 的惠斯通电桥取出两路正交信号。

<p class="c-note">AMR 的角度依赖周期是 180°，单靠磁阻桥只能唯一确定半圈；要覆盖 0 ~ 360°，需要另一路信息来区分是哪半圈。</p>

<p class="c-term-rel"><b>相关系列</b><a href="/msite/products/encoder/ktm52">KTM52 系列</a>、<a href="/msite/products/encoder/ktm53">KTM53 系列</a>、<a href="/msite/products/encoder/ktm58">KTM58 系列</a>、<a href="/msite/products/switch/ktm28">KTM28 系列</a></p>

<h3 id="tmr">TMR / 隧道磁电阻</h3>

<p class="c-term-short">隧道结电阻随自由层与钉扎层的磁化夹角变化</p>

磁性隧道结由钉扎层、绝缘势垒与自由层构成，自由层磁化方向随外场转动，隧穿电阻随两层磁化夹角变化，变化率比 AMR、GMR 高一个数量级以上。

由此带来输出幅值大、桥阻可以做得很高因而功耗低的特点；角度依赖周期为 360°，单组桥即可区分整圈。

<p class="c-note">TMR 的阻值与温度系数需要补偿，强场下存在饱和与磁滞。用作开关时回差（BOP 与 BRP 之差）可以做得比霍尔更小。</p>

<p class="c-term-rel"><b>相关系列</b><a href="/msite/products/encoder/ktm59">KTM59 系列</a>、<a href="/msite/products/switch/ktm13">KTM13 系列</a>、<a href="/msite/products/encoder/ktm58">KTM58 系列</a></p>

## 开关型器件

<h3 id="unipolar-omnipolar">单极型 / 全极型</h3>

<p class="c-term-short">按触发磁极区分：单极只认一个极，全极两极都认</p>

单极型只在指定极性（单 N 极或单 S 极）的磁场超过阈值时动作，反向磁场不响应，适合磁极朝向固定、需要防止反向误触发的场合。

全极型对 N、S 任一极性达到阈值都动作，装配时不必区分磁体极性，常用于翻盖检测、到位检测这类只关心「有没有磁体靠近」的场合。

<p class="c-note">单极与全极都是「来磁动作、去磁复位」，与锁存型的状态保持行为完全不同。互换时不能只比对阈值数值，要先确认动作逻辑一致。</p>

<p class="c-term-rel"><b>相关系列</b>KTH16 系列、<a href="/msite/products/switch/ktm13">KTM13 系列</a>、<a href="/msite/products/switch/ktm28">KTM28 系列</a>、<a href="/msite/products/switch/kth460">KTH460 系列</a></p>

<h3 id="latching">锁存型 / Latch</h3>

<p class="c-term-short">一个极性置位、相反极性复位，撤磁后保持原状态</p>

锁存型（双极锁存）需要交替出现的两种极性：一个极性把输出置位，只有相反极性才能把它复位，其间磁场消失时输出保持不变。

转子上 N、S 交替排列的磁环经过锁存型器件时，会得到占空比稳定的方波，因此它是测转速、计数与电机换向的常用器件。

<p class="c-note">锁存型不能用来判断「有没有磁体」——磁体移走后输出不回位。现场只有单一极性可用时，应改选单极型或全极型。</p>

<p class="c-term-rel"><b>相关系列</b>KTH16 系列、<a href="/msite/products/switch/ktm13">KTM13 系列</a>、<a href="/msite/products/switch/kth25">KTH25 系列</a>、<a href="/msite/products/switch/kth462">KTH462 系列</a></p>

<h3 id="bop-brp">BOP / BRP 与回差</h3>

<p class="c-term-short">动作阈值与释放阈值，两者之差称为回差</p>

BOP（operate point）是输出翻转到动作状态所需的磁通密度，BRP（release point）是恢复所需的磁通密度，两者之差称为回差（磁滞）。回差的作用是抑制阈值附近磁场抖动造成的输出反复跳变。

规格表通常按型号给出多档 BOP / BRP，并分别标出 N、S 两个方向对应的数值。

<p class="c-note">单位常混用，换算关系是 1 mT = 10 Gs（高斯）。选型要按最坏情况核算：用 BOP 的最大值校核能否可靠动作，用 BRP 的最小值校核能否可靠复位，不要拿典型值算裕量。</p>

<p class="c-term-rel"><b>相关系列</b>KTH16 系列、<a href="/msite/products/switch/ktm13">KTM13 系列</a>、<a href="/msite/products/switch/kth25">KTH25 系列</a>、<a href="/msite/products/switch/ktm28">KTM28 系列</a>、<a href="/msite/products/switch/kth462">KTH462 系列</a>、<a href="/msite/products/switch/kth460">KTH460 系列</a></p>

<div class="c-cta"><div><h2 class="c-cta__title">还有拿不准的参数？</h2><p>选型、磁路与接口对接上的问题，欢迎直接找我们的技术团队确认。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/msite/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
