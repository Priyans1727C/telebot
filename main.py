import telebot
import telegram
import openai


TELEGRAM_BOT_TOKEN = '***********************************************'
OPENAI_API_KEY = '****************************************************'
bot =telebot.TeleBot(Token)


import telegram
from telegram.ext import Updater, MessageHandler, Filters
import openai

# Set up your Telegram bot using your bot token
bot = telegram.Bot(token='YOUR_TELEGRAM_BOT_TOKEN')  # Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual token

# Set up your OpenAI API key
openai.api_key = openai_token  # Replace 'YOUR_OPENAI_API_KEY' with your actual key

# Define a function to respond to text messages
def respond_to_message(update, context):
    user_message = update.message.text  # Get the user's message
    # Call the OpenAI API to get a response from ChatGPT
    response = openai.Completion.create(
        engine="text-davinci-002",  # Choose the appropriate engine
        prompt=user_message,
        max_tokens=50  # You can adjust the response length
    )
    bot_response = response.choices[0].text  # Get the ChatGPT response
    # Send the response back to the user on Telegram
    update.message.reply_text(bot_response)

# Set up the Telegram bot's message handler
updater = Updater(token=Token, use_context=True)  # Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual token
dispatcher = updater.dispatcher

# Create a message handler for text messages
message_handler = MessageHandler(Filters.text & ~Filters.command, respond_to_message)
dispatcher.add_handler(message_handler)

# Start the Telegram bot
updater.start_polling()
updater.idle()



@bot.message_handler(['start','begin'])
def start(message):
    bot.reply_to(message,"hello priyanshu singh")



@bot.message_handler()
def costom(message):
        # msg=eval(message)
        msg=message.text
        if(msg in['hello','hi','Hello','Hi']):
            bot.reply_to(message,"Hi, how i can assist you!")
        elif(msg in['what is your name?']):
            bot.reply_to(message,'i am Anuj')
        else:
            bot.reply_to(message,'ujjwall chutiya hai')
        
            
        
bot.polling()
