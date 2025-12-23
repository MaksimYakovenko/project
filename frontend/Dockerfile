FROM node:20-alpine

WORKDIR /app

COPY movie-catalog/package*.json ./

RUN npm install

COPY movie-catalog/ ./

RUN chmod -R 755 /app && \
    chmod -R 755 /app/node_modules/.bin

EXPOSE 8090

CMD ["npm", "run", "dev"]
