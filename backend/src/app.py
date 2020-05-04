from flask import Flask
from flask import send_from_directory, render_template
from uptime import uptime
from sys import platform
from os import environ
from datetime import datetime
import os

STATIC_FOLDER = "static"
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = STATIC_FOLDER

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

@app.route("/html")
def send_static_bad():
    full_name = os.path.join(STATIC_FOLDER, "index.gif")
    return render_template("index.html", user_image=full_name)

if __name__ == "__main__":
    app.run(debug= True, host="0.0.0.0", port=8080)
