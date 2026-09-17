---
title: "热量表 · 工业4.0应用"
description: "为机械式热量表的流量部分计数，与供回水温差一起积算用热量。"
aside: false
pageClass: "c-page c-page--case"
---

<nav class="c-crumbs"><a href="/msite/">首页</a><i>/</i><a href="/msite/applications/">市场应用</a><i>/</i><a href="/msite/applications/industry4">工业4.0</a><i>/</i><span>热量表</span></nav>

<p class="c-kicker">工业4.0</p>

# 热量表

<p class="c-lead">为机械式热量表的流量部分计数，与供回水温差一起积算用热量。</p>

<div class="c-actions"><a class="c-btn c-btn--brand" href="/msite/products/switch/ktm13">推荐芯片 KTM13xx</a><a class="c-btn" href="/msite/contact">方案咨询</a></div>

## 场景说明

<div class="c-split c-split--overview"><div class="c-split__text">

热量表由流量传感器、一对温度传感器和积算仪组成：两支温度传感器分别装在供水管与回水管上测温差，流量传感器测流过的热水体积，积算仪把体积、温差和水的热系数相乘并累加，得到用热量。机械式热量表的流量部分是叶轮，转动经磁耦合传到积算仪一侧，由磁开关计数；超声式热量表没有转动部件，不需要这一环。

流量部分串在供暖管道上，热水温度高，分体式积算仪可与管段分开安装，但表体整个采暖季都处在温热环境里；用于制冷计量时表面又会凝露。整表靠一次锂电池工作多个采暖季，读数多经 M-Bus 或无线方式集中抄读。流量计数一旦漏计，积算出的热量直接偏低，所以计数要在高温和电池电压下降时都保持可靠。

</div><div class="c-split__media c-split__media--frame c-split__media--case"><img src="/msite/img/case/industry4-heat-meter.webp" alt="热量表" loading="lazy"></div></div>

## 检测需求

<p class="c-sec-lead">热量表对传感器的主要要求。</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>耐受温升</h3><p>表体靠近热水管段，整个采暖季处在温热环境。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>电池末期可靠</h3><p>锂电池放电后期电压下降，计数不能中断。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>慢转不漏计</h3><p>小流量时叶轮慢转，磁场在阈值附近缓慢变化。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>冷热两用</h3><p>制冷计量时会凝露，感应不能受潮气影响。</p></div></div></div>

## 为什么选 KTM13xx

<p class="c-sec-lead">TMR 阻桥与 ASIC 单芯片集成，平行磁场感应，回差可小于 3 高斯</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>宽温上限</h3><p>工作温度 -40 ~ 125 ℃，热水管段带来的温升在范围内。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>宽供电范围</h3><p>1.8 ~ 5.5 V 供电，电池电压下降后仍在工作范围内。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>小回差</h3><p>回差可小于 3 高斯，叶轮慢转时翻转点仍确定。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>纳安级功耗</h3><p>平均功耗低至 160 nA @ 3 V，计数环节占用电量很小。</p></div></div></div>

<div class="c-grid c-grid--2"><a class="c-card" href="/msite/products/switch/ktm13"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/ktm13.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM13 系列</span><h3>TMR 磁阻开关</h3><p>TMR 阻桥与 ASIC 单芯片集成，平行磁场感应，回差可小于 3 高斯</p><span class="c-card__more">查看产品</span></div></a></div>

## 设计注意点

<p class="c-sec-lead">通用工程建议，实际设计以产品手册与实测为准。</p>

<ul class="c-checklist"><li>磁铁剩磁随温度升高而下降，BOP 档位应按最高介质温度下芯片处的磁场来选，而不是按常温值。</li><li>每个脉冲对应的体积由叶轮几何决定，需要实流标定；更换磁铁、调整传感器位置后都要重新标定。</li><li>流量计数与温差采样要在时间上对齐，流量变化快时温度采样间隔过长，积算热量的偏差会变大。</li><li>冷热两用的表内会凝露，传感器所在电路板应做防潮涂覆，磁铁与芯片之间不留可积水的腔体。</li></ul>

## 相关案例

<div class="c-grid c-grid--4"><a class="c-card" href="/msite/applications/industry4/water-meter"><div class="c-card__media c-media--case"><img src="/msite/img/case/industry4-water-meter.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM13xx</span><h3>水表</h3><p>对表内指针或耦合磁铁计数，把机械水表的走字转成可远传的脉冲。</p><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/msite/applications/industry4/gas-meter"><div class="c-card__media c-media--case"><img src="/msite/img/case/industry4-2.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM13xx</span><h3>燃气表</h3><p>对计量机构上的磁铁计数，把气体流量转成脉冲。</p><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/msite/applications/industry4/electricity-meter"><div class="c-card__media c-media--case"><img src="/msite/img/case/industry4-0.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57xx</span><h3>电表</h3><p>监测表内异常外部磁场，识别用强磁干扰计量的行为。</p><span class="c-card__more">查看案例</span></div></a></div>

<div class="c-cta"><div><h2 class="c-cta__title">需要选型建议、样品或技术支持？</h2><p>昆泰芯提供芯片选型、磁场仿真与方案设计支持，欢迎与我们的销售和技术团队联系。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/msite/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
