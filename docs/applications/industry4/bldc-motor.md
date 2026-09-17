---
title: "无刷直流电机 · 工业4.0应用"
description: "读取无刷电机转子的绝对角度，用于换相与磁场定向控制，覆盖电动工具等大电流工况。"
aside: false
pageClass: "c-page c-page--case"
---

<nav class="c-crumbs"><a href="/msite/">首页</a><i>/</i><a href="/msite/applications/">市场应用</a><i>/</i><a href="/msite/applications/industry4">工业4.0</a><i>/</i><span>无刷直流电机</span></nav>

<p class="c-kicker">工业4.0</p>

# 无刷直流电机

<p class="c-lead">读取无刷电机转子的绝对角度，用于换相与磁场定向控制，覆盖电动工具等大电流工况。</p>

<div class="c-actions"><a class="c-btn c-btn--brand" href="/msite/products/encoder/kth78">推荐芯片 KTH78xx</a><a class="c-btn" href="/msite/products/encoder/kth71">也可选 KTH71xx</a><a class="c-btn" href="/msite/contact">方案咨询</a></div>

## 场景说明

<div class="c-split c-split--overview"><div class="c-split__text">

无刷直流电机没有电刷，控制器必须知道转子磁极转到了哪里，才能给三相绕组换相。传统做法是在定子里放三颗霍尔开关，只在每 60° 电角度给出一次跳变；做磁场定向控制（FOC）时则需要连续的转子角度。常见结构是在转轴尾端粘一块径向充磁的小磁铁，角度编码器芯片贴在后端盖的控制板上正对磁铁；轴端被占用时也可以偏离轴心安装。

电动工具是其中工况最苛刻的一类。电池直接供电，相电流大，相线、功率管和母线电容往往紧挨着传感器布置，电流产生的杂散磁场会叠加在磁铁的磁场上；空载转速高，启停、反转和堵转频繁，角度必须跟得上转子；整机还要承受冲击、跌落和持续振动，磁铁与芯片的相对位置会发生微小偏移。控制板空间紧凑、散热有限，传感器要在较高温度下长期工作。

</div><div class="c-split__media c-split__media--frame c-split__media--case"><img src="/msite/img/case/industry4-bldc-motor.webp" alt="无刷直流电机" loading="lazy"></div></div>

## 检测需求

<p class="c-sec-lead">无刷直流电机对传感器的主要要求。</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>连续绝对角度</h3><p>上电即知转子位置，FOC 需要连续角度而非 60° 跳变。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>跟得上高转速</h3><p>延时乘转速再乘极对数就是换相电角滞后，转速越高越大。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>抗杂散磁场</h3><p>大电流相线与功率器件就在传感器旁边。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>耐振耐温</h3><p>冲击、跌落、振动与功率器件发热同时存在。</p></div></div></div>

## 为什么选 KTH78xx

<p class="c-sec-lead">16 位分辨率，系统延时 1 μs 并做延时补偿，全系支持在轴与离轴应用</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>高转速低延时</h3><p>规格转速 120,000 rpm，角度每 1 μs 更新一次，内部做延时补偿。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>UVW 换相输出</h3><p>UVW 增量输出 1 ~ 8 对极可编程，可对接按霍尔信号换相的控制器。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>磁场诊断报警</h3><p>工作磁场 30 ~ 150 mT，磁场过低、过高报警阈值可由用户设置。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>可选自校准</h3><p>对精度要求更高时可选 <a class="c-xref" href="/msite/products/encoder/kth71">KTH71</a> 系列，内置自动非线性校准，在轴 INL 优于 ±0.1°。</p></div></div></div>

<div class="c-grid c-grid--2"><a class="c-card" href="/msite/products/encoder/kth78"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth78.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH78 系列</span><h3>低延时霍尔绝对角度编码器</h3><p>16 位分辨率，系统延时 1 μs 并做延时补偿，全系支持在轴与离轴应用</p><span class="c-card__more">查看产品</span></div></a></div>

## 设计注意点

<p class="c-sec-lead">通用工程建议，实际设计以产品手册与实测为准。</p>

<ul class="c-checklist"><li>相线、母线电容和功率管的大电流回路远离芯片，去线与回线平行靠近；杂散磁场在堵转和满载时最强，要在这两个工况下复测角度读数。</li><li>按最高转速和电机极对数折算一次延时对应的电角滞后，高速段的验收要在目标转速下做，不能只在低速台架上看精度。</li><li>角度读取时刻与相电流采样对齐到 PWM 周期的同一位置，两者错开会表现为额外的换相滞后，靠调整软件时序即可消除。</li><li>UVW 对极数设成与电机极对数一致；UVW 输出选 <a class="c-xref" href="/msite/products/encoder/kth78/kth7812-x-n-qn16">KTH7812</a> / <a class="c-xref" href="/msite/products/encoder/kth78/kth7813-x-n-qn16">KTH7813</a> 等 QFN16 封装型号，SOP-8 封装型号只有 PWM / SPI 输出。</li></ul>

## 相关案例

<div class="c-grid c-grid--4"><a class="c-card" href="/msite/applications/industry4/servo-motor"><div class="c-card__media c-media--case"><img src="/msite/img/case/industry4-servo-motor.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM58xx</span><h3>伺服电机</h3><p>测量伺服电机转子的绝对角度，供电流环换相与位置环闭环使用。</p><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/msite/applications/industry4/closed-loop-stepper"><div class="c-card__media c-media--case"><img src="/msite/img/case/industry4-closed-loop-stepper.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH78xx</span><h3>步进闭环</h3><p>在步进电机尾端读取转子绝对角度，实时发现失步并闭环修正，兼顾定位与发热。</p><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/msite/applications/consumer-electronics/drone-rotor"><div class="c-card__media c-media--case"><img src="/msite/img/case/consumer-electronics-drone-rotor.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH78xx</span><h3>无人机旋翼</h3><p>检测无人机动力电机的转子角度，为电调的磁场定向控制提供位置反馈。</p><span class="c-card__more">查看案例</span></div></a></div>

<div class="c-cta"><div><h2 class="c-cta__title">需要选型建议、样品或技术支持？</h2><p>昆泰芯提供芯片选型、磁场仿真与方案设计支持，欢迎与我们的销售和技术团队联系。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/msite/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
