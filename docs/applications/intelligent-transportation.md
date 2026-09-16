---
title: "智能交通"
description: "面向汽车角度与位置检测的车规级传感方案"
aside: false
pageClass: "c-page"
---

<nav class="c-crumbs"><a href="/msite/">首页</a><i>/</i><a href="/msite/applications/">市场应用</a><i>/</i><span>智能交通</span></nav>

<p class="c-kicker">市场应用</p>

# 智能交通

<p class="c-lead">面向汽车角度与位置检测的车规级传感方案</p>

<div class="c-stats"><div class="c-stat"><b>1</b><span>应用案例</span></div><div class="c-stat"><b>1</b><span>款推荐芯片</span></div></div>

车上的位置与角度检测点很密集：踏板与节气门开度、转向角、雨刮与门把手位置、水泵油泵与涡轮增压执行器的阀位、电机转子角度。这些点位共同的要求是全生命周期免维护、在振动与油污环境下不失效，因此几乎都走非接触磁方案，用磁铁跟随运动件、传感器固定在电路板上。

与消费和工业相比，汽车多出两层要求：一是认证与温度等级，器件要满足车规标准并覆盖发动机舱级别的温升；二是功能安全导向的诊断，系统需要知道传感器本身是否还在正常量程内，而不仅是拿到一个角度值。

## 领域需求

<p class="c-sec-lead">智能交通对磁传感器的共性要求。</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>车规与温度</h3><p>整车零部件需要符合车规认证要求，发动机舱与电机附近的器件温度等级要覆盖到更高上限。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>高转速低延时</h3><p>电机转子角度用于换相，采样延时直接转化为角度误差，高转速下这一项比分辨率更关键。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>故障可诊断</h3><p>磁铁脱落、气隙变化、通信误码都必须能被识别，系统要拿到诊断位而不是一个看似合理的错误角度。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>离轴安装</h3><p>轴端被占用时磁铁只能放在轴侧或做成环形，传感器需要支持离轴摆放并给出相应精度。</p></div></div><div class="c-feature"><span class="c-feature__no">05</span><div><h3>接口兼容</h3><p>既有电控单元的接口形式已固定，传感器需覆盖增量与绝对两类输出才能替换进现有平台。</p></div></div></div>

## 应用案例

<p class="c-sec-lead">电子节气门案例采用 KTH57 系列三轴霍尔传感器；车规级 KTH7801 符合 AEC-Q100，规格表所列应用领域包括水泵、油泵、智能车灯、转向传感器、涡轮增压、雨刮与门把手等。</p>

<div class="c-grid c-grid--4"><a class="c-card" href="/msite/applications/intelligent-transportation/e-throttle"><div class="c-card__media c-media--case"><img src="/msite/img/case/intelligent-transportation-0.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57xx</span><h3>电子节气门</h3><span class="c-card__more">查看案例</span></div></a></div>

## 推荐芯片一览

<div class="c-table c-table--links"><table><thead><tr><th>推荐芯片</th><th>对应产品</th><th>应用场景</th></tr></thead><tbody><tr><td class="c-mono">KTH57xx</td><td><a href="/msite/products/3d-hall/kth57">KTH57 系列 三轴线性霍尔传感器</a></td><td>电子节气门</td></tr></tbody></table></div>

## 需求与芯片对照

<div class="c-table c-table--links"><table><thead><tr><th>需求</th><th>推荐系列</th><th>依据</th></tr></thead><tbody><tr><td>踏板节气门开度</td><td><a href="/msite/products/3d-hall/kth57">KTH57 系列</a></td><td>检测范围 360°、16 bit，-40 ~ 125 ℃，I2C / SPI 输出。</td></tr><tr><td>车规绝对角度</td><td><a href="/msite/products/encoder/kth78">KTH78 系列</a></td><td>KTH7801 符合 AEC-Q100，-40 ~ 150 ℃，120,000 rpm。</td></tr><tr><td>高速换相角度</td><td><a href="/msite/products/encoder/kth78">KTH78 系列</a></td><td>刷新 1 MHz、每 1 μs 更新并做延时补偿，噪声低至 0.007°。</td></tr><tr><td>故障诊断能力</td><td><a href="/msite/products/encoder/kth78">KTH78 系列</a></td><td>磁场过低过高报警阈值可设，SPI 可选 CRC 校验。</td></tr><tr><td>接口替换兼容</td><td><a href="/msite/products/encoder/kth78">KTH78 系列</a></td><td>SPI / SSI / PWM，ABZ 4 ~ 4096 步/圈、UVW 1 ~ 8 对极。</td></tr><tr><td>离轴磁路布置</td><td><a href="/msite/products/encoder/kth78">KTH78 系列</a></td><td>全系支持在轴或离轴，离轴精度约 ±1°，可配磁仿真服务。</td></tr></tbody></table></div>

## 设计自检

<p class="c-sec-lead">方案定型前先回答这几个问题。</p>

<ul class="c-checklist"><li>这个点位的温度上限是多少？先按最热工况定器件温度等级，再谈精度，顺序反了会在夏季标定时返工。</li><li>需要绝对角度还是增量？上电即知位置的场合必须用绝对输出，否则要为回零动作预留机构与时间。</li><li>转速峰值下允许多大的角度误差？用转速乘以采样延时换算成角度，确认刷新率与延时补偿是否够用。</li><li>磁铁装在轴端还是轴侧？离轴方案的精度与磁场分布依赖磁路设计，建议在结构冻结前先做磁仿真核算。</li><li>系统需要哪些诊断信息？把磁场过低过高、通信校验这些诊断位在通信协议里预留好，不要等到台架阶段再补。</li></ul>

## 其他应用领域

<div class="c-grid c-grid--3"><a class="c-card" href="/msite/applications/consumer-electronics"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/app-consumer-electronics.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">7 个案例</span><h3>消费类电子</h3><p>为耳机、笔记本、手机与游戏设备提供位置与角度感知</p><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/msite/applications/intelligent-life"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/app-intelligent-life.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">11 个案例</span><h3>智能生活</h3><p>让门锁、水表、马桶与家电感知状态、响应操作</p><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/msite/applications/industry4"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/app-industry4.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">6 个案例</span><h3>工业4.0</h3><p>服务电表、断路器、闸机与电机转子位置检测</p><span class="c-card__more">查看案例</span></div></a></div>

<div class="c-cta"><div><h2 class="c-cta__title">需要选型建议、样品或技术支持？</h2><p>昆泰芯提供芯片选型、磁场仿真与方案设计支持，欢迎与我们的销售和技术团队联系。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/msite/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
