import re

text = input("Enter text: ")

match = re.search(r"\b[6-9]\d{9}\b", text)

if match:
    print("Mobile number:", match.group())
else:
    print("Mobile number not found")