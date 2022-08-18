from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

bot = Bot(token='5606526865:AAGFAtNAAJeOsjIVk-6X5BmmXrGxnk6bNFs')
updater = Updater(token='5606526865:AAGFAtNAAJeOsjIVk-6X5BmmXrGxnk6bNFs')
dispather = updater.dispatcher


def message(update, context):
    text = update.message.text
    text = text.replace('абв', ' ')
    context.bot.send_message(update.effective_chat.id, text)


message_handler = MessageHandler(Filters.text, message)
dispather.add_handler(message_handler)

print('server start')
updater.start_polling()
updater.idle()
