import pymysql

con = pymysql.connect(
    host="localhost",
    user="root",
    password="sahil1532",
    database="music_stream"
)

cur = con.cursor()

cur.execute("SELECT name, song_count FROM playlists WHERE song_count > 10")

data = cur.fetchall()

for row in data:
    print(row[0], row[1])

con.close()