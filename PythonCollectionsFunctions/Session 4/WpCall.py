calls=(12, 5, 0, 20, 7, 3, 15)

calls=[x for x in calls if x >= 5]

calls=tuple(calls)

print(calls)