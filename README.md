# Soundbook

By Sean Pan - https://sound-book.herokuapp.com/

This is the README for the final solo project from App Academy.
The project was inspired by Facebook and built using Javascript,
React.js and Redux for the front end and Python with Flask for the backend.

# Project Installation

1. Clone the project repository from https://github.com/span9692/Soundbook

2. Rename the folder to whatever you want.

3. Install dependencies

      ```
      pipenv install --dev -r dev-requirements.txt && pipenv install -r requirements.txt
      ```

4. Create a **.env** file based on the example with proper settings for your
   development environment
5. Setup your PostgreSQL user, password and database and make sure it matches your **.env** file

6. Get into your pipenv, migrate your database, seed your database, and run your flask app

   ```
   pipenv shell
   ```

   ```
   flask db upgrade
   ```

   ```
   flask seed all
   ```

   ```
   flask run
   ```

7. To run the React App in development, checkout the [README](./react-app/README.md) inside the `react-app` directory OR `cd` into the `react-app` folder and run `npm install` to install node package manager dependencies.

***
*IMPORTANT!*
   If you add any python dependencies to your pipfiles, you'll need to regenerate your requirements.txt before deployment.
   You can do this by running:

   ```
   pipenv lock -r > requirements.txt
   ```
   

*ALSO IMPORTANT!*
   psycopg2-binary MUST remain a dev dependency because you can't install it on apline-linux.
   There is a layer in the Dockerfile that will install psycopg2 (not binary) for us.
***



# Running Locally
>To start the server, run `flask run` from the root directory, then run `npm start` from the `react-app` directory. This will allow you to make requests to http://localhost:3000 using any client (browser and Postman).
>To stop the server from listening to requests, press CTRL + c for Windows/Linux or CMD + c for MacOS in the terminal that you started the server (wherever you >ran npm start).

# Running Live
>The live link for this project is located here: https://sound-book.herokuapp.com/

# Soundbook at a Glance

Soundbook is a fullstack app that allows artists to connect with one another all over the world. Artists can customize their profile pages by creating posts, adding photos, and updating their personal info. By connecting with other artists, artists can see, comment, and like each other's posts. 

![feed](https://res.cloudinary.com/photofinder/image/upload/v1640727220/Capture_a9jsms.jpg)

![profile](https://res.cloudinary.com/photofinder/image/upload/v1640727298/Capture_anqka6.jpg)

# Frontend Overview
Javascript
React
Redux

# Backend Overview
Python
PostgreSQL
Flask
