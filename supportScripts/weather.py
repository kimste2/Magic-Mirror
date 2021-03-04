 # weather.py
import json
import requests
import math
from datetime import datetime
import os 
def getWeather():
    weather = ""

    fileName = "/home/pi/Documents/microblog/supportScripts/config/config.txt"
    
    with open(fileName) as f:
        content = f.readlines()
    f.close()
    
    key = str(content[0]).strip()
    apiParameter = "api.openweathermap.org/data/2.5/weather?zip=01776,us&appid="+ key + "&units=imperial"

    response = requests.get("http://" + apiParameter)

    if response.status_code == 200:
        jsonString = json.loads(response.text)
    else:
        print("Error, status code is " + str(response.status_code))
        exit(1)
        
    now = datetime.now()
    current_date = now.strftime("%m/%d/%Y")
    current_time = now.strftime("%H:%M:%S")
    weather = "Current time is {time} on {date}.\n".format(time=current_time, date=current_date)

    currentWeather = jsonString["weather"][0]["main"].lower()
    weather += """Current weather is {weather}.\n""".format(weather=currentWeather)

    currentTemperature = str(math.ceil(jsonString["main"]["temp"]))
    feelsLike = str(math.ceil(jsonString["main"]["feels_like"]))
    weather +="Current temperature is {cTemp} (Fahrenheit) but feels like {fTemp} (Fahrenheit).\n".format(cTemp=currentTemperature, fTemp=feelsLike)

    currentHumidity = str(jsonString["main"]["humidity"])
    weather += "The current humidity level is {humidity}%.\n".format(humidity=currentHumidity)
    #print(weather)
    return weather

if __name__ == "__main__":
    getWeather()
