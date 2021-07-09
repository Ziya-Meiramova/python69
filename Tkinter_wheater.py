import json
from tkinter import *
import requests

window = Tk()
window.geometry('500x500')

input1 = Entry(window)
input1.grid(row='0', column='0')

label_city = Label(window, text="City: ", bg='grey')
label_city.grid(row='1', column='0')
label_temp = Label(window, text="Tempreture: ", bg='grey')
label_temp.grid(row='2', column='0')

label_city_value = Label(window,text = "CITY", bg='pink')
label_city_value.grid(row='1', column='1')
label_temp_value=Label(window, text='TEMP', bg='pink')
label_temp_value.grid(row='2', column='1')

def get_wheather():
    key = "17298b56d8282557b6d96de6cf9e08b7"
    city_name = input1.get()
    URL = "https://api.openweathermap.org/data/2.5/weather"

    parameters = {
        "q": city_name,
        "appid": key,
        "units": "metric"
    }
    data = requests.get(URL, params=parameters)
    label_city_value.configure(text=city_name)
    label_temp_value.configure(text=data.json()['main']['temp'])


btn1 = Button(window, text='Click', command=get_wheather)
btn1.grid(row='0', column='4')
window.mainloop()