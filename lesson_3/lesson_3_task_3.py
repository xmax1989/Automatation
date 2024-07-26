from address import Address
from mailing import Mailing

to_address = Address("35350", "Москва", "Королева", "12", "36")
from_address = Address("31031", "Тверь", "Пушкина", "3", "12")
mailing = Mailing(to_address, from_address, 400, "247891")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city},"
      f" ул.{mailing.from_address.street}, дом {mailing.from_address.house} кв {mailing.from_address.apartment}."
      f" В {mailing.to_address.index}, {mailing.to_address.city}, ул.{mailing.to_address.street}, "
      f" дом {mailing.to_address.house} кв {mailing.to_address.apartment}, Стоимомть {mailing.cost} рублей.")