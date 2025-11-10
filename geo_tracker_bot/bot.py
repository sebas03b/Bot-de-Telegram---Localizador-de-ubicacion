from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import TELEGRAM_TOKEN
from handlers.start_handler import start
from handlers.location_handler import handle_location

def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.LOCATION, handle_location))

    print("🤖 Bot ejecutándose...")
    app.run_polling()

if __name__ == "__main__":
    main()
