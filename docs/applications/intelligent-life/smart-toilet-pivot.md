---
title: "智能马桶-枢轴检测 · 智能生活应用"
description: "检测盖板与坐圈在枢轴处的开合角度，用于落座与翻盖判断。"
aside: false
pageClass: "c-page c-page--case"
---

<nav class="c-crumbs"><a href="/msite/">首页</a><i>/</i><a href="/msite/applications/">市场应用</a><i>/</i><a href="/msite/applications/intelligent-life">智能生活</a><i>/</i><span>智能马桶-枢轴检测</span></nav>

<p class="c-kicker">智能生活</p>

# 智能马桶-枢轴检测

<p class="c-lead">检测盖板与坐圈在枢轴处的开合角度，用于落座与翻盖判断。</p>

<div class="c-actions"><a class="c-btn c-btn--brand" href="/msite/products/3d-hall/kth57">推荐芯片 KTH57xx</a><a class="c-btn" href="/msite/contact">方案咨询</a></div>

## 场景说明

<div class="c-split c-split--overview"><div class="c-split__text">

智能马桶需要知道盖板和坐圈当前处于什么角度，才能控制自动翻盖、限位缓降，并与落座感应、冲洗动作联锁。在枢轴内放一颗磁铁，机身侧放芯片，就能读出开合角度。

枢轴位置紧邻水路和清洁区，长期处于潮湿环境，还会被反复擦洗。把检测做成隔空的磁式方案，枢轴不需要引出电线，也不必为传感器单独做密封。

</div><div class="c-split__media c-split__media--frame c-split__media--case"><img src="/msite/img/case/intelligent-life-6.webp" alt="智能马桶-枢轴检测" loading="lazy"></div></div>

## 检测需求

<p class="c-sec-lead">智能马桶-枢轴检测对传感器的主要要求。</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>潮湿环境</h3><p>枢轴长期受潮并被反复擦洗，触点式方案寿命有限。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>角度连续</h3><p>缓降与限位需要连续角度，不只是全开全关。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>空间紧凑</h3><p>枢轴内径有限，磁铁与芯片都只能做小。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>无引线转动</h3><p>转动部位走线易疲劳断裂，最好不引线。</p></div></div></div>

## 为什么选 KTH57xx

<p class="c-sec-lead">测量 X、Y、Z 三轴磁场，I2C / SPI 可选，工作模式在线配置，兼顾性能与功耗</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>隔空角度检测</h3><p>磁铁随枢轴转动，芯片留在机身侧，转动件无需引线。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>在轴离轴均可</h3><p>枢轴放不下在轴磁铁时可改离轴，机械上更好排。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>360° 范围</h3><p>检测范围 360°，盖板全关到全开只用其中一段。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>16 bit 输出</h3><p>16 bit 分辨率，九十多度行程也分得出缓降位置。</p></div></div></div>

<div class="c-grid c-grid--2"><a class="c-card" href="/msite/products/3d-hall/kth57"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth57.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57 系列</span><h3>三轴线性霍尔传感器</h3><p>测量 X、Y、Z 三轴磁场，I2C / SPI 可选，工作模式在线配置，兼顾性能与功耗</p><span class="c-card__more">查看产品</span></div></a></div>

## 设计注意点

<p class="c-sec-lead">通用工程建议，实际设计以产品手册与实测为准。</p>

<ul class="c-checklist"><li>盖板只转九十多度，磁铁装配角度应让这一段落在同一个解算分支内。</li><li>盖板与坐圈两路检测的磁铁如果靠得近，要核对互相串扰并适当错开轴向位置。</li><li>枢轴的机械间隙会让磁铁位置在转动中轻微摆动，选磁铁与气隙时要留出这部分余量。</li><li>缓降阻尼件老化后角速度会变，软件判定不要依赖固定的角度变化速率。</li></ul>

## 相关案例

<div class="c-grid c-grid--4"><a class="c-card" href="/msite/applications/intelligent-life/smart-toilet-knob"><div class="c-card__media c-media--case"><img src="/msite/img/case/intelligent-life-9.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57xx</span><h3>智能马桶-旋钮</h3><p>检测侧面板旋钮的角度，用于水温、水压与冲洗位置调节。</p><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/msite/applications/intelligent-life/smart-toilet-water-level"><div class="c-card__media c-media--case"><img src="/msite/img/case/intelligent-life-10.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM13xx</span><h3>智能马桶-水位监测</h3><p>用带磁浮子判断水箱液位是否到达上下限阈值。</p><span class="c-card__more">查看案例</span></div></a></div>

<div class="c-cta"><div><h2 class="c-cta__title">需要选型建议、样品或技术支持？</h2><p>昆泰芯提供芯片选型、磁场仿真与方案设计支持，欢迎与我们的销售和技术团队联系。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/msite/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
