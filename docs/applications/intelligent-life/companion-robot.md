---
title: "陪伴机器人 · 智能生活应用"
description: "检测头部、关节的转动角度与操作旋钮的位置。"
aside: false
pageClass: "c-page c-page--case"
---

<nav class="c-crumbs"><a href="/msite/">首页</a><i>/</i><a href="/msite/applications/">市场应用</a><i>/</i><a href="/msite/applications/intelligent-life">智能生活</a><i>/</i><span>陪伴机器人</span></nav>

<p class="c-kicker">智能生活</p>

# 陪伴机器人

<p class="c-lead">检测头部、关节的转动角度与操作旋钮的位置。</p>

<div class="c-actions"><a class="c-btn c-btn--brand" href="/msite/products/3d-hall/kth57">推荐芯片 KTH57xx</a><a class="c-btn" href="/msite/contact">方案咨询</a></div>

## 场景说明

<div class="c-split c-split--overview"><div class="c-split__text">

陪伴机器人的头部、颈部和手臂需要知道自己当前转到哪个角度，才能做闭环的动作控制与限位保护。在转轴上放一颗磁铁、对面放芯片，就能在不增加机械结构的前提下读出转角。

这类产品外壳圆润、内部空间被电池和音响占满，留给位置检测的体积很小；同时它常年开机待命，任何一个常驻传感器的功耗都会体现在续航上。

</div><div class="c-split__media c-split__media--frame c-split__media--case"><img src="/msite/img/case/intelligent-life-1.webp" alt="陪伴机器人" loading="lazy"></div></div>

## 检测需求

<p class="c-sec-lead">陪伴机器人对传感器的主要要求。</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>转角要连续</h3><p>闭环动作控制需要连续角度，而不是到位开关。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>体积受限</h3><p>关节内部空间小，传感器与磁铁都要做小。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>常驻低功耗</h3><p>整机常年待机，位置检测不能成为功耗大头。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>抗扬声器磁场</h3><p>机身内的扬声器磁体会形成稳定的背景磁场。</p></div></div></div>

## 为什么选 KTH57xx

<p class="c-sec-lead">测量 X、Y、Z 三轴磁场，I2C / SPI 可选，工作模式在线配置，兼顾性能与功耗</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>在轴离轴均可</h3><p>磁铁在轴、离轴都能用，关节结构不用迁就芯片。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>小尺寸封装</h3><p>DFN2*2.5-8L 封装，塞得进关节转轴旁的空隙。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>工作模式可配</h3><p>单次测量与持续感应按动静切换，静止时少采样。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>数字输出</h3><p>I2C / SPI 从机，多个关节可挂在同一条总线上。</p></div></div></div>

<div class="c-grid c-grid--2"><a class="c-card" href="/msite/products/3d-hall/kth57"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth57.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57 系列</span><h3>三轴线性霍尔传感器</h3><p>测量 X、Y、Z 三轴磁场，I2C / SPI 可选，工作模式在线配置，兼顾性能与功耗</p><span class="c-card__more">查看产品</span></div></a></div>

## 设计注意点

<p class="c-sec-lead">通用工程建议，实际设计以产品手册与实测为准。</p>

<ul class="c-checklist"><li>离轴摆放时磁场分量随位置变化更快，装配公差对角度误差的放大更明显，应优先保证同心度。</li><li>关节走线会随转动改变位置，信号线应固定走向，避免动态引入干扰。</li><li>关节靠角度判限位时，判定点要与机械硬限位错开，避免顶死堵转。</li><li>多关节共用一条 I2C 总线时要规划好地址与采样节奏，避免采样周期互相拖慢。</li></ul>

## 相关案例

<div class="c-grid c-grid--4"><a class="c-card" href="/msite/applications/intelligent-life/robot-vacuum"><div class="c-card__media c-media--case"><img src="/msite/img/case/intelligent-life-3.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57xx</span><h3>扫地机器人-真空吸尘器</h3><p>检测拖布、滚刷等可换模块的安装位置与抬升行程。</p><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/msite/applications/intelligent-life/smart-toilet-pivot"><div class="c-card__media c-media--case"><img src="/msite/img/case/intelligent-life-6.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57xx</span><h3>智能马桶-枢轴检测</h3><p>检测盖板与坐圈在枢轴处的开合角度，用于落座与翻盖判断。</p><span class="c-card__more">查看案例</span></div></a></div>

<div class="c-cta"><div><h2 class="c-cta__title">需要选型建议、样品或技术支持？</h2><p>昆泰芯提供芯片选型、磁场仿真与方案设计支持，欢迎与我们的销售和技术团队联系。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/msite/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
