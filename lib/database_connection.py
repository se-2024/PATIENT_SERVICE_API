#!/usr/bin/env python
""" Responsible for creating the connection to the database.
"""

import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()


def get_db_connection_string():
    """Get Db Connection String
    Returns:
        str: connection string
    """
    db_username = os.environ.get("username")
    db_password = os.environ.get("password")
    db_database_name = os.environ.get("dbname")
    db_host_name = os.environ.get("host")
    db_port = int(os.environ.get("port"))
    connection_string = f"postgresql+psycopg2://{db_username}:{db_password}@{db_host_name}:{db_port}/{db_database_name}"

    return connection_string


SQLALCHEMY_DATABASE_URL = get_db_connection_string()

# create a SQLAlchemy "engine".
# We will later use this engine in other places.
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Each instance of the SessionLocal class will be a database session.
# The class itself is not a database session yet.
# But once we create an instance of the SessionLocal class,
# this instance will be the actual database session.
# We name it SessionLocal to distinguish it from the
# Session we are importing from SQLAlchemy.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Inherit from this class to create each of the database models
# or classes (the ORM models):
Base = declarative_base()
