from cgitb import text
import telebot
import config
import requests
from lxml import  etree
import lxml.html



def parse(url):
    api = requests.get(url)
    tree= lxml.html.document_fromstring(api.text)
    anekdots=tree.xpath('/html/body/div[2]/div/main/article/div[0]/pre/text()') 
    print("!!")
    print(anekdots)
    return anekdots

def get_username(message):
    usr = bot.get_chat_member(message.chat.id, message.from_user.id)
    if not usr.user.username:
        return usr.user.first_name
    else:
        return '@'+usr.user.username


bot= telebot.TeleBot(config.TOKEN)
@bot.message_handler(content_types=['text'])
def Mess(message):
    print('['+get_username(message)+']====='+'["'+message.text+'"]')
    if(message.text=='привет'):
        bot.send_message(message.chat.id,'привет лох')
    elif(message.text=='/start'):
        bot.send_message(message.chat.id,'смотри, ты мне пишешь любой текст, а я тебе смешной анекдот ;)')
    elif(message.text=='катя' or message.text=='Катя'):
        bot.send_message(message.chat.id,'Катя, иди спать:)')
    elif(message.text=='Яна' or message.text=='яна'):
            bot.send_message(message.chat.id,'Ты котек <3')  
        
  
    else:
        bot.send_message(message.chat.id, parse('https://odessa-flat.com/anekdot'))
    
bot.polling(non_stop=True)    

