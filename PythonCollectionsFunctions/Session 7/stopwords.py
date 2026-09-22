text="the food is good and the service is fast"

stopwords=["the", "and", "in", "of", "a", "to", "is"]

words=text.lower().split()

freq = {}

for word in words:
    if word not in stopwords:
        freq[word] = freq.get(word, 0) + 1

print(freq)