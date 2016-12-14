class Exercise():
  def __init__(self, level, progress, answers, questions):
    self.level = level
    self.progress = progress
    self.answers = answers
    self.questions = questions

  def askQuestion(self, currentquestion):
    answer = input("Translate " + questions[currentquestion] + " to dutch: ")
    if self.progress >= len(questions) - 1:
        print("You passed the exercise!")
    else:
        if answer == self.answers[currentquestion]:
            self.progress += 1
            self.askQuestion(currentquestion + 1)
        else:
            print("Try again!")
            self.askQuestion(currentquestion)

  def passProgress(self, level,  progress):
        sql = "INSERT INTO USER" + level + "," + progress


questions = ["Book", "Telephone", "Hat"]
answers = ["Boek", "Telefoon", "Hoed"]
a = Exercise(1, 0, answers, questions)
a.askQuestion(a.progress)