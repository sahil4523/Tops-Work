import pymysql

def delete_playlist(playlist_id):
    con = None

    try:
        con = pymysql.connect(
            host="localhost",
            user="root",
            password="sahil1532",
            database="music_stream"
        )

        cur = con.cursor()

        cur.execute(
            "DELETE FROM playlists WHERE id = %s",
            (playlist_id,)
        )

        con.commit()

        if cur.rowcount > 0:
            print("Playlist deleted successfully")
        else:
            print("Playlist ID does not exist")

    except pymysql.MySQLError as e:
        print("Error:", e)

    finally:
        if con:
            con.close()

delete_playlist(1)