"""
Public bot - follows general trend, has enormous amount of money
Should start with large amount of each stock
Places mostly buy/sell orders, few if any bid/ask.

Suggest creating a 'true value' for each stock. Value is assigned randomly at beginning, and is continuously fluctuating. 'True value' affected by earnings and historical data
Then if Stock price is significantly greater than 'true value', sell the stock
Also if stock price is significantly less than 'true value', buy the stock
True value should only be accessible to 'gen public' trader

For each stock, create stock object, store in list
Cycle through list:
Add stock price, true value
if trueValue / stockPrice > 1.05
get available stock
stockToBuy = availableStock * 0.2
marketBuy(stockToBuy / 2)
stockToBuy /= 2
increment = abs(trueValue - stockPrice) / 3
bid(stockToBuy * 0.4 at $(StockPrice - increment))
bid(stockToBuy * 0.3 at $(StockPrice + increment))
bid(stockToBuy * 0.2 at $(StockPrice + 2 * increment))
bid(stockToBuy * 0.1 at $(StockPrice + 3 * increment))

elif trueValue / stockPrice < 0.95
get your stock
stockToSell = yourStock * 0.2
marketSell(stockToSell / 2)
stockToSell /= 2
increment abs(trueValue - stockPrice) / 3
ask(stockToSell * 0.4 at $(StockPrice + increment))
ask(stockToSell * 0.3 at $(StockPrice - increment))
ask(stockToSell * 0.2 at $(StockPrice - 2 * increment))
ask(stockToSell * 0.2 at $(StockPrice - 3 * increment))
"""

"""
Prolonged period of growth - 
Get stock prices and store it in a list
once the list has n entries, check first and last entries
If significant increase, buy stock
Otherwise sell
"""

"""
Randomly buy stock and hold value at which stock was bought
Only sell if stock price increases
"""

"""
MicroTrader

Randomly buy stock
If price decreases at all, sell stock
If price increases by 2 percent, sell stock
"""

"""
Company trader

Follow a single Company
Buy if price goes below a certain amount
sell if price goes above a certain amount
"""
