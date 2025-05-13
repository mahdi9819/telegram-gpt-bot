import os
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import nest_asyncio

# فعال کردن nest_asyncio برای سازگاری با Render
nest_asyncio.apply()

# گرفتن توکن‌ها از محیط
TELEGRAM_TOKEN = os.environ["8128126296:AAG1rD9IR7Qc7cDQHIs2fgqtDcmuVPou1kw"]
OPENAI_API_KEY = os.environ["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"]

openai.api_key = OPENAI_API_KEY


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! پیام بده تا با ChatGPT جواب بدم 😊")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.chat.send_action(action="typing")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )

    reply = response.choices[0].message.content
    await update.message.reply_text(reply)


app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("ربات روشن شد...")
app.run_polling()
