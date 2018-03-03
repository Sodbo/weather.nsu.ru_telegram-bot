# Sodbo Sharapov
# 20180303
# MIT License

# -*- coding: utf-8 -*-
import telebot  # package for the Telegram API
import config  # Here token is located
from get_nsu_temp import get_nsu_temp  # Module that get temp from NSU web page

# Initialize bot
bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])

# Function for responding to the request
def morning_message(message):
    bot.send_message(message.chat.id, get_nsu_temp())

# Endless loop that keep bot running
if __name__ == '__main__':
    bot.polling(none_stop=True)