from playlist import add_song, remove_song, display_playlist

playlist = []

add_song("Dope Shope", playlist)
add_song("Kaho na Kaho", playlist)
add_song("Chura ke Dil mera", playlist)

remove_song("Chura ke Dil mera", playlist)

display_playlist(playlist)