import random

songs = ["Tu Jaane naa", "Ishq Wishq", "Chaleya", "Tum Hi Ho", "Apna Bana Le"]

random.shuffle(songs)

print("Shuffled playlist:")
for song in songs:
    print(song)