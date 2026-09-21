---
title: "水表 · 工业4.0应用"
description: "对表内指针或耦合磁铁计数，把机械水表的走字转成可远传的脉冲。"
aside: false
pageClass: "c-page c-page--case"
ld: "{\"@context\": \"https://schema.org\", \"@type\": \"TechArticle\", \"headline\": \"水表：工业4.0应用方案\", \"description\": \"对表内指针或耦合磁铁计数，把机械水表的走字转成可远传的脉冲。\", \"about\": \"水表\", \"author\": {\"@type\": \"Organization\", \"name\": \"昆泰芯微电子\", \"alternateName\": \"CONNTEK\", \"url\": \"https://conntek.github.io/\"}, \"publisher\": {\"@type\": \"Organization\", \"name\": \"昆泰芯微电子\", \"alternateName\": \"CONNTEK\", \"url\": \"https://conntek.github.io/\"}, \"url\": \"https://conntek.github.io/applications/industry4/water-meter\"}"
---

<nav class="c-crumbs"><a href="/">首页</a><i>/</i><a href="/applications/">市场应用</a><i>/</i><a href="/applications/industry4">工业4.0</a><i>/</i><span>水表</span></nav>

<p class="c-kicker">工业4.0</p>

# 水表

<p class="c-lead">对表内指针或耦合磁铁计数，把机械水表的走字转成可远传的脉冲。</p>

<div class="c-actions"><a class="c-btn c-btn--brand" href="/products/switch/ktm13">推荐芯片 KTM13xx</a><a class="c-btn" href="/contact">方案咨询</a></div>

## 场景说明

<div class="c-split c-split--overview"><div class="c-split__text">

机械水表里，水流推动叶轮旋转，经齿轮减速带动计数器。干式水表用磁耦合把叶轮的转动隔着密封隔板传到干燥的计数腔，计数机构不泡在水里。电子远传模块装在表盖一侧，用磁开关对计数器某一位指针或专设的磁铁计数，再通过无线或 M-Bus 等有线方式把读数上报。

水表常装在地下表井或户外管道井中，会遇到积水浸泡、表盖内凝露和冬季冻结，电子模块要整体密封并靠一次电池工作多年。叶轮在小流量时转得很慢，磁场在阈值附近缓慢变化，大流量时转速又高出很多。管网压力波动会带来短时倒转，强磁铁贴表还可能让磁耦合打滑、计数停走，这些都需要在计数环节识别出来。

</div><div class="c-split__media c-split__media--frame c-split__media--case"><img src="/img/case/industry4-water-meter.webp" alt="水表" loading="lazy"></div></div>

## 检测需求

<p class="c-sec-lead">水表对传感器的主要要求。</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>隔壳密封感应</h3><p>表井积水、凝露与冻结，传感器只能隔着表壳感应。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>宽转速范围</h3><p>小流量慢转与大流量快转都要计准。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>识别倒转</h3><p>管网压力波动引起倒转，回流不能计成用水。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>识别磁干扰</h3><p>强磁贴表会干扰磁耦合，需要留下事件记录。</p></div></div></div>

## 为什么选 KTM13xx

<p class="c-sec-lead">TMR 阻桥与 ASIC 单芯片集成，平行磁场感应，回差可小于 3 高斯</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>锁存型可选</h3><p><a class="c-xref" href="/products/switch/ktm13/ktm1331ta">KTM1331</a> 锁存型阈值正负对称，最低 ±5 高斯，适合旋转磁铁计数。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>三档频率</h3><p>50 Hz、1600 Hz、5000 Hz 三档，按指针最高转速选档。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>纳安级功耗</h3><p>50 Hz 档平均功耗 160 nA @ 3 V，电量留给远传通信。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>低温可用</h3><p>工作温度 -40 ~ 125 ℃，表井冬季低温下照常翻转。</p></div></div></div>

<div class="c-grid c-grid--2"><a class="c-card" href="/products/switch/ktm13"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm13.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM13 系列</span><h3>TMR 磁阻开关</h3><p>TMR 阻桥与 ASIC 单芯片集成，平行磁场感应，回差可小于 3 高斯</p><span class="c-card__more">查看产品</span></div></a></div>

## 设计注意点

<p class="c-sec-lead">通用工程建议，实际设计以产品手册与实测为准。</p>

<ul class="c-checklist"><li>按最大流量下被测指针或磁铁的最高转速选频率档，保证每转一圈能被采样多次，不能只按平均用水量选最低档。</li><li>两颗开关错开相位布置可同时得到计数与转向，相位差尽量接近 90°；靠近 0° 或 180° 时两路会同时处在翻转边沿，转向容易误判。</li><li>按表壳厚度与装配公差取最大间隙，核对正向磁场峰值仍高于 BOP、反向峰值仍超过 BRP；锁存型任一侧不够都会停止翻转、漏计脉冲。</li><li>始动流量附近的计量偏差主要来自叶轮与轴承摩擦，属于机械侧问题，靠提高传感器灵敏度补不回来。</li></ul>

## 相关案例

<div class="c-grid c-grid--4"><a class="c-card" href="/applications/industry4/gas-meter"><div class="c-card__media c-media--case"><img src="/img/case/industry4-2.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM13xx</span><h3>燃气表</h3><p>对计量机构上的磁铁计数，把气体流量转成脉冲。</p><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/applications/industry4/heat-meter"><div class="c-card__media c-media--case"><img src="/img/case/industry4-heat-meter.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM13xx</span><h3>热量表</h3><p>为机械式热量表的流量部分计数，与供回水温差一起积算用热量。</p><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/applications/industry4/mechanical-meter"><div class="c-card__media c-media--case"><img src="/img/case/industry4-5.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM13xx</span><h3>机械电表</h3><p>对机械字轮上的磁铁计数，把机械读数转成电子脉冲。</p><span class="c-card__more">查看案例</span></div></a></div>

<div class="c-cta"><div><h2 class="c-cta__title">需要选型建议、样品或技术支持？</h2><p>昆泰芯提供芯片选型、磁场仿真与方案设计支持，欢迎与我们的销售和技术团队联系。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
