# swanson.py
import requests

def get1Quote():
    link = "http://ron-swanson-quotes.herokuapp.com/v2/quotes"
    response = requests.get(link)
    if response.status_code != 200:
        print("Error getting code")
        exit(1)

    else:
        quote = response.text.strip("[]")
        return quote
