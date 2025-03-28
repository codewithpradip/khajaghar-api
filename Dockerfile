# Pull base image
FROM python:3.13-alpine


LABEL maintainer="codewithpradip"

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /code

#  Copy requirements
COPY ./requirements.txt .

# Install dependencies
RUN python -m venv /py && \
    pip install --upgrade pip && \
    apk add --update --upgrade --no-cache postgresql-client && \
    apk add --update --upgrade --no-cache --virtual .tmp \
        build-base postgresql-dev

RUN pip install -r /requirements.txt && apk del .tmp

# Copy project
COPY ./code /code
