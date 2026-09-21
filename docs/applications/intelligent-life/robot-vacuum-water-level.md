---
title: "扫地机-水位监测 · 智能生活应用"
description: "用带磁浮子判断清水箱与污水箱的水位是否到达阈值。"
aside: false
pageClass: "c-page c-page--case"
ld: "{\"@context\": \"https://schema.org\", \"@type\": \"TechArticle\", \"headline\": \"扫地机-水位监测：智能生活应用方案\", \"description\": \"用带磁浮子判断清水箱与污水箱的水位是否到达阈值。\", \"about\": \"扫地机-水位监测\", \"author\": {\"@type\": \"Organization\", \"name\": \"昆泰芯微电子\", \"alternateName\": \"CONNTEK\", \"url\": \"https://conntek.github.io/\"}, \"publisher\": {\"@type\": \"Organization\", \"name\": \"昆泰芯微电子\", \"alternateName\": \"CONNTEK\", \"url\": \"https://conntek.github.io/\"}, \"url\": \"https://conntek.github.io/applications/intelligent-life/robot-vacuum-water-level\"}"
---

<nav class="c-crumbs"><a href="/">首页</a><i>/</i><a href="/applications/">市场应用</a><i>/</i><a href="/applications/intelligent-life">智能生活</a><i>/</i><span>扫地机-水位监测</span></nav>

<p class="c-kicker">智能生活</p>

# 扫地机-水位监测

<p class="c-lead">用带磁浮子判断清水箱与污水箱的水位是否到达阈值。</p>

<div class="c-actions"><a class="c-btn c-btn--brand" href="/products/switch/ktm13">推荐芯片 KTM13xx</a><a class="c-btn" href="/contact">方案咨询</a></div>

## 场景说明

<div class="c-split c-split--overview"><div class="c-split__text">

扫地机的清水箱缺水要停止出水，污水箱满了要提示倒水。常见做法是在水箱里放一个内嵌磁铁的浮子，浮子随液面升降，箱壁外侧的磁开关在浮子经过时翻转，给出到达阈值的信号。

水箱是频繁拆装、需要清洗的部件，任何电气件都不能进到水里。浮子加磁开关的组合把电路完全留在箱体之外，隔着塑料壁感应，不存在密封失效导致漏电的路径。

</div><div class="c-split__media c-split__media--frame c-split__media--case"><img src="/img/case/intelligent-life-4.webp" alt="扫地机-水位监测" loading="lazy"></div></div>

## 检测需求

<p class="c-sec-lead">扫地机-水位监测对传感器的主要要求。</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>电路不进水</h3><p>水箱可拆可洗，传感器必须留在箱体外。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>隔壁感应</h3><p>隔着塑料箱壁工作，气隙由壁厚与浮子行程决定。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>低功耗</h3><p>电池供电设备上的水位监测需长期守候。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>翻转确定</h3><p>液面晃动时输出不能反复抖动。</p></div></div></div>

## 为什么选 KTM13xx

<p class="c-sec-lead">TMR 阻桥与 ASIC 单芯片集成，平行磁场感应，回差可小于 3 高斯</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>纳安级功耗</h3><p>50 Hz 档平均功耗 160 nA @ 3 V，可挂在电池上常驻。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>小回差</h3><p>回差可小于 3 高斯，浮子到位与离开的判定更明确。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>平行磁场感应</h3><p>对平行磁场敏感，适合浮子沿箱壁上下滑动的结构。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>磁极类型可选</h3><p>全极、单 S 极、单 N 极与锁存型，按浮子装向选。</p></div></div></div>

<div class="c-grid c-grid--2"><a class="c-card" href="/products/switch/ktm13"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm13.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM13 系列</span><h3>TMR 磁阻开关</h3><p>TMR 阻桥与 ASIC 单芯片集成，平行磁场感应，回差可小于 3 高斯</p><span class="c-card__more">查看产品</span></div></a></div>

## 设计注意点

<p class="c-sec-lead">通用工程建议，实际设计以产品手册与实测为准。</p>

<ul class="c-checklist"><li>浮子磁铁的充磁方向要与芯片敏感方向一致，并保证浮子在导向柱上不会翻转。</li><li>液面晃动会让浮子在阈值附近反复经过，可靠机械阻尼或软件消抖处理。</li><li>选单极型时可利用磁极方向排除浮子装反的情况，全极型则不区分磁极。</li><li>水温变化与长期泡水会影响浮子浮力与磁铁性能，选型应留出磁场余量。</li></ul>

## 相关案例

<div class="c-grid c-grid--4"><a class="c-card" href="/applications/intelligent-life/smart-toilet-water-level"><div class="c-card__media c-media--case"><img src="/img/case/intelligent-life-10.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM13xx</span><h3>智能马桶-水位监测</h3><p>用带磁浮子判断水箱液位是否到达上下限阈值。</p><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/applications/intelligent-life/robot-vacuum"><div class="c-card__media c-media--case"><img src="/img/case/intelligent-life-3.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57xx</span><h3>扫地机器人-真空吸尘器</h3><p>检测拖布、滚刷等可换模块的安装位置与抬升行程。</p><span class="c-card__more">查看案例</span></div></a></div>

<div class="c-cta"><div><h2 class="c-cta__title">需要选型建议、样品或技术支持？</h2><p>昆泰芯提供芯片选型、磁场仿真与方案设计支持，欢迎与我们的销售和技术团队联系。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
