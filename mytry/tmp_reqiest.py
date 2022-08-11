#!/usr/bin/python

import requests as req

resp = req.get("https://api.open-meteo.com/v1/forecast?latitude=41.85&longitude=-87.65&hourly=temperature_2m")
data = resp.json()
dict_temp = dict(zip(data['hourly']['time'],data['hourly']['temperature_2m']))
print(dict_temp[[k for k in dict_temp.keys() if k.endswith("11:00")][1]])
