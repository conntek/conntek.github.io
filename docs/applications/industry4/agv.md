---
title: "AGV 搬运机器人 · 工业4.0应用"
description: "测量舵轮转向角与驱动电机转子角度，实现上电即知轮向和电机换相。"
aside: false
pageClass: "c-page c-page--case"
ld: "{\"@context\": \"https://schema.org\", \"@type\": \"TechArticle\", \"headline\": \"AGV 搬运机器人：工业4.0应用方案\", \"description\": \"测量舵轮转向角与驱动电机转子角度，实现上电即知轮向和电机换相。\", \"about\": \"AGV 搬运机器人\", \"author\": {\"@type\": \"Organization\", \"name\": \"昆泰芯微电子\", \"alternateName\": \"CONNTEK\", \"url\": \"https://conntek.grosso.link/\"}, \"publisher\": {\"@type\": \"Organization\", \"name\": \"昆泰芯微电子\", \"alternateName\": \"CONNTEK\", \"url\": \"https://conntek.grosso.link/\"}, \"url\": \"https://conntek.grosso.link/applications/industry4/agv\"}"
---

<nav class="c-crumbs"><a href="/">首页</a><i>/</i><a href="/applications/">市场应用</a><i>/</i><a href="/applications/industry4">工业4.0</a><i>/</i><span>AGV 搬运机器人</span></nav>

<p class="c-kicker">工业4.0</p>

# AGV 搬运机器人

<p class="c-lead">测量舵轮转向角与驱动电机转子角度，实现上电即知轮向和电机换相。</p>

<div class="c-actions"><a class="c-btn c-btn--brand" href="/products/encoder/kth78">推荐芯片 KTH78xx</a><a class="c-btn" href="/contact">方案咨询</a></div>

## 场景说明

<div class="c-split c-split--overview"><div class="c-split__text">

AGV 与 AMR 底盘上的角度反馈分两类位置。舵轮底盘的转向轴带着整个轮组绕竖直轴转动，需要测量轮组相对车体的转向角；驱动电机经减速器带动车轮前进，需要测量转子电角度，用于换相和速度闭环。转向角的磁铁多装在转向轴上，驱动电机的磁铁装在电机尾轴或轮毂电机的转子磁环上，芯片贴在相邻的控制板上。

车辆在工厂里连续运行，随时可能因急停、换电或断电停在任意姿态，重新上电时控制器必须直接读出轮子朝向，不能先转动回零，否则在窄通道里容易碰到货架。转向角的小偏差会随行驶距离放大成车身横向偏移。车体里驱动电机的大电流线束与编码器挨得很近，驶过地面接缝时的冲击又会让磁铁与芯片之间的气隙动态变化。

</div><div class="c-split__media c-split__media--frame c-split__media--case"><img src="/img/case/industry4-agv.webp" alt="AGV 搬运机器人" loading="lazy"></div></div>

## 检测需求

<p class="c-sec-lead">AGV 搬运机器人对传感器的主要要求。</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>上电即知角度</h3><p>断电后停在任意姿态，重新上电不能靠回零找方向。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>转向角稳定</h3><p>转向角的小偏差会随行驶距离放大成横向偏移。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>换相反馈快</h3><p>驱动电机采用磁场定向控制，反馈延迟影响起步平顺。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>抗振抗干扰</h3><p>电机大电流与地面冲击同时作用在传感器上。</p></div></div></div>

## 为什么选 KTH78xx

<p class="c-sec-lead">16 位分辨率，系统延时 1 μs 并做延时补偿，全系支持在轴与离轴应用</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>绝对角度</h3><p>16 bit 绝对角度输出，启动时间 1 ms，上电即可读出转向角。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>低延时</h3><p>每 1 μs 更新一次数据并做延时补偿，转速最高 120,000 rpm。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>换相输出</h3><p><a class="c-xref" href="/products/encoder/kth78/kth7812-x-n-qn16">KTH7812</a> / <a class="c-xref" href="/products/encoder/kth78/kth7813-x-n-qn16">KTH7813</a> 提供 UVW 输出，1 ~ 8 对极可编程。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>磁场诊断</h3><p>磁场过低、过高报警阈值用户可设，冲击造成的气隙异常可报警。</p></div></div></div>

<div class="c-grid c-grid--2"><a class="c-card" href="/products/encoder/kth78"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth78.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH78 系列</span><h3>低延时霍尔绝对角度编码器</h3><p>16 位分辨率，系统延时 1 μs 并做延时补偿，全系支持在轴与离轴应用</p><span class="c-card__more">查看产品</span></div></a></div>

## 设计注意点

<p class="c-sec-lead">通用工程建议，实际设计以产品手册与实测为准。</p>

<ul class="c-checklist"><li>转向角芯片应测转向轴本身而不是转向电机轴：电机轴经减速后要转多圈，单圈绝对角度无法在上电时直接给出轮组朝向。</li><li>驱动轮的里程误差主要来自轮子打滑，驱动电机编码器按换相与速度闭环的需要选型即可，不必在分辨率上加码。</li><li>转向轴中间常需穿过线缆，轴端放不下磁铁时改用离轴磁环方案，并在装配完成后做离轴校准。</li><li>编码器远离驱动电机动力线与电池主回路；数字读数选用带 CRC 校验的型号，控制器对校验失败的数据帧直接丢弃。</li></ul>

## 相关案例

<div class="c-grid c-grid--4"><a class="c-card" href="/applications/industry4/bldc-motor"><div class="c-card__media c-media--case"><img src="/img/case/industry4-bldc-motor.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH78xx</span><h3>无刷直流电机</h3><p>读取无刷电机转子的绝对角度，用于换相与磁场定向控制，覆盖电动工具等大电流工况。</p><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/applications/industry4/gearbox"><div class="c-card__media c-media--case"><img src="/img/case/industry4-gearbox.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH71xx</span><h3>齿轮箱</h3><p>测量减速齿轮箱输入轴或输出轴的转角，用于位置闭环与传动状态监测。</p><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/applications/intelligent-life/robot-vacuum"><div class="c-card__media c-media--case"><img src="/img/case/intelligent-life-3.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57xx</span><h3>扫地机器人-真空吸尘器</h3><p>检测拖布、滚刷等可换模块的安装位置与抬升行程。</p><span class="c-card__more">查看案例</span></div></a></div>

<div class="c-cta"><div><h2 class="c-cta__title">需要选型建议、样品或技术支持？</h2><p>昆泰芯提供芯片选型、磁场仿真与方案设计支持，欢迎与我们的销售和技术团队联系。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
