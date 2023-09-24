#!/bin/sh

echo "Alembic --- Run migrations!"
alembic upgrade heads

echo "Gunicorn --- Start app!"
uvicorn app.main:application --host 0.0.0.0 --port 8000