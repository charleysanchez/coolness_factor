import sqlite3

def retrieve_data(db):
    db_path = f'../data/{db}.db'

    try:
        conn = sqlite3.connect(db_path)

        cur = conn.cursor()

        cur.execute("SELECT * FROM photo_rating")

        data = cur.fetchall()


        cur.close()
        conn.close()

        return data 

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None
