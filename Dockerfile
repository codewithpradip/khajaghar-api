FROM python:3.13-alpine

LABEL maintainer="codewithpradip"

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /code

COPY ./requirements.txt .

RUN apk add --update --upgrade --no-cache \
        postgresql-client \
        build-base \
        postgresql-dev && \
    python -m venv /py && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    apk del build-base postgresql-dev

COPY ./code /code