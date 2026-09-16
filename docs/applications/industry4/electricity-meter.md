---
title: "电表 · 工业4.0应用"
description: "监测表内异常外部磁场，识别用强磁干扰计量的行为。"
aside: false
pageClass: "c-page c-page--case"
---

<nav class="c-crumbs"><a href="/msite/">首页</a><i>/</i><a href="/msite/applications/">市场应用</a><i>/</i><a href="/msite/applications/industry4">工业4.0</a><i>/</i><span>电表</span></nav>

<p class="c-kicker">工业4.0</p>

# 电表

<p class="c-lead">监测表内异常外部磁场，识别用强磁干扰计量的行为。</p>

<div class="c-actions"><a class="c-btn c-btn--brand" href="/msite/products/3d-hall/kth57">推荐芯片 KTH57xx</a><a class="c-btn" href="/msite/contact">方案咨询</a></div>

## 场景说明

<div class="c-split c-split--overview"><div class="c-split__text">

电子式电能表的电流互感器在强磁场下会饱和，计量随之偏低，用强磁体贴着表壳干扰计量是已知的窃电手法。表内放一颗三轴磁场传感器，可以持续监测背景磁场是否出现异常。

与单阈值磁开关相比，三轴测量能同时给出磁场的大小和方向，便于区分是环境中缓慢变化的背景场，还是某个方向上突然出现的强磁体，从而减少误报。

</div><div class="c-split__media c-split__media--frame c-split__media--case"><img src="/msite/img/case/industry4-0.webp" alt="电表" loading="lazy"></div></div>

## 检测需求

<p class="c-sec-lead">电表对传感器的主要要求。</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>要测幅值方向</h3><p>只有有无信号不够，需要知道强度与方向才能判事件。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>长期在线</h3><p>电表安装后长年不停机，监测必须一直有效。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>宽温稳定</h3><p>户外表箱全年温差大，判定门限不能跟着温度走。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>数字上报</h3><p>事件需记录并上报，模拟量不便直接入账。</p></div></div></div>

## 为什么选 KTH57xx

<p class="c-sec-lead">测量 X、Y、Z 三轴磁场，I2C / SPI 可选，工作模式在线配置，兼顾性能与功耗</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>三轴矢量测量</h3><p>三轴分量一起读，能给出磁场的大小和方向。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>宽磁场范围</h3><p>XY 轴 ±130 mT、Z 轴 ±80 mT，贴表强磁也不饱和。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>温度补偿</h3><p>集成温度传感器与内部补偿，季节温差下零点更稳。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>数字接口</h3><p>I2C / SPI 读数，事件可直接进计量主控记录。</p></div></div></div>

<div class="c-grid c-grid--2"><a class="c-card" href="/msite/products/3d-hall/kth57"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth57.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57 系列</span><h3>三轴线性霍尔传感器</h3><p>测量 X、Y、Z 三轴磁场，I2C / SPI 可选，工作模式在线配置，兼顾性能与功耗</p><span class="c-card__more">查看产品</span></div></a></div>

## 设计注意点

<p class="c-sec-lead">通用工程建议，实际设计以产品手册与实测为准。</p>

<ul class="c-checklist"><li>判据应建立在磁场的变化量上而不是绝对值上，表计安装位置的背景场差异很大。</li><li>表箱内相邻表计的磁场会互相影响，密集安装时按最坏排布评估一次。</li><li>传感器位置要避开表内互感器、继电器线圈等自身磁源，或把它们的影响做成已知量扣除。</li><li>采样率决定了能否捕捉短时磁场事件，需要与记录逻辑的时间分辨率匹配。</li></ul>

## 相关案例

<div class="c-grid c-grid--4"><a class="c-card" href="/msite/applications/industry4/mechanical-meter"><div class="c-card__media c-media--case"><img src="/msite/img/case/industry4-5.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM13xx</span><h3>机械电表</h3><p>对机械字轮上的磁铁计数，把机械读数转成电子脉冲。</p><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/msite/applications/industry4/circuit-breaker"><div class="c-card__media c-media--case"><img src="/msite/img/case/industry4-1.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH16xx</span><h3>断路器</h3><p>检测手柄或触头机构的分合闸位置，输出状态信号。</p><span class="c-card__more">查看案例</span></div></a></div>

<div class="c-cta"><div><h2 class="c-cta__title">需要选型建议、样品或技术支持？</h2><p>昆泰芯提供芯片选型、磁场仿真与方案设计支持，欢迎与我们的销售和技术团队联系。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/msite/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
