import telebot
import page
# Замените 'YOUR_BOT_TOKEN' на ваш токен бота, полученный от BotFather
BOT_TOKEN = page.TOKEN

# Создание экземпляра бота
bot = telebot.TeleBot(BOT_TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я простой бот. Попробуйте отправить мне любое сообщение.")

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Вы написали: {message.text}")

# Запуск бота
bot.polling()