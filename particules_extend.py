from time import gmtime, strftime
from pms5003 import PMS5003, ReadTimeoutError

#prom side
from prometheus_client import Gauge
from metrics import PROM_PARTICULES_METRICS

d_value_ug_m3={}
d_value_per_1l={}

d_value_ug_m3.update({"PM1_0":{"value":1.0,"atm":False}})
d_value_ug_m3.update({"PM2_5":{"value":2.5,"atm":False}})
d_value_ug_m3.update({"PM10":{"value":10,"atm":False}})
d_value_ug_m3.update({"PM1_0_atm":{"value":1.0,"atm":True}})
d_value_ug_m3.update({"PM2_5_atm":{"value":2.5,"atm":True}})
d_value_ug_m3.update({"PM10_atm":{"value":None,"atm":True}})

d_value_per_1l.update({"gt0_3um":{"value":0.3}})
d_value_per_1l.update({"gt0_5um":{"value":0.5}})
d_value_per_1l.update({"gt1_0um":{"value":1.0}})
d_value_per_1l.update({"gt2_5um":{"value":2.5}})
d_value_per_1l.update({"gt5_0um":{"value":5}})
d_value_per_1l.update({"gt10um":{"value":10}})


# Configure the PMS5003 for Enviro+
pms5003 = PMS5003(
    device='/dev/ttyAMA0',
    baudrate=9600,
    pin_enable=22,
    pin_reset=27
)

def r_int_value_pm_ug_per_m3(data,val,atm=False):
    try:
        if isinstance(data.pm_ug_per_m3(val,atm), int):
            return data.pm_ug_per_m3(val,atm)
        else:
            return 0
    except:
        return 0

def r_int_value_pm_per_1l_air(data,val):
    try: 
        if isinstance(data.pm_ug_per_m3(val), int):
            return data.pm_per_1l_air(val)
        else:
            return 0
    except :
        return 0

def json_parsing_return():
    d_jsonexport={}
    data = pms5003.read()
    
    d_jsonexport['instant']=strftime("%Y-%m-%d %H:%M:%S%Z", gmtime())

    for k,v in d_value_ug_m3.items():
        d_jsonexport[k]=r_int_value_pm_ug_per_m3(data, v['value'],v['atm'])
        PROM_PARTICULES_METRICS['gauge'][k].set(d_jsonexport[k])

    for k,v in d_value_per_1l.items():
        d_jsonexport[k]=r_int_value_pm_per_1l_air(data, v['value'])
        PROM_PARTICULES_METRICS['gauge'][k].set(d_jsonexport[k])

    return d_jsonexport

