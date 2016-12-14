from app.Exercise.Enumerable import Enumerable


# Example of how to implement an Array or Enumerable/Iterable in Python
class Array(Enumerable):
  def __init__(self):
    self.index = 0
    self.data = []

  def __iter__(self):
    return self

  def __next__(self):
    self.index += 1
    return self.data[self.index]

  def __repr__(self):
    return [d for d in self.data]

  def get_at_index(self, index):
    return self.data[index]

  def reset(self):
    self.index = 0

  def move_next(self):
    self.index += 1

  def get_current(self):
    return self.data[self.index]

  def add(self, x):
    self.data.append(x)

  def set(self, i, x):
    self.data.pop(i)
    self.data.insert(i,x)
