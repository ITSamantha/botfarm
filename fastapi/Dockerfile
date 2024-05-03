FROM python:3.9-alpine
WORKDIR /app

COPY ./requirements.txt requirements.txt
COPY ./alembic.ini alembic.ini
COPY ./migrations migrations

RUN apk update && \
    apk add build-base && \
    pip install -r requirements.txt

# RUN ["alembic", "revision", "--autogenerate"]

# RUN ["alembic", "upgrade", "heads"]

# RUN ["python", "src/database/seeders/database_seeder.py"]

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port","8000" ]
