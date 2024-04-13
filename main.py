from fastapi import FastAPI
from agraffe import Agraffe
from app.services import WebhookTransactionLogService

app = FastAPI()


def handle_payload(request):
    if request.method == "POST":
        try:
            jsonData = request.get_json()
            if jsonData:
                handle_webhook(jsonData)
        except Exception as e:
            print(f"Error: {e}")
        return jsonData
    else:
        return "System does not accepts GET request"


def handle_webhook(jsonData):
    transaction_log_service = WebhookTransactionLogService()
    webhook_log = transaction_log_service.create_new_webhook_log(jsonData)
    transaction_log_service.mark_webhook_log_as_processed(webhook_log)


handler = Agraffe.entry_point(app)
