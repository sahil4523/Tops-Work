products=["Mobile", "Mouse", "Laptop", "Monitor", "Keyboard"]

result=list(filter(lambda x: x.startswith("M"), products))

print(result)