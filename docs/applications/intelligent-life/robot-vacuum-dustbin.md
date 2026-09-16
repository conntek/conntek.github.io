---
title: "扫地机器人-尘盒检测 · 智能生活应用"
description: "用模拟量判断尘盒是否装入以及装到什么程度。"
aside: false
pageClass: "c-page c-page--case"
---

<nav class="c-crumbs"><a href="/msite/">首页</a><i>/</i><a href="/msite/applications/">市场应用</a><i>/</i><a href="/msite/applications/intelligent-life">智能生活</a><i>/</i><span>扫地机器人-尘盒检测</span></nav>

<p class="c-kicker">智能生活</p>

# 扫地机器人-尘盒检测

<p class="c-lead">用模拟量判断尘盒是否装入以及装到什么程度。</p>

<div class="c-actions"><a class="c-btn c-btn--brand" href="/msite/products/switch/linear-hall">推荐芯片 KTH564X</a><a class="c-btn" href="/msite/contact">方案咨询</a></div>

## 场景说明

<div class="c-split c-split--overview"><div class="c-split__text">

扫地机的尘盒需要经常取出倾倒，机器要在尘盒没装好时拒绝启动，否则会把灰尘直接吹进机体。在尘盒上放一颗磁铁、机体内放传感器，就能隔着壳体判断装配状态。

与单纯的到位开关相比，输出模拟量的好处是能看到磁铁距离的连续变化：不仅知道装没装，还能分辨是完全卡到位还是只推进了一半，从而在软件里设定更合适的判定门限。

</div><div class="c-split__media c-split__media--frame c-split__media--case"><img src="/msite/img/case/intelligent-life-8.webp" alt="扫地机器人-尘盒检测" loading="lazy"></div></div>

## 检测需求

<p class="c-sec-lead">扫地机器人-尘盒检测对传感器的主要要求。</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>区分半到位</h3><p>开关量只能给出装没装，分不出推进一半的状态。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>隔壳检测</h3><p>尘盒仓多尘，传感器需留在机体内隔壳感应。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>门限可调</h3><p>装配分散性大，判定门限最好由软件决定。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>宽温工作</h3><p>机体内电机与风机会使环境温度上升。</p></div></div></div>

## 为什么选 KTH564X

<p class="c-sec-lead">零磁场输出 1/2 VCC，输出随磁通密度线性变化，多档灵敏度匹配不同检测范围</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>线性模拟输出</h3><p>输出随磁通密度线性变化，可反映磁铁距离的连续变化。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>零磁场中点</h3><p>无磁场时输出 1/2 VCC，便于识别磁铁完全移开的状态。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>多档灵敏度</h3><p>1.5 ~ 13 mV/Gs 多档，按装配行程选最大输出摆幅。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>宽温范围</h3><p>工作温度 -40 ~ 125 ℃，覆盖机体内温升。</p></div></div></div>

<div class="c-grid c-grid--2"><a class="c-card" href="/msite/products/switch/linear-hall"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/linear-hall.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH564 系列</span><h3>线性霍尔芯片</h3><p>零磁场输出 1/2 VCC，输出随磁通密度线性变化，多档灵敏度匹配不同检测范围</p><span class="c-card__more">查看产品</span></div></a></div>

## 设计注意点

<p class="c-sec-lead">通用工程建议，实际设计以产品手册与实测为准。</p>

<ul class="c-checklist"><li>先量出尘盒完全到位与完全取出两个状态的磁场值，按这段差值挑灵敏度档位。</li><li>模拟输出会随温度与电源变化，判定门限宜用相对量（如与空盒基准的差值）而非绝对电压。</li><li>尘盒仓附近的风机电机磁场是固定背景场，可在出厂标定时采基准并扣除。</li><li>尘盒是用户反复操作的部件，磁铁应埋入结构件内，避免脱落或吸附金属杂物。</li></ul>

## 相关案例

<div class="c-grid c-grid--4"><a class="c-card" href="/msite/applications/intelligent-life/robot-vacuum"><div class="c-card__media c-media--case"><img src="/msite/img/case/intelligent-life-3.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57xx</span><h3>扫地机器人-真空吸尘器</h3><p>检测拖布、滚刷等可换模块的安装位置与抬升行程。</p><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/msite/applications/intelligent-life/robot-vacuum-water-level"><div class="c-card__media c-media--case"><img src="/msite/img/case/intelligent-life-4.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM13xx</span><h3>扫地机-水位监测</h3><p>用带磁浮子判断清水箱与污水箱的水位是否到达阈值。</p><span class="c-card__more">查看案例</span></div></a></div>

<div class="c-cta"><div><h2 class="c-cta__title">需要选型建议、样品或技术支持？</h2><p>昆泰芯提供芯片选型、磁场仿真与方案设计支持，欢迎与我们的销售和技术团队联系。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/msite/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
