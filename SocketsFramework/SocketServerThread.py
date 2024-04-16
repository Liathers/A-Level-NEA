from threading import Thread
import socket

from BaseClass import *
from SocketsFramework.SocketServerConnectionThread import *

class SocketServerThread(BaseClass, Thread):
    def __init__(self, ip, port):
        Thread.__init__(self)
        super().__init__()

        self.socket = None
        self.ip = ip
        self.port = port
        self.clients = []

        self.start()

    def run(self):
        self.socket = socket.socket()
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.output("Created socket")
        self.socket.bind((self.ip, self.port))
        self.output(f"Bound socket to port {self.port}")

        self.startListener()

    def startListener(self):
        self.socket.listen()
        self.output(f"Socket listening on {self.ip}:{self.port}")

        SocketServerConnectionThread(self)

    def removeClient(self, client):
        if client in self.clients:
            self.clients.remove(client)

    def killCurrentClients(self):
        self.output("Disconnecting clients..")
        for client in self.clients:
            client.close()

        self.socket.close()
        self.output("Closed socket!")
