#!/usr/bin/env python3
from time import gmtime, strftime

# Import device libs
from bme280 import BME280
try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

# Import metrics
from metrics import PROM_WEATHER_METRICS

# Get the temperature of the CPU for compensation
def get_cpu_temperature():
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        temp = f.read()
        temp = int(temp) / 1000.0
    return temp

def get_compensated_temperature(raw_temp):
    factor = 1.3
    cpu_temps = [get_cpu_temperature()] * 5
    cpu_temp = get_cpu_temperature()
    # Smooth out with some averaging to decrease jitter
    cpu_temps = cpu_temps[1:] + [cpu_temp]
    avg_cpu_temp = sum(cpu_temps) / float(len(cpu_temps))
    comp_temp = raw_temp - ((avg_cpu_temp - raw_temp) / factor)
    return comp_temp

# Initialize bme280
bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)

def json_parsing_return():
    d_jsonexport={}
    d_jsonexport['instant']=strftime("%Y-%m-%d %H:%M:%S%Z", gmtime())
    d_jsonexport["temperature"] = bme280.get_temperature()
    PROM_WEATHER_METRICS['gauge']['temperature'].set(d_jsonexport["temperature"])
    d_jsonexport["compensated_temperature"] = get_compensated_temperature(d_jsonexport["temperature"])
    PROM_WEATHER_METRICS['gauge']['compensated_temperature'].set(d_jsonexport["compensated_temperature"])
    d_jsonexport["pressure"] = bme280.get_pressure()
    PROM_WEATHER_METRICS['gauge']['pressure'].set(d_jsonexport["pressure"])
    d_jsonexport["humidity"] = bme280.get_humidity()
    PROM_WEATHER_METRICS['gauge']['humidity'].set(d_jsonexport["humidity"])
    return d_jsonexport
