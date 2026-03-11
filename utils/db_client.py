# Author:Yi Sun(Tim) 2023-8-30

'''Database Handle'''

import pyodbc

class DBClient:
    def __init__(self, connection_string):
        self.conn_str = connection_string
        self.connection = None

    def __enter__(self):
        self.connection = pyodbc.connect(self.conn_str)
        return self.connection.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()

    def fetch_one(self, query):
        with self as cursor:
            cursor.execute(query)
            return cursor.fetchone()