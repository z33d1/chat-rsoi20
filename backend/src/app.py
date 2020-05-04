from flask import Flask
from uptime import uptime
from sys import platform
from os import environ
from datetime import datetime

app = Flask(__name__)

@app.route('/hc')
def hc():
    env = {}
    for i,j in environ.items():
        env[i] = j
    return {
        "uptime": uptime(),
        "system.platform": platform,
        "environment vars": env,
        "current_time": datetime.now()
    }

if __name__ == "__main__":
    app.run(debug= True, host="0.0.0.0", port=8080)
