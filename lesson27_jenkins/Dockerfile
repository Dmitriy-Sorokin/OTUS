FROM python:3.8-alpine

WORKDIR /app

COPY poetry.lock poetry.lock
RUN poetry add -U poetry && poetry add -r poetry.lock

COPY . .

ENTRYPOINT ["pytest"]
