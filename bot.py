import telebot
from handler import Handler

bot = telebot.TeleBot(token)
handler = Handler()
@bot.message_handler()
def answer(message):
    bot.send_message(
        message.chat.id,
        handler.get_response(message.chat.id, message.text)
    )
if __name__ == '__main__':
    bot.polling(none_stop=True)