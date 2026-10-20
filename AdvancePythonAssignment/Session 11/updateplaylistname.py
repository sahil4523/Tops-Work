import pymysql

con = pymysql.connect(
    host="localhost",
    user="root",
    password="sahil1532",
    database="music_stream"
)

cur = con.cursor()

cur.execute("""
UPDATE playlists
SET name = 'Chill Hits'
WHERE name = 'Chill Vibes'
""")

con.commit()

print("Playlist name updated successfully")

con.close()