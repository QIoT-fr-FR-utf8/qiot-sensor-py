#!/usr/bin/env python3
"""
QIoT Sensor Application
"""

# Import basic libs
import atexit
import os

# Import flask for webservice and prometheus for metrics
from flask import Flask, jsonify, Response, request, render_template
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

# Import applications libs
import gas_extend
import particules_extend
import weather_extend
import lcd

atexit.register(lcd.stop)

# Create Flask application
APP = Flask(__name__)

@APP.route('/metrics')
def metrics():
    """Flask endpoint to gather the metrics, will be called by Prometheus."""
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

@APP.route('/', methods=['GET'])
def index():
    """ Returns index route """
    result = {}
    result['result'] = "Hello QIoT"
    return jsonify(result)


@APP.route('/api/sensors', methods=['GET'])
def list_sensor():
    """ Returns list of sensor routes """
    if request.method == 'GET':
        list_of_sensor = []
        list_of_sensor.append('/api/sensors/gas')
        list_of_sensor.append('/api/sensors/pollution')
        list_of_sensor.append('/api/sensors/weather')
        list_of_sensor.append('/api/lcd')
        result = {}
        result = {"result":list_of_sensor}

        return jsonify(result)
    return False

@APP.route('/api/sensors/gas', methods=['GET'])
def get_data_gas():
    """ Returns gas information """
    if request.method == 'GET':
        result = {}
        result = {"result":gas_extend.json_parsing_return()}
        return jsonify(result)
    return False

@APP.route('/api/sensors/pollution', methods=['GET'])
def get_data_particules():
    """ Returns particules information """
    if request.method == 'GET':
        result = {}
        result = {"result":particules_extend.json_parsing_return()}
        return jsonify(result)
    return False

@APP.route('/api/lcd', methods=['POST'])
def post_message_to_lcd():
    """ Send message to the LCD screen """
    if request.method == 'POST':
        data = request.get_json()
        result = {"result":{"message posted":lcd.draw_message(data['message'])}}
        return jsonify(result)
    return False

@APP.route('/api/sensors/weather', methods=['GET'])
def get_weather():
    """ Returns weather information """
    if request.method == 'GET':
        result = {}
        result = {"result":weather_extend.json_parsing_return()}
        return jsonify(result)
    return False

@APP.route('/api/docs')
def get_docs():
    """ Returns API docs with swagger """
    print('sending docs')
    return render_template('swaggerui.html')

@APP.errorhandler(404)
def ressource_not_found(err):
    """ Returns Error code """
    error = "{0}".format(err)
    return jsonify({"result":error}), 404

# Main application
if __name__ == '__main__':
    lcd.draw_message()
    APP.run(host=os.getenv('FLASK_APP_HOST'), port=os.getenv('FLASK_APP_PORT'),
            debug=os.getenv('FLASK_APP_DEBUG'))
