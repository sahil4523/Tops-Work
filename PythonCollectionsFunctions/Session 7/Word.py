import string

text="""I like Zomato because the food delivery is fast.
Zomato has many restaurants and good food."""

text=text.lower()
text=text.translate(str.maketrans("", "", string.punctuation))

words=text.split()

freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)