#!/bin/sh

echo "DB Connection --- Establishing . . ."

while ! nc -z "$DATABASE_HOST" 5432; do

    echo "DB Connection -- Failed!"

    sleep 1

    echo "DB Connection -- Retrying . . ."

done

echo "DB Connection --- Successfully Established!"

echo "Alembic --- Run migrations!"
alembic upgrade heads

echo "Gunicorn --- Start app!"
uvicorn app.main:application --host 0.0.0.0