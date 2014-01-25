#sequence of events
#for every loop: 
#picks a random stock
#buys it immediately
#sells it at a random price

import sys
sys.path.insert(0, '../')
from traderbot import traderBot

riskFactor = .05 #fraction of original price

robot = traderBot.traderBot()

stockArray = robot.getSymbols()

while (true)
	#checks if portfolio is empty
	portfolio = robot.getPortfolio()
    empty = True
    for stock in portfolio:
    	stock = stock.split(':')
    	if int(stock[1]) != 0
    		empty = False

    if empty:
    	#buy algorithm
	if !empty
		#sell algorithm