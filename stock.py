import random
from order import Order

class Stock:
  """A simple Stock class"""
  global accounts
  '''TODO: use a parameter: 1/-1 to decide whether sellQueue or buyQueue and
  reuse code (low priority)'''


  def __init__(self, ticker):
    self.price = random.uniform(5,20)
    self.trueValue = random.uniform(0.9,1.1) * self.price
    self.ticker = ticker
    self.buyQueue = []  # Decreasing order on price
    self.sellQueue = [] # Increasing order on price

  
  def updateTrueValue(self):
    randNum = random.uniform(0,1)
    if randNum > 0.5:
      self.trueValue *= random.uniform(1.00, 1.04)
    else:
      self.trueValue /= random.uniform(1.00, 1.04)

  # only for internal use
  def bidask(self):
    # Return diffence between lowest sell and highest buy; -1 if either empty
    if self.buyQueue!=[] and self.sellQueue!=[]:
      buyOrder = self.buyQueue[0]
      sellOrder = self.sellQueue[0]
      buyPrice = buyOrder.price
      sellPrice = sellOrder.price
      return  sellPrice - buyPrice
    else:
      return "error"

  def buy(self, quantity):
    """precondition: sufficient funds available, sufficient quantity available
       for purchase. """
    l = self.sellQueue[:] # copy by value
    for sell_idx in range(len(l)):
      sellOrder = l[sell_idx]
      sellQuantity = sellOrder.quantity
      price = sellOrder.price

      if quantity >= sellQuantity:
        sellNum = sellQuantity
        del self.sellQueue[sell_idx]
      else:
        sellNum = quantity
        self.sellQueue[sell_idx].quantity -= sellNum

      self.price = price
      quantity -= sellNum

      sellerID = sellOrder.client_id
      accounts[sellerID].availableFunds += sellNum*price
      accounts[sellerID].portfolio[ticker] -= sellNum

      if quantity == 0:
        return 1
    return -1

  def sell(self, quantity):
    #assumes buyQueue ordered by price in decreasing order
    #already checking if required quantity is available
    #already checking if funds available
    l = self.buyQueue[:]
    for buy_idx in range(len(l)):
      buyOrder = l[buy_idx]
      buyQuantity = buyOrder.quantity
      price = buyOrder.price

      if quantity > buyQuantity:
        buyNum = buyQuantity
        del self.buyQueue[buy_idx]
      else:
        buyNum = quantity
        self.buyQueue[buy_idx].quantity -= buyNum
      
      self.price = price
      quantity -= buyNum

      buyerID = buyOrder.client_id
      accounts[buyerID].availableFunds -= buyNum*price
      accounts[buyerID].portfolio[ticker] += buyNum
      if quantity == 0:
        return 1
    return -1

  def totalBuyCost(self, quantity):
    """ return cost of purchasing specified quantity (iterates through sell
        queue until desired quantity purchased); -1 if quantity desired more
        than quantity available """
    cost = 0
    for x in self.sellQueue:
      sellQuantity = x.quantity
      price = x.price

      if quantity > sellQuantity:
        sellNum = sellQuantity
      else:
        sellNum = quantity

      cost += sellNum*price
      quantity -= sellNum

      if quantity == 0:
        return cost
    return -1

  def totalSellCost(self, quantity):
    """ return cost of selling specified quantity (iterates through buy
        queue until desired quantity sold); -1 if quantity desired less than
        quantity available """
    cost = 0
    for x in self.buyQueue:
      buyQuantity = x.quantity
      price = x.price

      if quantity > buyQuantity:
        buyNum = buyQuantity
      else:
        buyNum = quantity

      cost += buyNum*price
      quantity -= buyNum

      if quantity  == 0:
        return cost
      return -1

  def checkQueues(self):

    while  self.bidask() != "error"  and self.bidask() <= 0:
      # process a transaction between the first in buy queue and first in
      # sell queue, should be called until returns 0

      buyOrder = self.buyQueue[0]
      sellOrder = self.sellQueue[0]
      buyQuantity = buyOrder.quantity
      buyPrice = buyOrder.price
      sellQuantity = sellOrder.quantity
      buyerID = buyOrder.client_id
      sellerID = sellOrder.client_id
      #transaction conducted at bid/buy price

      if buyQuantity < sellQuantity:
        numTransferred = buyQuantity

        #removes the first buy order
        del self.buyQueue[0]

         #reduces the first sell order
        self.sellQueue[0].quantity -= numTransferred
      else:
        numTransferred = sellQuantity
        del self.sellQueue[0]

        self.buyQueue[0].quantity -= numTransferred

      self.price = buyPrice
      #update buyer account
      accounts[buyerID].availableFunds -= numTransferred*buyPrice
      accounts[buyerID].portfolio[ticker] += numTransferred

       #update seller account
      accounts[sellerID].availableFunds += numTransferred*price
      accounts[sellerID].portfolio[ticker] -= numTransferred


  def sellQueueNum(self):
   total = 0
   for x in self.sellQueue:
     num = x.quantity
     total += num
   return total

  def buyQueueNum(self):
    total = 0
    for x in self.buyQueue:
      num = x.quantity
      total += num
    return total

  def buyAt(self, quantity, price, account_id):
    order = Order(account_id, quantity, price, self.ticker)
    self.buyQueue.append(order)
    self.buyQueue.sort(key = lambda order: order.price, reverse = True)
    self.checkQueue()
    #by price in descending
    #O(n*logn)

  def sellAt(self, quantity, price, acccount_id):
    order = Order(account_id, quantity, price, self.ticker)
    self.sellQueue.append(order)
    self.sellQueue.sort(key = lambda order: order.price)
    self.checkQueue()
    #by price in ascending
    #O(n*logn)
