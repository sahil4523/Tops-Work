def char_count_dict(text):
    freq = {}

    for char in text:
        freq[char] = freq.get(char, 0) + 1

    return freq


text=input("Enter text: ")

result=char_count_dict(text)

for char in sorted(result):
    print(char, result[char])