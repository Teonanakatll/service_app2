FROM node:20 as build

# Установка рабочей директории
WORKDIR /app

# Копирование package.json и package-lock.json
COPY package*.json ./

# Установка зависимостей
RUN npm install

# Копирование остальных файлов
COPY . .

RUN npm run build

# Экспозиция порта
EXPOSE 3000

# Запуск приложения
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]