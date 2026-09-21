import { defineConfig } from 'vitepress'
import data from './sidebar.json'

// 正式地址为 https://conntek.github.io/（仓库 conntek/conntek.github.io，组织主页站点，发布在根路径）；改部署路径时同时设置 SITE_BASE 重新跑 scripts/render.py
const base = process.env.SITE_BASE ?? '/'

const site = 'https://conntek.github.io'
// 标题后缀：正式上线时改为空串（render.py 里 SITE_TAG 同步改）
const siteTag = process.env.SITE_TAG ?? ' (dev site)'

export default defineConfig({
  base,
  lang: 'zh-CN',
  sitemap: { hostname: site + base },
  transformPageData(pageData) {
    const url = site + base + pageData.relativePath.replace(/((^|\/)index)?\.md$/, '$2')
    const title = pageData.frontmatter.title || pageData.title || '昆泰芯微电子'
    const desc = pageData.frontmatter.description || pageData.description || ''
    pageData.frontmatter.head ??= []
    const fm = pageData.frontmatter
    // render.py 写进 frontmatter 的结构化数据（Product / BlogPosting / TechArticle / DefinedTerm），供搜索引擎与 AI 爬虫理解页面
    if (typeof fm.ld === 'string' && fm.ld) {
      pageData.frontmatter.head.push(['script', { type: 'application/ld+json' }, fm.ld])
    }
    if (fm.date) {
      pageData.frontmatter.head.push(['meta', { property: 'article:published_time', content: String(fm.date).slice(0, 10) }])
    }
    pageData.frontmatter.head.push(
      ['link', { rel: 'canonical', href: url }],
      ['meta', { property: 'og:type', content: fm.date ? 'article' : 'website' }],
      ['meta', { property: 'og:locale', content: 'zh_CN' }],
      ['meta', { property: 'og:site_name', content: '昆泰芯微电子 CONNTEK' }],
      ['meta', { property: 'og:title', content: title }],
      ['meta', { property: 'og:description', content: desc }],
      ['meta', { property: 'og:url', content: url }],
      ['meta', { property: 'og:image', content: site + base + 'img/ref/hero-magnet-sensor-render.png' }],
      ['meta', { name: 'twitter:card', content: 'summary_large_image' }],
    )
  },
  title: '昆泰芯微电子',
  titleTemplate: ':title · 昆泰芯 CONNTEK' + siteTag,
  description: '昆泰芯微电子 · 智能感知世界 传递美好生活',
  cleanUrls: true,
  lastUpdated: false,
  // 全站强制深色，不跟随系统，也不显示明暗切换开关
  appearance: 'force-dark',
  head: [
    ['link', { rel: 'icon', type: 'image/png', href: `${base}img/logo-nav-light.png` }],
    ['meta', { name: 'theme-color', content: '#c30d23' }],
    // Google Search Console 网址前缀 https://conntek.github.io/ 的所有权验证（与 public/google354e7d89b86db777.html 二选一即可，两个都留）
    ['meta', { name: 'google-site-verification', content: 'lDieCfUA_J9D-j9E_WxXkPUdIf_PL10Z9RHEKfFZ0kY' }],
    ['meta', { name: 'keywords', content: '昆泰芯,CONNTEK,磁编码器芯片,霍尔传感器,3D霍尔,TMR磁开关,AMR编码器,绝对角度编码器,磁传感器芯片,KTH78,KTM59,KTH57' }],
    ['link', { rel: 'alternate', type: 'text/plain', title: 'llms.txt', href: `${base}llms.txt` }],
    // 全站：公司与站点的结构化数据
    ['script', { type: 'application/ld+json' }, JSON.stringify({
      '@context': 'https://schema.org',
      '@graph': [
        {
          '@type': 'Organization', '@id': site + '/#org', name: '昆泰芯微电子', alternateName: ['CONNTEK', '昆泰芯'],
          url: site + '/', logo: site + base + 'img/logo-nav-light.png',
          email: 'sales@conntek.com.cn', telephone: '+86-755-86186696',
          contactPoint: [
            { '@type': 'ContactPoint', contactType: 'sales', email: 'sales@conntek.com.cn', telephone: '+86-755-86186696', areaServed: 'Worldwide', availableLanguage: ['zh', 'en'] },
            { '@type': 'ContactPoint', contactType: 'technical support', email: 'support@conntek.com.cn', telephone: '+86-755-86006609' },
          ],
        },
        { '@type': 'WebSite', '@id': site + '/#website', url: site + '/', name: '昆泰芯微电子 CONNTEK', inLanguage: 'zh-CN', publisher: { '@id': site + '/#org' } },
      ],
    })],
  ],
  // 图片/视频/PDF 都在 public/ 下，按根路径直接引用，不走 Vite 的资源 import
  vue: { template: { transformAssetUrls: false } },
  themeConfig: {
    logo: { light: '/img/logo-nav-light.png', dark: '/img/logo-nav-dark.png', alt: 'CONNTEK 昆泰芯微电子' },
    siteTitle: false,
    nav: data.nav,
    sidebar: {
      '/products/': data.products,
      '/applications/': data.applications,
      '/basics/': data.basics,
      '/blog/': data.blog,
    },
    search: {
      provider: 'local',
      options: {
        // 中文按字切分，否则搜「编码器」匹配不到「磁编码器」
        miniSearch: {
          options: {
            tokenize: (text: string) => text.split(/[\s\-·、，。：；（）()/]+|(?<=[一-龥])(?=[一-龥])/).filter(Boolean),
          },
          searchOptions: { fuzzy: 0.2, prefix: true, boost: { title: 4, text: 2, titles: 1 } },
        },
        translations: {
          button: { buttonText: '搜索', buttonAriaLabel: '搜索' },
          modal: {
            noResultsText: '没有找到结果',
            resetButtonTitle: '清除',
            footer: { selectText: '选择', navigateText: '切换', closeText: '关闭' },
          },
        },
      },
    },
    outline: { label: '本页目录', level: [2, 2] },
    docFooter: { prev: false, next: false },
    returnToTopLabel: '回到顶部',
    sidebarMenuLabel: '目录',
    darkModeSwitchLabel: '外观',
    lightModeSwitchTitle: '切换到浅色模式',
    darkModeSwitchTitle: '切换到深色模式',
    footer: {
      message: '泉州总部 · 苏州 / 上海 / 南京 / 杭州研发中心 · 深圳运营中心　|　闽ICP备18009754号',
      copyright: '© 昆泰芯微电子 CONNTEK',
    },
  },
})
