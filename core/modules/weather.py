# get weather without using api key and without using any module or library in python 

import requests
from bs4 import BeautifulSoup

def weather(query):
    # QUERY--> weather in delhi
    query = query.replace("weather in", "")
    query = query.replace("temperature in", "")
    query = query.replace("climate in", "")
    query = query.replace(" ", "")
    query = query.lower()
    url = "https://www.google.com/search?q=weather+in+" + query
    r = requests.get(url)
    s = BeautifulSoup(r.text, "html.parser")
    update = s.find("div", class_="BNeawe").text
    return update
    