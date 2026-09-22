def add_song_to_playlist(playlists, user, playlist_name, song_title, artist):
    if user not in playlists:
        playlists[user] = {}

    if playlist_name not in playlists[user]:
        playlists[user][playlist_name] = []

    playlists[user][playlist_name].append({
        "title": song_title,
        "artist": artist
    })


playlists = {}

add_song_to_playlist(
    playlists, "sahil", "Favourite",
    "Dope Shope", "Honey Singh"
)

print(playlists)