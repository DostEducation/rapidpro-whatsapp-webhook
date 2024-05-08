from datetime import datetime, timezone


def get_ist_timestamp() -> datetime:
    # ist_offset = timedelta(hours=5, minutes=30)
    utc_now = datetime.now(timezone.utc)
    return utc_now


def check_activity_key(activity_key: str, keyword: str, status: str):
    return activity_key.startswith(keyword) and activity_key.endswith(status)
