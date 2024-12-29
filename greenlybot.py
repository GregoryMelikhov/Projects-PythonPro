import telebot
from greenlylogic import craft_xmas_ball, sorting, time_decomposition_of, about

token = ""
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, about)

@bot.message_handler(commands=['crafts'])
def send_crafts(message):
    bot.reply_to(message, craft_xmas_ball)

@bot.message_handler(commands=['sorting'])
def send_sorting_way(message):
    bot.reply_to(message, sorting)
print("Bot warking!")

@bot.message_handler(commands=['decompositionof'])
def send_time_decomposition_of(message):
    bot.reply_to(message, time_decomposition_of)
bot.polling()
