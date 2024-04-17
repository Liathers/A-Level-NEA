from threading import Thread

from BaseClass import *

class SocketServerListenerThread(BaseClass, Thread):
    def __init__(self, parent, socket):
        Thread.__init__(self)

        self.parent = parent
        self.socket = socket
        self.info = self.socket.getpeername()
        self.name = None
        self.daemon = True

        self.title = f"{self.__class__.__name__} {self.info[0]}:{self.info[1]}"

        self.start()

    def run(self):
        while True:
            try:
                messageEncoded = self.socket.recv(1024)
                if messageEncoded:
                    message = messageEncoded.decode()
                    if message.startswith("[CLIENTINFO]"):
                        message = message.replace("[CLIENTINFO]", "")
                        if message.endswith("[USERNAME]"):
                            self.name = message.replace("[USERNAME]", "")
                            self.parent.usernames.append(self.name)
                            self.output(f"Client assigned username \"{self.name}\"")
                    elif message.startswith("[MESSAGE]"):
                        message = message.replace("[MESSAGE]", "")
                        message = f"{self.name}: {message}"
                        self.output(f"[Recieved] {message}")
                        for client in self.parent.clients:
                            if client != self.socket:
                                client.send(f"[MESSAGERELAY]{message}".encode())
                            else:
                                continue
                    else:
                        self.output(f"[Unhandled] Recieved uncategorised message {message}")

                else:
                    self.output(f"Client {self.info[0]}:{self.info[1]} disconnected.")
                    self.socket.close()
                    self.parent.removeClient(self.socket)
                    break
            except:
                continue