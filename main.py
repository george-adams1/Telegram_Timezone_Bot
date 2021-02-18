import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

# Bot Setup
updater = Updater(token = '1445118809:AAGjcqQYlBDMzEy0Iv7xX6eZbU4c-9LYbaw', use_context = True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# /Start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome! I'm a bot, please talk to me!")
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def time_zone(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Which timezone are you in? (EST or CAT)")
timezone_handler = CommandHandler('Timezone', time_zone)
dispatcher.add_handler(timezone_handler)
timezone_message = MessageHandler(Filters.text & (~Filters.command), time_zone)
dispatcher.add_handler(timezone_message)
print(timezone_message)


# Polling
updater.start_polling()