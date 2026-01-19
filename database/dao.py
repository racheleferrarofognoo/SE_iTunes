from database.DB_connect import DBConnect
from model.album import Album


class DAO:
    @staticmethod
    def get_album_maggiori_di_durata(min_duration):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select a.id, a.title, a.artist_id, sum(t.milliseconds)/60000 as durata
                    from album a, track t
                    where a.id = t.album_id 
                    group by a.id, a.title, a.artist_id 
                    having durata > %s """

        cursor.execute(query, (min_duration,))

        for row in cursor:
            result.append(Album(**row))

        cursor.close()
        conn.close()
        return result #lista di oggetti album

    @staticmethod
    def get_connessioni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT t1.album_id AS a1, t2.album_id AS a2
                    FROM playlist_track pt1, playlist_track pt2, track t1, track t2
                    WHERE pt1.playlist_id = pt2.playlist_id and pt1.track_id = t1.id and pt2.track_id = t2.id and t1.album_id < t2.album_id
                    GROUP BY t1.album_id, t2.album_id """

        cursor.execute(query)

        for row in cursor:
            result.append((row['a1'], row['a2']))

        cursor.close()
        conn.close()
        return result #lista di tuple [(album id 1, album id 2), (..)...]