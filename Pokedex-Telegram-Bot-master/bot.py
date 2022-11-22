from typing import Text
from telegram.ext import *
import config_file
from pokedex import pokedex
import json
from telegram import ReplyKeyboardMarkup


    

#start command
def start_command(update,context):
    username = update.message.chat.first_name
    segundo = update.message.chat.last_name
    update.message.reply_text(f"Olá, treinardor: {username} {segundo} \nBem-vindo ao mundo dos Pokémons. Um lugar repleto de criaturas incriveis esperando por você. \nDigite um nome ou ID válido de um Pokémon (até 890) para começar ou se tiver duvidas digite (/help)")
     
#error handling
def error(update,context):
    print(f"{update} caused error {context.error}")
#help command
def help_command(update,context):
    
    update.message.reply_text("Olá esse bot é simples vc vai digitar o nome ou o numero do pokemon que você quer para ver as informações")
#message response
def message_response(update,context):

    text = str(update.message.text).lower()
    username = update.message.chat.first_name
    
    print(username)


    if text in ("oi", "olá", "yo", "e aí"):
        response = (f"<b> Como você está {username}. Digite um nome ou id de Pokémon para obter informações </b>")

    else:
        response,photo_url = pokedex(text)
        if response != None and photo_url != None:
            chat_id = update.message.chat_id
            context.bot.send_photo(chat_id=chat_id,photo=photo_url)
        else:
            response = " Desculpe, não entendi oque você quer. Digite um nome de Pokémon<b> válido </b> ou <b> ID (até 890) </b> para obter informações"

           

    update.message.reply_text(response,parse_mode='HTML')

def main():
    updater = Updater(config_file.api_key,use_context = True)
    dp = updater.dispatcher
    #adding all the command handler,message handler and error handler
    dp.add_handler(CommandHandler("start",start_command))
    dp.add_handler(CommandHandler("help",help_command))
    dp.add_handler(MessageHandler(Filters.text,message_response))
    dp.add_error_handler(error)
    #look for update every 3 seconds
    updater.start_polling(3)
    updater.idle()
    print(help)
    
print("Bot started running")

if __name__ == "__main__":
    main()

print(main)