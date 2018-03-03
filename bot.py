# Sodbo Sharapov
# 20180303
# MIT License

# -*- coding: utf-8 -*-
import telebot
import config
#import get_nsu_temp

def get_nsu_temp():
	weather_nsu_message = "The temrerature around NSU is 0 C"
	return(weather_nsu_message)

# Initialize bot
bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])

# Function for responding to the request
def repeat_all_messages(message):
    bot.send_message(message.chat.id, get_nsu_temp())

# Endless loop that keep bot running
if __name__ == '__main__':
    bot.polling(none_stop=True)