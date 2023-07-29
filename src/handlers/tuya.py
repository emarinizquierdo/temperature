from datetime import datetime
from dateutil.tz import tz
from env import ENDPOINT, ACCESS_ID, ACCESS_KEY, USERNAME, PASSWORD
from src.utils import get_start_and_end
from src.tuya_iot import TuyaOpenAPI

# Initialization of tuya openapi
openapi = TuyaOpenAPI(ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect(USERNAME, PASSWORD, "34", 'smartlife')


def get_temperatures(device_id, offset=1):
    start, end = get_start_and_end(offset=offset)
    response = openapi.get(f'/v2.0/cloud/thing/{device_id}/logs?codes=va_temperature&end_time={end}&query_type=1&size=300&start_time={start}&type=7')
    time_zone = tz.gettz('Europe/Madrid')
    values = list()
    for item in response.get('result').get('logs'):
        event_time = datetime.fromtimestamp(item['event_time'] // 1000, tz=time_zone).strftime("%m/%d/%Y %H:%M:%S")
        values.append([event_time, int(item['value']) / 10])

    return values
