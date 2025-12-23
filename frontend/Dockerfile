# Використовуємо офіційний Node.js образ
FROM node:20-alpine

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо package.json та package-lock.json (якщо існує)
COPY movie-catalog/package*.json ./

# Встановлюємо залежності
RUN npm install

# Копіюємо весь код проєкту
COPY movie-catalog/ ./

# Відкриваємо порт
EXPOSE 8090

# Запускаємо dev сервер
CMD ["npm", "run", "dev"]
