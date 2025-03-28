# Pull base image
FROM python:3.13-alpine


LABEL maintainer="codewithpradip"

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /code

# Install dependencies
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY ./code /code

# EXPOSE 8000

# CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]