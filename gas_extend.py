#!/usr/bin/env python3
from time import gmtime, strftime
from enviroplus import gas

from prometheus_client import Gauge

# Define metrics
PROM_GAS_METRICS = {
    "gauge" : {
        "adc": Gauge('gas_adc', 'TBD'),
        "nh3": Gauge('gas_nh3', 'TBD'),
        "oxidising": Gauge('gas_oxidising', 'TBD'),
        "reducing": Gauge('gas_reducing', 'TBD')
    }
}

def r_float_value_adc():
    if isinstance(gas.readall().adc, float):
        PROM_GAS_METRICS['gauge']['gas_adc'].set(gas.read_all().adc)
        return gas.read_all().adc
    else:
        return 0


def r_float_value_nh3():
    if isinstance(gas.readall().nh3, float):
        PROM_GAS_METRICS['gauge']['gas_nh3'].set(gas.read_all().nh3)
        return gas.read_all().nh3
    else:
        return 0


def r_float_value_oxidising():
    if isinstance(gas.readall().oxidising, float):
        PROM_GAS_METRICS['gauge']['gas_oxidising'].set(gas.read_all().oxidising)
        return gas.read_all().oxidising
    else:
        return 0


def r_float_value_reducing():
    if isinstance(gas.readall().reducing, float):
        PROM_GAS_METRICS['gauge']['gas_reducing'].set(gas.read_all().reducing)
        return gas.read_all().reducing
    else:
        return 0


def json_parsing_return():

    d_jsonexport={}
    d_jsonexport['instant']=strftime("%Y-%m-%d %H:%M:%S%Z", gmtime())
    d_jsonexport['nh3']=gas.read_all().nh3
    PROM_GAS_METRICS['gauge']['gas_nh3'].set(gas.read_all().nh3)
    d_jsonexport['oxidising']=gas.read_all().oxidising
    PROM_GAS_METRICS['gauge']['gas_oxidising'].set(gas.read_all().oxidising)
    d_jsonexport['reducing']=gas.read_all().reducing
    PROM_GAS_METRICS['gauge']['gas_reducing'].set(gas.read_all().reducing)

    return d_jsonexport