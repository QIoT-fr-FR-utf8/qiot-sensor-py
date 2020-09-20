#!/usr/bin/env python3

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

PROM_PARTICULES_METRICS = {
    "gauge" : {
        "pm1_0": Gauge('pm1_0', 'TBD'),
        "pm1_0_atm": Gauge('pm1_0_atm', 'TBD'),
        "pm2_5": Gauge('pm2_5', 'TBD'),
        "pm2_5_atm": Gauge('pm2_5_atm', 'TBD'),
        "pm10": Gauge('pm10', 'TBD'),
        "pm10_atm": Gauge('pm10_atm', 'TBD'),
        "gt0_3um": Gauge('gt0_3um', 'TBD'),
        "gt0_5um": Gauge('gt0_5um', 'TBD'),
        "gt1_0um": Gauge('gt1_0m', 'TBD'),
        "gt2_5um": Gauge('gt2_5m', 'TBD'),
        "gt5_0um": Gauge('gt5_0m', 'TBD'),
        "gt10um": Gauge('gt10m', 'TBD')
    }
}

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
