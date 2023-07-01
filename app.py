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

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual Telegram bot token
bot = telebot.TeleBot('6207495158:AAFaw81_BaW2bVMae73wuZcjsrGqVO--0ZE')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I am your bot. Type something, and I'll respond.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Replace the following line with your bot's logic to generate a response
    bot.send_message(message.chat.id, "This is a dummy response.")

# Replace 'YOUR_WEBHOOK_URL' with your actual webhook URL (e.g., https://yourdomain.com/webhook)
webhook_url = 'https://vercel-puthva-example.vercel.app'

# Remove this line if you want to use polling instead of a webhook
bot.remove_webhook()

# Set up the webhook
bot.set_webhook(url=webhook_url)

if __name__ == "__main__":
    # Start the Flask app with a dummy route to avoid Heroku errors
    from flask import Flask
    app = Flask(__name__)

    @app.route('/')
    def index():
        return "Bot is running!"

    app.run(port=5000)


