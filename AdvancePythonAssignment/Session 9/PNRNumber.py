import re

def is_valid_pnr(pnr):
    return bool(re.match(r"^\d{10}$", pnr))

pnr = input("Enter PNR number: ")

if is_valid_pnr(pnr):
    print("Valid PNR")
else:
    print("Invalid PNR")