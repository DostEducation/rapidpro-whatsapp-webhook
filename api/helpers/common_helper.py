from datetime import datetime, timezone


def get_current_utc_timestamp() -> datetime:
    return datetime.now(timezone.utc)


def check_activity_key(activity_key: str, keyword: str, status: str):
    return (
        True
        if activity_key.startswith(keyword) and activity_key.endswith(status)
        else False
    )
