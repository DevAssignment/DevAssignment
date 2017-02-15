class conjugationExercise():

  def __init__(self, level, progress, answers, questions):
        self.level = level
        self.progress = progress
        self.answers = answers
        self.questions = questions

  def conjugationExercise(self, currentquestion):
    print ("Conjugate the following verb according to it's form: ")
    question = "exercises"#input(conjugationQuestions[currentquestion])

    if self.progress >= len(conjugationQuestions) - 1:
        print ("You've passed the exercise!")
        restart = input("Do you want to restart the exercise? Y/N?")
        self.progress = 0
        if restart == "Y" or restart == "y":
            currentquestion = 0
            #self.conjugationExercise(currentquestion)
            return 3
        elif restart == "N" or restart == "n":
            print("Thanks for playing!")
            return 4
        else:
            print("Please input Y or N next time")
            return 5
    else:
        if question == self.answers[currentquestion]:
            self.progress += 1
            print("Correct!")
            #self.conjugationExercise(currentquestion + 1)
            return 1
        else:
            print("Try again")
            #self.conjugationExercise(currentquestion)
            return 0


conjugationQuestions = ["Exercise (Present) \nHe ", "Draw (Present)\nShe ", "Walk (Past) \nIt ", "Eat(Past) \nThey "]
conjugationAnswers = ["exercises", "draws", "walked", "ate"]
#conjugationAnswers = ["exercises"]
#conjugationQuestions = ["Exericse"]
conjugationExercisetest = conjugationExercise(1, 0, conjugationAnswers, conjugationQuestions)
conjugationExercisetest.conjugationExercise(conjugationExercisetest.progress)