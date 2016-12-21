from src.main.app.Exercise.CorrectVerb import CorrectVerb


class TestCorrectVerbWrong:
  def setup(self):
    self.CorrectVerb = CorrectVerb(0)

  def teardown(self):
    self.CorrectVerb = None

  def test_CorrectVerb(self):
    # Setup
    expected = "Try Again"

    # Testing
    answerList = "abc"

    assert expected == self.CorrectVerb.askQuestion(0, answerList)

    # Teardown