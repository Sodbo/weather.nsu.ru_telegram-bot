# Sodbo Sharapov
# 20180303
# MIT License

# -*- coding: utf-8 -*-
import telebot  # package for the Telegram API
import config  # Here token is located
from get_nsu_temp import get_nsu_temp
from get_nsu_temp import message_nsu_temp  # Module that get temp from NSU web page
import time

# Keep temperature in cache
cached_temp_value = get_nsu_temp()

# Initialize bot
bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])

# Function for responding to the request
def morning_message(message):
    global cached_temp_value
    if time.time() - cached_temp_value[1]<300:
        print("I'm using cached data")
        temp_mes = message_nsu_temp(cached_temp_value[0])
        bot.send_message(message.chat.id, temp_mes)
    else:
        print("I'm loading new data")
        cached_temp_value = get_nsu_temp()
        temp_mes = message_nsu_temp(cached_temp_value[0])
        bot.send_message(message.chat.id, temp_mes)

# Endless loop that keep bot running
if __name__ == '__main__':
    bot.polling(none_stop=True)