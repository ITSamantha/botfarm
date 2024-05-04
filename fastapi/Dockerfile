FROM python:3.9-alpine
WORKDIR /app

COPY . .
COPY ./entrypoint.sh entrypoint.sh

RUN apk update && \
    apk add build-base && \
    pip install -r requirements.txt

RUN ["chmod", "+x", "entrypoint.sh"]

ENTRYPOINT ["sh", "entrypoint.sh"]
