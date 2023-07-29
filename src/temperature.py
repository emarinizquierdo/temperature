from src.constants import DEVICES
from src.handlers.sheets import append_values
from src.handlers.tuya import get_temperatures


def request_temperatures():

    for device in DEVICES:
        values = get_temperatures(device['id'], offset=1)
        append_values(
            "1-jufz6qGinKt4O55X5PwmT74zvR_rPu_lfwRyX-acMk",
            device['range'],
            "USER_ENTERED",
            values
        )