# node image pull
FROM node:17.3.0

WORKDIR /usr/app

# dependencies
COPY package*.json ./
# RUN npm install -qyg nodemon@2.0.7
RUN npm install -qy

# copy app to container
COPY . .

# start server
CMD ["npm", "start"]