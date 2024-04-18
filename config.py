"""Flask configuration."""

import os

FLASK_APP = os.environ.get("FLASK_APP", "development")

if FLASK_APP == "development":
    from dotenv import load_dotenv

    load_dotenv()


# Database configuration
POSTGRES = {
    "user": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASSWORD"),
    "database": os.environ.get("DB_NAME"),
    "host": os.environ.get("DB_HOST"),
    "port": os.environ.get("DB_PORT"),
    "conn_str": os.environ.get("CONNECTION_NAME"),
}

SQLALCHEMY_DATABASE_URI = (
    "postgresql://%(user)s:%(password)s@%(host)s:%(port)s/%(database)s"
    % POSTGRES
)

# For socket based connection
if FLASK_APP in ("production", "staging"):
    SQLALCHEMY_DATABASE_URI = (
        "postgresql://%(user)s:%(password)s@/%(database)s?host=%(conn_str)s/"
        % POSTGRES
    )

LOGGING_LEVEL = os.environ.get("LOGGING_LEVEL", "DEBUG")
