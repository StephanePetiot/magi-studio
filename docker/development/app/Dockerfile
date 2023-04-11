# Base off the official python image
# Define a common stage for dev and prod images called base
FROM python:3.10-slim
# Set environment variables
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
  && pip install --no-cache-dir psycopg2 \
  # cleaning up unused files to reduce the image size
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*
# Create a directory for the source code and use it as base path
WORKDIR /code/
USER root
# Copy the python depencencies list for pip
COPY --chown=app:app requirements/ requirements/
# Install python packages at system level
RUN pip install --no-cache-dir -r requirements/local.txt
# Copy entrypoint script which waits for the db to be ready
COPY --chown=app:app docker/development/app/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
# Copy the scripts that starts the development application server (runserver)
COPY --chown=app:app docker/development/app/start-dev-server.sh /usr/local/bin/start-dev-server.sh
RUN chmod +x /usr/local/bin/start-dev-server.sh

RUN chown -R app:app /code/

ARG media_root
RUN chown -R app:app $media_root

USER app
# This script will run before every command executed in the container
ENTRYPOINT ["entrypoint.sh"]
CMD ["start-dev-server.sh"]
