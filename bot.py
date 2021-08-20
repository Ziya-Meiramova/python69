from telebot import *
from gtts import *
from random import *
import time

TOKEN = "1763733755:AAHRghKacreE8zScEQdBo3HfomdQKFFsjqo"

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def greeting(message):
    # bot.send_message(message.chat.id, "Hello")
    #INLINE KEYBOARD
    # клавиатура привязанная к сообщению, используется обратный вызов
    #CallbackQuerry, вместо отправки сообщения с обычной клавиатуры
    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text= "Хорошее", callback_data="aaa")
    btn2 = types.InlineKeyboardButton(text="Плохое", callback_data="bbb")
    keyboard.add(btn1)
    keyboard.add(btn2)
    bot.send_message(message.chat.id, "Какое у тебя настроение?", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def keyboard_click(call):
    if call.data == "aaa":
        text_audio = "Отлично"
        speech = gTTS(text= text_audio, lang="ru", slow=False)
        speech.save("audio.mp3")
        f = open("audio.mp3", "rb")
        bot.send_audio(call.message.chat.id, f)

        f = open("2.jpg", "rb")
        bot.send_photo(call.message.chat.id, f)


        # bot.send_message(call.message.chat.id, "Hello")
    elif call.data == "bbb":
        bot.send_message(call.message.chat.id, "Bye")
        text_audio = "Все будет хорошо"
        speech = gTTS(text=text_audio, lang="ru", slow=False)
        speech.save("audio.mp3")
        f = open("audio.mp3", "rb")
        bot.send_audio(call.message.chat.id, f)

        f = open("1.jpg", "rb")
        bot.send_photo(call.message.chat.id, f)

@bot.message_handler(content_types=['text'])
def handling(message):
    if message.text == "random":
        bot.send_message(message.chat.id, randint(1, 100) )
    elif message.text == "У меня сегодня др":
        bot.send_message(message.chat.id, "С днем рождения!")
    elif message.text == "time":
        bot.send_message(message.chat.id, time.asctime())



bot.polling()
