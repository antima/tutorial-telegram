from telegram.ext import Updater, CommandHandler

token = ""


def start(update, context):
    chat_id = update.effective_chat.id
    update.message.reply_text("start")
    print("start called from chat with id = {}".format(chat_id))


def end(update, context):
    chat_id = update.effective_chat.id
    update.message.reply_text("end")
    print("end called from chat with id = {}".format(chat_id))


def main():
    updater = Updater(token)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("end", end))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
