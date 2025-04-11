# Шаблон сайту

#import requests  # Запит

#from bs4 import BeautifulSoup as bs

#class Name:
#    def __init__(self, url):   # Вписуємо назву(посилання) сайту
#        self.url = url
#        self.header = {
#        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/114.0.0.0 Safari/537.36' # Які сайти ми можемо відкривати
#        }
#        self.soup = None

#    def auditSite(self):
#        response = requests.get(self.url, headers = self.header)  # Надсилаємо запит
#        if response.status_code == 200:
#            self.soup = bs(response.text, "html.parser")
#        else:
#            print("Не вдалося підключитися на сервер")

#    def getInfo(self):
#        pass
#    def snowInfo(self):
#        pass

#url = "Посилання"
#obj = Name(url)
#obj.auditSite()
#site = obj.getInfo()
#if site:
#    obj.snowInfo()
#else:
#    print("Жодної інформації не отримано")



# Тестуємо роботу з посиланням

import requests  # Запит

from bs4 import BeautifulSoup as bs

class Comfy:
    def __init__(self, url):   # Вписуємо назву(посилання) сайту
        self.url = url
        self.header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/114.0.0.0 Safari/537.36' # Які сайти ми можемо відкривати
        }


    def auditSite(self):
        response = requests.get(self.url, headers = self.header)  # Надсилаємо запит
        if response.status_code == 200:
            self.soup = bs(response.text, "html.parser")
        else:
            print("Не вдалося підключитися на сервер")

    def getInfo(self,):
        laptop = []
        lap = self.soup.find_all("div", class_= "products catalog") # Те що є на сайті у консолі
        if not lap:
            print("Помилка в пошуку на сторінці")
            return
        for i in laptop[0:4]:
            name = i.find("a", class_ = "prdl-item__name ellipsis-2-lines") # Те що є на сайті у консолі
            nameError = name.text() if name else "Відсутня назва"
            price = i.find("div", class_ = "products-list-item-price__actions-price-current") # Те що є на сайті у консолі
            priceError = price.text() if price else "Відсутня ціна"
            discount = i.find("span", class_ = "products-list-item-price__actions-price-discount") # Те що є на сайті у консолі
            discountError = discount.text() if discount else "Відсутня знижка"
            laptop.append(

                {
                    "Назва" : nameError,
                    "Ціна" : priceError,
                    "Знижка" : discountError,
                }

            )

        return laptop

    def snowInfo(self, laptop):


        print("№\t\1","НАЗВА", "\t"*2, "ЦІНА", "t"*2, "ЗНИЖКА", "\1"*2)
              print("-"*50)
                for i in laptop:


            print("\t", i("Назва"), "\t", i("Ціна"), "\t", i("Знижка"))

url = "https://comfy.ua/ua/noutbuk-igrovoj-asus-tuf-gaming-a15-fa506nfr-hn008-graphite-black.html" # Посилання на сторінку сайта
obj = Comfy(url)
obj.auditSite()
site = obj.getInfo()
if site:
       obj.snowInfo()
       else:
    print("Жодної інформації не отримано")


# Вдруге тестуємо роботу

#import requests  # Запит

#from bs4 import BeautifulSoup as bs

#class Coin:
#    def __init__(self, url):   # Вписуємо назву(посилання) сайту
#        self.url = url
#        self.header = {
#        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/114.0.0.0 Safari/537.36' # Які сайти ми можемо відкривати
#        }
#        self.soup = None

#    def auditSite(self):
#        response = requests.get(self.url, headers = self.header)  # Надсилаємо запит
#        if response.status_code == 200:
#            self.soup = bs(response.text, "html.parser")
#        else:
#            print("Не вдалося підключитися на сервер")

#    def getInfo(self):
#        coins = []
#        listCoin = self.soup.find("tbody")
#        if not listCoin:
#            print("Помилка в пошуку інформації")
#            return coins
#        info = listCoin.find_all("tr")[0:5]
#        for i in info:
#            name = i.find("p", class_ = "sc-65e7f566-0 lsTl")

#    def snowInfo(self):
#        pass

#url = "Посилання"
#obj = Coin(url)
#obj.auditSite()
#site = obj.getInfo()
#print("ТОП-5 найпопулярніших криптомонет")
#if site:
#    obj.snowInfo(site)
#else:
#    print("Жодної інформації не отримано")
