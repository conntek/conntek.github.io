---
title: "智能手表 · 消费类电子应用"
description: "检测旋转表冠的转动角度与方向，用于翻页与调节。"
aside: false
pageClass: "c-page c-page--case"
ld: "{\"@context\": \"https://schema.org\", \"@type\": \"TechArticle\", \"headline\": \"智能手表：消费类电子应用方案\", \"description\": \"检测旋转表冠的转动角度与方向，用于翻页与调节。\", \"about\": \"智能手表\", \"author\": {\"@type\": \"Organization\", \"name\": \"昆泰芯微电子\", \"alternateName\": \"CONNTEK\", \"url\": \"https://conntek.github.io/\"}, \"publisher\": {\"@type\": \"Organization\", \"name\": \"昆泰芯微电子\", \"alternateName\": \"CONNTEK\", \"url\": \"https://conntek.github.io/\"}, \"url\": \"https://conntek.github.io/applications/consumer-electronics/smart-watch\"}"
---

<nav class="c-crumbs"><a href="/">首页</a><i>/</i><a href="/applications/">市场应用</a><i>/</i><a href="/applications/consumer-electronics">消费类电子</a><i>/</i><span>智能手表</span></nav>

<p class="c-kicker">消费类电子</p>

# 智能手表

<p class="c-lead">检测旋转表冠的转动角度与方向，用于翻页与调节。</p>

<div class="c-actions"><a class="c-btn c-btn--brand" href="/products/3d-hall/kth57">推荐芯片 KTH57xx</a><a class="c-btn" href="/contact">方案咨询</a></div>

## 场景说明

<div class="c-split c-split--overview"><div class="c-split__text">

智能手表的旋转表冠承担翻页、缩放与数值调节，需要连续的角度增量而不只是按下。表冠轴端装一颗小磁铁，芯片读出磁场方向随转动的变化，就能算出转过的角度与方向。

表冠是表壳上的开孔部位，也是最常见的进水路径。磁式检测可以把表冠轴与内部完全密封隔开，同时省掉编码器的机械触点，对整表的防水与寿命都有利。

</div><div class="c-split__media c-split__media--frame c-split__media--case"><img src="/img/case/consumer-electronics-6.webp" alt="智能手表" loading="lazy"></div></div>

## 检测需求

<p class="c-sec-lead">智能手表对传感器的主要要求。</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>体积极小</h3><p>表壳内寸土寸金，磁铁与芯片都只能做到毫米级。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>功耗极低</h3><p>电池容量很小，表冠检测要能长期守候。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>密封要求高</h3><p>表冠是进水路径，最好不做机械贯穿。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>方向可辨</h3><p>需要区分正反转，而不只是转了多少。</p></div></div></div>

## 为什么选 KTH57xx

<p class="c-sec-lead">测量 X、Y、Z 三轴磁场，I2C / SPI 可选，工作模式在线配置，兼顾性能与功耗</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>三轴矢量</h3><p>由多轴分量解出磁场方向，可分辨转动方向而不只是计数。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>唤醒睡眠模式</h3><p>支持唤醒睡眠与单次测量模式，不转动时压低平均功耗。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>低功耗档位</h3><p>平均 25.2 μA @ 5 Hz，适合可穿戴的长待机需求。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>手表类型号</h3><p>系列中 <a class="c-xref" href="/products/3d-hall/kth57">KTH5762</a> / <a class="c-xref" href="/products/3d-hall/kth57">KTH5763</a> 为手表类应用型号。</p></div></div></div>

<div class="c-grid c-grid--2"><a class="c-card" href="/products/3d-hall/kth57"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth57.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57 系列</span><h3>三轴线性霍尔传感器</h3><p>测量 X、Y、Z 三轴磁场，I2C / SPI 可选，工作模式在线配置，兼顾性能与功耗</p><span class="c-card__more">查看产品</span></div></a></div>

## 设计注意点

<p class="c-sec-lead">通用工程建议，实际设计以产品手册与实测为准。</p>

<ul class="c-checklist"><li>表冠磁铁一般沿径向充磁，芯片放在轴端正对位置，同心度偏差会造成角度周期性误差。</li><li>不同刷新率对应不同的最高可跟踪转速，快速拨动时不要让采样跟不上而丢圈。</li><li>表壳与表带扣中的金属件、扬声器磁体都会引入背景磁场，布局阶段就要评估。</li><li>外部强磁（如磁吸充电座、冰箱贴）可能造成误动作，软件侧可对异常大的磁场幅值做屏蔽。</li></ul>

## 相关案例

<div class="c-grid c-grid--4"><a class="c-card" href="/applications/consumer-electronics/stylus"><div class="c-card__media c-media--case"><img src="/img/case/consumer-electronics-0.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM13xx</span><h3>触控笔</h3><p>检测笔身与屏幕侧边、笔帽或收纳仓的磁吸贴合状态，用于唤醒与休眠。</p><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/applications/consumer-electronics/handheld-joystick"><div class="c-card__media c-media--case"><img src="/img/case/consumer-electronics-5.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57xx</span><h3>掌机摇杆</h3><p>在很薄的机身里测出摇杆两轴摆角，避免电位器漂移。</p><span class="c-card__more">查看案例</span></div></a></div>

<div class="c-cta"><div><h2 class="c-cta__title">需要选型建议、样品或技术支持？</h2><p>昆泰芯提供芯片选型、磁场仿真与方案设计支持，欢迎与我们的销售和技术团队联系。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
