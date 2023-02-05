import view_console as view, control_content

from telegram import (Update)
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters
)

TELEGRAM_TOKEN =  ''

def isBot(is_bot, full_name):
    if is_bot:
        view.print_text(f'--BOT-- {full_name}')
        return True
    return False

def init_telegram_token(aTELEGRAM_TOKEN):
    global TELEGRAM_TOKEN
    TELEGRAM_TOKEN = aTELEGRAM_TOKEN

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if isBot(update.effective_user.is_bot, update.effective_user.full_name): return
    data = update.callback_query.data
    if data and len(data)>0 and data.isdigit():
        button_number = int(data)
    else:
        await update.callback_query.answer() # ??????
        return

    l_text, l_reply_markup = control_content.get_button_data(
        update.effective_user.id
      , update.effective_user.full_name
      , button_number
    )
    if not l_text:
        await update.callback_query.answer() #?????
        return
    await update.callback_query.edit_message_text(text=l_text, reply_markup=l_reply_markup)


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if isBot(update.effective_user.is_bot, update.effective_user.full_name): return
    l_text, l_reply_markup = control_content.get_echo_data(
        update.effective_user.id
      , update.effective_user.full_name
      , update.message.text
    )
    #    photo_file = await update.message.photo[-1].get_file()
    await update.message.reply_text(text=l_text, reply_markup=l_reply_markup)

async def db_to_file(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if isBot(update.effective_user.is_bot, update.effective_user.full_name): return
    control_content.db_to_file()
    await update.message.reply_text(text='ok')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if isBot(update.effective_user.is_bot, update.effective_user.full_name): return
    l_text, l_reply_markup = control_content.get_start_data(
        update.effective_user.id
      , update.effective_user.full_name
    )
    await update.message.reply_text(text=l_text, reply_markup=l_reply_markup)


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token( TELEGRAM_TOKEN ).build()
    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("db_to_log", db_to_file))
    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.add_handler(CallbackQueryHandler(button))
    # Run the bot until the user presses Ctrl-C
    view.print_text('Сервер запущен.')
    application.run_polling()

if __name__ == "__main__":
    main()