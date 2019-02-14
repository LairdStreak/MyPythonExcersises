from flask import Flask, request, render_template, abort, jsonify
import os
import logging
import json

log = logging.getLogger(__name__)
logging.basicConfig(format="[%(asctime)s]  %(levelname)s:%(message)s")
log.setLevel(logging.DEBUG)

def logging_fun(method, remote_addr):
    log.info('HTTP %s request from %s' % (method, remote_addr))

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite3')

#load_dotenv(verbose=True)
#SENTRYCONF = os.getenv('SENTRYCONF')

app = Flask(__name__)
app.debug = True

@app.route('/',methods = ['GET'])
def index(name=None):
    return "home"

@app.route('/dhtdatapush',methods = ['POST'])
def dhtdatapush():
    logging_fun(request.method, request.remote_addr)
    try:
        print(request.data)
        response_data = json.loads(request.text)
        logging_fun(request.method, type(response_data))
        update = request.json()
        logging_fun(request.method, update)
        logging_fun(request.method, type(update))
        print(update)
        print(update['temp'])
        message = { 'status': 200, 'message': 'json ID ' }
        resp = jsonify(message)
        resp.status_code = 200
        return resp
    except Exception as e:
        message = { 'status': 400, 'exception': 'error ' + str(e), }
        resp = jsonify(message)
        resp.status_code = 400
        return resp
    abort(500)

@app.route('/graphdata/')        
def graphdata():
    data = da.dht_data_get_latest(DEFAULT_PATH)
    gauge = pygal.SolidGauge(
            half_pie=True, inner_radius=0.70,
            show_y_labels=False,show_x_labels=False,
            show_legend=False,width=200, height=200)

    gauge.add('Temperature:', [{'value': data.temp, 'max_value': 600}])
    gauge.add('Humidity:', [{'value': data.humidity, 'max_value': 600}])
        
     
    graph_data = gauge.render_data_uri()
    return render_template("graphing.html", graph_data = graph_data)

@app.errorhandler(400)
def not_found(error):
    """
    Gives error message when any bad requests are made.
    Args:
        error (string):
    Returns:
        Error message.
    """
    print(error)
    return make_response(jsonify({'error': 'Bad request'}), 400)

if __name__ == '__main__':
    app.run(port='3000')
