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
        "PM1_0": Gauge('pm1_0_ug_per_m3', 'Particles of 1 micron and smaller concentration, in ug/m3'),
        "PM1_0_atm": Gauge('pm1_0_atm_ug_per_m3', 'Particles of 1 micron and smaller concentration, with atmospheric environment, in ug/m3'),
        "PM2_5": Gauge('pm2_5_ug_per_m3', 'Particles of 2.5 micron and smaller concentration, in ug/m3'),
        "PM2_5_atm": Gauge('pm2_5_atm_ug_per_m3', 'Particles of 2.5 micron and smaller concentration, with atmospheric environment, in ug/m3'),
        "PM10": Gauge('pm10_ug_per_m3', 'Particles of 10 micron and smaller concentration, in ug/m3'),
        "PM10_atm": Gauge('pm10_atm_ug_per_m3', 'Particles of 10 micron and smaller concentration, with atmospheric environment, in ug/m3'),
        "gt0_3um": Gauge('gt0_3um', 'Number of particles of 0.3 microns per tenth of a litre of air'),
        "gt0_5um": Gauge('gt0_5um', 'Number of particles of 0.5 microns per tenth of a litre of air'),
        "gt1_0um": Gauge('gt1_0m', 'Number of particles of 1.0 microns per tenth of a litre of air'),
        "gt2_5um": Gauge('gt2_5m', 'Number of particles of 2.5 microns per tenth of a litre of air'),
        "gt5_0um": Gauge('gt5_0m', 'Number of particles of 5.0 microns per tenth of a litre of air'),
        "gt10um": Gauge('gt10m', 'Number of particles of 10 microns per tenth of a litre of air')
    }
}

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
