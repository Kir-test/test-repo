from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 15", "+79161234567"))
catalog.append(Smartphone("Samsung", "Galaxy S23", "+79261234567"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 12", "+79361234567"))
catalog.append(Smartphone("Huawei", "P50", "+79461234567"))
catalog.append(Smartphone("Google", "Pixel 8", "+79561234567"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
