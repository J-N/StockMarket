import random
#I'll need to change this to incorporate 
from traderbot import traderbot

robot = TraderBot()

stockArray = robot.getSymbols()

portfolio = robot.getPortfolio()

#initial loop
for ticker in stockArray

	if (portfolio[ticker] != 0)

		#selling distribution:
		#50 percent at market price
		#20 percent at 10 percent above market price
		#20 percent at 10 percent below market price
		#10 percent at 5 percent below market price
		price = robot.getPrice(ticker)

		result = robot.ask(robot.accountID, (int)portfolio[ticker] *0.5 , price, ticker)
		if result == 'Accepted':
        	print "trade accepted"
    	elif result == 'Unsuccesful':
        	print "trade declined"
    	elif result == 'Pending':
        	print "trade pending"
    	else:
        	print "not a recognizable order state"
		result = robot.ask(robot.accountID, (int)portfolio[ticker]*0,2, price*1.10, ticker)
		if result == 'Accepted':
        	print "trade accepted"
    	elif result == 'Unsuccesful':
        	print "trade declined"
    	elif result == 'Pending':
        	print "trade pending"
    	else:
        	print "not a recognizable order state"
		result = robot.ask(robot.accountID, (int)portfolio[ticker]*0.2, price*0.9, ticker)
		if result == 'Accepted':
        	print "trade accepted"
    	elif result == 'Unsuccesful':
        	print "trade declined"
    	elif result == 'Pending':
        	print "trade pending"
    	else:
        	print "not a recognizable order state"
		result = robot.ask(robot.accountID, (int)portfolio[ticker]*0.1, price*0.95, ticker)
		if result == 'Accepted':
	        print "trade accepted"
	    elif result == 'Unsuccesful':
	        print "trade declined"
	    elif result == 'Pending':
	        print "trade pending"
	    else:
	        print "not a recognizable order state"
