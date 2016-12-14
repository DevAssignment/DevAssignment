class Counter:
  def __init__(self, init):
    self.init = init
    self.state = self.init

  def increment(self):
    self.state += 1

  def reset(self):
    self.state = self.init
