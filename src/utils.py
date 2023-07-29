from datetime import timedelta, datetime
from dateutil import tz


def get_start_and_end(offset=1):
    today = datetime.now(tz=tz.gettz('Europe/Madrid'))
    start = today.replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(offset)
    end = start + timedelta(1)

    return int(start.timestamp()*1000), int(end.timestamp()*1000)
