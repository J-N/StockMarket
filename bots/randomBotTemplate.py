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
riskFactor = .05 #fraction of original price
riskFactorMultiplier = 3


robot = traderBot.traderBot()

stockArray = robot.getSymbols()

while (true)
	#checks if portfolio is empty
	portfolio = robot.getPortfolio()
    currentlyOwnedStock = -1
    empty = True
    for stock in portfolio:
    	stock = stock.split(':')
    	if int(stock[1]) != 0
    		empty = False
            currentlyOwnedStock = stock[0]

    if empty:
    	#buy algorithm

        #picks random stock
        ticker = random.randint(0, portfolio.count() -1)
        price = robot.getPrice(ticker)

        robot.buy()

        #determines how much money it's willing to wager at once
        money = robot.getFunds()
        maxMoney = money*riskFactor*riskFactorMultiplier
        shares = 
	if !empty
		#sell algorithm