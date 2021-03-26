from telegram.ext import Updater, CommandHandler
import threading
import requests
import logging
import time

logging.basicConfig(level=logging.INFO)

token = ""
target_url = ""

chat_ids = set()
updater = Updater(token)


def page_updated():
    interval = 5
    older = requests.get(target_url).text

    while True:
        if len(chat_ids) > 0:
            page_data = requests.get(target_url).text
            if page_data != older:
                older = page_data
                for chat_id in chat_ids:
                    updater.bot.send_message(chat_id=chat_id, text="Pagina aggiornata!")
        time.sleep(interval)


def start(update, context):
    chat_id = update.effective_chat.id
    chat_ids.add(chat_id)
    logging.info("{}: start".format(chat_id))


def end(update, context):
    chat_id = update.effective_chat.id
    chat_ids.remove(chat_id)
    logging.info("{}: stop".format(chat_id))


def main():
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("end", end))
    threading.Thread(target=page_updated).start()
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
