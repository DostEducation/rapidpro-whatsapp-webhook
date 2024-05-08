from datetime import datetime, timezone


def get_ist_timestamp() -> datetime:
    return datetime.now(timezone.utc)


def check_activity_key(activity_key: str, keyword: str, status: str):
    return activity_key.startswith(keyword) and activity_key.endswith(status)
