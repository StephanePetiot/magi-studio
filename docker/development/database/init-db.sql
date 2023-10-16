\set DB_NAME `echo "\"$DB_NAME\""`
\set DB_USER `echo "\"$DB_USER\""`
\set DB_PASSWORD `echo "'$DB_PASSWORD'"`

-- as postgres user
-- Create the database for your application
CREATE DATABASE :DB_NAME;
-- Create the dedicated user
CREATE USER :DB_USER WITH PASSWORD :DB_PASSWORD;
ALTER DATABASE :DB_NAME OWNER TO :DB_USER;

-- Connect to mydb
\connect :DB_NAME;

-- Set some settings as recommended by the Django documentation
ALTER ROLE :DB_USER SET client_encoding TO 'utf8';
ALTER ROLE :DB_USER SET default_transaction_isolation TO 'read committed';
ALTER ROLE :DB_USER SET timezone TO 'UTC';