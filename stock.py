import random

class Stock:
  """A simple Stock class"""

  MIN_EARNINGS = -10000
  MAX_EARNINGS = 10000
  def __init__(self, symbol):
    self.symbol = symbol
    self.volume = random.randint(10000, 100000)
    self.earnings = random.randint(MIN_EARNINGS, MAX_EARNINGS)
