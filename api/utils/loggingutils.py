import logging
import os

from google.cloud import logging as gcloud_logging

from api import app
from config import LOGGING_LEVEL

logger = logging.getLogger()
logging.basicConfig(level=LOGGING_LEVEL)

if os.environ.get("FLASK_ENV", "development"):
    log_handler = logger.handlers[0]
    logger.addHandler(log_handler)
else:
    log_client = gcloud_logging.Client()
    log_client.setup_logging()
    log_handler = log_client.get_default_handler()
    app.logger.addHandler(log_handler)
