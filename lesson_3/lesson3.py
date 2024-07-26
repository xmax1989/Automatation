from user import User
from card import Card

alex = User("Alex")
maks = User("Maks")
alina = User("Alina")


alex.sayName()
maks.sayAge()
alina.sayName()
maks.setAge(33)
maks.sayAge()

card = Card("5555 6666 7777 8888","11/28", "Maks B")


maks.addCard(card)
maks.getCard().pay(1000)

