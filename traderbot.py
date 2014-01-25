#trader v. 0.1
import socket
import cPickle as pickle

class TraderBot:
    def connectToServer(self):
        #connects to server, requests account
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.sock.connect((self.host, self.port))

    def createAccount(self):
        #requests a new ID
        self.connectToServer()
        # Send data
        print 'Sending message.'
        self.sock.sendall('create')
        #recieve message
        self.accountID = pickle.loads(self.sock.recv(1024))
        print 'Created Account: ', self.accountID

    def getSymbols(self):
        #returns an array of all symbols
        data = self.sendMessage('symbols')
        print 'Symbols: ', data
        return data
        
    def getPrice(self, symbol):
        #gets the price of a specific symbol
        data = self.sendMessage('price,{0}'.format(symbol))
        data = float(data)
        print 'Price per Share: $', data
        return data
        
    def getVolume(self, symbol):
        #gets the available volume of the stock
        data = self.sendMessage('volume,{0}'.format(symbol))
        data = int(data)
        return data
        
    def buy(self, symbol, quantity):
        #attempts to buy a certain quantity of stock
        data = self.sendMessage('buy,{0},{1}'.format(symbol,quantity))
        data = int(data)
        if data == 1:
            data = True
        elif data == 0:
            data = False
        else:
            error(data)
            data = False
        print 'Successful: ', data
        return data
    
    def sell(self, symbol, quantity):
        #attempts to sell a given quantity
        data = self.sendMessage('sell,{0},{1}'.format(symbol,quantity))
        data = int(data)
        if data == 1:
            data = True
        elif data == 0:
            data = False
        else:
            # error(data) for future error codes
            data = False
        print 'Successful: ', data
        return data

    def bid(self, client_id, quantity, price, symbol):
        #attempts to buy a given quantity
        data = self.sendMessage('bid,{0},{1},{2}'.format(symbol,price,quantity))
        data = int(data)
        if data == 1:
            data = 'Accepted'
        elif data == 0:
            data = 'Pending'
        elif data == -1:
            data = 'Unsuccesful'
        else:
            # error(data) for future error codes
            data = False
        print 'Successful: ', data
        return data

    def ask(self, client_id, quantity, price, symbol):
        #attempts to sell a given quantity
        data = self.sendMessage('ask,{0},{1},{2}'.format(symbol,price,quantity))
        data = int(data)
        if data == 1:
            data = 'Accepted'
        elif data == 0:
            data = 'Pending'
        elif data == -1:
            data = 'Unsuccesful'
        else:
            # error(data) for future error codes
            data = False
        print 'Successful: ', data
        return data

    def getFunds(self):
        #returns the available funds in the account
        data = self.sendMessage('funds')
        data = float(data)
        print 'Funds: $', data
        return data
    
    def getPortfolio(self):
        #returns an array of arrays containing stock and volume
        data = self.sendMessage('portfolio')
        print data
        print 'Portfolio:',data
        return data
    
    def sendMessage(self, message):
        self.connectToServer()
        # Send data
        print 'Sending message.'
        self.sock.sendall(str(self.accountID) + ',' + message)
        #recieve message

        data = self.sock.recv(1024)
        data = pickle.loads(data)
        print data
        print 'Data received.'
        return data

    # def error(code):
        #eventually will handle non-zero errors

    def __init__(self, accountID = 0):
        #when account id is provided by brain
        self.host = 'localhost'
        self.port = 19290
        if accountID != 0:
            self.accountID = accountID
        else:
            self.createAccount()
