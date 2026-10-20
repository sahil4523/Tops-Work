song_duration = {
    "Haan Tu Hain": 5.2,
    "Tum Hi Ho": 4.2,
    "Dope Shop": 3.3
}

def get_song_duration(song):
    try:
        print("Song duration:", song_duration[song], "minutes")
    except KeyError:
        print("Song not found on Spotify!")

get_song_duration("Haan Tu Hain")
get_song_duration("Hello")