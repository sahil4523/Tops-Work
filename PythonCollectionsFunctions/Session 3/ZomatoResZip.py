restaurants=['Burger Hub', 'Pizza Point', 'Sushi House']
delivery=[30, 25, 40]

for name, minutes in zip(restaurants, delivery):
    print(f"{name} - {minutes} min")