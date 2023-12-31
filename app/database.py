import sqlalchemy
from loguru import logger
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists, drop_database

from app.internal.config import DATABASE_URL, TESTING

if TESTING:
    if database_exists(DATABASE_URL):
        drop_database(DATABASE_URL)
    engine = sqlalchemy.create_engine(DATABASE_URL, pool_pre_ping=True)
    create_database(engine.url)


# Postgres Database Configuration
try:

    engine = sqlalchemy.create_engine(DATABASE_URL, pool_pre_ping=True)

    logger.success("[+] Create database engine")

except SQLAlchemyError as error:
    logger.opt(exception=True).error(f"[-] Error connecting to {DATABASE_URL}: {error}")
    raise


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
