from src.main.app.Exercise.CorrectVerb import CorrectVerb


class TestCorrectVerb:
  def setup(self):
    self.CorrectVerb = CorrectVerb(0)

  def teardown(self):
    self.CorrectVerb = None

  def test_CorrectVerb(self):
    # Setup
    expected = "Congratulations"

    # Testing
    answerList = "told"

    assert expected == self.CorrectVerb.askQuestion(4, answerList)

    # Teardown
