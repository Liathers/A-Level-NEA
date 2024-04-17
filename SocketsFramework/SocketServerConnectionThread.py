from threading import Thread

from BaseClass import *
from SocketsFramework.SocketServerListenerThread import *

class SocketServerConnectionThread(BaseClass, Thread):
    def __init__(self, parent):
        Thread.__init__(self)
        super().__init__()

        self.parent = parent
        self.daemon = True

        self.start()

    def run(self):
        while True:
            client, address = self.parent.socket.accept()
            self.output(f"Client {address[0]}:{address[1]} established a connection")
            self.parent.connections.append([client, ""])

            SocketServerListenerThread(self.parent, client)