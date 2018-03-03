# Sodbo Sharapov
# 20180303
# MIT License

import dryscrape
import time
from bs4 import BeautifulSoup

def get_nsu_temp():
    wnsu_url = 'http://weather.nsu.ru/'
    session = dryscrape.Session()
    session.visit(wnsu_url)
    response = session.body()
    soup = BeautifulSoup(response, "lxml")
    nsu_temp = str(soup.find(id="temp"))
    nsu_temp = nsu_temp.split("<")[1].split('>')[1]
    cur_time = time.time()
    res = [nsu_temp , cur_time]
    return(res)

def message_nsu_temp(nsu_temp):
    weather_nsu_message = "The temperature nearby NSU is " + nsu_temp
    return(weather_nsu_message)