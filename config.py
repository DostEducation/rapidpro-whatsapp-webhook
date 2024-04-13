import os

# Database configuration
POSTGRES = {
    "user": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASSWORD"),
    "database": os.environ.get("DB_NAME"),
    "host": os.environ.get("DB_HOST"),
    "port": os.environ.get("DB_PORT"),
}

SQLALCHEMY_DATABASE_URL = (
    "postgresql://%(user)s:%(password)s@%(host)s:%(port)s/%(database)s" % POSTGRES
)
