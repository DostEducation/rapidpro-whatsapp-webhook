from datetime import datetime, timezone
from typing import Any


def get_current_utc_timestamp() -> datetime:
    return datetime.now(timezone.utc)


def check_activity_key(
    activity_key: str, activity_value: dict[str, Any], keyword: str, status: str
):
    return (
        True
        if activity_key.startswith(keyword)
        and activity_key.endswith(status)
        and activity_value["value"] == "yes"
        else False
    )
