def mask_phone_number(phone):
    return "*" * 6 + phone[-4:]

phone = input("Enter 10-digit phone number: ")
print(mask_phone_number(phone))