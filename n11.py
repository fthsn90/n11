import requests
from bs4 import BeautifulSoup
import re
import string



url = "https://www.n11.com/bilgisayar"

response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, "lxml")

liler = soup.findAll("li",attrs={"class":"column"}) 

for i in liler:
    urunadi = i.find("div",attrs={"class":"pro"}).text
    fiyat = i.find("ins").text
    fiyat1 = fiyat.translate({ord(c): None for c in string.whitespace}) # BOŞLUK FELAN BIRAKMA LA
    print("***********************************************")
    print("Ürün Adı: {}\n".format(re.sub(r"\s+", " ", urunadi), sep=' ')) # Boşluk
    print("Fiyatı  : {}".format(fiyat1))