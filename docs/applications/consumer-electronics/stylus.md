---
title: "触控笔 · 消费类电子应用"
description: "检测笔身与屏幕侧边、笔帽或收纳仓的磁吸贴合状态，用于唤醒与休眠。"
aside: false
pageClass: "c-page c-page--case"
ld: "{\"@context\": \"https://schema.org\", \"@type\": \"TechArticle\", \"headline\": \"触控笔：消费类电子应用方案\", \"description\": \"检测笔身与屏幕侧边、笔帽或收纳仓的磁吸贴合状态，用于唤醒与休眠。\", \"about\": \"触控笔\", \"author\": {\"@type\": \"Organization\", \"name\": \"昆泰芯微电子\", \"alternateName\": \"CONNTEK\", \"url\": \"https://conntek.github.io/\"}, \"publisher\": {\"@type\": \"Organization\", \"name\": \"昆泰芯微电子\", \"alternateName\": \"CONNTEK\", \"url\": \"https://conntek.github.io/\"}, \"url\": \"https://conntek.github.io/applications/consumer-electronics/stylus\"}"
---

<nav class="c-crumbs"><a href="/">首页</a><i>/</i><a href="/applications/">市场应用</a><i>/</i><a href="/applications/consumer-electronics">消费类电子</a><i>/</i><span>触控笔</span></nav>

<p class="c-kicker">消费类电子</p>

# 触控笔

<p class="c-lead">检测笔身与屏幕侧边、笔帽或收纳仓的磁吸贴合状态，用于唤醒与休眠。</p>

<div class="c-actions"><a class="c-btn c-btn--brand" href="/products/switch/ktm13">推荐芯片 KTM13xx</a><a class="c-btn" href="/contact">方案咨询</a></div>

## 场景说明

<div class="c-split c-split--overview"><div class="c-split__text">

主动式触控笔内置电池，整支笔的大部分时间并不在书写，而是吸附在平板侧边或插在收纳仓里。笔身或笔帽里放一颗小磁铁，笔内的磁开关判断它是否吸上去，从而决定进入深度休眠还是提前唤醒笔尖压感电路。

笔身直径通常只有一支铅笔粗，磁铁与传感器往往并排贴在笔杆内壁，磁场方向与芯片表面接近平行，且吸附前后的磁场变化量不大。这要求开关既能感应平行方向的磁场，又能在毫米级贴合距离变化上给出稳定的翻转。

</div><div class="c-split__media c-split__media--frame c-split__media--case"><img src="/img/case/consumer-electronics-0.webp" alt="触控笔" loading="lazy"></div></div>

## 检测需求

<p class="c-sec-lead">触控笔对传感器的主要要求。</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>极低静态功耗</h3><p>电池容量小，笔在待机状态必须常年监测磁场。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>平行磁场感应</h3><p>笔杆狭长，磁铁多为侧贴，磁场沿芯片表面方向穿过。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>翻转要干净</h3><p>贴合与脱开只差一两毫米，回差过大会漏检或反复抖动。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>封装要小</h3><p>笔杆内径有限，元件高度与占板面积都受限。</p></div></div></div>

## 为什么选 KTM13xx

<p class="c-sec-lead">TMR 阻桥与 ASIC 单芯片集成，平行磁场感应，回差可小于 3 高斯</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>纳安级功耗</h3><p>平均功耗低至 160 nA @ 3 V，常年待机监测不明显影响续航。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>平行磁场敏感</h3><p>TMR 阻桥随平行穿过的磁场变化，适合磁铁侧贴的笔杆结构。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>小回差</h3><p>回差可小于 3 高斯，贴合距离的小变化也能得到确定的翻转。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>小型封装</h3><p>提供 SOT-23-3L 与 DFN2*2-3L（<a class="c-xref" href="/products/switch/ktm13/ktm1304sb">KTM1304</a>）封装。</p></div></div></div>

<div class="c-grid c-grid--2"><a class="c-card" href="/products/switch/ktm13"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm13.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM13 系列</span><h3>TMR 磁阻开关</h3><p>TMR 阻桥与 ASIC 单芯片集成，平行磁场感应，回差可小于 3 高斯</p><span class="c-card__more">查看产品</span></div></a></div>

## 设计注意点

<p class="c-sec-lead">通用工程建议，实际设计以产品手册与实测为准。</p>

<ul class="c-checklist"><li>先确定磁铁的充磁方向与芯片敏感方向一致，再决定贴装位置；方向搞反时灵敏度会大幅下降。</li><li>按吸合与脱开两个极限位置分别算出磁场强度，再据此挑 BOP / BRP 档位，让两个状态都留出裕量。</li><li>笔杆内的金属结构件（笔夹、屏蔽罩）会改变磁路，布局定稿后应在整笔状态下复测。</li><li>全极型不区分磁极，单极型可利用磁极方向排除反向贴合的误触发，按装配方式二选一。</li></ul>

## 相关案例

<div class="c-grid c-grid--4"><a class="c-card" href="/applications/consumer-electronics/e-chessboard"><div class="c-card__media c-media--case"><img src="/img/case/consumer-electronics-1.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH1604</span><h3>电子棋盘</h3><p>逐格检测棋子有无，把棋盘上的落子位置变成可读的数字信号。</p><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/applications/consumer-electronics/smart-watch"><div class="c-card__media c-media--case"><img src="/img/case/consumer-electronics-6.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57xx</span><h3>智能手表</h3><p>检测旋转表冠的转动角度与方向，用于翻页与调节。</p><span class="c-card__more">查看案例</span></div></a></div>

<div class="c-cta"><div><h2 class="c-cta__title">需要选型建议、样品或技术支持？</h2><p>昆泰芯提供芯片选型、磁场仿真与方案设计支持，欢迎与我们的销售和技术团队联系。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
