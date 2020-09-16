#/usr/bin/env python3

# Import basic libs
import time
import logging

# Import flask for webservice and prometheus for metrics
from flask import Flask,jsonify,Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

# Import device libs
import enviroplus
from bme280 import BME280
try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

# Import applications libs
from metrics import PROM_WEATHER_METRICS, REQUEST_TIME

# Get the temperature of the CPU for compensation
def get_cpu_temperature():
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        temp = f.read()
        temp = int(temp) / 1000.0
    return temp

def get_compensated_temperature(raw_temp):
    factor = 2.25
    cpu_temps = [get_cpu_temperature()] * 5
    cpu_temp = get_cpu_temperature()
    # Smooth out with some averaging to decrease jitter
    cpu_temps = cpu_temps[1:] + [cpu_temp]
    avg_cpu_temp = sum(cpu_temps) / float(len(cpu_temps))
    comp_temp = raw_temp - ((avg_cpu_temp - raw_temp) / factor)
    logging.info("Compensated temperature: {:05.2f} *C".format(comp_temp))
    return comp_temp


# Initialize bme280
bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)

# Create Flask application
app = Flask(__name__)

@app.route('/weather')
@REQUEST_TIME.time()
def weather_sensors():
    result = {}
    result["temperature"] = bme280.get_temperature()
    PROM_WEATHER_METRICS['gauge']['temperature'].set(result["temperature"])
    result["compensated_temperature"] = get_compensated_temperature(result["temperature"])
    PROM_WEATHER_METRICS['gauge']['compensated_temperature'].set(result["compensated_temperature"])
    result["pressure"] = bme280.get_pressure()
    PROM_WEATHER_METRICS['gauge']['pressure'].set(result["pressure"])
    result["humidity"] = bme280.get_humidity()
    PROM_WEATHER_METRICS['gauge']['humidity'].set(result["humidity"])
    return jsonify(result)

@app.route('/metrics')
def metrics():
    """Flask endpoint to gather the metrics, will be called by Prometheus."""
    return Response(generate_latest(),
                    mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    # Just run the app!
    app.run(port=8000,debug=True, host='0.0.0.0')
