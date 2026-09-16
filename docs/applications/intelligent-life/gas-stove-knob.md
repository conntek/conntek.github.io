---
title: "燃气灶-旋钮 · 智能生活应用"
description: "检测火力旋钮的转动角度，面板不开孔即可读出档位。"
aside: false
pageClass: "c-page c-page--case"
---

<nav class="c-crumbs"><a href="/msite/">首页</a><i>/</i><a href="/msite/applications/">市场应用</a><i>/</i><a href="/msite/applications/intelligent-life">智能生活</a><i>/</i><span>燃气灶-旋钮</span></nav>

<p class="c-kicker">智能生活</p>

# 燃气灶-旋钮

<p class="c-lead">检测火力旋钮的转动角度，面板不开孔即可读出档位。</p>

<div class="c-actions"><a class="c-btn c-btn--brand" href="/msite/products/3d-hall/kth57">推荐芯片 KTH57xx</a><a class="c-btn" href="/msite/contact">方案咨询</a></div>

## 场景说明

<div class="c-split c-split--overview"><div class="c-split__text">

燃气灶的火力旋钮要把使用者的旋转动作转成火力档位。旋钮里放一颗磁铁，面板内侧放芯片，转动时磁场方向跟着变化，主控就能读出当前角度并对应到火力等级。

灶台面常年有油污、汤汁和清洁剂，传统旋钮的机械轴贯穿面板，是最容易渗漏和卡滞的地方。磁-电分离的做法让面板保持完整，旋钮可整体拆下清洗，油污不再进入电路腔。

</div><div class="c-split__media c-split__media--frame c-split__media--case"><img src="/msite/img/case/intelligent-life-2.webp" alt="燃气灶-旋钮" loading="lazy"></div></div>

## 检测需求

<p class="c-sec-lead">燃气灶-旋钮对传感器的主要要求。</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>面板不开孔</h3><p>灶台面要能整面擦洗，机械贯穿是渗漏路径。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>耐油污</h3><p>油污与清洁剂会腐蚀触点、卡死机械编码器。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>耐温</h3><p>灶台面板温度高于普通家电面板。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>档位准确</h3><p>火力档位读错直接影响燃烧控制与安全联锁。</p></div></div></div>

## 为什么选 KTH57xx

<p class="c-sec-lead">测量 X、Y、Z 三轴磁场，I2C / SPI 可选，工作模式在线配置，兼顾性能与功耗</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>隔空角度检测</h3><p>磁铁与芯片分居面板两侧，面板可做成完整无孔。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>360° 范围</h3><p>检测范围 360°，覆盖旋钮全部行程与档位划分。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>宽温范围</h3><p>工作温度 -40 ~ 125 ℃，适应灶面附近温升。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>温度补偿</h3><p>内部温度补偿算法减小灵敏度温漂，档位随温度更稳。</p></div></div></div>

<div class="c-grid c-grid--2"><a class="c-card" href="/msite/products/3d-hall/kth57"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/kth57.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57 系列</span><h3>三轴线性霍尔传感器</h3><p>测量 X、Y、Z 三轴磁场，I2C / SPI 可选，工作模式在线配置，兼顾性能与功耗</p><span class="c-card__more">查看产品</span></div></a></div>

## 设计注意点

<p class="c-sec-lead">通用工程建议，实际设计以产品手册与实测为准。</p>

<ul class="c-checklist"><li>旋钮可拆卸时，重新装回的角度与位置都会变，需要有机械定位特征保证可重复安装。</li><li>面板玻璃厚度决定了最小气隙，磁铁强度应按最厚面板加最大公差来选。</li><li>灶具的点火高压与电磁阀会产生瞬时干扰，信号线应远离点火针走线。</li><li>长期高温会削弱磁铁剩磁，选磁铁材料时要看其允许工作温度而不只看初始磁力。</li></ul>

## 相关案例

<div class="c-grid c-grid--4"><a class="c-card" href="/msite/applications/intelligent-life/gas-stove-temperature"><div class="c-card__media c-media--case"><img src="/msite/img/case/intelligent-life-7.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTAx333</span><h3>燃气灶-温度检测</h3><p>放大热电偶等温度传感元件输出的微弱电压信号。</p><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/msite/applications/intelligent-life/coffee-machine"><div class="c-card__media c-media--case"><img src="/msite/img/case/intelligent-life-0.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57xx</span><h3>咖啡机</h3><p>检测操作旋钮的转动角度与水箱、粉仓的安装到位状态。</p><span class="c-card__more">查看案例</span></div></a></div>

<div class="c-cta"><div><h2 class="c-cta__title">需要选型建议、样品或技术支持？</h2><p>昆泰芯提供芯片选型、磁场仿真与方案设计支持，欢迎与我们的销售和技术团队联系。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/msite/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
