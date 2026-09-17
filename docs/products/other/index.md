---
title: "其他芯片"
description: "面向传感器信号放大的零温漂高精度运放"
aside: false
pageClass: "c-page"
---

<nav class="c-crumbs"><a href="/msite/">首页</a><i>/</i><a href="/msite/products/">产品中心</a><i>/</i><span>其他芯片</span></nav>

<p class="c-kicker">产品中心</p>

# 其他芯片

<p class="c-lead">面向传感器信号放大的零温漂高精度运放</p>

<div class="c-stats"><div class="c-stat"><b>1</b><span>产品系列</span></div><div class="c-stat"><b>2</b><span>份技术文档</span></div><div class="c-stat"><b>0</b><span>个产品视频</span></div></div>

其他芯片收录信号链器件。桥式磁传感器的输出常常只有几十到几百微伏，直接送进 ADC 会被放大器自身的失调和温漂淹没——这一级运放的失调电压与失调温漂，直接决定整条链路的零点稳定性。

<a class="c-xref" href="/msite/products/other/ktax33">KTAx333</a> 系列是自校准 CMOS 运算放大器，失调电压 2 μV（典型值）、10 μV（最大值），失调温漂 0.02 μV/℃，轨到轨输入与输出，静态功耗 30 μA，供电 1.8 ~ 5.5 V，工作温度 -40 ~ 125 ℃。

## 怎么选

<p class="c-sec-lead">按下面几步缩小范围。</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>先看失调与温漂</h3><p>直流微弱信号放大先看这两项：<a class="c-xref" href="/msite/products/other/ktax33">KTAx333</a> 失调 2 μV（典型值）、10 μV（最大值），温漂 0.02 μV/℃。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>核对带宽与摆率</h3><p><a class="c-xref" href="/msite/products/other/ktax33">KTAx333</a> 增益带宽积 350 kHz、压摆率 0.16 V/μs，超出此范围的高速信号不适用。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>核对噪声与偏置</h3><p>电压噪声 1.1 μVpp（0.1 ~ 10 Hz），输入偏置电流 ±100 pA，输入失调电流 ±120 pA。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>定通道数与封装</h3><p>单通道选 KTA333-ST5（SOT23-5）；双通道选 KTA2333-MP8 / KTA2333-SP8。</p></div></div></div>

## 系列对照

<div class="c-table c-table--links"><table><thead><tr><th>型号</th><th>通道数</th><th>封装</th><th>失调电压</th><th>静态功耗</th></tr></thead><tbody><tr><td>KTA333-ST5</td><td>单通道</td><td>SOT23-5</td><td>2 μV（典型值）</td><td>30 μA</td></tr><tr><td>KTA2333-MP8</td><td>双通道</td><td>MSOP-8</td><td>2 μV（典型值）</td><td>30 μA</td></tr><tr><td>KTA2333-SP8</td><td>双通道</td><td>SOP-8</td><td>2 μV（典型值）</td><td>30 μA</td></tr></tbody></table></div>

## 产品系列

<p class="c-sec-lead"><a class="c-xref" href="/msite/products/other/ktax33">KTAx333</a> 系列自校准 CMOS 运放，失调电压 2 μV（典型值）、轨到轨输入 / 输出，提供单通道与双通道型号，适合各类传感器信号放大级。</p>

<div class="c-rows"><a class="c-row" href="/msite/products/other/ktax33"><div class="c-row__media c-media--icon"><img src="/msite/img/icons-web/ktax33.webp" alt="" loading="lazy"></div><div class="c-row__body"><span class="c-card__kicker">KTAx333 系列</span><h3>零温漂高精度运放</h3><p>自校准 CMOS 运放，失调电压 2 μV（典型值），轨到轨输入 / 输出</p><div class="c-minispecs"><span><b>2 μV（典型值）</b>失调电压</span><span><b>1.8 ~ 5.5 V</b>电压</span><span><b>30 μA</b>功耗</span><span><b>轨到轨输入 / 输出</b>接口</span></div><span class="c-card__more">查看详情</span></div></a></div>

## 应用案例

<p class="c-sec-lead">采用其他芯片的终端产品。</p>

<div class="c-grid c-grid--4"><a class="c-card" href="/msite/applications/intelligent-life/solar-converter"><div class="c-card__media c-media--case"><img src="/msite/img/case/intelligent-life-5.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTAx333</span><h3>太阳能光电转换器</h3></div></a><a class="c-card" href="/msite/applications/intelligent-life/gas-stove-temperature"><div class="c-card__media c-media--case"><img src="/msite/img/case/intelligent-life-7.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTAx333</span><h3>燃气灶-温度检测</h3></div></a></div>

## 常见问题

::: details 为什么适合驱动 ADC

<a class="c-xref" href="/msite/products/other/ktax33">KTAx333</a> 不存在传统互补输入级带来的交越问题，驱动 ADC 时不会降低微分线性；CMRR 120 dB，开环增益 120 dB，PSRR 1 μV/V。

:::

::: details 供电与温度范围是多少

工作电压 1.8 ~ 5.5 V，静态功耗 30 μA，工作温度 -40 ~ 125 ℃，轨到轨输入与输出。

:::

::: details 典型用在什么地方

各类传感器信号的放大级，产品页列出的场景包括太阳能光电转换器与燃气灶温度检测。

:::

## 其他产品线

<div class="c-grid c-grid--4"><a class="c-card" href="/msite/products/3d-hall/"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/cat-3d-hall.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">2 个系列</span><h3>3D霍尔芯片</h3><p>感知 X、Y、Z 三轴磁场，用于角度与位移检测</p><span class="c-card__more">浏览产品线</span></div></a><a class="c-card" href="/msite/products/encoder/"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/cat-encoder.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">7 个系列</span><h3>编码器芯片</h3><p>霍尔、AMR、TMR 与光学路线的高速高精度编码器芯片</p><span class="c-card__more">浏览产品线</span></div></a><a class="c-card" href="/msite/products/switch/"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/cat-switch.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">8 个系列</span><h3>开关芯片</h3><p>霍尔、TMR、AMR 开关与线性霍尔，从微功耗到车规高压</p><span class="c-card__more">浏览产品线</span></div></a><a class="c-card" href="/msite/products/knob/"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/cat-knob.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">1 个系列</span><h3>旋钮系列</h3><p>磁-电分离的磁旋钮，隔空检测角度，防水防尘 IP67</p><span class="c-card__more">浏览产品线</span></div></a></div>

<div class="c-cta"><div><h2 class="c-cta__title">需要选型建议、样品或技术支持？</h2><p>昆泰芯提供芯片选型、磁场仿真与方案设计支持，欢迎与我们的销售和技术团队联系。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/msite/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
