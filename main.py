import functions_framework

from api import app
from api.services import UserCreationService, WebhookTransactionLogService
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
    contact_data = jsonData["contact"]
    if contact_data:
        handle_contact_field_data(contact_data)

    transaction_log_service.mark_webhook_log_as_processed(webhook_log)


def handle_contact_field_data(contact_data):
    user_creation_service = UserCreationService()
    user_creation_service.create_new_user(contact_data)
