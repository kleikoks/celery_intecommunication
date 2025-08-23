# Hehe

## Showing the intercommunication of two celery apps using shared redis instance

Remarks to better understanding:
- Service A runs only on `--queues=A`, when service B runs on `--queues=B`
- Consuming other service message happens via `name` parameter. It should be in shared Enum.

**Start docker compose A service**
```shell
docker compose -f A_docker-compose.yaml up --build -d
```

**Start docker compose B service**
```shell
docker compose -f B_docker-compose.yaml up --build -d
```
