# from telebot import *
# import requests
#
# TOKEN = "1903269438:AAGqEZs-uF48m0ZCHA9E2FLXV7zhx1idBCU"
#
# bot = TeleBot(TOKEN)
#
# KEY = "17298b56d8282557b6d96de6cf9e08b7"
# URL = "http://api.openweathermap.org/data/2.5/weather"
#
# @bot.message_handler(commands=['hello'])
# def greeting(message):
#     bot.send_message(message.chat.id, "Hello")
#
# @bot.message_handler(content_types=['text'])
# def get_wheather(message):
#     city = message.text.capitalize()
#     params = {
#         'q':city,
#         'appid':KEY,
#         'units':'metric'
#     }
#     data = requests.get(URL, params)
#     data = data.json()
#     print(data)
#     temp = data['main']['temp']
#     bot.send_message(message.chat.id, temp)
#
#
#
# bot.polling()
