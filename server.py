#!/usr/bin/env python

"""
Stock Market server that manages client transactions.
"""
# return values: 1(accept transaction), 0(decline transaction),
# -1 (invalid syntax/error)
import cPickle as pickle
import socket
from account import Account
from stock import Stock

stocks = {}
accounts = {}

def initMarket(account_id):
  # initialize stocks
  account = accounts[account_id]
  for letter in "ABCDEFGHIJ":
    ticker = "Stock" + letter
    stocks[ticker] = Stock(ticker)
    account.portfolio[ticker] = 10000

# Account Actions
def ask(account_id, ticker, price, quantity):
  """Add ask order to stock sell queue."""
  global stocks
  stock = stocks[ticker]
  account = accounts[account_id]
  quantityAvailable = account.portfolio[ticker]
  if quantity > quantityAvailable:
    return 0
  stock.sellAt(quantity, price, account_id)
  stocks[ticker]=stock
  return 1

def bid(account_id, ticker, price, quantity):
  """Add bid order to stock bid queue."""
  global stocks
  stock = stocks[ticker]
  account = accounts[account_id]
  if price * quantity > account.availableFunds:
    return 0
  stock.buyAt(quantity, price, account_id)
  stocks[ticker]=stock
  return 1

def buy(account_id, ticker, quantity):
  """Return 0 if insufficent funds or insufficient quantity; 1 for success."""
  global stocks
  account = accounts[account_id]
  stock = stocks[ticker]

  # Check sufficient quantity
  if stock.sellQueueNum() < quantity:
    print "Failed, insufficient quantity available"
    return 0

  # Check sufficient funds
  if stock.totalBuyCost(quantity) > account.availableFunds:
    print "Failed, insufficient funds"
    return 0

  stock.buy(quantity)
  print "Bought", buyVolume, "shares of ticker:", ticker, "at price:", stock.price
  return 1

def sell(account_id, ticker, quantity):
  """Return 0 if insufficient quantity; 1 for success."""
  global stocks
  account = accounts[account_id]
  stock = stocks[ticker]

  # Check sufficient quantity to sell
  if account.portfolio[ticker] < quantity:
    print "Failed, insufficient quantity in portfolio"
    return 0

  # Check sufficient quantity demanded
  if stock.buyQueueNum() < quantity:
    print "Failed, insufficient quantity demanded from market"
    return 0

  stock.sell(quantity)
  stocks[ticker] = stock
  print "Sold", sellVolume, "shares of ticker:", ticker, "at price:", stock.price
  return 1

def parseData(data):
  # parse client requests according to server_api
  global stocks
  if data == "create":
    account = Account(stocks.keys())
    accounts[account.id] = account
    if account.id == 1:
      initMarket(1)

    print "Account created with account id:", account.id
    return account.id

  split_data = data.split(",")
  account_id = int(split_data[0])
  action = split_data[1]
  account = accounts[account_id]
  print "Loaded account:", account_id
  print "Funds Available:", account.availableFunds

  if action == "buy":
    ticker = split_data[2]
    buyVolume = int(split_data[3])

    return buy(account_id, ticker, buyVolume)

  elif action == "sell":
    ticker = split_data[2]
    sellVolume = int(split_data[3])

    return sell(account_id, ticker, sellVolume)

  elif action == "bid":
    ticker = split_data[2]
    price  = float(split_data[3])
    quantity = int(split_data[4])

    return bid(account_id, ticker, price, quantity)

  elif action == "ask":
    ticker = split_data[2]
    price  = float(split_data[3])
    quantity = int(split_data[4])

    return ask(account_id, ticker, price, quantity)

  elif action == "price":
    ticker = split_data[2]
    print "Price of ticker:", ticker, "is", stocks[ticker].price
    return stocks[ticker].price

  elif action == "volume":
    ticker = split_data[2]
    print "Volume of ticker:", ticker, "is", stocks[ticker].volume
    return stocks[ticker].volume

  elif action == "portfolio":
    print "portfolio requested"
    return account.portfolio

  elif action == "funds":
    print "Available funds requested"
    return account.availableFunds

  elif action == "symbols":
    print "Symbols requested"
    return stocks.keys()

  elif action == "trueValue":
    ticker = split_data[2]
    stock = stocks[ticker]
    print "trueValue requested"
    return stock.trueValue

  else:
    return -1


def main():
  global stocks
  host = 'localhost'
  port = 19290
  backlog = 5
  size = 1024
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind((host,port))
  s.listen(backlog)
  print("listening for connections on port 19290")
  counter = 0
  while True:
    # Update true value every 20 cycles
    if counter % 20 == 0:
      for stock in stocks:
        stocks[stock].updateTrueValue()

    client, address = s.accept()
    data = client.recv(size)
    print data
    if data != 0:
      sendData = parseData(data)
    else:
      sendData = -1
      print "Error: no data received"
    print "\n"
    # print sendData

    sendData = pickle.dumps(sendData)
    client.send(sendData)
    client.close()
    counter += 1


if __name__ == "__main__":
  main()
