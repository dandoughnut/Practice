CREATE DATABASE "AdventureWorks"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

CREATE USER etl WITH PASSWORD 'demopass';

GRANT CONNECT ON DATABASE ""

/*
WEATHER OBSERVATION 5
*/
(
    SELECT city, LENGTH(city)
    FROM station
    ORDER BY LENGTH(city), city
    LIMIT 1
)
UNION
(
    SELECT city, LENGTH(city)
    FROM station
    ORDER BY LENGTH(city) DESC, city
    LIMIT 1
)