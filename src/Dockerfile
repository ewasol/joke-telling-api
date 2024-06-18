FROM python:3.11-alpine
ENV FLASK_APP=joke_api.run
WORKDIR /src
ENV PYTHONPATH=../
COPY requirements-dev.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements-dev.txt
COPY joke_api/ joke_api/
