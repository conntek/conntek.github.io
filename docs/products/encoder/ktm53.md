---
title: "KTM53 系列 离轴 AMR 角度编码器"
description: "AMR 配合垂直霍尔与数字算法实现离轴测量，校准后 INL ±0.03°（典型值）"
aside: false
pageClass: "c-page c-page--product"
ld: "{\"@context\": \"https://schema.org\", \"@type\": \"Product\", \"name\": \"KTM53 系列 离轴 AMR 角度编码器\", \"description\": \"AMR 配合垂直霍尔与数字算法实现离轴测量，校准后 INL ±0.03°（典型值）\", \"category\": \"编码器芯片\", \"brand\": {\"@type\": \"Brand\", \"name\": \"CONNTEK 昆泰芯\"}, \"manufacturer\": {\"@type\": \"Organization\", \"name\": \"昆泰芯微电子\", \"alternateName\": \"CONNTEK\", \"url\": \"https://conntek.grosso.link/\"}, \"image\": \"https://conntek.grosso.link/img/icons-web/ktm53.webp\", \"url\": \"https://conntek.grosso.link/products/encoder/ktm53\"}"
---

<nav class="c-crumbs"><a href="/">首页</a><i>/</i><a href="/products/">产品中心</a><i>/</i><a href="/products/encoder/">编码器芯片</a><i>/</i><span>KTM53 系列</span></nav>

<div class="c-product-hero"><div class="c-product-hero__text">

<p class="c-kicker">KTM53 系列</p>

# 离轴 AMR 角度编码器

<p class="c-lead">AMR 配合垂直霍尔与数字算法实现离轴测量，校准后 INL ±0.03°（典型值）</p>

<div class="c-specs"><div class="c-spec"><b>21 bit</b><span>分辨率</span></div><div class="c-spec"><b>±0.03°</b><span>精度 · 离轴校准后典型值</span></div><div class="c-spec"><b>60000 rpm</b><span>转速</span></div><div class="c-spec"><b>3 ~ 5.5 V</b><span>电压</span></div></div>

<div class="c-actions"><a class="c-btn c-btn--brand" href="#技术文档">下载技术文档<small>1</small></a><a class="c-btn" href="/contact">申请样品 / 咨询</a></div>

</div><div class="c-product-hero__media"><img src="/img/icons-web/ktm53.webp" alt="KTM53 系列"></div></div>

## 产品概述

<div class="c-split c-split--overview"><div class="c-split__text">

KTM5300 是基于各向异性磁阻（AMR）技术的高速高精度角度编码器芯片，内部集成两对互成 45° 的 AMR 惠斯通电桥及专用信号处理电路。AMR 器件在角度测量中工作于饱和区（饱和磁场约 300 高斯），主要响应平行于芯片表面的磁场方向变化，对磁场强度变化不敏感，因此对磁铁加工误差和安装距离误差的容忍度较高。

KTM5300 采用离轴安装，配合垂直霍尔与数字算法实现高精度离轴测量，校准后 INL 精度可达 ±0.03°（典型值），角度噪声 0.005°。芯片提供 4 线 SPI 接口读取 21 位绝对角度，并支持单线 PWM 输出；增量 ABZ 输出可替代传统光电编码器，分辨率最高 65,536 脉冲/圈（262,144 步/圈），增量 UVW 输出支持 1 ~ 64 对极/圈。

核心优势是用户侧一键自校准，可补偿磁铁不理想与安装偏差引入的非线性误差，显著改善 INL。工作电压 3 ~ 5.5 V，工作电流 25 mA，磁场检测范围 20 ~ 150 mT，启动时间 1 ~ 260 ms 可调，工作温度 -40 ~ 125 ℃，封装 QFN3*3_16L。

</div><div class="c-split__media c-split__media--frame"><img src="/img/photo/ktm53.webp" alt="KTM53 系列 产品图" loading="lazy"></div></div>

## 核心特点

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>AMR 磁阻技术</h3><p>两对互成 45° 的 AMR 电桥，0 ~ 360° 绝对角度检测</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>离轴安装</h3><p>配合垂直霍尔与数字算法，实现高精度离轴测量</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>一键自校准</h3><p>闭环自校准，离轴校准后 INL 可达 ±0.03°</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>非匀速自校准</h3><p>优化非匀速工况下的自校准性能</p></div></div><div class="c-feature"><span class="c-feature__no">05</span><div><h3>高速低延时</h3><p>转速最高 60000 rpm，角度输出延时 2 ~ 10 μs</p></div></div><div class="c-feature"><span class="c-feature__no">06</span><div><h3>多路同时输出</h3><p>增量 ABZ、增量 UVW、PWM 绝对值与 4 线 SPI</p></div></div><div class="c-feature"><span class="c-feature__no">07</span><div><h3>可编程增量</h3><p>ABZ 1 ~ 65536 脉冲/圈，UVW 1 ~ 64 对极</p></div></div><div class="c-feature"><span class="c-feature__no">08</span><div><h3>参数存储</h3><p>内置 EEPROM，3.3 ~ 5.0 V 供电下烧录与保存参数</p></div></div></div>

## 规格参数

<div class="c-table c-kv"><table><tbody><tr><th scope="row">型号</th><td>KTM5300</td><th scope="row">系列</th><td>KTM53XX</td></tr><tr><th scope="row">磁铁摆放方式</th><td>离轴</td><th scope="row">检测范围</th><td>360°</td></tr><tr><th scope="row">供电电压</th><td>3 ~ 5.5 V</td><th scope="row">噪声</th><td>0.005°</td></tr><tr><th scope="row">角度 INL</th><td>±0.03°</td><th scope="row">工作电流</th><td>25 mA</td></tr><tr><th scope="row">转速</th><td>60000 rpm</td><th scope="row">输出方式</th><td>SPI / ABZ / UVW / PWM</td></tr><tr><th scope="row">SPI 分辨率</th><td>21 bit</td><th scope="row">ABZ 分辨率</th><td>1 ~ 65536 线可调</td></tr><tr><th scope="row">磁场检测范围</th><td>20 ~ 150 mT</td><th scope="row">启动时间</th><td>1 ~ 260 ms 可调</td></tr><tr><th scope="row">工作温度</th><td>-40 ~ 125 ℃</td><th scope="row">封装</th><td>QFN3*3_16L</td></tr></tbody></table></div>

## 技术文档

<p class="c-sec-lead">产品手册、评估套件说明与上位机软件，点击文件名直接下载。</p>

<div class="c-table c-docs"><table><thead><tr><th>型号</th><th>类型</th><th>中文版</th><th>英文版</th></tr></thead><tbody><tr><td class="c-mono">KTM5300</td><td><span class="c-badge">产品手册</span></td><td><a class="c-file" href="/files/KTM5300%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf" target="_blank"><em>PDF</em>KTM5300 产品手册.pdf</a></td><td><span class="c-muted">—</span></td></tr></tbody></table></div>

## 同类产品

<p class="c-sec-lead">编码器芯片产品线的其他系列。</p>

<div class="c-grid c-grid--4"><a class="c-card" href="/products/encoder/ktm52"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm52.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM52 系列</span><h3>21 位高精度 AMR 角度编码器</h3><p>21 位分辨率，一键自校准后 INL ±0.015°（典型值），最高 60000 rpm</p><span class="c-card__more">查看详情</span></div></a><a class="c-card" href="/products/encoder/ktm58"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm58.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM58 系列</span><h3>30 bit 绝对角度细分器</h3><p>最大 4096 对极输入，30 bit 绝对角度细分，适配磁电阻与光编、光栅、磁栅</p><span class="c-card__more">查看详情</span></div></a><a class="c-card" href="/products/encoder/ktm59"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm59.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM59 系列</span><h3>高速 TMR 磁编码器</h3><p>双 16 bit 2M SAR ADC，单对极细分 24 bit，最高 180,000 rpm</p><span class="c-card__more">查看详情</span></div></a><a class="c-card" href="/products/encoder/kth78"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kth78.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH78 系列</span><h3>低延时霍尔绝对角度编码器</h3><p>16 位分辨率，系统延时 1 μs 并做延时补偿，全系支持在轴与离轴应用</p><span class="c-card__more">查看详情</span></div></a></div>

<div class="c-cta"><div><h2 class="c-cta__title">需要选型建议、样品或技术支持？</h2><p>昆泰芯提供芯片选型、磁场仿真与方案设计支持，欢迎与我们的销售和技术团队联系。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
