from telegram import (
    Update,
    ReplyKeyboardMarkup
)
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from config import BOT_TOKEN

keyboard = [
    ["🟢 Check In", "🔴 Check Out"],
    ["🚬 Smoke", "🚻 Washroom"],
    ["🍽 Dinner", "🔙 Back"],
    ["📊 My Report"]
]

reply_markup = ReplyKeyboardMarkup(
    keyboard,
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to Attendance Bot",
        reply_markup=reply_markup
    )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🟢 Check In":
        await update.message.reply_text("✅ Check In Recorded")

    elif text == "🔴 Check Out":
        await update.message.reply_text("✅ Check Out Recorded")

    elif text == "🚬 Smoke":
        await update.message.reply_text("🚬 Smoke Break Started")

    elif text == "🚻 Washroom":
        await update.message.reply_text("🚻 Washroom Break Started")

    elif text == "🍽 Dinner":
        await update.message.reply_text("🍽 Dinner Break Started")

    elif text == "🔙 Back":
        await update.message.reply_text("✅ Welcome Back")

    elif text == "📊 My Report":
        await update.message.reply_text("📊 Report Coming Soon")

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, buttons)
    )

    print("Bot Started...")
    app.run_polling()

if __name__ == "__main__":
    main()
