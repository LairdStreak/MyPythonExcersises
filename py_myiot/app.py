from flask import Flask, request, render_template, abort
from dotenv import load_dotenv
import os
import sentry_sdk
from sentry_sdk import capture_exception, capture_message

load_dotenv(verbose=True)


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index(name=None):
    return render_template('index.htm', name=name)

@app.route('/data', methods=['POST','GET'])
def telegram_webhook():
    try:
        update = request.get_json()
        print(update)
        return "OK"
    except Exception as e:
        capture_exception(e)
    abort(500)

if __name__ == '__main__':
    app.run(port='3000', debug=True)
    #app.run(host='0.0.0.0', port='3000')
