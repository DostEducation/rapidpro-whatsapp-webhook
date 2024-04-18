import traceback

from api import db
from api.utils.loggingutils import logger


def save(data):
    try:
        db.session.add(data)
        db.session.commit()
    except Exception as e:
        logger.error(
            "Error occurred while committing the data in the database."
            f"Error message: {e}"
        )
        logger.debug(traceback.format_exc())
        db.session.rollback()
