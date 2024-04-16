import time
from threading import Thread

from BaseClass import *
from SocketsFramework.SocketServer import *
from SocketsFramework.SocketClient import *

class SocketHandler(BaseClass):
    def __init__(self):
        super().__init__()

    def createSocketSession(self, ip, port):
        self.serverSocket = SocketServer(ip, port)
        self.serverSocket.makeSocketSession()
        self.serverSocket.listenSocketSession()
        
        #thread = Thread(target=self.serverSocket.acceptSocketClientConnection())
        #thread.daemon = True
        #thread.start()

        #time.sleep(10)
        #self.serverSocket.killCurrentClients()
        self.output("Function completed.")

    def connectToSocketServerSession(self, ip, port, name):
        self.clientSocket = SocketClient(ip, port, name)
        self.clientSocket.establishSocketServerConnection()
        
        thread = threading.Thread(target=self.clientSocket.listenForSocketServerMessages())
        thread.daemon = True
        thread.start()

        self.output("Gotten past thread creation")
    