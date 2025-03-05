import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({

  // plugins: [react({fastRefresh: true,})],
  plugins: [react()],
    server: {
    port: 3000,  // Здесь укажи порт, который тебе нужен
    host: '0.0.0.0',  // Добавьте эту строку
    // hmr: {
    //   overlay: true,  // Показывать уведомления об ошибках в браузере
    // },
  },
  base: '/app/',
})