from pathlib import Path

from starlette.config import Config

BASE_PATH = Path(__file__).resolve().parent.parent.parent.parent
MEDIA = f"{BASE_PATH}/media/"

config = Config(f"{str(BASE_PATH)}/.env")


# API
PROJECT_DESCRIPTION_API = config(
    "PROJECT_DESCRIPTION_API", cast=str, default="Desafio MaisTodos"
)
PROJECT_VERSION_API = config("PROJECT_VERSION_API", cast=str, default="0.0.1")
PROJECT_NAME_API = config("PROJECT_NAME_API", cast=str, default="MaisTodos")
PROJECT_CONTACT_API = config(
    "PROJECT_AUTHORS_API",
    cast=dict,
    default={
        "name": "Francisco Silva",
        "email": "Chicosilva1@gmail.com",
    },
)
BASIC_HEADERS = {"Content-Type": "application/json"}


# PostgreSQL Database
DATABASE_PORT = config("DATABASE_PORT", cast=int, default=5432)
DATABASE_HOST = config("DATABASE_HOST", cast=str, default="localhost")
DATABASE_NAME = config("DATABASE_NAME", cast=str, default="todos_dev")
DATABASE_USER = config("DATABASE_USER", cast=str, default="todos_dev")
DATABASE_PASS = config("DATABASE_PASS", cast=str, default="todos_dev")

TESTING = config("TESTING", cast=bool, default=False)
TESTING_TEMPORAL_DATABASE = "postgres"

if TESTING:
    DATABASE_NAME += "_test"

DATABASE_URL = config(
    "DATABASE_URL",
    cast=str,
    default=f"postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASS}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}",
)

DATABASE_SCHEMA = config("DATABASE_SCHEMA", cast=str, default="public")

# MODE for environment
MODE = config("MODE", cast=str, default="DEV")


# Gunicorn
GUNICORN_BIND = config("GUNICORN_BIND", cast=str, default="0.0.0.0:8000")
GUNICORN_WORKER_CLASS = config(
    "GUNICORN_WORKER_CLASS", cast=str, default="uvicorn.workers.UvicornWorker"
)
GUNICORN_WORKERS_PER_CORE = config("GUNICORN_WORKERS_PER_CORE", cast=int, default=1)
GUNICORN_WORKERS = config("GUNICORN_WORKERS", cast=int, default=0)
GUNICORN_KEEPALIVE = config("GUNICORN_KEEPALIVE", cast=int, default=5)
GUNICORN_GRACEFUL_TIMEOUT = config("GUNICORN_GRACEFUL_TIMEOUT", cast=int, default=120)
GUNICORN_TIMEOUT = config("GUNICORN_TIMEOUT", cast=int, default=120)

JWT_SECRET = config("JWT_SECRET", default="todos_dev")
JWT_ALGORITHM = config("JWT_ALGORITHM", default="HS256")
