f = open("playlist.txt", "r")

f.readline()
f.readline()

song = f.readline()

print("Third song:", song.strip())

f.close()