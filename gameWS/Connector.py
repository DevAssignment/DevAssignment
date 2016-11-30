import mysql.connector

class Connector():
    def __init__(self):
        # TODO
        self.conn = mysql.connector.connect(user='root',password='Test123', host='localhost',database='pgamedb',port=3306)


class Query():
    def __init__(self, queryLevel):
        # TODO
        pass
