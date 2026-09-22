names = ['Shoes', 'Bag', 'Watch', 'Headphones']
prices = [999, 1500, 700, 2200]

result = [(name, price)
          for name, price in zip(names, prices)
          if price > 1000]

print(result)