class SongAlreadyExistsError(Exception):
    pass


def add_song_to_playlist(song_name, playlist):
    if song_name in playlist:
        raise SongAlreadyExistsError("Song already exists in playlist")

    playlist.append(song_name)
    print("Song added successfully")


playlist = ["Jeene Laga Hoon", "Do You Know", "Paisa Hai Toh"]

try:
    add_song_to_playlist("Do You Know", playlist)

except SongAlreadyExistsError as e:
    print(e)