import { defineConfig } from 'vitepress'
import data from './sidebar.json'

// GitHub Pages 地址为 https://conntek.github.io/msite/；改部署路径时同时设置 SITE_BASE 重新跑 scripts/render.py
const base = process.env.SITE_BASE ?? '/msite/'

export default defineConfig({
  base,
  lang: 'zh-CN',
  title: '昆泰芯微电子',
  titleTemplate: ':title · 昆泰芯 CONNTEK',
  description: '昆泰芯微电子 · 智能感知世界 传递美好生活',
  cleanUrls: true,
  lastUpdated: false,
  head: [
    ['link', { rel: 'icon', type: 'image/png', href: `${base}img/logo-nav-light.png` }],
    ['meta', { name: 'theme-color', content: '#c30d23' }],
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
    },
    search: {
      provider: 'local',
      options: {
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
