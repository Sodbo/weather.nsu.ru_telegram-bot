# Sodbo Sharapov
# 20180303
# GNU GPL2

# -*- coding: utf-8 -*-
import telebot
import config

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])

def repeat_all_messages(message):
    bot.send_message(message.chat.id, 'Doobs ne pidr')

if __name__ == '__main__':
    bot.polling(none_stop=True)