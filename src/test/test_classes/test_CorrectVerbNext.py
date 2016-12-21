from src.main.app.Exercise.CorrectVerb import CorrectVerb


class TestCorrectVerbNext:
  def setup(self):
    self.CorrectVerb = CorrectVerb(0)

  def teardown(self):
    self.CorrectVerb = None

  def test_CorrectVerb(self):
    # Setup
    expected = "Next Question"

    # Testing
    answerList = "ate"

    assert expected == self.CorrectVerb.askQuestion(0, answerList)

    # Teardown
