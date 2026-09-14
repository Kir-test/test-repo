from address import Address
from mailing import Mailing

from_address = Address("123456", "Москва", "Ленина", "10", "5")
to_address = Address("654321", "Санкт-Петербург", "Невский проспект", "20", "12")

my_mailing = Mailing(to_address, from_address, 350, "RA123456789RU")

print(
    f"Отправление {my_mailing.track} "
    f"из {my_mailing.from_address.index}, {my_mailing.from_address.city}, "
    f"{my_mailing.from_address.street}, {my_mailing.from_address.house} - "
    f"{my_mailing.from_address.apartment} "
    f"в {my_mailing.to_address.index}, {my_mailing.to_address.city}, "
    f"{my_mailing.to_address.street}, {my_mailing.to_address.house} - "
    f"{my_mailing.to_address.apartment}. "
    f"Стоимость {my_mailing.cost} рублей."
)
