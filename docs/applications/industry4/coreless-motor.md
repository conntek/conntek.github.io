---
title: "空心杯电机 · 工业4.0应用"
description: "在空心杯电机尾端读取转子绝对角度，为小体积、高转速的精密运动控制提供位置反馈。"
aside: false
pageClass: "c-page c-page--case"
---

<nav class="c-crumbs"><a href="/msite/">首页</a><i>/</i><a href="/msite/applications/">市场应用</a><i>/</i><a href="/msite/applications/industry4">工业4.0</a><i>/</i><span>空心杯电机</span></nav>

<p class="c-kicker">工业4.0</p>

# 空心杯电机

<p class="c-lead">在空心杯电机尾端读取转子绝对角度，为小体积、高转速的精密运动控制提供位置反馈。</p>

<div class="c-actions"><a class="c-btn c-btn--brand" href="/msite/products/encoder/kth78">推荐芯片 KTH78xx</a><a class="c-btn" href="/msite/contact">方案咨询</a></div>

## 场景说明

<div class="c-split c-split--overview"><div class="c-split__text">

空心杯电机的绕组做成无铁心的杯状，转动惯量小、响应快、没有齿槽转矩，常用于手持云台、精密仪器、医疗器械和机器人手指等需要小体积精密运动的场合。电机外径小，编码器一般做在电机尾部并与电机装成一体：转轴尾端粘一颗小直径磁铁，传感器芯片焊在尾部的小圆形电路板上，测量转子的绝对角度，供换相、速度环和位置环使用。

难点首先是空间。尾部电路板的直径往往与电机外径相当，磁铁只能做得很小，芯片处的磁场强度和安装公差都更紧，编码器也不能明显增加电机长度。其次是速度两头都要顾：空载转速高、常配减速箱，高速段看角度延时；云台、仪器这类应用又要求低速平稳，角度的周期误差会经速度环变成转矩波动。编码器信号还要和电机引线共用细线缆，线数越少越好。

</div><div class="c-split__media c-split__media--frame c-split__media--case"><img src="/msite/img/case/industry4-coreless-motor.webp" alt="空心杯电机" loading="lazy"></div></div>

## 检测需求

<p class="c-sec-lead">空心杯电机对传感器的主要要求。</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>占板面积小</h3><p>尾部电路板直径与电机外径相近，元件摆放很紧。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>高低速都要稳</h3><p>高速看角度延时，低速看周期误差，二者都会变成转矩波动。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>小磁铁可用</h3><p>磁铁直径小，磁场强度与气隙公差都很紧。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>引线要少</h3><p>编码器与电机共用细线缆，信号线越少越好。</p></div></div></div>

## 为什么选 KTH78xx

<p class="c-sec-lead">16 位分辨率，系统延时 1 μs 并做延时补偿，全系支持在轴与离轴应用</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>高转速低延时</h3><p>规格转速 120,000 rpm，角度刷新频率 1 MHz，内部做延时补偿。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>宽工作磁场</h3><p>工作磁场 30 ~ 150 mT，为小磁铁和气隙公差留出选择空间。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>宽压供电</h3><p>3.0 ~ 5.5 V 供电，可与电机驱动共用 3.3 V 或 5 V 电源。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>接口可选</h3><p>QFN16 型号可选 ABZ / UVW 增量输出，SOP-8 型号为 PWM / SPI 输出。</p></div></div></div>

<div class="c-grid c-grid--2"><a class="c-card" href="/msite/products/encoder/kth78"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth78.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH78 系列</span><h3>低延时霍尔绝对角度编码器</h3><p>16 位分辨率，系统延时 1 μs 并做延时补偿，全系支持在轴与离轴应用</p><span class="c-card__more">查看产品</span></div></a></div>

## 设计注意点

<p class="c-sec-lead">通用工程建议，实际设计以产品手册与实测为准。</p>

<ul class="c-checklist"><li>磁铁尺寸受限时先做磁场仿真，确认最大气隙下芯片处磁场仍不低于 30 mT，再定磁铁直径与厚度。</li><li>小电机优先在轴安装：离轴时芯片处于磁场边缘的不均匀区，对装配偏移和窜动明显更敏感。</li><li>尾部电路板与磁铁的间隙受电机轴向窜动影响，要按窜动的两个极限位置分别核对磁场强度和角度误差。</li><li>低速平稳性要求高时，在整机上测一条全圈「角度误差-机械角」曲线，重点看每圈一次的偏心分量，它最容易落进速度环带宽。</li></ul>

## 相关案例

<div class="c-grid c-grid--4"><a class="c-card" href="/msite/applications/industry4/robot-joint"><div class="c-card__media c-media--case"><img src="/msite/img/case/industry4-robot-joint.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM59xx</span><h3>机器人关节</h3><p>测量关节电机端与减速器输出端的角度，支撑机械臂关节的精确定位。</p><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/msite/applications/industry4/gripper"><div class="c-card__media c-media--case"><img src="/msite/img/case/industry4-gripper.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH71xx</span><h3>夹爪</h3><p>测量电动夹爪驱动电机或手指关节的转角，用于开合位置反馈与夹持动作控制。</p><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/msite/applications/industry4/bldc-motor"><div class="c-card__media c-media--case"><img src="/msite/img/case/industry4-bldc-motor.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH78xx</span><h3>无刷直流电机</h3><p>读取无刷电机转子的绝对角度，用于换相与磁场定向控制，覆盖电动工具等大电流工况。</p><span class="c-card__more">查看案例</span></div></a></div>

<div class="c-cta"><div><h2 class="c-cta__title">需要选型建议、样品或技术支持？</h2><p>昆泰芯提供芯片选型、磁场仿真与方案设计支持，欢迎与我们的销售和技术团队联系。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/msite/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
