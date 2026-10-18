
import os
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

logging.basicConfig(level=logging.INFO)

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "أهلًا بك في MyBook AI 📚🥇\n\n"
        "أنا مساعدك لكتب التداول والذهب XAUUSD.\n"
        "حاليًا أنا في مرحلة الإعداد، وسنضيف قراءة الكتب "
        "والإجابة عن أسئلتك في الخطوات القادمة."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "أرسل سؤالك عن كتب التداول أو الذهب XAUUSD.\n"
        "ميزات قراءة الكتب والتحليل ستُضاف لاحقًا."
    )


async def handle_message(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
        "وصلت رسالتك ✅\n"
        "ما زلت في مرحلة الإعداد. سنضيف قدرات الذكاء الاصطناعي لاحقًا."
    )


def main():
    if not TOKEN:
        raise RuntimeError("متغير TELEGRAM_BOT_TOKEN غير مضبوط")

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )
    app.run_polling()


if __name__ == "__main__":
    main()
