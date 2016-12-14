import psycopg2


class DatabaseConnection:
    def __init__(self):
        self.conn = None

    # Opens db connection
    def open(self):
        self.conn = psycopg2.connect(database="Dev06B", user="postgres", password="root", host="127.0.0.1", port="5433")
        print("db connection succeful")

    # Closes db connection
    def close(self):
        self.conn.close()
        print("db succesfully closed")

    # Returns a list/array/enumerable of a result of the query
    def selectQuery(self, query):
        cur = self.conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        return rows


