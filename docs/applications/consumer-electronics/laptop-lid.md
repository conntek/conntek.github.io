---
title: "笔记本与平板合盖检测 · 消费类电子应用"
description: "检测屏幕与机身的开合状态，触发笔记本与平板的休眠、唤醒和平板模式切换。"
aside: false
pageClass: "c-page c-page--case"
ld: "{\"@context\": \"https://schema.org\", \"@type\": \"TechArticle\", \"headline\": \"笔记本与平板合盖检测：消费类电子应用方案\", \"description\": \"检测屏幕与机身的开合状态，触发笔记本与平板的休眠、唤醒和平板模式切换。\", \"about\": \"笔记本与平板合盖检测\", \"author\": {\"@type\": \"Organization\", \"name\": \"昆泰芯微电子\", \"alternateName\": \"CONNTEK\", \"url\": \"https://conntek.github.io/\"}, \"publisher\": {\"@type\": \"Organization\", \"name\": \"昆泰芯微电子\", \"alternateName\": \"CONNTEK\", \"url\": \"https://conntek.github.io/\"}, \"url\": \"https://conntek.github.io/applications/consumer-electronics/laptop-lid\"}"
---

<nav class="c-crumbs"><a href="/">首页</a><i>/</i><a href="/applications/">市场应用</a><i>/</i><a href="/applications/consumer-electronics">消费类电子</a><i>/</i><span>笔记本与平板合盖检测</span></nav>

<p class="c-kicker">消费类电子</p>

# 笔记本与平板合盖检测

<p class="c-lead">检测屏幕与机身的开合状态，触发笔记本与平板的休眠、唤醒和平板模式切换。</p>

<div class="c-actions"><a class="c-btn c-btn--brand" href="/products/switch/ktm13">推荐芯片 KTM13xx</a><a class="c-btn" href="/contact">方案咨询</a></div>

## 场景说明

<div class="c-split c-split--overview"><div class="c-split__text">

笔记本合盖检测通常把一颗小磁铁嵌在屏幕边框里，磁开关贴在机身掌托下方的对应位置。合盖时磁铁靠近，开关翻转，主控据此关屏并进入睡眠；开盖时再唤醒系统。可翻转到背面的二合一机型还要识别屏幕折到背面的状态，用来切换平板模式、关闭键盘输入；平板配磁吸键盘盖时，也用同样的方式判断盖板是否贴合。

这个检测在整机彻底关机前一直在工作，本身就是待机功耗的一部分。机身越做越薄，磁铁只能用小尺寸，隔着边框和外壳，到达芯片的磁场并不强；扬声器磁体、铰链钢件、磁吸手写笔和各类磁吸配件又在周围形成干扰场。传统方案多用干簧管，存在玻璃管易碎、个体一致性差、需要较强磁场才能吸合的问题。

</div><div class="c-split__media c-split__media--frame c-split__media--case"><img src="/img/case/consumer-electronics-laptop-lid.webp" alt="笔记本与平板合盖检测" loading="lazy"></div></div>

## 检测需求

<p class="c-sec-lead">笔记本与平板合盖检测对传感器的主要要求。</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>常驻低功耗</h3><p>睡眠状态下也要持续监测，功耗直接计入待机时间。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>弱磁可触发</h3><p>磁铁小，又隔着边框与外壳，到达芯片的磁场弱。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>抗周边磁场</h3><p>扬声器与磁吸配件的磁场不能造成误判合盖。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>薄型贴装</h3><p>掌托下方空间很薄，元件高度与面积都受限。</p></div></div></div>

## 为什么选 KTM13xx

<p class="c-sec-lead">TMR 阻桥与 ASIC 单芯片集成，平行磁场感应，回差可小于 3 高斯</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>平行磁场感应</h3><p>对平行磁场敏感，配合不同方向桥阻可做 360° 两维感应。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>低阈值档位</h3><p>全极型 BOP 最低 ±7 高斯，小磁铁隔着外壳也能触发。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>薄型封装</h3><p><a class="c-xref" href="/products/switch/ktm13/ktm1304sb">KTM1304</a> 提供 DFN2*2-3L 封装，适合薄型主板贴装。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>低压常开供电</h3><p>1.8 ~ 5.5 V 供电，平均功耗低至 160 nA @ 3 V。</p></div></div></div>

<div class="c-grid c-grid--2"><a class="c-card" href="/products/switch/ktm13"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm13.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM13 系列</span><h3>TMR 磁阻开关</h3><p>TMR 阻桥与 ASIC 单芯片集成，平行磁场感应，回差可小于 3 高斯</p><span class="c-card__more">查看产品</span></div></a></div>

## 设计注意点

<p class="c-sec-lead">通用工程建议，实际设计以产品手册与实测为准。</p>

<ul class="c-checklist"><li>从霍尔开关换成 TMR 开关时，敏感方向由垂直芯片表面变为平行芯片表面，磁铁充磁方向或安装姿态要相应转 90°。</li><li>分别算出合盖、最小开合角度和折到背面三个位置的磁场，BOP 取在合盖场强之下、BRP 高于开盖残余场，两侧都留裕量。</li><li>把扬声器、手写笔磁吸位、磁吸键盘盖等磁源逐一列出，按最坏叠加核对开盖状态下的磁场仍低于 BRP。</li><li>需要同时区分合盖与折到背面时，可在两个磁铁位置各放一颗开关，或选单 S 极 / 单 N 极型，让两个状态对应相反的磁极。</li></ul>

## 相关案例

<div class="c-grid c-grid--4"><a class="c-card" href="/applications/consumer-electronics/stylus"><div class="c-card__media c-media--case"><img src="/img/case/consumer-electronics-0.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM13xx</span><h3>触控笔</h3><p>检测笔身与屏幕侧边、笔帽或收纳仓的磁吸贴合状态，用于唤醒与休眠。</p><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/applications/consumer-electronics/smart-watch"><div class="c-card__media c-media--case"><img src="/img/case/consumer-electronics-6.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57xx</span><h3>智能手表</h3><p>检测旋转表冠的转动角度与方向，用于翻页与调节。</p><span class="c-card__more">查看案例</span></div></a></div>

<div class="c-cta"><div><h2 class="c-cta__title">需要选型建议、样品或技术支持？</h2><p>昆泰芯提供芯片选型、磁场仿真与方案设计支持，欢迎与我们的销售和技术团队联系。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
