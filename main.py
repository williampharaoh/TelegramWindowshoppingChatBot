
from flask import Flask
from asyncore import dispatcher
from cgitb import text
from urllib import response
import Constants as keys
from telegram.ext import *
import Responses as Res


#print bot started when it is started and running 
print("Bot started.....")

# commands handler 

# start message 
def start_command(update, context):
    update.message.reply_text("""Hi there ! am window shopping bot. How may I help you? \n\n! You can access the following services.\n 1.Available shops typing shops.\n 2.Available product by typing name of the product\n 3. type shop name to access products in that shop\n 4. for help type 'help'""")

# help command 
def help_command(update, context):
    update.message.reply_text('if you need help! You should ask for it on google')

# message handler 
def handle_message(update, context):
    text = str(update.message.text).lower()
    response = Res.sample_responses(text)

    update.message.reply_text(response)

# errror handler 
def error(update, context):
    print(f"Update {update} caused error {context.error}")
    
# main function 
def main():

     # Create the Updater and pass it your bot's token.
    updater = Updater(keys.API_KEY, use_context=True)

     # Get the dispatcher to register handlers
    dp = updater.dispatcher

     # Register the command handlers...
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("start", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # ...and the error handler
    dp.add_error_handler(error)

     # Start the Bot
    updater.start_polling()

     # Run the bot until you press Ctrl-C 
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

main()