import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎬 أهلاً بيك في Cartoon Kids Studio\n\n"
        "استخدم /shorts ثم ابعتلي الفيديو الطويل."
    )

async def shorts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎥 تمام! ابعتلي الفيديو الطويل دلوقتي."
    )

async def video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎬 ابعت فكرة الفيديو اللي عايز تعملها."
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("shorts", shorts))
app.add_handler(CommandHandler("video", video))

app.run_polling()
