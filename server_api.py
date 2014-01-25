"""
Port for communication: 19290

Interface:

10 stocks:
    0..9

Stock: symbol, volume, bid-ask price
        
Public functions: (available to client)

getAll() : list of symbols

getInfo(string symbol) : returns the bid ask price

buy(string symbol, int quantity): returns 1/0 (for accept/decline)

sell(string symbol, int quantity): returns 1/0 (for accept/decline)

getAccount()

getPortfolio()
 
Commands
    string buy,int ticker,int shares;
    string sell,int ticker,int shares;
    string info,int ticker;
    string portfolio;
    string account;
    string all;
    string done;
"""
