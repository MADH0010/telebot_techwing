# imports
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

# variables
updater = Updater(token='813878892:AAGZmZYUh8j_tgeFKTxqIZtrcxE4jE7b4uM', use_context=True)
dispatcher = updater.dispatcher

# functions
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="hi i am a bot")

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def setdate(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="temp")

def horoscope(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="okay")
# main
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

date_handler = CommandHandler('setdate', setdate)
dispatcher.add_handler(date_handler)

horoscope_handler = CommandHandler('horoscope', horoscope)
dispatcher.add_handler(horoscope_handler)

updater.start_polling()
print('Bot is working')