#trader v. 0.1
import socket

class traderBot:
    def connectToServer():
        #connects to server, requests account
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.sock.connect((self.host, self.port))
        self.sock.send('create')
        self.accountID = self.sock.recv(1024)
        
    def getSymbols():
        data = sendMessage('symbols')
        return data
        
    def getPrice(symbol):
        data = sendMessage('price,{0}'.format(symbol))
        return data
        
    def getVolume(symbol):
        data = sendMessage('volume,{0}'.format(symbol))
        return data
        
    def buy(symbol, quantity):
        data = sendMessage('buy,{0},{1}'.format(symbol,quantity))
        return data
    
    def sell(symbol, quantity):
        data = sendMessage('sell,{0},{1}'.format(symbol,quantity))
        return data
    
    def getFunds():
        data = sendMessage('funds')
        return data
    
    def getPortfolio():
        data = sendMessage('portfolio')
        return data
    
    def sendMessage(message):
        try:
            # Send data
            print 'sending "%s"' % message
            sock.sendall(accountID + ',' + message + ';')
            #recieve message
            data = sock.recv(1024)
            return data

    
    def __init__(self):
        self.host = 'localhost'
        self.port = 19290
        self.connectToServer()
    

     
    
    
