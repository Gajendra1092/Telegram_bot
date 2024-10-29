import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Replace this with your bot token
TOKEN = "7510375858:AAEXwVZ-yoKXsbxkKtQa1zyZgY2mUWuQ9_A"

# Paths to the files you want to send
file_paths = {
    "File 1": r"C:\Users\DELL\Desktop\2022KUEC2014_dbms_assignment.pdf",
    "File 2":r"C:\Users\DELL\Desktop\OOSD.txt"
    }

# Initialize the bot application
application = Application.builder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Create an inline keyboard with options to send files
    keyboard = [
        [InlineKeyboardButton(name, callback_data=name)] for name in file_paths.keys()
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Please choose a file to receive:", reply_markup=reply_markup)

async def send_file(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    file_name = query.data
    await query.answer()
    
    # Check if the file exists before sending
    file_path = file_paths.get(file_name)
    if file_path and os.path.exists(file_path):
        await query.message.reply_document(document=open(file_path, 'rb'))
    else:
        await query.message.reply_text(f"Sorry, {file_name} is not available.")

# Add handlers to the application
application.add_handler(CommandHandler("start", start))
application.add_handler(CallbackQueryHandler(send_file))

# Run the bot
if __name__ == "__main__":
    application.run_polling()
