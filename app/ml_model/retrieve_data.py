import sqlite3

def retrieve_data(db):
    # Construct the path to the SQLite database file
    db_path = f'../data/{db}.db'

    try:
        # Connect to the database
        conn = sqlite3.connect(db_path)

        # Create a cursor to execute SQL commands
        cur = conn.cursor()

        # Example SQL query to retrieve data (replace with your specific query)
        cur.execute("SELECT * FROM photo_rating")

        # Fetch all rows from the result set
        data = cur.fetchall()


        # Close the cursor and connection
        cur.close()
        conn.close()

        return data  # Return the retrieved data (modify as needed)

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None  # Return None or handle error appropriately
