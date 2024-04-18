from threading import Thread
from socket import socket, SOL_SOCKET, SO_REUSEADDR

from BaseClass import *
from SocketsFramework.SocketServerConnectionThread import *

#This is the thread that will handle logic related to the socket server
class SocketServerThread(BaseClass, Thread):
    def __init__(self, ip, port):
#Prepare the thread and also get the base functions from BaseClass
        Thread.__init__(self)
        super().__init__()

#Define variables that will be needed throughout the class
        self.socket = None
        self.ip = ip
        self.port = port
        self.connections = []

#Start the thread
        self.start()

#Execute this function as the thread is executing
    def run(self):
#Create the socket that will be used for the server, and bind it to a port
        self.socket = socket()
        self.socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.output("Created socket")

        self.socket.bind((self.ip, self.port))
        self.output(f"Bound socket to port {self.port}")

#Start the listener that will await and process incoming connections to the server
        self.startListener()

#Listen for connections, and also start the thread that will process to connections
    def startListener(self):
        self.socket.listen()
        self.output(f"Socket listening on {self.ip}:{self.port}")
        SocketServerConnectionThread(self)

#Remove a client from the server
    def removeClient(self, client):
#Look through the list of connections, and once the client is found, remove it from the list of connections and then
#close the connection
        pos = 0
        for connection in self.connections:
            if connection[0] == client:
                self.connections.pop(pos)
                connection[0].close()
            else:
                pos += 1

#Assign a name to the client within the list of connections
    def nameClient(self, client, username):
        for connection in self.connections:
            if connection[0] == client:
                connection[1] = username

#Allow the simple broadcase of a message to all clients connected to the server
    def broadcastFromAuthorToClients(self, author, message):
#For each connection within connections, get the socket as well as the username and information
        for connection in self.connections:
            socket = connection[0]
            username = connection[1]
            info = socket.getpeername()
#If the socket is not the same as the author, try to encode and send the message
            if socket != author:
                try:
                    socket.send(message.encode())
#If an error occurs, then notify the user, and also broadcast it to all connected clients, and remove it from the list
#of current connections
                except Exception as error:
                    self.output(f"[{info[0]}:{info[1]}] Failed to connect to remote client, formally disconnecting client")
                    self.removeClient(socket)
                    self.broadcastFromAuthorToClients(None, f"[DISCONNECTED]{username}")
            else:
                continue

#Remove all of the currently connected clients from the server, as well as closing the socket so that
#not further connections can be established
    def removeAllClients(self):
        self.output("Disconnecting all clients..")
#For every client in connections, remove it
        for connection in self.connections:
            self.removeClient(connection[0])

        self.socket.close()
        self.output("Closed socket!")
