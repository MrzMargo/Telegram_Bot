import telebot
import page
BOT_TOKEN = page.TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    help_button = telebot.types.KeyboardButton('Help')
    review_button = telebot.types.KeyboardButton('Rate Bot')
    begin_button = telebot.types.KeyboardButton('Begin')
    keyboard.add(help_button, review_button, begin_button)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == "Help":
        bot.send_message(chat_id=message.chat.id, text="Hello, my name is Monica. I'll help you clean your mind:3", reply_markup=keyboard)


bot.polling()