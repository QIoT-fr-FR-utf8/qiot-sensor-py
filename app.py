#/usr/bin/env python3

# Import basic libs
import random
import time
import logging

# Import flask for webservice and prometheus for metrics
from flask import (Flask,
                   Response)
from prometheus_client import (generate_latest,
                               CONTENT_TYPE_LATEST,
                               Counter,
                               Gauge,
                               Summary)

# Import device libs
import enviroplus
from bme280 import BME280
try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

# Define metrics
PROM_METRICS = {
    "counter": {
        "my_counter": Counter('my_counter',
                                 'Number Of counts',
                                 ['count'])
    },
    "gauge": {
        "temperature": Gauge('bme280_temperature_degrees', 'Temperature of the BME280 sensor'),
        "compensated_temperature": Gauge('bme280_compensated_temperature_degrees', 'Temperature of the BME280 sensor, compensated'),
        "cpu_temperature": Gauge('cpu_temperature_degrees', 'Temperature of the CPU')
    }
}
# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Get the temperature of the CPU for compensation
def get_cpu_temperature():
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        temp = f.read()
        temp = int(temp) / 1000.0
    return temp

def get_temperature():
    raw_temp = bme280.get_temperature()
    return raw_temp

def get_compensated_temperature():
    factor = 2.25
    cpu_temps = [get_cpu_temperature()] * 5
    cpu_temp = get_cpu_temperature()
    # Smooth out with some averaging to decrease jitter
    cpu_temps = cpu_temps[1:] + [cpu_temp]
    avg_cpu_temp = sum(cpu_temps) / float(len(cpu_temps))
    raw_temp = bme280.get_temperature()
    comp_temp = raw_temp - ((avg_cpu_temp - raw_temp) / factor)
    logging.info("Compensated temperature: {:05.2f} *C".format(comp_temp))
    return comp_temp

# Initialize bme280
bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)

# Create Flask application
app = Flask(__name__)

@app.route('/metrics')
@REQUEST_TIME.time()
def metrics():
    """Flask endpoint to gather the metrics, will be called by Prometheus."""
    PROM_METRICS['counter']['my_counter'].labels('count').inc()
    PROM_METRICS['gauge']['cpu_temperature'].set(get_cpu_temperature())
    PROM_METRICS['gauge']['temperature'].set(get_temperature())
    PROM_METRICS['gauge']['compensated_temperature'].set(get_compensated_temperature())
    return Response(generate_latest(),
                    mimetype=CONTENT_TYPE_LATEST)

# Just run the app!
app.run(port=8000,debug=True, host='0.0.0.0')
