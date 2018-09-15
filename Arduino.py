import telepot
import time
import json
from nanpy import ArduinoApi, SerialManager
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

bannati = [] #Inserisci qui gli id dei utenti bannati

connection = SerialManager(device='COM3') #eventualmente cambiare la porta COM3 
a = ArduinoApi(connection=connection)     #con quella effettivamente usata
a.pinMode(12, a.OUTPUT)
a.pinMode(11, a.OUTPUT)
a.pinMode(10, a.OUTPUT)
a.pinMode(9, a.OUTPUT)

def onchatmessage(msg):
 from_id = msg["from"]["id"]
 if from_id in bannati:
  bot.sendMessage(from_id, "Sei stato bandito dall' utilizzo di questo bot")
 else:
    content_type, chat_type, chat_id = telepot.glance(msg)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Blu", callback_data='/blu'), InlineKeyboardButton(text="Rosso", callback_data='/rosso')],
                                     [InlineKeyboardButton(text="Verde", callback_data='/verde'), InlineKeyboardButton(text="Giallo", callback_data='/giallo')]])

    bot.sendMessage(chat_id, 'Creato da Checco_Fire (@LordMystery)!\n Source Code: https://github.com/CheccoFire/ArduinoTelegramBot', reply_markup=keyboard)
            

def on_callback_query(msg): #aziona i vari LED in base al pulsante toccato
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    
    if query_data == '/blu' and from_id != bannati:
         if a.digitalRead(12)==0:
                a.digitalWrite(12, 1)
                print("Log => Led Blu Acceso! | Da =>", from_id)
                bot.answerCallbackQuery(query_id, text='Blu acceso')
                bot.sendMessage(231454335, 'Log => Led Blu Acceso!\n\nUsername => @'+msg["from"]["username"]+'\nID => '+str(from_id))
         else:
                    a.digitalWrite(12, 0)
                    print("Log => Led Blu Spento! | Da =>", from_id)
                    bot.answerCallbackQuery(query_id, text='Blu spento')
                    bot.sendMessage(231454335, 'Log => Led Blu Spento!\n\nUsername => @'+msg["from"]["username"]+'\nID => '+str(from_id))
    elif query_data == '/blu' and from_id in bannati:  
          bot.answerCallbackQuery(query_id, text='Sei stato bannato')
    elif query_data == '/rosso' and from_id in bannati:  
          bot.answerCallbackQuery(query_id, text='Sei stato bannato')
    elif query_data == '/giallo' and from_id in bannati:  
          bot.answerCallbackQuery(query_id, text='Sei stato bannato')
    elif query_data == '/verde' and from_id in bannati:  
          bot.answerCallbackQuery(query_id, text='Sei stato bannato')
    elif query_data == '/rosso':
                        if a.digitalRead(9)==0:
                            a.digitalWrite(9, 1)
                            print("Log => Led Rosso Acceso! | Da =>", from_id)
                            bot.answerCallbackQuery(query_id, text='Rosso acceso')
                            bot.sendMessage(231454335, 'Log => Led Rosso Acceso!\n\nUsername => @'+msg["from"]["username"]+'\nID => '+str(from_id))
                        else:
                            a.digitalWrite(9, 0)
                            print("Log => Led Rosso Spento! | Da =>", from_id)
                            bot.sendMessage(231454335, 'Log => Led Rosso Spento!\n\nUsername => @'+msg["from"]["username"]+'\nID => '+str(from_id))
                            bot.answerCallbackQuery(query_id, text='Rosso spento')
                
    elif query_data == '/verde':
            if a.digitalRead(10)==0:
                a.digitalWrite(10, 1)
                bot.answerCallbackQuery(query_id, text='Verde acceso')
                bot.sendMessage(231454335, 'Log => Led Verde Acceso!\n\nUsername => @'+msg["from"]["username"]+'\nID => '+str(from_id))
                print("Log => Led Verde Acceso! | Da =>", from_id)
            else:
                a.digitalWrite(10, 0)
                print("Log => Led Verde Spento! | Da =>", from_id)
                bot.sendMessage(admin, 'Log => Led Verde Spento!\n\nUsername => @'+msg["from"]["username"]+'\nID => '+str(from_id))
                bot.answerCallbackQuery(query_id, text='Verde spento')
                
    elif query_data == '/giallo':
            if a.digitalRead(11)==0:
                a.digitalWrite(11, 1)
                print("Log => Led Giallo Acceso! | Da =>", from_id)
                bot.sendMessage(231454335, 'Log => Led Giallo Acceso!\n\nUsername => @'+msg["from"]["username"]+'\nID => '+str(from_id))
                bot.answerCallbackQuery(query_id, text='Giallo acceso')
            else:
                a.digitalWrite(11, 0)
                print("Log => Led Giallo Spento! | Da =>", from_id)
                bot.sendMessage(231454335, 'Log => Led Giallo Spento!\n\nUsername => @'+msg["from"]["username"]+'\nID => '+str(from_id))
                bot.answerCallbackQuery(query_id, text='Giallo spento')

msg = ["text"]
bot=telepot.Bot('Inserisci la token qui') #Inserisci qui la token fornita da BotFather
bot.message_loop({'chat': onchatmessage, 'callback_query': on_callback_query})
print ('Bot Avviato Con Successo...')
print ('Console Avviata Con Successo...')
print ('Ora ti avvertirò di ogni cosa che succede')
print ('')

while 1:
    time.sleep(10)
