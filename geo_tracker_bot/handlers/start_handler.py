from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    botones = [[KeyboardButton("📍 Compartir ubicación", request_location=True)]]
    markup = ReplyKeyboardMarkup(botones, one_time_keyboard=True, resize_keyboard=True)
    
    await update.message.reply_text( # type: ignore
        "👋 ¡Hola! ¿Quieres compartir tu ubicación actual conmigo?",
        reply_markup=markup
    )
