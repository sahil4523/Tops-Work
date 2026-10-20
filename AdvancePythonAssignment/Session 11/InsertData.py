import pymysql

con = pymysql.connect(
    host="localhost",
    user="root",
    password="your_password"
)

cur = con.cursor()

cur.execute("CREATE DATABASE IF NOT EXISTS music_stream")
cur.execute("USE music_stream")

cur.execute("""
CREATE TABLE IF NOT EXISTS playlists (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    song_count INT
)
""")

cur.execute("""
INSERT INTO playlists (name, song_count)
VALUES
('Chill Vibes', 15),
('Party Songs', 20),
('Love Songs', 8)
""")

con.commit()

print("Data inserted successfully")

con.close()