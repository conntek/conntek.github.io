---
title: "闸机 · 工业4.0应用"
description: "检测摆翼或门翼的开合角度，用于限位与防夹判断。"
aside: false
pageClass: "c-page c-page--case"
ld: "{\"@context\": \"https://schema.org\", \"@type\": \"TechArticle\", \"headline\": \"闸机：工业4.0应用方案\", \"description\": \"检测摆翼或门翼的开合角度，用于限位与防夹判断。\", \"about\": \"闸机\", \"author\": {\"@type\": \"Organization\", \"name\": \"昆泰芯微电子\", \"alternateName\": \"CONNTEK\", \"url\": \"https://conntek.github.io/\"}, \"publisher\": {\"@type\": \"Organization\", \"name\": \"昆泰芯微电子\", \"alternateName\": \"CONNTEK\", \"url\": \"https://conntek.github.io/\"}, \"url\": \"https://conntek.github.io/applications/industry4/turnstile\"}"
---

<nav class="c-crumbs"><a href="/">首页</a><i>/</i><a href="/applications/">市场应用</a><i>/</i><a href="/applications/industry4">工业4.0</a><i>/</i><span>闸机</span></nav>

<p class="c-kicker">工业4.0</p>

# 闸机

<p class="c-lead">检测摆翼或门翼的开合角度，用于限位与防夹判断。</p>

<div class="c-actions"><a class="c-btn c-btn--brand" href="/products/3d-hall/kth57">推荐芯片 KTH57xx</a><a class="c-btn" href="/contact">方案咨询</a></div>

## 场景说明

<div class="c-split c-split--overview"><div class="c-split__text">

摆闸、翼闸的门翼由电机驱动开合，控制器需要实时知道门翼当前转到哪个角度，才能做减速、限位、以及被人挡住时的防夹回退。门翼转轴上放磁铁、机箱内放芯片，就能连续读出角度。

闸机装在地铁、写字楼出入口，每天动作上万次，还要面对灰尘与偶尔的强行推挤。非接触的角度检测没有机械磨损，也不怕被强推时的过行程损坏。

</div><div class="c-split__media c-split__media--frame c-split__media--case"><img src="/img/case/industry4-4.webp" alt="闸机" loading="lazy"></div></div>

## 检测需求

<p class="c-sec-lead">闸机对传感器的主要要求。</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>高频动作</h3><p>每天上万次开合，接触式检测寿命不够。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>角度连续</h3><p>减速与防夹需要连续角度和角速度信息。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>抗强推</h3><p>被强行推动时检测结构不能损坏。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>抗电机干扰</h3><p>驱动电机就在旁边，磁与电磁干扰都很强。</p></div></div></div>

## 为什么选 KTH57xx

<p class="c-sec-lead">测量 X、Y、Z 三轴磁场，I2C / SPI 可选，工作模式在线配置，兼顾性能与功耗</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>隔空角度检测</h3><p>磁铁随转轴转动，芯片固定在机箱内，无机械连接。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>360° 范围</h3><p>角度量程 360°，门翼往复的全部行程都能读到。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>千赫兹刷新</h3><p>工作频率 1000 Hz，快速开合过程能连续采到。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>宽磁场范围</h3><p>磁场量程 XY ±130 mT、Z ±80 mT，电机杂散场挤不满。</p></div></div></div>

<div class="c-grid c-grid--2"><a class="c-card" href="/products/3d-hall/kth57"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth57.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57 系列</span><h3>三轴线性霍尔传感器</h3><p>测量 X、Y、Z 三轴磁场，I2C / SPI 可选，工作模式在线配置，兼顾性能与功耗</p><span class="c-card__more">查看产品</span></div></a></div>

## 设计注意点

<p class="c-sec-lead">通用工程建议，实际设计以产品手册与实测为准。</p>

<ul class="c-checklist"><li>驱动电机的定子磁场会叠加到检测点上，磁铁与芯片应尽量远离电机或加导磁隔离。</li><li>防夹判断依赖角速度与角加速度，采样率要能分辨出被挡住时的减速过程。</li><li>门翼行程不到一圈，机械零位与角度原点应在装配时对齐一次。</li><li>断电情况下门翼需可手动推开，机械结构变化后要复核磁铁位置是否仍在可测范围。</li></ul>

## 相关案例

<div class="c-grid c-grid--4"><a class="c-card" href="/applications/industry4/knob-control"><div class="c-card__media c-media--case"><img src="/img/case/industry4-3.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57xx</span><h3>旋钮操控</h3><p>工业设备面板旋钮的角度检测，面板可做成全封闭。</p><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/applications/industry4/circuit-breaker"><div class="c-card__media c-media--case"><img src="/img/case/industry4-1.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH16xx</span><h3>断路器</h3><p>检测手柄或触头机构的分合闸位置，输出状态信号。</p><span class="c-card__more">查看案例</span></div></a></div>

<div class="c-cta"><div><h2 class="c-cta__title">需要选型建议、样品或技术支持？</h2><p>昆泰芯提供芯片选型、磁场仿真与方案设计支持，欢迎与我们的销售和技术团队联系。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
