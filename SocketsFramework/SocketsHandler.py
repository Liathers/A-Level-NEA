from BaseClass import *
from SocketsFramework.SocketClientThread import *
from SocketsFramework.SocketServerThread import *

class SocketHandler(BaseClass):
    def __init__(self):
        super().__init__()
        self.clientSocket = None

    def createSocketSession(self, ip, port):
        self.output("Creating Socket Server")
        SocketServerThread(ip, port)

    def connectToSocketServerSession(self, ip, port, name):
        self.output("Creating Socket Client")
        self.clientSocket = SocketClientThread(ip, port, name)
    