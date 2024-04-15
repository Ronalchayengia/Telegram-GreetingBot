import logging
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext, filters 

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

async def greet_new_user(update: Update, context: CallbackContext) -> None:
    # Get the new user's name
    new_user = update.message.new_chat_members[0]
    new_user_name = new_user.first_name

    bot_message = "Blip blop"
    greeting_message = context.chat_data.get("greeting_message", "welcome to")
 
    # Send the greeting message to the chat
    await update.message.reply_text(f"{bot_message} {greeting_message} {update.message.chat.title}, @{new_user_name}")
   
async def goodbye(update: Update, context: CallbackContext) -> None:
    # Get the new user's name
    left_user = update.message.left_chat_member
    left_user_name = left_user.first_name

    
    bot_message = "Goodbye"
    greeting_message = context.chat_data.get("greeting_message", "left the group")

    # Send the goodbye message to the chat
    await update.message.reply_text(f"{bot_message} , @{left_user_name}  {greeting_message} ")
       
    
def main(): 
    # your bot token
    application = Application.builder().token("token here").build()

    
    # application.add_handler(MessageHandler(filters.TEXT& ~filters.COMMAND, echo))
    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, greet_new_user), group=1)
    application.add_handler(MessageHandler(filters.StatusUpdate.LEFT_CHAT_MEMBER, goodbye), group=1)
 
    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
