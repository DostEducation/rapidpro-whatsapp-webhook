import json
from app.helpers import db
from app import models
from app.utils.loggingutils import logger


class WebhookTransactionLogService:
    def create_new_webhook_log(self, jsonData):
        try:
            data = json.dumps(jsonData)
            new_webhook_log = models.WebhookTransactionLog(
                payload=data,
                processed=False,
                attempts=0,
            )
            db.add(new_webhook_log)
            db.commit()
            return new_webhook_log
        except Exception as e:
            logger.error(
                f"Error while creating new webhook log. Webhook: {jsonData}. Error message: {e}"
            )
        finally:
            db.close()

    def mark_webhook_log_as_processed(self, webhook_log):
        try:
            webhook_log.processed = True
            db.add(webhook_log)
            db.commit()
        except Exception as e:
            logger.error(
                f"Error while marking webhook log as processed. Error message: {e}"
            )
        finally:
            db.close()
