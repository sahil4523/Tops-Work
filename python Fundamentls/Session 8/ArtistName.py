def extract_artist(song_title):
    position = song_title.index("-")
    artist = song_title[position + 1:]
    return artist.strip()

song = input("Enter song title: ")
print("Artist:", extract_artist(song))