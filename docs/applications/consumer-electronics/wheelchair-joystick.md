---
title: "轮椅摇杆 · 消费类电子应用"
description: "把摇杆的两轴倾角转成连续的速度与方向指令。"
aside: false
pageClass: "c-page c-page--case"
---

<nav class="c-crumbs"><a href="/msite/">首页</a><i>/</i><a href="/msite/applications/">市场应用</a><i>/</i><a href="/msite/applications/consumer-electronics">消费类电子</a><i>/</i><span>轮椅摇杆</span></nav>

<p class="c-kicker">消费类电子</p>

# 轮椅摇杆

<p class="c-lead">把摇杆的两轴倾角转成连续的速度与方向指令。</p>

<div class="c-actions"><a class="c-btn c-btn--brand" href="/msite/products/3d-hall/kth57">推荐芯片 KTH57xx</a><a class="c-btn" href="/msite/contact">方案咨询</a></div>

## 场景说明

<div class="c-split c-split--overview"><div class="c-split__text">

电动轮椅的操作摇杆需要把使用者手上的推杆动作，连续地转成前后速度与左右转向量。摇杆下方装一颗磁铁，磁铁随推杆摆动，传感器测出磁场矢量的偏转方向与幅度，主控再换算成两轴位移量。

摇杆是轮椅上使用最频繁的部件，室外要经历雨水、灰尘与温差，还要长期承受推靠与碰撞。磁式方案不需要机械接触与电位器滑道，磨损与进液的失效途径都被去掉了。

</div><div class="c-split__media c-split__media--frame c-split__media--case"><img src="/msite/img/case/consumer-electronics-2.webp" alt="轮椅摇杆" loading="lazy"></div></div>

## 检测需求

<p class="c-sec-lead">轮椅摇杆对传感器的主要要求。</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>两轴连续量</h3><p>需要连续的角度或位移量，不是几档开关量。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>无接触磨损</h3><p>每天上千次操作，机械接触式结构寿命有限。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>防水防尘</h3><p>室外使用，传感与操作面之间最好完全隔离。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>宽温工作</h3><p>室外冬夏温差大，零位与灵敏度都不能随温度跑。</p></div></div></div>

## 为什么选 KTH57xx

<p class="c-sec-lead">测量 X、Y、Z 三轴磁场，I2C / SPI 可选，工作模式在线配置，兼顾性能与功耗</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>三轴磁场测量</h3><p>同时测 X、Y、Z 三轴，可直接解出摇杆的两轴摆动量。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>隔空检测</h3><p>磁铁与芯片之间可以整面密封，无需机械贯穿。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>温度补偿</h3><p>集成温度传感器与内部补偿，减小灵敏度温漂。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>宽温范围</h3><p>工作温度 -40 ~ 125 ℃，覆盖室外使用环境。</p></div></div></div>

<div class="c-grid c-grid--2"><a class="c-card" href="/msite/products/3d-hall/kth57"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth57.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57 系列</span><h3>三轴线性霍尔传感器</h3><p>测量 X、Y、Z 三轴磁场，I2C / SPI 可选，工作模式在线配置，兼顾性能与功耗</p><span class="c-card__more">查看产品</span></div></a></div>

## 设计注意点

<p class="c-sec-lead">通用工程建议，实际设计以产品手册与实测为准。</p>

<ul class="c-checklist"><li>先定磁铁的充磁方向与摆动中心到芯片的距离，再决定用在轴还是离轴摆放，两者的解算方式不同。</li><li>行程两端对应的磁场分量应落在芯片工作范围内（XY 轴典型 ±130 mT、Z 轴典型 ±80 mT），留出装配偏差余量。</li><li>轮椅电机与电缆会产生外磁场，摇杆位置应尽量远离，必要时加导磁屏蔽罩。</li><li>回中弹簧的机械零位与磁场零位不一定重合，量产时需要留一次上电零点标定的入口。</li></ul>

## 相关案例

<div class="c-grid c-grid--4"><a class="c-card" href="/msite/applications/consumer-electronics/handheld-joystick"><div class="c-card__media c-media--case"><img src="/msite/img/case/consumer-electronics-5.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57xx</span><h3>掌机摇杆</h3><p>在很薄的机身里测出摇杆两轴摆角，避免电位器漂移。</p><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/msite/applications/consumer-electronics/game-controller"><div class="c-card__media c-media--case"><img src="/msite/img/case/consumer-electronics-4.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH564X</span><h3>游戏手柄</h3><p>把扳机键与摇杆的行程转成连续模拟量输出。</p><span class="c-card__more">查看案例</span></div></a></div>

<div class="c-cta"><div><h2 class="c-cta__title">需要选型建议、样品或技术支持？</h2><p>昆泰芯提供芯片选型、磁场仿真与方案设计支持，欢迎与我们的销售和技术团队联系。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/msite/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
