from pms5003 import PMS5003, ReadTimeoutError


pms5003 = PMS5003()
data = pms5003.read()
d_value_ug_m3={}
d_value_per_1l={}

d_value_ug_m3={"PM1_0":{"value":1.0,"atm":False}}
d_value_ug_m3={"PM2_5":{"value":2.5,"atm":False}}
d_value_ug_m3={"PM10":{"value":10,"atm":False}}
d_value_ug_m3={"PM1_0_atm":{"value":1.0,"atm":True}}
d_value_ug_m3={"PM2_5_atm":{"value":2.5,"atm":True}}
d_value_ug_m3={"PM10_atm":{"value":10,"atm":True}}

d_value_per_1l={"gt0_3um":{"value":0.3}}
d_value_per_1l={"gt0_5um":{"value":0.5}}
d_value_per_1l={"gt1_0um":{"value":1.0}}
d_value_per_1l={"gt2_5um":{"value":2.5}}
d_value_per_1l={"gt5_0um":{"value":5}}
d_value_per_1l={"gt10um":{"value":10}}

def r_int_value_pm_ug_per_m3(val,atm=False):
    if isinstance(data.pm_ug_per_m3(val,atm), int):
        return data.pm_ug_per_m3(val,atm)
    else:
        return 0

def r_int_value_pm_per_1l_air(val):
    if isinstance(data.pm_ug_per_m3(val), int):
        return data.pm_per_1l_air(val)
    else:
        return 0


def json_parsing_return():
    d_jsonexport={}
    
    for k,v in d_value_ug_m3.items():
        d_jsonexport[k]=r_int_value_pm_ug_per_m3(v['value'],v['atm'])

    for k,v in d_value_per_1l.items():
        d_jsonexport[k]=r_int_value_pm_ug_per_m3(v['value'],v['atm'])

    return d_jsonexport