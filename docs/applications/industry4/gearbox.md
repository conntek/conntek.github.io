---
title: "齿轮箱 · 工业4.0应用"
description: "测量减速齿轮箱输入轴或输出轴的转角，用于位置闭环与传动状态监测。"
aside: false
pageClass: "c-page c-page--case"
---

<nav class="c-crumbs"><a href="/msite/">首页</a><i>/</i><a href="/msite/applications/">市场应用</a><i>/</i><a href="/msite/applications/industry4">工业4.0</a><i>/</i><span>齿轮箱</span></nav>

<p class="c-kicker">工业4.0</p>

# 齿轮箱

<p class="c-lead">测量减速齿轮箱输入轴或输出轴的转角，用于位置闭环与传动状态监测。</p>

<div class="c-actions"><a class="c-btn c-btn--brand" href="/msite/products/encoder/kth71">推荐芯片 KTH71xx</a><a class="c-btn" href="/msite/contact">方案咨询</a></div>

## 场景说明

<div class="c-split c-split--overview"><div class="c-split__text">

减速齿轮箱把电机的高速小扭矩变成输出轴的低速大扭矩，常见于执行器、云台和自动化设备的关节。磁编码器可以装在电机侧的输入轴端，负责电机换相与速度控制；也可以装在输出轴端，直接测负载实际转到的角度。两处各看得见不同的东西：齿隙、负载下的扭转变形和温升引起的尺寸变化都发生在齿轮箱内部，电机侧的编码器看不到它们。

只在电机侧测量时，正反转切换那一刻齿先空走一段，输出轴不动而读数已经变化，编码器位数再高也补不回这段误差。输出侧测量能把这些误差纳入闭环，但一圈转得慢、要求单圈精度高，且传感器往往紧挨电机绕组和抱闸线圈，要面对它们通电时的杂散磁场。两侧都装时，两路角度之差可以直接反映齿隙与传动变形的大小。齿轮箱内还有润滑脂和运转温升，非接触的磁测量更适合这种环境。

</div><div class="c-split__media c-split__media--frame c-split__media--case"><img src="/msite/img/case/industry4-gearbox.webp" alt="齿轮箱" loading="lazy"></div></div>

## 检测需求

<p class="c-sec-lead">齿轮箱对传感器的主要要求。</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>单圈精度高</h3><p>输出侧测量时，角度误差直接等于末端定位误差。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>耐高转速</h3><p>输入侧跟随电机转速，高速下角度不能滞后。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>抗杂散磁场</h3><p>输出端常紧邻电机绕组与抱闸，通电时有杂散场。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>宽温工作</h3><p>齿轮箱长时间运行发热，要看全温区表现。</p></div></div></div>

## 为什么选 KTH71xx

<p class="c-sec-lead">内置自动非线性校准（ANLC），无需复杂外部干预，在轴 INL 优于 ±0.1°</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>校准后高精度</h3><p>内置 ANLC 自校准，<a class="c-xref" href="/msite/products/encoder/kth71/kth7112-qn16">KTH7112</a> 在轴精度 ±0.07°。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>高转速</h3><p>支持最高 120,000 rpm，输入侧高速轴也能跟随。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>低延时</h3><p>角度刷新频率 1 MHz，内部做延时补偿，匀速下系统延时接近零。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>宽温范围</h3><p>工作温度 -40 ~ 125 ℃，适应齿轮箱运行温升。</p></div></div></div>

<div class="c-grid c-grid--2"><a class="c-card" href="/msite/products/encoder/kth71"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth71.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH71 系列</span><h3>自校准霍尔磁编码器</h3><p>内置自动非线性校准（ANLC），无需复杂外部干预，在轴 INL 优于 ±0.1°</p><span class="c-card__more">查看产品</span></div></a></div>

## 设计注意点

<p class="c-sec-lead">通用工程建议，实际设计以产品手册与实测为准。</p>

<ul class="c-checklist"><li>先定系统精度预算，把齿隙、扭转变形、温漂和安装误差逐项扣掉，再决定编码器装在哪一侧、需要多高的精度。</li><li>需要补偿齿隙和传动弹性时把传感器放在输出轴端，或在输入、输出两端各装一颗并利用两路读数之差。</li><li>输出端传感器靠近电机绕组或抱闸时，在满载电流和抱闸动作两种状态下分别复测角度误差。</li><li>芯片与磁铁之间用非导磁盖板隔开润滑腔，磁铁座避免用导磁钢材，并在高温工况下复核磁场仍在 30 ~ 150 mT 之内。</li></ul>

## 相关案例

<div class="c-grid c-grid--4"><a class="c-card" href="/msite/applications/industry4/robot-joint"><div class="c-card__media c-media--case"><img src="/msite/img/case/industry4-robot-joint.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM59xx</span><h3>机器人关节</h3><p>测量关节电机端与减速器输出端的角度，支撑机械臂关节的精确定位。</p><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/msite/applications/industry4/servo-motor"><div class="c-card__media c-media--case"><img src="/msite/img/case/industry4-servo-motor.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM58xx</span><h3>伺服电机</h3><p>测量伺服电机转子的绝对角度，供电流环换相与位置环闭环使用。</p><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/msite/applications/industry4/agv"><div class="c-card__media c-media--case"><img src="/msite/img/case/industry4-agv.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH78xx</span><h3>AGV 搬运机器人</h3><p>测量舵轮转向角与驱动电机转子角度，实现上电即知轮向和电机换相。</p><span class="c-card__more">查看案例</span></div></a></div>

<div class="c-cta"><div><h2 class="c-cta__title">需要选型建议、样品或技术支持？</h2><p>昆泰芯提供芯片选型、磁场仿真与方案设计支持，欢迎与我们的销售和技术团队联系。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/msite/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
