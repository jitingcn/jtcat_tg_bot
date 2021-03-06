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
# from telegram.ext import MessageHandler, Filters
import logging
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler
from function import get_stream

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="我是寂听的bot喵~")


def blsu(bot, update, args):
    if len(args) != 0:
        room_id = int(args[0])
    else:
        room_id = 74151
    text_blive_stream = get_stream(room_id)
    bot.send_message(chat_id=update.message.chat_id, text=text_blive_stream)


def inline_blive_stream(bot, update):
    query = update.inline_query.query
    if not query:
        return
    sth = int(query)
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=sth,
            title='bilibili.com live stream url',
            input_message_content=InputTextMessageContent(get_stream(sth))
        )
    )
    bot.answer_inline_query(update.inline_query.id, results)


# def unknown(bot, update):
#    bot.send_message(chat_id=update.message.chat_id, text="你说什么喵?不明白喵?")


inline_blive_stream_handler = InlineQueryHandler(inline_blive_stream)
dispatcher.add_handler(inline_blive_stream_handler)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
blive_stream_url_handler = CommandHandler('blsu', blsu, pass_args=True)
dispatcher.add_handler(blive_stream_url_handler)
# unknown_handler = MessageHandler(Filters.command, unknown)
# dispatcher.add_handler(unknown_handler)
updater.start_polling()
