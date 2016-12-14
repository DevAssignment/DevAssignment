class DatabaseConnector:
    def __init__(self):
        self.connection = None # get a connection here

    def connect(self):
        # TODO: Create DB connection
        self.connection = NotImplementedError
        return self.connection

    def get_first_row(self, query):
        return self.connection.select(query).get(0)

    def get_rows(self, query):
        return self.connection.select(query)

# This is currently all dummy code
