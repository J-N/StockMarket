#sequence of events
#for every loop: 
#picks a random stock
#buys it immediately
#sells it at a random price

import traderBot

robot = traderBot.traderBot()

stockArray = robot.getSymbols()

while (true)
    money = robot.getFunds()
    
    #picks a random stock
    stockArray = robot.getSymbols()
    size = stockArray.count()
    randomStock = random.randint(0, size - 1)
    
    maxShares = 

