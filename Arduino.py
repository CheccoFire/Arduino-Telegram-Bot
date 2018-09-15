import telepot
import time
from nanpy import ArduinoApi, SerialManager
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton


connection = SerialManager(device='COM3') #eventualmente cambiare la porta COM3 
a = ArduinoApi(connection=connection)     #con quella effettivamente usata
a.pinMode(12, a.OUTPUT)
a.pinMode(11, a.OUTPUT)
a.pinMode(10, a.OUTPUT)
a.pinMode(9, a.OUTPUT)

def on_chat_message(msg): #crea la tastiera personalizzata
    content_type, chat_type, chat_id = telepot.glance(msg)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Blu", callback_data='/blu'), InlineKeyboardButton(text="Rosso", callback_data='/rosso')],
                                     [InlineKeyboardButton(text="Verde", callback_data='/verde'), InlineKeyboardButton(text="Giallo", callback_data='/giallo')]])

    bot.sendMessage(chat_id, 'Source creata da Checco_Fire (@LordMystery) GitHub: https://github.com/CheccoFire/ArduinoTelegramBot/', reply_markup=keyboard)
            

def on_callback_query(msg): #aziona i vari LED in base al pulsante toccato
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)
    
    if query_data == '/blu':
         if a.digitalRead(12)==0:
                a.digitalWrite(12, 1)
                bot.answerCallbackQuery(query_id, text='Blu acceso')
         else:
                    a.digitalWrite(12, 0)
                    bot.answerCallbackQuery(query_id, text='Blu spento')
    elif query_data == '/rosso':
                        if a.digitalRead(9)==0:
                            a.digitalWrite(9, 1)
                            bot.answerCallbackQuery(query_id, text='Rosso acceso')
                        else:
                            a.digitalWrite(9, 0)
                            bot.answerCallbackQuery(query_id, text='Rosso spento')
                
    elif query_data == '/verde':
            if a.digitalRead(10)==0:
                a.digitalWrite(10, 1)
                bot.answerCallbackQuery(query_id, text='Verde acceso')
            else:
                a.digitalWrite(10, 0)
                bot.answerCallbackQuery(query_id, text='Verde spento')
                
    elif query_data == '/giallo':
            if a.digitalRead(11)==0:
                a.digitalWrite(11, 1)
                bot.answerCallbackQuery(query_id, text='Giallo acceso')
            else:
                a.digitalWrite(11, 0)
                bot.answerCallbackQuery(query_id, text='Giallo spento')


bot=telepot.Bot('- BOT TOKEN -')
bot.message_loop({'chat': on_chat_message,
                  'callback_query': on_callback_query})
print ('Listening ...')

while 1:
    time.sleep(10)
