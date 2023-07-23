# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from env import ENDPOINT, ACCESS_ID, ACCESS_KEY, USERNAME, PASSWORD, DEVICE_ID

from tuya_iot import TuyaOpenAPI, TUYA_LOGGER

# Initialization of tuya openapi
openapi = TuyaOpenAPI(ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect(USERNAME, PASSWORD, "34", 'smartlife')


# # Uncomment the following lines to see logs.
import logging

TUYA_LOGGER.setLevel(logging.DEBUG)

def test():
    flag = True
    while True:
        input('Hit Enter to toggle light switch.')
        flag = not flag
        openapi.get('/v2.0/cloud/thing/{}/logs?codes=va_temperature&end_time=1690142168490&query_type=1&size=20&start_time=1689969368490&type=7'.format(DEVICE_ID))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
