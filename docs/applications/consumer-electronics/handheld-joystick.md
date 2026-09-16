---
title: "掌机摇杆 · 消费类电子应用"
description: "在很薄的机身里测出摇杆两轴摆角，避免电位器漂移。"
aside: false
pageClass: "c-page c-page--case"
---

<nav class="c-crumbs"><a href="/msite/">首页</a><i>/</i><a href="/msite/applications/">市场应用</a><i>/</i><a href="/msite/applications/consumer-electronics">消费类电子</a><i>/</i><span>掌机摇杆</span></nav>

<p class="c-kicker">消费类电子</p>

# 掌机摇杆

<p class="c-lead">在很薄的机身里测出摇杆两轴摆角，避免电位器漂移。</p>

<div class="c-actions"><a class="c-btn c-btn--brand" href="/msite/products/3d-hall/kth57">推荐芯片 KTH57xx</a><a class="c-btn" href="/msite/contact">方案咨询</a></div>

## 场景说明

<div class="c-split c-split--overview"><div class="c-split__text">

掌机摇杆的机身厚度只有十几毫米，摇杆模组必须做得又矮又小。摇杆底部的磁铁随拨动摆动，传感器读出磁场矢量方向，主控换算成两轴坐标。

掌机是电池设备且长时间连续游戏，摇杆采样既要够快，又不能成为功耗大头。磁式方案没有滑动触点，也就没有电位器常见的用久后零点漂移与摇杆自走问题。

</div><div class="c-split__media c-split__media--frame c-split__media--case"><img src="/msite/img/case/consumer-electronics-5.webp" alt="掌机摇杆" loading="lazy"></div></div>

## 检测需求

<p class="c-sec-lead">掌机摇杆对传感器的主要要求。</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>模组要薄</h3><p>机身厚度有限，传感器占高与占板面积都很紧张。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>两轴同时读</h3><p>需要一次拿到两个方向的分量，减少主控开销。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>功耗可控</h3><p>电池供电且长时间连续采样。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>零点稳定</h3><p>回中后读数必须回到同一点，否则会出现自走。</p></div></div></div>

## 为什么选 KTH57xx

<p class="c-sec-lead">测量 X、Y、Z 三轴磁场，I2C / SPI 可选，工作模式在线配置，兼顾性能与功耗</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>单芯片两轴</h3><p>一颗芯片同时测 X、Y、Z 三轴，无需两路器件拼装。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>小尺寸封装</h3><p>提供 DFN2*2.5-8L 与 QFN3x3-16L 封装。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>模式可配</h3><p>持续感应、唤醒睡眠、单次测量三种模式在线切换。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>功耗可调</h3><p>平均 25.2 μA @ 5 Hz、113.7 μA @ 25 Hz，按刷新率取舍。</p></div></div></div>

<div class="c-grid c-grid--2"><a class="c-card" href="/msite/products/3d-hall/kth57"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth57.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57 系列</span><h3>三轴线性霍尔传感器</h3><p>测量 X、Y、Z 三轴磁场，I2C / SPI 可选，工作模式在线配置，兼顾性能与功耗</p><span class="c-card__more">查看产品</span></div></a></div>

## 设计注意点

<p class="c-sec-lead">通用工程建议，实际设计以产品手册与实测为准。</p>

<ul class="c-checklist"><li>摇杆回中位置应尽量落在磁场解算的线性区中心，机械限位角度要与磁场可测范围匹配。</li><li>薄型机身里磁铁离芯片很近，要核对最近距离下磁场是否超出工作范围。</li><li>两支摇杆间距较近时要评估互相串扰，必要时错位布置或减小磁铁尺寸。</li><li>上电时做一次零点采集并存为基准，可以吸收装配偏差带来的静态偏移。</li></ul>

## 相关案例

<div class="c-grid c-grid--4"><a class="c-card" href="/msite/applications/consumer-electronics/game-controller"><div class="c-card__media c-media--case"><img src="/msite/img/case/consumer-electronics-4.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH564X</span><h3>游戏手柄</h3><p>把扳机键与摇杆的行程转成连续模拟量输出。</p><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/msite/applications/consumer-electronics/wheelchair-joystick"><div class="c-card__media c-media--case"><img src="/msite/img/case/consumer-electronics-2.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57xx</span><h3>轮椅摇杆</h3><p>把摇杆的两轴倾角转成连续的速度与方向指令。</p><span class="c-card__more">查看案例</span></div></a></div>

<div class="c-cta"><div><h2 class="c-cta__title">需要选型建议、样品或技术支持？</h2><p>昆泰芯提供芯片选型、磁场仿真与方案设计支持，欢迎与我们的销售和技术团队联系。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/msite/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
