---
title: "洗衣机 · 消费类电子应用"
description: "检测程序旋钮的旋转角度与门盖的开合位置。"
aside: false
pageClass: "c-page c-page--case"
ld: "{\"@context\": \"https://schema.org\", \"@type\": \"TechArticle\", \"headline\": \"洗衣机：消费类电子应用方案\", \"description\": \"检测程序旋钮的旋转角度与门盖的开合位置。\", \"about\": \"洗衣机\", \"author\": {\"@type\": \"Organization\", \"name\": \"昆泰芯微电子\", \"alternateName\": \"CONNTEK\", \"url\": \"https://conntek.github.io/\"}, \"publisher\": {\"@type\": \"Organization\", \"name\": \"昆泰芯微电子\", \"alternateName\": \"CONNTEK\", \"url\": \"https://conntek.github.io/\"}, \"url\": \"https://conntek.github.io/applications/consumer-electronics/washing-machine\"}"
---

<nav class="c-crumbs"><a href="/">首页</a><i>/</i><a href="/applications/">市场应用</a><i>/</i><a href="/applications/consumer-electronics">消费类电子</a><i>/</i><span>洗衣机</span></nav>

<p class="c-kicker">消费类电子</p>

# 洗衣机

<p class="c-lead">检测程序旋钮的旋转角度与门盖的开合位置。</p>

<div class="c-actions"><a class="c-btn c-btn--brand" href="/products/3d-hall/kth57">推荐芯片 KTH57xx</a><a class="c-btn" href="/contact">方案咨询</a></div>

## 场景说明

<div class="c-split c-split--overview"><div class="c-split__text">

洗衣机面板上的程序旋钮要区分十几个洗涤模式，门盖或上盖则需要判断是否关到位才允许启动。旋钮轴上或门盖边放磁铁，传感器读出磁场方向的变化，就能同时得到连续的旋转角度和开合状态。

洗衣机内部长期处于潮湿、有洗涤剂蒸汽的环境，面板背后还有溅水风险。磁式检测可以把磁铁做在面板外侧的旋钮里、芯片放在面板内侧，两者之间不开孔，从结构上避免进水进汽。

</div><div class="c-split__media c-split__media--frame c-split__media--case"><img src="/img/case/consumer-electronics-3.webp" alt="洗衣机" loading="lazy"></div></div>

## 检测需求

<p class="c-sec-lead">洗衣机对传感器的主要要求。</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>隔面板检测</h3><p>面板不能开孔，磁铁与芯片分居两侧。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>抗潮湿</h3><p>潮气与洗涤剂蒸汽会腐蚀触点式开关与电位器。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>档位要稳</h3><p>同一档位反复旋到时读数必须一致，不能跳档。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>整机温升</h3><p>烘干机型面板附近温度会明显升高。</p></div></div></div>

## 为什么选 KTH57xx

<p class="c-sec-lead">测量 X、Y、Z 三轴磁场，I2C / SPI 可选，工作模式在线配置，兼顾性能与功耗</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>360° 角度检测</h3><p>检测范围 360°，一圈十几个洗涤模式都能划开。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>隔面板工作</h3><p>磁铁随旋钮在面板外转动，面板上不必留轴孔。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>宽温范围</h3><p>面板温升可达几十度，工作温度上限 125 ℃ 有余量。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>16 bit 输出</h3><p>16 bit 分辨率，相邻档位之间留得出判定余量。</p></div></div></div>

<div class="c-grid c-grid--2"><a class="c-card" href="/products/3d-hall/kth57"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth57.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57 系列</span><h3>三轴线性霍尔传感器</h3><p>测量 X、Y、Z 三轴磁场，I2C / SPI 可选，工作模式在线配置，兼顾性能与功耗</p><span class="c-card__more">查看产品</span></div></a></div>

## 设计注意点

<p class="c-sec-lead">通用工程建议，实际设计以产品手册与实测为准。</p>

<ul class="c-checklist"><li>旋钮磁铁一般用径向充磁的环形或圆片磁铁，安装同心度直接决定角度线性度。</li><li>档位边界应避开角度解算误差最大的位置，并在软件里加迟滞，防止停在边界时来回跳档。</li><li>门盖检测只需要判断到位与否时，可按位置阈值处理，但阈值要按门盖最大装配间隙来定。</li><li>洗衣机电机与变频驱动是强磁与强电磁干扰源，传感器位置与信号线需要与之拉开距离。</li></ul>

## 相关案例

<div class="c-grid c-grid--4"><a class="c-card" href="/applications/consumer-electronics/smart-watch"><div class="c-card__media c-media--case"><img src="/img/case/consumer-electronics-6.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57xx</span><h3>智能手表</h3><p>检测旋转表冠的转动角度与方向，用于翻页与调节。</p><span class="c-card__more">查看案例</span></div></a></div>

<div class="c-cta"><div><h2 class="c-cta__title">需要选型建议、样品或技术支持？</h2><p>昆泰芯提供芯片选型、磁场仿真与方案设计支持，欢迎与我们的销售和技术团队联系。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
