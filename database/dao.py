from database.DB_connect import DBConnect
from model.album import Album


class DAO:
    @staticmethod
    def get_album(durata):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select a.id, a.title, a.artist_id, sum(t.milliseconds/60000) as durata
                    from album a, track t
                    where a.id = t.album_id 
                    group by a.id, a.title, a.artist_id
                    having  durata > %s
                                         """

        cursor.execute(query, (durata,))

        for row in cursor:
            result.append(Album(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_connessioni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT DISTINCT t1.album_id as album1, t2.album_id as album2
                    FROM track t1, track t2, playlist_track pt1, playlist_track pt2
                    WHERE pt1.playlist_id = pt2.playlist_id 
                    AND	pt1.track_id != pt2.track_id 
                    AND t1.id = pt1.track_id 
                    AND t2.id = pt2.track_id
                    AND t1.album_id<t2.album_id """

        cursor.execute(query)

        for row in cursor:
            result.append((row["album1"],row["album2"]))

        cursor.close()
        conn.close()
        return result