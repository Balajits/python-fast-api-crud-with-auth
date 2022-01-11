import os
from dotenv import load_dotenv, find_dotenv

from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker


load_dotenv(find_dotenv())


DB_CONNECTION= os.environ.get("DB_CONNECTION")
DB_HOST= os.environ.get("DB_HOST")
DB_PORT= os.environ.get("DB_PORT")
DB_DATABASE= os.environ.get("DB_DATABASE")
DB_USERNAME= os.environ.get("DB_USERNAME")
DB_PASSWORD= os.environ.get("DB_PASSWORD")

SQLALCHEMY_DATABASE_URL = f'{DB_CONNECTION}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}'


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
