#trader v. 0.1
import socket

class traderBot:
    def connectToServer():
        #connects to server, requests account
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.sock.connect((self.host, self.port))
        self.sock.send('create')
        self.accountID = self.sock.recv(1024)
        print 'Created Account: ' + self.accountID
        
    def getSymbols():
        #returns an array of all symbols
        data = sendMessage('symbols')
        data = data.split(',')
        print 'Symbols: ' + data
        return data
        
    def getPrice(symbol):
        #gets the price of a specific symbol
        data = sendMessage('price,{0}'.format(symbol))
        data = float(data)
        print 'Price per Share: $' + data
        return data
        
    def getVolume(symbol):
        #gets the available volume of the stock
        data = sendMessage('volume,{0}'.format(symbol))
        data = int(data)
        return data
        
    def buy(symbol, quantity):
        #attempts to buy a certain quantity of stock
        data = sendMessage('buy,{0},{1}'.format(symbol,quantity))
        data = int(data)
        if data == 1:
            data = true
        elif data == 0:
            data = false
        else:
            error(data)
            data = false
        print 'Successful: ' + data
        return data
    
    def sell(symbol, quantity):
        #attempts to sell a given quantity
        data = sendMessage('sell,{0},{1}'.format(symbol,quantity))
        data = int(data)
        if data == 1:
            data = true
        elif data == 0:
            data = false
        else:
            error(data)
            data = false
        print 'Successful: ' + data
        return data
    
    def getFunds():
        #returns the available funds in the account
        data = sendMessage('funds')
        data = float(data)
        print 'Funds: $' + data
        return data
    
    def getPortfolio():
        #returns an array of arrays containing stock and volume
        data = sendMessage('portfolio')
        data = data.split(',')
        for stock in data:
            stock = stock.split(':')
        print 'Stocks:'
        for stock in data:
            print stock
        return data
    
    def sendMessage(message):
        try:
            # Send data
            print 'Sending message.'
            sock.sendall(self.accountID + ',' + message + ';')
            #recieve message
            data = sock.recv(1024)
            print 'Data received.'
            return data

    def error(code):
        #eventually will handle non-zero errors
    
    def __init__(self, accountID):
        #when account id is provided by brain
        self.host = 'localhost'
        self.port = 19290
        self.connectToServer()
        if accountID != 0
            self.accountID = accountID
