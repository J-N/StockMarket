import random

class Stock:
  """A simple Stock class"""

  def __init__(self, symbol):
    self.symbol = symbol
    self.volume = random.randint(100, 1000)
    self.bidask = random.randint(5, 500)
