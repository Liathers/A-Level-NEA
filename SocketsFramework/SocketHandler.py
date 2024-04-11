import socket

from BaseClass import *

class SocketHandler(BaseClass):
    def __init__(self):
        super().__init__()
        self.hostSocket = None

    def makeSocketSession(self, port: int):
        self.hostSocket = socket.socket()
        self.output("Created socket")
        self.hostSocket.bind(("", port))
        self.output(f"Bound socket to port {port}")
