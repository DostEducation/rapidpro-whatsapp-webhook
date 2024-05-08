from datetime import datetime, timedelta


def get_ist_timestamp() -> datetime:
    return datetime.utcnow() + timedelta(minutes=330)


def check_activity_key(activity_key: str, keyword: str, status: str):
    return activity_key.startswith(keyword) and activity_key.endswith(status)
