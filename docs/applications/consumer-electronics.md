---
title: "消费类电子"
description: "为耳机、笔记本、手机与游戏设备提供位置与角度感知"
aside: false
pageClass: "c-page"
---

<nav class="c-crumbs"><a href="/msite/">首页</a><i>/</i><a href="/msite/applications/">市场应用</a><i>/</i><span>消费类电子</span></nav>

<p class="c-kicker">市场应用</p>

# 消费类电子

<p class="c-lead">为耳机、笔记本、手机与游戏设备提供位置与角度感知</p>

<div class="c-stats"><div class="c-stat"><b>9</b><span>应用案例</span></div><div class="c-stat"><b>5</b><span>款推荐芯片</span></div></div>

消费类产品里的磁传感，绝大多数落在三件事上：判断两个部件有没有合到位（开盖、合盖、入仓、吸附），测一段有限行程的位移（笔尖压感、滑盖、升降摄像头），以及测一个二维方向（摇杆、旋钮、表冠）。这些位置信息本来可以用微动开关或电位器做，改用磁方案的原因是非接触——没有触点磨损，可以隔着塑胶外壳工作，密封结构不必为传感器开孔。

约束也很集中：整机靠电池供电，传感器多半要常年在线，于是平均功耗直接决定待机天数；可用的板面往往只有一两平方毫米，封装尺寸先于性能被筛一遍；同时整机批量大，芯片的阈值一致性与温度漂移必须小到不用逐台标定。

## 领域需求

<p class="c-sec-lead">消费类电子对磁传感器的共性要求。</p>

<div class="c-features"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>常开待机功耗</h3><p>盖开关、入仓检测这类功能必须一直在线，平均电流决定整机待机时长，往往要求做到微安甚至纳安量级。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>封装尺寸</h3><p>耳机仓、触控笔、手表内部留给传感器的面积只有毫米级，封装选不下来，性能再好也用不上。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>批量一致性</h3><p>百万台量级不可能逐台标定，翻转阈值与温漂必须在出厂范围内收敛，否则产线要加校准工序。</p></div></div><div class="c-feature"><span class="c-feature__no">04</span><div><h3>二维/三维方向</h3><p>摇杆、旋钮要的是方向而不是有无，需要同时拿到两个以上轴向的磁场分量再算角度。</p></div></div><div class="c-feature"><span class="c-feature__no">05</span><div><h3>主控接口</h3><p>低功耗主控的 ADC 通道与 IO 都紧张，数字接口和开关量输出对系统资源的占用差别很大。</p></div></div></div>

## 应用案例

<p class="c-sec-lead">典型应用有 TWS 耳机、笔记本电脑开盖唤醒、升降摄像头位置检测、智能皮套与折叠屏手机。应用案例：触控笔采用 <a class="c-xref" href="/msite/products/switch/ktm13">KTM13</a> 系列，电子棋盘采用 <a class="c-xref" href="/msite/products/switch/kth16/kth1604th">KTH1604</a>，轮椅摇杆、洗衣机、掌机摇杆与智能手表采用 <a class="c-xref" href="/msite/products/3d-hall/kth57">KTH57</a> 系列，游戏手柄采用 <a class="c-xref" href="/msite/products/switch/linear-hall">KTH564</a> 系列。</p>

<div class="c-grid c-grid--4"><a class="c-card" href="/msite/applications/consumer-electronics/stylus"><div class="c-card__media c-media--case"><img src="/msite/img/case/consumer-electronics-0.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM13xx</span><h3>触控笔</h3><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/msite/applications/consumer-electronics/e-chessboard"><div class="c-card__media c-media--case"><img src="/msite/img/case/consumer-electronics-1.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH1604</span><h3>电子棋盘</h3><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/msite/applications/consumer-electronics/wheelchair-joystick"><div class="c-card__media c-media--case"><img src="/msite/img/case/consumer-electronics-2.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57xx</span><h3>轮椅摇杆</h3><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/msite/applications/consumer-electronics/washing-machine"><div class="c-card__media c-media--case"><img src="/msite/img/case/consumer-electronics-3.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57xx</span><h3>洗衣机</h3><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/msite/applications/consumer-electronics/game-controller"><div class="c-card__media c-media--case"><img src="/msite/img/case/consumer-electronics-4.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH564X</span><h3>游戏手柄</h3><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/msite/applications/consumer-electronics/handheld-joystick"><div class="c-card__media c-media--case"><img src="/msite/img/case/consumer-electronics-5.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57xx</span><h3>掌机摇杆</h3><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/msite/applications/consumer-electronics/smart-watch"><div class="c-card__media c-media--case"><img src="/msite/img/case/consumer-electronics-6.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH57xx</span><h3>智能手表</h3><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/msite/applications/consumer-electronics/drone-rotor"><div class="c-card__media c-media--case"><img src="/msite/img/case/consumer-electronics-drone-rotor.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTH78xx</span><h3>无人机旋翼</h3><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/msite/applications/consumer-electronics/laptop-lid"><div class="c-card__media c-media--case"><img src="/msite/img/case/consumer-electronics-laptop-lid.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM13xx</span><h3>笔记本与平板合盖检测</h3><span class="c-card__more">查看案例</span></div></a></div>

## 推荐芯片一览

<div class="c-table c-table--links"><table><thead><tr><th>推荐芯片</th><th>对应产品</th><th>应用场景</th></tr></thead><tbody><tr><td class="c-mono"><a class="c-xref" href="/msite/products/switch/ktm13">KTM13xx</a></td><td><a href="/msite/products/switch/ktm13">KTM13 系列 TMR 磁阻开关</a></td><td>触控笔、笔记本与平板合盖检测</td></tr><tr><td class="c-mono"><a class="c-xref" href="/msite/products/switch/kth16/kth1604th">KTH1604</a></td><td><a href="/msite/products/switch/kth16">KTH13/16/17 系列 微功耗 1D 霍尔开关</a></td><td>电子棋盘</td></tr><tr><td class="c-mono"><a class="c-xref" href="/msite/products/3d-hall/kth57">KTH57xx</a></td><td><a href="/msite/products/3d-hall/kth57">KTH57 系列 三轴线性霍尔传感器</a></td><td>轮椅摇杆、洗衣机、掌机摇杆、智能手表</td></tr><tr><td class="c-mono"><a class="c-xref" href="/msite/products/switch/linear-hall">KTH564X</a></td><td><a href="/msite/products/switch/linear-hall">KTH564 系列 线性霍尔芯片</a></td><td>游戏手柄</td></tr><tr><td class="c-mono"><a class="c-xref" href="/msite/products/encoder/kth78">KTH78xx</a></td><td><a href="/msite/products/encoder/kth78">KTH78 系列 低延时霍尔绝对角度编码器</a></td><td>无人机旋翼</td></tr></tbody></table></div>

## 需求与芯片对照

<div class="c-table c-table--links"><table><thead><tr><th>需求</th><th>推荐系列</th><th>依据</th></tr></thead><tbody><tr><td>开合到位检测</td><td><a href="/msite/products/switch/ktm13">KTM13 系列</a></td><td>TMR 与 ASIC 单芯片集成，160 nA @ 3 V，回差可小于 3 高斯。</td></tr><tr><td>极小空间开关位</td><td><a href="/msite/products/switch/kth16">KTH13/16/17 系列</a></td><td><a class="c-xref" href="/msite/products/switch/kth16/kth1604th">KTH1604</a> 为 DFN/FBP 1*1-4L 封装，1.6 μA @ 1.8 V。</td></tr><tr><td>摇杆旋钮角度</td><td><a href="/msite/products/3d-hall/kth57">KTH57 系列</a></td><td>X、Y、Z 三轴磁场，16 bit 分辨率，I2C / SPI，待机 1.4 μA。</td></tr><tr><td>连续位移模拟量</td><td><a href="/msite/products/switch/linear-hall">KTH564 系列</a></td><td>零磁场输出 1/2 VCC，1.5 ~ 13 mV/Gs 多档匹配行程。</td></tr><tr><td>宽温整机环境</td><td><a href="/msite/products/switch/ktm13">KTM13 系列</a></td><td>-40 ~ 125 ℃，频率 50 / 1600 / 5000 Hz 三档可选。</td></tr></tbody></table></div>

## 设计自检

<p class="c-sec-lead">方案定型前先回答这几个问题。</p>

<ul class="c-checklist"><li>这个功能是常开还是被事件唤醒？常开的按平均功耗选频率档，被唤醒的可以用高频档换响应速度。</li><li>机构公差（装配间隙、磁铁贴装偏差、跌落后的位移）会让气隙变化多少？把最差气隙下的磁场值算出来，再回头选 BOP / BRP 或灵敏度档。</li><li>需要的是「有没有到位」还是「到了哪个位置」？前者用开关型输出，后者才需要线性或数字角度输出，两者的功耗和 BOM 差一个量级。</li><li>整机里有没有扬声器磁体、马达、无线充电线圈？先确认它们在传感器位置产生的杂散磁场，再定阈值裕量。</li><li>主控是否有空余 ADC 与足够的采样带宽？没有就优先走数字接口，把角度计算放到芯片侧或主控软件侧要提前定。</li></ul>

## 其他应用领域

<div class="c-grid c-grid--3"><a class="c-card" href="/msite/applications/intelligent-life"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/app-intelligent-life.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">11 个案例</span><h3>智能生活</h3><p>让门锁、水表、马桶与家电感知状态、响应操作</p><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/msite/applications/industry4"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/app-industry4.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">21 个案例</span><h3>工业4.0</h3><p>服务电表、断路器、闸机与电机转子位置检测</p><span class="c-card__more">查看案例</span></div></a><a class="c-card" href="/msite/applications/intelligent-transportation"><div class="c-card__media c-media--icon"><img src="/msite/img/icons-web/app-intelligent-transportation.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">2 个案例</span><h3>智能交通</h3><p>面向汽车角度与位置检测的车规级传感方案</p><span class="c-card__more">查看案例</span></div></a></div>

<div class="c-cta"><div><h2 class="c-cta__title">需要选型建议、样品或技术支持？</h2><p>昆泰芯提供芯片选型、磁场仿真与方案设计支持，欢迎与我们的销售和技术团队联系。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/msite/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
