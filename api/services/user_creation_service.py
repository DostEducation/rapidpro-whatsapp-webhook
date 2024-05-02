from api import models
from api.utils import db_utils
from api.utils.loggingutils import logger


class UserCreationService:
    def __init__(self):
        self.class_model = models.Users

    def create_new_user(self, contact_data):
        try:
            user_phone = contact_data["phone"]
            formatted_user_phone = int(user_phone[-10:])
            user = self.class_model.query.get_by_phone(formatted_user_phone)
            if user:
                logger.info(
                    f"Skipped user creation for user {user.phone}. "
                    "Reason: User already exists."
                )
                return user

            user = self.create_user(contact_data, formatted_user_phone)

            logger.info(f"Created a new user entry with phone number {user.phone}.")

            return user
        except Exception as e:
            logger.error(
                f"Error while creating new user. Contact data: {contact_data}."
                f"Error message: {e}"
            )

    def create_user(self, contact_data, formatted_user_phone):
        glific_user_id = contact_data["id"]
        name = contact_data["name"]

        user = self.class_model(
            glific_user_id=glific_user_id,
            phone=formatted_user_phone,
            name=name,
            location=None,
        )

        db_utils.save(user)
        return user
