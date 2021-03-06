# Super Tracks [![CodeFactor](https://www.codefactor.io/repository/github/kardoso/supertracks/badge)](https://www.codefactor.io/repository/github/kardoso/supertracks) [![](https://img.shields.io/badge/Python-3.8.2-blue.svg)](https://www.python.org/downloads/release/python-382/) [![](https://img.shields.io/badge/Django-3.0.8-green)](https://www.djangoproject.com/) [![](https://img.shields.io/github/license/kardoso/SuperTracks.svg)](https://github.com/kardoso/SuperTracks/blob/master/LICENSE)

Super Tracks is a small and simple web application that lists music tracks from a database, showing the following columns:

- Track Name
- Artist Name
- Album Title

## Running the application

Assuming you already have Docker and Docker Compose installed, run the following command at the root folder of the repository to build and start the application:

```
docker-compose up --build
```

It'll take some time because it will set up the containers, initialize the database and the application. Go drink some water and wait.

When it's done you'll see the message `Quit the server with CONTROL-C.` and you can now access the application from the browser at http://localhost:8000/

Alternatively, you can run `docker-compose up -d` to run in the background. After it, you can run `docker-compose stop <service_name>` to stop running containers.
