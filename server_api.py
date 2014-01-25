"""
Port for communication: 19290

Interface:

10 stocks:
    0..9

Stock: symbol, volume, bid-ask price

Public functions: (available to client)

getSymbols() : list of symbols

getPrice(string symbol): return the bid ask price (double)
getVolume(string symbol): return the volume (int)

buy(string symbol, int quantity): returns 1/0 (for accept/decline)
sell(string symbol, int quantity): returns 1/0 (for accept/decline)

getFunds(): return available funds of current client
getPortfolio(): return dictionary (symbol: volume)

Commands
    string buy,int ticker,int shares;
    string sell,int ticker,int shares;
    string info,int ticker;
    string portfolio;
    string account;
    string all;
    string done;
"""
