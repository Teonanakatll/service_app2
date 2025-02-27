import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],

    host: 'localhost',
    server: {
    port: 3000,  // Здесь укажи порт, который тебе нужен
  },

})
