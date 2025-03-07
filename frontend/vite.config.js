// import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { resolve } from 'path'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  server: {
    // port: 8991,
  },
  resolve: {
    alias: {
      // '@': fileURLToPath(new URL('./src', import.meta.url))
      '@': resolve('./src'),
    }
  },
  test: {
    testTimeout: 600000,
    environment: "happy-dom",
    setupFiles: resolve('./tests/setup.js'),
  },
})
