class DatabaseConnection:
  def __init__(self, dbc):
    self.DirectConnection = dbc

  def open(self):
    self.DirectConnection.open()

  def close(self):
    self.DirectConnection.close()

