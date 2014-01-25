class Account:
  """Account class used by server to maintain client connections. """
  class_counter = 0
  def __init__(self):
    self.id = Account.class_counter
    Account.class_counter += 1
    self.availableFunds = 1000000.0
    self.portfolio = {}
