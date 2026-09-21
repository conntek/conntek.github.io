---
title: "游标 / Vernier（Nonius） · 技术 Wiki"
description: "用两条周期数不同的码道拼出高分辨率的单圈绝对位置"
aside: false
pageClass: "c-page c-page--wiki"
ld: "{\"@context\": \"https://schema.org\", \"@type\": \"DefinedTerm\", \"name\": \"游标 / Vernier（Nonius）\", \"description\": \"用两条周期数不同的码道拼出高分辨率的单圈绝对位置\", \"inDefinedTermSet\": {\"@type\": \"DefinedTermSet\", \"name\": \"昆泰芯技术 Wiki\", \"url\": \"https://conntek.grosso.link/basics/\"}, \"url\": \"https://conntek.grosso.link/basics/vernier\"}"
---

<nav class="c-crumbs"><a href="/">首页</a><i>/</i><a href="/basics/">技术 Wiki</a><i>/</i><span>游标 / Vernier（Nonius）</span></nav>

<p class="c-kicker">精度、噪声与动态</p>

# 游标 / Vernier（Nonius）

<p class="c-lead">用两条周期数不同的码道拼出高分辨率的单圈绝对位置</p>

## 是什么

游标（也称 Nonius）方案有两条周期数不同的码道，常见取法是一条 N 个周期、另一条 N-1 个周期。两条码道的相位之差随机械角缓慢变化，机械转一圈只走过一个周期，据此可以判断当前处在主码道的第几个周期；再用主码道的细分给出高分辨率。

光学码盘与多极磁环都可以采用这种结构，结果是上电即得、不需要回零的高分辨率单圈绝对位置。

## 设计约束

**周期数不能有公约数**：两条码道的周期数若有大于 1 的公约数，一圈内会有多个位置得到完全相同的读数组合，绝对位置无法唯一确定。

**判别裕量随周期数收紧**：主码道周期越多，每个周期对应的判别窗口越窄。两条码道的相位误差——噪声、偏心、充磁不均、码道间串扰、温漂——加起来必须留在窗口的一半以内。

**两条码道要一起设计**：相邻码道的磁场或光信号会互相串扰，两道的幅值与相位一致性要在结构与磁路阶段就考虑。

## 失效是什么样子

游标判错周期时，输出会整整跳一个主码道周期，是离散的阶跃，而不是连续变大的误差。所以验收不能只看平均误差，要看各位置离判别边界还有多少裕量。

::: tip 要点提示
游标方案的风险是离散跳变：平均误差很小的样品，也可能在裕量最小的位置偶发跳一个周期。
:::

## 常见误区

<p class="c-sec-lead">每条标题是常听到的说法，下方是工程上的实际情况。</p>

<div class="c-features c-pitfalls"><div class="c-feature"><span class="c-feature__no">01</span><div><h3>游标只是为了堆位数</h3><p>它的核心价值是在单圈内给出上电即得的绝对位置，同时保留细码道的分辨率。</p></div></div><div class="c-feature"><span class="c-feature__no">02</span><div><h3>两个周期数随便取</h3><p>周期数有公约数就无法唯一定位；差值和周期数还决定了判别裕量与抗噪能力。</p></div></div><div class="c-feature"><span class="c-feature__no">03</span><div><h3>精度合格就不会跳周期</h3><p>判周期看的是相位误差对判别窗口的裕量，要在最差温度、偏心和噪声下单独验证。</p></div></div></div>

## 相关系列

<p class="c-sec-lead">正文涉及的原理与指标，在这些产品系列上用得到。</p>

<div class="c-grid c-grid--3"><a class="c-card" href="/products/encoder/kto95"><div class="c-card__media c-media--icon"><img src="/img/icons-web/kto95.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTO95 系列</span><h3>游标绝对值光学编码器</h3><p>集成高清相位阵列光电传感器，三通道 Nonius 插值实现最高 24 位单圈分辨率</p><span class="c-card__more">查看产品</span></div></a><a class="c-card" href="/products/encoder/ktm58"><div class="c-card__media c-media--icon"><img src="/img/icons-web/ktm58.webp" alt="" loading="lazy"></div><div class="c-card__body"><span class="c-card__kicker">KTM58 系列</span><h3>30 bit 绝对角度细分器</h3><p>最大 4096 对极输入，30 bit 绝对角度细分，适配磁电阻与光编、光栅、磁栅</p><span class="c-card__more">查看产品</span></div></a></div>

## 相关词条

<div class="c-grid c-grid--3"><a class="c-card" href="/basics/pole-pairs"><div class="c-card__body"><span class="c-card__kicker">角度测量与安装</span><h3>对极数 / Pole pairs</h3><p>磁环沿圆周的 N-S 磁极对数，一对极为一个信号周期</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/resolution"><div class="c-card__body"><span class="c-card__kicker">精度、噪声与动态</span><h3>分辨率 / Resolution</h3><p>输出能区分的最小角度步距，与准确度是两回事</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/absolute-incremental"><div class="c-card__body"><span class="c-card__kicker">输出接口</span><h3>绝对值输出 / 增量输出</h3><p>绝对值上电即知当前角度，增量只给出位移量</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/noise"><div class="c-card__body"><span class="c-card__kicker">精度、噪声与动态</span><h3>角度噪声 / Angle noise</h3><p>静止时角度读数的随机起伏，通常以 1σ（均方根）表示</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/inl"><div class="c-card__body"><span class="c-card__kicker">精度、噪声与动态</span><h3>INL / 积分非线性</h3><p>输出角度对真实角度的最大偏差，即角度准确度</p><span class="c-card__more">阅读词条</span></div></a><a class="c-card" href="/basics/latency"><div class="c-card__body"><span class="c-card__kicker">精度、噪声与动态</span><h3>延时与动态误差 / Latency</h3><p>磁场变化到角度输出之间的时间，转速越高，它造成的角度滞后越大</p><span class="c-card__more">阅读词条</span></div></a></div>

<div class="c-wiki-pager">

<div class="c-grid c-grid--2"><a class="c-card" href="/basics/self-calibration"><div class="c-card__body"><span class="c-card__kicker">← 上一条</span><h3>自校准 / Self-calibration</h3><p>器件在实装状态下测量并补偿角度非线性误差</p></div></a><a class="c-card" href="/basics/absolute-incremental"><div class="c-card__body"><span class="c-card__kicker">下一条 →</span><h3>绝对值输出 / 增量输出</h3><p>绝对值上电即知当前角度，增量只给出位移量</p></div></a></div>

</div>

<div class="c-cta"><div><h2 class="c-cta__title">还有拿不准的参数？</h2><p>选型、磁路与接口对接上的问题，欢迎直接找我们的技术团队确认。</p></div><div class="c-cta__actions"><a class="c-btn c-btn--brand" href="/contact">联系我们</a><a class="c-btn" href="mailto:sales@conntek.com.cn">sales@conntek.com.cn</a><a class="c-btn" href="mailto:support@conntek.com.cn">support@conntek.com.cn</a></div></div>
