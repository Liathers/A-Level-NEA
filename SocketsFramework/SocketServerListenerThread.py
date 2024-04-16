from threading import Thread

from BaseClass import *

class SocketServerListenerThread(BaseClass, Thread):
    def __init__(self, parent, socket):
        Thread.__init__(self)
        super().__init__()

        self.parent = parent
        self.socket = socket
        self.daemon = True

        self.start()

    def run(self):
        socketInfo = self.socket.getpeername()
        self.title = f"{self.__class__.__name__} {socketInfo[0]}:{socketInfo[1]}"

        while True:
            try:
                messageEncoded = self.socket.recv(1024)
                if messageEncoded:
                    message = messageEncoded.decode()
                    messageFinal = message.replace("[SEPARATOR]", ": ")
                    self.output(f"[Recieved] {messageFinal}")

                    for client in self.parent.clients:
                        clientInfo = client.getpeername()
                        if client != self.socket:
                            client.send(messageEncoded)
                            #self.output(f"[Sent] Relayed message to {clientInfo[0]}:{clientInfo[1]}")
                else:
                    self.output(f"Client {socketInfo[0]}:{socketInfo[1]} disconnected.")
                    self.socket.close()
                    self.parent.removeClient(self.socket)
                    break
            except:
                continue