#!/usr/bin/env python3

# Import basic libs
import time
import os
import atexit
import redis
# Import flask for webservice and prometheus for metrics
from flask import Flask,jsonify,Response,request
# from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

# Import applications libs
from metrics import REQUEST_TIME
import lcd

atexit.register(lcd.stop)

def redis_connect():
    return redis.Redis(host=os.getenv('REDIS_HOST'),port=6379, db=0, decode_responses=True)

# Create Flask application
app = Flask(__name__)

#@app.route('/metrics')
#def metrics():
#    """Flask endpoint to gather the metrics, will be called by Prometheus."""
#    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

@app.route('/', methods=['GET'])
def index():
    result={}
    result['result']="Hello QIoT"
    return jsonify(result)


@app.route('/api/sensors', methods=['GET'])
def listsensor():
    if request.method == 'GET':
        listofSensor=[]
        listofSensor.append('/api/sensors/gas')
        listofSensor.append('/api/sensors/particules')
        listofSensor.append('/api/sensors/weather')
        listofSensor.append('/api/lcd')
        result={}
        result={"result":listofSensor}

        return jsonify(result)

@app.route('/api/sensors/gas', methods=['GET'])
def get_data_gas():
    redisClient = redis_connect()
    if request.method == 'GET':
        result={}
        l_result=[]
        while(redisClient.llen('gas')!=0):
            l_result.append(str(redisClient.lpop('gas')))
        result={"result":l_result}
        return jsonify(result)

@app.route('/api/sensors/particules', methods=['GET'])
def get_data_particules():
    if request.method == 'GET':
        result={}
        result={"result":particules_extend.json_parsing_return()}
        return jsonify(result)

@app.route('/api/lcd', methods=['POST'])
def post_message_to_lcd():
    if request.method == 'POST':
        data=request.get_json()
        result={"result":{"message posted":lcd.draw_message(data['message'])}}
        return jsonify(result)
    

@app.route('/api/sensors/weather', methods=['GET'])
@REQUEST_TIME.time()
def get_weather():
    if request.method == 'GET':
        result={}
        result={"result":weather_extend.json_parsing_return()}
        return jsonify(result)

if __name__=='__main__':
 #   lcd.draw_message()
    app.run(host=os.getenv('FLASK_APP_HOST'),port=os.getenv('FLASK_APP_PORT'),
            debug=os.getenv('FLASK_APP_DEBUG'))
