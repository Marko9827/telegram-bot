# Eronelit AI -> Telegram bot template

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Replace 'YOUR_BOT_TOKEN' with the actual token of your bot
TOKEN = 'YOUR_BOT_TOKEN'

def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}!',
        reply_markup=None
    )

def welcome_message(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_text(f'Welcome, {user.first_name} <3 \n please don't spam, don't discuss politics, don\'t post about freelancers, admins see and ban everything!')

def main() -> None:
    # Create the Updater and pass it your bot's token
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register the command handlers
    dp.add_handler(CommandHandler("start", start))

    # Register a message handler to trigger the welcome message
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome_message))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop it
    updater.idle()

if __name__ == '__main__':
    main()
