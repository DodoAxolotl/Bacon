FROM node:20-alpine

WORKDIR /frontend

COPY . .

EXPOSE 5173

RUN npm install

CMD ["npm", "run", "dev", "--", "--host"]
