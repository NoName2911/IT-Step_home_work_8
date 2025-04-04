# Перша робота

#class Character:
#    def __init__(self, name, health):
#        self.__name = name
#        self.__health = health

#    def attack(self):
#        raise NotImplementedError("Цей метод має бути реалізований у підкласі.")

#    def take_damage(self, amount):
#        self.__health = max(0, self.__health - amount)

#    def is_alive(self):
#        return self.__health > 0

#    def get_name(self):
#        return self.__name

#    def get_health(self):
#        return self.__health


#class Warrior(Character):
#    def __init__(self, name):
#        super().__init__(name, 150)  # більше здоров'я

#    def attack(self):
#        print(self.get_name + "атакує мечем!")


#class Mage(Character):
#    def __init__(self, name):
#        super().__init__(name, 80)  # менше здоров'я

#    def attack(self):
#        print(self.get_name + "атакує магією!")


#warrior = Warrior("Артур")
#mage = Mage("Мерлін")

#print(warrior.attack())
#print(mage.attack())

#mage.take_damage(30)


# Друга робота

#class LibraryItem:
#    def __init__(self, title, author, item_id):
#        self.__title = title
#        self.__author = author
#        self.__item_id = item_id
#        self._is_checked_out = False

#    def get_title(self):
#        return self.__title

#    def get_author(self):
#        return self.__author

#    def get_item_id(self):
#        return self.__item_id

#    def is_same_item(self, other_item):
#        return self.__item_id == other_item.get_item_id()

#    def display_info(self):
#        return self.display_info

#    def check_out(self):
#        if not self._is_checked_out:
#            self._is_checked_out = True
#            print(self.__title + "видано.")
#        else:
#            print(self.__title + "вже у користуванні.")

#    def return_item(self):
#        if self._is_checked_out:
#            self._is_checked_out = False
#            print(self.__title + "повернено.")
#        else:
#            print(self.__title + "вже знаходиться у бібліотеці.")


#class Book(LibraryItem):
#    def __init__(self, title, author, item_id, pages):
#        super().__init__(title, author, item_id)
#        self.__pages = pages

#    def display_info(self):
#        print("Книга: " + self.get_title(), "Автор: " + self.get_author(), "Сторінки: " + self.__pages)


#class Magazine(LibraryItem):
#    def __init__(self, title, author, item_id, issue_number):
#        super().__init__(title, author, item_id)
#        self.__issue_number = issue_number

#    def display_info(self):
#        print("Журнал: " + self.get_title(), "Автор: " + self.get_author(), "Номер випуску: " + self.__issue_number)


#class Audiobook(LibraryItem):
#    def __init__(self, title, author, item_id, duration):
#        super().__init__(title, author, item_id)
#        self.__duration = duration

#    def display_info(self):
#        print("Аудіокнига:" + self.get_title(), "Автор:" + self.get_author(), "Тривалість: ", self.__duration, "хвилин")


#library_items = [
#    Book("Марвел", "Джо Сімпсон", 1, 28),
#    Magazine("Батьківщина", "Редакція", 2, 1945),
#    Audiobook("Гаррі Поттер", "Дж. К. Ролінг", 3, 720)
#]

#for item in library_items:
#    item.display_info()
#
#book = library_items[0]
#book.check_out()
#book.return_item()
