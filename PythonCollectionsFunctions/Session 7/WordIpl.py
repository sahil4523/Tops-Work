def word_freq_dict(text):
    words=text.lower().split()
    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    return freq


text="Virat scored 100, Rohit scored 80, and Gill scored 50"

print(word_freq_dict(text))