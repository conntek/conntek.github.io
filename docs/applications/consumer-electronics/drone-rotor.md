---
title: "无人机旋翼 · 消费类电子应用"
description: "检测无人机动力电机的转子角度，为电调的磁场定向控制提供位置反馈。"
aside: false
pageClass: "c-page c-page--case"
---

<nav class="c-crumbs"><a href="/msite/">首页</a><i>/</i><a href="/msite/applications/">市场应用</a><i>/</i><a href="/msite/applications/consumer-electronics">消费类电子</a><i>/</i><span>无人机旋翼</span></nav>

<p class="c-kicker">消费类电子</p>

# 无人机旋翼

<p class="c-lead">检测无人机动力电机的转子角度，为电调的磁场定向控制提供位置反馈。</p>

<div class="c-actions"><a class="c-btn c-btn--brand" href="/msite/products/encoder/kth78">推荐芯片 KTH78xx</a><a class="c-btn" href="/msite/contact">方案咨询</a></div>

## 场景说明

<div class="c-split c-split--overview"><div class="c-split__text">

多旋翼无人机的每支旋翼由一台无刷电机直接驱动，电调用磁场定向控制（FOC）调节转速和推力。电机轴端或转子端面装一块径向充磁磁铁，芯片贴在电机底座或电调板上正对磁铁，读出转子的绝对角度。无感方案靠反电动势估算转子位置，而起转和低速段的反电动势接近于零，带大尺寸桨叶、低 KV 电机的机型尤其容易在起转时抖动或失步，这是加装角度传感器的主要原因。

旋翼电机转速高，从悬停到满油门转速变化快。角度反馈只要晚一点，折算到电角度上的误差就随转速和极对数成比例放大，直接表现为换相超前或滞后、效率下降。传感器又紧挨着相线和功率管，大电流在芯片附近产生的杂散磁场会叠加到测量磁场上；机臂振动会改变磁铁与芯片之间的气隙，而整机对重量和体积同样敏感。

</div><div class="c-split__media c-split__media--frame c-split__media--case"><img src="/msite/img/case/consumer-electronics-drone-rotor.webp" alt="无人机旋翼" loading="lazy"></div></div>

## 检测需求

<p class="c-sec-lead">无人机旋翼对传感器的主要要求。</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>低速起转</h3><p>起转与低速段反电动势太弱，需要直接测得转子位置。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>高速低延时</h3><p>角度延时会按转速与极对数放大成换相误差。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>抗电流干扰</h3><p>芯片紧邻相线与功率管，大电流杂散场不能带偏读数。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>小而轻</h3><p>电机底座与电调板空间有限，整机对重量敏感。</p></div></div></div>

## 为什么选 KTH78xx

<p class="c-sec-lead">16 位分辨率，系统延时 1 μs 并做延时补偿，全系支持在轴与离轴应用</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>上电即知位置</h3><p>启动时间 1 ms，静止上电即可读出转子角度，无需先转动定位。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>高速低延时</h3><p>转速 120,000 rpm，系统延时 1 μs 且内部已做延时补偿。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>换相信号可编程</h3><p><a class="c-xref" href="/msite/products/encoder/kth78/kth7812-x-n-qn16">KTH7812</a> / <a class="c-xref" href="/msite/products/encoder/kth78/kth7813-x-n-qn16">KTH7813</a> 提供 UVW 输出，可编程 1 ~ 8 对极。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>离轴与多对极</h3><p>全系支持在轴与离轴应用及多对极磁铁，轴端空间紧时可偏置布置。</p></div></div></div>

<div class="c-grid c-grid--2"><a class="c-card" href="/msite/products/encoder/kth78"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth78.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH78 系列</span><h3>低延时霍尔绝对角度编码器</h3><p>16 位分辨率，系统延时 1 μs 并做延时补偿，全系支持在轴与离轴应用</p><span class="c-card__more">查看产品</span></div></a></div>

## 设计注意点

<p class="c-sec-lead">通用工程建议，实际设计以产品手册与实测为准。</p>

<ul class="c-checklist"><li>先按最高转速、电机极对数和从采样到控制输出的总延时估算电角度滞后（约为电角速度乘以总延时），再决定读 SPI 绝对角度还是用 UVW / ABZ 直接换相。</li><li>芯片尽量远离相线与功率回路，三相走线并行靠拢以互相抵消磁场，布局定稿后在满油门电流下复测角度抖动。</li><li>按机臂振动和装配公差带来的最大、最小气隙分别核算芯片处磁场，两端都应落在 30 ~ 150 mT 工作磁场范围内。</li><li>SOP-8 封装版本只有 PWM / SPI 输出，需要 ABZ 或 UVW 增量信号的方案应选 QFN16 封装的对应型号。</li></ul>

## 相关案例

<div class="c-grid c-grid--4"><a class="c-card" href="/msite/applications/industry4/bldc-motor"><div class="c-card__media c-media--case"><img src="/msite/img/case/industry4-bldc-motor.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH78xx</span><h3>无刷直流电机</h3><p>读取无刷电机转子的绝对角度，用于换相与磁场定向控制，覆盖电动工具等大电流工况。</p><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/msite/applications/industry4/coreless-motor"><div class="c-card__media c-media--case"><img src="/msite/img/case/industry4-coreless-motor.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH78xx</span><h3>空心杯电机</h3><p>在空心杯电机尾端读取转子绝对角度，为小体积、高转速的精密运动控制提供位置反馈。</p><span class="c-card__more">查看案例</span></div></a></div>

<div class="c-cta"><div><h2 class="c-cta__title">需要选型建议、样品或技术支持？</h2><p>昆泰芯提供芯片选型、磁场仿真与方案设计支持，欢迎与我们的销售和技术团队联系。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/msite/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
