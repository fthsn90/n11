import requests
from bs4 import BeautifulSoup
import re
import string

class n11():
    def __init__(self,kate):
        self.url = "https://www.n11.com/"+str(kate)
        self.response = requests.get(self.url)
        self.html = self.response.content
        self.soup = BeautifulSoup(self.html, "lxml")

    def vericek(self):
        self.liler = self.soup.findAll("li",attrs={"class":"column"})
        for i in self.liler:
            self.urunadi = i.find("div",attrs={"class":"pro"}).text
            self.fiyat = i.find("ins").text
            self.fiyat1 = self.fiyat.translate({ord(c): None for c in string.whitespace}) # BOŞLUK FELAN BIRAKMA LA
            print("***********************************************")
            print("Ürün Adı: {}\n".format(re.sub(r"\s+", " ", self.urunadi), sep=' ')) # Boşluk
            print("Fiyatı  : {}".format(self.fiyat1))


ne = input("Çekmek istediğiniz kategoriyi giriniz:")
vss = n11(ne)
vss.vericek()