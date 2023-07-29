from flask import Flask
from src.temperature import request_temperatures

app = Flask(__name__)


@app.route("/tasks/temperature")
def temperature():
    request_temperatures()
    return "ok"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
