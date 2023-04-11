FROM node:19-alpine as static-build
WORKDIR /code/frontend
COPY ./frontend ./
RUN apk update \
    && apk add --no-cache --virtual .build-deps python3 make g++ git \
    && npm install \
    && apk del .build-deps
RUN ["npm", "run", "build"]


FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1

# Create a user to avoid running containers as root in production
# Need to specify UID/GID to avoid permission issues on mounted volumes
RUN addgroup --system --gid 1000 app  \
    && adduser --system --ingroup app --uid 1000 app
WORKDIR /code
RUN mkdir app static media && chown -R app:app .
# Install os-level dependencies (as root)
RUN apt-get update && apt-get install -y -q --no-install-recommends \
  # dependencies for building Python packages
  build-essential \
  # postgress client (psycopg2) dependencies
  libpq-dev \
  # Dependency needed for celery autoreload management command
  procps \
  && pip install --no-cache-dir psycopg2 \
  # cleaning up unused files to reduce the image size
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*
# Create a directory for the source code and use it as base path
WORKDIR /code/
USER root
# Copy the python depencencies list for pip
COPY --chown=app:app ./requirements /requirements/
# Install python packages at system level
RUN pip install --no-cache-dir -r requirements/base.txt
RUN ["python", "-c", "import nltk; nltk.download(['stopwords', 'punkt'], download_dir='/usr/local/nltk_data')" ]
# Copy entrypoint script which waits for the db to be ready
COPY --chown=app:app ./docker/staging/app/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
# Copy the script that starts the staging application server
COPY --chown=app:app ./docker/staging/app/prepare-staging.sh /usr/local/bin/prepare-staging.sh
RUN chmod +x /usr/local/bin/prepare-staging.sh
COPY --chown=app:app ./docker/staging/app/start-gunicorn-server.sh /usr/local/bin/start-gunicorn-server.sh
RUN chmod +x /usr/local/bin/start-gunicorn-server.sh
COPY --chown=app:app ./docker/staging/app/start-daphne-server.sh /usr/local/bin/start-daphne-server.sh
RUN chmod +x /usr/local/bin/start-daphne-server.sh
# Copy celery worker script
COPY --chown=app:app ./docker/staging/app/start-celery-worker.sh /usr/local/bin/start-celery-worker.sh
RUN chmod +x /usr/local/bin/start-celery-worker.sh
# Copy the source code of our django app to the working directoy
USER app
COPY --chown=app:app ./app ./
COPY --from=static-build --chown=app:app /code/frontend/build /code/frontend/build
COPY --from=static-build --chown=app:app /code/frontend/webpack-stats.json /code/frontend/webpack-stats.json
# This script will run before every command executed in the container
ENTRYPOINT ["entrypoint.sh"]
CMD ["prepare-staging.sh"]
