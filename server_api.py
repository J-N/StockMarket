"""
Port for communication: 19290

Interface:

{
import json

data sent as string can be converted using:
data_unzipped = json.loads(string data)
The type of the data will be according to return types listed below for each command
}




10 stocks:
    0..9

Stock: symbol, volume, bid-ask price

Public functions: (available to client)

getSymbols() : list of symbols

getPrice(string symbol): return the bid ask price (double)
getVolume(string symbol): return the volume (int)

buy(string symbol, int quantity): returns 1/0 (for accept/decline)
sell(string symbol, int quantity): returns 1/0 (for accept/decline)

createAccount(): return unique id (int) for newly created account
getFunds(): return available funds of current client
getPortfolio(): return dictionary (symbol: volume)

Preface all commands with unique id (received from createAccount())
Commands

for all commands:
returns -1 if invalid syntax
    getid
        returns int id
    
    id,buy,ticker,shares
        returns int 1 if accepted, 0 if declined 
    
    id,sell,ticker,shares
        returns int 1 if accepted, 0 if declined

    id,bid,ticker,price,quantity
        returns int 1 if accepted, 0 pending, -1 if declined

    id,ask,ticker,price,quantity
        returns int 1 if accepted, 0 pending, -1 if declined

    id,price,ticker
        returns int price
    
    id,volume,ticker
        returns int volume
    
    id,portfolio
        returns dict portfolio {symbol : volumeOwned}

    id,orders
        returns orders for account

    id,funds
        returns double availableFunds
        
    id,symbols
        returns list of symbols
    
"""
