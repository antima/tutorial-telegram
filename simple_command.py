from telegram.ext import Updater, CommandHandler

token = ""


def start(update, _):
    chat_id = update.effective_chat.id
    print("start called from chat with id = {}".format(chat_id))


def end(update, _):
    chat_id = update.effective_chat.id
    print("end called from chat with id = {}".format(chat_id))


def main():
    updater = Updater(token)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("end", end))
    updater.start_polling()


if __name__ == "__main__":
    main()
