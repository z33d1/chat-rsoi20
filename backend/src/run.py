from flask import Flask
from uptime import uptime
from sys import platform
app = Flask(__name__)

@app.route('/hc')
def hc():
    return {
        "uptime": uptime(),
        "system.platform": platform
    }

if __name__ == "__main__":
    app.run(debug= True, host="0.0.0.0", port=8080)
