import re

email = input("Enter Gmail: ")

if re.match(r"^[a-z][a-zA-Z0-9._%+-]*@gmail\.com$", email):
    print("Valid Gmail")
else:
    print("Invalid Gmail")