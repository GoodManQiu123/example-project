FROM node:20 as build-stage

WORKDIR /frontend

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

# run the app in a nginx server
FROM nginx:stable as prod-stage

COPY --from=build-stage /frontend/dist/ /usr/share/nginx/html/

COPY default.conf /etc/nginx/conf.d/default.conf

RUN ["ls", "/etc/nginx/conf.d"]
RUN ["cat", "/etc/nginx/nginx.conf"]
RUN ["cat", "/etc/nginx/conf.d/default.conf"]

EXPOSE 5173

CMD ["nginx", "-g", "daemon off;"]
