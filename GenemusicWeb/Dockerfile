# Create image based on the official Node 6 image from dockerhub
FROM node:8

# Change directory so that our commands run inside this new directory
WORKDIR /usr/src/genemusic-app

# Copy dependency definitions
COPY package.json ./

# Install dependecies
RUN npm install

# Get all the code needed to run the app
COPY . .

# Expose the port the app runs in
EXPOSE 8080

# Serve the app
CMD ["npm", "run", "start:dev"]