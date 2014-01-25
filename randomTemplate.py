#sequence of events
#for every loop: 
#picks a random stock
#buys it immediately
#sells it at a random price

import sys
import random
sys.path.insert(0, '../')
from traderbot import traderBot

#riskFactor represents how risky the bot is in general
#it affects both how much money it's willing to wager, and how long it'll wait
#before giving up
riskFactor = ### 
riskFactorMultiplier = 3


robot = traderBot.traderBot()

stockArray = robot.getSymbols()

startingPrice = -1

while (True):
	#checks if portfolio is empty
	portfolio = robot.getPortfolio()
    currentlyOwnedStock = -1
    stockQuantity = -1
    empty = True
    for stock in portfolio:
    	stock = stock.split(':')
    	if int(stock[1]) != 0
    		empty = False
            currentlyOwnedStock = stock[0]
            stockQuantity = stock[1]

    if empty:
        print "portfolio is empty, picking a stock to buy"
    	#buy algorithm

        #picks random stock
        ticker = random.randint(0, portfolio.count() -1)
        print "decided to buy stock with ticker :", ticker
        startingPrice = robot.getPrice(ticker)
        print "price of stock: $", startingPrice, "per share"

        #determines how much money it's willing to wager at once
        money = robot.getFunds()
        maxMoney = money*riskFactor*riskFactorMultiplier
        print "bot is willing to risk $" , maxMoney
        shares = (int)(maxMoney/startingPrice)
        print "purchasing", shares, "shares at $" , startingPrice, "per share"

        #ourchases stock
        result = robot.bid(robot.accountID, shares, price, ticker)
        if result == 'Accepted':
            print "trade accepted"
        elif result == 'Unsuccesful':
            print "trade declined"
        elif result == 'Pending'
            print "trade pending"
        else
            print "not a recognizable order state"

	if !empty:
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
        elif priceDifference > 0.05
            "price increased sufficiently, selling for a profit"
            result = robot.ask(robot.accountID, stockQuantity, currentPrice, currentlyOwnedStock)
            print "selling", stockQuantity, "shares at $" , currentPrice, "per share"

        if result == 'Accepted':
            print "trade accepted"
        elif result == 'Unsuccesful':
            print "trade declined"
        elif result == 'Pending'
            print "trade pending"
        else
            print "not a recognizable order state"


