---
title: "机械电表 · 工业4.0应用"
description: "对机械字轮上的磁铁计数，把机械读数转成电子脉冲。"
aside: false
pageClass: "c-page c-page--case"
ld: "{\"@context\": \"https://schema.org\", \"@type\": \"TechArticle\", \"headline\": \"机械电表：工业4.0应用方案\", \"description\": \"对机械字轮上的磁铁计数，把机械读数转成电子脉冲。\", \"about\": \"机械电表\", \"author\": {\"@type\": \"Organization\", \"name\": \"昆泰芯微电子\", \"alternateName\": \"CONNTEK\", \"url\": \"https://conntek.grosso.link/\"}, \"publisher\": {\"@type\": \"Organization\", \"name\": \"昆泰芯微电子\", \"alternateName\": \"CONNTEK\", \"url\": \"https://conntek.grosso.link/\"}, \"url\": \"https://conntek.grosso.link/applications/industry4/mechanical-meter\"}"
---

<nav class="c-crumbs"><a href="/">首页</a><i>/</i><a href="/applications/">市场应用</a><i>/</i><a href="/applications/industry4">工业4.0</a><i>/</i><span>机械电表</span></nav>

<p class="c-kicker">工业4.0</p>

# 机械电表

<p class="c-lead">对机械字轮上的磁铁计数，把机械读数转成电子脉冲。</p>

<div class="c-actions"><a class="c-btn c-btn--brand" href="/products/switch/ktm13">推荐芯片 KTM13xx</a><a class="c-btn" href="/contact">方案咨询</a></div>

## 场景说明

<div class="c-split c-split--overview"><div class="c-split__text">

存量的机械式表计要接入远程抄表系统时，常见做法是在最低位字轮上装一颗磁铁，旁边装磁开关，字轮每转一圈输出一个脉冲，由采集模块累加并上报，从而在不改动计量机构的前提下实现电子读数。

这类改造模块多为电池供电，安装后要求多年不换电池；字轮转速又很低，磁场变化缓慢。因此计数环节既要省电，又要在慢速磁场变化下保持确定的翻转。

</div><div class="c-split__media c-split__media--frame c-split__media--case"><img src="/img/case/industry4-5.webp" alt="机械电表" loading="lazy"></div></div>

## 检测需求

<p class="c-sec-lead">机械电表对传感器的主要要求。</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>超低功耗</h3><p>电池供电的采集模块要求多年免维护。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>慢速可靠翻转</h3><p>字轮转速低，磁场变化缓慢容易在阈值附近徘徊。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>不改计量机构</h3><p>只能在原表上加装，磁铁尺寸与位置受限。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>脉冲不丢</h3><p>脉冲对应用量，漏计直接造成账目差异。</p></div></div></div>

## 为什么选 KTM13xx

<p class="c-sec-lead">TMR 阻桥与 ASIC 单芯片集成，平行磁场感应，回差可小于 3 高斯</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>纳安级功耗</h3><p>160 nA @ 3 V，加装采集模块的电池负担很小。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>低频档位</h3><p>50 Hz 档对应最低功耗，字轮转速低用不上高频。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>平行磁场感应</h3><p>TMR 阻桥对平行磁场敏感，磁铁可侧贴字轮。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>多档阈值</h3><p>BOP / BRP 多档，按加装磁铁尺寸与安装距离选。</p></div></div></div>

<div class="c-grid c-grid--2"><a class="c-card" href="/products/switch/ktm13"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm13.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM13 系列</span><h3>TMR 磁阻开关</h3><p>TMR 阻桥与 ASIC 单芯片集成，平行磁场感应，回差可小于 3 高斯</p><span class="c-card__more">查看产品</span></div></a></div>

## 设计注意点

<p class="c-sec-lead">通用工程建议，实际设计以产品手册与实测为准。</p>

<ul class="c-checklist"><li>加装磁铁会给字轮带来额外负载与不平衡，磁铁质量应尽量小并做对称配重。</li><li>慢速穿越阈值时最容易出现临界徘徊，选较小回差档位并在软件中加计数确认。</li><li>两路错相检测可判断转向，避免字轮回摆时被重复计数。</li><li>加装件与原表之间的相对位置可能随振动变化，结构上应有可靠的固定与定位。</li></ul>

## 相关案例

<div class="c-grid c-grid--4"><a class="c-card" href="/applications/industry4/gas-meter"><div class="c-card__media c-media--case"><img src="/img/case/industry4-2.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM13xx</span><h3>燃气表</h3><p>对计量机构上的磁铁计数，把气体流量转成脉冲。</p><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/applications/industry4/electricity-meter"><div class="c-card__media c-media--case"><img src="/img/case/industry4-0.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57xx</span><h3>电表</h3><p>监测表内异常外部磁场，识别用强磁干扰计量的行为。</p><span class="c-card__more">查看案例</span></div></a></div>

<div class="c-cta"><div><h2 class="c-cta__title">需要选型建议、样品或技术支持？</h2><p>昆泰芯提供芯片选型、磁场仿真与方案设计支持，欢迎与我们的销售和技术团队联系。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
