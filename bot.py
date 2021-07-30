from telebot import *
import random, time
from gtts import *
import requests

TOKEN = "1903269438:AAGqEZs-uF48m0ZCHA9E2FLXV7zhx1idBCU"

bot = TeleBot(TOKEN)

KEY = "17298b56d8282557b6d96de6cf9e08b7"
URL = "http://api.openweathermap.org/data/2.5/weather"

@bot.message_handler(content_types=['text'])
def get_wheather(message):
    city_list=["Almaty", "Moscow", "Astana"]
    city = message.text.capitalize()
    for i in city_list:
        if i == city:
            pass

    params = {
        'q':city,
        'appid':KEY,
        'units':'metric'
    }
    data = requests.get(URL, params)
    data = data.json()
    print(data)
    temp = data['main']['temp']
    bot.send_message(message.chat.id, temp)

@bot.message_handler(commands=['start'])
def greeting(message):
    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='time', callback_data="btn1")
    btn2 = types.InlineKeyboardButton(text='img', callback_data="btn2")
    keyboard.add(btn1)
    keyboard.add(btn2)
    bot.send_message(message.chat.id, "выберите команду: ", reply_markup=keyboard)

@bot.callback_query_handler(func= lambda call:True)
def click(call):
    if call.data == "btn1":
        bot.send_message(call.message.chat.id, time.asctime())
    elif call.data == "btn2":
        f = open("python.jpg", 'rb')
        bot.send_photo(call.message.chat.id, f)

@bot.message_handler(commands=['time'])
def getTime(message):
    bot.send_message(message.chat.id, str(time.asctime()))

@bot.message_handler(commands=['image'])
def get_image(message):
    f = open("python.jpg", 'rb')
    bot.send_photo(message.chat.id, f)

@bot.message_handler(content_types=['text'])
def handler(message):
    if message.text == "random":
        bot.send_message(message.chat.id, random.randint(1, 100))
    else:
        text = message.text
        speech = gTTS(text=text, lang='en', slow=False)
        speech.save("audio.mp3")
        f = open("audio.mp3", 'rb')
        bot.send_audio(message.chat.id, f)


bot.polling()
