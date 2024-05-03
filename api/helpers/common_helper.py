from datetime import datetime, timedelta


def get_ist_timestamp() -> datetime:
    return datetime.utcnow() + timedelta(minutes=330)
