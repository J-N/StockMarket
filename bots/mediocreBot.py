import sys
sys.path.insert(0, '../')
from ... import traderBot

robot = traderBot.traderBot()

#sequence of events:
#get a list of stock
#randomly pick a stock
#get current price, then wait until the price is 30 cents below that current price
#wait until price rises by $1.00
#sells stock
#party (robo-wolf of wall street)

stockArray = robot.getSymbols()
size = stockArray.count()
randomStock = random.randint(0, size - 1)

price = robot.getPrice(randomStock)
oldPrice = price
priceDifference = randrange(0, 2, 0.1)
target = price - priceDifference

while (price > target)
    price = robot.getPrice(randomStock)

money = robot.getFunds()

shares = money/price

robot.buy(randomStock, shares)

print "bought" + shares + "at a total price of" + shares*price

positivePriceDifference = randrange(0, 1, 0.1) + priceDifference

target = price + positivePriceDifference

while (price < target)
    price = robot.getPrice(randomStock)

robot.sell(randomStock, shares)

print "sold" + shares + "at a total price of" + shares*price

profit = price*shares - oldPrice*shares

print "made" + profit + "dollars"
