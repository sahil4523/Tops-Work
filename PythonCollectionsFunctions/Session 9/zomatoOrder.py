prices=[120, 250, 99, 180, 310]

new_prices=list(map(lambda x: x+x*10/100, prices))

print(new_prices)