f = open("my_fav_songs.txt", "r")

count = 1

for song in f:
    print(count, song.strip())
    count=count + 1

f.close()