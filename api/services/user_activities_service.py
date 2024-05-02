from datetime import (
    datetime,
    timedelta,
)

from api import db, models
from api.utils.loggingutils import logger


class UserActivitiesService:
    def __init__(self, user, user_flow_id):
        self.started = "started"  # Prefix for the activity key in payload
        self.success = "success"  # Prefix for the activity key in payload
        self.completed = "completed"  # Prefix for the activity key in payload
        self.user_id = user.id
        self.user_phone = user.phone
        self.user_flow_id = user_flow_id
        self.class_model = models.UserActivities

    def handle_user_activities(self, json_data):
        try:
            activities = [(key, json_data[key]) for key in json_data]
            contact_activities = json_data.get("contact", {})
            contact_fields = contact_activities.get("fields", {})

            for activity_key, _ in activities:
                for sub_key, _ in contact_fields.items():
                    if sub_key.strip() == activity_key.strip():
                        user_activity = self.class_model(
                            user_id=self.user_id,
                            user_phone=self.user_phone,
                            user_flow_id=self.user_flow_id,
                            activity=activity_key.strip(),
                            is_started=(
                                True if self.started in activity_key else False
                            ),
                            started_on=datetime.utcnow() + timedelta(minutes=330),
                            is_succeeded=(
                                True if self.success in activity_key else False
                            ),
                            succeeded_on=datetime.utcnow() + timedelta(minutes=330),
                            is_completed=(
                                True if self.completed in activity_key else False
                            ),
                            completed_on=datetime.utcnow() + timedelta(minutes=330),
                        )
                        db.session.add(user_activity)

            db.session.commit()
            logger.info(f"Captured user activity for {self.user_phone}.")
        except Exception as e:
            logger.error(
                f"Error while capturing user activity for {self.user_phone}."
                f"Error message: {e}"
            )
