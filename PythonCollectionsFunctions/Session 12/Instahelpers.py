def format_likes(count):
    if count >= 1000000:
        return f"{count / 1000000:.1f}M"
    elif count >= 1000:
        return f"{count / 1000:.1f}K"
    else:
        return str(count)

print(format_likes(1200))
print(format_likes(1500000))
print(format_likes(500))