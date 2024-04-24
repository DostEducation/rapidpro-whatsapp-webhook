"""Flask configuration."""

import os

FLASK_APP = os.environ.get("FLASK_APP", "development")

SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", None)

LOGGING_LEVEL = os.environ.get("LOGGING_LEVEL", "DEBUG")
