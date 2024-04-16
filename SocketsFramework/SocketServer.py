import socket
from threading import Thread

from BaseClass import *

class SocketServer(BaseClass, Thread):
    def __init__(self, ip, port):
        super().__init__()

        self.socket = None
        self.ip = ip
        self.port = port
        
        self.clients = []

    def makeSocketSession(self):
        self.socket = socket.socket()
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.output("Created socket")
        self.socket.bind((self.ip, self.port))
        self.output(f"Bound socket to port {self.port}")

    def listenSocketSession(self):
        self.socket.listen()
        self.output(f"Socket listening on {self.ip}:{self.port}")

        thread = Thread(target=self.acceptSocketClientConnection())
        thread.daemon = True
        thread.start()

    def acceptSocketClientConnection(self):
        while True:
            client, address = self.socket.accept()
            self.output(f"Client {address[0]}:{address[1]} established a connection")
            self.clients.append(client)
            
            thread = Thread(target=self.listenForSocketSessionClients, args=(client,))
            thread.daemon = True
            thread.start()

    def listenForSocketSessionClients(self, clientSocket: socket.socket):
        clientInfo = clientSocket.getpeername()
        clientIP = clientInfo[0]
        clientPort = clientInfo[1]
        while True:
            try:
                messageEncoded = clientSocket.recv(1024)
                if messageEncoded:
                    message = messageEncoded.decode()
                    messageFinal = message.replace("[SEPARATOR]", ": ")
                    self.output(f"[Socket Recieved] {messageFinal}")

                    for client in self.clients:
                        if client != clientSocket:
                            client.send(messageEncoded)
                else:
                    self.output(f"[Disconnect] Client {clientIP}:{clientPort} disconnected.")
                    clientSocket.close()
                    self.removeClient(clientSocket)
                    break
            except:
                continue

    def listenForSocketSessionClientsOld(self, clientSocket: socket.socket):
        while True:
            try:
                messageEncoded = clientSocket.recv(1024)
                message = messageEncoded.decode()
            except ConnectionResetError:
                self.output(f"[Disconnect] Client {clientSocket.getsockname()} disconnected")
                clientSocket.close()
                self.removeClient(clientSocket)
                break
            except Exception as error:
                self.output(f"[Error] {error}")
                clientSocket.close()
                self.removeClient(clientSocket)
                break
            else:
                message = message.replace("[SEPARATOR]", ": ")
                self.output(f"[Socket Recieved] {message}")
            
            for client in self.clients:
                client.send(message.encode())

    def removeClient(self, client: socket.socket):
        if client in self.clients:
            self.clients.remove(client)

    def killCurrentClients(self):
        self.output("Disconnecting clients")
        for client in self.clients:
            client.close()

        self.output("Closing socket")
        self.socket.close()