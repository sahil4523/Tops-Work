def display_friends(friends):
    for username, followers in friends.items():
        print(username + ":", followers, "followers")


friends = {
    "Krupa": "2.3K",
    "Sahil": "1.5K",
    "Nidhi": "3.1K"
}

display_friends(friends)