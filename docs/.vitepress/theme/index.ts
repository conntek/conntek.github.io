import DefaultTheme from 'vitepress/theme'
import type { Theme } from 'vitepress'
import './style.css'
import './layout.css'
import './mountains.css'
import './wiki.css'
import './blog.css'

// 侧栏在宽屏下是绝对定位（跟随页面滚动），不参与排版；页脚又是全宽的。
// 量出侧栏实际高度写进 --c-sidebar-h，让正文区至少与侧栏等高，页脚就永远排在两者下面、不压住侧栏末尾。
function trackSidebarHeight() {
  if (typeof window === 'undefined') return
  const root = document.documentElement
  let observed: Element | null = null
  const ro = new ResizeObserver(() => update())
  function update() {
    const sb = document.querySelector('.VPSidebar') as HTMLElement | null
    if (sb !== observed) {
      if (observed) ro.unobserve(observed)
      if (sb) ro.observe(sb)
      observed = sb
    }
    const h = sb && getComputedStyle(sb).position === 'absolute' ? sb.offsetHeight : 0
    root.style.setProperty('--c-sidebar-h', h ? `${h}px` : '0px')
  }
  // 侧栏会随路由切换、折叠展开而重建或变高：观察 DOM 变化再重新挂 ResizeObserver
  new MutationObserver(() => update()).observe(document.body, { childList: true, subtree: true })
  window.addEventListener('resize', update)
  update()
}

export default {
  extends: DefaultTheme,
  enhanceApp() {
    if (typeof window !== 'undefined') {
      window.addEventListener('DOMContentLoaded', trackSidebarHeight)
      if (document.readyState !== 'loading') trackSidebarHeight()
    }
  },
} satisfies Theme
