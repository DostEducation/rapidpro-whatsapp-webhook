from datetime import datetime, timedelta

from api import models
from api.utils import db_utils
from api.utils.loggingutils import logger


class FlowRunLogService:
    def __init__(self, user):
        self.user = user
        self.class_model = models.UserFlows

    def create_user_flow_log(self, json_data):
        try:
            flow_uuid = json_data.get("flow_uuid")
            flow_name = json_data.get("flow_name")
            flow_type = json_data.get("flow_type")
            flow_completed = json_data.get("flow_completed")

            today_flow_log = self.class_model.query.get_by_flow_uuid_and_phone(
                flow_uuid, self.user.phone
            )

            user_flow_log = None

            if not today_flow_log:
                user_flow_log = self.create_log(flow_uuid, flow_name, flow_type)
            elif today_flow_log and flow_completed:
                user_flow_log = self.update_log(today_flow_log)

            return user_flow_log
        except Exception as e:
            logger.error(
                f"Error while creating new user flow log. json data: {json_data}."
                f"Error message: {e}"
            )
            raise

    def create_log(self, flow_uuid, flow_name, flow_type):
        user_flow_log = self.class_model(
            user_id=self.user.id,
            user_phone=self.user.phone,
            flow_uuid=flow_uuid,
            flow_name=flow_name,
            flow_type=flow_type,
            flow_run_status=self.class_model.FlowRunStatus.IN_PROGRESS,
            flow_start_time=datetime.utcnow() + timedelta(minutes=330),
            is_active=True,
        )

        db_utils.save(user_flow_log)
        logger.info(f"Created a user flow log for phone number {self.user.phone}.")
        return user_flow_log

    def update_log(self, today_flow_log):
        today_flow_log.flow_run_status = self.class_model.FlowRunStatus.COMPLETED
        today_flow_log.flow_end_time = datetime.utcnow() + timedelta(minutes=330)
        today_flow_log.is_active = False

        db_utils.save(today_flow_log)
        logger.info(f"Updated user flow log for phone number {self.user.phone}.")
        return today_flow_log
