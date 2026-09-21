---
title: "直线电机 · 工业4.0应用"
description: "细分直线电机磁栅或光栅读头的正余弦信号，得到动子的高分辨率位置。"
aside: false
pageClass: "c-page c-page--case"
ld: "{\"@context\": \"https://schema.org\", \"@type\": \"TechArticle\", \"headline\": \"直线电机：工业4.0应用方案\", \"description\": \"细分直线电机磁栅或光栅读头的正余弦信号，得到动子的高分辨率位置。\", \"about\": \"直线电机\", \"author\": {\"@type\": \"Organization\", \"name\": \"昆泰芯微电子\", \"alternateName\": \"CONNTEK\", \"url\": \"https://conntek.grosso.link/\"}, \"publisher\": {\"@type\": \"Organization\", \"name\": \"昆泰芯微电子\", \"alternateName\": \"CONNTEK\", \"url\": \"https://conntek.grosso.link/\"}, \"url\": \"https://conntek.grosso.link/applications/industry4/linear-motor\"}"
---

<nav class="c-crumbs"><a href="/">首页</a><i>/</i><a href="/applications/">市场应用</a><i>/</i><a href="/applications/industry4">工业4.0</a><i>/</i><span>直线电机</span></nav>

<p class="c-kicker">工业4.0</p>

# 直线电机

<p class="c-lead">细分直线电机磁栅或光栅读头的正余弦信号，得到动子的高分辨率位置。</p>

<div class="c-actions"><a class="c-btn c-btn--brand" href="/products/encoder/ktm58">推荐芯片 KTM58xx</a><a class="c-btn" href="/contact">方案咨询</a></div>

## 场景说明

<div class="c-split c-split--overview"><div class="c-split__text">

直线电机没有旋转轴，动子沿导轨直接做直线运动，位置反馈来自沿行程铺设的磁栅尺或光栅尺。读头随动子移动，输出与栅距对应的正弦、余弦信号，每移动一个信号周期就重复一次。这里用不上把磁铁装在轴端的旋转编码器，需要的是能直接接收正余弦模拟信号的细分器，它把一个周期再切成成千上万份，驱动器据此完成换相和位置闭环。

磁栅信号的幅值随读头气隙按指数规律衰减，衰减快慢由磁化周期决定；导轨平行度不好时，气隙沿行程变化，幅值就跟着起伏，气隙压得太小，高次谐波占比又会上升。动子线圈就在读头附近，电机电流产生的磁场和驱动器的开关干扰都会叠加在模拟信号上。细分倍数再高也只是提高分辨率，栅尺刻划误差与安装误差仍会原样带进位置里。

</div><div class="c-split__media c-split__media--frame c-split__media--case"><img src="/img/case/industry4-linear-motor.webp" alt="直线电机" loading="lazy"></div></div>

## 检测需求

<p class="c-sec-lead">直线电机对传感器的主要要求。</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>接正余弦输入</h3><p>栅尺读头输出模拟正余弦，需要细分器直接接收。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>输入容差大</h3><p>气隙沿行程变化，信号幅值随之起伏。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>高速不丢位</h3><p>动子高速运动时，细分输出不能丢脉冲。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>增量接口</h3><p>驱动器多按 ABZ 脉冲计数取位置。</p></div></div></div>

## 为什么选 KTM58xx

<p class="c-sec-lead">最大 4096 对极输入，30 bit 绝对角度细分，适配磁电阻与光编、光栅、磁栅</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>多信号源适配</h3><p>可对光栅、磁栅等传感器的正余弦信号做细分。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>宽输入范围</h3><p>模拟电平输入 20 mV ~ 2 V，集成可编程增益运放。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>高位细分</h3><p>单对极细分最高 18 bit，双 16 bit 2M SAR ADC 采样。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>ABZ 可编程</h3><p>±ABZ 1 ~ 65536 线可编程，另有 36M SPI 读数。</p></div></div></div>

<div class="c-grid c-grid--2"><a class="c-card" href="/products/encoder/ktm58"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm58.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM58 系列</span><h3>30 bit 绝对角度细分器</h3><p>最大 4096 对极输入，30 bit 绝对角度细分，适配磁电阻与光编、光栅、磁栅</p><span class="c-card__more">查看产品</span></div></a></div>

## 设计注意点

<p class="c-sec-lead">通用工程建议，实际设计以产品手册与实测为准。</p>

<ul class="c-checklist"><li>按磁化周期估算全行程气隙变化带来的幅值变化，倍数过大时优先收紧导轨与读头安装公差，而不是靠增益硬撑。</li><li>沿全行程测一遍正余弦幅值，按最小幅值设定增益，峰值不超过推荐的 1 V 输入。</li><li>先由信号周期和目标线分辨率算出所需细分倍数，再按最高速度核对 ABZ 输出频率是否在驱动器接收范围内。</li><li>读头到细分器的模拟线用双绞屏蔽线，与电机动力线分开布线，屏蔽层与地的连接方式在整机状态下确认。</li></ul>

## 相关案例

<div class="c-grid c-grid--4"><a class="c-card" href="/applications/industry4/servo-motor"><div class="c-card__media c-media--case"><img src="/img/case/industry4-servo-motor.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM58xx</span><h3>伺服电机</h3><p>测量伺服电机转子的绝对角度，供电流环换相与位置环闭环使用。</p><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/applications/industry4/robot-joint"><div class="c-card__media c-media--case"><img src="/img/case/industry4-robot-joint.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM59xx</span><h3>机器人关节</h3><p>测量关节电机端与减速器输出端的角度，支撑机械臂关节的精确定位。</p><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/applications/industry4/cylinder-position"><div class="c-card__media c-media--case"><img src="/img/case/industry4-cylinder-position.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM280X</span><h3>气缸位置检测</h3><p>卡在气缸外壁安装槽里，感应活塞磁环，输出活塞是否到位的开关信号。</p><span class="c-card__more">查看案例</span></div></a></div>

<div class="c-cta"><div><h2 class="c-cta__title">需要选型建议、样品或技术支持？</h2><p>昆泰芯提供芯片选型、磁场仿真与方案设计支持，欢迎与我们的销售和技术团队联系。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
