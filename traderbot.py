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
        data = sendMessage('symbols')
        data = data.split(',')
        print 'Symbols: ' + data
        return data
        
    def getPrice(symbol):
        data = sendMessage('price,{0}'.format(symbol))
        data = float(data)
        print 'Price per Share: $' + data
        return data
        
    def getVolume(symbol):
        data = sendMessage('volume,{0}'.format(symbol))
        data = int(data)
        return data
        
    def buy(symbol, quantity):
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
        data = sendMessage('funds')
        data = float(data)
        print 'Funds: $' + data
        return data
    
    def getPortfolio():
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
    
    def __init__(self):
        self.host = 'localhost'
        self.port = 19290
        self.connectToServer()