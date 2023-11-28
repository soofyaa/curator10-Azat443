import telebot
bot = telebot.TeleBot('6825079935:AAFLVthzKmKfrEMSVelx8dphTxzpUUqHkbc')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Какое-то СМС')

@bot.message_handler(commands=['run'])
def main(message):
    bot.send_message(message.chat.id, 'run has activated \n press F to pay respect')


bot.infinity_polling()