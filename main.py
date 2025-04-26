from bs4 import BeautifulSoup
import requests
import csv
url="https://www.amazon.com/Lululemon-Everywhere-Belt-Bag-Black/dp/B08V79CRMH"
responce=requests.get(url)
soup=BeautifulSoup(responce.text,'html.parser')
with open("soup.txt",'w')as file:
    file.write(soup.prettify())
