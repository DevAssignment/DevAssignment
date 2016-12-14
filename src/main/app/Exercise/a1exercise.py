from src.main.app.Exercise.Exercise import Exercise
from src.main.app.PrettyPrinter import PrettyPrinter

console = PrettyPrinter()


class A1Exercise(Exercise):
    def __init__(self, progress):
        questions = ["Book", "Telephone", "Hat"]
        answers = ["Boek", "Telefoon", "Hoed"]
        super(A1Exercise, self).__init__(1, progress, answers, questions)

    def askQuestion(self):
        console.output("Translate " + self.questions[self.progress] + " to dutch: ")
        answer = console.input()

        if answer == self.answers[self.progress].lower():
            if self.progress >= (len(self.questions) - 1):
                console.output("You passed the exercise!")
                return
            self.progress += 1
            self.askQuestion()
        else:
            console.output("Try again!")
            self.askQuestion()


# Dummy Code
def get_user_progress():
    return 0

a1 = A1Exercise(get_user_progress())
a1.askQuestion()
