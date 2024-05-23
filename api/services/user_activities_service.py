from datetime import datetime
from typing import Any, Optional

from api import db, models
from api.helpers import common_helper
from api.utils.loggingutils import logger


class UserActivitiesService:
    def __init__(self, user, user_flow):
        self.user_id = user.id
        self.user_phone = user.phone
        self.user_flow_id = user_flow.id
        self.class_model = models.UserActivities

    def handle_user_activities(self, json_data: dict[str, Any]):
        try:
            current_time = common_helper.get_current_utc_timestamp()
            contact_activities = json_data.get("contact", {}).get("fields", {})

            for activity_key, activity_value in contact_activities.items():
                user_activity = self.create_or_update_user_activity(
                    activity_key, activity_value, current_time
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
        self, activity_key: str, activity_value: dict[str, Any], current_time: datetime
    ) -> Optional[models.UserActivities]:
        is_started = common_helper.check_activity_key(
            activity_key, activity_value, "activity_", "_started"
        )
        is_succeeded = common_helper.check_activity_key(
            activity_key, activity_value, "activity_", "_success"
        )
        is_completed = common_helper.check_activity_key(
            activity_key, activity_value, "activity_", "_completed"
        )

        if is_started:
            return self.create_activity(activity_key, current_time)
        elif is_succeeded:
            return self.update_succeeded_activity(current_time)
        elif is_completed:
            return self.update_completed_activity(current_time)
        else:
            return None

    def create_activity(
        self, activity_key: str, current_time: datetime
    ) -> models.UserActivities:
        return self.class_model(
            user_id=self.user_id,
            user_phone=self.user_phone,
            user_flow_id=self.user_flow_id,
            activity=activity_key.strip(),
            is_started=True,
            started_on=current_time,
        )

    def update_succeeded_activity(
        self, current_time: datetime
    ) -> Optional[models.UserActivities]:
        last_activity = self.class_model.query.get_todays_started_activity_for_user(
            self.user_id, self.user_phone
        )

        if last_activity:
            last_activity.is_succeeded = True
            last_activity.succeeded_on = current_time
            return last_activity
        else:
            logger.error("No previous activity found for updating 'is_succeeded'.")
            return None

    def update_completed_activity(
        self, current_time: datetime
    ) -> Optional[models.UserActivities]:
        last_activity = self.class_model.query.get_todays_succeeded_activity_for_user(
            self.user_id, self.user_phone
        )

        if last_activity:
            last_activity.is_completed = True
            last_activity.completed_on = current_time
            return last_activity
        else:
            logger.error("No previous activity found for updating 'is_completed'.")
            return None
