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

def initMarket():
  # initialize stocks
  for letter in "ABCDEFGHIJ":
    ticker = "Stock" + letter
    stocks[ticker] = Stock(ticker)

# Account Actions
def ask(account_id, ticker, price, quantity):
  """Add ask order to stock sell queue."""
  stock = stocks[ticker]
  return stock.sellAt(quantity, price, account_id)

def bid(account_id, ticker, price, quantity):
  """Add bid order to stock bid queue."""
  stock = stocks[ticker]
  return stock.buyAt(quantity, price, account_id)

def parseData(data):
  # parse client requests according to server_api
  if data == "create":
    account = Account(stocks.keys())
    accounts[account.id] = account
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
    volume = int(split_data[3])
    stock = stocks[ticker]

    if buyVolume > stock.volume:
      print "Failed, not enough shares available for purchase"
      return 0
    transactionCost = stock.bidask * buyVolume

    if transactionCost > account.availableFunds:
      print "Failed, insufficient funds"
      return 0

    account.availableFunds -= transactionCost
    account.portfolio[ticker] += buyVolume
    stock.volume -= buyVolume
    #update stocks
    stocks[ticker] = stock
    print "Bought", buyVolume, "shares of ticker:", ticker, "at price:", stock.bidask
    return 1

  elif action == "sell":
    ticker = split_data[2]
    volume = int(split_data[3])
    stock = stocks[ticker]
    if volume <= account.portfolio[ticker]:
      account.availableFunds += stock.bidask*volume
      account.portfolio[ticker] -= volume
      stock.volume += volume
      stocks[ticker] = stock
      return 1
    return 0

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
    print "Price of ticker:", ticker, "is", stocks[ticker].bidask
    return stocks[ticker].bidask

  elif action == "volume":
    ticker = split_data[2]
    return stocks[ticker].volume

  elif action == "portfolio":
    return account.portfolio

  elif action == "funds":
    return account.availableFunds

  elif action == "symbols":
    return stocks.keys()
  else:
    return -1


def main():
  host = 'localhost'
  port = 19290
  backlog = 5
  size = 1024
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind((host,port))
  s.listen(backlog)
  print("listening for connections on port 19290")
  initMarket()
  while True:
    client, address = s.accept()
    data = client.recv(size)
    print data
    if data != 0:
      sendData = parseData(data)
    else:
      sendData = -1
    print sendData

    sendData = pickle.dumps(sendData)
    client.send(sendData)
    client.close()

if __name__ == "__main__":
  main()
