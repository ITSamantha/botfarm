

# Запуск приложения

```
docker compose build
```

```
docker compose up
```

```
docker-compose run --rm backend alembic revision --autogenerate
```

```
docker-compose run --rm backend alembic upgrade head
```