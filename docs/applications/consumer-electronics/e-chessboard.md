---
title: "电子棋盘 · 消费类电子应用"
description: "逐格检测棋子有无，把棋盘上的落子位置变成可读的数字信号。"
aside: false
pageClass: "c-page c-page--case"
---

<nav class="c-crumbs"><a href="/msite/">首页</a><i>/</i><a href="/msite/applications/">市场应用</a><i>/</i><a href="/msite/applications/consumer-electronics">消费类电子</a><i>/</i><span>电子棋盘</span></nav>

<p class="c-kicker">消费类电子</p>

# 电子棋盘

<p class="c-lead">逐格检测棋子有无，把棋盘上的落子位置变成可读的数字信号。</p>

<div class="c-actions"><a class="c-btn c-btn--brand" href="/msite/products/switch/kth16">推荐芯片 KTH1604</a><a class="c-btn" href="/msite/contact">方案咨询</a></div>

## 场景说明

<div class="c-split c-split--overview"><div class="c-split__text">

电子棋盘在每颗棋子底部嵌一颗小磁铁，棋盘面板下按格子排布传感器阵列，棋子放上或拿走时对应格子的输出翻转，主控扫描整个阵列就得到当前局面。

棋盘是全封闭面板，传感器不能露出，只能隔着一层面板感应，属于典型的隔空检测。一块十九路棋盘可能要上百个检测点，单点的功耗、成本与占板面积会被格子数直接放大，因此单点指标比精度更关键。

</div><div class="c-split__media c-split__media--frame c-split__media--case"><img src="/msite/img/case/consumer-electronics-1.webp" alt="电子棋盘" loading="lazy"></div></div>

## 检测需求

<p class="c-sec-lead">电子棋盘对传感器的主要要求。</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>点数多</h3><p>阵列动辄数十上百点，单点功耗与面积直接乘以点数。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>隔面板检测</h3><p>隔着面板感应，有效气隙由面板厚度决定。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>一致性好</h3><p>各格阈值需接近，否则同一颗棋子在不同格表现不同。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>电池供电</h3><p>便携棋盘多用电池，整机待机电流要控制。</p></div></div></div>

## 为什么选 KTH1604

<p class="c-sec-lead">CMOS 工艺集成霍尔元件，1 μA 超低功耗，温度补偿优良，覆盖全极、单极与锁存型</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>微功耗</h3><p>KTH1604 平均功耗 1.6 μA @ 1.8 V（5 Hz 版本），适合大规模阵列。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>1 毫米级封装</h3><p>DFN/FBP 1*1-4L 封装，密排格子时占板面积小。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>低压工作</h3><p>供电 1.6 ~ 5.5 V，可直接跟随电池电压工作。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>多档阈值</h3><p>BOP 提供 46 / 33 / 22 Gs 三档，按面板厚度选灵敏度。</p></div></div></div>

<div class="c-grid c-grid--2"><a class="c-card" href="/msite/products/switch/kth16"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth16.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH13/16/17 系列</span><h3>微功耗 1D 霍尔开关</h3><p>CMOS 工艺集成霍尔元件，1 μA 超低功耗，温度补偿优良，覆盖全极、单极与锁存型</p><span class="c-card__more">查看产品</span></div></a></div>

## 设计注意点

<p class="c-sec-lead">通用工程建议，实际设计以产品手册与实测为准。</p>

<ul class="c-checklist"><li>先按面板厚度与磁铁尺寸估算格心处的磁场，再倒推该选哪一档 BOP，不要先定芯片再补磁铁。</li><li>格间距过小时相邻格会互相串扰，可以缩小磁铁、加大格距，或让相邻行列错开布置。</li><li>扫描频率决定了落子响应速度，20 Hz 与 5 Hz 两种版本对应不同的功耗与响应折中。</li><li>面板下的金属加强筋、电池片会削弱磁场，应在整机装配状态下复测各格的翻转余量。</li></ul>

## 相关案例

<div class="c-grid c-grid--4"><a class="c-card" href="/msite/applications/consumer-electronics/stylus"><div class="c-card__media c-media--case"><img src="/msite/img/case/consumer-electronics-0.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM13xx</span><h3>触控笔</h3><p>检测笔身与屏幕侧边、笔帽或收纳仓的磁吸贴合状态，用于唤醒与休眠。</p><span class="c-card__more">查看案例</span></div></a></div>

<div class="c-cta"><div><h2 class="c-cta__title">需要选型建议、样品或技术支持？</h2><p>昆泰芯提供芯片选型、磁场仿真与方案设计支持，欢迎与我们的销售和技术团队联系。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/msite/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
