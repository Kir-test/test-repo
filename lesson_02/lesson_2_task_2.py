def is_year_leap(year):
    return year % 4 == 0


year = 2024
result = is_year_leap(year)
print(f"год {year}: {result}")

year = 2023
result = is_year_leap(year)
print(f"год {year}: {result}")

# Другой вариант кода
year = 2024
result = is_year_leap(year)
print("год", year, ":", result)

year = 2023
result = is_year_leap(year)
print("год", year, ":", result)
