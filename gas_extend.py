from time import gmtime, strftime
from enviroplus import gas

# prom side
from metrics import PROM_GAS_METRICS

def r_float_value_adc():
    adc = gas.read_adc()
    if isinstance(adc, float):
        return adc
    return 0


def r_float_value_nh3():
    nh3 = gas.read_nh3()
    if isinstance(nh3, float):
        return nh3
    return 0


def r_float_value_oxidising():
    oxidising = gas.read_oxidising()
    if isinstance(oxidising, float):
        return oxidising
    return 0


def r_float_value_reducing():
    reducing = gas.read_reducing()
    if isinstance(reducing, float):
        return reducing
    return 0


def json_parsing_return():

    d_jsonexport={}
    d_jsonexport['instant']=strftime("%Y-%m-%d %H:%M:%S%Z", gmtime())
    d_jsonexport['nh3']=r_float_value_nh3()
    d_jsonexport['oxidising']=r_float_value_oxidising()
    d_jsonexport['reducing']=r_float_value_reducing()
    
    PROM_GAS_METRICS['gauge']['nh3'].set(d_jsonexport['nh3'])
    PROM_GAS_METRICS['gauge']['oxidising'].set(d_jsonexport['oxidising'])
    PROM_GAS_METRICS['gauge']['reducing'].set(d_jsonexport['reducing'])

    return d_jsonexport
