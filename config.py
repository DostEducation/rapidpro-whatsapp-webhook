"""Flask configuration."""

import os

FLASK_ENV = os.environ.get("FLASK_ENV", "development")

if FLASK_ENV == "development":
    from dotenv import load_dotenv

    load_dotenv()

SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", None)

LOGGING_LEVEL = os.environ.get("LOGGING_LEVEL", "DEBUG")
