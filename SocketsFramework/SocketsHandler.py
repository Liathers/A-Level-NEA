from BaseClass import *
from SocketsFramework.SocketClientThread import *
from SocketsFramework.SocketServerThread import *

#This class will be used for the handling of sockets
class SocketHandler(BaseClass):
    def __init__(self):
#Get base functions from BaseClass
        super().__init__()

#Define variables that will be needed throughout the class
        self.clientSocket = None

#Create a server thread and notify the user
    def createSocketSession(self, ip, port):
        self.output("Creating Socket Server")
        SocketServerThread(ip, port, "caesarcipher", 5)

#Create a client thread and notify the user, whilst allowing interaction with the thread
    def connectToSocketServerSession(self, ip, port, name):
        self.output("Creating Socket Client")
        self.clientSocket = SocketClientThread(ip, port, "caesarcipher", 3, name)
    