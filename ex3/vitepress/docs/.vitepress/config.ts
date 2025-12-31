import { defineConfig } from 'vitepress'

export default defineConfig({
  appearance: 'dark',
  themeConfig: {
    logo: '/logo.png',
    nav: [
      { text: 'בית', link: '/' },
      { text: 'התקנה', link: '/install' }
    ]
  }
  
})
console.log('VitePress config loaded');
