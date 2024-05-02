import functions_framework

from api import app
from api.services import (
    UserActivitiesService,
    UserCreationService,
    UserIndicatorResponseService,
    WebhookTransactionLogService,
)
from api.utils.loggingutils import logger


# Endpoint for Cloud function
@functions_framework.http
def handle_payload(request):
    if request.method == "POST":
        with app.app_context():
            try:
                json_data = request.get_json()
                if not json_data:
                    return "The request cannot be processed", 400

                handle_webhook(json_data)
                return "Success", 200
            except Exception as e:
                logger.error(
                    f"Exception while handling the webhook payload: {json_data}"
                    f"Error: {e}"
                )
            return "Success", 200
    else:
        return (
            "HTTP method used for the request is not valid at the requested URL",
            405,
        )


def handle_webhook(json_data):
    transaction_log_service = WebhookTransactionLogService()
    webhook_log = transaction_log_service.create_new_webhook_log(json_data)

    contact_data = json_data["contact"]
    if contact_data:
        user = handle_contact_field_data(contact_data)
        handle_flow_activity_data(user, json_data)
        process_user_indicators(user, json_data)

    transaction_log_service.mark_webhook_log_as_processed(webhook_log)


def handle_contact_field_data(contact_data):
    user_creation_service = UserCreationService()
    return user_creation_service.create_new_user(contact_data)


def process_user_indicators(
    user,
    json_data,
):

    user_flow_id = (
        1  # Placeholder for user_flow_id, should be obtained from user_flow details.
    )
    user_indicator_res_service = UserIndicatorResponseService(user, user_flow_id)
    user_indicator_res_service.process_user_indicator_responses(json_data)


def handle_flow_activity_data(user, json_data):
    user_flow_id = (
        1  # Placeholder for user_flow_id, should be obtained from user_flow details.
    )
    user_activities_service = UserActivitiesService(user, user_flow_id)
    user_activities_service.handle_user_activities(json_data)
