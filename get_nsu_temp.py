# Sodbo Sharapov
# 20180303
# MIT License
# -*- coding: utf-8 -*-

import requests
import time
from bs4 import BeautifulSoup
import re

def get_nsu_temp():
    wnsu_url = 'http://weather.nsu.ru/loadata.php'
    r = requests.get(wnsu_url)
    nsu_temp = re.findall("cnv.innerHTML = '(.*)&deg;C';", r.text)
    nsu_temp = nsu_temp[0]
    cur_time = time.time()
    res = [nsu_temp , cur_time]
    return(res)

def message_nsu_temp(nsu_temp):
    weather_nsu_message = "The temperature nearby NSU is " + nsu_temp + "°C"
    return(weather_nsu_message)
