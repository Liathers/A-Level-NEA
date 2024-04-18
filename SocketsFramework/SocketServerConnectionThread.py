from threading import Thread

from BaseClass import *
from SocketsFramework.SocketServerListenerThread import *

#This thread is used to allow clients to establish a connection to the server
class SocketServerConnectionThread(BaseClass, Thread):
    def __init__(self, parent):
#Prepare the thread and also get the base functions from BaseClass
        Thread.__init__(self)
        super().__init__()

#Define variables that will be needed throughout the class
        self.parent = parent
        self.daemon = True

#Start the thread
        self.start()

#Execute this function as the thread is running
    def run(self):
#Indefinately attempt to accept incoming connections, notify the user and also append the connection
#to the connections array, so that the server can keep trakc of them
        while True:
            client, address = self.parent.socket.accept()
            self.output(f"Client {address[0]}:{address[1]} established a connection")
            self.parent.connections.append([client, ""])

#Establish a thread so that the server can listen for messages that are incoming from a connected client
            SocketServerListenerThread(self.parent, client)