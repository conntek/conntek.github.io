---
title: "气缸位置检测 · 工业4.0应用"
description: "卡在气缸外壁安装槽里，感应活塞磁环，输出活塞是否到位的开关信号。"
aside: false
pageClass: "c-page c-page--case"
ld: "{\"@context\": \"https://schema.org\", \"@type\": \"TechArticle\", \"headline\": \"气缸位置检测：工业4.0应用方案\", \"description\": \"卡在气缸外壁安装槽里，感应活塞磁环，输出活塞是否到位的开关信号。\", \"about\": \"气缸位置检测\", \"author\": {\"@type\": \"Organization\", \"name\": \"昆泰芯微电子\", \"alternateName\": \"CONNTEK\", \"url\": \"https://conntek.grosso.link/\"}, \"publisher\": {\"@type\": \"Organization\", \"name\": \"昆泰芯微电子\", \"alternateName\": \"CONNTEK\", \"url\": \"https://conntek.grosso.link/\"}, \"url\": \"https://conntek.grosso.link/applications/industry4/cylinder-position\"}"
---

<nav class="c-crumbs"><a href="/">首页</a><i>/</i><a href="/applications/">市场应用</a><i>/</i><a href="/applications/industry4">工业4.0</a><i>/</i><span>气缸位置检测</span></nav>

<p class="c-kicker">工业4.0</p>

# 气缸位置检测

<p class="c-lead">卡在气缸外壁安装槽里，感应活塞磁环，输出活塞是否到位的开关信号。</p>

<div class="c-actions"><a class="c-btn c-btn--brand" href="/products/switch/ktm28">推荐芯片 KTM280X</a><a class="c-btn" href="/contact">方案咨询</a></div>

## 场景说明

<div class="c-split c-split--overview"><div class="c-split__text">

气动系统里，活塞上装一圈永磁环，缸体多为不导磁的铝材。位置开关卡在缸体外壁的安装槽里，活塞运动到行程端点时磁环经过传感器下方，开关输出信号给 PLC，作为下一步动作的联锁条件。一台自动化设备上常有几十只气缸，每只气缸装两个开关，分别检测伸出到位和缩回到位。

早期多用干簧管开关，机械触点存在抖动和寿命问题；磁阻式开关没有触点，更适合高频往复动作。现场的难点集中在几处：接线有两线和三线两种，PLC 输入又分源型和漏型；相邻气缸的磁环和焊接设备的大电流电缆会带来干扰场；活塞速度快时，磁环在感应区内停留的时间很短。

</div><div class="c-split__media c-split__media--frame c-split__media--case"><img src="/img/case/industry4-cylinder-position.webp" alt="气缸位置检测" loading="lazy"></div></div>

## 检测需求

<p class="c-sec-lead">气缸位置检测对传感器的主要要求。</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>两线三线通用</h3><p>现场接线方式不统一，一款开关最好都能接。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>高速不漏检</h3><p>活塞高速经过端位，信号持续时间很短。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>接线故障保护</h3><p>现场接线常有短路或接错，不能一次损坏。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>磁环极性不限</h3><p>磁环充磁方向不统一，开关不应挑极性。</p></div></div></div>

## 为什么选 KTM280X

<p class="c-sec-lead">SIP 集成 AMR 与 ASIC，支持两线 / 三线气缸位置检测，任意极性感应水平磁场</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>两线三线兼容</h3><p>支持两线与三线接法，三线时等效负载 ≤ 50 kΩ。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>负载自适应</h3><p>开漏输出，上拉或下拉负载自适应；输出过流保护 220 mA。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>响应快</h3><p>工作频率 4 kHz，活塞高速经过端位时不易漏检。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>任意极性感应</h3><p>全极感应，BOP ±18 Gs、BRP ±16 Gs，磁环装反也能动作。</p></div></div></div>

<div class="c-grid c-grid--2"><a class="c-card" href="/products/switch/ktm28"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm28.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM28 系列</span><h3>AMR 高压气缸开关</h3><p>SIP 集成 AMR 与 ASIC，支持两线 / 三线气缸位置检测，任意极性感应水平磁场</p><span class="c-card__more">查看产品</span></div></a></div>

## 设计注意点

<p class="c-sec-lead">通用工程建议，实际设计以产品手册与实测为准。</p>

<ul class="c-checklist"><li>先确认 PLC 输入是源型还是漏型，对应开关接下拉或上拉负载，再决定采用两线还是三线接法。</li><li>两线接法时传感器自身工作电流会作为关断态电流流过 PLC 输入，需核对它低于输入模块的关断判定门限。</li><li>全极感应下，磁环两端的反向磁场也可能达到阈值，安装后应沿整个行程移动活塞，确认只出现一个动作区。</li><li>相邻气缸间距过小或缸体旁有钢制夹具时，磁环磁场会被分流或叠加，定位后应在整机状态下复核开关点。</li></ul>

## 相关案例

<div class="c-grid c-grid--4"><a class="c-card" href="/applications/industry4/gripper"><div class="c-card__media c-media--case"><img src="/img/case/industry4-gripper.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH71xx</span><h3>夹爪</h3><p>测量电动夹爪驱动电机或手指关节的转角，用于开合位置反馈与夹持动作控制。</p><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/applications/industry4/linear-motor"><div class="c-card__media c-media--case"><img src="/img/case/industry4-linear-motor.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM58xx</span><h3>直线电机</h3><p>细分直线电机磁栅或光栅读头的正余弦信号，得到动子的高分辨率位置。</p><span class="c-card__more">查看案例</span></div></a></div>

<div class="c-cta"><div><h2 class="c-cta__title">需要选型建议、样品或技术支持？</h2><p>昆泰芯提供芯片选型、磁场仿真与方案设计支持，欢迎与我们的销售和技术团队联系。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
