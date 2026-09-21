---
title: "电梯 · 工业4.0应用"
description: "测量曳引机与门机电机的转子角度，为低速平层和开关门的速度闭环提供反馈。"
aside: false
pageClass: "c-page c-page--case"
ld: "{\"@context\": \"https://schema.org\", \"@type\": \"TechArticle\", \"headline\": \"电梯：工业4.0应用方案\", \"description\": \"测量曳引机与门机电机的转子角度，为低速平层和开关门的速度闭环提供反馈。\", \"about\": \"电梯\", \"author\": {\"@type\": \"Organization\", \"name\": \"昆泰芯微电子\", \"alternateName\": \"CONNTEK\", \"url\": \"https://conntek.grosso.link/\"}, \"publisher\": {\"@type\": \"Organization\", \"name\": \"昆泰芯微电子\", \"alternateName\": \"CONNTEK\", \"url\": \"https://conntek.grosso.link/\"}, \"url\": \"https://conntek.grosso.link/applications/industry4/elevator\"}"
---

<nav class="c-crumbs"><a href="/">首页</a><i>/</i><a href="/applications/">市场应用</a><i>/</i><a href="/applications/industry4">工业4.0</a><i>/</i><span>电梯</span></nav>

<p class="c-kicker">工业4.0</p>

# 电梯

<p class="c-lead">测量曳引机与门机电机的转子角度，为低速平层和开关门的速度闭环提供反馈。</p>

<div class="c-actions"><a class="c-btn c-btn--brand" href="/products/encoder/kth78">推荐芯片 KTH78xx</a><a class="c-btn" href="/contact">方案咨询</a></div>

## 场景说明

<div class="c-split c-split--overview"><div class="c-split__text">

电梯里需要连续角度反馈的主要是两台电机：驱动轿厢升降的永磁同步曳引机，以及装在轿厢顶上带动门板开合的门机。两者都采用磁场定向控制，驱动器要实时知道转子转到了哪个电角度，才能决定各相电流的大小和方向。磁铁装在电机轴端或轴上的磁环，芯片贴在后端盖的电路板上，测出的角度同时用于换相和速度闭环。

乘坐体验集中在低速段：曳引机启动和平层时转速很低，门机在关门末段要以爬行速度缓停，角度噪声和反馈延迟会直接表现为轿厢抖动、门板发顿。曳引机轴径大，轴端还要让出制动器和线缆位置，芯片常只能离轴装在磁环侧面。另一方面，平层、门到位和限位只需判断到没到，属于整梯安全回路，应由独立的开关与安全电路承担，不由角度编码芯片替代。

</div><div class="c-split__media c-split__media--frame c-split__media--case"><img src="/img/case/industry4-elevator.webp" alt="电梯" loading="lazy"></div></div>

## 检测需求

<p class="c-sec-lead">电梯对传感器的主要要求。</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>低速要平稳</h3><p>平层与关门末段转速很低，角度噪声会直接变成抖动。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>可离轴安装</h3><p>曳引机轴径大、轴端空间被占，芯片常装在磁环侧面。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>长线能传输</h3><p>编码器信号要从电机走到控制柜，途经强电线缆附近。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>异常可诊断</h3><p>磁铁松动或气隙变化时，驱动器需要及时得到提示。</p></div></div></div>

## 为什么选 KTH78xx

<p class="c-sec-lead">16 位分辨率，系统延时 1 μs 并做延时补偿，全系支持在轴与离轴应用</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>低延时反馈</h3><p>每 1 μs 更新一次数据并做延时补偿，速度环拿到的是当下位置。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>在轴离轴通用</h3><p>全系支持离轴应用，精度在轴 ±0.35°、离轴 ±1° 左右。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>差分增量输出</h3><p><a class="c-xref" href="/products/encoder/kth78/kth7814-x-c-qn16">KTH7814</a> 提供 SPI / ABZ / -ABZ 输出并带 CRC 校验。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>磁场报警</h3><p>磁场过低、过高报警阈值可由用户设置，工作磁场 30 ~ 150 mT。</p></div></div></div>

<div class="c-grid c-grid--2"><a class="c-card" href="/products/encoder/kth78"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth78.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH78 系列</span><h3>低延时霍尔绝对角度编码器</h3><p>16 位分辨率，系统延时 1 μs 并做延时补偿，全系支持在轴与离轴应用</p><span class="c-card__more">查看产品</span></div></a></div>

## 设计注意点

<p class="c-sec-lead">通用工程建议，实际设计以产品手册与实测为准。</p>

<ul class="c-checklist"><li>先把曳引机、门机的连续角度反馈与平层、门到位、限位这类到位信号分开选型，后者按电梯安全回路要求使用独立开关，不用角度编码芯片替代。</li><li>曳引机轴端空间不足时采用离轴磁环方案，定稿前先用磁仿真确认芯片位置的磁场落在 30 ~ 150 mT 内，装配后再按实际偏心与气隙完成离轴校准。</li><li>曳引机轴端的电磁制动器在吸合与释放时会产生杂散磁场，芯片尽量远离制动器线圈，并在制动器两种状态下各测一次角度误差。</li><li>编码器线缆与电机动力线分开走线；电机到控制柜距离较长时优先选差分 ABZ 输出，数字读数选用带 CRC 校验的型号。</li></ul>

## 相关案例

<div class="c-grid c-grid--4"><a class="c-card" href="/applications/industry4/platform-screen-door"><div class="c-card__media c-media--case"><img src="/img/case/industry4-platform-screen-door.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH78xx</span><h3>屏蔽门</h3><p>测量站台门门机电机角度并换算门扇位置，用于平滑减速和精确停位。</p><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/applications/industry4/bldc-motor"><div class="c-card__media c-media--case"><img src="/img/case/industry4-bldc-motor.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH78xx</span><h3>无刷直流电机</h3><p>读取无刷电机转子的绝对角度，用于换相与磁场定向控制，覆盖电动工具等大电流工况。</p><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/applications/industry4/closed-loop-stepper"><div class="c-card__media c-media--case"><img src="/img/case/industry4-closed-loop-stepper.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH78xx</span><h3>步进闭环</h3><p>在步进电机尾端读取转子绝对角度，实时发现失步并闭环修正，兼顾定位与发热。</p><span class="c-card__more">查看案例</span></div></a></div>

<div class="c-cta"><div><h2 class="c-cta__title">需要选型建议、样品或技术支持？</h2><p>昆泰芯提供芯片选型、磁场仿真与方案设计支持，欢迎与我们的销售和技术团队联系。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
