import re

def extract_hashtags(text):
    return re.findall(r"#\w+", text)

caption = "Enjoying #music and #travel with #friends"
print(extract_hashtags(caption))