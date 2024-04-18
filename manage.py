from __future__ import absolute_import

from flask.cli import FlaskGroup
from flask_migrate import Migrate

from api import app, db

migrate = Migrate(app, db)
cli = FlaskGroup(app)

if __name__ == "__main__":
    cli()
