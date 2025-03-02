import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import {BrowserRouter, Route, Routes} from "react-router-dom";

createRoot(document.getElementById('root')).render(
  <StrictMode>

          <BrowserRouter basename="/app">  {/* Указываем базовый путь */}
      <Routes>
        <Route path="/" element={<App />} />  {/* Маршрут будет доступен по /app/ */}

      </Routes>
    </BrowserRouter>
    <App />
  </StrictMode>,
)
