import socket
import threading

from BaseClass import *

class SocketClient(BaseClass):
    def __init__(self, ip, port, name):
        super().__init__()

        self.socket = None
        self.serverIp = ip
        self.serverPort = port
        self.name = name

    def establishSocketServerConnection(self):
        self.socket = socket.socket()
        self.socket.connect((self.serverIp, self.serverPort))
        self.output(f"Established connection to {self.serverIp}:{self.serverPort}")

    def listenForSocketServerMessages(self):
        self.output("Listening for socket server messages")
        while True:
            try:
                message = self.socket.recv(1024).decode()
                self.output(f"Message recieved: \"{message}\"")
            except ConnectionError:
                self.output("Connection closed unexpectedly")
                break

    def sendMessage(self, message):
        outboundMessage = f"{self.name}[SEPARATOR]{message}"
        outboundMessageEncoded = outboundMessage.encode()
        self.socket.send(outboundMessageEncoded)
        self.output("Sent message")
        #self.closeSocketServerConnection()

    def closeSocketServerConnection(self):
        self.socket.close()
        self.output("Closed socket")