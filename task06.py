def is_valid_phone_number(phone: str):
    return len(phone) == 9 and phone.isdigit()

phone = input("Telefon raqamini kiriting: ")

if is_valid_phone_number(phone):
    print(True)
else:
    print(False)