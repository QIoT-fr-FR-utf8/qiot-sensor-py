#!/usr/bin/env python3

# Import basic libs
import time
import os
import atexit

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

# Import flask for webservice and prometheus for metrics
#from flask import Flask, Response,request, render_template

from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

# Import applications libs
from metrics import REQUEST_TIME
import gas_extend
import particules_extend
import weather_extend
import lcd

atexit.register(lcd.stop)

# Create Flask application
# app = Flask(__name__)
app = FastAPI()

# @app.get('/metrics')
# def metrics():
#     """Flask endpoint to gather the metrics, will be called by Prometheus."""
#     return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

@app.get('/')
def index():
    result={}
    result['result']="Hello QIoT"
    return jsonable_encoder(result)


@app.get('/api/sensors')
def listsensor():
        listofSensor=[]
        listofSensor.append('/api/sensors/gas')
        listofSensor.append('/api/sensors/pollution')
        listofSensor.append('/api/sensors/weather')
        listofSensor.append('/api/lcd')
        result={}
        result={"result":listofSensor}

        return jsonable_encoder(result)


@app.get('/api/sensors/gas')
def get_data_gas():
        result={}
        result={"result":gas_extend.json_parsing_return()}
        return jsonable_encoder(result)

@app.get('/api/sensors/pollution')
def get_data_particules():
        result={}
        result={"result":particules_extend.json_parsing_return()}
        return jsonable_encoder(result)

@app.post('/api/lcd')
def post_message_to_lcd():
        data=request.get_json()
        result={"result":{"message posted":lcd.draw_message(data['message'])}}
        return jsonable_encoder(result)
    

@app.get('/api/sensors/weather')
@REQUEST_TIME.time()
def get_weather():
        result={}
        result={"result":weather_extend.json_parsing_return()}
        return jsonable_encoder(result)


# @app.get('/api/docs')
# def get_docs():
#     print('sending docs')
#     return render_template('swaggerui.html')

# @app.errorhandler(404)
# def ressource_not_found(e):
#     error="{0}".format(e)
#     return jsonable_encoder({"result":error}), 404


if __name__=='__main__':
    lcd.draw_message()
    app.run(host=os.getenv('FLASK_APP_HOST'),port=os.getenv('FLASK_APP_PORT'),
            debug=os.getenv('FLASK_APP_DEBUG'))
