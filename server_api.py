"""
Port for communication: 19290

Interface:

10 stocks:
    0..9

Stock: symbol, volume, bid-ask price
        
Public functions: (available to client)

getAll() : list of symbols

getStock(string symbol) : returns the stock object



buy(string symbol, int quantity): returns 1/0 (for accept/decline)

sell(string symbol, int quantity): returns 1/0 (for accept/decline)

getFunds()
    returns double money available 
    
    
getPortfolio()
    returns dictionary with keys: stocks
                            values: number of shares

 

"""
"""
Ideas for next version:

Overloaded getStock function:

getStock(string symbol, string data_field) : returns int volume or double  
data_field can be: volume, price    
"""
