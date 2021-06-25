import json
import requests
key = "17298b56d8282557b6d96de6cf9e08b7"
city_name = "Almaty"
URL = "http://api.openweathermap.org/data/2.5/weather"

parameters = {
    "q":city_name,
    "appid":key,
    "units":"metric"
}
data = requests.get(URL, params=parameters)
print(data.json())