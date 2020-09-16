#!/usr/bin/env python3
from time import gmtime, strftime
from enviroplus import gas

def r_float_value_adc():
    if isinstance(gas.readall().adc, float):
        return gas.read_all().adc
    else:
        return 0


def r_float_value_nh3():
    if isinstance(gas.readall().nh3, float):
        return gas.read_all().nh3
    else:
        return 0


def r_float_value_oxidising():
    if isinstance(gas.readall().oxidising, float):
        return gas.read_all().oxidising
    else:
        return 0


def r_float_value_reducing():
    if isinstance(gas.readall().reducing, float):
        return gas.read_all().reducing
    else:
        return 0


def json_parsing_return():

    d_jsonexport={}
    d_jsonexport['instant']=strftime("%Y-%m-%d %H:%M:%S%Z", gmtime())
    d_jsonexport['nh3']=gas.read_all().nh3
    d_jsonexport['oxidising']=gas.read_all().oxidising
    d_jsonexport['reducing']=gas.read_all().reducing

    return d_jsonexport