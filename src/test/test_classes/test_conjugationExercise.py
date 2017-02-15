from src.main.app.Exercise.conjugationExercise import conjugationExercise

class testconjugationExercise:

    def setup(self):
        question = ["Exercises?"]
        answer = ["Exercises"]
        self.exercise = conjugationExercise(1, 0, answer, question)

    def test_question(self):
        expected = 1

        assert expected == self.exercise.conjugationExercise(0)

    def test_wronganswer(self):
        expected = 0

        assert expected == self.exercise.conjugationExercise(0)

    def test_yesAnswer(self):
        expected = 3

        assert expected == self.exercise.conjugationExercise(0)

    def test_noAnswer(self):
        expected = 4

        assert expected == self.exercise.conjugationExercise(0)

    def test_wrongAnswer(self):
        expected = 5

        assert expected == self.exercise.conjugationExercise(0)


        from src.main.app.Exercise.conjugationExercise import conjugationExercise

class testconjugationExercise:

 def test(self):
  cEx = conjugationExercise(1,0)
  self.assertequals(cEx.checkAnswer("exercises"), 'correct', True)
  self.assertequals(cEx.checkAnswer("ExErCiSes"), 'correct', True)
  self.assertequals(cEx.checkAnswer("Ex"), 'incorrect', True)
  cEx = conjugationExercise(1,1)
  self.assertequals(cEx.checkAnswer("draws"), 'correct', True)
  self.assertequals(cEx.checkAnswer("DrAwS"), 'correct', True)
  self.assertequals(cEx.checkAnswer("dr"), 'incorrect', True)
  cEx = conjugationExercise(1,2)
  self.assertequals(cEx.checkAnswer("walked"), 'correct', True)
  self.assertequals(cEx.checkAnswer("WaLkEd"), 'correct', True)
  self.assertequals(cEx.checkAnswer("wa"), 'incorrect', True)
  cEx = conjugationExercise(1,3)
  self.assertequals(cEx.checkAnswer("ate"), 'correct', True)
  self.assertequals(cEx.checkAnswer("aTe"), 'correct', True)
  self.assertequals(cEx.checkAnswer("at"), 'incorrect', True)