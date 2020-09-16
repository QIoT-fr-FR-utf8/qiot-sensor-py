from pms5003 import PMS5003, ReadTimeoutError
pms5003 = PMS5003()

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

    d_jsonexport["PM1_0"]
    d_jsonexport["PM2_5"]
    d_jsonexport["PM10"]
    d_jsonexport["PM1_0_atm"]
    d_jsonexport["PM2_5_atm"]
    d_jsonexport["PM10_atm"]
    d_jsonexport["gt0_3um"]
    d_jsonexport["gt0_5um"]
    d_jsonexport["gt1_0um"]
    d_jsonexport["gt2_5um"]
    d_jsonexport["gt5_0um"]
    d_jsonexport["gt10um"]

    return d_jsonexport










    d_jsonexport['instant']=strftime("%Y-%m-%d %H:%M:%S%Z", gmtime())
    d_jsonexport['nh3']=gas.read_all().nh3
    d_jsonexport['oxidising']=gas.read_all().oxidising
    d_jsonexport['reducing']=gas.read_all().reducing

    return d_jsonexport