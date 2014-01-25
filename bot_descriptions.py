"""
Public bot - follows general trend, has enormous amount of money
Should start with large amount of each stock
Places mostly buy/sell orders, few if any bid/ask.

Suggest creating a 'true value' for each stock. Value is assigned randomly at beginning, and is continuously fluctuating. 'True value' affected by earnings and historical data
Then if Stock price is significantly greater than 'true value', sell the stock
Also if stock price is significantly less than 'true value', buy the stock
True value should only be accessible to 'gen public' trader
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
