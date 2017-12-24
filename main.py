#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# jtcat_tg_bot - main.py
# Created by Jiting on 2017/12/24 22:53.
# Blog: https://blog.jtcat.com/
#
__author__ = '寂听 <jiting@jtcat.com>'
from config import TOKEN
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import logging

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="我是寂听的bot喵~")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)


echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()
