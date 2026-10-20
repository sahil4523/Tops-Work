f = open("orders.txt", "w")

f.write("Order 1: Mobile\n")
f.write("Order 2: Laptop\n")
f.write("Order 3: Headphones\n")
f.write("Order 4: Keyboard\n")
f.write("Order 5: Mouse\n")

f.close()

f = open("orders.txt", "r")

while True:
    line=f.readline()

    if not line:
        break

    print(line.strip())
    print("File pointer position:", f.tell())

f.close()