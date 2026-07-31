FROM node:22-alpine

WORKDIR /app

COPY package*.json ./

RUN npm ci --omit=dev

COPY src ./src

RUN addgroup -S nodeapp && adduser -S nodeapp -G nodeapp

USER nodeapp

EXPOSE 3000

CMD ["npm","start"]