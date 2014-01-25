import random

class Stock:
  """A simple Stock class"""

  MIN_PRICE = 5
  MAX_PRICE = 500
  def __init__(self, symbol):
    self.symbol = symbol
    self.volume = random.randint(10000, 100000)
    self.bidask = random.randint(Stock.MIN_PRICE, Stock.MAX_PRICE)
