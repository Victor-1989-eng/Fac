import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Напиши /weather <город>")

async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Напиши: /weather Город")
        return

    city = " ".join(context.args)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=ru"

    try:
        data = requests.get(url).json()
        if data.get("cod") != 200:
            raise ValueError(data.get("message", "Ошибка"))

        name = data["name"]
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        msg = f"🌤 Погода в городе {name}:\nТемпература: {temp}°C\nОписание: {desc}"
        await update.message.reply_text(msg)
    except Exception as e:
        await update.message.reply_text(f"Ошибка: {e}")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("weather", weather))

app.run_polling()
