FROM node:19-alpine as static-build
WORKDIR /code/
COPY frontend/ frontend/
WORKDIR /code/frontend/
RUN apk update \
    && apk add --no-cache --virtual .build-deps python3 make g++ git \
    && npm install \
    && apk del .build-deps
RUN ["npm", "run", "production"]


FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1

# Create a user to avoid running containers as root in production
# Need to specify UID/GID to avoid permission issues on mounted volumes
RUN addgroup --system --gid 1000 app  \
    && adduser --system --ingroup app --uid 1000 app
# Install os-level dependencies (as root)
RUN apt-get update && apt-get install -y -q --no-install-recommends \
  # dependencies for building Python packages
  build-essential \
  # postgress client (psycopg2) dependencies
  libpq-dev \
  # Dependency needed for celery autoreload management command
  procps \
  # For I18N and L10N
  gettext \
  && pip install --no-cache-dir psycopg2 \
  # cleaning up unused files to reduce the image size
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*
# Create a directory for the source code and use it as base path
WORKDIR /code/
# TO DO : REVIEW THIS PART, NOT SUPPOSED TO KNOW WHERE THE STATIC AND MEDIA ROOT ARE SUPPOSED TO BE
USER root
RUN mkdir -p /var/www/static/ && chown -R app:app /var/www/static/
RUN mkdir -p /var/www/media/ && chown -R app:app /var/www/media/
# Copy the python depencencies list for pip
COPY --chown=app:app requirements/ requirements/
# Install python packages at system level
RUN pip install --no-cache-dir -r requirements/base.txt
# Copy the script that prepare the production application
COPY --chown=app:app docker/production/app/prepare-production.sh /usr/local/bin/prepare-production.sh
RUN chmod +x /usr/local/bin/prepare-production.sh
COPY --chown=app:app docker/production/app/start-gunicorn-server.sh /usr/local/bin/start-gunicorn-server.sh
RUN chmod +x /usr/local/bin/start-gunicorn-server.sh
COPY --chown=app:app docker/production/app/start-daphne-server.sh /usr/local/bin/start-daphne-server.sh
RUN chmod +x /usr/local/bin/start-daphne-server.sh
# Copy celery worker script
COPY --chown=app:app docker/production/app/start-celery-worker.sh /usr/local/bin/start-celery-worker.sh
RUN chmod +x /usr/local/bin/start-celery-worker.sh
# Copy the source code of our django app to the working directoy
USER app
COPY --chown=app:app app/ app/
COPY --chown=app:app config/ config/
COPY --chown=app:app manage.py manage.py
COPY --from=static-build --chown=app:app /code/frontend/build /code/frontend/build
COPY --from=static-build --chown=app:app /code/frontend/templates /code/frontend/templates
COPY --from=static-build --chown=app:app /code/frontend/webpack-stats.json /code/frontend/webpack-stats.json
CMD ["prepare-production.sh"]
