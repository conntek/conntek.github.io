---
title: "断路器 · 工业4.0应用"
description: "检测手柄或触头机构的分合闸位置，输出状态信号。"
aside: false
pageClass: "c-page c-page--case"
ld: "{\"@context\": \"https://schema.org\", \"@type\": \"TechArticle\", \"headline\": \"断路器：工业4.0应用方案\", \"description\": \"检测手柄或触头机构的分合闸位置，输出状态信号。\", \"about\": \"断路器\", \"author\": {\"@type\": \"Organization\", \"name\": \"昆泰芯微电子\", \"alternateName\": \"CONNTEK\", \"url\": \"https://conntek.grosso.link/\"}, \"publisher\": {\"@type\": \"Organization\", \"name\": \"昆泰芯微电子\", \"alternateName\": \"CONNTEK\", \"url\": \"https://conntek.grosso.link/\"}, \"url\": \"https://conntek.grosso.link/applications/industry4/circuit-breaker\"}"
---

<nav class="c-crumbs"><a href="/">首页</a><i>/</i><a href="/applications/">市场应用</a><i>/</i><a href="/applications/industry4">工业4.0</a><i>/</i><span>断路器</span></nav>

<p class="c-kicker">工业4.0</p>

# 断路器

<p class="c-lead">检测手柄或触头机构的分合闸位置，输出状态信号。</p>

<div class="c-actions"><a class="c-btn c-btn--brand" href="/products/switch/kth16">推荐芯片 KTH16xx</a><a class="c-btn" href="/contact">方案咨询</a></div>

## 场景说明

<div class="c-split c-split--overview"><div class="c-split__text">

配电箱里的断路器需要把分合闸状态上报给监控系统。做法是在操作机构的活动件上放一颗磁铁，机构旁固定一颗磁开关，机构翻到合闸位置时磁铁靠近、开关翻转，状态就以数字电平输出。

断路器内部是强电环境，机构动作时伴随电弧与冲击，触点式辅助开关既怕污染又有机械寿命限制。磁式方案不接触、不引入新的机械磨损点，也便于把弱电部分与主回路隔开。

</div><div class="c-split__media c-split__media--frame c-split__media--case"><img src="/img/case/industry4-1.webp" alt="断路器" loading="lazy"></div></div>

## 检测需求

<p class="c-sec-lead">断路器对传感器的主要要求。</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>强电环境</h3><p>主回路电流与电弧会带来强干扰和温升。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>状态要确定</h3><p>分合闸是二值状态，输出必须干净无抖动。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>低功耗</h3><p>辅助回路取电有限，状态检测应常驻低功耗。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>体积小</h3><p>模数化壳体内部空间非常紧张。</p></div></div></div>

## 为什么选 KTH16xx

<p class="c-sec-lead">CMOS 工艺集成霍尔元件，1 μA 超低功耗，温度补偿优良，覆盖全极、单极与锁存型</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>微功耗</h3><p>系列功耗低至 1 μA，可长期常驻检测状态。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>锁存型可选</h3><p>系列含锁存型（<a class="c-xref" href="/products/switch/kth16/kth1631fu">KTH1631</a> / <a class="c-xref" href="/products/switch/kth16/kth1731pu">KTH1731</a>），适合两位置状态保持。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>温度补偿</h3><p>具备温度补偿，部分型号工作温度达 -40 ~ 125 ℃。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>小封装</h3><p>SOT-23-3L、TO-92S、DFN/FBP 1*1-4L 等封装可选。</p></div></div></div>

<div class="c-grid c-grid--2"><a class="c-card" href="/products/switch/kth16"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth16.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH13/16/17 系列</span><h3>微功耗 1D 霍尔开关</h3><p>CMOS 工艺集成霍尔元件，1 μA 超低功耗，温度补偿优良，覆盖全极、单极与锁存型</p><span class="c-card__more">查看产品</span></div></a></div>

## 设计注意点

<p class="c-sec-lead">通用工程建议，实际设计以产品手册与实测为准。</p>

<ul class="c-checklist"><li>锁存型需要正反两个磁极分别触发，机构两个极限位置要能各自提供足够的反向磁场。</li><li>主回路大电流本身会产生磁场，检测点布局应与母排拉开距离或调整敏感方向。</li><li>断路器内部温升明显，型号的工作温度上限要按最热工况选，而不是按室温。</li><li>机构动作瞬间存在振动与过冲，软件侧应加去抖，避免把过冲当成一次状态翻转。</li></ul>

## 相关案例

<div class="c-grid c-grid--4"><a class="c-card" href="/applications/industry4/electricity-meter"><div class="c-card__media c-media--case"><img src="/img/case/industry4-0.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57xx</span><h3>电表</h3><p>监测表内异常外部磁场，识别用强磁干扰计量的行为。</p><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/applications/industry4/turnstile"><div class="c-card__media c-media--case"><img src="/img/case/industry4-4.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57xx</span><h3>闸机</h3><p>检测摆翼或门翼的开合角度，用于限位与防夹判断。</p><span class="c-card__more">查看案例</span></div></a></div>

<div class="c-cta"><div><h2 class="c-cta__title">需要选型建议、样品或技术支持？</h2><p>昆泰芯提供芯片选型、磁场仿真与方案设计支持，欢迎与我们的销售和技术团队联系。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
