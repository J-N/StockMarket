class Account:
  """Account class used by server to maintain client connections. """
  class_counter = 0
  # stocks is a list of symbols
  def __init__(self, stocks):
    self.id = Account.class_counter
    Account.class_counter += 1
    self.availableFunds = 1000000.0
    self.portfolio = {}
    for ticker in stocks:
      self.portfolio[ticker] = 0
