# DBAS 3200 Workshop 03

## Project
A Django web application running in Docker with PostgreSQL as its database.

## Requirements
- Docker Desktop
- Docker Compose

## Run the project
1. Create a local `.env` file using `.env.example` as a guide.
2. Add your own secret key and database password to `.env`.
3. Start the containers:

   `docker compose up -d --build`

4. Open http://localhost:8000

## Useful commands
- `make up` - start the application
- `make down` - stop the containers
- `make migrate` - apply database migrations
- `make logs` - view container logs

## Database
Django connects to PostgreSQL using the Compose service name `db`.
The `pgdata` named volume stores database data when containers stop or restart.
