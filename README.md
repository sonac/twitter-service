## Twitter service

Simple service for getting twitter feed for user and retrieveing afterwards simple information regarding it (average length of tweet or follower with biggest amount of followers)

## Building

For building and running it independently simply run `docker build .` and then run it with proper environment variables and postgres database configured somewhere.

For local run simply use `docker-compose up` but don't forget to properly set all needed environment variables in your system beforehand. List is below:
```
CONSUMER_KEY
CONSUMER_SECRET
ACCESS_TOKEN
ACCESS_TOKEN_SECRET
POSTGRES_DB
POSTGRES_PASSWORD
POSTGRES_USER
POSTGRES_PORT
```
Postgres host is not needed as its being set inside docker-compose but you will need it if you will run it out of it.

## Testing

For testing properly create virtual environment with all packages installed (you can use `pyenv` for that purpose) and run `python -m pytest` to run unit tests.
