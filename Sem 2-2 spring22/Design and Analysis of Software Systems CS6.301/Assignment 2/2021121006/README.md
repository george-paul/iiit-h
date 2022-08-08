# README

## DASS - Assignment 2 - Dockerizing

The app created in Assignment 1 was dockerized into four containers: 

* The frontend container which starts a server that serves the web pages.
* The backend container which starts the server that serves API requests, mainly with the help of the database server.
* The database container that manages the database for the app and helps the backend.
* The `nginx` container that routes all the http requests to the appropriate URLs depending on the user's needs.

### How to

* How to start the containers:

```
docker-compose start
```

* How to run and test the app:
  * Open a web browser
  * Navigate to `localhost:3050`



