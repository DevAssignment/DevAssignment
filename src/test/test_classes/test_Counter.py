from Counter import Counter


class TestCounter:
  def setup(self):
    self.counter = Counter(0)

  def teardown(self):
    self.counter = None

  def test_increment(self):
    # Setup
    expected = self.counter.state + 1

    # Testing
    self.counter.increment()
    assert expected == self.counter.state

    # Teardown

  def test_reset(self):
    # Setup
    expected = self.counter.init

    # Testing
    self.counter.increment()
    self.counter.reset()
    assert expected == self.counter.state

    # Teardown

