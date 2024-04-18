import traceback

import psycopg2

from api import app, db
from api.utils.loggingutils import logger


def get_db_connection(connection_data={}):
    db_name = connection_data.get("db_name", app.config["DB_NAME"])
    db_user = connection_data.get("db_user", app.config["DB_USER"])
    db_host = connection_data.get("db_host", app.config["DB_HOST"])
    db_pwd = connection_data.get("db_pwd", app.config["DB_PWD"])

    db_conn_string = f"dbname={db_name} user={db_user} host={db_host} password={db_pwd}"

    try:
        return psycopg2.connect(db_conn_string)
    except Exception as e:
        logger.error(
            f"DB Helper: Unable to connect to the database: {db_conn_string}. Error message:{e}"
        )
        return None


def save(data):
    try:
        db.session.add(data)
        db.session.commit()
    except Exception as e:
        logger.error(
            f"Error occurred while committing the data in the database. Error message: {e}"
        )
        logger.debug(traceback.format_exc())
        db.session.rollback()
