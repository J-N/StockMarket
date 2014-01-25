#!/usr/bin/env python

"""
A simple echo server
"""

import socket

stocks = {}
accounts = {}
host = 'localhost'
port = 19290
backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)
print("listening for connections on port 19290")
while True:
  client, address = s.accept()
  data = client.recv(size)
  if data != 0:
    sendData = parseData(data)
    else:


    client.send(sendData)
  client.close()


def parseData(data):
  if data == "getid;":
    account = Account()
    accounts[account.id] = account
    return account.id

  split_data = data.split(",")
  account_id = int(split_data[0])
  action = split_data[1]
  if action == "buy":
    ticker = split_data[2]
    shares = split_data[3]
    account = accounts[account_id]
    stock = stocks[ticker]
    if shares <= stock.volume:
      if stock.bidask*shares <= account.availableFunds:
        account.availableFunds -= stock.bidask*shares
        account.portfolio[ticker] += shares
        stock.volume -= shares
        stocks[ticker] = stock
        return 1
    return 0

  elif action == "sell":
    ticker = split_data[2]
    shares = split_data[3]
    account = accounts[account_id]
    stock = stocks[ticker]
    if shares <= account.portfolio[ticker]:
      account.availableFunds += stock.bidask*shares
      account.portfolio[ticker] -= shares
      stock.volume += shares
      stocks[ticker] = stock
      return 1
    return 0

  elif action == "price":
    ticker = split_data[2]
    return stocks[ticker].price
  elif action == "volume":
    ticker = split_data[2]
    return stocls[ticker].volume
  elif action == "portfolio":
  elif action == "account"
  elif action == "all"
  else:
    return -1
