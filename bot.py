import telebot
from handler import Handler
token = '5064765189:AAEcdgf2yUcfvPF8aXY5HY_SvU6-49Ne2W8'
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
