import { defineConfig } from 'vitepress'
import sidebar from './sidebar.json'

// GitHub Pages 地址为 https://conntek.github.io/msite/；改部署路径时同时设置 SITE_BASE 重新跑 scripts/build.py
const base = process.env.SITE_BASE ?? '/msite/'

export default defineConfig({
  base,
  lang: 'zh-CN',
  title: '昆泰芯微电子',
  description: 'CONNTEK 官网内容本地镜像 · 智能感知世界 传递美好生活',
  cleanUrls: true,
  lastUpdated: false,
  head: [['link', { rel: 'icon', href: `${base}images/logo.jpg` }]],
  // 图片/视频/PDF 都在 public/ 下，按根路径直接引用，不走 Vite 的资源 import（缺文件也不会整页报错）
  vue: { template: { transformAssetUrls: false } },
  themeConfig: {
    logo: '/images/logo.jpg',
    siteTitle: '昆泰芯 CONNTEK',
    nav: [
      { text: '首页', link: '/' },
      { text: '产品中心', link: '/products/', activeMatch: '^/products/' },
      { text: '市场应用', link: '/applications/', activeMatch: '^/applications/' },
      { text: '磁仿真&技术服务', link: '/services' },
      { text: '技术洞见', link: '/tech-talks' },
      { text: '关于我们', link: '/about/' },
      { text: '联系我们', link: '/contact' },
    ],
    sidebar: {
      '/products/': sidebar.products,
      '/applications/': sidebar.applications,
    },
    search: {
      provider: 'local',
      options: {
        translations: {
          button: { buttonText: '搜索', buttonAriaLabel: '搜索' },
          modal: { noResultsText: '没有找到结果', resetButtonTitle: '清除', footer: { selectText: '选择', navigateText: '切换', closeText: '关闭' } },
        },
      },
    },
    outline: { label: '本页目录' },
    docFooter: { prev: '上一页', next: '下一页' },
    returnToTopLabel: '回到顶部',
    sidebarMenuLabel: '菜单',
    darkModeSwitchLabel: '外观',
    footer: {
      message: '闽ICP备18009754号',
      copyright: '© 昆泰芯微电子',
    },
  },
})
