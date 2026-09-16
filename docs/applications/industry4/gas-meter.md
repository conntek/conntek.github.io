---
title: "燃气表 · 工业4.0应用"
description: "对计量机构上的磁铁计数，把气体流量转成脉冲。"
aside: false
pageClass: "c-page c-page--case"
---

<nav class="c-crumbs"><a href="/msite/">首页</a><i>/</i><a href="/msite/applications/">市场应用</a><i>/</i><a href="/msite/applications/industry4">工业4.0</a><i>/</i><span>燃气表</span></nav>

<p class="c-kicker">工业4.0</p>

# 燃气表

<p class="c-lead">对计量机构上的磁铁计数，把气体流量转成脉冲。</p>

<div class="c-actions"><a class="c-btn c-btn--brand" href="/msite/products/switch/ktm13">推荐芯片 KTM13xx</a><a class="c-btn" href="/msite/contact">方案咨询</a></div>

## 场景说明

<div class="c-split c-split--overview"><div class="c-split__text">

膜式燃气表的计量机构随着气体流过而转动，在字轮或计数轴上装磁铁，旁边的磁开关每转过一圈输出一个脉冲，主控累加脉冲就得到用气量。这是把机械计量转成电子读数最直接的一条路。

燃气表通常用一次电池供电并要求多年免维护，表体安装在户外或厨房橱柜内，全年温差大。所以计数环节的平均功耗、以及低温高温下阈值的稳定性，往往比精度指标更关键。

</div><div class="c-split__media c-split__media--frame c-split__media--case"><img src="/msite/img/case/industry4-2.webp" alt="燃气表" loading="lazy"></div></div>

## 检测需求

<p class="c-sec-lead">燃气表对传感器的主要要求。</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>超低功耗</h3><p>一次电池要支撑多年，计数电路必须常驻且省电。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>不漏计不多计</h3><p>脉冲数直接对应计费，翻转必须干净可靠。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>宽温稳定</h3><p>户外与橱柜内全年温差大，阈值不能随温度跑。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>防磁攻击</h3><p>外部强磁可能使计数停止，需要可识别的检测方式。</p></div></div></div>

## 为什么选 KTM13xx

<p class="c-sec-lead">TMR 阻桥与 ASIC 单芯片集成，平行磁场感应，回差可小于 3 高斯</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>纳安级功耗</h3><p>平均功耗 160 nA @ 3 V，一次电池支撑多年计量。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>小回差</h3><p>回差可小于 3 高斯，字轮慢转时翻转点仍确定。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>两维感应</h3><p>不同方向 TMR 桥阻配合可做 360° 两维感应。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>宽温范围</h3><p>户外与橱柜全年温差大，-40 ~ 125 ℃ 全覆盖。</p></div></div></div>

<div class="c-grid c-grid--2"><a class="c-card" href="/msite/products/switch/ktm13"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/ktm13.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM13 系列</span><h3>TMR 磁阻开关</h3><p>TMR 阻桥与 ASIC 单芯片集成，平行磁场感应，回差可小于 3 高斯</p><span class="c-card__more">查看产品</span></div></a></div>

## 设计注意点

<p class="c-sec-lead">通用工程建议，实际设计以产品手册与实测为准。</p>

<ul class="c-checklist"><li>计量轴转速很低，磁场变化缓慢，选型时要确认在最低转速下仍能稳定翻转。</li><li>用两路检测并让其相位错开，可在计数之外得到转动方向，识别倒转。</li><li>外部强磁攻击表现为磁场长时间维持在一侧，可在软件中按持续时间判定并记录事件。</li><li>燃气环境对器件与结构有安全要求，磁铁与传感器的安装需符合表具整体的防爆与密封设计。</li></ul>

## 相关案例

<div class="c-grid c-grid--4"><a class="c-card" href="/msite/applications/industry4/mechanical-meter"><div class="c-card__media c-media--case"><img src="/msite/img/case/industry4-5.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM13xx</span><h3>机械电表</h3><p>对机械字轮上的磁铁计数，把机械读数转成电子脉冲。</p><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/msite/applications/industry4/electricity-meter"><div class="c-card__media c-media--case"><img src="/msite/img/case/industry4-0.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57xx</span><h3>电表</h3><p>监测表内异常外部磁场，识别用强磁干扰计量的行为。</p><span class="c-card__more">查看案例</span></div></a></div>

<div class="c-cta"><div><h2 class="c-cta__title">需要选型建议、样品或技术支持？</h2><p>昆泰芯提供芯片选型、磁场仿真与方案设计支持，欢迎与我们的销售和技术团队联系。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/msite/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
