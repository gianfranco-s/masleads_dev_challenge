
## Set up local PostgreSQL
```
$ sudo -u postgres psql
```

```
postgres=# DROP DATABASE masleads;
postgres=# DROP ROLE masleads;

postgres=# CREATE ROLE masleads WITH PASSWORD 'masleads-pwd';
postgres=# ALTER ROLE masleads WITH LOGIN;
postgres=# CREATE DATABASE masleads WITH OWNER masleads;
postgres=# \c masleads
postgres=# GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE "ElementsToProcess" TO masleads;
postgres=# GRANT USAGE ON SCHEMA public TO masleads;
postgres=# GRANT USAGE, SELECT ON SEQUENCE "ElementsToProcess_id_seq" TO masleads;
```


## Run the project locally
In the project's root directory:
```
export IS_DEV=1 && (cd web/ && python -m flask run)
```

## Run the project with docker compose
In the project's root directory:
```
sudo docker compose --env-file docker.env up --build
```

## Run tests
```
(cd web/ && pytest)
```
