import functions_framework

from api import app
from api.services import WebhookTransactionLogService
from api.utils.loggingutils import logger


# Endpoint for Cloud function
@functions_framework.http
def handle_payload(request):
    if request.method == "POST":
        with app.app_context():
            try:
                jsonData = request.get_json()
                if jsonData:
                    handle_webhook(jsonData)
            except Exception as e:
                logger.error(
                    f"Exception while handling the webhook payload: {jsonData}"
                    f"Error: {e}"
                )
            return "Success"
    else:
        return "Currently, the system does not accept a GET request"


def handle_webhook(jsonData):
    transaction_log_service = WebhookTransactionLogService()
    webhook_log = transaction_log_service.create_new_webhook_log(jsonData)
    transaction_log_service.mark_webhook_log_as_processed(webhook_log)
