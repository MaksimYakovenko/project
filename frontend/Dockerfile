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

# Встановлюємо правильні права доступу
RUN chown -R node:node /app

# Переключаємось на непривілейованого користувача
USER node

# Відкриваємо порт
EXPOSE 5173

# Запускаємо dev сервер з доступом для всіх мереж використовуючи npx
CMD ["npx", "vite", "--host", "0.0.0.0"]
