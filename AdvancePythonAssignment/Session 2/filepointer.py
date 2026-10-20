f = open("lyrics.txt", "r")

print("Position before reading:", f.tell())

data = f.read(10)
print("First 10 characters:", data)

print("Position after reading:", f.tell())

f.close()