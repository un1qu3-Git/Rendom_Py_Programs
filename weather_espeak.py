import json
import requests
import os

def weather():
    city = input("Enter your city: ")
    url = f"http://api.weatherapi.com/v1/current.json?key=f3dec116e7564ce8bba222747232307&q={city}"
    r = requests.get(url)
    wdic = json.loads(r.text)
    temperature_celsius = wdic["current"]["temp_c"]
    print(f"Current temperature in {city}: {temperature_celsius}°C")

    # text weather information to speech using espeakkk
    os.system(f"espeak 'Current temperature in {city} is {temperature_celsius} degrees Celsius.'")

weather()
