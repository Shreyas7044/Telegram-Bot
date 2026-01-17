from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

# Replace with your BotFather API Token
updater = Updater("YOUR_BOT_API_TOKEN", use_context=True)


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hello sir, Welcome to the Bot.\nPlease type /help to see available commands."
    )


def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands:
    /youtube  - Get YouTube URL
    /linkedin - Get LinkedIn profile URL
    /gmail    - Get Gmail URL
    /geeks    - Get GeeksforGeeks URL
    """)


def gmail_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Your Gmail link here (hidden for security reasons)"
    )


def youtube_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "YouTube Link 👉 https://www.youtube.com/"
    )


def linkedIn_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "LinkedIn URL 👉 https://www.linkedin.com/"
    )


def geeks_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "GeeksforGeeks 👉 https://www.geeksforgeeks.org/"
    )


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        f"Sorry '{update.message.text}' is not a valid command"
    )


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        f"Sorry, I can't recognize you. You said '{update.message.text}'"
    )


# Command Handlers
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedIn_url))
updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
updater.dispatcher.add_handler(CommandHandler('geeks', geeks_url))

# Message Handlers
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

# Start the Bot
updater.start_polling()
print("Bot is running...")
