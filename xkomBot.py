from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time
#Wpisz tutaj link
URL = 'https://www.x-kom.pl/p/1071030-smartwatch-apple-watch-se-2-40-starlight-aluminum-starlight-sport-gps.html?gclid=CjwKCAjws7WkBhBFEiwAIi168ws7T0Z6fFxqwFKPVRxAZglivOdikGMQyVl9GtJkDGD3lAXo7NAYFhoCJykQAvD_BwE'

TOKEN = ""
chat_id = ""
message = f"Cena zegarka spadła: {URL}"
chat_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"


headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    #Wpisz nazwe klasy nazwy produktu
    title = soup.find("h1", class_="sc-1bker4h-4 hMQkuz").get_text()
    #Wpisz nazwe klasy ceny
    price = soup.find("div", class_="hYfBFq").get_text()
    converted_price = float(price.replace(" ", "").replace(",", ".").replace("zł", ""))
    if(converted_price < 1500):
        print("Cena spadłą!")
        print(URL)

    print(title.strip())
    print(converted_price)
    print(requests.get(chat_url).json())

while(True):
    check_price()
    time.sleep(360)