import sys
sys.path.insert(0, '../')
import random
from traderbot import TraderBot

robot = TraderBot()

stockArray = robot.getSymbols()

print "Stock Array", stockArray

size = len(stockArray)

print "Array Size", size

randomStock = random.randint(0, size - 1)

print "random stock ticker:", randomStock

price = robot.getPrice(randomStock)

print "stock price:", price

money = robot.getFunds()

maxShares = 100

confirmation = robot.buy(randomStock, maxShares)

if (confirmation == 1):
    print "buy confirmed"
else:
    print "buy failed"
    
portfolio = robot.getPortfolio()

print "Portfolio before selling:"

print portfolio

confirmation = robot.sell(randomStock, maxShares)

if (confirmation == 1):
    print "sell confirmed"
else:
    print "sell failed"

portfolio = robot.getPortfolio()

print "Portfolio before selling:"

for array in portfolio:
    print array