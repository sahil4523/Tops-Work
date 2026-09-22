calculate=lambda a, b: (a + b, a * b)

pairs=[(3, 4), (5, 2), (7, 8)]

for a, b in pairs:
    print(calculate(a, b))