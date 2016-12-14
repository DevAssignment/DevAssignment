import abc
from src.main.app.PrettyPrinter import PrettyPrinter

console = PrettyPrinter()

class Exercise:
  __metaclass__ = abc.ABCMeta

  def __init__(self, level, progress, answers, questions):
    self.level = level
    self.progress = progress
    self.answers = answers
    self.questions = questions

  @abc.abstractmethod
  def askQuestion(self):
      pass

  def passProgress(self, level,  progress):
        sql = "INSERT INTO USER" + level + "," + progress