\set DB_NAME `echo "\"$DB_NAME\""`
\set DB_USER `echo "\"$DB_USER\""`
\set DB_PASSWORD `echo "'$DB_PASSWORD'"`

CREATE DATABASE :DB_NAME;
CREATE USER :DB_USER WITH PASSWORD :DB_PASSWORD;
ALTER ROLE :DB_USER SET client_encoding TO 'utf8';
ALTER ROLE :DB_USER SET default_transaction_isolation TO 'read committed';
ALTER ROLE :DB_USER SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE :DB_NAME TO :DB_USER;