from datetime import datetime
from typing import Dict, Any

from api import db, models
from api.helpers import common_helper
from api.utils.loggingutils import logger


class UserActivitiesService:
    def __init__(self, user, user_flow):
        self.user_id = user.id
        self.user_phone = user.phone
        self.user_flow_id = user_flow.id
        self.started = "flow_started"
        self.success = "flow_suceeded"
        self.completed = "flow_completed"
        self.class_model = models.UserActivities

    def handle_user_activities(self, json_data: Dict[str, Any]):
        try:
            current_ist_time = common_helper.get_ist_timestamp()
            contact_activities = json_data.get("contact", {}).get("fields", {})

            for activity_key, _ in contact_activities.items():
                if activity_key.strip() in contact_activities:
                    user_activity = self.create_or_update_user_activity(
                        activity_key, current_ist_time
                    )
                    if user_activity:
                        db.session.add(user_activity)

            db.session.commit()
            logger.info(f"Captured user activity for {self.user_phone}.")
        except Exception as e:
            logger.error(
                f"Error while capturing user activity for {self.user_phone}."
                f"Error message: {e}"
            )

    def create_or_update_user_activity(
        self, activity_key: str, current_ist_time: datetime
    ):
        is_started = self.started in activity_key
        is_succeeded = self.success in activity_key
        is_completed = self.completed in activity_key

        if is_started:
            return self.class_model(
                user_id=self.user_id,
                user_phone=self.user_phone,
                user_flow_id=self.user_flow_id,
                activity=activity_key.strip(),
                is_started=is_started,
                started_on=current_ist_time,
                is_succeeded=None,
                succeeded_on=None,
                is_completed=None,
                completed_on=None,
            )
        elif is_succeeded:
            last_activity = self.class_model.query.get_started_activity_for_user(
                self.user_id, self.user_phone, self.user_flow_id
            )

            if last_activity:
                last_activity.is_succeeded = True
                last_activity.succeeded_on = current_ist_time
                return last_activity
            else:
                logger.error("No previous activity found for updating 'is_succeeded'.")
                return None
        elif is_completed:
            last_activity = self.class_model.query.get_succeeded_activity_for_user(
                self.user_id, self.user_phone, self.user_flow_id
            )

            if last_activity:
                last_activity.is_completed = True
                last_activity.completed_on = current_ist_time
                return last_activity
            else:
                logger.error("No previous activity found for updating 'is_completed'.")
                return None
        else:
            return None
