import socket

from BaseClass import *
from SocketsFramework.SocketClientListenerThread import *

class SocketClient(BaseClass):
    def __init__(self, ip, port, name):
        super().__init__()

        self.socket = None
        self.serverIp = ip
        self.serverPort = port
        self.name = name

        self.establishSocketServerConnection()
        SocketClientListenerThread(self.socket)

    def establishSocketServerConnection(self):
        self.socket = socket.socket()
        self.socket.connect((self.serverIp, self.serverPort))
        self.output(f"Established connection to {self.serverIp}:{self.serverPort}")

    def sendMessage(self, message):
        outboundMessage = f"{self.name}[SEPARATOR]{message}"
        outboundMessageEncoded = outboundMessage.encode()
        self.socket.send(outboundMessageEncoded)
        self.output(f"Sent message \"{message}\" to server")

    def closeSocketServerConnection(self):
        self.socket.close()
        self.output("Closed socket")