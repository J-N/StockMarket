import sys
import random

sys.path.append('../')

from traderbot import TraderBot

robot = TraderBot(555555)

stockArray = robot.getSymbols()

startingPrice = -1

buy(robot.accountID,'StockA',1)