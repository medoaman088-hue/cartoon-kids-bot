import os
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import fal_client

BOT_TOKEN = os.environ[8925475804:AAHT-ZshDDkP8iZEIBZAdF8y7AbMtbiRCTU]
FAL_KEY = os.environ["d060dc8b-22ff-45d2-896b-04f890f8f3b3:ca65cadf7738fcd19678087fbbec8500"]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎬 أهلاً بيك!\n\n"
        "اكتب وصف الفيديو اللي عايزه، وأنا هحاول أعملهولك."
    )


async def generate_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = update.message.text

    await update.message.reply_text("⏳ جاري إنشاء الفيديو... استنى شوية 🎬")

    try:
        result = await asyncio.to_thread(
            fal_client.subscribe,
            "fal-ai/kandinsky5/text-to-video",
            arguments={
                "prompt": prompt
            },
            with_logs=False
        )

        video_url = result["video"]["url"]

        await update.message.reply_video(
            video=video_url,
            caption="✅ الفيديو جاهز!"
        )

    except Exception as e:
        await update.message.reply_text(
            "❌ حصل خطأ أثناء إنشاء الفيديو.\n"
            "جرب وصف تاني."
        )
        print(e)


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, generate_video)
    )

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
