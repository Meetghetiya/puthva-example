# import telebot
# import os
# import openai
# import time
# import requests
# import random
# from flask import Flask
# from modules import modules
# from handlers.routes import configure_routes




# TOKEN = "6164227662:AAGggFI3DeX4LbMhfSuXN20XhJ2_3485oME"
# URL = "https://vercel-puthva-example.vercel.app"
# OWNER = 846546194
# # SHORTEN_URL_ENDPOINT = os.getenv('SHORTEN_URL_ENDPOINT')
# openai.api_key = "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"

# bot = telebot.TeleBot(token=TOKEN, threaded=False)
# app = Flask(__name__)
# configure_routes(app, bot)


# @bot.message_handler(commands=['start'])
# def command_start(message):
#     cid = message.chat.id
#     bot.send_message(
#         cid, "Welcome to putuwaw_bot!\nType /help to find all commands.")


# @bot.message_handler(commands=['help'])
# def command_help(message):
#     cid = message.chat.id
#     help_text = "The following commands are available: \n"
#     for key in modules.COMMANDS:
#         help_text += '/' + key + ': '
#         help_text += modules.COMMANDS[key] + '\n'
#     bot.send_message(cid, help_text)


# @bot.message_handler(func=lambda message: modules.is_command(message.text))
# def command_unknown(message):
#     command = str(message.text).split()[0]
#     bot.reply_to(
#         message, "Sorry, {} command not found!\nPlease use /help to find all commands.".format(command))


import telebot
import os
import openai
import time
import requests
import random
from flask import Flask
from modules import modules
from handlers.routes import configure_routes
from dotenv import load_dotenv

load_dotenv()

TOKEN = "6207495158:AAFaw81_BaW2bVMae73wuZcjsrGqVO--0ZE"
URL = "https://vercel-puthva-example.vercel.app"
OWNER = 846546194

bot = telebot.TeleBot(token=TOKEN, threaded=False)
app = Flask(__name__)
configure_routes(app, bot)


@bot.message_handler(commands=['start'])
def command_start(message):
    cid = message.chat.id
    bot.send_message(
        cid, "Welcome to putuwaw_bot!\nType /help to find all commands.")


@bot.message_handler(commands=['help'])
def command_help(message):
    cid = message.chat.id
    help_text = "The following commands are available: \n"
    for key in modules.COMMANDS:
        help_text += '/' + key + ': '
        help_text += modules.COMMANDS[key] + '\n'
    bot.send_message(cid, help_text)

@bot.message_handler(func=lambda message: modules.is_command(message.text))
def command_unknown(message):
    command = str(message.text).split()[0]
    bot.reply_to(
        message, "Sorry, {} command not found!\nPlease use /help to find all commands.".format(command))

