def format_follower_count(num):
    if num >= 1000000:
        return str(num / 1000000) + "M"
    elif num >= 1000:
        return str(num / 1000) + "K"
    else:
        return str(num)

print(format_follower_count(1500))
print(format_follower_count(1200000))