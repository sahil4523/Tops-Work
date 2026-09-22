usernames=["sahil", "guddi", "nidhi"]
followers=[1500, 1200, 800]

users = {}

for i in range(len(usernames)):
    users[usernames[i]] = followers[i]

print(users)