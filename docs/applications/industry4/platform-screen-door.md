---
title: "屏蔽门 · 工业4.0应用"
description: "测量站台门门机电机角度并换算门扇位置，用于平滑减速和精确停位。"
aside: false
pageClass: "c-page c-page--case"
ld: "{\"@context\": \"https://schema.org\", \"@type\": \"TechArticle\", \"headline\": \"屏蔽门：工业4.0应用方案\", \"description\": \"测量站台门门机电机角度并换算门扇位置，用于平滑减速和精确停位。\", \"about\": \"屏蔽门\", \"author\": {\"@type\": \"Organization\", \"name\": \"昆泰芯微电子\", \"alternateName\": \"CONNTEK\", \"url\": \"https://conntek.grosso.link/\"}, \"publisher\": {\"@type\": \"Organization\", \"name\": \"昆泰芯微电子\", \"alternateName\": \"CONNTEK\", \"url\": \"https://conntek.grosso.link/\"}, \"url\": \"https://conntek.grosso.link/applications/industry4/platform-screen-door\"}"
---

<nav class="c-crumbs"><a href="/">首页</a><i>/</i><a href="/applications/">市场应用</a><i>/</i><a href="/applications/industry4">工业4.0</a><i>/</i><span>屏蔽门</span></nav>

<p class="c-kicker">工业4.0</p>

# 屏蔽门

<p class="c-lead">测量站台门门机电机角度并换算门扇位置，用于平滑减速和精确停位。</p>

<div class="c-actions"><a class="c-btn c-btn--brand" href="/products/encoder/kth78">推荐芯片 KTH78xx</a><a class="c-btn" href="/contact">方案咨询</a></div>

## 场景说明

<div class="c-split c-split--overview"><div class="c-split__text">

地铁站台屏蔽门每一侧由多扇滑动门组成，每扇门的门机把电机旋转经皮带或丝杠转换成门扇的直线移动。门控单元需要连续知道门扇走到了哪里，才能按速度曲线加速、匀速、减速，并在开到位和关到位之前平稳停住。磁铁装在门机电机轴端，角度编码芯片贴在电机后部的电路板上，角度逐圈累计后换算成门扇行程。

屏蔽门随列车每次进出站开关一次，门机长期高频动作，站台上还叠加列车通过带来的振动和牵引供电的电磁干扰。门控单元与门机之间有一段线缆，信号要能抵抗共模噪声。门关闭并锁紧是列车允许发车的前提，这类到位与锁闭信号属于安全回路，由独立的检测开关与安全电路完成；角度编码芯片提供的是门机闭环控制所需的连续位置，防夹检测同样另有专用手段。

</div><div class="c-split__media c-split__media--frame c-split__media--case"><img src="/img/case/industry4-platform-screen-door.webp" alt="屏蔽门" loading="lazy"></div></div>

## 检测需求

<p class="c-sec-lead">屏蔽门对传感器的主要要求。</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>连续位置</h3><p>门扇按速度曲线运行，到位前需要平滑减速并停稳。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>频繁启停</h3><p>列车每次进出站都要开关门，门机长期高频动作。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>抗振抗扰</h3><p>列车通过的振动与牵引供电的电磁干扰同时存在。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>长线传输</h3><p>门控单元与门机之间有线缆，信号需要抵抗共模噪声。</p></div></div></div>

## 为什么选 KTH78xx

<p class="c-sec-lead">16 位分辨率，系统延时 1 μs 并做延时补偿，全系支持在轴与离轴应用</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>可编程增量</h3><p>ABZ 4 ~ 4096 步/圈可编程，可沿用门控单元原有的增量计数方式。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>差分增量输出</h3><p><a class="c-xref" href="/products/encoder/kth78/kth7814-x-c-qn16">KTH7814</a> 提供 SPI / ABZ / -ABZ 输出并带 CRC 校验，适合线缆传输。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>磁场诊断</h3><p>磁场过低、过高报警阈值用户可设，气隙异常时可给出报警。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>无刷换相</h3><p><a class="c-xref" href="/products/encoder/kth78/kth7812-x-n-qn16">KTH7812</a> / <a class="c-xref" href="/products/encoder/kth78/kth7813-x-n-qn16">KTH7813</a> 提供 UVW 输出，1 ~ 8 对极可编程。</p></div></div></div>

<div class="c-grid c-grid--2"><a class="c-card" href="/products/encoder/kth78"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth78.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH78 系列</span><h3>低延时霍尔绝对角度编码器</h3><p>16 位分辨率，系统延时 1 μs 并做延时补偿，全系支持在轴与离轴应用</p><span class="c-card__more">查看产品</span></div></a></div>

## 设计注意点

<p class="c-sec-lead">通用工程建议，实际设计以产品手册与实测为准。</p>

<ul class="c-checklist"><li>门机电机要转多圈才走完一个行程，单圈绝对角度只给出圈内位置，上电后需结合到位开关或一次低速找位来建立门扇的绝对位置。</li><li>关门到位、锁闭和防夹由独立的开关与安全电路完成，角度芯片只承担门机闭环所需的连续位置，两类器件分开选型。</li><li>门机随列车通过持续受振，磁铁与芯片间的气隙会动态变化；结构上把磁铁固定牢，并把磁场过低、过高报警接入门控单元作为气隙异常的监测。</li><li>门控单元与门机距离较长时选用差分 ABZ 输出，编码器线使用屏蔽线并与电机动力线分开走线。</li></ul>

## 相关案例

<div class="c-grid c-grid--4"><a class="c-card" href="/applications/industry4/elevator"><div class="c-card__media c-media--case"><img src="/img/case/industry4-elevator.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH78xx</span><h3>电梯</h3><p>测量曳引机与门机电机的转子角度，为低速平层和开关门的速度闭环提供反馈。</p><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/applications/industry4/turnstile"><div class="c-card__media c-media--case"><img src="/img/case/industry4-4.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57xx</span><h3>闸机</h3><p>检测摆翼或门翼的开合角度，用于限位与防夹判断。</p><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/applications/industry4/bldc-motor"><div class="c-card__media c-media--case"><img src="/img/case/industry4-bldc-motor.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH78xx</span><h3>无刷直流电机</h3><p>读取无刷电机转子的绝对角度，用于换相与磁场定向控制，覆盖电动工具等大电流工况。</p><span class="c-card__more">查看案例</span></div></a></div>

<div class="c-cta"><div><h2 class="c-cta__title">需要选型建议、样品或技术支持？</h2><p>昆泰芯提供芯片选型、磁场仿真与方案设计支持，欢迎与我们的销售和技术团队联系。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
