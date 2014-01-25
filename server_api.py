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
    getid;
    id,buy,ticker,shares;
    id,sell,ticker,shares;
    id,price,ticker;
    id,volume,ticker;
    id,portfolio;
    id,funds;
    id,symbols;
"""
