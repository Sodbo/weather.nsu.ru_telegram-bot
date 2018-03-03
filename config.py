from os.path import expanduser

# -*- coding: utf-8 -*-

# Token from the @MorCheka_bot bot

home = expanduser("~")

token_file = open(home+"/.telegram/weather_nsu_bot_token",'r')

token = token_file.read().splitlines()[0]