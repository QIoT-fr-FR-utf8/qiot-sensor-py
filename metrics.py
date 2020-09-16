#/usr/bin/env python3

from prometheus_client import (Counter,
                               Gauge,
                               Summary)

# Define metrics
PROM_WEATHER_METRICS = {
    "gauge" : {
        "temperature": Gauge('bme280_temperature_degrees', 'Temperature of the BME280 sensor'),
        "compensated_temperature": Gauge('bme280_compensated_temperature_degrees', 'Temperature of the BME280 sensor, compensated'),
        "pressure": Gauge('bme280_pressure_hpa', 'Pressure of the BME280 sensor'),
        "humidity": Gauge('bme280_humidity_percent', 'Humidity of the BME280 sensor')
    }
}

PROM_GAS_METRICS = {
    "gauge" : {
        "nh3": Gauge('gas_nh3_ohms', 'TBD'),
        "oxidising": Gauge('gas_oxidising_ohms', 'TBD'),
        "reducing": Gauge('gas_reducing_ohms', 'TBD')
    }
}

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')