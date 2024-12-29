import telebot
from bot_logic import gen_pass, gen_emoji

Token = ""
bot = telebot.TeleBot(Token)

# Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}! Напиши /help чтобы посмотреть список команд.')

# Обработчик команды '/help'
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'Список команд: /start и /hello - приветствие | /heh (число) - бот будет смеятся заданное количество раз | /password (число) - генерирует пароль с заданной длинной | /emoji (число) - генерирует смайлики заданное количество раз')
 
# Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)

# Обработчик команды '/password'
@bot.message_handler(commands=['password'])  
def send_password(message):
    lenght_password = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, gen_pass(lenght_password))
    
# Обработчик команды '/emoji'
@bot.message_handler(commands=['emoji'])
def send_emoji(message):
    emoji_count = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, gen_emoji(emoji_count))


print('bot start')
bot.polling()
