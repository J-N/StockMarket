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
        #gets a list of all stock symbols
        
        
    def getPrice(symbol):
        #price for a specific ticker
        
    def getVolume(symbol):
        #volume for a specific ticker
        
    def buy(symbol, quantity):
        
    def sell(symbol, quantity):
    
    def getFunds():
    
    def getPortfolio():
    
    def __init__(self):
        self.host = 'localhost'
        self.port = 19290
        self.connectToServer()
    

     
    
    