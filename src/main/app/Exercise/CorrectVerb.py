from src.main.app.Exercise.Exercise import Exercise
from src.main.app.PrettyPrinter import PrettyPrinter

console = PrettyPrinter()


class CorrectVerb(Exercise):
    def __init__(self, progress):
        questions = ["I eaten yesterday", "I will walked tomorrow", "I pray now", "I will asked him a question tomorrow", "I tell him yesterday"]
        answers = ["ate", "walk", "pray", "ask", "told" ]
        super(CorrectVerb, self).__init__(1, progress, answers, questions)

    def askQuestion(self, currentquestion, answer):
        console.output("Verander het werkwoord, indien fout, naar de juiste vervorming: " + self.questions[currentquestion])

        if answer == self.answers[currentquestion].lower():
            if currentquestion >= (len(self.questions) - 1):
                return "Congratulations"
            self.progress += 1
            return "Next Question"
        else:
            return "Try Again"





