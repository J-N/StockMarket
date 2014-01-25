#sequence of events
#for every loop: 
#picks a random stock
#buys it immediately
#sells it at a random price

import sys
import random
sys.path.append('../')
from traderbot import TraderBot

#riskFactor represents how risky the bot is in general
#it affects both how much money it's willing to wager, and how long it'll wait
#before giving up
riskFactor = 0.63 <--- will be replaced by generator #fraction of original price
riskFactorMultiplier = 3


robot = TraderBot()

stockArray = robot.getSymbols()

startingPrice = -1

while (True):
  #checks if portfolio is empty
  portfolio = robot.getPortfolio()
  currentlyOwnedStock = -1
  stockQuantity = -1
  empty = True
  for x in range(0,len(portfolio))
    if portfolio[str(x)] != 0
        empty=False
        currentlyOwnedStock = str(x)
        stockQuantity=portfolio[str(x)]

  if empty:
    print "portfolio is empty, picking a stock to buy"
    #buy algorithm

    #picks random stock
    ticker = random.randint(0, len(portfolio) -1)
    print "decided to buy stock with ticker :", ticker
    startingPrice = robot.getPrice(ticker)
    print "price of stock: $", startingPrice, "per share"

    #determines how much money it's willing to wager at once
    money = robot.getFunds()
    maxMoney = money*riskFactor*riskFactorMultiplier
    if maxMoney > money:
        maxMoney = money
    print "bot is willing to risk $" , maxMoney
    shares = (int)(maxMoney/startingPrice)
    print "purchasing", shares, "shares at $" , startingPrice, "per share"

    #ourchases stock
    result = robot.bid(robot.accountID, shares, price, ticker)
    if result == 'Accepted':
        print "trade accepted"
    elif result == 'Unsuccesful':
        print "trade declined"
    elif result == 'Pending':
        print "trade pending"
    else:
        print "not a recognizable order state"

  if not empty:
    #sell algorithm
    currentPrice = robot.getPrice(currentlyOwnedStock)

    priceDifference = (currentPrice - startingPrice)/startingPrice
    print "percentage difference between purchasing price and current price: ", priceDifference

    #price has gone down too much, give up and sell
    result = ""

    if priceDifference < 0.05:
        print "price too low, giving up and selling at a loss"
        result = robot.ask(robot.accountID, stockQuantity, currentPrice, currentlyOwnedStock)
        print "selling", stockQuantity, "shares at $" , currentPrice, "per share"
    elif priceDifference > 0.05:
        "price increased sufficiently, selling for a profit"
        result = robot.ask(robot.accountID, stockQuantity, currentPrice, currentlyOwnedStock)
        print "selling", stockQuantity, "shares at $" , currentPrice, "per share"

    if result == 'Accepted':
        print "trade accepted"
    elif result == 'Unsuccesful':
        print "trade declined"
    elif result == 'Pending':
        print "trade pending"
    else:
        print "not a recognizable order state"