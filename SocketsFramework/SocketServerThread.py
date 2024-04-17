from threading import Thread
from socket import socket, SOL_SOCKET, SO_REUSEADDR

from BaseClass import *
from SocketsFramework.SocketServerConnectionThread import *

class SocketServerThread(BaseClass, Thread):
    def __init__(self, ip, port):
        Thread.__init__(self)
        super().__init__()

        self.socket = None
        self.ip = ip
        self.port = port
        self.connections = []

        self.start()

    def run(self):
        self.socket = socket()
        self.socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.output("Created socket")

        self.socket.bind((self.ip, self.port))
        self.output(f"Bound socket to port {self.port}")

        self.startListener()

    def startListener(self):
        self.socket.listen()
        self.output(f"Socket listening on {self.ip}:{self.port}")
        SocketServerConnectionThread(self)

    def removeClient(self, client):
        pos = 0
        for connection in self.connections:
            if connection[0] == client:
                self.connections.pop(pos)
                connection[0].close()
            else:
                pos += 1

    def nameClient(self, client, username):
        for connection in self.connections:
            if connection[0] == client:
                connection[1] = username

    def broadcastFromAuthorToClients(self, author, message):
        for connection in self.connections:
            socket = connection[0]
            username = connection[1]
            info = socket.getpeername()
            if socket != author:
                try:
                    socket.send(message.encode())
                except Exception as error:
                    self.output(f"[{info[0]}:{info[1]}] Failed to connect to remote client, formally disconnecting client")
                    self.removeClient(socket)
                    self.broadcastFromAuthorToClients(None, f"[DISCONNECTED]{username}")
            else:
                continue


    def killCurrentClients(self):
        self.output("Disconnecting all clients..")
        for connection in self.connections:
            self.removeClient(connection[0])

        self.socket.close()
        self.output("Closed socket!")
