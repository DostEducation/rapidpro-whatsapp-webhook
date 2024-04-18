"""Flask configuration."""

import os

FLASK_APP = os.environ.get("FLASK_APP", "development")

if FLASK_APP == "development":
    from os import path

    from dotenv import load_dotenv

    basedir = path.abspath(path.dirname(__file__))
    load_dotenv(path.join(basedir, ".env"))


# Database configuration
POSTGRES = {
    "user": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASSWORD"),
    "database": os.environ.get("DB_NAME"),
    "host": os.environ.get("DB_HOST"),
    "port": os.environ.get("DB_PORT"),
    "connection_name": os.environ.get("CONNECTION_NAME"),
}

SQLALCHEMY_DATABASE_URI = (
    "postgresql://%(user)s:%(password)s@%(host)s:%(port)s/%(database)s" % POSTGRES
)

# For socket based connection
if FLASK_APP in ("production", "staging"):
    SQLALCHEMY_DATABASE_URI = (
        "postgresql://%(user)s:%(password)s@/%(database)s?host=%(connection_name)s/"
        % POSTGRES
    )
