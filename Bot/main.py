from telegram import *
from telegram.ext import *

from typing import Final

TOKEN: Final = "7243209707:AAGPo2mwtL6z-m_xm9IMZZ8Ghjsm8aFL4JQ"
BOT_USERNAME: Final = "@MY_TON_Society_bot"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton("📜 Register Group 📜", callback_data="1"),
        ],
        [
            InlineKeyboardButton("🌐 Society List", callback_data="2"),
            InlineKeyboardButton("🌐 Join Society", callback_data="2"),
        ],
        [
            InlineKeyboardButton("💎 Fill with TON 💎", callback_data="3"),
        ],
        [
            InlineKeyboardButton("💎 Get Back TON 💎", callback_data="3"),
        ],
        [
            InlineKeyboardButton("🗂️ My Society List", callback_data="4"),
            InlineKeyboardButton("🗂️ My Society Jetton List", callback_data="4"),
        ],
        [
            InlineKeyboardButton("❗ Ranking", callback_data="5"),
            InlineKeyboardButton("❗ Reward", callback_data="5"),
            InlineKeyboardButton("❗ Referral", callback_data="5"),
            InlineKeyboardButton("❗ Vote", callback_data="5"),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_photo(
        "https://cdn.pixabay.com/photo/2017/02/07/10/33/crowd-2045499_1280.jpg",
        caption="awdadwadwawdawd",
        reply_markup=reply_markup,
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()

    await query.edit_message_text(text=f"Selected option: {query.data}")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Displays info on how to use the bot."""
    await update.message.reply_text("Use /start to test this bot.")


def main() -> None:
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
