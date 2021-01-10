import requests
from flask import Flask

app = Flask(__name__)


@app.route('/info')
def info():
    res = requests.post("http://127.0.0.1:5000/get_info")
    return res.text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)