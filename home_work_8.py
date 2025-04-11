# Перше завдання

import requests  # Запит

from bs4 import BeautifulSoup as bs

class BooksToscrape:
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

    def getInfo(self,find):
        books = []
        item = self.soup.find_all("article", class_= "product_pod") # Те що є на сайті у консолі
        if not item:
            print("Помилка в пошуку на сторінці")
            return
        for i in books[0:4]:
            name = i.find("a", class_ = "a-light-in-the-attic_1000") # Те що є на сайті у консолі
            nameError = name.text() if name else "Відсутня назва"
            price = i.find("div", class_ = "col-sm-6 product_main") # Те що є на сайті у консолі
            priceError = price.text() if price else "Відсутня ціна"
            rating = i.find("p", class_ = "star-rating Three") # Те що є на сайті у консолі
            ratingError = rating.text() if rating else "Відсутній рейтинг"
            books.append(

                {
                    "Назва" : nameError,
                    "Ціна" : priceError,
                    "Рейтинг" : ratingError,
                }

            )

        return books

    def snowInfo(self, laptop):


        print("№\t\1","НАЗВА", "\t"*2, "ЦІНА", "t"*2, "РЕЙТИНГ", "\1"*2)
        print("-"*50)
        for i in laptop:


            print("\t", i("Назва"), "\t", i("Ціна"), "\t", i("Рейтинг"))

url = "https://books.toscrape.com/" # Посилання на сторінку сайта
obj = BooksToscrape(url)
obj.auditSite()
site = obj.getInfo()
if site:
       obj.snowInfo()
else:
    print("Жодної інформації не отримано")

# Друге завдання

import requests  # Запит

from bs4 import BeautifulSoup as bs

class TCH:
    def __init__(self, url):   # Вписуємо назву(посилання) сайту
        self.url = url
        self.header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/114.0.0.0 Safari/537.36' # Які сайти ми можемо відкривати
        }

    def text(self, soup):
        response = requests.get(self.url, headers = self.header)  # Надсилаємо запит
        soup = bs(response.text, "html.parser")

    def getInfo(self):
        text = []
        headers = self.soup.find_all("h2", class_= "c-title c-title--h3 text-2xl lg:mt-2 mb-7 hidden lg:block")
        if not text:
            print("Останні стрічки новин ТСН")
        return
    for i in text[0:5]:
            name = i.find("a", class_="c-entry__title c-title c-title--h1 font-bold")  # Те що є на сайті у консолі
            nameError = name.text() if name else "Відсутня стрічка"
            name2 = i.find("a", class_="c-entry__title c-title c-title--h1 font-bold")  # Те що є на сайті у консолі
            name2Error = name.text() if name else "Відсутня стрічка2"
            name3 = i.find("a", class_="c-entry__title c-title c-title--h1 font-bold")  # Те що є на сайті у консолі
            name3Error = name.text() if name else "Відсутня стрічка3"
            name4 = i.find("a", class_="c-entry__title c-title c-title--h1 font-bold")  # Те що є на сайті у консолі
            name4Error = name.text() if name else "Відсутня стрічка4"
            name5 = i.find("a", class_="c-entry__title c-title c-title--h1 font-bold")  # Те що є на сайті у консолі
            name5Error = name.text() if name else "Відсутня стрічка5"
            text.append(

                {
                    "Відсутня стрічка": nameError,
                    "Відсутня стрічка2": name2Error,
                    "Відсутня стрічка3": name3Error,
                    "Відсутня стрічка4": name4Error,
                    "Відсутня стрічка5": name5Error,

                }

            )

url = "https://tsn.ua/"
obj = TCH(url)
obj.text()
