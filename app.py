#/usr/bin/env python3

# Import basic libs
import time
import os

# Import flask for webservice and prometheus for metrics
from flask import Flask,jsonify,Response,request
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

# Import applications libs
from metrics import REQUEST_TIME
import gas_extend
import particules_extend
import weather_extend


# Create Flask application
app = Flask(__name__)

@app.route('/metrics')
def metrics():
    """Flask endpoint to gather the metrics, will be called by Prometheus."""
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

@app.route('/')
def index():
    result={}
    result['result']="Hello QIoT"
    return jsonify(result)


@app.route('/api/sensors')
def listsensor():
    listofSensor=[]
    listofSensor.append('/api/sensors/gas')
    listofSensor.append('/api/sensors/pollution')
    listofSensor.append('/api/sensors/weather')
    result={}
    result={"result":listofSensor}

    return jsonify(result)

#get /api/gas
# Message type
# {
#   "stationId":int,
#   "instant":String*,
#   "adc":double,
#   "nh3":double,
#   "oxidising":double,
#   "reducing":double,
# }

@app.route('/api/sensors/gas', methods=['GET'])
def get_data_gas():
    result={}
    result={"result":gas_extend.json_parsing_return()}
    return jsonify(result)

@app.route('/api/sensors/particules', methods=['GET'])
def get_data_particules():
    result={}
    result={"result":particules_extend.json_parsing_return()}
    return jsonify(result)

@app.route('/api/sensors/weather', methods=['GET'])
@REQUEST_TIME.time()
def get_weather():
    result={}
    result={"result":weather_extend.json_parsing_return()}
    return jsonify(result)

if __name__=='__main__':
    app.run(host=os.getenv('FLASK_APP_HOST'),port=os.getenv('FLASK_APP_PORT'),
            debug=os.getenv('FLASK_APP_DEBUG'))
