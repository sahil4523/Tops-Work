user_bio="Music lover | Foodie | Traveller"

count = 0

for ch in user_bio:
    if ch != " ":
        count += 1

print("Number of characters:", count)

#"The for loop checks each character. The if statement skips spaces, and count += 1 increases the count for every other character."