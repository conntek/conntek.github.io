---
title: "智能马桶-水位监测 · 智能生活应用"
description: "用带磁浮子判断水箱液位是否到达上下限阈值。"
aside: false
pageClass: "c-page c-page--case"
---

<nav class="c-crumbs"><a href="/msite/">首页</a><i>/</i><a href="/msite/applications/">市场应用</a><i>/</i><a href="/msite/applications/intelligent-life">智能生活</a><i>/</i><span>智能马桶-水位监测</span></nav>

<p class="c-kicker">智能生活</p>

# 智能马桶-水位监测

<p class="c-lead">用带磁浮子判断水箱液位是否到达上下限阈值。</p>

<div class="c-actions"><a class="c-btn c-btn--brand" href="/msite/products/switch/ktm13">推荐芯片 KTM13xx</a><a class="c-btn" href="/msite/contact">方案咨询</a></div>

## 场景说明

<div class="c-split c-split--overview"><div class="c-split__text">

带即热或储热水箱的智能马桶需要知道箱内水位，低于下限要补水、高于上限要停止进水，同时为加热部件提供干烧保护的前提条件。水箱内放带磁浮子，箱壁外放磁开关，浮子经过时给出翻转信号。

水箱内壁长期泡水并可能结垢，任何插入液体的电极式方案都要面对结垢和腐蚀。浮子加磁开关的组合把电路完全留在水外，检测面只隔一层塑料壁。

</div><div class="c-split__media c-split__media--frame c-split__media--case"><img src="/msite/img/case/intelligent-life-10.webp" alt="智能马桶-水位监测" loading="lazy"></div></div>

## 检测需求

<p class="c-sec-lead">智能马桶-水位监测对传感器的主要要求。</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>电路不接触水</h3><p>长期泡水与结垢会让电极式方案失效。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>隔壁感应</h3><p>隔着水箱壁检测，壁上结垢还会再加一段距离。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>上下限两点</h3><p>通常需要上下两个阈值点，各自要判定明确。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>长期可靠</h3><p>与加热干烧保护相关，误判后果比较严重。</p></div></div></div>

## 为什么选 KTM13xx

<p class="c-sec-lead">TMR 阻桥与 ASIC 单芯片集成，平行磁场感应，回差可小于 3 高斯</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>纳安级功耗</h3><p>平均功耗 160 nA @ 3 V，上下限两点都能常年守候。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>小回差</h3><p>回差可小于 3 高斯，液面晃动时不容易来回翻。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>锁存型可选</h3><p>锁存型 KTM1331 翻转后保持状态，适合上下限逻辑。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>宽温工作</h3><p>储热水箱附近偏热，125 ℃ 上限仍留有裕量。</p></div></div></div>

<div class="c-grid c-grid--2"><a class="c-card" href="/msite/products/switch/ktm13"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/ktm13.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM13 系列</span><h3>TMR 磁阻开关</h3><p>TMR 阻桥与 ASIC 单芯片集成，平行磁场感应，回差可小于 3 高斯</p><span class="c-card__more">查看产品</span></div></a></div>

## 设计注意点

<p class="c-sec-lead">通用工程建议，实际设计以产品手册与实测为准。</p>

<ul class="c-checklist"><li>上下限两个检测点的磁铁与芯片要拉开足够距离，避免浮子在一点翻转时影响另一点。</li><li>水箱结垢会使浮子行程变化，机械导向应便于清洁并留出余量。</li><li>锁存型与全极型在液面反复晃动时的行为不同，应按控制逻辑选择类型。</li><li>与加热相关的保护逻辑不宜只依赖单一磁开关，建议在系统层面另有独立判据。</li></ul>

## 相关案例

<div class="c-grid c-grid--4"><a class="c-card" href="/msite/applications/intelligent-life/robot-vacuum-water-level"><div class="c-card__media c-media--case"><img src="/msite/img/case/intelligent-life-4.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM13xx</span><h3>扫地机-水位监测</h3><p>用带磁浮子判断清水箱与污水箱的水位是否到达阈值。</p><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/msite/applications/intelligent-life/smart-toilet-pivot"><div class="c-card__media c-media--case"><img src="/msite/img/case/intelligent-life-6.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57xx</span><h3>智能马桶-枢轴检测</h3><p>检测盖板与坐圈在枢轴处的开合角度，用于落座与翻盖判断。</p><span class="c-card__more">查看案例</span></div></a></div>

<div class="c-cta"><div><h2 class="c-cta__title">需要选型建议、样品或技术支持？</h2><p>昆泰芯提供芯片选型、磁场仿真与方案设计支持，欢迎与我们的销售和技术团队联系。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/msite/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
