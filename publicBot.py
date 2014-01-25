import random
#I'll need to change this to incorporate 
from traderbot import traderbot

robot = TraderBot()

stockArray = robot.getSymbols()

#initial loop
for ticker in stockArray
	portfolio = robot.getPortfolio()

	if (portfolio[ticker] != 0)

		#selling distribution:
		#25 percent at market price
		#10 percent at 10 percent above market price
		#10 percent at 10 percent below market price
		#5 percent at 5 percent below market price

		marketFraction = 0.25
		aboveMarket = 0.10
		tenBelowMarket = 0.10
		fiveBelowMarket = 0.05
			
		price = robot.getPrice(ticker)

		result = robot.ask(robot.accountID, (int)portfolio[ticker] *marketFraction , price, ticker)
		if result == 'Accepted':
        	print "trade accepted"
    	elif result == 'Unsuccesful':
        	print "trade declined"
    	elif result == 'Pending':
        	print "trade pending"
    	else:
        	print "not a recognizable order state"
		result = robot.ask(robot.accountID, (int)portfolio[ticker]*aboveMarket, price*1.10, ticker)
		if result == 'Accepted':
        	print "trade accepted"
    	elif result == 'Unsuccesful':
        	print "trade declined"
    	elif result == 'Pending':
        	print "trade pending"
    	else:
        	print "not a recognizable order state"
		result = robot.ask(robot.accountID, (int)portfolio[ticker]*tenBelowMarket, price*0.9, ticker)
		if result == 'Accepted':
        	print "trade accepted"
    	elif result == 'Unsuccesful':
        	print "trade declined"
    	elif result == 'Pending':
        	print "trade pending"
    	else:
        	print "not a recognizable order state"
		result = robot.ask(robot.accountID, (int)portfolio[ticker]*fiveBelowMarket, price*0.95, ticker)
		if result == 'Accepted':
	        print "trade accepted"
	    elif result == 'Unsuccesful':
	        print "trade declined"
	    elif result == 'Pending':
	        print "trade pending"
	    else:
	        print "not a recognizable order state"


while True:

	for ticker in stockArray:
		portfolio = robot.getPortfolio()
		if (portfolio[ticker] != 0):
			trueValue = robot.getTrueValue(ticker)
			price = robot.getPrice(ticker)
			increment = abs(trueValue - price)/3

			#bid for 10 percent of the total stock @ market value
			#bid for 4 percent of total stock @ below market value
			#bid for 3 percent of total stock @ above market value
			#bid for 2 percent of total stock @ significantly above market value
			#bid for 1 percent of total stock @ true value
			if trueValue/price >1.05:
				stockToBuy = 0.2 * robot.getVolume(ticker)
				robot.bid(robot.accountID, (int)stockToBuy/2, price, ticker)
				stockToBuy/= 2
				robot.bid(robot.accountID, (int)stockToBuy*0.4, price - increment, ticker)
				robot.bid(robot.accountID, (int)stockToBuy*0.3, price + increment, ticker)
				robot.bid(robot.accountID, (int)stockToBuy*0.2, price + 2 * increment, ticker)
				robot.bid(robot.accountID, (int)stockToBuy*0.1, price + 3 * increment, ticker)

			#ask for 10 percent of the total stock @ market value
			#ask for 4 percent of total stock @ above market value
			#ask for 3 percent of total stock @ below market value
			#ask for 2 percent of total stock @ significantly below market value
			#ask for 1 percent of total stock @ true value
			if trueValue/price < 0.95:
				stockToSell = 0.3 * portfolio[ticker]
				robot.ask(robot.accountID, (int)stockToSell/2, price, ticker)
				stockToBuy/= 2
				robot.ask(robot.accountID, (int)stockToSell*0.4, price + increment, ticker)
				robot.ask(robot.accountID, (int)stockToSell*0.3, price - increment, ticker)
				robot.ask(robot.accountID, (int)stockToSell*0.2, price - 2 * increment, ticker)
				robot.ask(robot.accountID, (int)stockToSell*0.1, price - 3 * increment, ticker)

	
