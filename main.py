from telebot import*
from gtts import *
token = "1903269438:AAGqEZs-uF48m0ZCHA9E2FLXV7zhx1idBCU"

bot = TeleBot(token)

@bot.message_handler(commands=["start"])
def greeting(message):
    pass
    # bot.send_message(message.chat.id, "Hello")
    # print(message)

    # keyboard = types.ReplyKeyboardMarkup(False)
    #
    # btn1 = types.KeyboardButton(text="Hello")
    # keyboard.add(btn1)
    # btn2 = types.KeyboardButton(text="Bye")
    # keyboard.add(btn2)
    # bot.send_message(message.chat.id, "hello", reply_markup=keyboard)

@bot.message_handler(content_types=["text"])
def handling(message):
    if message.text == "month":
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="January", callback_data="Jan")
        btn2 = types.InlineKeyboardButton(text="February", callback_data="Feb")
        btn3 = types.InlineKeyboardButton(text="March", callback_data="Mar")
        btn4 = types.InlineKeyboardButton(text="April", callback_data="Apr")
        btn5 = types.InlineKeyboardButton(text="May", callback_data="May")
        keyboard.add(btn1)
        keyboard.add(btn2)
        keyboard.add(btn3)
        keyboard.add(btn4)
        keyboard.add(btn5)
        bot.send_message(message.chat.id, "Choose month", reply_markup=keyboard)

    #bot.send_message(message.chat.id, message.text)
    # if message.text == "Ziya":
    #     bot.send_message(message.chat.id, "Hello Ziya")
    # else:
    #     bot.send_message(message.chat.id, "Hello, " + message.text)

    # text = message.text
    # speech = gTTS(text=text, lang='en', slow=False)
    # speech.save("audio.mp3")
    # f = open("audio.mp3", 'rb') #'rb' чтение файла в виде gTTs
    # bot.send_audio(message.chat.id, f)

@bot.callback_query_handler(func=lambda call: True)

def month_handler(call):
    if call.data == "Jan":
        bot.send_message(call.message.chat.id, "In January 31 days")
    elif call.data == "Feb":
        bot.send_message(call.message.chat.id, "In February 28-29 days")
    elif call.data == "Mar":
        bot.send_message(call.message.chat.id, "In March 31 days")
    elif call.data == "Apr":
        bot.send_message(call.message.chat.id, "In April 30 days")
    elif call.data == "May":
        bot.send_message(call.message.chat.id, "In May 31 days")
bot.polling()

