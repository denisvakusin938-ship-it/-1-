import logging
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler # Добавили CallbackQueryHandler
import asyncio
import nest_asyncio
nest_asyncio.apply()

BOT_TOKEN = ""

BIOGRAPHIES = {
    "demina": "Ирина Демина — Великий биолог и по совместительству барбос",
    "mulagalieva": "Алина Мулагалиева — ЛПшка Ирины, учится на бизнес информатике ха-ха-ха",
    "koshankov": "Матвей Кошанков — Москвич, по своместительству друг Дениса",
    "vakushin": "Денис Вакушин — Великий програмист, выдающийся спортсмен, бог всего"
}

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[KeyboardButton("/help, тебе это не надо")], [KeyboardButton("/info")]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Здарова! Нажми на кнопку:", reply_markup=reply_markup)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("Перейти на сайт", url="https://example.com")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Нажми на кнопку для перехода на сайт:", reply_markup=reply_markup)

async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Ирина Демина", callback_data="demina")],
        [InlineKeyboardButton("Алина Мулагалиева", callback_data="mulagalieva")],
        [InlineKeyboardButton("Матвей Кошанков", callback_data="koshankov")],
        [InlineKeyboardButton("Денис Вакушин", callback_data="vakushin")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Выбери человека, чтобы узнать его биографию:", reply_markup=reply_markup)

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    bio_text = BIOGRAPHIES.get(query.data, "Биография не найдена.")
    
    await query.message.reply_text(bio_text)

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("info", info_command))
    
    app.add_handler(CallbackQueryHandler(button_callback))

    print("Бот запущен...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())





