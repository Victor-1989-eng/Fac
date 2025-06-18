import os
from telegram import Update, Bot
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

def handle_message(update: Update, context: CallbackContext):
    msg = update.effective_message

    # Пересылаем админу (укажи свой Telegram ID)
    if ADMIN_ID:
        context.bot.forward_message(
            chat_id=ADMIN_ID,
            from_chat_id=msg.chat_id,
            message_id=msg.message_id
        )

    # Ответ пользователю
    msg.reply_text("Спасибо! Если будет токсично — опубликуем 😈")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.all, handle_message))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
