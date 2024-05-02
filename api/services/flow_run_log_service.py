from api import models
from api.utils import db_utils
from api.utils.loggingutils import logger


class FlowRunLogService:
    def __init__(self, user, flow_uuid, flow_name, flow_type):
        self.user = user
        self.flow_uuid = flow_uuid
        self.flow_name = (flow_name,)
        self.flow_type = (flow_type,)
        self.class_model = models.UserFlows

    def create_user_flow_log(self, json_data):
        try:
            user_flow_log = self.create_log(json_data)

            logger.info(f"Created a user flow log for phone number {self.user.phone}.")

            return user_flow_log
        except Exception as e:
            logger.error(
                f"Error while creating new user flow log. json data: {json_data}."
                f"Error message: {e}"
            )

    def create_log(self, json_data):
        flow_uuid = (json_data["flow_uuid"],)
        flow_name = (json_data["flow_name"],)
        flow_type = (json_data["flow_type"],)

        user_flow_log = self.class_model(
            user_id=self.user.id,
            user_phone=self.user.phone,
            flow_uuid=flow_uuid,
            flow_name=flow_name,
            flow_type=flow_type,
        )

        db_utils.save(user_flow_log)
        return user_flow_log
