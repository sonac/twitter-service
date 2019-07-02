FROM python:3.7-alpine

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

COPY . /app

WORKDIR /app

RUN pip install --no-cache-dir pipenv && pipenv install --system

RUN chmod +x entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["./entrypoint.sh"]