from telegram import Update
from telegram.ext import ContextTypes
from services.database import save_location

async def handle_location(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    location = update.message.location # type: ignore

    lat = location.latitude # type: ignore
    lon = location.longitude # type: ignore

    save_location(user.id, lat, lon) # type: ignore

    await update.message.reply_text( # type: ignore
        f"✅ Ubicación guardada.\nLatitud: {lat}\nLongitud: {lon}"
    )
